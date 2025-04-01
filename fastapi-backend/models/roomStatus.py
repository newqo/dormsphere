from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .rooms import Rooms

class RoomStatusBase(SQLModel):
    room_status_description: str = Field(default=None, max_length=255, index=True)

class RoomStatus(RoomStatusBase, table=True):
    id_room_status: int = Field(primary_key=True)
    rooms: list["Rooms"] = Relationship(back_populates="room_status")

class RoomStatusPublic(RoomStatusBase):
    id_room_status: int

class RoomStatusCreate(RoomStatusBase):
    rooms: list["Rooms"] | None

class RoomStatusUpdate(RoomStatusBase):
    room_status_description : str | None = None
    rooms : list["Rooms"] | None = None