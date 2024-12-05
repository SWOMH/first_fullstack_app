from fastapi import APIRouter

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.get("/registration/")
def registration():
    return {"mesage": "Нахуй тебе тут регаться, свинота?"}