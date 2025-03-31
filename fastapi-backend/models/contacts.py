from sqlmodel import Field, SQLModel, Relationship
import datetime
from .contactsDuration import ContactsDuration
from .contactsStatus import ContactsStatus

class ContactsBase(SQLModel):
    sign_date : datetime.date | None = Field(default=None)
    contacts_file_name : str | None = Field(default=None, max_length=255)
    contacts_duration : ContactsDuration | None = Relationship(back_populates=ContactsDuration.contacts)
    contacts_status : ContactsStatus | None = Relationship(back_populates=ContactsStatus.contacts)

class Contacts(ContactsBase, table=True):
    id_contacts : int = Field(primary_key=True)