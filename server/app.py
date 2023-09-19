from fastapi import FastAPI

from routers import existing_card_order, new_card_order, database_test

app = FastAPI()

app.include_router(existing_card_order.router)
app.include_router(new_card_order.router)
app.include_router(database_test.router)
