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