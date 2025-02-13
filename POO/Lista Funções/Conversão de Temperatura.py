# Crie um programa que converte uma temperatura em graus Celsius para Fahrenheit. A
# fórmula de conversão é: F=59C+32

c = float(input("Digite a temperatura que deseja converter para fahrenheit: "))

def conversão(c):
  f = (c * 9/5) + 32
  print(f"{c} Celcius é equivalente a {f}")

conversão(c)    