from typing import Annotated, Optional

from passlib.handlers.postgres import postgres_md5
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from ..models import Todos, Address, Users
from ..database import SessionLocal, engine
from .auth import get_current_user

router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not found"}}
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Address(BaseModel):
    address1: str
    address2: Optional[str]
    city: str
    state: str
    country: str
    postal_code: str


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/", response_model=Address)
def create_address(address: Address,
                   db: Session = Depends(get_db),
                   user: dict = Depends(get_current_user)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    address_model = Address()
    address_model.address1 = address.address1
    address_model.address2 = address.address2
    address_model.city = address.city
    address_model.state = address.state
    address_model.country = address.country
    address_model.postal_code = address.postal_code

    db.add(address_model)
    db.flush()

    user_model = db.query(Users).filter(Users.id == user.get("id")).first()
    user_model.address_id = address_model.id
    db.add(user_model)
    db.commit()

    return address_model
