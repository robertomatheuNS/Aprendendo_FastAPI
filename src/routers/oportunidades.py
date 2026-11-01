from schemas.oportunidade import CriarOportunidade
from services import oportunidade_service
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/oportunidade1")
def listar_oportunidade1():
    return "Estágio em Desenvolvimento"

@router.get("/oportunidade2")
def listar_oportunidade2():
    return "Bolsa de Iniciação Científica"

@router.get("/oportunidade3")
def listar_oportunidade3():
    return "Programa Jovem Aprendiz"

@router.post("/oportunidades")
def criar_oportunidade(nova_oportunidade: CriarOportunidade):

    resultado = oportunidade_service.criar_oportunidades(nova_oportunidade)

    if "erro" in resultado:
        raise HTTPException(
            status_code=400,
            detail=resultado["erro"]
        )

    return resultado
