from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .roomStatus import RoomStatus
    from .roomTypes import RoomTypes
    from .rentSelectedRoom import RentSelectedRoom

class RoomsBase(SQLModel):
    room_status: "RoomStatus" = Relationship(back_populates="rooms")
    room_types: "RoomTypes" = Relationship(back_populates="rooms")

class Rooms(RoomsBase, table=True):
    id_room: int = Field(primary_key=True)
    rooms_rent : list["RentSelectedRoom"] = Relationship(back_populates="user_rent_room", link_model=RentSelectedRoom)

class RoomsPublic(RoomsBase):
    id_room: int

class RoomsCreate(RoomsBase):
    room_status : "RoomStatus"

class RoomsUpdate(RoomsBase):
    room_status : "RoomStatus" | None = None