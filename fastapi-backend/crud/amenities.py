from ..database import SessionDep
from sqlmodel import select
from ..models.amenities import Amenities

def read_amenities(session: SessionDep):
    amenities = session.exec(select(Amenities)).all()
    return amenities