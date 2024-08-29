from pydantic import BaseModel
from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from app.model.member import Member

class NewMember(BaseModel):
    userid: str
    passwd: str
    name: str
    email: str
    captcha: str


