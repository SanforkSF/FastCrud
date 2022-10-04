import datetime

from pydantic import BaseModel
from sqlalchemy import Column, String, Float, Integer, DateTime, Date, ForeignKey
from sqlalchemy import create_engine, MetaData, Table, and_, select
import sqlalchemy.orm
from typing import Optional

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class AuthorCreate(BaseModel):
    name: str
    gender: Optional[str]


class Author(AuthorCreate):
    id: int

    class Config:
        orm_mode = True


class AuthorModel(Base):
    __tablename__ = 'mainapp_author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)


class BookCreate(BaseModel):
    title: str
    amount: Optional[int]
    text: Optional[str]
    genre: Optional[str]


class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True


class BookModel(Base):
    __tablename__ = 'mainapp_book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Integer)
    text = Column(String)
    genre = Column(String)


class AuthorBookCreate(BaseModel):
    author_id: int
    book_id: int


class AuthorBook(AuthorBookCreate):
    id: int

    class Config:
        orm_mode = True


class AuthorBookModel(Base):
    __tablename__ = 'mainapp_authorbook'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("mainapp_author.id"))
    book_id = Column(Integer, ForeignKey("mainapp_book.id"))





class CodeCreate(BaseModel):
    first_level: Optional[str]
    second_level: Optional[str]
    third_level: Optional[str]
    fourth_level: Optional[str]
    extra_level: Optional[str]
    category: Optional[str]
    object_name: Optional[str]


class Code(CodeCreate):
    id: int

    class Config:
        orm_mode = True


class CodeModel(Base):
    __tablename__ = 'codes_pg'
    id = Column(Integer, primary_key=True)
    first_level = Column(String)
    second_level = Column(String, nullable=True)
    third_level = Column(String, nullable=True)
    fourth_level = Column(String, nullable=True)
    extra_level = Column(String, nullable=True)
    category = Column(String)
    object_name = Column(String)
#
#
class AdProdCreate(BaseModel):
    Name: Optional[str]
    rowguid: Optional[str]
    ModifiedDate: Optional[datetime.datetime]


class AdProd(AdProdCreate):
    ProductModelID: int

    class Config:
        orm_mode = True


class AdProdModel(Base):
    __tablename__ = 'ProductModel'
    __table_args__ = {"schema": "SalesLT"}
    ProductModelID = Column(Integer, primary_key=True)
    Name = Column(String)
    rowguid = Column(String)
    ModifiedDate = Column(DateTime)

    products = relationship("AdModel",
                            primaryjoin="AdModel.ProductModelID==AdProdModel.ProductModelID")


class AdCreate(BaseModel):
    Name: Optional[str]
    ProductNumber: Optional[str]
    StandardCost: Optional[float]
    SellStartDate: Optional[datetime.datetime]
    ProductModelID: Optional[int]
    rowguid: Optional[str]
    ModifiedDate: Optional[datetime.datetime]
    ProductModelID: Optional[str]


class Ad(AdCreate):
    ProductID: int

    class Config:
        orm_mode = True


class AdModel(Base):
    __tablename__ = 'Product'
    __table_args__ = {"schema": "SalesLT"}
    ProductID = Column(Integer, primary_key=True)
    Name = Column(String)
    ProductNumber = Column(String, nullable=True)
    StandardCost = Column(Float, nullable=True)
    SellStartDate = Column(DateTime)
    rowguid = Column(String, nullable=True)
    ModifiedDate = Column(DateTime)
    ProductModelID = Column(Integer, ForeignKey('SalesLT.ProductModel.ProductModelID'))