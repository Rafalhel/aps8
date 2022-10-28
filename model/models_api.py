import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

import requests



def buscar_dados():
    request = requests.get("http://servicodados.ibge.gov.br/api/v2/metadados/pesquisas")
    dados = json.loads(request.content)

    assunto = dados[0]['classificacoes_tematicas'][0]['nome']
    corpo = dados[0]['classificacoes_tematicas'][0]['descricao']
    return assunto, corpo

def enviar_email(destinatario):
    email = 'meioambienteapsccinfo@gmail.com'
    senha = 'nkabyhhjazaubwhi'
    host = 'smtp.gmail.com'
    porta = '465'

    serverEmail = smtplib.SMTP_SSL(host, porta)
    serverEmail.login(email, senha)

    email_msd = MIMEMultipart()

    corpo = buscar_dados()[1]
    email_msd['subject'] = f'Curiosidades sobre o Meio Ambiente'

    email_msd['From'] = email
    email_msd['To'] = destinatario

    email_msd.attach(MIMEText(corpo, 'html'))

    serverEmail.sendmail(email_msd['From'], email_msd['To'], email_msd.as_string())

    serverEmail.quit()

def checar_dia():
    import datetime
    dia = datetime.datetime.today().weekday()
    hora = datetime.datetime.today().hour
    if dia == 4 and hora >= 8:
        return True
    else:
        return False

def checar_arquivo():
    if os.path.isfile('enviarEmail'):
        return True
    else:
        return False

def criar_arquivo():
    if not os.path.isfile('enviarEmail'):
        arquivo = open("enviarEmail", "w")
        arquivo.close()

def deletar_arquivo():
    os.remove("enviarEmail")
