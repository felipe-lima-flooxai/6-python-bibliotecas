from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
meses = 60
parcela_mensal = valor_total / meses

data_inicio = datetime.now()
for i in range(meses):
    data_parcela = data_inicio + relativedelta(months=i)
    print(f"Parcela {i+1:02d}: R$ {parcela_mensal:,.2f} - Vencimento: {data_parcela.strftime('%d/%m/%Y')}")