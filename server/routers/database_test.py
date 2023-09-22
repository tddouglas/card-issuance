from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, schemas, crud

router = APIRouter()

# models.Base.metadata.drop_all(bind=engine)  # Use to refresh schema after changes
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@router.get("/orders/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


@router.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.post("/orders/{order_id}/cards/", response_model=schemas.Card)
def create_card_for_order(
    order_id: int, card: schemas.CardCreate, db: Session = Depends(get_db)
):
    return crud.create_card(db=db, card=card, order_id=order_id)


@router.get("/orders/{order_id}/cards/", response_model=List[schemas.Card])
def read_cards(order_id: int, db: Session = Depends(get_db)):
    db_cards = crud.get_cards_for_order(db, order_id=order_id)
    if db_cards is None:
        raise HTTPException(status_code=404, detail="Cards not found")
    return db_cards


@router.get("/cards/{card_id}", response_model=schemas.Card)
def read_card(card_id: int, db: Session = Depends(get_db)):
    db_card = crud.get_card(db, card_id=card_id)
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return db_card


@router.post("/logos/", response_model=schemas.Logo)
def create_card_for_order(
    logo: schemas.LogoCreate, db: Session = Depends(get_db)
):
    return crud.create_logo(db=db, logo=logo)


@router.get("/logos/{logo_id}", response_model=schemas.Logo)
def read_logo(logo_id: int, db: Session = Depends(get_db)):
    db_logo = crud.get_logo(db, logo_id=logo_id)
    if db_logo is None:
        raise HTTPException(status_code=404, detail="Logo not found")
    return db_logo


@router.get("/logos/", response_model=List[schemas.Logo])
def read_logos(db: Session = Depends(get_db)):
    db_logos = crud.get_logos(db)
    if db_logos is None:
        raise HTTPException(status_code=404, detail="Logos not found")
    return db_logos


@router.post("/usecases/", response_model=schemas.Usecase)
def create_usecase(
    usecase: schemas.UsecaseCreate, db: Session = Depends(get_db)
):
    return crud.create_usecase(db=db, usecase=usecase)


@router.get("/usecases/{usecase_id}", response_model=schemas.Usecase)
def read_usecase(usecase_id: int, db: Session = Depends(get_db)):
    db_usecase= crud.get_usecase(db, usecase_id=usecase_id)
    if db_usecase is None:
        raise HTTPException(status_code=404, detail="Usecase not found")
    return db_usecase


@router.get("/usecases/", response_model=List[schemas.Usecase])
def read_usecases(db: Session = Depends(get_db)):
    db_usecases = crud.get_usecases(db)
    if db_usecases is None:
        raise HTTPException(status_code=404, detail="Usecases not found")
    return db_usecases

