from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

# Cria uma instância do FastAPI
app = FastAPI()

# URL de conexão com o banco de dados SQLite
DATABASE_URL = "sqlite:///./teste.db"

# Cria uma conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base declarativa para definir modelos do SQLAlchemy
Base = declarative_base()

# Define a classe de modelo do SQLAlchemy para a tabela "usuarios"
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String, unique=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    telefone = Column(String)

class Endereco(Base):
    __tablename__ = "endereco"

    id = Column(Integer, primary_key=True, index=True)
    endereco_rua = Column(String)
    endereco_numero = Column(String)
    endereco_bairro = Column(String)
    endereco_cidade = Column(String)
    endereco_estado = Column(String)
    fk_usuario_id = Column(Integer, ForeignKey("usuarios.id"))



# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Define o modelo Pydantic para a saída de informações do usuário
class UsuarioOut(BaseModel):
    id: int
    cpf: str
    nome: str
    email: str
    telefone: str

# Define o modelo Pydantic para a entrada de informações ao criar um usuário
class UsuarioCreate(BaseModel):
    cpf: str
    nome: str
    email: str
    senha: str
    telefone: str

# Define o modelo Pydantic para a saída de informações do endereço
class EnderecoOut(BaseModel):
    id: int
    endereco_rua: str
    endereco_numero: str
    endereco_bairro: str
    endereco_cidade: str
    endereco_estado: str
    fk_usuario_id: int

# Define o modelo Pydantic para a entrada de informações ao criar um endereço
class EnderecoCreate(BaseModel):
    endereco_rua: str
    endereco_numero: str
    endereco_bairro: str
    endereco_cidade: str
    endereco_estado: str
    fk_usuario_id: int

# Define a rota POST para criar um endereço
@app.post("/enderecos/", response_model=EnderecoOut)
def criar_endereco(endereco: EnderecoCreate):
    db = SessionLocal()
    # Verifica se o usuário com o ID especificado existe
    usuario = db.query(Usuario).filter(Usuario.id == endereco.fk_usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db_endereco = Endereco(**endereco.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

# Define a rota GET para ler informações de um endereço pelo ID
@app.get("/enderecos/{endereco_id}", response_model=EnderecoOut)
def ler_endereco(endereco_id: int):
    db = SessionLocal()
    endereco = db.query(Endereco).filter(Endereco.id == endereco_id).first()
    if endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return endereco

# Define a rota PUT para atualizar um endereço pelo ID
@app.put("/enderecos/{endereco_id}", response_model=EnderecoOut)
def atualizar_endereco(endereco_id: int, endereco: EnderecoCreate):
    db = SessionLocal()
    # Verifica se o usuário com o ID especificado existe
    usuario = db.query(Usuario).filter(Usuario.id == endereco.fk_usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    endereco_db = db.query(Endereco).filter(Endereco.id == endereco_id).first()
    if endereco_db is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    endereco_db.endereco_rua = endereco.endereco_rua
    endereco_db.endereco_numero = endereco.endereco_numero
    endereco_db.endereco_bairro = endereco.endereco_bairro
    endereco_db.endereco_cidade = endereco.endereco_cidade
    endereco_db.endereco_estado = endereco.endereco_estado
    endereco_db.fk_usuario_id = endereco.fk_usuario_id

    db.commit()
    db.refresh(endereco_db)
    return endereco_db

# Define a rota DELETE para deletar um endereço pelo ID
@app.delete("/enderecos/{endereco_id}")
def deletar_endereco(endereco_id: int):
    db = SessionLocal()
    endereco_db = db.query(Endereco).filter(Endereco.id == endereco_id).first()
    if endereco_db is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    db.delete(endereco_db)
    db.commit()
    return {"message": "Endereço deletado com sucesso"}

# Define a rota POST para criar um usuário
@app.post("/usuarios/", response_model=UsuarioOut)
def criar_usuario(usuario: UsuarioCreate):
    db = SessionLocal()
    db_usuario = Usuario(**usuario.dict())  # Cria um objeto Usuario a partir dos dados do modelo Pydantic
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Define a rota GET para ler informações de um usuário pelo ID
@app.get("/usuarios/{usuario_id}", response_model=UsuarioOut)
def ler_usuario(usuario_id: int):
    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# Define a rota PUT para atualizar um usuário pelo ID
@app.put("/usuarios/{usuario_id}", response_model=UsuarioOut)
def atualizar_usuario(usuario_id: int, usuario: UsuarioCreate):
    db = SessionLocal()
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario_db.cpf = usuario.cpf
    usuario_db.nome = usuario.nome
    usuario_db.email = usuario.email
    usuario_db.senha = usuario.senha
    usuario_db.telefone = usuario.telefone
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

# Define a rota DELETE para deletar um usuário pelo ID
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    db = SessionLocal()
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario_db)
    db.commit()
    return {"message": "Usuário deletado com sucesso"}

# Define a rota POST para autenticar um usuário
@app.post("/usuarios/authenticate/", response_model=UsuarioOut)
def autenticar_usuario(usuario_credenciais: UsuarioCreate):
    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.email == usuario_credenciais.email, Usuario.senha == usuario_credenciais.senha).first()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Autenticação falhou")
    return usuario


