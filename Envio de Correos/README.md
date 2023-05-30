# Envio de Correos
El envío de correos (mediante scripts) se refiere a la capacidad de escribir programas o scripts en lenguajes de programación, como Python, que automatizan el proceso de envío de correos electrónicos. Estos scripts pueden incluir la configuración del servidor de correo saliente, la creación del mensaje de correo con su contenido, destinatarios, asunto y archivos adjuntos, y luego enviar el correo utilizando protocolos como SMTP (Simple Mail Transfer Protocol). Esto permite a los desarrolladores enviar correos electrónicos automáticamente desde sus aplicaciones o realizar tareas programadas, como enviar notificaciones por correo electrónico o informes automatizados, sin tener que hacerlo manualmente. El envío de correos mediante scripts simplifica y agiliza el proceso de comunicación por correo electrónico a través de la automatización.

A continuacion se mostraran y explicaran de manera breve un  script escrito en Python sobre Envio de Correos.

## enviocorreo.py
Este script en Python realiza el envío de un correo electrónico utilizando la biblioteca smtplib y las clases MIME (Multipurpose Internet Mail Extensions) para adjuntar un cuerpo de correo HTML y una imagen.

![imagen15](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/b4f9e075-0fcc-4864-9ba8-9fbce09ac487)

1. Importación de módulos:
   - Se importa el módulo smtplib para el manejo del protocolo SMTP.
   - Se importan las clases MIMEMultipart, MIMEImage y MIMEText del módulo email.mime para construir el mensaje de correo.

2. Definición de variables:
   - Se define la dirección de correo remitente en la variable "remitente".
   - Se especifica la contraseña del remitente en la variable "password".
   - Se indica la dirección de correo destinatario en la variable "destinatario".

3. Construcción del mensaje:
   - Se crea un objeto MIMEMultipart para el mensaje, indicando el tipo "related".
   - Se establecen los campos del mensaje como el asunto, remitente y destinatario.
   - Se crea el cuerpo del mensaje en formato HTML utilizando la clase MIMEText y se asigna a la variable "cuerpo".
   - Se adjunta el cuerpo al mensaje utilizando el método attach().
   - Se abre el archivo de imagen "fcfm_cool.png" en modo lectura binaria y se crea un objeto MIMEImage con su contenido.
   - Se asigna un identificador único a la imagen utilizando el encabezado "Content-ID".
   - Se adjunta la imagen al mensaje utilizando el método attach().

4. Configuración del servidor de correo:
   - Se crea un objeto SMTP con la dirección y puerto del servidor SMTP de Gmail.
   - Se inicia la conexión TLS utilizando starttls().
   - Se autentica en el servidor SMTP utilizando el método login() con el remitente y la contraseña.

5. Envío del correo:
   - Se utiliza el método sendmail() del servidor SMTP para enviar el mensaje.
   - Se especifica el remitente, destinatario y el mensaje convertido a cadena utilizando mensaje.as_string().

6. Finalización del programa:
   - Se imprime un mensaje indicando que el correo ha sido enviado con éxito.
   - Se cierra la conexión con el servidor SMTP utilizando quit().

***El Script enviocorreo.py original se enccuentra en este repositorio, para verlo puedes dar click aqui: [enviocorreo.py](./enviocorreo.py)***



Esto seria todo en la seccion de Envio de Correos!
