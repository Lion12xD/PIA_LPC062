#Leonardo Hasiel Alvarado Zamora - 1949295
#Parte1
#Importamos librerias necesarias
import sys
import threading
from socket import *
#Parte2
#Creamos una funcion tcp_test la cual
#permite probar mediante socket los puertos
#abiertos, se lo agrega lock.release()
def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    try:
        sock.connect((target_ip, port))
        print("Opened Port:", port)
    except:
        pass
    finally:
        sock.close()


#Parte3
#Establecemos el main del script
#Guardamos en variables host y portstrs
if __name__=='__main__':
    # portscan.py <host> <start_port>-<end_port>
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')
#Parte4
#portstrs se convierte en lista al momento
#de hacer split y de ahi obtener dos valores
start_port = int(portstrs[0])
end_port = int(portstrs[1])
#Parte5
#Usando la funcion gethostbyname se obtiene
#la direccion ip.
target_ip = gethostbyname(host)
#Parte6
#Se inicia buble para probar puertos
#usando la funcion tcp_test y generando
#un hilo por cada puerto a probar
hilos = []
for port in range(start_port, end_port):
    hilo = threading.Thread(target=tcp_test, args=(port,))
    hilos.append(hilo)
    hilo.start()