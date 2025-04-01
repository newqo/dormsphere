from sqlmodel import Field, SQLModel, Relationship
from .bill import Bill

class UnitBase(SQLModel):
    water : int = Field(default=None, index=True)
    electricity : int = Field(default=None, index=True)

class Unit(UnitBase, table=True):
    id_unit : int = Field(primary_key=True)
    bill : list[Bill] = Relationship(back_populates=Bill.unit)

class UnitPublic(UnitBase):
    id_unit : int

class UnitCreate(UnitBase):
    pass

class UnitUpdate(UnitBase):
    water : int | None = None
    electricity : int | None = None