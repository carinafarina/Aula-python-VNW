# print("Olá mundo!!!")
# print("Primeira aula!!!")

#nome = 'Carina'
# print(nome)

#nome_sobrenome = "Farina"
# print(nome,nome_sobrenome)

# tipos de dados 
# interiro (int)

#idade = 18
#frio = -10

# float

#altura = 1.75 
#graus = -2.2

#string (str)

#frase = "Boa noite !!"

# boolean

#tem_saldo = True

# Null

#idade = None

# not defined

#  dia 
#  print(dia)

# Exibir soma 


# primeiro_valor = 2.2
# segundo_valor = 2.1
# print( primeiro_valor + segundo_valor)

#Exibir frasse

# nome = "Marina"
# frase = "Chuvinha de like"
# print(nome, frase)


# idade = 40
# nome = "Carina"

# print(type(idade))
# print(type(nome))


###----------------------------------------------------------

# nome = input("Qual seu nome: ")
# print("olá", nome)

#------------------------------------------------------------

# primeiro_valor = int(input("Digite o primeiro numero: "))
# segundo_valor = int(input("Digite o segundo numero: "))

# soma = primeiro_valor + segundo_valor

# print("A soma dos valores são: ", soma )

#------------------------Condições---------------------------

#saldo = True

#if saldo == True:
    #print('Você está com dinheiro!')

#---------------------------------------------

#idade = 40

#if idade >= 18:
    #print("Você pode dirigir!")
#else:
    #print("Você nâo tem idade para dirigir")

#---------------------------------------------

#idade = 18
#saldo = True        

#if idade >= 18 and saldo  == True: 
    #print('Você pode tirar sua habilitação')
#elif idade <18 and saldo == False:   
    #print('Você não tem idade e dinheiro para tirar habilitação') 
#else:
    #print('Você pode dirigir no vai na web')    
#------------------Operadores logicos--------

# and # == &&
# or # == ||
# not # == !

# for é uma estrutura de repetição (loop)

# for caracter in 'Python':
    #print(caracter)

# lista_dos_sonhos = ["Iate", "Ferrari", "Resort", "Jatinho"]

# for item in lista_dos_sonhos:
    #print(item)

#-----------------
# contador = 0

# while contador <= 10:
#    print(contador)
#    contador += 1
#------------------
#lanche = 'Pizza'
#print(lanche.upper())
#------------------
#lanche = 'Pizza'
#print(lanche.lower())
#---tamplete string----
#lanche = 'Pizza'
#print(f'seu lanche é:{lanche}')

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

