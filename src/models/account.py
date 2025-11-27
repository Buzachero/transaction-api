from database import metadata
from enum import Enum
import sqlalchemy as sa


accounts = sa.Table(
    "account",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_name", sa.String, nullable=False, index=True),
    sa.Column("balance", sa.Numeric(10, 2), nullable=False, default=0),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)


class TransactionType(str, Enum):
  DEPOSIT = "Deposit"
  WITHDRAWAL = "Withdrawal"

transactions = sa.Table(
    "transaction",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id"), nullable=False),
    sa.Column("type", sa.Enum(TransactionType, name="transaction_types"), nullable=False),
    sa.Column("value", sa.Numeric(10, 2), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)