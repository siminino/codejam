from printresult.fileresult import writeresult

from codigo import spelling

n = int(raw_input())
result = ''

for testcase in range(n):
    text = raw_input('Input #%d: '%(testcase+1))
    result += 'Case #%d: %s\n' % (testcase+1, spelling(text))

writeresult('result-C-larger.in')
