#EJERCICIO 1
def devolver_distintos(*args):
    suma = sum(args)
    if suma > 15:
        return max(args)
    elif suma < 10:
        return min(args)
    else:
        return sorted(args)[1]

print(devolver_distintos(9,6,1))

#EJERCICIO 2
print("\n")

def letras_unicas_ordenadas(palabra):
    # Convertir la palabra a un conjunto para obtener letras únicas
    letras_unicas = set(palabra)
    # Ordenar las letras únicas alfabéticamente
    letras_ordenadas = sorted(letras_unicas)
    return letras_ordenadas

resultado = letras_unicas_ordenadas("python")

print(resultado)

#EJERCICIO 3 
("\n")

def contiene_doble_cero(*args):

    for item in range(len(args) - 1):
        if args[item] == 0 and args[item + 1] == 0:
            return True
    return False

# Probar la función con los ejemplos proporcionados
print(contiene_doble_cero(5, 6, 1, 0, 0, 9, 3, 5,0))


