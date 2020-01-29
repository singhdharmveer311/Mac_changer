#!/usr/bin/env python

import subprocess
import optparse
import re
# To return input value of user
def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address ")
    parser.add_option("-m", "--mac", dest="new_mac", help="New mac address ")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        #Code to handle error
        parser.error("[-] Please specify the interface, use --help for info. ")
    elif not options.new_mac:
        #Code to handle mac error
        parser.error("[-] Plaese specify a new mac, use --help for info. ")

    return options

def change_mac(interface, new_mac):
    print("[+] Changing mac address for: " + interface + " to " + new_mac)
    # SECURE WAY THAT WE ARE USING -------
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    # mac_address_search_result = re.search(r"(\w{2}:){5}\w{2}", ifconfig_result)
    # Decode it by using regex
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read the MAC address. ")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current mac = " + str(current_mac))

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac address was successfully changed to " + current_mac)
else:
    print("[-] Mac addresss did not changed. " )
# change_mac(options.interface, options.new_mac)   # Call of change mac funtion


# UNSECURE WAY (Because user can manipulate input )-------------------
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

