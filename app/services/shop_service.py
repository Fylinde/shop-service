import requests
from sqlalchemy.orm import Session
from app.crud.shop_crud import get_all_shops, get_shop_by_id, create_shop, delete_shop
from app.schemas.shop_schema import CreateShopSchema
from app.config import settings

PRODUCT_SERVICE_URL = settings.PRODUCT_SERVICE_URL

def fetch_all_shops(db: Session):
    return get_all_shops(db)

def fetch_shop_by_id(db: Session, shop_id: int):
    shop = get_shop_by_id(db, shop_id)
    if not shop:
        raise Exception("Shop not found")
    return shop

def create_new_shop(db: Session, shop_data: CreateShopSchema):
    return create_shop(db, shop_data)

def remove_shop(db: Session, shop_id: int):
    shop = delete_shop(db, shop_id)
    if not shop:
        raise Exception("Shop not found")
    return shop

def fetch_products_by_shop(shop_id: int):
    try:
        response = requests.get(f"{PRODUCT_SERVICE_URL}/products?shop_id={shop_id}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error fetching products for shop {shop_id}: {str(e)}")

def add_product_to_shop(shop_id: int, product_data: dict):
    try:
        response = requests.post(f"{PRODUCT_SERVICE_URL}/products", json={"shop_id": shop_id, **product_data})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error adding product to shop {shop_id}: {str(e)}")
