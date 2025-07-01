import os

caminho = os.path.join("Desktop", "floox-ai", "curso", "arquivo.txt")
print(caminho)
diretorio, arquivo = os.path.split(caminho)
print(diretorio)
print(arquivo)
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho)
print(caminho_arquivo, extensao_arquivo)

print(os.path.exists(caminho))