from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from .roomFeatures import RoomFeatures
from .amenitiesCategory import AmenitiesCategory

class AmentiesBase(SQLModel):
    amenities_description: str = Field(default=None, max_length=255, index=True)

class Amenities(AmentiesBase, table=True):
    __tablename__ = "amenities"
    id_amenities: int = Field(primary_key=True)
    amenities_category_id: int | None = Field(default=None, foreign_key="amenities_category.id_amenities_category")
    amenities_category: "AmenitiesCategory" = Relationship(back_populates="amenities")
    room_amenities_link: list["RoomFeatures"] = Relationship(back_populates="room_features_link", link_model=RoomFeatures)

class AmenitiesPublic(AmentiesBase):
    id_amenities: int

class AmenitiesCreate(AmentiesBase):
    room_amenities: list["RoomFeatures"] | None

class AmenitiesUpdate(AmentiesBase):
    amenities_description: str | None = None
    amenities_category: Optional["AmenitiesCategory"] | None = None
    room_amenities: Optional[list["RoomFeatures"]] | None = None