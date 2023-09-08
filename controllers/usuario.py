from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioOut, UsuarioCreate

def criar_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def ler_usuario(db: Session, usuario_id: str):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


def atualizar_usuario(db: Session, usuario_id: str, usuario: UsuarioCreate):
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

def deletar_usuario(db: Session, usuario_id: str):
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario_db)
    db.commit()
    return {"message": "Usuário deletado com sucesso"}

def autenticar_usuario(db: Session, email: str, senha: str):
    usuario = db.query(Usuario).filter(Usuario.email == email, Usuario.senha == senha).first()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Autenticação falhou")
    return usuario