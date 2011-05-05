def create_matriz(H, W, content):
    matriz = []
    content = content.split('\n')
    for h in range(H):
        line = content[h].split(' ')
        matriz.append(line)

    return matriz

