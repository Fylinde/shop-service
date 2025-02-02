from sqlalchemy.orm import Session
from app.models.shop import ShopModel
from app.schemas.shop_schema import CreateShopSchema

def get_all_shops(db: Session):
    return db.query(ShopModel).all()

def get_shop_by_id(db: Session, shop_id: int):
    return db.query(ShopModel).filter(ShopModel.id == shop_id).first()

def create_shop(db: Session, shop_data: CreateShopSchema):
    shop = ShopModel(name=shop_data.name, description=shop_data.description, logo=shop_data.logo)
    db.add(shop)
    db.commit()
    db.refresh(shop)
    return shop

def delete_shop(db: Session, shop_id: int):
    shop = db.query(ShopModel).filter(ShopModel.id == shop_id).first()
    if shop:
        db.delete(shop)
        db.commit()
    return shop
