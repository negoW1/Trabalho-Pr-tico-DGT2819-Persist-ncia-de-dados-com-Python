"""
kdd.py
Versão FINAL: após a comparação de desempenho, foi escolhido o método
nativo sort() (o mais rápido). Lê o txt, quebra em palavras, ordena e
grava o glossário em um novo arquivo txt.
"""
ARQUIVO_ENTRADA = "documento.txt"
ARQUIVO_SAIDA = "glossario_ordenado.txt"

palavras = list()

with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        for palavra in linha.split():
            palavra = palavra.strip(".,;:!?()\"'").lower()
            if palavra:
                palavras.append(palavra)

palavras.sort()

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as saida:
    for palavra in palavras:
        saida.write(palavra + "\n")

print(f"{len(palavras)} palavras ordenadas e gravadas em '{ARQUIVO_SAIDA}'.")
