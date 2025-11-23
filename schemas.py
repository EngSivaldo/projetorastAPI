# schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# -----------------------------
# Schemas base para Usuário
# -----------------------------
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    ativo: Optional[bool] = True
    admin: Optional[bool] = False

    class Config:
        orm_mode = True  # permite converter objetos ORM direto para Pydantic

# -----------------------------
# Schema para criação de usuário
# -----------------------------
class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., min_length=6)  # valida senha com pelo menos 6 caracteres

# -----------------------------
# Schema para retorno de usuário (sem senha)
# -----------------------------
class UsuarioOut(UsuarioBase):
    id: int

# -----------------------------
# Schemas para Autenticação
# -----------------------------
class LoginSchema(BaseModel):
    email: EmailStr
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    usuario_id: int
    email: Optional[EmailStr] = None
