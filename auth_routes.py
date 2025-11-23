# auth.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Usuario
from security import gerar_hash, verificar_senha, criar_token
from dependencies import pegar_sessao
from schemas import UsuarioCreate, UsuarioOut, LoginSchema, Token

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Rota padrão
@auth_router.get("/")
async def home():
    return {"mensagem": "Você acessou a rota de padrão de autenticação", "autenticado": False}


# Criar usuário usando Pydantic schema
@auth_router.post("/criar_conta", response_model=UsuarioOut)
async def criar_conta(usuario: UsuarioCreate, session: Session = Depends(pegar_sessao)):

    # Verifica email duplicado
    if session.query(Usuario).filter(Usuario.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=gerar_hash(usuario.senha),
        ativo=usuario.ativo,
        admin=usuario.admin
    )

    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)

    return novo_usuario


# Login usando Pydantic schema
@auth_router.post("/login", response_model=Token)
async def login(dados: LoginSchema, session: Session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email == dados.email).first()

    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    if not verificar_senha(dados.senha, usuario.senha):
        raise HTTPException(status_code=400, detail="Senha incorreta")

    token = criar_token({"usuario_id": usuario.id, "email": usuario.email})

    return {"access_token": token, "token_type": "bearer"}
