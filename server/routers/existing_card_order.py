from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


def order_status(order_id):
    # db lookup for the order status
    return {order_id: "Shipped"}


@router.get("/existingCardOrder/{order_id}")
def get_order_status(order_id: str):
    return JSONResponse(
        status_code=200,
        content=order_status(order_id),
    )
