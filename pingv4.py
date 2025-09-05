from scapy.all import IP, ICMP, send
import sys, time

texto_cifrado = sys.argv[1]
destino = "8.8.8.8"

for i, char in enumerate(texto_cifrado, start=1):
    paquete = IP(dst=destino)/ICMP()/char.encode('utf-8')
    send(paquete, verbose=0)  # Cambiado a verbose=0
    print(".", end="", flush=True)
    print(f"\nsent {i} packets.", flush=True)
    time.sleep(0.2)