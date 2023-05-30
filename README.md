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

¿Cómo funciona este script?

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

¿Cómo funciona este script?

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

¿Cómo funciona este script?

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

¿Cómo funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `read -p “Escribe tu nombre:“ nombre`: Esta línea utiliza el comando `read` para leer la entrada del usuario y asignarla a la variable `nombre`. El texto "Escribe tu nombre:" se muestra como un mensaje de solicitud antes de que el usuario ingrese su nombre.
3. `echo “Hola, $nombre. Seamos amigos!”`: Esta línea utiliza el comando `echo` para mostrar un mensaje de saludo personalizado que incluye el nombre ingresado por el usuario. La variable `$nombre` se sustituirá por el valor que el usuario proporcionó durante la ejecución del script.

***El Script bro.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [bro.sh](./Scripting%20en%20Bash/bro.sh)***

### number.sh
Este script en bash tiene como objetivo solicitar al usuario que ingrese tres números y luego muestra los números proporcionados.

![imagen6](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/ed2cc5c3-9201-421f-94b8-3cd36533b0fc)

¿Cómo funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `# Script number.sh`: Esta línea es un comentario que proporciona información sobre el nombre y el propósito del script.
3. `read -p “Proporciona un numero para variable 1:“ n1`: Estas líneas utilizan el comando `read` para leer la entrada del usuario y asignarla a las variables `n1`, `n2` y `n3`. Los mensajes entre comillas después de `-p` se muestran como mensajes de solicitud antes de que el usuario ingrese cada número.
4. `# Despliega los 3 numeros proporcionados por el usuario`: Esta línea es un comentario que describe la siguiente sección del script.
5. `echo “Numero 1 - $n1”`: Esta línea utiliza el comando `echo` para mostrar el valor de la variable `n1`, que es el primer número proporcionado por el usuario.
6. `echo “Numero 2 - $n2”`: Esta línea utiliza el comando `echo` para mostrar el valor de la variable `n2`, que es el segundo número proporcionado por el usuario.
7. `echo “Numero 3 - $n3”`: Esta línea utiliza el comando `echo` para mostrar el valor de la variable `n3`, que es el tercer número proporcionado por el usuario.

***El Script number.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [number.sh](./Scripting%20en%20Bash/number.sh)***

### netdiscover.sh
Este script en bash es un escáner de red básico que determina el segmento de red y verifica la conectividad de los hosts en ese segmento.

![imagen7](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/a90cc957-7b1e-47c4-a50b-b3fb27579ea4)

¿Cómo funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `# Script netdiscover.sh`: Esta línea es un comentario que proporciona información sobre el nombre y el propósito del script.
3. `# Escaner de red basico en BASH`: Esta línea es un comentario que describe la funcionalidad general del script.
4. `if which ifconfig > /dev/null; then`: Esta línea verifica si el comando `ifconfig` está disponible en el sistema. Si está disponible, se ejecuta el bloque de código dentro de `if`. De lo contrario, se ejecuta el bloque de código dentro de `else`.
5. `echo "Comando ifconfig existe..."`: Esta línea muestra un mensaje indicando que el comando `ifconfig` existe en el sistema.
6. `direccion_ip=$(ifconfig | grep inet | grep -v "127.0.0.1" | awk '{print $2}')`: Esta línea utiliza el comando `ifconfig` junto con `grep` y `awk` para obtener la dirección IP del sistema.
7. `echo "Esta es tu direccion ip: $direccion_ip"`: Esta línea muestra la dirección IP obtenida del paso anterior.
8. `subred=$(ifconfig | grep inet | grep -v "127.0.0.1" | awk '{print $2}' | awk -F. '{print $1"."$2"."$3"."}')`: Esta línea utiliza el comando `ifconfig` junto con `grep` y `awk` para obtener el segmento de red al cual pertenece la dirección IP.
9. `echo "Esta es tu subred: $subred"`: Esta línea muestra el segmento de red obtenido del paso anterior.
10. `for ip in {1..254}; do`: Este bucle `for` itera desde 1 hasta 254, generando números que representan los últimos octetos de las direcciones IP dentro del segmento de red.
11. `if ping -q -c 4 "${subred}${ip}" > /dev/null; then`: Esta línea utiliza el comando `ping` para verificar la conectividad de cada dirección IP en el segmento de red. `-q` suprime la salida detallada de ping, `-c 4` especifica el número de intentos de ping, y `> /dev/null` redirige la salida a la nada.
12. `echo "Host responde: ${subred}${ip}"`: Esta línea muestra un mensaje indicando que un host en el segmento de red ha respondido al ping.

