"""
Practica 2

Crea una lista formada por las tuplas (indice, elemento), 
formadas a partir de obtener mediante enumerate() los índices 
de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices .
"""
lista_indices="Python"

for indice, elemento in enumerate(lista_indices):
    print(f"{indice}{elemento}")
lista_indices=list(enumerate("Python"))
print (lista_indices)