from sqlalchemy.orm import sessionmaker
from models import db  # seu engine SQLAlchemy

# Cria o factory de sessão
SessionLocal = sessionmaker(bind=db, autoflush=False, autocommit=False)

def pegar_sessao():
    session = SessionLocal()  # cria uma instância da sessão
    try:
        yield session          # devolve a sessão para uso nas rotas
    finally:
        session.close()        # fecha a sessão corretamente
