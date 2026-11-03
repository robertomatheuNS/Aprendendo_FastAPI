from schemas import oportunidade
from repositories import oportunidade_repository

def validar_periodo_oportunidade(data_inicio, data_fim):

    if data_fim <= data_inicio:
        return False

    return True

def criar_oportunidade(nova_oportunidade: oportunidade.CriarOportunidade):

    dados = nova_oportunidade.model_dump()

    datas_validas = validar_periodo_oportunidade(dados["data_inicio"], dados["data_fim"])

    if not datas_validas:
        return {
            "erro": "Datas estão inválidas"
        }

    return oportunidade_repository.salvar_oportunidade(dados)

def listar_oportunidades():

    return oportunidade_repository.listar_oportunidades()

def buscar_oportunidade_por_id(oportunidade_id):

    return oportunidade_repository.buscar_oportunidade_por_id(oportunidade_id)

def atualizar_oportunidade_por_id(oportunidade_id, novos_dados: oportunidade.AtualizarOportunidade):

    dados = novos_dados.model_dump(exclude_unset=True)

    datas_validas = validar_periodo_oportunidade(dados["data_inicio"], dados["data_fim"])

    if not datas_validas:
        return {
            "erro": "Datas estão inválidas"
        }
        
    return oportunidade_repository.atualizar_oportunidade_por_id(oportunidade_id, dados)


