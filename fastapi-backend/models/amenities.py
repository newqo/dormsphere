from sqlmodel import Field, SQLModel, Relationship
from .amenitiesCategory import AmenitiesCategory
from .roomFeatures import RoomFeatures
from .roomTypes import RoomTypes

class AmentiesBase(SQLModel):
    amenities_description: str | None = Field(default=None,max_length=255,index=True)
    amenities_category: AmenitiesCategory = Relationship(back_populates=AmenitiesCategory.amenities)
    room_features: list[RoomFeatures] | None = Relationship(back_populates=RoomTypes.room_features, link_model=RoomFeatures)

class Amenities(AmentiesBase, table=True):
    id_amenities: int = Field(primary_key=True)

