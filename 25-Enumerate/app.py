lista=["a", "b", "c","d"]
indice=0
for item in lista:
    print(indice, item)
    #ESTO 
    #Operadores de asignación
    indice += 1
    #ES LO MISMO QUE ESTO
    #indice =indice+1
print("\n")
#CON ENUMERATE

lista=["a", "b", "c","d"]

for i, item in enumerate(lista):
    print(i, item)
    
####UNA COMBINACIÓN DE ENUMERATE CON RANGE
print("\n")
for i, item in enumerate(range(60,65)):
    print(f"{i} - {item}")
####################################
print("\n")

lista=["a", "b", "c","d"]

mis_tuplas= list(enumerate(lista))
print(mis_tuplas)

print(mis_tuplas[1])
print(mis_tuplas[1][0])
print(mis_tuplas[1][1])