from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from routers import existing_card_order, new_card_order, database_test
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(existing_card_order.router)
app.include_router(new_card_order.router)
app.include_router(database_test.router)
