from string import Template
from datetime import datetime
#ficou mt top

template = Template("""
🎬 Convite Especial 🎬

Olá, $nome!

Você está convidado para a nossa noite de cinema com o filme:
"$filme" ($ano)

📍 Local: $local
🕒 Horário: $horario
📅 Data: $data

Prepare a pipoca e venha curtir com a gente! 🍿

Atenciosamente,
Equipe CineClub
""")

dados = {
    "nome": "Felipe",
    "filme": "Como Treinar o Seu Dragão",
    "ano": 2010,
    "local": "CineSystem - Sala 3",
    "horario": "19:30",
    "data": datetime.now().strftime("%d/%m/%Y")
}

convite = template.substitute(dados)
print(convite)