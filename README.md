# PIA_LPC062
Proyecto Integrador de Aprendizaje para la Materia de Laboratorio de Programacion para Ciberseguridad Grupo 062
 
Alumno: Leonardo Hasiel Alvarado Zamora

Matricula: 1949295

## Descripcion General Del Repositorio
¡Bienvenido! 

Este repositorio se dedica a ofrecer una pequeña pero concisa colección de scripts relacionados con la programación y la ciberseguridad. Aquí encontrarás una variedad de scripts acompañados de explicaciones claras que detallan su propósito y las tareas que cumplen para lograr su función específica.
Ya sea que estés interesado en desarrollar habilidades en programación o en fortalecer tus conocimientos en ciberseguridad, este repositorio te proporcionará una valiosa base de recursos.

Todo el contenido de este repositorio viene de lo visto en la clase de Laboratorio de Programacion de Ciberseguridad.
Te invitamos a sumergirte en este repositorio y aprovechar al máximo las explicaciones que acompañan a cada script. Estamos seguros de que encontrarás una amplia gama de scripts interesantes y útiles que te ayudarán a mejorar tus habilidades en programación y ciberseguridad.
¡Disfruta explorando los scripts y aprendiendo más sobre el fascinante mundo de la programación y la ciberseguridad!

**Este repositorio cuenta con las siguientes secciones:**
- [Scripting en PowerShell](#Scripting-en-PowerShell)
- [Scripting en Bash](#Scripting-en-Bash)
- [Webscraping](Webscraping)
- [Escáner de Puertos](#Escáner-de-Puertos)
- [Envio de Correos](#Envio-de-Correos)

## Scripting en PowerShell
PowerShell scripting es una forma eficiente y poderosa de automatizar tareas en entornos de Windows. Con PowerShell, puedes escribir secuencias de comandos (scripts) que ejecutan una serie de instrucciones para realizar acciones repetitivas o complejas de manera rápida y sencilla. Estos scripts te permiten administrar sistemas, configurar servidores, interactuar con servicios web y mucho más. Con su lenguaje intuitivo y su amplia gama de funciones integradas, PowerShell te brinda el poder de la automatización en tus manos, facilitando la administración y el control de tus entornos Windows.

A continuacion se mostraran y explicaran de manera breve algunos scripts escritos en PowerShell para realizar diferentes acciones.
### scan_portv1.ps1
Este script de PowerShell obtiene la puerta de enlace predeterminada, calcula el rango de la subred, solicita una dirección IP y realiza un escaneo de puertos para encontrar aquellos que están abiertos.

![imagen1](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/fa376550-2e4d-49c0-b11d-283e7a5f72b9)

Como funciona este script?

1. Obtiene la dirección de la puerta de enlace predeterminada (gateway) utilizando el comando `Get-NetRoute -DestinationPrefix 0.0.0.0/0`.
2. Determina el rango de la subred basado en la dirección de la puerta de enlace.
3. Muestra en la consola el valor del rango de la subred.
4. Define una lista de puertos a escanear.
5. Establece un tiempo de espera para la conexión a cada puerto.
6. Solicita al usuario que ingrese una dirección IP.
7. Itera sobre cada puerto en la lista de puertos a escanear.
8. Crea un objeto de cliente TCP (`TcpClient`) y trata de conectarlo a la dirección IP y puerto correspondientes utilizando `ConnectAsync`.
9. Espera un tiempo determinado (`$waittime`) para la conexión.
10. Si la conexión se realizó correctamente, muestra en la consola el mensaje "Puerto abierto: " y el número del puerto en color verde.

**El Script scan_portv1.ps1 original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_portv1.ps1](./Scripting%20en%20Powershell/scan_portv1.ps1)**


### scan_alive1.ps1
Este script obtiene la puerta de enlace predeterminada, calcula un rango de direcciones IP y realiza pruebas de conexión para determinar qué hosts están respondiendo dentro de ese rango de IP.

![imagen2](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/45f02320-cf2f-4568-9230-795a87377e31)

Como funciona este script?

1. Obtiene la puerta de enlace predeterminada (gateway) utilizando el comando `Get-NetRoute -DestinationPrefix 0.0.0.0/0` y la guarda en la variable `$subred`.
2. Calcula un rango de direcciones IP basado en el valor de `$subred` y lo guarda en la variable `$rango`.
3. Muestra en la consola el valor de la variable `$rango`.
4. Verifica si el rango de IP termina con un punto.
5. Crea un array llamado `$rango_ip` que contiene los números del 1 al 254.
6. Itera sobre cada número en el array `$rango_ip`.
7. Combina el rango de IP y el número actual para formar una dirección IP completa.
8. Realiza una prueba de conexión (`Test-Connection`) a la dirección IP actual con un recuento de 1 y en modo silencioso (`-Quiet`).
9. Si la respuesta de la prueba de conexión es verdadera, muestra en la consola "Host responde: " seguido de la dirección IP actual en color verde.

**El Script scan_alivev1.ps1 original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_alivev1,ps1](./Scripting%20en%20Powershell/scan_alivev1.ps1)**


### scan_alivev2.ps1
Este script determina la puerta de enlace predeterminada y el rango de subred correspondiente. Luego, escanea los hosts en esa subred y muestra aquellos que responden a las pruebas de conexión.

Como funciona este script?

1. Obtiene la puerta de enlace predeterminada (gateway) utilizando el comando `Get-NetRoute -DestinationPrefix 0.0.0.0/0` y guarda el valor en la variable `$subred`.
2. Muestra en la consola el valor de la puerta de enlace obtenido en el paso anterior, utilizando la variable `$subred`.
3. Calcula el rango de la subred a partir de la puerta de enlace, utilizando varias manipulaciones de cadenas de texto.
4. Muestra en la consola el valor del rango de subred obtenido en el paso anterior.
5. Crea un array llamado `$rango_ip` que contiene los números del 1 al 254.
6. Muestra en la consola "-- Subred actual:" para indicar que se está escaneando la subred actual.
7. Muestra en la consola el valor del rango de subred seguido de "0/24" en color rojo.
8. Itera sobre cada número en el array `$rango_ip`.
9. Combina el rango de subred y el número actual para formar una dirección IP completa.
10. Realiza una prueba de conexión (`Test-Connection`) a la dirección IP actual con un recuento de 1 y en modo silencioso (`-Quiet`).
11. Si la respuesta de la prueba de conexión es verdadera, muestra en la consola "Host responde:" seguido de la dirección IP actual en color verde.

**El Script scan_alivev1.ps1 original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_alivev2.ps2](./Scripting%20en%20Powershell/scan_alivev2.ps1)

Esto seria todo en la seccion de Scriptin en Powershell!

## Scripting en Bash

## Webscraping

## Escáner de Puertos

## Envio de Correos

