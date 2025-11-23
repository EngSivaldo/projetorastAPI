# security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "MEU_TOKEN_SUPER_SEGURO_123"  # troque no futuro
ALGORITHM = "HS256"
EXPIRA_EM_MINUTOS = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# cria hash seguro
def gerar_hash(senha: str):
    return pwd_context.hash(senha)


# compara senha digitada com hash guardado
def verificar_senha(senha_digitada: str, senha_hash: str):
    return pwd_context.verify(senha_digitada, senha_hash)


# gera JWT
def criar_token(dados: dict):
    dados_para_token = dados.copy()
    expira = datetime.utcnow() + timedelta(minutes=EXPIRA_EM_MINUTOS)
    dados_para_token.update({"exp": expira})

    return jwt.encode(dados_para_token, SECRET_KEY, algorithm=ALGORITHM)


# valida token
def verificar_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return None
