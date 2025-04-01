from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
import datetime
if TYPE_CHECKING:
    from .roles import Roles
    from .bill import Bill

class UsersBase(SQLModel):
    email : str = Field(primary_key=True, max_length=255)
    name: str = Field(default=None, max_length=255, index=True)
    lastname: str = Field(default=None, max_length=255, index=True)
    birthDate : datetime.date = Field(default=None)

class Users(UsersBase, table=True):
    password : str = Field(max_length=255)
    role : "Roles" = Relationship(back_populates="users")
    bills : list["Bill"] = Relationship(back_populates="user")

class UserPublic(UsersBase):
    pass

class UserBills(UsersBase):
    bills : list["Bill"]

class UserCreate(UsersBase):
    email : str
    password : str
    role : "Roles"

class UserUpdate(UsersBase):
    email : str | None = None
    name : str | None = None
    lastname : str | None = None
    birthDate : datetime.date | None = None
    password : str | None = None
    role : "Roles" | None = None