import json

with open("filmes.json", "r", encoding="utf-8") as f:
    filmes_carregados = json.load(f)

for filme in filmes_carregados:
    print(f"Título: {filme['titulo']} | Ano: {filme['ano']} | Gênero: {filme['genero']}")