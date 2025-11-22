from fastapi import APIRouter

#criar roteador
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
  """
  Rota padrão de Autenticação
  """
  return {"mensagem": "voce acessou a rota de padrão de autenticação", "autenticado":False}
