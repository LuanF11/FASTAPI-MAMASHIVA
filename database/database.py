import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados SQLite
DATABASE_URL = "sqlite:///./teste.db"

# Exclua o arquivo do banco de dados existente (se houver)
if os.path.exists("teste.db"):
    os.remove("teste.db")

# Cria uma instância do SQLAlchemy Base
Base = declarative_base()

# Cria uma conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        # Retorna a sessão do banco de dados
        yield db
    finally:
        # Fecha a sessão do banco de dados
        db.close()
