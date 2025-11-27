from decimal import Decimal
from typing import Annotated
from fastapi import Query
from exceptions import InvalidTransactionError
from models.account import transactions
from database import database
from schemas.account import TransactionIn, TransactionType
from services.account import AccountService


account_service = AccountService()


class TransactionService:
  async def read_all_transactions_by_account(self,
                                             account_id: int,
                                            offset: int = 0,
                                            limit: Annotated[int, Query(le=100)] = 100):
    query = transactions.select().where(transactions.c.account_id == account_id).limit(limit).offset(offset)
    return await database.fetch_all(query)
  
  
  async def create_transaction(self, transaction: TransactionIn):
    if transaction.value <= 0:    
      raise InvalidTransactionError("Transaction value should not be less or equal 0")
    
    account = await account_service.read_account_by_id(transaction.account_id)
  
    new_balance = self.calculate_new_balance(transaction, account.balance)

    insert_tx_command = transactions.insert().values(account_id=transaction.account_id, type=transaction.type, value=transaction.value)
    transaction_id = await database.execute(insert_tx_command)
    await account_service.update_balance_account(new_balance)

    query = transactions.select().where(transactions.c.id == transaction_id)
    return await database.fetch_one(query)
  
  
  def calculate_new_balance(self, 
                            transaction: TransactionIn, 
                            account_balance: Decimal):
    print(f"transaction.type: {transaction.type}")
    if transaction.type == TransactionType.DEPOSIT.value:
      return account_balance + Decimal(transaction.value)
    
    if transaction.value > account_balance:      
      raise InvalidTransactionError("Account does not have enough balance for withdrawal operation")
      
    return account_balance - Decimal(transaction.value)
      
  
  
  