from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Administrador de Productos")

class Product(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Café")
    price: float = Field(..., example=12.5, gt=0)
    quantity: int = Field(..., example=10, ge=0)

class ProductCreate(BaseModel):
    name: str = Field(..., example="Café")
    price: float = Field(..., example=12.5, gt=0)
    quantity: int = Field(..., example=10, ge=0)

products: List[Product] = [
    Product(id=1, name="Café", price=12.5, quantity=10),
    Product(id=2, name="Té", price=8.0, quantity=20),
    Product(id=3, name="Chocolate", price=15.0, quantity=5),
]
next_id = 4

@app.get("/", summary="Bienvenida")
def root():
    return {"message": "Administrador de Productos. Usa /products o /docs para ver la API."}

@app.get("/products", response_model=List[Product])
def list_products():
    return products

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.post("/products", response_model=Product, status_code=201)
def create_product(product_data: ProductCreate):
    global next_id
    product = Product(id=next_id, **product_data.dict())
    next_id += 1
    products.append(product)
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: ProductCreate):
    for index, product in enumerate(products):
        if product.id == product_id:
            updated = Product(id=product_id, **product_data.dict())
            products[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            products.pop(index)
            return
    raise HTTPException(status_code=404, detail="Producto no encontrado")
