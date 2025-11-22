from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType

# Conexão com o banco SQLite
db = create_engine("sqlite:///banco.db", echo=True)

Base = declarative_base()


# -------------------------
# TABELA USUÁRIO
# -------------------------
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String, nullable=False)
    senha = Column(String)
    ativo = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)

    pedidos = relationship("Pedido", back_populates="usuario")

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


# -------------------------
# TABELA PEDIDO
# -------------------------
class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = [
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO"),
    # ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    preco_total = Column(Float, default=0.0)

    usuario = relationship("Usuario", back_populates="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido")

    def __init__(self, usuario_id, status="PENDENTE", preco_total=0.0):
        self.usuario_id = usuario_id
        self.status = status
        self.preco_total = preco_total


# -------------------------
# TABELA ITEM DO PEDIDO
# -------------------------
class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer)
    sabor = Column(String)
    tamanho = Column(String)
    preco_unitario = Column(Float)
    total_item = Column(Float)
    
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    pedido = relationship("Pedido", back_populates="itens")

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido_id):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.total_item = quantidade * preco_unitario
        self.pedido_id = pedido_id
