import sqlalchemy.orm
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy import create_engine, MetaData, Table, and_, select
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter, MemoryCRUDRouter as CRUDRouter
from models import Code, CodeCreate, CodeModel, Base, AdModel, Ad, AdCreate, AdProdModel, AdProd, AdProdCreate


app = FastAPI()

# engine_pg = create_engine('postgresql://postgres:Usero999@poka-db-instance.cypwyvrimquj.eu-west-1.rds.amazonaws.com:5432/poka_db')
engine_mssql = create_engine("mssql+pyodbc://adventure:postgres@FORKUNO-SM:1433/AdventureWorksLT2019?driver=ODBC+Driver+17+for+SQL+Server", use_setinputsizes=True)
engine_pg2 = create_engine('postgresql://postgres:postgres@localhost:5432/booker_db')


# session_pg = sqlalchemy.orm.sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine_pg
# )
#
#
# def get_db_pg():
#     session = session_pg()
#     try:
#         yield session
#         session.commit()
#     finally:
#         session.close()


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


router1 = SQLAlchemyCRUDRouter(
    schema=Ad,
    create_schema=AdCreate,
    db_model=AdModel,
    db=get_db_mssql
)

# router2 = SQLAlchemyCRUDRouter(
#     schema=Code,
#     create_schema=CodeCreate,
#     db_model=CodeModel,
#     db=get_db_pg
# )

router3= SQLAlchemyCRUDRouter(
    schema=AdProd,
    create_schema=AdProdCreate,
    db_model=AdProdModel,
    db=get_db_mssql
)

from models import AuthorCreate, Author, AuthorModel, BookCreate, Book, BookModel, AuthorBook, AuthorBookCreate, AuthorBookModel
session_booker = sqlalchemy.orm.sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_pg2
)



def get_db_booker():
    session = session_booker()
    try:
        yield session
        session.commit()
    finally:
        session.close()


router4= SQLAlchemyCRUDRouter(
    schema=Author,
    create_schema=AuthorCreate,
    db_model=AuthorModel,
    db=get_db_booker
)

router5= SQLAlchemyCRUDRouter(
    schema=Book,
    create_schema=BookCreate,
    db_model=BookModel,
    db=get_db_booker
)

router6= SQLAlchemyCRUDRouter(
    schema=AuthorBook,
    create_schema=AuthorBookCreate,
    db_model=AuthorBookModel,
    db=get_db_booker
)

app.include_router(router4)
app.include_router(router5)
app.include_router(router6)

app.include_router(router1)
# app.include_router(router2)
app.include_router(router3)


# meta = MetaData()

# table = Table(
#     'codes_pg',
#     meta,
#     autoload=True,
#     autoload_with=engine
# )
#
# stmt = select([
#     table.columns.id
# ])
#
# # results = connection.execute(stmt).fetchall()
# #
# # for result in results:
# #     print(result)
#
# session.close()


# {
#     "Name": "Sport-100 Helmet, Blue",
#     "ProductNumber": "HL-U509-B",
#     "StandardCost": 13.0863,
#     "SellStartDate": "2005-07-01T00:00:00",
#     "ProductModelID": "33",
#     "rowguid": "FD7C0858-4179-48C2-865B-ABD5DFC7BC1D",
#     "ModifiedDate": "2008-03-11T10:01:36.827000",
#     "ProductID": 711
# }