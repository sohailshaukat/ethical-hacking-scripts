#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP()
    print(arp_request.summary())

scan("192.168.0.1/24")