***El Script netdiscover.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [netdiscover.sh](./Scripting%20en%20Bash/netdiscover.sh)***

### portscanv1.sh
este script en bash realiza un escaneo de puertos en una dirección IP especificada utilizando un archivo especial en `/dev`. Verifica la disponibilidad de los puertos en la dirección IP y muestra un mensaje indicando si cada puerto está abierto o cerrado. Es un escáner de puertos básico que puede ayudar a identificar los servicios activos en una dirección IP específica.

![imagen8](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/a0a6f814-778d-41b2-921e-edd599477781)

¿Cómo funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `# Script portscanv1.sh`: Esta línea es un comentario que proporciona información sobre el nombre y el propósito del script.
3. `direccion_ip=$1`: Esta línea asigna el primer argumento pasado al script a la variable `direccion_ip`, que representa la dirección IP a escanear.
4. `puertos=(20 21 22 23 25 50 51 53 80 110 135 136 137 138 139 143 161 162 389 443 445 636 1025 1443 3389 5985 5986 8080 10000)`: Esta línea define un array llamado `puertos` que contiene los números de puerto a escanear.
5. `[ $# -eq 0 ] && { echo "Modo de uso: $0 <direccion ip>"; exit 1; }`: Esta línea verifica si no se ha proporcionado ningún argumento (es decir, la dirección IP). Si no se ha proporcionado, muestra un mensaje de uso y finaliza la ejecución del script.
6. `for port in "${puertos[@]}"; do`: Este bucle `for` itera sobre cada elemento del array `puertos`, asignando cada número de puerto a la variable `port`.
7. `timeout 1 bash -c "echo > /dev/tcp/$direccion_ip/$port" >/dev/null 2>&1 &&\`: Esta línea utiliza el comando `timeout` junto con `bash` para intentar establecer una conexión a través del protocolo TCP con la dirección IP y el puerto especificados. Si la conexión se establece correctamente dentro de 1 segundo, el resultado se redirige a `/dev/null`.
8. `echo "$direccion_ip:$port is open"`: Esta línea muestra un mensaje indicando que el puerto en la dirección IP está abierto, si la conexión se estableció correctamente.
9. `echo "$direccion_ip:$port is closed"`: Esta línea muestra un mensaje indicando que el puerto en la dirección IP está cerrado, si la conexión no se estableció correctamente.

***El Script portscanv1.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [portscanv1.sh](./Scripting%20en%20Bash/portscanv1.sh)***

### superscan.sh
Este script en bash muestra un menú con opciones numeradas al usuario y ejecuta diferentes scripts dependiendo de la opción seleccionada. Proporciona una forma interactiva para que el usuario elija entre diferentes acciones, como realizar un descubrimiento de red, escanear puertos, mostrar un mensaje de bienvenida o salir del programa.

![imagen9](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/ba2cab95-4f24-4db6-b7da-21c40b1646c3)

¿Cómo funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `date`: Esta línea muestra la fecha actual.
3. `echo "---------------------------"`: Estas líneas muestran líneas de separación para mejorar la presentación del menú.
4. `echo "   Menu Principal"`: Esta línea muestra el encabezado del menú principal.
5. `echo "---------------------------"`: Esta línea muestra una línea de separación después del encabezado del menú.
6. `echo "1. Net Discover"`: Esta línea muestra la primera opción del menú.
7. `echo "2. Port Scan"`: Esta línea muestra la segunda opción del menú.
8. `echo "3. Welcome"`: Esta línea muestra la tercera opción del menú.
9. `echo "4. Exit"`: Esta línea muestra la cuarta opción del menú.
10. `read -p "Opción  [ 1 - 4 ] " c`: Esta línea solicita al usuario que ingrese una opción del menú y almacena la entrada en la variable `c`.
11. `case $c in`: Esta línea inicia una estructura `case` que evalúa el valor de `c`.
12. `1) $HOME/netdiscover.sh;;`: Esta línea ejecuta el script `netdiscover.sh` ubicado en el directorio `$HOME` cuando el usuario selecciona la opción 1 del menú.
13. `2) $HOME/portscanv1.sh;;`: Esta línea ejecuta el script `portscanv1.sh` ubicado en el directorio `$HOME` cuando el usuario selecciona la opción 2 del menú.
14. `3) $HOME/welcome.sh;;`: Esta línea ejecuta el script `welcome.sh` ubicado en el directorio `$HOME` cuando el usuario selecciona la opción 3 del menú.
15. `4) echo "Bye!"; exit 0;;`: Esta línea muestra un mensaje de despedida y finaliza la ejecución del script cuando el usuario selecciona la opción 4 del menú.
16. `esac`: Esta línea marca el final de la estructura `case`.

***El Script superscan.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [superscan.sh](./Scripting%20en%20Bash/superscan.sh)***

## Webscraping
El webscraping es una técnica que permite extraer datos de manera automatizada desde sitios web. Consiste en desarrollar programas o scripts que recorren las páginas web, analizan su estructura y extraen la información relevante, como texto, imágenes o tablas. Esta práctica es ampliamente utilizada en diversas industrias para obtener datos en tiempo real, realizar análisis de mercado, monitorizar precios, recopilar información para investigación y muchas otras aplicaciones.

El webscraping se basa en enviar solicitudes HTTP a los servidores web, recibir las respuestas y extraer los datos deseados del código HTML. Para lograrlo, se utilizan diferentes herramientas y bibliotecas en diversos lenguajes de programación.

A continuacion se mostraran y explicaran de manera breve algunos scripts escritos en Python sobre webscraping.

### scrape_quote.py
El script en Python realiza una solicitud GET a una página web y utiliza BeautifulSoup para analizar el contenido HTML. Luego extrae las citas y los autores de la página, los imprime y los guarda en un archivo CSV.

![imagen10](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/5aaa3102-08d8-4d59-8224-fd88e2511acc)

¿Cómo funciona este script?

1. Importar bibliotecas: Se importan las bibliotecas necesarias para el script, incluyendo "requests" para realizar solicitudes HTTP, "csv" para trabajar con archivos CSV y "BeautifulSoup" para analizar el HTML.
2. Definir la URL: Se establece la dirección URL del sitio web que se desea escrapear.
3. Realizar una solicitud GET: Se utiliza la biblioteca "requests" para enviar una solicitud GET a la URL y obtener la respuesta del servidor. La respuesta se guarda en la variable "response".
4. Analizar el HTML: Se utiliza la biblioteca "BeautifulSoup" para analizar sintácticamente el HTML de la respuesta obtenida. Se crea un objeto "html" que representa la estructura del documento HTML.
5. Extraer citas: Mediante el uso de la función "find_all" de "BeautifulSoup", se buscan todos los elementos HTML que tienen la etiqueta "span" y la clase "text". Estos elementos representan las citas en el sitio web. Se guardan las citas en la lista "quotes".
6. Extraer autores: De manera similar al paso anterior, se buscan los elementos HTML que tienen la etiqueta "small" y la clase "author". Estos elementos representan los autores de las citas. Se guardan los autores en la lista "authors".
7. Imprimir citas y autores: Se utiliza un bucle "for" y la función "zip" para iterar sobre las listas de citas y autores al mismo tiempo. Se imprime cada par de cita y autor.
8. Escribir en un archivo CSV: Se abre un archivo CSV llamado "zitate.csv" en modo de escritura. Se utiliza el objeto "csv_writer" para escribir los datos en el archivo CSV. Se utiliza la función "writerows" y la función "zip" para combinar las listas de citas y autores en pares y escribirlos en el archivo CSV.

### scrap12.py

![imagen11](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/c7be0144-5736-46f9-9c27-402c8729d69d)

## Escáner de Puertos

## Envio de Correos

