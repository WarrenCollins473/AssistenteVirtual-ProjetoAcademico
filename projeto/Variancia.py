import webbrowser as wb

url = 'https://www.todamateria.com.br/variancia-e-desvio-padrao/#:~:text=Para%20calcular%20a,n%C3%BAmero%20de%20dados.'
mensagem = "É claro! Aqui está informações sobre como calcular a Variância"

def atuar_sobre_variancia(acao, objeto, _):
    executado = False
    

    if acao == "calcular" and objeto == "variância":
        executado = True
        
        wb.open(url)
        print(mensagem)
       
    return executado