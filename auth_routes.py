from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import sessionmaker
from passlib.hash import bcrypt
from models import Usuario, db

#criar roteador
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
  """
  Rota padrão de Autenticação
  """
  return {"mensagem": "voce acessou a rota de padrão de autenticação", "autenticado":False}


@auth_router.post("/criar_conta")
async def criar_conta(nome: str, email: str, senha: str):
    # Criar sessão
    SessionLocal = sessionmaker(bind=db)
    session = SessionLocal()

    # Verificar se já existe usuário com email
    if session.query(Usuario).filter(Usuario.email == email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    # Criar hash da senha
    senha_hash = bcrypt.hash(senha)

    # Criar usuário
    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha_hash,
        ativo=True,
        admin=False,
    )

    # Salvar no banco
    session.add(novo_usuario)
    session.commit()

    # Atualizar objeto após commit
    session.refresh(novo_usuario)

    return {
        "mensagem": "Conta criada com sucesso",
        "id": novo_usuario.id,
        "nome": novo_usuario.nome,
        "email": novo_usuario.email
    }