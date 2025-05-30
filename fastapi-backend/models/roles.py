from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .users import Users

class RolesBase(SQLModel):
    role_description : str = Field(default=None, max_length=255, index=True)

class Roles(RolesBase, table=True):
    id_roles : int = Field(primary_key=True)
    users : list["Users"] = Relationship(back_populates="role")

class RolesPublic(RolesBase):
    id_roles : int

class RolesCreate(RolesBase):
    pass

class RolesUpdate(SQLModel):
    role_description : str
