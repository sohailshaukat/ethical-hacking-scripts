#!/usr/bin/env python
import scapy.all as scapy

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


if __name__ == "__main__":
    print_result(scan("192.168.0.1/24"))
