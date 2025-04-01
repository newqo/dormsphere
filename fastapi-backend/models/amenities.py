from sqlmodel import Field, SQLModel, Relationship
from .amenitiesCategory import AmenitiesCategory
from .roomFeatures import RoomFeatures, RoomTypes

class AmentiesBase(SQLModel):
    amenities_description: str = Field(default=None,max_length=255,index=True)
    amenities_category: AmenitiesCategory = Relationship(back_populates=AmenitiesCategory.amenities)

class Amenities(AmentiesBase, table=True):
    id_amenities: int = Field(primary_key=True)
    room_features: list[RoomFeatures] = Relationship(back_populates=RoomTypes.room_features, link_model=RoomFeatures)

class AmenitiesPublic(AmentiesBase):
    id_amenities: int

class AmenitiesCreate(AmentiesBase):
    room_feartures: list[RoomFeatures] | None

class AmenitiesUpdate(AmentiesBase):
    amenities_description: str | None = None
    amenities_category: AmenitiesCategory | None = None
    room_features: list[RoomFeatures] | None = None
