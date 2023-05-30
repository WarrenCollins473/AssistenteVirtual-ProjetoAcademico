import webbrowser as wb

url = 'https://mundoeducacao.uol.com.br/matematica/desvio-padrao.htm#:~:text=A%20f%C3%B3rmula%20para,elementos%20do%20conjunto.'
mensagem = "É claro! Aqui está informações sobre como calcular o desvio padrão"

def atuar_sobre_desvio(acao, objeto, _):
    executado = False
    

    if acao == "calcular" and objeto == "desvio":
        executado = True
        
        wb.open(url)
        print(mensagem)
       
        return executado