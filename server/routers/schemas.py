from datetime import date
from pydantic import BaseModel
from typing import List, Union


class CardBase(BaseModel):
    payment_instrument_id: str
    cardholder_name: str
    status: str
    order_id: int


class CardCreate(CardBase):
    pass


class Card(CardBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    requesting_user: str
    number_of_cards: int
    approved_usecase_id: int
    event_start_date: date
    event_end_date: date
    card_shipping_address: str
    logo_id: int


class Order(OrderBase):
    id: int
    shipping_status: Union[str, None]
    card_order_id: Union[str, None]

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    pass


class UsecaseBase(BaseModel):
    issuing_country: str
    event_type: str
    # spending_limit: int
    allowed_countries: str
    allowed_mccs: str
    max_daily_spend: int
    max_amount_per_transaction: int
    currency: str
    payment_instrument_group_id: str


class Usecase(UsecaseBase):
    id: int

    class Config:
        orm_mode = True


class UsecaseCreate(UsecaseBase):
    pass


class LogoBase(BaseModel):
    url: str


class LogoCreate(LogoBase):
    pass


class Logo(LogoBase):
    id: int

    class Config:
        orm_mode = True
