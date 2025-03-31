from sqlmodel import Field, SQLModel, Relationship
from .contacts import Contacts

class ContactsDurationBase(SQLModel):
    contacts_duration_descroption: str | None = Field(default=None, max_length=255, index=True)

class ContactsDuration(ContactsDurationBase, table=True):
    contacts : list[Contacts] | None = Relationship(back_populates=Contacts.contacts_duration)
    id_contacts_duration: int = Field(primary_key=True)