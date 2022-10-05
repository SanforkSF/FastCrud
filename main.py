import sqlalchemy.orm
import os
from sqlalchemy import create_engine, MetaData, Table, and_, select
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter, MemoryCRUDRouter as CRUDRouter
from models import ProductSQLModel, Product, ProductModelSQLModel, ProductModel
from schemas import *

# CREATING FastAPI application and connection to database

app = FastAPI()

# CREDENTIALS (create .env file before this step)

mssql_user = os.getenv('MSSQL_USER')
mssql_password = os.getenv('MSSQL_PASSWORD')
mssql_host = os.getenv('MSSQL_HOST')
mssql_database = os.getenv('MSSQL_DATABASE')


engine_mssql = create_engine(f"mssql+pyodbc://{mssql_user}:{mssql_password}@{mssql_host}:1433/"
                             f"{mssql_database}?driver=ODBC+Driver+17+for+SQL+Server", use_setinputsizes=True)

# SESSION SETTINGS

session_mssql = sqlalchemy.orm.sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_mssql
)


def get_db_mssql():
    session = session_mssql()
    try:
        yield session
        session.commit()
    finally:
        session.close()

# CREATING AND CONFIGURATION of routers for CRUD

router_product = SQLAlchemyCRUDRouter(
    schema=Product,
    create_schema=ProductCreate,
    db_model=ProductSQLModel,
    db=get_db_mssql
)

router_productmodel= SQLAlchemyCRUDRouter(
    schema=ProductModel,
    create_schema=ProductModelCreate,
    db_model=ProductModelSQLModel,
    db=get_db_mssql
)

app.include_router(router_product)
app.include_router(router_productmodel)
