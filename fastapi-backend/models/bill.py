from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .billStatus import BillStatus
    from .unit import Unit
    from .users import Users
    from .rent import Rent

class BillBase(SQLModel):
    unit : "Unit" = Relationship(back_populates="bill")

class Bill(BillBase, table=True):
    id_bill : int = Field(primary_key=True)
    bill_status : "BillStatus" = Relationship(back_populates="bill")
    user : "Users" = Relationship(back_populates="bills")
    rent : "Rent" = Relationship(back_populates="bills")

class BillPublic(BillBase):
    id_bill : int
    bill_status : "BillStatus"
    rent : "Rent"

class BillCreate(BillBase):
    bill_status : "BillStatus"
    user : "Users"
    rent : "Rent"

class BillUpdate(SQLModel):
    unit : "Unit" | None = None
    bill_status : "BillStatus" | None = None
    user : "Users" | None = None
    rent : "Rent" | None = None