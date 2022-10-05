from pydantic import BaseModel
from uuid import UUID
from typing import Optional
import datetime


class AuthorCreate(BaseModel):
    name: str
    gender: Optional[str]


class BookCreate(BaseModel):
    title: str
    amount: Optional[int]
    text: Optional[str]
    genre: Optional[str]


class AuthorBookCreate(BaseModel):
    author_id: int
    book_id: int


class CodeCreate(BaseModel):
    first_level: Optional[str]
    second_level: Optional[str]
    third_level: Optional[str]
    fourth_level: Optional[str]
    extra_level: Optional[str]
    category: Optional[str]
    object_name: Optional[str]


class AdProdCreate(BaseModel):
    Name: Optional[str]
    rowguid: Optional[UUID]
    ModifiedDate: Optional[datetime.datetime]


class AdCreate(BaseModel):
    Name: Optional[str]
    ProductNumber: Optional[str]
    StandardCost: Optional[float]
    ListPrice: Optional[float]
    SellStartDate: Optional[datetime.datetime]
    ProductModelID: Optional[int]
    rowguid: Optional[UUID]
    ModifiedDate: Optional[datetime.datetime]
    ProductModelID: Optional[int]

