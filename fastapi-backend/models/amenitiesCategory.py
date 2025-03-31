from sqlmodel import Field, SQLModel, Relationship
from .amenities import Amenities

class AmenitiesCategoryBase(SQLModel):
    amenities_category_description: str | None = Field(default=None,max_length=255,index=True)
    amenities : list[Amenities] | None = Relationship(back_populates=Amenities.amenities_cateory)

class AmenitiesCategory(AmenitiesCategoryBase, table=True):
    id_amenities_category: int = Field(primary_key=True)