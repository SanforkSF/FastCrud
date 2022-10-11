# FAST CRUD for AdventureWorksLT2019 on FastAPI

This repository can create fast CRUD for AdventureWorksLT2019 tables.

You can donwload AdventureWorksLT2019 database here:

https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms


# Configuration and using:

1. Copy this repository
2. Create file '.env' with your credentials (check "dotenv_example" file for example)
```
MSSQL_USER = 'user'
MSSQL_PASSWORD = 'password'
MSSQL_HOST = 'hostname'
MSSQL_DATABASE = 'AdventureWorksLT2019'
```
3. Set virtual environment and then install dependencies:
```
pip install -r requirements.txt
```

4. Start application with command:
```
uvicorn main:app --reload
```
Now you've got access to OpenAPI with CRUD methods.

You can discover it on .../docs#/ address (http://127.0.0.1:8000/docs#/ for example).
