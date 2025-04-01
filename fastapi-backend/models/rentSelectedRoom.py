from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .contacts import Contacts

class RentSelectedRoom(SQLModel, table=True):
    id_room: int = Field(foreign_key="Rooms.id_room", primary_key=True)
    id_rent: int = Field(foreign_key="Rent.id_rent", primary_key=True)

class RentSelectedRoomContacts(RentSelectedRoom):
    contact: "Contacts" = Relationship(back_populates="room_rent")