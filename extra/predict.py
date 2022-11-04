import joblib
import os
import warnings
import sys


class Predict:
    def __init__(self) -> None:
        port = os.path.join("model/port.pkl")
        model = os.path.join("model/model.pkl")
        self.vullenbillity = joblib.load(port)
        self.exploit = joblib.load(model)

    def predict(self, port:int, state:str, service:str, version:int):
        if state != 'open':
            warnings.warn("\033[1;31mSorry Port is Closed")
            sys.exit(127)

        else:
            try:
                warnings.filterwarnings('ignore')
                STATE = 0
                SERVICE = int(self.service(service))
                VERSION = self.version(str(version).split()[0])
                vullenbillity = int(self.vullenbillity.predict([[STATE, SERVICE, VERSION]]))
                EXPLOITS = int(self.exploit.predict([[port, STATE, SERVICE, VERSION, vullenbillity]]))

                return self.Exploit_classifier(EXPLOITS)
            except Exception:
                pass

    def Exploit_classifier(self, n:int) -> int:
        n = int(n)
        if n == 8:
            exploit = "exploit/unix/ftp/vsftpd_234_backdoor"
        elif n == 1:
            exploit = "exploit/linux/misc/gld_postfix"
        elif n == 5:
            exploit = "exploit/multi/http/apache_normalize_path_rce"
        elif n == 6:
            exploit = "exploit/multi/samba/usermap_script"
        elif n == 4:
            exploit = "exploit/multi/browser/java_rmi_connection_impl"
        elif n == 7:
            exploit = "exploit/unix/ftp/proftpd_133c_backdoor"
        elif n == 3:
            exploit = "exploit/linux/postgres/postgres_payload"
        elif n == 2:
            exploit = "exploit/linux/misc/igel_command_injection"
        elif n == 9:
            exploit = "exploit/unix/irc/unreal_ircd_3281_backdoor"
        else:
            exploit = None

        return exploit

    def service(self, n:str) -> str:
        n = str(n)
        if n == 'ftp':
            service = 5
        elif n == "ssh":
            service = 16
        elif n == "telnet":
            service = 17
        elif n == "smtp":
            service = 15
        elif n == "domain":
            service = 3
        elif n == "http":
            service = 6
        elif n == "rpcbind":
            service = 13
        elif n == "Netbios-ssn":
            service = 0
        elif n == "exec?":
            service = 4
        elif n == "login":
            service = 9
        elif n == "shell?":
            service = 14
        elif n == "java-rmi":
            service = 8
        elif n == "bindshell":
            sevice = 2
        elif n == "nfs":
            service = 11
        elif n == "mysql":
            service = 10
        elif n == "postgresql":
            service = 12
        elif n == "vnc":
            service = 18
        elif n == "x11":
            service = 19
        elif n == "irc":
            service = 7
        elif n == "ajp13":
            service = 1
        else:
            service = None

        return service

    def version(self, n:str):
        n = str(n)
        if n == "vsftpd":
            version = 19
        elif n == "OpenSSH":
            version = 12
        elif n == "Linux telnetd" or n == "Linux":
            version = 8
        elif n == 'Postfix':
            version = 13
        elif n == "ISC":
            version = 7
        elif n == "Apache httpd":
            version = 5
        elif n == "Samba":
            version = 16
        elif n == "GNU":
            version = 6
        elif n == "Metasploitable":
            version = 9
        elif n == "ProFTPD":
            version = 15
        elif n == "MySQL":
            version = 10
        elif n == "PostgreSQL":
            version = 14
        elif n == "UnrealIRCd":
            version = 17
        elif n == "Apache":
            version = 3
        else:
            version = None

        return int(version)
