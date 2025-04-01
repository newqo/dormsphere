from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
import datetime
if TYPE_CHECKING:
    from .contactsDuration import ContactsDuration
    from .contactsStatus import ContactsStatus

class ContactsBase(SQLModel):
    contacts_duration : "ContactsDuration" = Relationship(back_populates="contacts")
    contacts_status : "ContactsStatus" = Relationship(back_populates="contacts")

class Contacts(ContactsBase, table=True):
    id_contacts : int = Field(primary_key=True)
    sign_date : datetime.date  = Field(default=None)
    contacts_file_name : str = Field(default=None, max_length=255)
    room_rent = Relationship(back_populates="contact")

class ContactsPublic(ContactsBase):
    id_contacts : int

class ContactsCreate(ContactsBase):
    sign_date : datetime.date
    contacts_file_name : str | None
    contacts_duration : "ContactsDuration"
    contacts_status : "ContactsStatus"

class ContactsUpdate(ContactsBase):
    sign_date : datetime.date | None = None
    contacts_file_name : str | None = None
    contacts_duration : "ContactsDuration" | None = None
    contacts_status : "ContactsStatus" | None = None