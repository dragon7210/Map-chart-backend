from fastapi import APIRouter
import json

router = APIRouter(
    prefix='/digital',
    tags=['digital'],
    responses={404: {"description": "Not found"}},
)

with open('../data/trial_final.json', 'r') as file:
    data = json.load(file)

print(data)


@router.get("/")
async def findKey():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{key}")
async def findKey(key: str):
    return [{"username": "Rick"}, {"username": "Morty"}]
