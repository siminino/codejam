def reverse_words(text):
    text = text.split(' ')
    reverse_text = []
    for word in text[::-1]:
        reverse_text.append(word)

    return ' '.join(reverse_text)
