from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
import moviepy.editor as mp
import re
import os

def downloadMP3(dict):
    link = dict['link']
    path = dict['path']
    yt = YouTube(link)
    #Fazer o dowload
    ys = yt.streams.filter(only_audio=True).first().download(path)
    #Converter o video(mp4) para mp3
    for file in os.listdir(path):                  #For para percorrer dentro da pasta passada anteriormente
        if re.search('mp4', file):                 #If verificando se o arquivo e .MP4                    
            mp4_path = os.path.join(path , file)   #Cria uma variavel para armazenar o arquivo .MP4
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') #Variavel que cria o nome do arquivo e adiciona .MP3 ao final
            new_file = mp.AudioFileClip(mp4_path)  #Cria o arquivo de áudio (.MP3)
            new_file.write_audiofile(mp3_path)     #Renomeia o arquivo, setando o nome criado anteriormente
            os.remove(mp4_path)                    #Remove o arquivo .MP4

#Layout
def janela_cliente():
    sg.theme('Reddit')
    layout = [
    [sg.Text('Digite o Link da musica:', size=(18,0)), sg.Input(key = 'link', size=(50,0))], #input que retornara no dicionar com a key='link' e o valor que for digitado
    [sg.Text('Selecione a pasta:', size=(18,0)), sg.InputText('Default Folder',size = (40,0),key = 'path'), sg.FolderBrowse('Arquivo', size = (7,0))],
    [sg.Button('Baixar', size=(20,0),)]
    ]
    return sg.Window('Downloader MP3 Music',layout=layout, finalize=True)
#criar as janelas
janela = janela_cliente()
#ler os eventos
while True:
    event,values = janela.Read()
    #quando a janela for fechada
    if event == sg.WIN_CLOSED:
        break
    if event == 'Baixar':
        downloadMP3(values)
        sg.popup("Download Completo")
        break
