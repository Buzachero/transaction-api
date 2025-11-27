from sqlmodel import SQLModel
from datetime import datetime
from pydantic import BaseModel


class AccountOut(BaseModel):
  id: int
  user_name: str
  balance: float
  created_at: datetime
  
  
class TransactionOut(BaseModel):  
  account_id: int
  type: str
  value: float