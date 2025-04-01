from sqlmodel import Field, SQLModel, Relationship
from .amenities import Amenities

class AmenitiesCategoryBase(SQLModel):
    amenities_category_description: str = Field(default=None,max_length=255,index=True)

class AmenitiesCategory(AmenitiesCategoryBase, table=True):
    id_amenities_category: int = Field(primary_key=True)
    amenities : list[Amenities] = Relationship(back_populates=Amenities.amenities_cateory)

class AmenitiesCategoryPublic(AmenitiesCategoryBase):
    id_amenities_category: int

class AmenitiesCategoryCreate(AmenitiesCategoryBase):
    amenities : list[Amenities] | None

class AmenitiesCategoryUpdate(AmenitiesCategoryBase):
    amenities_category_description: str | None = None
    amenities : list[Amenities] | None = None