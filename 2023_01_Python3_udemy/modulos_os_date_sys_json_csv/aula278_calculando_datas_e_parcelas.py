from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# fmt = '%d/%m/%Y %H:%M:%S'
# fmt = '%d/%m/%Y'

valor_do_emprestimo = 1000000
data_emprestimo = datetime(2012, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []      # criar uma lista com todas as datas de parcelas

data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_cada_parcela = valor_do_emprestimo / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_cada_parcela:,.2f}' )

print(numero_parcelas)
print(f'{valor_cada_parcela:,.2f}')
