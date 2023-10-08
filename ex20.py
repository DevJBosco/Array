numeros= []

for x in range (10):
     num = float(input("Digite um número:"))
     numeros.append(num)

#listas separadas

numeros_pares = []
numeros_impares = []
numeros_zeros = []
numeros_positivos = []
numeros_negativos = []

for num in (numeros):
     if num %2==0:
          numeros_impares.append(num)
     else:
          numeros_pares.append(num)
     if num > 0:
          numeros_positivos.append(num)
     elif num < 0:
          numeros_negativos.append(num)
     elif num == 0:
          numeros_zeros.append(num)

print(f"Na lista  {numeros_pares} são números pares e {numeros_impares} números impáres")
print(f"{numeros_positivos} são positivos e {numeros_negativos} são negativos.")
print(f"{numeros_zeros} são zero")
