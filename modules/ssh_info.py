import os,sys,subprocess

ssh_client = os.getenv('SSH_CLIENT')
user = os.getenv('USER')


def getIPDetail():    
    pseudoTermID = os.ttyname(sys.stdout.fileno()).replace('/dev/','')
    cmdStr       = 'last | grep "still logged in" | grep "'+pseudoTermID+'"'
    sp           = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True)
    (out, err)   = sp.communicate()
    RemoteIP = out.split()[2].replace(":0.0", "") if len(out.split()) > 2 else ""

def getUser():
    if ssh_client is None:
        print(f"Hello, {user}! My name is Al. Pleased to meet you.")
    else:
        client_ip = ssh_client.split()[0]
        client_port = ssh_client.split()[-1]
        client_string = f"[ {client_ip} : {client_port} ]"
        
        print(f"Hey {client_string}! My name is Al. Pleased to meet you.")
    

