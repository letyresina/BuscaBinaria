lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def buscaBinaria(array, x, low, high): # low -> mais esquerda // right -> mais a direita
    while low <= high:
        # pra funcionar a busca binaria a lista tem que estar ordenada do low (menor) para maior (high)
        mid = (high + low) // 2 
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Função
def buscaLinear(lista, numero):
    '''
        Função criada para buscar o número presene da lista através do valor informado pelo usuário
    '''
    for i in range(len(lista)):
        if lista[i] == numero:
            print(f"O indíce do número {numero} nessa lista é de {i}")