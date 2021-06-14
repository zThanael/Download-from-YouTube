from tkinter import font
from PySimpleGUI import PySimpleGUI as sg

def janela_musica():
    sg.theme('Topanga')
    layout = [
    [sg.Text('Digite o Link da música:', size=(24,0)), sg.Input(key = 'music', size=(45,0))], #input que retornara no dicionar com a key='link' e o valor que for digitado
    [sg.Text('Selecione a pasta:', size=(24,0)), sg.InputText('Default Folder',size = (35,0),key = 'path'), sg.FolderBrowse('Arquivo', button_color=('#808000','#E6E6FA'),font=("Cooper Black", 10),size = (7,0)),],
    [sg.Text( size=(24,1)),sg.Button('Baixar',font=("Cooper Black", 12), size=(20,1),button_color=('#808000','#E6E6FA'))]
    ]
    return sg.Window('Dowloader Music',layout=layout,font=("Courier New", 10), finalize=True)
# sg.theme_previewer()
janela = janela_musica()
while True:
    event,values = janela.read()

    if event == sg.WIN_CLOSED:
        break