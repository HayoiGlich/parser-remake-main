from fastapi import APIRouter

router = APIRouter(
    prefix = "/license"
)

@router.get("")
async def get_license():
    ...