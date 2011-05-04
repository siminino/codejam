from alienlang import alien_trans

name_input = raw_input('Name input file: ')
name_output = raw_input('Name output file: ')

file_input = open(name_input, 'r')

info = file_input.readline().split(' ')
content = file_input.read().split('\n')

words = []
words_test = []

for line in range(int(info[1])+int(info[2])):
    if line < int(info[1]):
        words.append(content[line])
    else:
        words_test.append(content[line])

print len(words)
print len(words_test)


words = '\n'.join(words)
words_test = '\n'.join(words_test)


result =  alien_trans(int(info[0]), int(info[1]),int(info[2]), words, words_test)

file(name_output, 'w').write(result)


