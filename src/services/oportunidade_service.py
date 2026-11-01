def validar_periodo_oportunidade(data_inicio, data_fim):
    if data_fim <= data_inicio:
        return False

    return True