import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(user_name, user_surname, user_tel, user_email, selected_option, message):
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    # Este es el correo que se ocupa de enviar los correos!!!
    smtp_user = 'iturritek.correo@hotmail.com'
    smtp_password = 'correoIturritek'

    subject = 'Nueva peticion desde iturritek'
    email_body = f'Nuevo formulario enviado con los siguientes datos:\n\n'
    email_body += f'Nombre: {user_name}\n'
    email_body += f'Apellidos: {user_surname}\n'
    email_body += f'Teléfono: {user_tel}\n'
    email_body += f'Email: {user_email}\n'
    email_body += f'Servicio seleccionado: {selected_option}\n'
    email_body += f'Mensaje: {message}\n'

    sender = smtp_user
    # Este correo se envia a la direccion de la "empresa"
    recipients = ['iturritek.correo@hotmail.com']

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender, recipients, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f'Error al enviar el correo a iturritek: {str(e)}')
        return False
    
def enviar_correo_cliente(user_name, user_email):
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    smtp_user = 'iturritek.correo@hotmail.com'
    smtp_password = 'correoIturritek'

    subject = 'Confirmacion de recepcion de mensaje'
    email_body = f'Estimado/a  {user_name}\n\n'
    email_body += f'Le escribimos para confirmar la recepción de su correo electrónico. Apreciamos su contacto y nos pondremos en contacto con usted a la brevedad posible para abordar sus consultas o necesidades.\n\n'
    email_body += f'Gracias por considerarnos como su opción. Esperamos servirle pronto.\n\n'
    email_body += f'Atentamente Iturritek'

    sender = smtp_user
    recipients = [user_email]

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender, recipients, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f'Error al enviar el al usuario: {str(e)}')
        return False


