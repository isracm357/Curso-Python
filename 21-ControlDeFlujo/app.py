if 5==2:
    print('Es correcto')
else:
    print('No es correcto')

#JEMPLO 2
mascota='perro'
if mascota=='gato':
    print("Tiene un gato")
elif mascota=='perro':
    print("Tienes un perro")
else:
    print("No tienes una mascota")
    
#EJEMPLO 3

edad =14
calificacion=9
if edad <18:
    print("Eres menor de edad")
    if calificacion>=7:
        print('Aprobado')
    else:
        print('No apruebo')
elif edad>18:
    print("Eres una persona adulta")