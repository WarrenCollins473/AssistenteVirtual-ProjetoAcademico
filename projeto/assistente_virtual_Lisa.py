import speech_recognition as sr
from nltk import word_tokenize, corpus
from Variancia import *
from calculadora import *
from medias import *
from desvio import *
from video import *
import json

IDIOMA_CORPUS = "portuguese"
IDIOMA_FALA = "pt-BR"
CAMINHO_CONFIGURACAO = "config.json"

ATUADORES = [
    {
        "nome":"variância",
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_variancia
    },
    {
        "nome":"calculadora",
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_calculadora
    },
    {
        "nome":"médias",
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_medias
    },
    {
        "nome":"desvio",
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_desvio
    },
    {
        "nome":"vídeo",
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_video
    }
]

def iniciar():

    iniciado = False

    reconhecedor = sr.Recognizer()
 
    palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))   
    with open(CAMINHO_CONFIGURACAO, "r", encoding= "utf-8") as arquivo_de_configuracao:
        configuracao = json.load(arquivo_de_configuracao)

        nome_do_assistente = configuracao["nome"]
        acoes = configuracao["acoes"]

        arquivo_de_configuracao.close()

    iniciado = True

    print("Olá! Sou sua assistente virtual, LISA")

    return iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes

def escutar_fala(reconhecedor):
    tem_fala = False

    with sr.Microphone() as fonte_de_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_de_audio)

        print("Como posso te ajudar?")
      
        fala = reconhecedor.listen(fonte_de_audio, timeout = 20)
        tem_fala = True

    return tem_fala, fala

def processar_audio_da_fala(audio_da_fala, reconhecedor):

    tem_fala = False
    with sr.AudioFile(audio_da_fala) as fonte_audio:

        fala = reconhecedor.listen(fonte_audio)
        tem_fala = True

    return tem_fala, fala
           


def transcrever_fala(fala, reconhecedor):
    tem_transcricao = False
    
    transcricao = reconhecedor.recognize_google(fala, language=IDIOMA_FALA)
    tem_transcricao = True
   
    return tem_transcricao, transcricao.lower()

def tokenizar_transcricao(transcricao):
    return word_tokenize(transcricao)

def eliminar_palavras_de_parada(tokens, palavras_de_parada):
    tokens_filtrados = []
    
    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados

def validar_comando(tokens, nome_do_assistente, acoes):
    valido, acao, objeto = False, None, None

    if len(tokens) >= 3:
        if nome_do_assistente == tokens[0]:
            acao = tokens[1]
            objeto = tokens[2]

        for acao_cadastrada in acoes:
            if acao == acao_cadastrada["nome"]:
                if objeto in acao_cadastrada["objetos"]:
                    valido = True

                    break

    return valido, acao, objeto

def executar_comando(acao, objeto):
    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["parametro_de_atuacao"]
        atuou = atuador["atuar"](acao, objeto, parametro_de_atuacao)

        if atuou:
            break

if __name__ == "__main__":
    iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()

    if iniciado:
        while True:
            tem_fala, fala = escutar_fala(reconhecedor)
            if tem_fala:
                tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
                if tem_transcricao:
                    tokens = tokenizar_transcricao(transcricao)
                    tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)

                    valido, acao, objeto = validar_comando(tokens, nome_do_assistente, acoes)
                    if valido:
                        executar_comando(acao, objeto)
                    else:
                        print("Não conheço esse comando, por favor tente novamente!")
