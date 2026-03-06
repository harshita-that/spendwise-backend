from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class ExpenseCreate(BaseModel):
    title: str
    amount: float


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    owner_id: int

    class Config:
        from_attributes = True
class UserLogin(BaseModel):
    email: str
    password: str
class ExpenseCreate(BaseModel):
    title: str
    amount: float