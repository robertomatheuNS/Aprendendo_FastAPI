from datetime import date
from pydantic import BaseModel, Field


class CriarOportunidade(BaseModel):
    titulo: str = Field(min_length=5, max_length=100)
    empresa: str
    descricao: str | None = None
    professor: str
    quantidade_vagas: int = Field(gt=0)
    remoto: bool
    data_inicio: date
    data_fim: date

class AtualizarOportunidade(BaseModel):
    titulo: str  | None = Field(default=None, min_length=5, max_length=100)
    empresa: str | None = None
    descricao: str | None = None
    professor: str | None = None
    quantidade_vagas: int  | None = Field(default=None, gt=0)
    remoto: bool | None = None
    data_inicio: date | None = None
    data_fim: date | None = None