"""
Practica 2
Las leyes de un país establecen que un adulto puede conducir 
si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.

Crea una estructura condicional para verificar 
si una persona de 16 años sin licencia puede conducir, 
y muestra el resultado que corresponda en pantalla:

- "Puedes conducir"
- "No puedes conducir aún. Debes tener 18 años y contar con una licencia"
- "No puedes conducir. Necesitas contar con una licencia"

Utiliza la base de código ya proporcionada para 
plantear la estructura de control de flujo apropiada y verificar dichas condiciones.
"""
edad=float(input("Ingrese su edad: "))
tiene_licencia= input("Tiene licencia? si o no: ")

if edad > 18:
    if tiene_licencia=="si":
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

