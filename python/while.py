# EXEMPLO 1

numero_sorteado = 15

numero_escolhido = int (input ("Informe um número entre 1 e 20:"))

while numero_escolhido != numero_sorteado:
    print ("Você errou o número. Tente novamente!")

    numero_escolhido = int (input ("Informe um número entre 1 e 20:"))

print ("Parabéns, você acertou!")



# EXEMPLO 2

contador = 0

while contador <10:
    print (contador)

contador = contador + 1



"""
erro de "looping infinito": aperte ctrl + c pra parar a execução/fluxo
para apagar os dados no terminal: escreva CLS
"""