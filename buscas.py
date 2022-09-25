def busca_linear(lista, item):
    for i in range(len(lista)):         # percorre lista do índice 0 a n–1
        if lista[i] == item:
            return i                    # encontrou item na posição i
    return -1                           # não encontrou o item


def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2      # índice da metade da lista
        if lista[meio] == item:         # encontrou item
            return meio
        elif item > lista[meio]:        # busca na segunda metade da lista
            inicio = meio + 1
        else:                           # busca na primeira metade da lista
            fim = meio - 1
    return -1                           # não encontrou o item


'''
EXERCÍCIO 1:
Implemente a função 'busca_linear_alteracao', alterando o algoritmo de
busca linear para que ele se torne um algoritmo de atualização.
Caso seja encontrado o item, ele faz a alteração para um novo valor.
Deve alterar apenas a primeira ocorrência do valor encontrado.
'''


def busca_linear_alteracao(lista, item, novo_valor):
    


'''
EXERCÍCIO 2:
Implemente a função 'busca_binaria_alteracao', alterando o algoritmo de
busca binária para que ele se torne um algoritmo de atualização.
Caso seja encontrado o item, ele faz a alteração para um novo valor.
Deve alterar apenas a primeira ocorrência do valor encontrado.
'''


def busca_binaria_alteracao(lista, item, novo_valor):
    pass


'''
EXERCÍCIO 3:
Implemente a função 'busca_linear_comparacoes', alterando o algoritmo de
busca linear para que a função retorne a quantidade de comparações realizadas
na tentativa de encontrar um determinado item.
'''


def busca_linear_comparacoes(lista, item):
    pass


'''
EXERCÍCIO 4:
Implemente a função 'busca_binaria_comparacoes', alterando o algoritmo de
busca binária para que a função retorne a quantidade de comparações realizadas
na tentativa de encontrar um determinado item.
'''


def busca_binaria_comparacoes(lista, item):
    pass


# TESTES DAS FUNÇÕES
try:
    lista = [1]
    busca_linear_alteracao(lista, 1, 50)
    assert lista == [50]
    lista = [1, 2, 3, 4, 5, 6]
    busca_linear_alteracao(lista, 4, 100)
    assert lista == [1, 2, 3, 100, 5, 6]
    lista = [1, 2, 3, 4, 5, 6]
    busca_linear_alteracao(lista, 10, 100)
    assert lista == [1, 2, 3, 4, 5, 6]
    lista = [1, 4, 3, 4, 5, 4]
    busca_linear_alteracao(lista, 4, 100)
    assert lista == [1, 100, 3, 4, 5, 4]
    print("CORRETO - Função busca_linear_alteracao")
except AssertionError:
    print("ERRADO  - Função busca_linear_alteracao")
except Exception:
    print("ERRADO  - Função busca_linear_alteracao")

try:
    lista = [1]
    busca_binaria_alteracao(lista, 1, 50)
    assert lista == [50]
    lista = [1, 2, 3, 4, 5, 6]
    busca_binaria_alteracao(lista, 4, 100)
    assert lista == [1, 2, 3, 100, 5, 6]
    lista = [1, 2, 3, 4, 5, 6]
    busca_binaria_alteracao(lista, 10, 100)
    assert lista == [1, 2, 3, 4, 5, 6]
    lista = [1, 3, 4, 4, 5, 5]
    busca_binaria_alteracao(lista, 4, 100)
    assert lista == [1, 3, 100, 4, 5, 5]
    print("CORRETO - Função busca_binaria_alteracao")
except AssertionError:
    print("ERRADO  - Função busca_binaria_alteracao")
except Exception:
    print("ERRADO  - Função busca_binaria_alteracao")

try:
    lista = [1, 4, 5, 7, 9, 11, 15, 20, 24, 30]
    cont = busca_linear_comparacoes(lista, 9)
    assert cont == 5
    cont = busca_linear_comparacoes(lista, 1)
    assert cont == 1
    cont = busca_linear_comparacoes(lista, 30)
    assert cont == 10
    cont = busca_linear_comparacoes(lista, 50)
    assert cont == 10
    print("CORRETO - Função busca_linear_comparacoes")
except AssertionError:
    print("ERRADO  - Função busca_linear_comparacoes")
except Exception:
    print("ERRADO  - Função busca_linear_comparacoes")

try:
    lista = [1, 4, 5, 7, 9, 11, 15, 20, 24, 30]
    cont = busca_binaria_comparacoes(lista, 9)
    assert cont == 1
    cont = busca_binaria_comparacoes(lista, 1)
    assert cont == 3
    cont = busca_binaria_comparacoes(lista, 30)
    assert cont == 4
    cont = busca_binaria_comparacoes(lista, 50)
    assert cont == 4
    print("CORRETO - Função busca_binaria_comparacoes")
except AssertionError:
    print("ERRADO  - Função busca_binaria_comparacoes")
except Exception:
    print("ERRADO  - Função busca_binaria_comparacoes")