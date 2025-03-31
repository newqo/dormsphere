from sqlmodel import Field, SQLModel, Relationship
from .roomFeatures import RoomFeatures
from .amenities import Amenities

class RoomTypesBase(SQLModel):
    room_types_description: str | None = Field(default=None, max_length=255, index=True)
    room_price: float | None = Field(default=None, index=True)
    room_features: list[RoomFeatures] = Relationship(back_populates=Amenities.room_features,link_model=RoomFeatures)

class RoomTypes(RoomTypesBase, table=True):
    id_room_types: int = Field(primary_key=True)
