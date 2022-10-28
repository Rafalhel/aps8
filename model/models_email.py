import time

from models_api import enviar_email, checar_dia, deletar_arquivo, checar_arquivo, criar_arquivo
from models import ConectandoBD

while True:
    bd = ConectandoBD()
    listaEmail = bd.obterListaDeEmail()
    if checar_dia() and checar_arquivo():
        for email in listaEmail:
            enviar_email(email[1])
            print(f'Email enviado para {email[1]}')
        time.sleep(5)
        deletar_arquivo()
    elif checar_dia() == False:
        criar_arquivo()
        time.sleep(60)