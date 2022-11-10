from fastapi import APIRouter, Depends
from dependencies.database_deps import get_db_session
from sqlalchemy.orm import Session
from models.data import Data
from models.new import New
from models.base import Base1
from sqlalchemy import and_, or_

router = APIRouter(
    prefix='/digital',
    tags=['digital'],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def All(session: Session = Depends(get_db_session)):
    result = session.query(New).all()
    return result


@router.get("/{name}")
async def Find(name: str, session: Session = Depends(get_db_session)):

    q = session.query(Data, Base1, New.pak)\
        .outerjoin(New, Data.name == New.name)\
        .filter(and_(New.name == name, Base1.name == name)).all()

    return q


@ router.put('/add/')
async def Add(name: str, age: int, tall: float, bigo: str, session: Session = Depends(get_db_session)):
    new_Data = Data()
    new_Data.name = name
    new_Data.age = age
    new_Data.tall = tall
    new_Data.bigo = bigo

    session.add(new_Data)
    session.commit()

    return session.query(Data).all()


@ router.delete('/delete/{name}')
async def Delete(name: str, session: Session = Depends(get_db_session)):
    session.query(Data).filter(Data.name == name).delete()
    session.commit()
    return session.query(Data).all()


@ router.post('/update/{name}')
async def Update(name: str, age: str, tall: str, bigo: str, session: Session = Depends(get_db_session)):
    session.query(Data).filter(Data.name == name).update(
        {"name": name, "age": age, "tall": tall, "bigo": bigo}, synchronize_session="fetch"
    )
    session.commit()
    return session.query(Data).all()
