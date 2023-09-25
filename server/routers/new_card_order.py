import json
import os
import requests
import time

from copy import deepcopy
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator

from server.adyen_requests.paymentInstruments import get_payment_instruments_request
from server.routers import schemas
from server.routers.database_test import create_order, create_card_for_order
from server.routers.schemas import CardCreate

# LIVE URLs
BASE_URL = "https://balanceplatform-api-live.adyen.com/bcl/v2/"
BASE_URL_BTL = "https://balanceplatform-api-live.adyen.com/btl/v2/"

# TEST URLs
TEST_BASE_URL = "https://balanceplatform-api-test.adyen.com/bcl/v2/"
TEST_BASE_URL_BTL = "https://balanceplatform-api-test.adyen.com/btl/v2/"

router = APIRouter()


# Endpoint to bulk create card orders
@router.post("/new_order")
def create_card_order(order: schemas.OrderCreate):
    if os.getenv('TEST_MODE') == "True":
        credentials = os.getenv('TEST_WEBSERVICE_USERNAME'), os.getenv('TEST_WEBSERVICE_PASSWORD')
        url = TEST_BASE_URL + "paymentInstruments"
        pi_request = get_payment_instruments_request(True, order.approved_usecase_id)
    else:
        credentials = (os.getenv('WEBSERVICE_USERNAME'), os.getenv('WEBSERVICE_PASSWORD'))
        url = BASE_URL + "paymentInstruments"
        pi_request = get_payment_instruments_request(False, order.approved_usecase_id)

    pi_results = []
    for i in range(0, order.number_of_cards):
        time.sleep(0.005)
        pi_request_unique = deepcopy(pi_request)
        pi_request_unique["card"]["cardholderName"] = pi_request["card"]["cardholderName"] + str(i)

        r = requests.post(url, json=pi_request_unique, auth=credentials)
        print("Response is\n{}".format(r.json()))

        if r.ok:
            response_dict = json.loads(r.text)
            # Replace printout of row with DB write
            row = [response_dict["id"], response_dict["status"], response_dict["card"]["bin"],
                   response_dict["card"]["lastFour"], response_dict["card"]["expiration"]["month"],
                   response_dict["card"]["expiration"]["year"], response_dict["card"]["cardholderName"]]
            print(row)
            pi_results.append(row)

    if len(pi_results) > 0:
        create_order_res = create_order(order)
        for row in pi_results:
            # Construct Card object for db write
            #  CardCreate(payment_instrument_id: str, cardholder_name: str, status: str, order_id: int)
            card = CardCreate(payment_instrument_id=row[0], cardholder_name=row[6], status=row[1],
                              order_id=create_order_res.id)
            create_card_for_order(create_order_res.id, card)

            return JSONResponse(
                status_code=201,
                content={"order_id": create_order_res.id, "message": "Order created"},
            )

    return JSONResponse(
        status_code=500,
        content={"message": "Create Order Failed"},
    )
