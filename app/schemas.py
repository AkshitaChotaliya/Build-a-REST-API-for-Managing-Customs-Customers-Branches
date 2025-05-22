from pydantic import BaseModel
from typing import List, Optional


class BranchBase(BaseModel):
    branch_code: str
    location: str

class BranchCreate(BranchBase):
    customer_id: int

class Branch(BranchBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    name: str
    email: str
    gstin: str

class CustomerCreate(CustomerBase):
    pass
    

class Customer(CustomerBase):
    id: int
    branches: List[Branch] = []

    class Config:
        orm_mode = True
