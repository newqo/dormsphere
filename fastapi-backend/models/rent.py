from sqlmodel import Field, SQLModel, Relationship
from .users import Users
from .bill import Bill
from .rentSelectedRoom import RentSelectedRoom, Rooms

class RentBase(SQLModel):
    bills : list[Bill] = Relationship(back_populates=Bill.rent)

class Rent(RentBase, table=True):
    id_rent : int = Field(primary_key=True)
    user : Users = Relationship(back_populates=Users.rent)
    user_rent_room : list[RentSelectedRoom] = Relationship(back_populates=Rooms.rooms_rent, link_model=RentSelectedRoom)

class RentPublic(RentBase):
    id_rent : int

class RentCreate(RentBase):
    user : Users

class RentUpdate(RentBase):
    user : Users | None = None
    bills : list[Bill] | None