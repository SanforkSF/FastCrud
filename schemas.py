from pydantic import BaseModel
from uuid import UUID
from typing import Optional
import datetime

# Schemas for creation AdventureWorksLT2019 tables

class ProductModelCreate(BaseModel):
    Name: Optional[str]
    rowguid: Optional[UUID]
    ModifiedDate: Optional[datetime.datetime]


class ProductCreate(BaseModel):
    Name: Optional[str]
    ProductNumber: Optional[str]
    StandardCost: Optional[float]
    ListPrice: Optional[float]
    SellStartDate: Optional[datetime.datetime]
    ProductModelID: Optional[int]
    rowguid: Optional[UUID]
    ModifiedDate: Optional[datetime.datetime]
    ProductModelID: Optional[int]

