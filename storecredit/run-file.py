from storecredit import s_credit

name_file_input = raw_input('Arquivo com entrada: ')
name_file_output = raw_input('Arquivo com saida: ')

file_input = open(name_file_input, 'r').read()
entry = file_input.split('\n')
n = int(entry[0])
result = []

for case in range(n):
    print case
    pont = (case * 3)
    credits = int(entry[pont+1])
    n_itens = int(entry[pont+2])
    itens = entry[pont+3]
    result.append('Case #%d: %s' %((case+1), s_credit(credits, n_itens, itens)))

result = '\n'.join(result)

file_output = file(name_file_output, 'w')
file_output.write(result)
file_output.close()
