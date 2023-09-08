from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from database.database import Base  
import uuid



class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(String(36), primary_key=True, index=True, default=str(uuid.uuid4()))
    reserva_data = Column(String)
    reserva_horario = Column(Enum("7:00", "8:00", "9:00", "10:00", "11:00", "12:00", 
                                  "13:00", "14:00", "15:00", "16:00", "17:00", 
                                  name="horario_enum"))
    fk_usuario_id = Column(String(36), ForeignKey("usuarios.id"))