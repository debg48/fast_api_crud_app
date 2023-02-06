# CRUD API using FastAPI


## Installation Guide:-


Requirements :
 * Fast Api
 * Uvicorn
 * SQL Connector
 * pydantic
 
``` pip install fastapi ```<br>
``` pip install uvicorn[standard] ```<br>
``` pip install mysql-connector-python ```<br>



Configuring MYSQL :

* Create and use the Database
``` 
CREATE DATABASE test_db;
```

```
USE test_db;
```

*

``` 
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL
);
```

Running App : 

``` uvicorn main:app --reload ```
