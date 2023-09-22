from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base


class Order(Base):
    __tablename__ = "card_orders"

    id = Column(Integer, primary_key=True, index=True)
    requesting_user = Column(String, index=True)
    number_of_cards = Column(Integer)
    approved_usecase_id = Column(Integer, ForeignKey("approved_usecases.id"))
    event_start_date = Column(TIMESTAMP)
    event_end_date = Column(TIMESTAMP)
    card_shipping_address = Column(String)
    shipping_status = Column(String)
    logo_id = Column(Integer, ForeignKey("logos.id"))  # todo can we have a logo per order or only per usecase?

    approved_usecase = relationship("Usecase", back_populates="card_orders")
    cards = relationship("Card", back_populates="card_orders")
    logo = relationship("Logo", back_populates="card_orders")


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    payment_instrument_id = Column(String, unique=True, index=True)
    cardholder_name = Column(String)
    status = Column(String)
    order_id = Column(Integer, ForeignKey("card_orders.id"))

    card_orders = relationship("Order", back_populates="cards")


class Usecase(Base):
    __tablename__ = "approved_usecases"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    issuing_country = Column(String, index=True)
    event_type = Column(String, index=True)
    # spending_limit = Column(Integer)
    allowed_countries = Column(String)
    allowed_mccs = Column(String)
    max_daily_spend = Column(Integer)
    max_amount_per_transaction = Column(Integer)
    currency = Column(String)
    payment_instrument_group_id = Column(String)

    card_orders = relationship("Order", back_populates="approved_usecase")


class Logo(Base):
    __tablename__ = "logos"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)

    card_orders = relationship("Order", back_populates="logo")
