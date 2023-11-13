# ANTES

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# COM LISTA

notas = [7.9, 9.7, 8.2]

# CRIANDO LISTAS

lista = []
lista = list ()
lista = [26, "Pedro", 3.14459, False]
lista_de_listas = [10, [1,2,3]]

# INDEXAÇÃO E SLICES

lista = [26, "Pedro", 3.14459, False]
print (lista [0])
print (lista [1])
print (lista [2])
print (lista [3])
# print (lista[4]) retorna "out of range"

print (lista [-1])
# retorna o último número da lista, -2 seria o antepenúltimo e assim sucessivamente 


# SLICES

lista = [10, 50, 30, 40, 25, 60, 5]
print (lista [0:3])
print (lista [3:6])
# começa no três e vai até o índice menor que 6
print (lista [3:])
print (lista [2:6:2])

# INTERAÇÕES COM FOR 

# 1 utilizando os próprios elementos da lista
for elemento in lista:
    print (elemento)

# 2 utilizando os índices
print ("Comprimento da lista:", len (lista))

for i in range (len (lista)):
    print (i)
    # código mais dinâmico, conta quantos elementos tem


# MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

#append
