from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
from .roomFeatures import RoomFeatures
if TYPE_CHECKING:
    from .rooms import Rooms

class RoomTypesBase(SQLModel):
    room_types_description: str = Field(default=None, max_length=255, index=True)
    room_price: float = Field(default=None, index=True)

class RoomTypes(RoomTypesBase, table=True):
    __tablename__ = 'room_types'
    id_room_types: int = Field(primary_key=True)
    room_features_link: list["RoomFeatures"] = Relationship(back_populates="room_amenities_link",link_model=RoomFeatures)
    rooms : list["Rooms"] = Relationship(back_populates="room_types")

class RoomTypesPublic(RoomTypesBase):
    id_room_types: int

class RoomTypesCreate(RoomTypesBase):
    room_features: list["RoomFeatures"] | None

class RoomTypesUpdate(RoomTypesBase):
    room_types_description: str | None = None
    room_price: float | None = None
    room_features: list["RoomFeatures"] | None = None
