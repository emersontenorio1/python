from PySimpleGUI import PySimpleGUI as sG


sG.theme('default')

layout = [
    [sG.Text('Usuário'), sG.Input(key='usuario')],
    [sG.Text('Senha'), sG.Input(key='senha', password_char='*')],
    [sG.Checkbox('Salvar o Login')],
    [sG.Button('Entrar')]
]
janela = sG.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sG.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'emerson' and valores['Senha'] == '123456':
            print('Bem vindo ao dev aprender')

