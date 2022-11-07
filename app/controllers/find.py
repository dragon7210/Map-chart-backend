from fastapi import APIRouter
import json

router = APIRouter(
    prefix='/digital',
    tags=['digital'],
    responses={404: {"description": "Not found"}},
)

with open('../data/trial_final.json', 'r') as file:
    data = json.load(file)


@router.get("/")
async def all():
    return data


@router.get("/{key}")
async def find(key: str):
    for item in data:
        if item['tpt_id_key'] == key:
            return item
