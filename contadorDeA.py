def contar_letra_a(string):
    #Converte a string 
    string_minuscula = string.lower()

    #Faz a contagem de a e ã
    conta_a = string_minuscula.count('a')
    conta_ã = string_minuscula.count('ã')

    total = conta_a + conta_ã                         
    
    #condicional
    if total > 0:
        print(f"A letra 'a' aparece {total} vez(es) no texto.")

    else:
        print("A letra 'a' não aparece no texto!")
        
#função de chamada
def main():
    texto = input("Digite o texto desejado: ")
    contar_letra_a(texto)

main()
            
                                 
        
        
