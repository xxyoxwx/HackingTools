import scapy.all as scapy
import optparse

def get_args():
    parser = optparse.OptionParser()

    parser.add_option("-t","--target",dest = "ip",help="Enter IP/s you would like to scan/scans")
    (opt,arg) = parser.parse_args()
    if not opt.ip:
        parser.error("[+] Please specify an InternetProtocol, use --help for more help.")
    return opt

def scan(ip):
    print('''\t     ####################WELCOME TO NETWORK SCANNER####################
             #                                                                #
             #                     Developed by wm3ryfxwz                     #
             #                                                                #
             ##################################################################\n''')
    arp_req = scapy.ARP(pdst=ip)
    brdcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_brdcast = brdcast / arp_req
    ans_list = scapy.srp(arp_req_brdcast, timeout=1, verbose=False)[0]

    infoc_list = []

    for index in ans_list:
        infoc_dict = {"IP": index[1].psrc, "MAC": index[1].hwsrc}
        infoc_list.append((infoc_dict))
    return infoc_list

def printdata(results):
    num = 0
    print("IP\t\t\t\tMAC ADDRESS\n-------------------------------------------------")
    for infoc in results:
        print(infoc["IP"]+"\t\t\t"+infoc["MAC"])
        num +=1
    print("\nnumber of results: " + str(num))

option = get_args()
scan_res = scan(option.ip)
printdata(scan_res)
