


import random

def primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_numeros_primos():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

    suma = num1 + num2

    if primo(suma):
        print("Los números aleatorios", num1, "y", num2, "tienen una suma prima:", suma)
    else:
        print("Los números aleatorios", num1, "y", num2, "no tienen una suma prima.")

encontrar_numeros_primos()