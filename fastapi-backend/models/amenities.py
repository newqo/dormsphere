from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
from .roomFeatures import RoomFeatures
if TYPE_CHECKING:
    from .amenitiesCategory import AmenitiesCategory

class AmentiesBase(SQLModel):
    amenities_description: str = Field(default=None, max_length=255, index=True)

class Amenities(AmentiesBase, table=True):
    id_amenities: int = Field(primary_key=True)
    amenities_category: "AmenitiesCategory" = Relationship(back_populates="amenities")
    room_amenities: list["RoomFeatures"] = Relationship(back_populates="room_features", link_model=RoomFeatures)

class AmenitiesPublic(AmentiesBase):
    id_amenities: int

class AmenitiesCreate(AmentiesBase):
    room_feartures: list["RoomFeatures"] | None

# class AmenitiesUpdate(AmentiesBase):
#     amenities_description: str | None = None
#     amenities_category: "AmenitiesCategory" | None = None
#     room_amenities: list["RoomFeatures"] | None = None