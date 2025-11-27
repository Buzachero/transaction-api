from fastapi import APIRouter, HTTPException, Query, status
from schemas.account import TransactionIn
from views.account import TransactionOut
from services.transaction import TransactionService
from typing import Annotated


router = APIRouter(prefix="/transactions")
service = TransactionService()


@router.get("/account/{account_id}", status_code = status.HTTP_200_OK, response_model = list[TransactionOut])
async def read_all_transactions_by_account(account_id: int,                                           
                                            offset: int = 0,
                                            limit: Annotated[int, Query(le=100)] = 100):
  return await service.read_all_transactions_by_account(account_id, offset, limit)


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = TransactionOut)
async def create_transaction(transaction: TransactionIn):
  try:
    return await service.create_transaction(transaction);
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(e))