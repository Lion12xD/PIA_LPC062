# Scripting en Bash
scripting en Bash se refiere a la creación y ejecución de secuencias de comandos o scripts utilizando el intérprete de comandos Bash en sistemas operativos Unix y Linux. Estos scripts permiten automatizar tareas y realizar acciones repetitivas de manera más eficiente. El lenguaje de scripting Bash ofrece una amplia gama de funciones y comandos que facilitan la manipulación de archivos, el procesamiento de texto, la gestión de procesos y muchas otras tareas comunes del sistema, tambien brinda la capacidad de escribir programas simples pero efectivos para mejorar la productividad y la automatización en entornos de línea de comandos.

A continuacion se mostraran y explicaran de manera breve algunos scripts escritos en Bash para realizar diferentes acciones.

## welcome.sh
Este script en bash tiene como objetivo mostrar un mensaje de bienvenida y proporcionar información sobre los usuarios conectados y sus procesos.

![imagen4](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/8aa662d7-2da9-4ff0-b02f-468277c97fea)

Como funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `echo “Hola ${LOGNAME}”`: Esta línea utiliza el comando `echo` para mostrar un saludo personalizado al usuario actual. La variable `${LOGNAME}` se sustituirá por el nombre de usuario actual.
3. `echo “Hoy es ${date}”`: Esta línea muestra la fecha actual utilizando el comando `date`. La variable `${date}` no es reconocida en bash, debería ser `${DATE}` para mostrar la fecha correcta.
4. `echo “Usuarios actuales conectados, y sus procesos:”`: Esta línea muestra un mensaje descriptivo.
5. `w`: Esta línea utiliza el comando `w` para mostrar una lista de los usuarios actuales conectados y sus procesos.

***El Script welcome.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [welcome.sh](./welcome.sh)***



## bro.sh
Este script en bash tiene como objetivo solicitar al usuario que ingrese su nombre y luego muestra un mensaje de saludo personalizado.

![imagen5](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/e76c6e7a-bdc0-416e-a957-4a998a66a0a5)

¿Cómo funciona este script?

1. `#!/bin/bash`: Esta línea es llamada "shebang" y se utiliza para indicar que el script debe ser interpretado por el intérprete de bash.
2. `read -p “Escribe tu nombre:“ nombre`: Esta línea utiliza el comando `read` para leer la entrada del usuario y asignarla a la variable `nombre`. El texto "Escribe tu nombre:" se muestra como un mensaje de solicitud antes de que el usuario ingrese su nombre.
3. `echo “Hola, $nombre. Seamos amigos!”`: Esta línea utiliza el comando `echo` para mostrar un mensaje de saludo personalizado que incluye el nombre ingresado por el usuario. La variable `$nombre` se sustituirá por el valor que el usuario proporcionó durante la ejecución del script.

***El Script bro.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [bro.sh](./bro.sh)***



## number.sh
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

***El Script number.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [number.sh](./number.sh)***



## netdiscover.sh
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

***El Script netdiscover.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [netdiscover.sh](./netdiscover.sh)***



## portscanv1.sh
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

***El Script portscanv1.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [portscanv1.sh](./portscanv1.sh)***



## superscan.sh
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

***El Script superscan.sh original se enccuentra en este repositorio, para verlo puedes dar click aqui: [superscan.sh](./superscan.sh)***



Esto seria todo en la seccion de Scripting en Bash!
