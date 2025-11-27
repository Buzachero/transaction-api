from pydantic import BaseModel
from enum import Enum


class AccountIn(BaseModel):
  user_name: str
  balance: float | None


class TransactionType(Enum):
  DEPOSIT = "Deposit"
  WITHDRAWAL = "Withdrawal"
  
  
class TransactionIn(BaseModel):  
  account_id: int
  type: TransactionType
  value: float
  
  class Config:
    use_enum_values = True  