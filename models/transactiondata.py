from pydantic import BaseModel


class TransactionData(BaseModel):
    status: str
    data: str | bytes
