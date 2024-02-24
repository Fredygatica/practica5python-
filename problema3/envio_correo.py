import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo(destinatario, asunto, cuerpo):
    # Configurar servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Credenciales de correo electrónico
    username = 'tucorreo@gmail.com'
    password = 'tupassword'

    # Iniciar sesión y enviar correo
    server.login(username, password)

    # Crear mensaje
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Adjuntar cuerpo del correo
    msg.attach(MIMEText(cuerpo, 'plain'))

    # Enviar correo
    server.send_message(msg)

    # Cerrar conexión
    server.quit()