from codigo import reverse_words

n = int(raw_input())
result = ''

for testcase in range(n):
    text = raw_input()
    result += 'Case #%d: %s\n' % (testcase+1,reverse_words(text))

print result


