#!/usr/bin/python3

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:

        num = int(input('Ingresa un número: '))
        assert num > 0,"debe ser numero y positivo"
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("El dato debe ser un entero")

if __name__ == "__main__":
    run()