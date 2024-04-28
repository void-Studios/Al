import platform 
import sys


print(sys.platform)

sysuname  = platform.uname()

for name in sysuname:
    print(name)
    print("|_")