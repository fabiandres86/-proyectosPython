a=(input("3 letras: ")) ##Pido ingresar 3 letras
c=[] ##creo una variable de lista vacia
b=len(a) ##creo una variable con el valor de len de a
while b>0: #mientras el valor de b sea mayor que 0
    c.append([]) #agrego un espacio vacio a la lista de c
    b=b-1 ##y le resto 1 a b
    if b==0: ##cuando b es igual a 0
        break ##rompo el ciclo
print(c) ##print c para verificar que se creo la lista vacia en c
c[0]=a[0] ##asigno el indice 0 de a en indice 0 de c
c[1]=a[1] ##lo mismo pero con indices 1 y 2
c[2]=a[2] ##basicamente, los valores que ingresé los pongo en c
          ##eso porque no se como crear una lista con input xd
print(c) ##print c para verificar que los valores se pusieron correctamente
d=["0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
   "t","u","v","w","x","y","z","a"] ##creo una lista con todas las letras del
                                    ##del alfabeto y empiezo por "0" y termino
                                    ##con "a" adelante explicaré porque
e=0 ##creo una variable con valor 0
f=d[e] ##creo una variable con valor al indice del valor de e, 0 en este caso
while c[0]!=f[0]: ##mientras el indice 0 de c no sea igual al indice 0 de f
                  ##aqui si la lista de d empeiza por a y el primer indice
                  ##de c es a también, nunca empieza el while, por eso empieza
                  ##la lista en 0
    e=e+1 ##el valor de e aumenta en 1
    f=d[e] ##vuelvo a asignar el indice e a f porque si no, f se queda en "0"
    if c[0]==f[0]: ##si indice 0 de es igual a indice 0 de f
        e=e+1 ##vuelvo a aumentar el valor de e en 1
        f=d[e] ##y lo vuelvo a asignar a f
        c[0]=f[0] ##y le doy el valor de indice 0 de f a indice 0 de c
        e=0 ##reseteo e devolviendolo a 0
        f=d[e] ##y otra vez asigno e al indice d para f
        print(c) ##print c para corroborar que cambió el indice 0 correctamente
        break ##romper el ciclo
##después hago 2 veces más el mismo while, pero con indice 1 y 2 de c para
##cambiar todos los indices, y por cierto, la lista d termina en a, para que
##cuando un indice valga "z" y lo compruebe en d, se pueda mover una vez más
##y así asignarle "a"
while c[1]!=f[0]:
    e=e+1
    f=d[e]
    if c[1]==f[0]:
        e=e+1
        f=d[e]
        c[1]=f[0]
        e=0
        f=d[e]
        print(c)
        break
while c[2]!=f[0]:
    e=e+1
    f=d[e]
    if c[2]==f[0]:
        e=e+1
        f=d[e]
        c[2]=f[0]
        e=0
        f=d[e]
        print(c)
        break



        
##c=0
##d=b[c]
##print(c,d)
##while a[0]!=d[0]:
    ##c=c+1
    ##d=b[c]
    ##print(c,d)
    ##if a[0]==d[0]:
        ##c=c+1
        ##d=b[c]
        ##a[0]=d[0]
        ##c=0
        ##d=b[c]
        ##print(a)
        ##break