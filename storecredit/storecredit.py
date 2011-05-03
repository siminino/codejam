def s_credit(credit, n_itens, itens):
    itens = itens.split(' ')
    result = 0

    if len(itens) == 1:
        return '1'

    for item_1 in range(len(itens)):
        for item_2 in range(len(itens)):
            if int(itens[item_1]) + int(itens[item_2]) > result and int(itens[item_1]) + int(itens[item_2]) <= credit and item_1 != item_2:
                result = int(itens[item_1]) + int(itens[item_2])
                response = '%d %d' % ((item_1 + 1), (item_2 + 1))

    return response


