#Script de Envio de Correos
#Leonardo Hasie Alvarado Zamora - 1949295
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# Datos del remitente
remitente = "correo@gmail.com"
password = "contraseña"

# Datos del destinatario
destinatario = "destinatario@uanl.edu.mx"

# Creación del mensaje
mensaje = MIMEMultipart("related")
mensaje["Subject"] = "Prueba de envio (script Python) - (Matricula)"
mensaje["From"] = remitente
mensaje["To"] = destinatario

# Cuerpo del mensaje
cuerpo = MIMEText("""
    <html>
      <body>
        <p><b><font size="5">Practica 12</font></b></p>
        <p><font size="4">Ejercicio de la practica 12 para envío de correos</font></p>
        <p><b><font size="4">Alumno:</font></b> (Nombre)</p>
        <p><b><font size="4">Matricula:</font></b> (Matricula)</p>
        <img src="cid:fcfm_cool">
      </body>
    </html>
""", "html")

mensaje.attach(cuerpo)

# Adjuntar imagen
with open("fcfm_cool.png", "rb") as archivo:
    imagen = MIMEImage(archivo.read())
    imagen.add_header("Content-ID", "<fcfm_cool>")
    mensaje.attach(imagen)

# Conexión al servidor de correo
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(remitente, password)

# Envío del mensaje
server.sendmail(remitente, destinatario, mensaje.as_string())
print("Mensaje enviado con éxito")

# Cerrar conexión con el servidor
server.quit()
