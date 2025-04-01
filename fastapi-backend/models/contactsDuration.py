from sqlmodel import Field, SQLModel, Relationship
from .contacts import Contacts

class ContactsDurationBase(SQLModel):
    contacts_duration_descroption: str = Field(default=None, max_length=255, index=True)

class ContactsDuration(ContactsDurationBase, table=True):
    id_contacts_duration: int = Field(primary_key=True)
    contacts : list[Contacts] = Relationship(back_populates=Contacts.contacts_duration)

class ContactsDurationPublic(ContactsDurationBase):
    id_contacts_duration: int

class ContactsDurationCreate(ContactsDurationBase):
    contacts : list[Contacts] | None

class ContactsDurationUpdate(ContactsDurationBase):
    contacts_duration_descroption : str | None = None
    contacts : list[Contacts] | None = None