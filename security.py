# security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import os
from dotenv import load_dotenv

# carrega variáveis do .env
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
EXPIRA_EM_MINUTOS = int(os.getenv("EXPIRA_EM_MINUTOS", 60))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def gerar_hash(senha: str):
    return pwd_context.hash(senha)


def verificar_senha(senha_digitada: str, senha_hash: str):
    return pwd_context.verify(senha_digitada, senha_hash)


def criar_token(dados: dict):
    dados_para_token = dados.copy()
    expira = datetime.utcnow() + timedelta(minutes=EXPIRA_EM_MINUTOS)
    dados_para_token.update({"exp": expira})
    return jwt.encode(dados_para_token, SECRET_KEY, algorithm=ALGORITHM)


def verificar_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return None
