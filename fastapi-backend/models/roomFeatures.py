from sqlmodel import Field, SQLModel

# Composite Entity between RoomTypes and Amenities
class RoomFeatures(SQLModel, table=True):
    id_room_types: int | None = Field(default=None, foreign_key="RoomTypes.id_room_types", primary_key=True)
    id_amenities: int | None = Field(default=None, foreign_key="Amenities.id_amenities", primary_key=True)