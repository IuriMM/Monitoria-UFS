def ler_arquivo(matriz,tamanho_matriz):
    for i in range(tamanho_matriz):
        linha = input().replace(" ", "").strip()
        matriz.append([int(valor) for valor in linha[:tamanho_matriz]])

def verificar_caminho(vertice_inicial_i, vertice_inicial_j, matriz, tamanho_matriz):

    if vertice_inicial_i < 0 or vertice_inicial_j < 0:
        return False

    if vertice_inicial_i >= tamanho_matriz or vertice_inicial_j >= tamanho_matriz:
        return False

    if matriz[vertice_inicial_i][vertice_inicial_j] == 0:
        return False

    if vertice_inicial_i == tamanho_matriz - 1 and vertice_inicial_j == tamanho_matriz - 1:
        return True

    matriz[vertice_inicial_i][vertice_inicial_j] = '0'

    if verificar_caminho(vertice_inicial_i + 1, vertice_inicial_j, matriz, tamanho_matriz):
        return True

    if verificar_caminho(vertice_inicial_i, vertice_inicial_j + 1, matriz, tamanho_matriz):
        return True

    return False

tamanho_matriz = int(input())
matriz = []
ler_arquivo(matriz, tamanho_matriz)
print(verificar_caminho(0, 0, matriz, tamanho_matriz))
