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
    
array = [3, 4, 5, 6, 7, 8, 9]
x = 4
resultado = buscaBinaria(array, x, 0, len(array)-1)

if resultado != -1:
    print(f"Elemento presente no index {resultado}")
else:
    print("Elemento não encontrado")