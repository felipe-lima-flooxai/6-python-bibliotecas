import calendar

#print(calendar.calendar(2022))
#print("-----------------")
#print(calendar.month(2025, 7))

ano = 2025
mes = 7

print("Calendário do ano:")
print(calendar.calendar(ano))

print("\nCalendário do mês:")
print(calendar.month(ano, mes))

print("Primeiro dia da semana:", calendar.firstweekday())

print("É bissexto?", calendar.isleap(ano))

print("Qtd anos bissextos entre 2000 e 2030:", calendar.leapdays(2000, 2030))

primeiro_dia, dias_no_mes = calendar.monthrange(ano, mes)
print(f"Julho de {ano} começa em {calendar.day_name[primeiro_dia]} e tem {dias_no_mes} dias")

print("\nMatriz de semanas")
for semana in calendar.monthcalendar(ano, mes):
    print(semana)

print("\nDatas da semana de cada dia útil:")
dias_da_semana = list(calendar.day_name)
for i in range(7):
    print(f"{i}: {dias_da_semana[i]}")