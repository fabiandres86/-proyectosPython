from random import randint
c = []
i = 0
while i < 3:
    c.append(input('Ingrese la letra ' + str(i+1)+':\n'))
    i = i + 1
print('Lista original: '+ str(c))

d = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
   "t","u","v","w","x","y","z"]
n = len(d)
for j in range(len(c)):
    for k in range(len(d)):
        if c[j] == d[k]:
            c[j] = d[randint(0, 25)]
            
print('Nueva lista: ' + str(c))
