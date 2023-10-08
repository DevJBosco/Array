
a=[]
contador=0
num = 0
while contador <= 8:
     if num %2 == 0:
          num += 1
          a.append(num)
     else:
          num += 2
          a.append(num)
          contador += 1
print(a)