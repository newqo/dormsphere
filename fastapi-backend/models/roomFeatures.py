from sqlmodel import Field, SQLModel, Relationship
from .amenities import Amenities
from .roomTypes import RoomTypes

# Composite Entity between RoomTypes and Amenities
class RoomFeatures(SQLModel, table=True):
    id_room_types: int = Field(foreign_key=RoomTypes.id_room_types, primary_key=True)
    id_amenities: int = Field(foreign_key=Amenities.id_amenities, primary_key=True)