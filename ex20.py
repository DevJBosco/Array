D = [0,0,0,0,0,0,0,0,0,0]
impares= []
pares = []
positivos = []
negativos = []
zero = []
for y in range (10):
     D[y]=int(input("digite um número: "))

for z in range(10):
    if D[z]%2!=0:
        impares.append(z)
    else:
        pares.append(z)

    if D[z]>0:
        positivos.append(z)
    elif D[z]<0:
        negativos.append(z)
    else:
        zero.append(z)
print(f"Deste números os pares são: {pares}")
print(f"Destes números os impares são {impares}")
print(f"Destes números {positivos} são positivos")
print(f"Destes números  {negativos} são negativos")
print(f"Destes números foram encontrados {zero} zero(s)")
