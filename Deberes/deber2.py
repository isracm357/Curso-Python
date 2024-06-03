
factura= float(input("¿Cuál fue la factura total? "))
propina= float(input("¿Cuanta propina te gustaría dar (%)? "))
cuenta=int(input("¿Cuántas personas para dividir la cuenta? "))

porcentaje_propina=factura/cuenta*propina/100
print(f"Factura por persona: {factura/cuenta}")
print(f"Propina: {factura/cuenta*propina/100}")


total_por_persona= factura/cuenta+porcentaje_propina
total_por_persona_redondeado=round(total_por_persona, 2)

print(f"Cada persona debe pagar: {total_por_persona_redondeado}")





