from sqlmodel import Field, SQLModel, Relationship
from .billStatus import BillStatus
from .unit import Unit

class BillBase(SQLModel):
    unit : Unit = Relationship(back_populates=Unit.bill)
    bill_status : BillStatus = Relationship(back_populates=BillStatus)

class Bill(BillBase, table=True):
    id_bill : int = Field(primary_key=True)