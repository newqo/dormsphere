from sqlmodel import Field, SQLModel, Relationship
from .rooms import Rooms
from .rent import Rent
from .contacts import Contacts

class RentSelectedRoom(SQLModel, table=True):
    id_room: int = Field(foreign_key=Rooms.id_room, primary_key=True)
    id_rent: int = Field(foreign_key=Rent.id_rent, primary_key=True)

class RentSelectedRoomContacts(RentSelectedRoom):
    contact: int = Relationship(back_populates=Contacts.room_rent)