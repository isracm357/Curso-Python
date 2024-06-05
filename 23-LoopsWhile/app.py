monedas =5
while monedas >0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
    
#EJERCICIO

respuesta ='s'
""""
while respuesta== 's':
    #respuesta=input("Quieres seguir ?(s/n)")
    pass
else:
    print("Gracias")
"""
#break
nombre= input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        #break
        continue
    print(letra)