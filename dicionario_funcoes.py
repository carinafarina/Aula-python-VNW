#-------Dicionario e Funções------------


# alunos = { #Qdo usa a chaves é o dicionario (objeto no js)
  #'nome': 'Carina',
  #'idade': 20, # colocarr o f na antes do valor e as chaves para incluir algo como o exemplo.
  #'altura': 1.75
# } # seu eu incluir virgula no final da chave vira uma tuplas, se add conchete antes da chaves vira lista.

#print(type(alunos))
#print(alunos)

#print(alunos['idade']) # colocar o conchete para trazer o campo do dicionario que voce quer exibir.

#alunos['cidade'] = 'Salvador' # serve para inserior outra chave de valor. 
#alunos['nome'] = 'Marina'
#--------------------------------------------
#alunos.update({'aluno':True, 'cpf':3333333})
#print(alunos)


#--------------------------------------------
# del alunos['cidade']
# print(alunos)

# alunos.clear() # Para remover todos os itens do dicionario
# print(alunos)

#-------------------------------------------
#restaurante = {
#    'prato1': 'Pizza',
#    'prato2': 'Tapioca',   
#}
#restaurante['prato3'] = 'Manga com Sal'
#print(restaurante)

#ultimo_item = restaurante.popitem()
#print(restaurante)

#-----------Funções--------------------------

def minha_funcao():
    print('Olá, seja bem vindo !!! ')   

minha_funcao()
    
def criar_email(nome,dominio='gmail.com'):
    endereco_email = f'{nome}@{dominio}'
    return endereco_email

print(criar_email('carina'))

def par_impar(numero):    
    if numero % 2 == 0:
        numero =True
    else:
        numero = False    
    return numero

print(par_impar)

par_impar(5)


