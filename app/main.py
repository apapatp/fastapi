# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List, Optional
from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException

from models import User, Role, Transaction

app = FastAPI()

db: List[User] = [
    User(id=UUID("948ae23e-f0cc-4deb-b212-8426e7d0483a"), roles=[Role.general]),
    User(id=UUID("948ae23e-f0cc-4deb-b212-8426e7d0483a"), roles=[Role.admin]),
    User(id=UUID("948ae23e-f0cc-4deb-b212-8426e7d0483a"), roles=[Role.general])
]

transaction_db: List[Transaction] = [
    Transaction(transaction_id=uuid4()),
    Transaction(transaction_id=uuid4()),
    Transaction(transaction_id=uuid4())
]


def create_transaction():
    return


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.get("/api/v1/transactions")
async def fetch_transactions():
    return transaction_db


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.post("/api/v1/transactions")
async def register_transactions(transaction: Transaction):
    transaction_db.append(transaction)
    return {"id": transaction.transaction_id}


@app.delete("/api/v1/transactions/{transaction_id}")
async def register_transactions(transaction_id: UUID):
    for transaction in transaction_db:
        if transaction_id == transaction.transaction_id:
            transaction_db.remove(transaction)
            return {"success": "ok"}

    raise HTTPException(
        status_code=404,
        detail=f"transaction with transaction id of {transaction_id} does not exist"
    )
