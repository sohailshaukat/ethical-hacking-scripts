#!/usr/bin/env python
import scapy.all as scapy
import argparse

def print_result(clients_list):
    print("_"*50)
    print("IP \t\t\t MAC Address")
    print("-"*50)
    for client in clients_list:
        print(client["ip"]+"\t\t"+client["mac"])

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answererd_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    clients_list = []
    for el in answererd_list:
        client_dict = {"ip":el[1].psrc, "mac":el[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def get_ip():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--iprange", dest = "ip_range", help = "IP range to be scanned")

    options = parser.parse_args()
    ip_range = options.ip_range
    if not ip_range:
        ip_range = raw_input("ip range >")
    return ip_range

if __name__ == "__main__":
    ip_range = get_ip()
    print_result(scan(ip_range))
