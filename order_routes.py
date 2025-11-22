from fastapi import APIRouter


order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
  """
  Rota padrão de pedidos!!!!!
  """
  return {"mensagem": "voce acessou a rota de pedidos"}
  
  