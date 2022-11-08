from fastapi import APIRouter, Depends
from dependencies.database_deps import get_db_session
from sqlalchemy.orm import Session
from models.user import User

router = APIRouter(
    prefix='/digital',
    tags=['digital'],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all(session: Session = Depends(get_db_session)):
    data = session.query(User).all()
    return data


@router.get("/{key}")
async def find(key: str):

    return
