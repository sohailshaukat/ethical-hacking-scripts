#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answererd_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    print("_"*50)
    print("IP \t\t\t MAC Address")
    print("-"*50)
    for el in answererd_list:
        print(el[1].psrc+"\t\t"+el[1].hwsrc)
        print("-"*50)

if __name__ == "__main__":
    scan("192.168.0.1/24")
