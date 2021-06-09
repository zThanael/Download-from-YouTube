from tkinter import font
from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

def download_music(dict):
    link = dict['music']
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
    sg.popup("Download Completo")

def download_playlist(dict):
    link = dict['playlist']
    path = dict['path']

    playlist = Playlist(link)
    for indice, video in enumerate(playlist.videos):
        print(f'Baixando vídeo {indice + 1}/{len(playlist)}')
        video.streams.filter(only_audio=True).first().download(path)
    
    for file in os.listdir(path):                  #For para percorrer dentro da pasta passada anteriormente
        if re.search('mp4', file):                 #If verificando se o arquivo e .MP4                    
            mp4_path = os.path.join(path , file)   #Cria uma variavel para armazenar o arquivo .MP4
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') #Variavel que cria o nome do arquivo e adiciona .MP3 ao final
            new_file = mp.AudioFileClip(mp4_path)  #Cria o arquivo de áudio (.MP3)
            new_file.write_audiofile(mp3_path)     #Renomeia o arquivo, setando o nome criado anteriormente
            os.remove(mp4_path)                    #Remove o arquivo .MP4
    sg.popup("Download Completo")

def janela_inicio():
    #layout
    sg.theme('DarkGreen3')
    layout = [
        [sg.Button('Música',size=(20,3), button_color=(sg.theme_button_color('red'))), 
        sg.Button('Playlist',size=(20,3),button_color=(sg.theme_button_color('red')))],
    ]
    return sg.Window('Dowloader MP3 Music',layout=layout, font=("Cooper Black", 13), finalize=True)

def janela_musica():
    sg.theme('DarkGreen3')
    layout = [
    [sg.Text('Digite o Link da música:', size=(18,0)), sg.Input(key = 'music', size=(50,0))], #input que retornara no dicionar com a key='link' e o valor que for digitado
    [sg.Text('Selecione a pasta:', size=(18,0)), sg.InputText('Default Folder',size = (40,0),key = 'path'), sg.FolderBrowse('Arquivo', size = (7,0))],
    [sg.Text( size=(20,1)),sg.Button('Baixar', size=(20,1))]
    ]
    return sg.Window('Dowloader Music',layout=layout, finalize=True)

def janela_playlist():
    sg.theme('DarkGreen3')
    layout = [
    [sg.Text('Digite o Link da Playlist:', size=(18,0)), sg.Input(key = 'playlist', size=(50,0))], #input que retornara no dicionar com a key='link' e o valor que for digitado
    [sg.Text('Selecione a pasta:', size=(18,0)), sg.InputText('Default Folder',size = (40,0),key = 'path'), sg.FolderBrowse('Arquivo', size = (7,0))],
    [sg.Text( size=(20,1)),sg.Button('Baixar', size=(20,1))]
    ]
    return sg.Window('Dowloader Playlist',layout=layout, finalize=True)

#criar as janelas
janela1,janela2,janela3 = janela_inicio(),None,None

#ler as janelas
while True:
    window,event,values = sg.read_all_windows()

                #Controlar as interações do úsuario 

    #quando a janela principal for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #Quando clicar em Música:
    if window == janela1 and event == 'Música':
        janela2 = janela_musica()
        janela1.hide()
    #Quando clicar em fechar a tela musica
    if window == janela2 and (event == sg.WIN_CLOSED or event == None):
        janela2.hide()
        janela1.un_hide()
    #Quando clicar em Baixar da tela Musica
    if window == janela2 and event =='Baixar':
        download_music(values)
        janela2.hide()
        janela1.un_hide()
    #Quando clicar em Playlist da tela principal
    if window == janela1 and event == 'Playlist':
        janela3 = janela_playlist()
        janela1.hide()
    #Quando clicar em fechar da tela playlist
    if window == janela3 and event == sg.WIN_CLOSED:
        janela3.hide()
        janela1.un_hide()
    #Quando clicar em baixar da tela playlist
    if window == janela3 and event =='Baixar':
        download_playlist(values)
        janela3.hide()
        janela1.un_hide()