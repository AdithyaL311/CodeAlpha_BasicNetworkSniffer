from scapy.all import *

def packet_callback(packet):
    print(packet.summary())

print("Capturing packets...")

sniff(
    iface="\\Device\\NPF_Loopback",
    prn=packet_callback,
    count=10,
    store=False
)