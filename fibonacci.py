#Função principal
def sequencia_fibonacci(entrada):
    #Valores Inicias
    a, b = 0, 1

    #Enquanto 'a' for menor ou igual a entrada 
    while a <= entrada:
        if a == entrada:
            return True
        else:
            a = b
            b = a + b
    return False

#Funcão de inicio
def main():
    entrada = int(input("Digite um número: "))


    #Verificação de saída
    if sequencia_fibonacci(entrada):
        print(f'O número {entrada} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {entrada} não pertence à sequência de Fibonacci.')


main()
