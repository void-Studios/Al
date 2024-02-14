import platform
import os
import sys
from art import tprint,text2art


print(":v")
print(sys.platform)
print(":v")
sysuname = platform.uname()

for name in sysuname:
    print(name)
    print(":v")

# tprint("Hello World", font="bulbhead")
# print(text2art("This is another print"))
