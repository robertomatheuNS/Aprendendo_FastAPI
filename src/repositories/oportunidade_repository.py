oportunidades = []

def salvar_oportunidade(nova_oportunidade):

    novo_id = len(oportunidades) + 1

    nova_oportunidade["id"] = novo_id

    oportunidades.append(nova_oportunidade)

    return nova_oportunidade

def listar_oportunidades():
    return oportunidades

def buscar_oportunidade_por_id(oportunidade_id):
    for oportunidade in oportunidades:
        if oportunidade_id == oportunidade["id"]:
            return oportunidade
        
    return None

def atualizar_oportunidade_por_id(oportunidade_id, novos_dados):
    oportunidade_encontrada = buscar_oportunidade_por_id(oportunidade_id)

    if oportunidade_encontrada is not None:
        oportunidade_encontrada.update(novos_dados)

    return oportunidade_encontrada