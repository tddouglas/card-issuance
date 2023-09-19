from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator


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
    # write an order to DB
    return JSONResponse(
        status_code=201,
        content={"order_id": request.id, "message": "Order created"},
    )
