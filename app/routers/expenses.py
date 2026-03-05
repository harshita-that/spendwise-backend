from fastapi import APIRouter

router = APIRouter()

@router.get("/expenses")
def get_expenses():
    return {"message": "expenses endpoint"}