import os,sys,subprocess
pseudoTermID = os.ttyname(sys.stdout.fileno()).replace('/dev/','')
cmdStr       = 'last | grep "still logged in" | grep "'+pseudoTermID+'"'
sp           = subprocess.Popen([cmdStr], stdout=subprocess.PIPE, shell=True)
(out, err)   = sp.communicate()
RemoteIP     = out.split()[2].replace(":0.0","")   #Returns "" if not SSH

