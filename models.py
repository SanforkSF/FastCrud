import datetime

from sqlalchemy import Column, String, Float, Integer, DateTime, Date, ForeignKey

from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

from schemas import *

# CREATING OF SQLAlchemy models for AdventureWorksLT2019 tables

class ProductModel(ProductModelCreate):
    ProductModelID: int

    class Config:
        orm_mode = True


class ProductModelSQLModel(Base):
    __tablename__ = 'ProductModel'
    __table_args__ = {"schema": "SalesLT"}
    ProductModelID = Column(Integer, primary_key=True)
    Name = Column(String)
    rowguid = Column(String)
    ModifiedDate = Column(DateTime)

    products = relationship("ProductSQLModel",
                            primaryjoin="ProductSQLModel.ProductModelID==ProductModelSQLModel.ProductModelID")


class Product(ProductCreate):
    ProductID: int

    class Config:
        orm_mode = True


class ProductSQLModel(Base):
    __tablename__ = 'Product'
    __table_args__ = {"schema": "SalesLT"}
    ProductID = Column(Integer, primary_key=True)
    Name = Column(String)
    ProductNumber = Column(String, nullable=True)
    StandardCost = Column(Float, nullable=True)
    ListPrice = Column(Float, nullable=True)
    SellStartDate = Column(DateTime)
    rowguid = Column(UNIQUEIDENTIFIER, nullable=True)
    ModifiedDate = Column(DateTime)
    ProductModelID = Column(Integer, ForeignKey('SalesLT.ProductModel.ProductModelID'))

