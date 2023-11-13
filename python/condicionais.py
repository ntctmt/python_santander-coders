"""
imprimir "aprovada(o)" caso o estudante tenha uma média superior ou igual a 7 e "reprovada(o)" caso a média seja inferior a 7
"""

# EXEMPLO 1

"""
idade = 20
if idade >= 18:
    print ("Você é maior de idade!")
else: 
    print ("Você é menor de idade!")
"""


# EXEMPLO 2

media = float (input ("Informe a média:"))

if media >= 7:
    print ("Você foi aprovado(a)!")
elif media >= 5:    #else + if
    print ("Recuperação!")
else: 
    print ("Você foi reprovado(a)!")

media = 5
presenca = 50

if media >=7 and presenca >= 70:
    print("Aprovado(a)!")
    print("Parabéns!")
else:
    print("Reprovado(a)!")
    print("Tente novamente.")

