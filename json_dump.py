import json

filmes = [
    {"titulo": "Como Treinar o Seu Dragão", "ano": 2010, "genero": "Animação"},
    {"titulo": "Guardiões da Galáxia", "ano": 2014, "genero": "Ação/Ficção Científica"},
    {"titulo": "Forrest Gump", "ano": 1994, "genero": "Drama"},
    {"titulo": "Alerta Vermelho", "ano": 2021, "genero": "Ação/Comédia"}
]

with open("filmes.json", "w", encoding="utf-8") as f:
    json.dump(filmes, f, ensure_ascii=False, indent=4)