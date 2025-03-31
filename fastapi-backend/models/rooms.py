from sqlmodel import Field, SQLModel, Relationship
from .roomStatus import RoomStatus

class RoomsBase(SQLModel):
    room_status: RoomStatus = Relationship(back_populates=RoomStatus.rooms)

class Rooms(RoomsBase, table=True):
    id_room: int = Field(primary_key=True)