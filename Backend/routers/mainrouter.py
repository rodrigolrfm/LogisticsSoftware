from fastapi import APIRouter


from routers.general import router as generalrouter

router = APIRouter()

router.include_router(generalrouter, prefix="/general")
