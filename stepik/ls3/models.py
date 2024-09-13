from pydantic import BaseModel


class ProductResponse(BaseModel):
    product_id: int
    name: str
    category: str
    price: float

