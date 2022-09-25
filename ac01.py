# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO: Leonardo Araujo Ieva - RA: 2202124

'''
Implemente a função 'posicoes' que recebe como argumentos de entrada uma
tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, num):
  lista = []

  for posicao in range(0,len(tupla)):
    if tupla[posicao] == num:
      lista.append(posicao)

  return lista   


'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma tupla e dois itens (velho e novo) e retorna uma tupla onde todas as
ocorrências do item velho são substituídas pelo item novo.
'''


def substituir(tupla, velho, novo):
    mudar = list(tupla)
    for elemento in mudar:
        if elemento == velho:
            mudar[mudar.index(elemento)] = novo

    mudar = tuple(mudar)      
    
    return mudar


'''
Implemente a função 'multiplica_matriz' que recebe como argumento de entrada
uma matriz de qualquer tamanho e multiplica cada item da matriz pelo maior
item dessa matriz. A função deve retornar a matriz resultante.
'''


def multiplica_matriz(matriz):
  lista_maiores = []
  copia_matriz = [linha[:] for linha in matriz]

  for linha in copia_matriz:
    lista_maiores.append(max(linha))

  maior_maiores = max(lista_maiores)

  for linha in copia_matriz:
    for elemento in linha:
      mult_escalar = maior_maiores * elemento
      linha[linha.index(elemento)] = mult_escalar 

  return copia_matriz


'''
Considere um dicionario onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada 'reprovados' que recebe como argumentos
de entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
A lista de nomes deve ser ordenada em ordem alfabética.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
'''


def reprovados(alunos):
  lista_reprovados = []

  for aluno in alunos:
    media = (sum(alunos[aluno]) / len(alunos[aluno]))
    if media < 6:
      lista_reprovados.append(aluno)
  
  lista_reprovados.sort()
  
  return lista_reprovados


'''
Considere um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Implemente a função 'excluir_menor_nota' que recebe como argumentos
de entrada o dicionário e o nome de um aluno. A função deve excluir a menor
nota do aluno informado e retornar o dicionário com as alterações realizadas.
Se aluno não estiver no dicionário, deve retornar o dicionário sem alterações.
'''


def excluir_menor_nota(alunos, nome):
  if nome not in alunos:
    return alunos    

  nota_alunos = alunos[nome]
  nota_minima = min(nota_alunos)
  nota_alunos.remove(nota_minima)

  return alunos


'''
Implemente a função 'caracteres_unicos' que recebe como argumento de entrada
uma string e retorna a quantidade de caracteres exclusivos presentes na string.
Por exemplo a string "exemplo de texto" possui 9 caracteres exclusivos
('e', 'x', 'm', 'p', 'l', 'o', 'd', 't', ' '), já a string "zzz" possui
apenas 1 caractere exclusivo ('z').
'''


def caracteres_unicos(texto):

  lista_car_unicos = []

  for caracter in texto:
    if caracter not in lista_car_unicos:
      lista_car_unicos.append(caracter)
    
  contagem_unicos = len(lista_car_unicos)
  
  return contagem_unicos
    