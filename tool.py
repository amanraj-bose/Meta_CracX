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
import datetime

class Soviet(predict.Predict):
    def __init__(self) -> None:
        with open(os.path.join("config/config.json"), "r") as f:
            data = json.load(f)
        self.name = data['Name']
        self.Version = data['Version']
        self.font = data['font']
        self.port = data['port']
        self.arg = data['arguments']

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
            self.user = str(input("\033[0;36m-->\033[1;37m "))
        except Exception and KeyboardInterrupt:
            sys.exit(0)

        nmap = nm.PortScanner()
        scan = nmap.scan(self.user, self.port, self.arg)
        main = scan['scan'][str(self.user)]['tcp']
        self.ip = scan['scan'][str(self.user)]['tcp'].keys()
        self.PORT = np.random.choice(np.array(list(self.ip)))
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
        command.sprint(f"{self.name} is Starting....")
        print("\033[0m", end="")
        os.system("clear")
        self.logo()
        dt = datetime.datetime()
        print(f"\033[1;37m\n[ Author : Aman Raj ]\n[ Version : {self.Version} ]\n[ Starting Time & Date : {time.strftime('%H:%M')} & {dt.date()} ]\n [ System Found : {str(platform.system()).capitalize()} ]\033[0m")
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
        self.predicted = self.predict(self.PORT, self.STATE, self.SERVICE, self.VERSION)
        print(f"{Color.BLUE}[+] {Color.WHITE}Exploit Used => {self.predicted}")
        command.metasploit(self.predicted, self.user, self.lhost()[0])


if __name__ == '__main__':
    run = Soviet()
    run.USER()
