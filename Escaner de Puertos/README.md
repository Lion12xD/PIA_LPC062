# Escáner de Puertos
El escaneo de puertos es un proceso que se utiliza para identificar los puertos abiertos en un dispositivo o en una red. Cada dispositivo tiene múltiples puertos, que son puntos de conexión utilizados para la comunicación de datos. Al realizar un escaneo de puertos, se envían solicitudes a cada puerto para determinar si está abierto o cerrado. Esto proporciona información sobre los servicios o aplicaciones que están disponibles y escuchando en esos puertos. El escaneo de puertos es una técnica utilizada tanto por administradores de redes para detectar vulnerabilidades en la seguridad, como por piratas informáticos para buscar posibles puntos de acceso y explotarlos.

A continuacion se mostraran y explicaran de manera breve algunos scripts escritos en Python sobre Escaner de Puertos.

## scan_portv1.py
El script realiza un escaneo de puertos en un rango especificado para determinar los puertos abiertos en un host dado.

![imagen12](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/7d1b9d2a-1047-4fc7-ab62-718586790873)


1. Importación de librerías: Se importan las librerías necesarias, como `sys` y `socket`, que se utilizarán en el script.
2. Modo de ejecución del script: Se establece el modo de ejecución del script, que requiere dos argumentos: el host y el rango de puertos. Estos argumentos se obtienen de `sys.argv` y se guardan en variables correspondientes.
3. Definición de los valores de inicio y fin del rango de puertos: Los valores del rango de puertos se obtienen del segundo argumento y se asignan a las variables `start_port` y `end_port` después de convertirlos a enteros.
4. Preparación del socket y la lista de puertos abiertos: Se obtiene la dirección IP del host utilizando `gethostbyname()`. Se inicializa una lista vacía llamada `opened_ports` para almacenar los puertos abiertos.
5. Bucle de escaneo de puertos: Se inicia un bucle `for` para iterar a través de los puertos en el rango especificado. Se crea un objeto de socket y se establece un tiempo de espera. Luego, se utiliza `connect_ex()` para intentar una conexión al host y puerto específico. Si el resultado es 0, significa que el puerto está abierto y se agrega a la lista `opened_ports`.
6. Impresión de los puertos abiertos: Se imprime la lista de puertos abiertos en la salida estándar mediante un bucle `for`.

***El Script scan_portv1.py original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_portv1.py](./scan_portv1.py)***



## scan_portv2.py
El script utiliza sockets para escanear diferentes puertos en un rango de direcciones IP específico. Comprueba la conexión a los puertos definidos y muestra si la conexión fue exitosa o falló para cada dirección IP y puerto escaneado.

![imagen13](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/e761e074-c0d3-4d3b-855c-75ab4762bc2a)

1. Importación de librerías: Se importa la librería `socket` para utilizar funciones relacionadas con la comunicación a través de sockets.
2. Definición de la función de escaneo: Se define la función `scan` que utiliza sockets para probar la conexión a diferentes puertos. Se crea un nuevo objeto de socket, se establece un tiempo de espera y se intenta establecer una conexión con la dirección y puerto proporcionados. El resultado de la conexión se devuelve.
3. Lista de puertos a escanear: Se define una lista de puertos que se desean escanear. En este caso, los puertos 21, 22, 25 y 80 están incluidos en la lista.
4. Bucle de escaneo: Se realiza un bucle `for` para iterar a través de las direcciones IP en el rango 192.168.56.1-192.168.56.254. Se llama a la función `scan` para cada dirección IP y puerto en la lista. Si el resultado es 0, se imprime que la conexión fue exitosa, de lo contrario, se imprime que ha fallado.

***El Script scan_portv2.py original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_portv2.py](./scan_portv2.py)***



## scan_portv3.py
El script utiliza hilos para realizar pruebas de conexión TCP a un rango de puertos específico en una dirección IP objetivo. Crea y ejecuta hilos para cada puerto, lo que permite realizar las pruebas de forma concurrente. Muestra los puertos abiertos durante el proceso de prueba.

![imagen14](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/0ecd47b0-0778-4ec3-a3e3-34a0d3360f90)

1. Importación de librerías: Se importa la librería `sys` para acceder a los argumentos de línea de comandos, `threading` para utilizar hilos y `socket` para la comunicación a través de sockets.
2. Definición de la función de prueba TCP: Se define la función `tcp_test` que realiza una prueba de conexión TCP a un puerto específico. Crea un nuevo socket, establece un tiempo de espera, intenta establecer una conexión con la dirección IP objetivo y el puerto dado. Si la conexión tiene éxito, se imprime que el puerto está abierto. Luego, el socket se cierra.
3. Verificación de ejecución principal: Se verifica si el script se está ejecutando como el programa principal.
4. Obtención de argumentos: Se obtienen los argumentos de línea de comandos. El primer argumento se guarda como `host` y el segundo argumento se divide en una lista de cadenas utilizando el carácter `-`. El inicio y fin del rango de puertos se guardan en las variables `start_port` y `end_port`.
5. Obtención de la dirección IP objetivo: Se obtiene la dirección IP correspondiente al `host` utilizando la función `gethostbyname`.
6. Creación y ejecución de hilos: Se crea una lista `hilos` para almacenar los hilos. Luego, se realiza un bucle `for` para iterar a través de los puertos en el rango especificado. Para cada puerto, se crea un hilo que llama a la función `tcp_test` pasando el puerto como argumento. El hilo se agrega a la lista y se inicia su ejecución.

***El Script scan_portv3.py original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scan_portv3.py](./scan_portv3.py)***



Esto seria todo en la seccion de Escaneo de Puertos!
