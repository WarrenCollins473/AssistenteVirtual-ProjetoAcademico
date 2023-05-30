import webbrowser as wb

url = "https://www.calculadoraonline.com.br/cientifica"
mensagem = "É claro! Abrindo a calculadora científica"

def atuar_sobre_calculadora(acao, objeto, _):
    executado = False
    

    if acao == "abrir" and objeto == "calculadora":
        executado = True
        
        wb.open(url)
        print(mensagem)

    return executado