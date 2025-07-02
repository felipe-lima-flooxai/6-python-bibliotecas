import sys

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

if len(sys.argv) != 3:
    print("Formato da entrada: python <nome_do_arquivo>.py <valor> <unidade>")
    print("Exemplo: python conversor_temp.py 100 C")
    sys.exit(1)

try:
    valor = float(sys.argv[1])
except ValueError:
    print("Erro: o valor informado não é um número")
    sys.exit(1)

unidade = sys.argv[2].upper()

if unidade == "C":
    convertido = celsius_para_fahrenheit(valor)
    print(f"{valor:.1f}°C = {convertido:.1f}°F")
elif unidade == "F":
    convertido = fahrenheit_para_celsius(valor)
    print(f"{valor:.1f}°F = {convertido:.1f}°C")
else:
    print("Erro: unidade inválida. Use 'C' para Celsius ou 'F' para Fahrenheit.")
