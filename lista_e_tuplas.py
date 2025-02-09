#---------------------------------------------------------------------

# Listas e Tuplas

# ---------------------------------------------------------------------

# lista é a mesma coissa que array

# aluno = ['Carina', 'Maria','João']
# print(len(aluno))
#           0         1       2  
# print(aluno[0:2])
# print(aluno[-3])
# print(type(aluno))

frutas = ['maçã', 'banana', 'uva', 'laranja', 'banana']

#frutas.insert(1,'Manga') # metodo insert é para incluir um item.
#print(frutas)

#frutas.append('abacaxi') # metodo append adiciona um item ao final da lista.
#print(frutas)

#frutas.remove('banana') # metodo remove o item como nome especifico da lista.
#print(frutas)

#frutas.pop(2) # metodo remove com o nomero da casa do item da lista .
#print(frutas)


#frutas.sort() # metodo sort ordenar os item da lista.
#print(frutas)

#numeros = [10,11,15,60,2,1]

# numeros.sort()
# print(numeros)

# quantidade = frutas.count('banana') # metodo count retorna quantas vezes o item aparece na lista.
# print('Quantas bananas tem na lista: ',quantidade)

#---------------Tuplas---------------------------------------------------

# as tuplas não podem ser modificadas como as const em javascript
# uma lista pode estar dentro de uma tupla ou vice e versa

minha_tuplas = ('Carina', '1234',['rg ', 'cpf'], 10, True)
print(type(minha_tuplas))

pratos = ('Lasanha', 'Churrasco')
pratos2 = ('Strogonoff', 'Feijoada')
print(pratos, pratos2)

nova_tuplas = pratos + pratos2
print(nova_tuplas)
print ('Lasanha' in nova_tuplas)

lista = [1,2,3]
tuple = tuple(lista) # (1,2,3)

nova_lista = list(tuple)
print(type(nova_lista))

# a tupla é imutavel e é mais rapida, eficiente

