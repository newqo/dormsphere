from sqlmodel import Field, SQLModel

# Composite Entity between RoomTypes and Amenities
class RoomFeatures(SQLModel, table=True):
    __tablename__ = 'room_features'
    room_types_id: int = Field(foreign_key="room_types.id_room_types", primary_key=True)
    amenities_id: int = Field(foreign_key="amenities.id_amenities", primary_key=True)