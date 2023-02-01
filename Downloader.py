import requests
import optparse

def get_args():
    parser = optparse.OptionParser()

    parser.add_option("-d","--wget",dest="url",help="Enter source you would like to Download")
    (opt,arg) = parser.parse_args()
    if not opt.url:
        parser.error("[+] Please specify source you would like to Download, use --help for more info.")
    return opt


def download(url):
    get_response = requests.get(url)
    file = url.split("/")[-1]
    with open(file,"wb") as output:
        output.write(get_response.content)

option = get_args()
download(option.url)
