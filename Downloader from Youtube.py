from tkinter import font
from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

#Funções para Downloads
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

def download_video(dict):
    link = dict['video']
    path = dict['path']
    yt = YouTube(link)
    #Fazer o dowload
    ys = yt.streams.filter().first().download(path)
    sg.popup("Download Completo")

#I N T E R F A C E
def janela_inicio():
    #layout
    sg.theme('Topanga')
    layout = [
        [sg.Button('Música',size=(20,3),button_color=('#808000','#E6E6FA'))],
        [sg.Button('Playlist',size=(20,3),button_color=('#808000','#E6E6FA'))],
        [sg.Button('Vídeo',size=(20,3), button_color=('#808000','#E6E6FA'))]
    ]
    return sg.Window('Dowloader MP3 Music',layout=layout, font=("Cooper Black", 13), finalize=True)

def janela_musica():
    sg.theme('Topanga')
    layout = [
    [sg.Text('Digite o Link da música:', size=(24,0)), sg.Input(key = 'music', size=(45,0))], #input que retornara no dicionar com a key='link' e o valor que for digitado
    [sg.Text('Selecione a pasta:', size=(24,0)), sg.InputText('Default Folder',size = (35,0),key = 'path'), sg.FolderBrowse('Arquivo', button_color=('#808000','#E6E6FA'),font=("Cooper Black", 10),size = (7,0)),],
    [sg.Text( size=(24,1)),sg.Button('Baixar',font=("Cooper Black", 12), size=(20,1),button_color=('#808000','#E6E6FA'))]
    ]
    return sg.Window('Dowloader Music',layout=layout,font=("Courier New", 10), finalize=True)

def janela_playlist():
    sg.theme('Topanga')
    layout = [
    [sg.Text('Digite o Link da Playlist:', size=(24,0)), sg.Input(key = 'playlist', size=(45,0))], #input que retornara no dicionar com a key='link' e o valor que for digitado
    [sg.Text('Selecione a pasta:', size=(24,0)), sg.InputText('Default Folder',size = (35,0),key = 'path'), sg.FolderBrowse('Arquivo', button_color=('#808000','#E6E6FA'),font=("Cooper Black", 10),size = (7,0)),],
    [sg.Text( size=(24,1)),sg.Button('Baixar',font=("Cooper Black", 12), size=(20,1),button_color=('#808000','#E6E6FA'))]
    ]
    return sg.Window('Dowloader Playlist',layout=layout,font=("Courier New", 10), finalize=True)

def janela_video():
    sg.theme('Topanga')
    layout = [
    [sg.Text('Digite o Link do Vídeo:', size=(24,0)), sg.Input(key = 'video', size=(45,0))], 
    [sg.Text('Selecione a pasta:', size=(24,0)), sg.InputText('Default Folder',size = (35,0),key = 'path'), sg.FolderBrowse('Arquivo', button_color=('#808000','#E6E6FA'),font=("Cooper Black", 10),size = (7,0)),],
    [sg.Text( size=(24,1)),sg.Button('Baixar',font=("Cooper Black", 12), size=(20,1),button_color=('#808000','#E6E6FA'))]
    ]
    return sg.Window('Dowloader Vídeo',layout=layout,font=("Courier New", 10), finalize=True)

#Criar as janelas
janela,janelaMusic,janelaPlaylist,JanelaVideo = janela_inicio(),None,None,None

#ler as janelas
while True:
    window,event,values = sg.read_all_windows()

                #Controlar as interações do úsuario 

    #quando a janela principal for fechada
    if window == janela and event == sg.WIN_CLOSED:
        break
    #Quando clicar em Música:
    if window == janela and event == 'Música':
        janelaMusic = janela_musica()
        janela.hide()
    #Quando clicar em fechar a tela musica
    if window == janelaMusic and (event == sg.WIN_CLOSED or event == None):
        janelaMusic.hide()
        janela.un_hide()
    #Quando clicar em Baixar da tela Musica
    if window == janelaMusic and event =='Baixar':
        download_music(values)
        janelaMusic.hide()
        janela.un_hide()
    #Quando clicar em Playlist da tela principal
    if window == janela and event == 'Playlist':
        janelaPlaylist = janela_playlist()
        janela.hide()
    #Quando clicar em fechar da tela playlist
    if window == janelaPlaylist and event == sg.WIN_CLOSED:
        janelaPlaylist.hide()
        janela.un_hide()
    #Quando clicar em baixar da tela playlist
    if window == janelaPlaylist and event =='Baixar':
        download_playlist(values)
        janelaPlaylist.hide()
        janela.un_hide()
        #Quando clicar em video da tela principal
    if window == janela and event == 'Vídeo':
        JanelaVideo = janela_video()
        janela.hide()
    #Quando clicar em fechar da tela video
    if window == JanelaVideo and event == sg.WIN_CLOSED:
        JanelaVideo.hide()
        janela.un_hide()
    #Quando clicar em baixar da tela video
    if window == JanelaVideo and event =='Baixar':
        download_video(values)
        JanelaVideo.hide()
        janela.un_hide()