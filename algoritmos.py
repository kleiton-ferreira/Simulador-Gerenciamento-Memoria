def first_fit(blocos, processo_id, tamanho_processo):
    for i, bloco in enumerate(blocos):
        if bloco['status'] == 'livre' and bloco['tamanho'] >= tamanho_processo:
            if bloco['tamanho'] > tamanho_processo:
                novo_bloco = {'status': 'livre',
                              'tamanho': bloco['tamanho'] - tamanho_processo,
                              'processo_id': None}
                blocos.insert(i + 1, novo_bloco)

            bloco['status'] = 'ocupado'
            bloco['tamanho'] = tamanho_processo
            bloco['processo_id'] = processo_id
            return True
    return False


def best_fit(blocos, processo_id, tamanho_processo):
    melhor_bloco = -1
    for i, bloco in enumerate(blocos):
        if bloco['status'] == 'livre' and bloco['tamanho'] >= tamanho_processo:
            if melhor_bloco == -1 or blocos[melhor_bloco]['tamanho'] > bloco['tamanho']:
                melhor_bloco = i

    if melhor_bloco != -1:
        bloco = blocos[melhor_bloco]
        if bloco['tamanho'] > tamanho_processo:
            novo_bloco = {'status': 'livre',
                          'tamanho': bloco['tamanho'] - tamanho_processo,
                          'processo_id': None}
            blocos.insert(melhor_bloco + 1, novo_bloco)

        bloco['status'] = 'ocupado'
        bloco['tamanho'] = tamanho_processo
        bloco['processo_id'] = processo_id
        return True
    return False


def worst_fit(blocos, processo_id, tamanho_processo):
    pior_bloco = -1
    for i, bloco in enumerate(blocos):
        if bloco['status'] == 'livre' and bloco['tamanho'] >= tamanho_processo:
            if pior_bloco == -1 or blocos[pior_bloco]['tamanho'] < bloco['tamanho']:
                pior_bloco = i

    if pior_bloco != -1:
        bloco = blocos[pior_bloco]
        if bloco['tamanho'] > tamanho_processo:
            novo_bloco = {'status': 'livre',
                          'tamanho': bloco['tamanho'] - tamanho_processo,
                          'processo_id': None}
            blocos.insert(pior_bloco + 1, novo_bloco)

        bloco['status'] = 'ocupado'
        bloco['tamanho'] = tamanho_processo
        bloco['processo_id'] = processo_id
        return True
    return False
