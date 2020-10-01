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



def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)
slowprint('''\033[1;31m \033[91m    
       __  ___                 ________                               
      /  |/  /___ ______      / ____/ /_  ____ _____  ____ ____  _____
     / /|_/ / __ `/ ___/_____/ /   / __ \/ __ `/ __ \/ __ `/ _ \/ ___/
    / /  / / /_/ / /__/_____/ /___/ / / / /_/ / / / / /_/ /  __/ /    
   /_/  /_/\__,_/\___/      \____/_/ /_/\__,_/_/ /_/\__, /\___/_/     
                                                   /____/\033[97m             
''')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
slowprint("\t\t                                         \033[93mBy :Lamani Hani VEGETA-LFH\033[97m")
print(" ")
print("1- show the current MAC-ADDRESS")
print("")
print("2- change your MAC-ADDRESS Randomly")
print("")
print("3- change your MAC-ADDRESS Customly")
print("")
print("4- reset the original MAC-ADDRESS")
print(" ")
print("5- why change MAC-ADDRESS")
print("")
mohamed=input("\033[92m[?] \033[96mmake your choise ==>")
if mohamed==('1') :
            print(" ")
            print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
            print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
            print(" ")
            lawla=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
            if lawla==('1') :
                      slowprint("\033[97m")
                      os.system('macchanger -s wlan0')
                      print(" ")
                      alla=input('press any key to cuntinue')
                      os.system('clear') 
                      os.system('python3 mac.py')
            if lawla==('2') :
                       slowprint("\033[97m")
                       os.system('macchanger -s eth0')
                       print(" ")
                       allah=input('press any key to cuntinue')
                       os.system('clear')
                       os.system('python3 mac.py')

if mohamed==('2') :
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               deuxs=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if deuxs==('2') :
                        slowprint("")
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -r eth0')
                        os.system('ifconfig eth0 up')
                        print(" ")
                        hoho=input("press any key to cuntinue")
                        os.system('clear')
                        os.system('python3 mac.py')
               if deuxs==('1') :
                        slowprint("")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -r wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ")
                        hoho=input("press any key to cuntinue")
                        os.system('clear')
                        os.system('python3 mac.py')


