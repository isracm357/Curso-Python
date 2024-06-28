class Calculadora:
    def __init__(self):
        pass
    
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero no permitida."
        return a / b
    
    def potencia(self, a, b):
        return a ** b
    
    def raiz_cuadrada(self, a):
        if a < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo."
        return a ** 0.5

def mostrar_menu():
    print("\nCalculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Salir")

def obtener_numero(prompt):
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def main():
    calculadora = Calculadora()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            a = obtener_numero("Ingrese el primer número: ")
            b = obtener_numero("Ingrese el segundo número: ")
            print(f"Resultado: {calculadora.sumar(a, b)}")
        elif opcion == '2':
            a = obtener_numero("Ingrese el primer número: ")
            b = obtener_numero("Ingrese el segundo número: ")
            print(f"Resultado: {calculadora.restar(a, b)}")
        elif opcion == '3':
            a = obtener_numero("Ingrese el primer número: ")
            b = obtener_numero("Ingrese el segundo número: ")
            print(f"Resultado: {calculadora.multiplicar(a, b)}")
        elif opcion == '4':
            a = obtener_numero("Ingrese el primer número: ")
            b = obtener_numero("Ingrese el segundo número: ")
            print(f"Resultado: {calculadora.dividir(a, b)}")
        elif opcion == '5':
            a = obtener_numero("Ingrese la base: ")
            b = obtener_numero("Ingrese el exponente: ")
            print(f"Resultado: {calculadora.potencia(a, b)}")
        elif opcion == '6':
            a = obtener_numero("Ingrese el número: ")
            print(f"Resultado: {calculadora.raiz_cuadrada(a)}")
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()