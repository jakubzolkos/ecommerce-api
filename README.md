# E-Commerce Product API 

## Introduction
Product API for an E-Commerce store leveraging Django Rest Framework and Test Driven Development. The API provides access to product inventory data and allows searching for items based on category or product web ID, as well as performing keyword searches. 

---

## Installation Guide
1. Download the code and open it in your preferred code editor.
2. Create a virtual environment by running the following command:

```
virtualenv venv
```

3. Activate venv

```
source  venv/bin/activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Install Docker Desktop and PostgreSQL. Start a new container.

```
docker-compose up -d
```

6. Load data fixtures into the database. Fixtures with JSON data can be found in the ecommerce/demo folder.

```
python3 manage.py demo-fixtures
```

7. Start Django server

```
python3 manage.py runserver
```

## API Endpoints

- /api/&nbsp;&nbsp;&nbsp;&nbsp;**Root**
- GET &nbsp;/api/inventory/category/all/&nbsp;&nbsp;&nbsp;&nbsp;**Category list**
- GET &nbsp;/api/inventory/products/category/<str:query>/&nbsp;&nbsp;&nbsp;&nbsp;**Search items with a given category**
- GET &nbsp;/api/inventory/<int:query>/&nbsp;&nbsp;&nbsp;&nbsp;**Find items with a given web ID**
- GET &nbsp;/api/search/<str:query>/&nbsp;&nbsp;&nbsp;&nbsp;**Find all products related to query string**
```
