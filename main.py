from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from models.usuario import Usuario
from schemas.usuario import UsuarioOut, UsuarioCreate
from controllers.usuario import criar_usuario, ler_usuario, atualizar_usuario, deletar_usuario, autenticar_usuario

from models.endereco import Endereco
from schemas.endereco import EnderecoOut, EnderecoCreate
from controllers.endereco import criar_endereco, ler_endereco, atualizar_endereco, deletar_endereco

from models.reserva import Reserva
from schemas.reserva import ReservaOut, ReservaCreate
from controllers.reserva import criar_reserva, ler_reserva, atualizar_reserva, deletar_reserva

from database.database import engine, get_db

app = FastAPI()

from database.database import Base
Base.metadata.create_all(bind=engine)


# Rota para criar um usuário
@app.post("/usuarios/", response_model=UsuarioOut)
def criar_usuario_endpoint(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)

# Rota para ler informações de um usuário pelo ID
@app.get("/usuarios/{usuario_id}", response_model=UsuarioOut)
def ler_usuario_endpoint(usuario_id: str, db: Session = Depends(get_db)):
    return ler_usuario(db, usuario_id)

# Rota para atualizar um usuário pelo ID
@app.put("/usuarios/{usuario_id}", response_model=UsuarioOut)
def atualizar_usuario_endpoint(usuario_id: str, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return atualizar_usuario(db, usuario_id, usuario)

# Rota para deletar um usuário pelo ID
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario_endpoint(usuario_id: str, db: Session = Depends(get_db)):
    return deletar_usuario(db, usuario_id)

# Rota para autenticar um usuário
@app.post("/usuarios/authenticate/", response_model=UsuarioOut)
def autenticar_usuario_endpoint(email: str, senha: str, db: Session = Depends(get_db)):
    return autenticar_usuario(db, email, senha)

# Rota para criar um endereço
@app.post("/enderecos/", response_model=EnderecoOut)
def criar_endereco_endpoint(endereco: EnderecoCreate, db: Session = Depends(get_db)):
    return criar_endereco(db, endereco)

# Rota para ler informações de um endereço pelo ID
@app.get("/enderecos/{endereco_id}", response_model=EnderecoOut)
def ler_endereco_endpoint(endereco_id: str, db: Session = Depends(get_db)):
    return ler_endereco(db, endereco_id)

# Rota para atualizar um endereço pelo ID
@app.put("/enderecos/{endereco_id}", response_model=EnderecoOut)
def atualizar_endereco_endpoint(endereco_id: str, endereco: EnderecoCreate, db: Session = Depends(get_db)):
    return atualizar_endereco(db, endereco_id, endereco)

# Rota para deletar um endereço pelo ID
@app.delete("/enderecos/{endereco_id}")
def deletar_endereco_endpoint(endereco_id: str, db: Session = Depends(get_db)):
    return deletar_endereco(db, endereco_id)

# Rota para criar uma reserva
@app.post("/reservas/", response_model=ReservaOut)
def criar_reserva_endpoint(reserva: ReservaCreate, db: Session = Depends(get_db)):
    return criar_reserva(db, reserva)

# Rota para ler informações de uma reserva pelo ID
@app.get("/reservas/{reserva_id}", response_model=ReservaOut)
def ler_reserva_endpoint(reserva_id: str, db: Session = Depends(get_db)):
    return ler_reserva(db, reserva_id)

# Rota para atualizar uma reserva pelo ID
@app.put("/reservas/{reserva_id}", response_model=ReservaOut)
def atualizar_reserva_endpoint(reserva_id: str, reserva: ReservaCreate, db: Session = Depends(get_db)):
    return atualizar_reserva(db, reserva_id, reserva)

# Rota para deletar uma reserva pelo ID
@app.delete("/reservas/{reserva_id}")
def deletar_reserva_endpoint(reserva_id: str, db: Session = Depends(get_db)):
    return deletar_reserva(db, reserva_id)