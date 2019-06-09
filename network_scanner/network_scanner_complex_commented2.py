#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    #arp_request.show()
    #print(arp_request.summary())
    #scapy.ls(scapy.ARP()) #to print all the attributes of the class in parenthesis
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()
    #scapy.ls(scapy.Ether())
    #print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    #print(arp_request_broadcast.summary())
    #arp_request_broadcast.show()
    answererd_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0] #if no timeout provided it will result in infinite loop
    #print(answererd_list.summary())
    print("_"*50)
    print("IP \t\t\t MAC Address")
    print("-"*50)
    clients_list = []
    for el in answererd_list:
        client_dict = {"ip":el[1].psrc, "mac": el[1].hwsrc}
        clients_list.append(client_dict)
    print(clients_list)
if __name__ == "__main__":
    scan("192.168.0.1/24")
