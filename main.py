from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import mysql.connector
import jwt
import datetime
from fastapi.responses import JSONResponse
from fastapi import Request

app = FastAPI()

class Account(BaseModel):
    email: str
    password : str

class Product(BaseModel):
    name: str
    description: str
    price: float
    
# connect to mysql server

@app.on_event("startup")
async def startup():
    app.db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="test_db"
    )

#disconnect

@app.on_event("shutdown")
async def shutdown():
    app.db_conn.close()

#register new user

@app.post("/register/")
async def register_Acc(account : Account):
    if str(account.email).strip()=='':
        return{"success": False, "message": "email field cannot be blank"}
    if str(account.password).strip()=='':
        return{"success": False, "message": "password field cannot be blank"}
    cursor = app.db_conn.cursor()
    cursor.execute("INSERT INTO accounts (email, password) VALUES (%s, %s)", 
                   (account.email, account.password))
    app.db_conn.commit()
    return {"success": True, "message": "Registration Successful!"}

@app.post("/login/")
async def login(account : Account):
    cursor = app.db_conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE email = %s  AND password = %s", (account.email,account.password))
    product = cursor.fetchone()
    if product == None:
        return {"success":False , "message":"Email or Password didn't match !"}
    
    payload = {
                "email" : account.email,
                "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                "iat" : datetime.datetime.utcnow()
            }
    token = jwt.encode(payload,'secret',algorithm="HS256")
    response = JSONResponse({"success":True,"message":"Login Successful"})
    response.set_cookie(key='jwt',value=token,httponly=True)
    return response

@app.post("/logout/")
async def logout():
    response=JSONResponse({
                "message" : "Logout Successfull",
                "success" : True
            })
    response.delete_cookie('jwt')
    return response

@app.get("/products/{prod_id}")
async def read_product(prod_id: int):
    cursor = app.db_conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = %s", (prod_id,))
    product = cursor.fetchone()
    if product == None:
        return {"success":False , "message":"Product not found !"}
    return {"product": {"id": product[0], "name": product[1], "description": product[2], "price": product[3]}}

@app.get("/products/")
async def read_product_list():
    cursor = app.db_conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return {"products": [{"id": product[0], "name": product[1], "description": product[2], "price": product[3] } for product in products]}

@app.post("/products/")
async def create_product(product: Product,request:Request):
    token=request.cookies
    if not token:
        return {"success":False , "message":"Unauthorized!"}
    try:
        data=jwt.decode(token['jwt'], "secret", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"success":False , "message":"Unauthorized!"}
    if str(product.name).strip =='':
        return {"success":False , "message":"Product name cannot be empty!"}
    if str(product.description).strip =='':
        return {"success":False , "message":"Product description cannot be empty!"}
    cursor = app.db_conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price) VALUES (%s, %s, %s)", 
                   (product.name, product.description, product.price))
    app.db_conn.commit()
    return {"product": {"product": product.name, "description": product.description, "price": product.price}}

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product,request : Request):
    token=request.cookies
    if not token:
        return {"success":False , "message":"Unauthorized!"}
    try:
        data=jwt.decode(token['jwt'], "secret", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"success":False , "message":"Unauthorized!"}
    cursor = app.db_conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    data = cursor.fetchone()
    if data == None:
        return {"success":False , "message":"Product not found !"}
    cursor.execute("UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s", 
                   (product.name, product.description, product.price, product_id))
    app.db_conn.commit()
    return {"product": {"id": product_id, "name": product.name, "description": product.description, "price": product.price}}

@app.delete("/products/{product_id}")
async def delete_product(product_id: int,request : Request):
    token=request.cookies
    if not token:
        return {"success":False , "message":"Unauthorized!"}
    try:
        data=jwt.decode(token['jwt'], "secret", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"success":False , "message":"Unauthorized!"}
    cursor = app.db_conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    app.db_conn.commit()
    return {"msg": "product deleted"}