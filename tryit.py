from time import sleep as slp
from os import system as s
def box(tapp,neww):
    s("cls")
    print(neww)
    print(tapp+" ________   ")
    print(tapp+"|        |  ")
    print(tapp+"|        |  ")
    print(tapp+"|        |  ")
    print(tapp+"|________|  ")
    slp(0.001)
tap="\t"
new="\n"
#You want exit press [Ctrl+c] 
while True:
    for x in range(1,18):
        tapp=tap*x
        box(tapp,"")
    for y in range(1,29):
        neww=new*y
        box(tapp,neww)
    for z in range(16,0,-1):
        tapp=tap*z
        box(tapp,neww)
    for a in range(29,1,-1):
        neww=new*a
        box("\t",neww)