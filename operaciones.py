def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

if __name__ == "__main__":
    x = 10
    y = 5

    print(f"Suma: {sumar(x, y)}")
    print(f"Resta: {restar(x, y)}")
    print(f"Multiplicación: {multiplicar(x, y)}")
    print(f"División: {dividir(x, y)}")
