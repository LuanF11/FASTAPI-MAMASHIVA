from pydantic import BaseModel

class UsuarioOut(BaseModel):
    id: str
    usuario_cpf: str
    usuario_nome: str
    usuario_email: str
    usuario_telefone: str

class UsuarioCreate(BaseModel):
    usuario_cpf: str
    usuario_nome: str
    usuario_email: str
    usuario_senha: str
    usuario_telefone: str