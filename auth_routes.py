from fastapi import APIRouter, HTTPException,Depends
from models import Usuario
from security import gerar_hash, verificar_senha, criar_token
from dependencies import pegar_sessao
#criar roteador
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
  """
  Rota padrão de Autenticação
  """
  return {"mensagem": "voce acessou a rota de padrão de autenticação", "autenticado":False}

# criar usuário
@auth_router.post("/criar_conta")
async def criar_conta(nome: str, email: str, senha: str, session= Depends(pegar_sessao)):
    # Session = sessionmaker(bind=db)
    # session = Session()

    # verifica email duplicado
    if session.query(Usuario).filter(Usuario.email == email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    usuario = Usuario(
        nome=nome,
        email=email,
        senha=gerar_hash(senha)
    )

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return {"mensagem": "Usuário criado com sucesso!", "usuario_id": usuario.id}


# login
@auth_router.post("/login")
async def login(email: str, senha: str):
    Session = sessionmaker(bind=db)
    session = Session()

    usuario = session.query(Usuario).filter(Usuario.email == email).first()

    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    if not verificar_senha(senha, usuario.senha):
        raise HTTPException(status_code=400, detail="Senha incorreta")

    token = criar_token({"usuario_id": usuario.id, "email": usuario.email})

    return {"access_token": token, "token_type": "bearer"}