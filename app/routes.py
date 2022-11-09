from fastapi import APIRouter
from controllers import dataController

router = APIRouter(
    responses={404: {"description": "Not found"}},
)

router.include_router(dataController.router)
