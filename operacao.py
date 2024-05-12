# Codigo gerado com chatGPT


def soma(a, b): 
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

# Solicita ao usuário dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicita ao usuário a operação desejada
operacao = input("Escolha a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão): ")

# Realiza a operação selecionada
if operacao == '+':
    resultado = soma(numero1, numero2)
elif operacao == '-':
    resultado = subtracao(numero1, numero2)
elif operacao == '*':
    resultado = multiplicacao(numero1, numero2)
elif operacao == '/':
    resultado = divisao(numero1, numero2)
else:
    resultado = "Operação inválida!"

# Imprime o resultado
print("Resultado da operação:", resultado)
