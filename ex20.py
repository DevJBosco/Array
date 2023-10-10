D = [0,0,0,0,0,0,0,0,0,0]

for y in range (10):
     D[y]=int(input("digite um número: "))

for z in range(10):
    if D[z]%2!=0:
        print(f"Este é impar: {D[z]}")
    else:
        print(f"Este é par: {D[z]}")

    if D[z]>0:
        print(f"Este é positivo: {D[z]}")
    elif D[z]<0:
        priont(f"Este é negativo: {D[z]}")
    else:
        print(f"Zero {D[z]}")
