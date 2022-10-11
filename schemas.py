from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional, Annotated
import datetime

# Schemas for creation AdventureWorksLT2019 tables


class ProductModelCreate(BaseModel):
    Name: Optional[str]
    rowguid: Optional[UUID]
    ModifiedDate: Optional[datetime.datetime]


class ProductCreate(BaseModel):
    Name: str
    ProductNumber: Optional[str]
    StandardCost: Optional[float]
    ListPrice: Optional[float]
    SellStartDate: Optional[datetime.datetime]
    ProductModelID: Optional[int]
    ProductCategoryID: Optional[int]
    rowguid: Optional[UUID]
    ModifiedDate: Optional[datetime.datetime]
    ProductModelID: Optional[int]


class ProductCategoryCreate(BaseModel):
    Name: str
    rowguid: Optional[UUID]
    ModifiedDate: Optional[datetime.datetime]


class CustomerCreate(BaseModel):
    NameStyle: int
    FirstName: Annotated[str, Field(max_length=50)]
    MiddleName: Optional[str]
    LastName: Annotated[str, Field(max_length=50)]
    PasswordHash: Annotated[str, Field(max_length=128)]
    PasswordSalt: Annotated[str, Field(max_length=10)]
    rowguid: UUID
    ModifiedDate: datetime.datetime
