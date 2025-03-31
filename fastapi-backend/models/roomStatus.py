from sqlmodel import Field, SQLModel, Relationship
from .rooms import Rooms

class RoomStatusBase(SQLModel):
    room_status_description: str | None = Field(default=None, max_length=255, index=True)
    rooms: list[Rooms] | None = Relationship(back_populates=Rooms.room_status)

class RoomStatus(RoomStatusBase, table=True):
    id_room_status: int = Field(primary_key=True)