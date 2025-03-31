from sqlmodel import Field, SQLModel, Relationship
from .bill import Bill

class BillStatusBase(SQLModel):
    bill_status_description : str | None = Field(default=None, max_length=255, index=True)
    bill : list[Bill] | None = Relationship(back_populates=Bill.bill_status)

class BillStatus(BillStatusBase, table=True):
    id_bill_status : int = Field(default=None, primary_key=True)