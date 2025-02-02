from pydantic import BaseModel
from typing import Optional

class ShopSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]
    logo: Optional[str]

    class Config:
        orm_mode = True

class CreateShopSchema(BaseModel):
    name: str
    description: Optional[str]
    logo: Optional[str]
