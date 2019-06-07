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
    for el in answererd_list:
        print(el[1].psrc+"\t\t"+el[1].hwsrc)
        print("-"*50)
        #print(el[1].show())

if __name__ == "__main__":
    scan("192.168.0.1/24")
