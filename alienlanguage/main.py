from alienlang import alien_trans

info = raw_input().split(' ')
words = []
words_test = []

for L in range(int(info[1])):
    word = raw_input()
    words.append(word)

for N in range(int(info[2])):
    word_test = raw_input()
    words_test.append(word_test)

words = '\n'.join(words)
words_test = '\n'.join(words_test)

print alien_trans(int(info[0]), int(info[1]), int(info[2]), words, words_test)



