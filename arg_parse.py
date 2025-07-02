from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-b", "--basic",
                    help="Mostra 'Olá mundo' na tela",
                    type=str, #tipo do argumento
                    metavar="STRING", 
                    #default="Olá Mundo", #valor padrão
                    required=False,
                    #nargs="+" #recebe mais de um valor
                    action="append")

parser.add_argument("-v", "--verbose",
                    help="Mostra logs",
                    type=str, #tipo do argumento
                    metavar="STRING", 
                    #default="Olá Mundo", #valor padrão
                    required=False,
                    #nargs="+" #recebe mais de um valor
                    action="store_true")
args = parser.parse_args()

if args.basic is None:
    print("Você não passou o valor de b/basic")
else:
    print("O valor de basic é: ", args.basic)