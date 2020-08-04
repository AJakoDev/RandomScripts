import os
import subprocess

IP = input("What is the IP address? ")

os.system('mkdir nmap')

subprocess.check_call(['nmap','-sC', '-sV','-T4','-oA','nmap/quick',IP])

with open("nmap/quick.nmap") as f:
    port = f.read()
    if "80/tcp open" in port:
        os.system("dirb http://" + IP + "-r -o results.dirb")
    elif "443/tcp open" in port:
        os.system("dirb http://" + IP + "-r -o results.dirb")
    else:
        print("\nNO 80 OR 443 PORTS OPEN!\n")
        
subprocess.check_call(['nmap','-A', '-p-', '-T4', '-oA', 'nmap/full', IP])
 
