from fastapi import APIRouter, status, Query
from schemas.account import AccountIn
from views.account import AccountOut
from services.account import AccountService
from typing import Annotated


router = APIRouter(prefix="/accounts")
service = AccountService()


@router.get("/", status_code = status.HTTP_200_OK, response_model = list[AccountOut])
async def read_all_accounts(offset: int = 0,
                            limit: Annotated[int, Query(le=100)] = 100):
  return await service.read_all_accounts(offset, limit)


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = AccountOut)
async def create_account(account: AccountIn):
  return await service.create_account(account)