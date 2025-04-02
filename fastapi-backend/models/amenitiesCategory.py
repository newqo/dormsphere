from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .amenities import Amenities

class AmenitiesCategoryBase(SQLModel):
    amenities_category_description: str = Field(max_length=255,index=True)

class AmenitiesCategory(AmenitiesCategoryBase, table=True):
    __tablename__ = "amenities_category"
    id_amenities_category: int = Field(primary_key=True)

    amenities : list["Amenities"] = Relationship(back_populates="amenities_category")

class AmenitiesCategoryPublic(AmenitiesCategoryBase):
    id_amenities_category: int

class AmenitiesCategoryCreate(AmenitiesCategoryBase):
    amenities : list["Amenities"] | None

class AmenitiesCategoryUpdate(AmenitiesCategoryBase):
    amenities_category_description: str | None = None
    amenities : list["Amenities"] | None = None
