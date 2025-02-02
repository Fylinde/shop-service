from fastapi import FastAPI
from app.routes import shop
from fastapi.middleware.cors import CORSMiddleware
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.error")



app = FastAPI(
    title="Shop Service",
    description="A microservice for managing shops in the AI marketplace.",
    version="1.0.0",
)

# Include shop routes
app.include_router(shop.router, prefix="/api/shop", tags=["Shop Management"])


# Configure CORS
origins = [
    "http://localhost:3000",  # Your frontend application
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def log_routes(app: FastAPI):
    """
    Logs all the routes available in the FastAPI app.
    """
    logger.info("Available routes:")
    for route in app.routes:
        logger.info(f"Path: {route.path}, Name: {route.name}, Methods: {route.methods}")
        
@app.get("/")
def read_root():
    return {"message": "Welcome to the Seller Service!"}
