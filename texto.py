# Feito com uso do chatGPT

def repetir_string(string, vezes):
    return string * vezes

# Solicita ao usuário uma string e um número inteiro
string = input("Digite uma string: ")
vezes = int(input("Digite o número de vezes que deseja repetir a string: "))

# Chama a função e imprime o resultado
resultado = repetir_string(string, vezes)
print("Resultado da repetição:", resultado)
