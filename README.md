# CRUD API using FastAPI


## Installation Guide:-


Requirements :
 * Fast Api
 * Uvicorn
 * SQL Connector
 * pydantic
 
``` pip install fastapi ```<br>
``` pip install uvicorn[standard] ```


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
CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    tax FLOAT NOT NULL
);
```

Running App : 

``` uvicorn main:app --reload ```
