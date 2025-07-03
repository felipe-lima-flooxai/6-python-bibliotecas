import PyPDF2

#modulo maneirinho, só é meio chato o assunto. Diverchato.
#ler pdf
def ler_pdf(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as arquivo_pdf:
            leitor = PyPDF2.PdfReader(arquivo_pdf)
            total_paginas = len(leitor.pages)
            print(f'Total de páginas: {total_paginas}')

            for i, pagina in enumerate(leitor.pages):
                texto = pagina.extract_text()
                print(f'\n-Página {i + 1}-')
                if texto:
                    print(texto.strip())
                else:
                    print('Sem texto na página')
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except Exception:
        print(f'Erro ao ler o PDF: {Exception}')

#combinar/mesclar pdfs
def mesclar_pdfs(lista_arquivos, arquivo_saida):
    mesclador = PyPDF2.PdfMerger()
    try:
        for arquivo in lista_arquivos:
            mesclador.append(arquivo)
        mesclador.write(arquivo_saida)
        print(f'PDFs mesclados com sucesso em "{arquivo_saida}".')
    except Exception:
        print(f'Erro ao mesclar PDFs: {Exception}')
    finally:
        mesclador.close()


if __name__ == '__main__':

    ler_pdf('entrada.pdf')


    arquivos_para_mesclar = ['entrada.pdf', 'outro.pdf']
    mesclar_pdfs(arquivos_para_mesclar, 'resultado.pdf')
