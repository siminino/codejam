from storecredit import s_credit

n = int(raw_input())
result = []

for cases in range(n):
    print cases
    credits = int(raw_input())
    n_itens = int(raw_input())
    itens = raw_input() 
    result.append('Case #%d: %s' %((cases+1), s_credit(credits, n_itens, itens)))

result = '\n'.join(result)

file_output = file('result-A-larger.in', 'w')
file_output.write(result)
file_output.close()
