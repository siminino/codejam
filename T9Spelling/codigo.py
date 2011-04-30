def spelling(text):
    teclado = [' ','.','abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz', '*', '#']
    sequencia = ''
    result = []

    for letra in text:
        for tecla in teclado:
            if letra in tecla:
                try:
                    if str(teclado.index(tecla)) in sequencia[-1]:
                        result.append(sequencia)
                        sequencia = ''
                except:
                    pass
                sequencia += (tecla.index(letra) + 1) * str(teclado.index(tecla))

    result.append(sequencia)

    return ' '.join(result)


