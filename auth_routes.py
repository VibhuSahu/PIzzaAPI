from fastapi import APIRouter

order_router = APIRouter(
    prefix="/auth",
    tags=["auth"]

)


@order_router.get('/')
async def hello():
    return {"message":"Hello World"}