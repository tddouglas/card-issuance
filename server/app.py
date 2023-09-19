from fastapi import FastAPI
from routers import existing_card_order, new_card_order


app = FastAPI()

app.include_router(existing_card_order.router)
app.include_router(new_card_order.router)
