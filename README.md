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

***El Script scan_portv1.ps1 original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_portv1.ps1](./Scripting%20en%20Powershell/scan_portv1.ps1)***


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

***El Script scan_alivev1.ps1 original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_alivev1,ps1](./Scripting%20en%20Powershell/scan_alivev1.ps1)***


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

***El Script scan_alivev2.ps1 original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_alivev2.ps2](./Scripting%20en%20Powershell/scan_alivev2.ps1)***

Esto seria todo en la seccion de Scriptin en Powershell!

## Scripting en Bash
scripting en Bash se refiere a la creación y ejecución de secuencias de comandos o scripts utilizando el intérprete de comandos Bash en sistemas operativos Unix y Linux. Estos scripts permiten automatizar tareas y realizar acciones repetitivas de manera más eficiente. El lenguaje de scripting Bash ofrece una amplia gama de funciones y comandos que facilitan la manipulación de archivos, el procesamiento de texto, la gestión de procesos y muchas otras tareas comunes del sistema, tambien brinda la capacidad de escribir programas simples pero efectivos para mejorar la productividad y la automatización en entornos de línea de comandos.

A continuacion se mostraran y explicaran de manera breve algunos scripts escritos en Bash para realizar diferentes acciones.

### welcome.sh
Este script en bash tiene como objetivo mostrar un mensaje de bienvenida y proporcionar información sobre los usuarios conectados y sus procesos.

![imagen4](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/8aa662d7-2da9-4ff0-b02f-468277c97fea)

Como funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `echo “Hola ${LOGNAME}”`: Esta línea utiliza el comando `echo` para mostrar un saludo personalizado al usuario actual. La variable `${LOGNAME}` se sustituirá por el nombre de usuario actual.
3. `echo “Hoy es ${date}”`: Esta línea muestra la fecha actual utilizando el comando `date`. La variable `${date}` no es reconocida en bash, debería ser `${DATE}` para mostrar la fecha correcta.
4. `echo “Usuarios actuales conectados, y sus procesos:”`: Esta línea muestra un mensaje descriptivo.
5. `w`: Esta línea utiliza el comando `w` para mostrar una lista de los usuarios actuales conectados y sus procesos.

***El Script welcome.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [welcome.sh](./Scripting%20en%20Bash/welcome.sh)***

### bro.sh
Este script en bash tiene como objetivo solicitar al usuario que ingrese su nombre y luego muestra un mensaje de saludo personalizado.

![imagen5](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/e76c6e7a-bdc0-416e-a957-4a998a66a0a5)

Como funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `read -p “Escribe tu nombre:“ nombre`: Esta línea utiliza el comando `read` para leer la entrada del usuario y asignarla a la variable `nombre`. El texto "Escribe tu nombre:" se muestra como un mensaje de solicitud antes de que el usuario ingrese su nombre.
3. `echo “Hola, $nombre. Seamos amigos!”`: Esta línea utiliza el comando `echo` para mostrar un mensaje de saludo personalizado que incluye el nombre ingresado por el usuario. La variable `$nombre` se sustituirá por el valor que el usuario proporcionó durante la ejecución del script.

***El Script bro.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [welcome.sh](./Scripting%20en%20Bash/bro.sh)***

### number.sh
Este script en bash tiene como objetivo solicitar al usuario que ingrese tres números y luego muestra los números proporcionados.

![imagen6](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/ed2cc5c3-9201-421f-94b8-3cd36533b0fc)

Como funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `# Script number.sh`: Esta línea es un comentario que proporciona información sobre el nombre y el propósito del script.
3. `read -p “Proporciona un numero para variable 1:“ n1`: Estas líneas utilizan el comando `read` para leer la entrada del usuario y asignarla a las variables `n1`, `n2` y `n3`. Los mensajes entre comillas después de `-p` se muestran como mensajes de solicitud antes de que el usuario ingrese cada número.
4. `# Despliega los 3 numeros proporcionados por el usuario`: Esta línea es un comentario que describe la siguiente sección del script.
5. `echo “Numero 1 - $n1”`: Esta línea utiliza el comando `echo` para mostrar el valor de la variable `n1`, que es el primer número proporcionado por el usuario.
6. `echo “Numero 2 - $n2”`: Esta línea utiliza el comando `echo` para mostrar el valor de la variable `n2`, que es el segundo número proporcionado por el usuario.
7. `echo “Numero 3 - $n3”`: Esta línea utiliza el comando `echo` para mostrar el valor de la variable `n3`, que es el tercer número proporcionado por el usuario.

***El Script number.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [welcome.sh](./Scripting%20en%20Bash/number.sh)***

### netdiscover.sh

![imagen7](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/a90cc957-7b1e-47c4-a50b-b3fb27579ea4)

### portscanv1.sh

![imagen8](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/a0a6f814-778d-41b2-921e-edd599477781)

### superscan.sh

![imagen9](

## Webscraping

## Escáner de Puertos

## Envio de Correos

