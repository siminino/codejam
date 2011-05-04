def alien_trans(L,D,N,words,text):
    words = words.split('\n')
    text = text.split('\n')
    caso = 0
    result = []

    for test_text in text:
        caso +=1

        letter_possible = list_letter(test_text)
        cont = times_in_words(words, test_text, letter_possible, L)

        result.append('Case #%d: %s' % (caso, cont))

    response = '\n'.join(result)

    return response


def list_letter(test_text):
    em_paren = False
    letter_possible = []
    for letter in test_text:
        if letter == '(':
            em_paren = True
            letter_possible.append('')
        elif letter == ')':
            em_paren = False
        elif em_paren == False:
            letter_possible.append(letter)
        elif em_paren:
            letter_possible[-1] +=letter

    return letter_possible

def times_in_words(words, test_text, letter_possible, L):
    cont = 0
    for test_words in words:
        if test_text == test_words:
            cont += 1
        else:
            for letter_index in range(L):
                if (test_words[letter_index] in letter_possible[letter_index]):
                    is_equal = True
                else:
                    is_equal = False
                    break
            if is_equal:
                cont +=1

    return cont

