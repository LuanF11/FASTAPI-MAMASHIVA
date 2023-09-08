from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.endereco import Endereco
from schemas.endereco import EnderecoOut, EnderecoCreate
from models.usuario import Usuario

def criar_endereco(db: Session, endereco: EnderecoCreate):
    # Verifique se o usuário com o ID especificado existe
    usuario = db.query(Usuario).filter(Usuario.id == endereco.fk_usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Crie um objeto de endereço
    db_endereco = Endereco(**endereco.dict())

    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

def ler_endereco(db: Session, endereco_id: int):
    endereco = db.query(Endereco).filter(Endereco.id == endereco_id).first()
    if endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return endereco

def atualizar_endereco(db: Session, endereco_id: int, endereco: EnderecoCreate):
    # Verifique se o usuário com o ID especificado existe
    usuario = db.query(Usuario).filter(Usuario.id == endereco.fk_usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Verifique se o endereço com o ID especificado existe
    endereco_db = db.query(Endereco).filter(Endereco.id == endereco_id).first()
    if endereco_db is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    # Atualize os dados do endereço
    endereco_db.endereco_rua = endereco.endereco_rua
    endereco_db.endereco_numero = endereco.endereco_numero
    endereco_db.endereco_bairro = endereco.endereco_bairro
    endereco_db.endereco_cidade = endereco.endereco_cidade
    endereco_db.endereco_estado = endereco.endereco_estado
    endereco_db.fk_usuario_id = endereco.fk_usuario_id

    db.commit()
    db.refresh(endereco_db)
    return endereco_db

def deletar_endereco(db: Session, endereco_id: int):
    endereco_db = db.query(Endereco).filter(Endereco.id == endereco_id).first()
    if endereco_db is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    db.delete(endereco_db)
    db.commit()
    return {"message": "Endereço deletado com sucesso"}