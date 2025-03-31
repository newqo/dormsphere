from sqlmodel import Field, SQLModel, Relationship
from .contacts import Contacts

class ContactsStatusBase(SQLModel):
    contacts_status_description: str | None = Field(default=None, max_length=255, index=True)

class ContactsStatus(ContactsStatusBase, table=True):
    contacts : list[Contacts] | None = Relationship(back_populates=Contacts.contacts_status)
    id_contacts_status: int = Field(primary_key=True)