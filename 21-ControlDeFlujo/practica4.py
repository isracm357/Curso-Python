print("INDICE DE MASA CORPORAL")
peso=float(input("Ingrese su peso en kg: "))
estatura=float(input("Ingrese su estatura en m: "))

imc=(peso/estatura**2)
imc2=round(imc, 2)
print(f"Su IMC es de {imc2}")
#resultado=(f"{(peso)/(estatura**2)}")
resultado_numero=float(imc2)

if resultado_numero <= 18.5:
    print("Tiene un peso bajo")
elif resultado_numero >= 25:
    print("Tiene sobrepeso")
elif resultado_numero >= 18.5 and resultado_numero <=25:
    print("Tiene un peso normal")
elif resultado_numero >= 30:
    print ("Tiene Obesidad")




