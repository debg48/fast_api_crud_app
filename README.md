# CRUD API using FastAPI


## Installation Guide:-


### Requirements :
 * git
 * Fast Api
 * uvicorn
 * SQL Connector
 * pyjwt
 
``` pip install fastapi ```<br>
``` pip install uvicorn[standard] ```<br>
``` pip install mysql-connector-python ```<br>
``` pip install pyjwt ```<br>

### Installing the code locally :

``` git clone https://github.com/debg48/fast_api_crud_app.git```

Configuring MYSQL :

* Create and use the Database
``` 
CREATE DATABASE test_db;
```

```
USE test_db;
```

* Create table account

``` 
CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```


* Create table products 

``` 
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL
);
```

### Running App : 

``` uvicorn main:app --reload ```


### Testing Apis :

THe endpoints for testing along with http methods are described below (along with body parameters)

Note : The CRUD apis will require a login of a registered account in the account tables from the database . (Authentication used -> JWT (token is sent using cookies in this app)) Make sure jwt token appears in cookies while login before hitting crud api endpoints .

* #### POST (Register Account) :

Endpoint

```127.0.0.1:8000/register/```

Body raw (json) :

```
{
    "email":"debgandhar4000@gmail.com",
    "password" : "1234"
}
```

* #### POST (Login Account) :

Endpoint

```127.0.0.1:8000/login/```

Body raw (json) :

```
{
    "email":"debgandhar4000@gmail.com",
    "password" : "1234"
}
```
* #### POST (Logout Account) :

Endpoint

```127.0.0.1:8000/logout/```


* #### POST (Create Product) :

Endpoint

 ```127.0.0.1:8000/products/```
 
 Body raw (json) :
 
 ```
 {
    "name": " ",
    "description" : "Nike Shoes",
    "price" : 5999.99
    
}
 ```

* #### GET (Get All Products):

Endpoint

 ```127.0.0.1:8000/products/```
 
 
* #### GET (Get a Particular Products):

Endpoint

 ```127.0.0.1:8000/products/<id>```
 
 <id> corresponds to the id of the product which we want to find 
 
 * #### PUT (Update a Particular Product):
 
 Endpoint

  ```127.0.0.1:8000/products/<id>```
 
 <id> corresponds to the id of the product which we want to find 
  
  Body raw (json) :
  
  ```
  {
    "name" : "Dairy",
    "description" : "Note taking diary , premium quality",
    "price" : 199.00
    }
  ```

 * #### DELETE (Delete a Product):
  
  Endpoint
  
  ```127.0.0.1:8000/products/<id>```
  
  <id> corresponds to the id of the product which we want to find
   
   
  
