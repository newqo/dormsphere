from fastapi import APIRouter, HTTPException
from ..database import SessionDep
from ..crud.amenities import *
from ..models.amenities import AmenitiesPublic

router = APIRouter(
    prefix="/amenities",
)

@router.get("/",response_model=list[AmenitiesPublic])
def read_amenities_route(session: SessionDep):
    response = read_amenities(session)
    if not response:
        raise HTTPException(status_code=404, detail="Amenities not found")
    else:
        return response