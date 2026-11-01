from schemas import oportunidade

def validar_periodo_oportunidade(data_inicio, data_fim):
    if data_fim <= data_inicio:
        return False

    return True

def criar_oportunidades(nova_oportunidade: oportunidade.CriarOportunidade):

    dados = nova_oportunidade.model_dump()

    datas_validas = validar_periodo_oportunidade(dados["data_inicio"], dados["data_fim"])

    if not datas_validas:
        return {
            "erro": "Datas estão inválidas"
        }

    return dados