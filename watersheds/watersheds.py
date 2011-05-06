def create_matriz(H, W, content):
    matriz = []
    content = content.split('\n')
    for h in range(H):
        line = content[h].split(' ')
        matriz.append(line)

    return matriz

def min_west_sheed(H,W,matriz):
    menor = 9999999
    for item_index in range(W):
        for line_index in range(H):
            if int(matriz[line_index][item_index]) < menor:
                menor = int(matriz[line_index][item_index])
                line = line_index
                item = item_index

    return [line, item]

