from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Query
from typing import Annotated
from sqlmodel import Field, SQLModel, select
from fastapi import Depends, FastAPI, status
from controllers import account, transaction, auth
from schemas.account import TransactionIn
from views.account import TransactionOut
from database import database, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()
    

app = FastAPI(lifespan=lifespan)  
    

app.include_router(account.router, tags=["account"])
app.include_router(transaction.router, tags=["transaction"])
app.include_router(auth.router, tags=["auth"])