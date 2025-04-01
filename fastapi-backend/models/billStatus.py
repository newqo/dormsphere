from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .bill import Bill

class BillStatusBase(SQLModel):
    bill_status_description : str = Field(default=None, max_length=255, index=True)

class BillStatus(BillStatusBase, table=True):
    id_bill_status : int = Field(default=None, primary_key=True)
    bill : list["Bill"] = Relationship(back_populates="bill_status")

class BillStatusPublic(BillStatusBase):
    id_bill_status : int

class BillStatusCreate(BillStatusBase):
    bill : list["Bill"] | None

class BillStatusUpdate(SQLModel):
    bill_status_description : str | None = None
    bill : list["Bill"] | None = None