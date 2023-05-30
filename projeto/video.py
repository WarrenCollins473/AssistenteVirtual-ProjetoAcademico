import webbrowser as wb

url = 'https://www.youtube.com/watch?v=r991SFQr9Nw'
mensagem = "É claro! Encontrei essa video aula:"

def atuar_sobre_video(acao, objeto, _):
    executado = False
    

    if acao == "abrir" and objeto == "vídeo":
        executado = True
        
        wb.open(url)
        print(mensagem)

    return executado