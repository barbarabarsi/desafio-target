def inverter(string):

    # Copia no final da string os caracteres na ordem contrária
    for i in range(len(string)-1,-1,-1):
        string = string + string[i]
    tam = int(len(string)/2) # Como a string dobrou de tamanho (pois possui uma cópia sua revertida unida a si), calculamos o tamanho da string invertida
    return string[tam:] # Retorna apenas a metade final, ou seja, a parte invertida

def insere_string():
    string = input("Insira a string a ser invertida: ")
    print(f"A string {string} invertida é {inverter(string)}")
    
insere_string()