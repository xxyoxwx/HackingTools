import subprocess
import optparse
import time
import re

def get_args():
    parser = optparse.OptionParser()
     
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC addr")
    parser.add_option("-m", "--mac_address", dest="mac_address", help="Interface to set its new mac address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify an interface, use --help for more help.")
    elif not options.mac_address:
        parser.error("[+] Please specify an mac_address, use --help for more help.")
    return options
    


def change_mac(interface,new_mac):
    print("\n[+] changing mac address...")
    time.sleep(0.4)
    print("10")
    time.sleep(0.4)
    print("9")
    time.sleep(0.4)
    print("8")  
    time.sleep(0.4)    
    print("7")  
    time.sleep(0.4)     
    print("6")  
    time.sleep(0.4)      
    print("5")  
    time.sleep(0.4)     
    print("4")  
    time.sleep(0.4)     
    print("3")  
    time.sleep(0.4)
    print("2")      
    time.sleep(0.4)  
    print("1") 
    time.sleep(0.4)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])    
    subprocess.call(["ifconfig", interface, "up"])

def get_mac(interface):
    result_ifconfig_new = subprocess.check_output(["ifconfig", interface])
    address_new = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",result_ifconfig_new.decode("utf-8"))
    if address_new:
        return address_new.group(0)
    else:
        print("\n[+] Could not read MAC address\n")


print('''         ##################WELCOME TO MAC ADRESS CHANGER##################
         #                                                               #
         #                    developed by wm3ryfxwz                     #
         #                                                               #
         ############################################################### #''')
options = get_args()
old_mac = get_mac(options.interface)
print("\nYour current MAC address is > " + str(old_mac))

change_mac(options.interface,options.mac_address)

new_mac = get_mac(options.interface)
if old_mac != new_mac:
    print("[+] Your mac address has been changed successfully >.<\n")

print("Your new MAC address is > " + str(new_mac))
