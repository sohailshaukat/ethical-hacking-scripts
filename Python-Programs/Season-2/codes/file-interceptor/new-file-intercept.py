#! usr/bin/env python3

import netfilterqueue
import scapy.all as scapy

ack_list = []

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(scapy.TCP):
        if scapy_packet[scapy.TCP].dport == 80:
            print("lel")
        elif scapy_packet[scapy.TCP].sport == 80:
            print("hmmst")

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
