#Leonardo Hasiel Alvarado Zamora - 1949295
import os
import sys
import socket
import platform
import subprocess

def menu():
    print("Bienvenido al programa de escaneo de red.")
    print("Seleccione una opción:")
    print("1. Escaneo UDP")
    print("2. Escaneo completo")
    print("3. Detección de sistema operativo")
    print("4. Escaneo de red con ping")
    print("5. Salir")

    opcion = input("Ingrese su opción: ")
    return opcion

def escaneo_udp():
    # Código de escaneo UDP
    destino = input("Ingrese la dirección IP o nombre de host del destino: ")
    
    # Puerto que se va a escanear
    puerto = int(input("Ingrese el número del puerto que desea escanear: "))
    
    # Crear un objeto de socket UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(2) # Tiempo de espera de la respuesta en segundos
    
    try:
        # Enviar un mensaje UDP al destino y puerto especificado
        mensaje = "Mensaje de prueba"
        udp_socket.sendto(mensaje.encode(), (destino, puerto))
        
        # Esperar a recibir una respuesta
        respuesta, direccion = udp_socket.recvfrom(1024)
        
        # Imprimir la respuesta recibida
        print("Respuesta recibida desde {}:{}\n{}".format(direccion[0], direccion[1], respuesta.decode()))
    except socket.timeout:
        print("No se recibió respuesta del destino en el puerto especificado.")
    finally:
        udp_socket.close()

def escaneo_completo():
    # Código de escaneo completo
    # Dirección IP o nombre de host del destino
    destino = input("Ingrese la dirección IP o nombre de host del destino: ")
    
    # Realizar un escaneo completo utilizando el comando 'nmap' del sistema
    resultado = subprocess.check_output(["nmap", "-p 1-65535", "-T4", "-A", "-v", destino])
    print(resultado.decode())

def deteccion_sistema_operativo():
    # Código de detección de sistema operativo
    # Dirección IP o nombre de host del destino
    destino = input("Ingrese la dirección IP o nombre de host del destino: ")
    
    # Crear un objeto de socket ICMP
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    icmp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    try:
        # Enviar un paquete ICMP al destino especificado
        paquete_icmp = bytearray(b'\x08\x00\x7d\x4b\x00\x00\x00\x00Ping')
        icmp_socket.sendto(paquete_icmp, (destino, 0))
        
        # Esperar a recibir una respuesta
        respuesta, direccion = icmp_socket.recvfrom(1024)
        
        # Analizar la respuesta para determinar el sistema operativo
        if respuesta[20:22] == b'\x02\x00':
            print("El sistema operativo del destino es Linux.")
        elif respuesta[20:22] == b'\x02\x02':
            print("El sistema operativo del destino es Windows.")
        else:
            print("No se pudo determinar el sistema operativo del destino.")
    except socket.timeout:
        print("No se recibió respuesta del destino.")
    finally:
        icmp_socket.close()

def escaneo_red_ping():
    # Código de escaneo de red con ping
    # Dirección de red en formato CIDR
    red = input("Ingrese la dirección de red en formato CIDR (por ejemplo, 192.168.1.0/24)")

while True:
    opcion = menu()

    if opcion == "1":
        print("Realizando escaneo UDP...")
        escaneo_udp()
    elif opcion == "2":
        print("Realizando escaneo completo...")
        escaneo_completo()
    elif opcion == "3":
        print("Detectando sistema operativo...")
        deteccion_sistema_operativo()
    elif opcion == "4":
        print("Realizando escaneo de red con ping...")
        escaneo_red_ping()
    elif opcion == "5":
        print("Gracias por utilizar el programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")
