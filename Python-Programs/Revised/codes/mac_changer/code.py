#! usr/bin/python

import subprocess
import optparse
import re

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change it's MAC address.")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a mac-address, use --help for more info.")
    return options

def get_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",options.interface])
    mac_addr_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_addr_search_result:
        return(mac_addr_search_result.group(0))
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()
interface = options.interface
new_mac = options.new_mac

current_mac = get_mac(interface)
print("...Current MAC = "+str(current_mac))

change_mac(interface, new_mac)

current_mac = get_mac(interface)

if current_mac == new_mac:
    print("[+] MAC address was successfully changed to "+ current_mac)
else:
    print("[-] MAC address did not get changed.")
