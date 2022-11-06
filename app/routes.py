from fastapi import APIRouter
from controllers import find

router = APIRouter(
    responses={404: {"description": "Not found"}},
)

router.include_router(find.router)
