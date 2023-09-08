from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.reserva import Reserva
from schemas.reserva import ReservaOut, ReservaCreate
from models.usuario import Usuario

def criar_reserva(db: Session, reserva: ReservaCreate):
    # Verifique se o usuário com o ID especificado existe
    usuario = db.query(Usuario).filter(Usuario.id == reserva.fk_usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Crie um objeto de reserva
    db_reserva = Reserva(**reserva.dict())

    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

def ler_reserva(db: Session, reserva_id: str):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return reserva

def atualizar_reserva(db: Session, reserva_id: str, reserva: ReservaCreate):
    # Verifique se o usuário com o ID especificado existe
    usuario = db.query(Usuario).filter(Usuario.id == reserva.fk_usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Verifique se a reserva com o ID especificado existe
    reserva_db = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva_db is None:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    # Atualize os dados da reserva
    reserva_db.reserva_data = reserva.reserva_data
    reserva_db.reserva_horario = reserva.reserva_horario
    reserva_db.fk_usuario_id = reserva.fk_usuario_id

    db.commit()
    db.refresh(reserva_db)
    return reserva_db

def deletar_reserva(db: Session, reserva_id: str):
    reserva_db = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva_db is None:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    db.delete(reserva_db)
    db.commit()
    return {"message": "Reserva deletada com sucesso"}