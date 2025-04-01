from sqlmodel import Field, SQLModel, Relationship
from .roomFeatures import RoomFeatures, Amenities

class RoomTypesBase(SQLModel):
    room_types_description: str | None = Field(default=None, max_length=255, index=True)
    room_price: float | None = Field(default=None, index=True)

class RoomTypes(RoomTypesBase, table=True):
    id_room_types: int = Field(primary_key=True)
    room_features: list[RoomFeatures] | None = Relationship(back_populates=Amenities.room_features,link_model=RoomFeatures)

class RoomTypesPublic(RoomTypesBase):
    id_room_types: int

class RoomTypesCreate(RoomTypesBase):
    room_features: list[RoomFeatures] | None

class RoomTypesUpdate(RoomTypesBase):
    room_types_description: str | None = None
    room_price: float | None = None
    room_features: list[RoomFeatures] | None = None
