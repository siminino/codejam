def alien_trans(L,D,N,words,text):
    words = words.split('\n')
    text = text.split('\n')
    caso = 0
    result = []

    for test_text in text:
        letter_possible = []
        caso +=1
        cont = 0
        em_paren = False
        for letter in test_text:
            letter_possible.append('')
            if letter == '(':
                em_paren = True
            if letter == ')':
                em_paren = False

            if em_paren:
                letter_possible[-1] +=letter

        for test_words in words:
            if test_text == test_words:
                cont += 1
            else:
                for letter_index in range(L):
                    if (test_words[letter_index] in letter_possible[letter_index]) or (test_words[letter_index] == test_text[letter_index]):
                        is_equal = True
                    else:
                        is_equal = False
                        break
                if is_equal:
                    cont +=1

        result.append('Case #%d: %s' % (caso, cont))

    response = '\n'.join(result)

    return response





