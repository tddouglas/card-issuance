from sqlalchemy.orm import Session

from . import models
from . import schemas


def get_card(db: Session, card_id: int):
    return db.query(models.Card).filter(models.Card.id == card_id).first()


def get_cards_for_order(db: Session, order_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Card).filter(models.Card.order_id == order_id).offset(skip).limit(limit).all()


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


def get_logo(db: Session, logo_id: int):
    return db.query(models.Logo).filter(models.Logo.id == logo_id).first()


def get_logos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Logo).offset(skip).limit(limit).all()


def get_usecase(db: Session, usecase_id: int):
    return db.query(models.Usecase).filter(models.Usecase.id == usecase_id).first()


def get_usecases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usecase).offset(skip).limit(limit).all()


def create_card(db: Session, card: schemas.CardCreate, order_id: int):
    db_card = models.Card(
        payment_instrument_id=card.payment_instrument_id,
        cardholder_name=card.cardholder_name,
        status=card.status,
        order_id=order_id)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        requesting_user=order.requesting_user,
        number_of_cards=order.number_of_cards,
        approved_usecase_id=order.approved_usecase_id,
        event_start_date=order.event_start_date,
        event_end_date=order.event_end_date,
        card_shipping_address=order.card_shipping_address,
        shipping_status=None,
        logo_id=order.logo_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def create_logo(db: Session, logo: schemas.LogoCreate):
    db_logo = models.Logo(url=logo.url)
    db.add(db_logo)
    db.commit()
    db.refresh(db_logo)
    return db_logo


def create_usecase(db: Session, usecase: schemas.UsecaseCreate):
    db_usecase = models.Usecase(
        issuing_country=usecase.issuing_country,
        event_type=usecase.event_type,
        # spending_limit=usecase.spending_limit,
        allowed_countries=usecase.allowed_countries,
        allowed_mccs=usecase.allowed_mccs,
        max_daily_spend=usecase.max_daily_spend,
        max_amount_per_transaction=usecase.max_amount_per_transaction,
        currency=usecase.currency,
        payment_instrument_group_id=usecase.payment_instrument_group_id)
    db.add(db_usecase)
    db.commit()
    db.refresh(db_usecase)
    return db_usecase
