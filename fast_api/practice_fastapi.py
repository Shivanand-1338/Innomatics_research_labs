from fastapi import FastAPI, Query

app = FastAPI() 

products=[
    {'id':1, 'name':'wireless Mouse', 'price':499,'category':'Electronics','in_stock':True},
    {'id':2, 'name':'Notebook','price':99,'category':'stationary','in_stock':True},
    {'id':3, 'name':"Usb HUB",'price':799,'category':'Electronics','in_stock':False},
    {'id':4,'name':'Pen Set','price':49,'category':'stationery','in_stock':True}
]
@app.get("/")
def home():
    return {"message":"Welcome to our app"}


@app.get('/products')
def get_all_products():
    return {'products':  products, 'total':len(products)}
@app.get('/products/filter')
def filter_products(
    category: str = Query(None,description='Electronics or stationery'),
    max_price: int = Query(None,description='Maximum price'),
    in_stock: bool = Query(None,description='True or False')
):
    result=products
    if category:
        result=[product for product in result if product['category']==category]
    if max_price:
        result=[product for product in result if product['price']<=max_price]
    if in_stock is not None:
        result=[product for product in result if product['in_stock']==in_stock]
    return {'products': result, 'total': len(result)}
@app.get('/products/{product_id}')
def get_product(product_id:int):
    for product in products:
        if product['id']==product_id:
            return {'product':product}
    return {'error':'product not found'}





#run the engine
# #uvicorn main:app --reload
# http: methods:- the language of apis
# get: fetch/read Data
# post: create/submit Data
# put : update/replace Data
# delete: delete/remove Data
# status code: 200: success
# 201: created
# 400: bad request
# 404: not found
# 500: internal server error
#Json: Java Script Object Notation

