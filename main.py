from fastapi import FastAPI

app = FastAPI()


#importar das roteadores
from auth_routes import auth_router
from order_routes import order_router
#para rodar codigo uvicorn main:app --reload

# incluir as roteadores
app.include_router(auth_router)
app.include_router(order_router)
