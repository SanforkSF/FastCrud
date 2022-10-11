import datetime

from sqlalchemy import Column, String, Float, Integer, DateTime, Date, ForeignKey

from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, BIT

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
    rowguid = Column(UNIQUEIDENTIFIER)
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
    rowguid = Column(UNIQUEIDENTIFIER)
    ModifiedDate = Column(DateTime)
    ProductModelID = Column(Integer, ForeignKey('SalesLT.ProductModel.ProductModelID'))
    ProductCategoryID = Column(Integer, ForeignKey('SalesLT.ProductCategory.ProductCategoryID'))



class ProductCategory(ProductCategoryCreate):
    ProductCategoryID: int

    class Config:
        orm_mode = True


class ProductCategorySQLModel(Base):
    __tablename__ = 'ProductCategory'
    __table_args__ = {"schema": "SalesLT"}
    ProductCategoryID = Column(Integer, primary_key=True)
    Name = Column(String)
    rowguid = Column(UNIQUEIDENTIFIER)
    ModifiedDate = Column(DateTime)
    products = relationship("ProductSQLModel",
                            primaryjoin="ProductSQLModel.ProductCategoryID==ProductCategorySQLModel.ProductCategoryID")


class Customer(CustomerCreate):
    CustomerID: int

    class Config:
        orm_mode = True


class CustomerSQLModel(Base):
    __tablename__ = 'Customer'
    __table_args__ = {"schema": "SalesLT"}
    CustomerID = Column(Integer, primary_key=True)
    NameStyle = Column(BIT)
    FirstName = Column(String)
    MiddleName = Column(String, nullable=True)
    LastName = Column(String)
    PasswordHash = Column(String)
    PasswordSalt = Column(String)
    rowguid = Column(UNIQUEIDENTIFIER)
    ModifiedDate = Column(DateTime)
