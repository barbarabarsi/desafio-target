
# Definição dos elementos de base de Fibonacci
fib = [0,1]

# Função que estrutura a sequência até encontrar o número desejado enquanto não existir um número maior que ele
def verifica_fib(num):
    if fib[-1] == num or fib[0] == num:
        return 0
    elif fib[-1] > num:
        return 1
    fib.append(fib[-1]+fib[-2])
    return verifica_fib(num)

def fibonacci():

    num = input("Insira o número a ser verificado na sequência: ")
    
    # Validação de entrada
    if num.isdigit() == False:
        print("Número invalido. Insira um número positivo e verifique a existência de caracteres não-numéricos.")
        return fibonacci()   

    if verifica_fib(int(num)):
        print("O número não está presente na sequência de Fibonacci.")
    else:
        print(f"O número está presente na sequência de Fibonacci na posição {fib.index(int(num))+1}.")
    
fibonacci()