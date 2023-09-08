from pydantic import BaseModel

class EnderecoOut(BaseModel):
    id: str
    endereco_rua: str
    endereco_numero: str
    endereco_bairro: str
    endereco_cidade: str
    endereco_estado: str
    fk_usuario_id: str

class EnderecoCreate(BaseModel):
    endereco_rua: str
    endereco_numero: str
    endereco_bairro: str
    endereco_cidade: str
    endereco_estado: str
    fk_usuario_id: str