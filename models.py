from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

# cria a conexao do banco
db = create_engine("sqlite:///banco.db", echo=True)

# criar a base do banco de dados
Base = declarative_base()


# criar classes/tabelas do banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"     # 

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String, nullable=False)
    senha = Column(String)
    ativo = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


#Pedidos

#Itenpedidos