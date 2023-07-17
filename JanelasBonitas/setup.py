import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatarios):
    # Configurações do servidor SMTP do Gmail
    smtp_host = 'smtp-mail.outlook.com'
    smtp_port = 587
    smtp_username = 'emersontenorio1@hotmail.com'
    smtp_password = 'Ems#246813'

    # Informações do email
    sender = 'emersontenorio1@hotmail.com'
    subject = 'Assunto do email'
    message_text = 'Conteúdo do email'

    # Configurar a conexão SMTP
    smtp_server = smtplib.SMTP(smtp_host, smtp_port)
    smtp_server.starttls()
    smtp_server.login(smtp_username, smtp_password)
    print(destinatarios)
    for recipient in destinatarios:
        # Criar a mensagem
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(message_text, 'plain'))

        # Enviar o email
        smtp_server.sendmail(sender, recipient, message.as_string())

    # Encerrar a conexão SMTP
    smtp_server.quit()

    print("Emails enviados com sucesso!")

# Exemplo de uso da função
emails_destinatarios = ["emersontenorio1@hotmail.com", "emersontenorio1@gmail.com", "emersontenorio1@terra.com.br"]
enviar_email(emails_destinatarios)
