from typing import Union, List
from fastapi import APIRouter
from stepik.ls3.models import ProductResponse


router = APIRouter()
sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


@router.get("/product/{product_id}")
def get_product():
    pass


@router.get("/products/search", response_model=List[ProductResponse])
def search_product(keyword: str, category: Union[str, None] = None, limit: Union[int, None] = None):
    return [product for product in sample_products if product.get("name") == keyword \
            and (product.get("category") is None or product.get("category") == category)][:limit + 1]
