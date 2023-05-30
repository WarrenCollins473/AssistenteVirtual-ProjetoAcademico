import webbrowser as wb

url = "https://www.todamateria.com.br/media/#:~:text=M%C3%A9dia%20Aritm%C3%A9tica%20Simples,2%2C...%2Cxn%3A%20valores%20dos%20dados"
mensagem = "É claro! Aqui está informações sobre como calcular médias"

def atuar_sobre_medias(acao, objeto, _):
    executado = False
    

    if acao == "calcular" and objeto == "médias":
        executado = True
        
        wb.open(url)
        print(mensagem)

    return executado