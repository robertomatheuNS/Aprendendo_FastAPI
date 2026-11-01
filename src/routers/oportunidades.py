from fastapi import APIRouter

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
