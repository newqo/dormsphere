from sqlmodel import Field, SQLModel, Relationship
from .roomStatus import RoomStatus
from .rentSelectedRoom import RentSelectedRoom, Rent

class RoomsBase(SQLModel):
    room_status: RoomStatus = Relationship(back_populates=RoomStatus.rooms)

class Rooms(RoomsBase, table=True):
    id_room: int = Field(primary_key=True)
    rooms_rent : list[RentSelectedRoom] = Relationship(back_populates=Rent.user_rent_room, link_model=RentSelectedRoom)

class RoomsPublic(RoomsBase):
    id_room: int

class RoomsCreate(RoomsBase):
    room_status : RoomStatus

class RoomsUpdate(RoomsBase):
    room_status : RoomStatus | None = None