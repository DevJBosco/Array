cont = 0
impar = 0
c=[0,0,0,0,0,0,0,0,0,0]
while True:
    if cont%2!=0:
        c[impar]=cont
        impar+=1
    cont+=1
    if impar>=10:
        break
print(c)
