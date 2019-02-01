import os.path

str1=input("enter file name")
str2="/keySound"
str2=str1+str2
if os.path.isfile(str2):
    fp=open(str2 ,"r")
    print("opened")
else:
    print('keySound is not found in the folder')
    exit()

x=[]
with open(str2) as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = list(filter(None, content))
for i in content:
    i=i[:5]+":"+i[6:]
    x.append(i)
d={}
#print(x)
for b in x:
    i = b.split(':')
    d[i[0]] = i[1]
#print("enter * to exit")
#playSound(1)
s1=0
for s in x:
    if(s[0]!=s1):
        s1=s[0]
        print("In Page Number",s1)
    if s[2]=="1":
        if s[4]=="1":
            print("q")
        elif s[4]=="2":
            print("w")
        elif s[4] == "3":
            print("e")
        elif s[4] == "4":
            print("r")
        elif s[4] == "5":
            print("t")
        elif s[4]=="6":
            print("y")
        elif s[4] == "7":
            print("u")
        elif s[4] == "8":
            print("i")
    elif s[2]=="2":
        if s[4]=="1":
            print("a")
        elif s[4]=="2":
            print("s")
        elif s[4] == "3":
            print("d")
        elif s[4] == "4":
            print("f")
        elif s[4] == "5":
            print("g")
        elif s[4]=="6":
            print("h")
        elif s[4] == "7":
            print("j")
        elif s[4] == "8":
            print("k")
    elif s[2]=="3":
        if s[4]=="1":
            print("z")
        elif s[4]=="2":
            print("x")
        elif s[4] == "3":
            print("c")
        elif s[4] == "4":
            print("v")
        elif s[4] == "5":
            print("b")
        elif s[4]=="6":
            print("n")
        elif s[4] == "7":
            print("m")
        elif s[4] == "8":
            print(",")
    elif s[2]=="4":
        if s[4]=="1":
            print("o")
        elif s[4]=="2":
            print("p")
        elif s[4] == "3":
            print("[")
        elif s[4] == "4":
            print("]")
        elif s[4] == "5":
            print("l")
        elif s[4]=="6":
            print(";")
        elif s[4] == "7":
            print("'")
        elif s[4] == "8":
            print("/")
    elif s[2]=="5":
        if s[4]=="1":
            print("Q")
        elif s[4]=="2":
            print("W")
        elif s[4] == "3":
            print("E")
        elif s[4] == "4":
            print("R")
        elif s[4] == "5":
            print("T")
        elif s[4]=="6":
            print("Y")
        elif s[4] == "7":
            print("U")
        elif s[4] == "8":
            print("I")
    elif s[2]=="6":
        if s[4]=="1":
            print("A")
        elif s[4]=="2":
            print("S")
        elif s[4] == "3":
            print("D")
        elif s[4] == "4":
            print("F")
        elif s[4] == "5":
            print("G")
        elif s[4]=="6":
            print("H")
        elif s[4] == "7":
            print("J")
        elif s[4] == "8":
            print("K")
    elif s[2]=="7":
        if s[4]=="1":
            print("Z")
        elif s[4]=="2":
            print("X")
        elif s[4] == "3":
            print("C")
        elif s[4] == "4":
            print("V")
        elif s[4] == "5":
            print("B")
        elif s[4]=="6":
            print("N")
        elif s[4] == "7":
            print("M")
        elif s[4] == "8":
            print("<")
    elif s[2]=="8":
        if s[4]=="1":
            print("O")
        elif s[4]=="2":
            print("P")
        elif s[4] == "3":
            print("{")
        elif s[4] == "4":
            print("}")
        elif s[4] == "5":
            print("L")
        elif s[4]=="6":
            print(":")
        elif s[4] == "7":
            print('"')
        elif s[4] == "8":
            print("?")

x=input()
x=input()
x=input()
