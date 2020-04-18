#! usr/bin/env python

import scapy.all as sc
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = sc.srp(arp_request_broadcast, timeout=10)[0]
    client_list = []
    for element in answered_list:
        client_dict = {'ip':element[1].psrc, 'mac':element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(client_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in client_list:
        print(client["ip"]+"\t\t"+client["mac"])
        print("-----------------------------------------")

print_result(scan(get_arguments().target))
