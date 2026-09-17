import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def soma(a, b):                #define a função de soma
    return a + b

def sub(a, b):
    return a - b              #Define a função de subitração nessa porra

def mult(a, b):
    return a * b                #Define a função de multiplicação

def div(a, b):
    return a / b                     #Define a função divisão

print("Bem vindo á Calculadora Leal")
print("Para iniciarmos, digite 2 números inteiros:  ")


while True:
    try:
        d1 = int(input(""))
        break
    except ValueError:
        print("Aviso! Entrada inválida! Por favor, digite apenas valores inteiros!: ")
while True:
    try:
        d2 = int (input(""))
        break
    except ValueError:
        print("Aviso! Entrada inválida! Por favor, digite apenas valores inteiros!: ")

limpar_terminal()

print(f"{d1, d2} Perfeito!")



