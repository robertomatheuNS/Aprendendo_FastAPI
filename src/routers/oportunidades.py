from schemas.oportunidade import CriarOportunidade
from services import oportunidade_service
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/listar_oportunidades")
def listar_oportunidades():
    return oportunidade_service.listar_oportunidades()

@router.get("/listar_oportunidades/{oportunidade_id}")
def listar_oportunidade_por_id(oportunidade_id: int):
    resultado = oportunidade_service.buscar_oportunidade_por_id(oportunidade_id)

    if resultado == None:
        raise HTTPException(
                    status_code=404,
                    detail="Oportunidade não encontrada"
                )

    return resultado

@router.post("/criar_oportunidade")
def criar_oportunidade(nova_oportunidade: CriarOportunidade):

    resultado = oportunidade_service.criar_oportunidade(nova_oportunidade)

    if "erro" in resultado:
        raise HTTPException(
            status_code=400,
            detail=resultado["erro"]
        )

    return resultado
