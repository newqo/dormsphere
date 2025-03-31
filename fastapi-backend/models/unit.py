from sqlmodel import Field, SQLModel, Relationship
from .bill import Bill

class UnitBase(SQLModel):
    water : int | None = Field(default=None, index=True)
    electricity : int | None = Field(default=None, index=True)
    bill : list[Bill] | None = Relationship(back_populates=Bill.unit)

class Unit(UnitBase, table=True):
    id_unit : int = Field(primary_key=True)