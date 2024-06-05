lista= ['a', 'b', 'c','d']

#print(lista[0])
#print(lista[1])
#print(lista[2])

#DE FORMA MÁS SENCILLA SE UTILIZAN LOS LOOPS
for item in lista:
    numero_letra=lista.index(item) + 1
    print(f"letra {numero_letra}: {item}")
    
    
#EJEMPLO 2 
lista1=['Pablo', 'laura', 'jose', 'luis', 'julia']

for item in lista1:
    if item.startswith('l'):
        print(item)
    else:
        print("Nombre que no comienza con l")
        
#EJEMPLO 3
numeros=[1,2,3,4,5]
mi_valor= 0
for item in numeros:
    mi_valor= mi_valor + item 
    print (mi_valor)
    
#DIRECTAMENTE DATOS DE SUBLISTAS

for a,b in [[11,2],[2,3],[5,6]]:
    print(f"{a} - {b}")
    
#DICCIONARIOS
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for a,b in dic.items():
    print(a,b)