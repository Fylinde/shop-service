from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.shop_service import (
    fetch_all_shops,
    fetch_shop_by_id,
    create_new_shop,
    remove_shop,
    fetch_products_by_shop,
    add_product_to_shop,
)
from app.schemas.shop_schema import CreateShopSchema, ShopSchema
from app.database import get_db

router = APIRouter()

@router.get("/all", response_model=list[ShopSchema])
def get_shops(db: Session = Depends(get_db)):
    return fetch_all_shops(db)

@router.get("/{shop_id}", response_model=ShopSchema)
def get_shop(shop_id: int, db: Session = Depends(get_db)):
    shop = fetch_shop_by_id(db, shop_id)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    return shop

@router.post("/create", response_model=ShopSchema)
def create_shop(shop_data: CreateShopSchema, db: Session = Depends(get_db)):
    return create_new_shop(db, shop_data)

@router.delete("/delete/{shop_id}")
def delete_shop(shop_id: int, db: Session = Depends(get_db)):
    shop = remove_shop(db, shop_id)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    return {"message": "Shop deleted successfully"}

@router.get("/{shop_id}/products")
def get_products_by_shop(shop_id: int):
    try:
        return fetch_products_by_shop(shop_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{shop_id}/product/add")
def add_product(shop_id: int, product_data: dict):
    try:
        return add_product_to_shop(shop_id, product_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
