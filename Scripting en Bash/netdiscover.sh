#!/bin/bash
# Script netdiscover.sh
# 07/03/2023 - Leonardo
# Escaner de red basico en BASH

# Determinando el segmento de red
if which ifconfig > /dev/null; then
	echo "Comando ifconfig existe..."
	direccion_ip=$(ifconfig | grep inet | grep -v "127.0.0.1" | awk '{print $2}')
	echo "Esta es tu direccion ip: $direccion_ip"
	subred=$(ifconfig | grep inet | grep -v "127.0.0.1" | awk '{print $2}' | awk -F. '{print $1"."$2"."$3"."}')
	echo "Esta es tu subred: $subred"
else
	echo "No existe el comando ifconfig...usando ip"
	direccion_ip=$(ip addr show | grep inet | grep -v "127.0.0.1" | awk '{print $2}')
	echo "Esta es tu direccion ip: $direccion_ip"
	subred=$(ip addr show | grep inet | grep -v "127.0.0.1" | awk '{print $2}' | awk -F. '{print $1"."$2"."$3"."}')
	echo "Esta es tu subred: $subred"
fi

for ip in {1..254}; do
	if ping -q -c 4 "${subred}${ip}" > /dev/null; then
		echo "Host responde: ${subred}${ip}"
	fi
done
