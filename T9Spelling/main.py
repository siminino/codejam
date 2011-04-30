from codigo import spelling
import os

n = int(raw_input())
result = ''

for testcase in range(n):
    text = raw_input('Input #%d: '%(testcase+1))
    result += 'Case #%d: %s\n' % (testcase+1, spelling(text))

os.mknod('result-C-larger.in')

archive = file('result-C-larger.in','w')
archive.write(result)
archive.close()

