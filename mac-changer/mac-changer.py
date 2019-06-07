#!/usr/bin/env python
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

    (options, arguments) = parser.parse_args()

    interface = options.interface
    new_mac = options.new_mac

    if not interface:
        interface = input("interface >")
    if not new_mac:
        new_mac = input("new MAC address >")
    return interface,new_mac

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", (ifconfig_result))
    if mac_address_search_result:
        return(mac_address_search_result.group(0))
    else:
        print("[-] Could not read MAC address")

if __name__ == "__main__":
    interface, new_mac = get_arguments()
    current_mac = get_current_mac(interface)
    print(f"current MAC > {str(current_mac)}")
    change_mac(interface, new_mac)
    current_mac = get_current_mac(interface)
    if current_mac == new_mac:
        print(f"[+] MAC address was successfully changed to {current_mac}")
    else:
        print("[-] MAC address didn't get changed.")