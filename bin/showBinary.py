#!/usr/bin/env python3
import sys

codes = ["."]
codes += [ chr(i+64) for i in range(1,27) ]
codes += [ "1","2","3", "4","5", "6"]
codes += [ chr(i+64+32) for i in range(1,27) ]
codes += ["7","8","9","!"]

esc=chr(27)
red=esc+"[31m"
blue=esc+"[34m"
green=esc+"[32m"
black=esc+"[30m"
off=esc+"[(B"+esc+"[m"

lo = [red,black]
hi = [green,blue]

def encode(txt):
    result=""
    for b in txt:
        result+=code(b)
    return result+off

def code(x):
    if x == 32:
       return ' '
    if x > 127:
       x-=128
       text=blue
       ctrl=green
    else:
       text=black
       ctrl=red
     
    if x == 127:
       return ctrl +"?"
    elif x == 0:
       return ctrl + "@"
    elif x >=1 and x <= 26:
       return ctrl + chr(x+64)
    elif x == 27:
       return ctrl + "["
    elif x == 28: 
       return ctrl + "\\"
    elif x == 29: 
       return ctrl + "]"
    elif x == 30: 
       return ctrl + "^"
    elif x == 31:
       return ctrl + "_"
    elif x == 32: 
       return ctrl + "`"
    return text + chr(x)

def read(name):
    with open(name,"rb") as f:
         txt=f.read()
    return txt

def test():
    txt = [i for i in range(256)]
    print(encode(txt))

# red ⇒ ^ + c (^?⇒ chr(127); ^c ⇒ chr(c-64)
# black ⇒ c (\^ ⇒ ^, \& ⇒ &, \@ ⇒ @, \\ ⇒ \) 
# green ⇒ @ (@? ⇒ chr(255); @c ⇒ chr(c+64) 
# blue ⇒ & + c (&c => chr(c+128))

if __name__ == "__main__":
    if len(sys.argv) < 2:
       print("No files given: test mode")
       test()
    else:
       for f in sys.argv[1:]:
           print("{} ⇒ ".format(f))           
           print(encode(read(f))) 
