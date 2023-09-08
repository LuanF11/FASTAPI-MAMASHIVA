from pydantic import BaseModel

class ReservaOut(BaseModel):
    id: str
    reserva_data: str
    reserva_horario: str
    fk_usuario_id: str

class ReservaCreate(BaseModel):
    reserva_data: str
    reserva_horario: str
    fk_usuario_id: str