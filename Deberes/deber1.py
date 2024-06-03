"""
La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones. 
"""

print("Trabajador: "+ (input("Nombre: ")))

comisión=input("Ventas del mes: ")

comisiónTotal=int(comisión)

x=comisiónTotal


print(f"Su Comisión es de: {x*0.13}")


print("Nombre y monto correspondiente por las comisiones: "+(input("Nombre: ")+(input(f"Su Comisión es de: {x*0.13}"))))


