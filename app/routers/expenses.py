from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from ..utils import get_current_user

router = APIRouter()


# CREATE EXPENSE
@router.post("/expenses")
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    new_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        owner_id=current_user.id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


# GET ALL EXPENSES
@router.get("/expenses")
def get_expenses(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    expenses = db.query(models.Expense).filter(
        models.Expense.owner_id == current_user.id
    ).all()

    return expenses


# DELETE EXPENSE
@router.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id,
        models.Expense.owner_id == current_user.id
    ).first()

    if not expense:
        raise HTTPException(status_code=404, detail="expense not found")

    db.delete(expense)
    db.commit()

    return {"message": "expense deleted"}