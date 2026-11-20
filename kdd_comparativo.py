"""
kdd_comparativo.py
Versão de MEDIÇÃO: lê o txt, quebra em palavras e compara o tempo de
Bubble Sort, Selection Sort e do método nativo sort().
"""
import time

ARQUIVO_ENTRADA = "documento.txt"


def ler_palavras(caminho):
    """Lê o arquivo linha a linha e devolve uma lista com todas as palavras."""
    palavras = list()
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            for palavra in linha.split():
                # remove pontuação das pontas e padroniza em minúsculas
                palavra = palavra.strip(".,;:!?()\"'").lower()
                if palavra:
                    palavras.append(palavra)
    return palavras


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                a = array[j]
                array[j] = array[j + 1]
                array[j + 1] = a


def selection_sort(array):
    for i in range(len(array)):
        menor = i
        for j in range(i + 1, len(array)):
            if array[menor] > array[j]:
                menor = j
        array[i], array[menor] = array[menor], array[i]


def medir(nome, funcao, palavras):
    copia = palavras.copy()  # cada método recebe a mesma lista desordenada
    inicio = time.time()
    funcao(copia)
    fim = time.time()
    tempo = fim - inicio
    print(f"\n=== {nome} ===")
    print(f"Tempo de execução: {tempo:.6f} segundos")
    print(f"Primeiras 15 palavras: {copia[:15]}")
    return tempo


if __name__ == "__main__":
    palavras = ler_palavras(ARQUIVO_ENTRADA)
    print(f"Total de palavras lidas: {len(palavras)}")

    resultados = {
        "Bubble Sort": medir("Bubble Sort", bubble_sort, palavras),
        "Selection Sort": medir("Selection Sort", selection_sort, palavras),
        "sort() nativo": medir("sort() nativo", lambda l: l.sort(), palavras),
    }

    print("\n=== Comparativo (do mais rápido ao mais lento) ===")
    for nome, tempo in sorted(resultados.items(), key=lambda x: x[1]):
        print(f"{nome:<16} {tempo:.6f} s")
