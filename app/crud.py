from sqlalchemy.orm import Session
from . import models, schemas

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)
    if customer:
        db.delete(customer)
        db.commit()
    return customer


def create_branch(db: Session, branch: schemas.BranchCreate):
    db_branch = models.Branch(**branch.dict())
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch

def get_branches_by_customer(db: Session, customer_id: int):
    return db.query(models.Branch).filter(models.Branch.customer_id == customer_id).all()



