from fastapi import Query
from models.account import accounts
from schemas.account import AccountIn
from typing import Annotated
from database import database

class AccountService:
  async def read_all_accounts(self,
                        offset: int = 0,
                        limit: Annotated[int, Query(le=100)] = 100):
    query = accounts.select().limit(limit).offset(offset)
    return await database.fetch_all(query)
  
  
  async def read_account_by_id(self, account_id: int):
    query = accounts.select().where(accounts.c.id == account_id)
    return await database.fetch_one(query)


  async def create_account(self, account: AccountIn):
    insert_command = accounts.insert().values(user_name=account.user_name, balance=account.balance)
    account_id = await database.execute(insert_command)

    query = accounts.select().where(accounts.c.id == account_id)
    return await database.fetch_one(query)
  
  
  async def update_balance_account(self, new_balance: float):
    update_command = accounts.update().values(balance=new_balance)
    return await database.execute(update_command)