import sqlalchemy.orm
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy import create_engine, MetaData, Table, and_, select
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel
from fastapi_crudrouter import SQLAlchemyCRUDRouter, MemoryCRUDRouter as CRUDRouter
from models import Code, CodeCreate, CodeModel, Base, AdModel, Ad, AdCreate



# engine_mssql = create_engine("mssql+pyodbc://adventure:postgres@FORKUNO-SM:1433/AdventureWorksLT2019?driver=ODBC+Driver+17+for+SQL+Server")

engine_mssql = create_engine("mssql+pyodbc://adventure:postgres@FORKUNO-SM:1433/AdventureWorksLT2019?driver=SQL Server Native Client 10.0")


if __name__ == '__main__':
    q = f'SELECT * FROM SalesLT.product'
    connection = engine_mssql.connect()
    execution = connection.execute(sqlalchemy.text(q))
    print(execution.fetchall())