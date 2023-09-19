from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator

# TODO: Set Username/Password via .env file
# Live TestBalancePlatform
WEBSERVICE_USERNAME = ""
WEBSERVICE_PASSWORD = ""

# TEST TestBalancePlatformUS credentials
TEST_WEBSERVICE_USERNAME = ""
TEST_WEBSERVICE_PASSWORD = ""

# LIVE URLs
BASE_URL = "https://balanceplatform-api-live.adyen.com/bcl/v2/"
BASE_URL_BTL = "https://balanceplatform-api-live.adyen.com/btl/v2/"

# TEST URLs
TEST_BASE_URL = "https://balanceplatform-api-test.adyen.com/bcl/v2/"
TEST_BASE_URL_BTL = "https://balanceplatform-api-test.adyen.com/btl/v2/"


# models are used for creating schemas for requests
# and validating the request
class OrderRequest(BaseModel):
    id: str
    event_name: str
    start_date: str

    # this is just an example, such a validation can be done on frontend
    @validator("id")
    def start_date_not_too_soon(cls, id):
        # validate that id is long enough. This is just an example of syntax,
        # we'll do more meaningful validations
        assert len(id) > 14

        return id


router = APIRouter()


@router.post("/new_order")
def create_card_order(request: OrderRequest):
    # bulk PI creation
    NR_OF_CARDS = 60
    piRequest = {
        "type": "card",
        "description": "Card Descriptoin",
        "status": "inactive",
        "issuingCountryCode": "NL",
        "balanceAccountId": "BAID",
        "paymentInstrumentGroupId": "PIGID",
        "card": {
            "formFactor": "physical",
            "brand": "mc",
            "brandVariant": "mc_debit_mdt",
            "cardholderName": "Cardholder Name",
            "configuration": {
                "configurationProfileId": "CP123",
                "bulkAddress": {
                    "city": "Amsterdam",
                    "company": "Adyen",
                    "country": "NL",
                    "houseNumberOrName": "49",
                    "postalCode": "1012 KK",
                    "street": "Rokin"
                },
                "shipmentMethod": "nationalDhlBulk",
            },
            "deliveryContact": {
                "address": {
                    "city": "Amsterdam",
                    "country": "NL",
                    "line1": "Rokin 49",
                    "postalCode": "1012 KK",
                },
                "name": {
                    "firstName": "Adyen",
                    "lastName": "Card"
                }
            }
        }
    }

    test_creds = (TEST_WEBSERVICE_USERNAME, TEST_WEBSERVICE_PASSWORD)
    test_url = TEST_BASE_URL + "paymentInstruments"

    live_creds = (WEBSERVICE_USERNAME, WEBSERVICE_PASSWORD)
    live_url = BASE_URL + "paymentInstruments"


    for i in range(0, NR_OF_CARDS):
        time.sleep(0.005)
        piRequest_unique = deepcopy(piRequest_live)
        piRequest_unique["card"]["cardholderName"] = piRequest_live["card"]["cardholderName"] + str(i)

        r = requests.post(live_url, json=piRequest_unique, auth=live_creds)
        print("Response is\n{}".format(r.json()))
        response_dict = json.loads(r.text)

        # Replace printout of row with DB write
        row = [response_dict["id"], response_dict["status"], response_dict["card"]["bin"],
               response_dict["card"]["lastFour"], response_dict["card"]["expiration"]["month"],
               response_dict["card"]["expiration"]["year"], response_dict["card"]["cardholderName"]]
        print(row)
        
    return JSONResponse(
        status_code=201,
        content={"order_id": request.id, "message": "Order created"},
    )
