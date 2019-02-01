import os.path
import simpleaudio as sa
import msvcrt
pNum=1
def playSound(a):
    try:
        a = msvcrt.getch()
        a = "".join(map(chr, a))
        #a=input()
        if a is "*":
            exit()
        s=search_sound(a)
        global pNum
        s=str(pNum)+" "+str(s)
        #print(s)
        sound=d[s]
        sound=str1+"/sounds/"+sound
        #print(sound)
        wave_obj = sa.WaveObject.from_wave_file(sound)
        play_obj = wave_obj.play()
        playSound(a)

    except KeyError:
        playSound(a)


def search_sound(c):
    if c is 'q':
        return "1 1"
    elif c is 'w':
        return "1 2"
    elif c is 'e':
        return "1 3"
    elif c is 'r':
        return "1 4"
    elif c is 't':
        return "1 5"
    elif c is 'y':
        return "1 6"
    elif c is 'u':
        return "1 7"
    elif c is 'i':
        return "1 8"
    elif c is 'a':
        return "2 1"
    elif c is 's':
        return "2 2"
    elif c is 'd':
        return "2 3"
    elif c is 'f':
        return "2 4"
    elif c is 'g':
        return "2 5"
    elif c is 'h':
        return "2 6"
    elif c is 'j':
        return "2 7"
    elif c is 'k':
        return "2 8"
    elif c is 'z':
        return "3 1"
    elif c is 'x':
        return "3 2"
    elif c is 'c':
        return "3 3"
    elif c is 'v':
        return "3 4"
    elif c is 'b':
        return "3 5"
    elif c is 'n':
        return "3 6"
    elif c is 'm':
        return "3 7"
    elif c is ',':
        return "3 8"
    elif c is 'o':
        return "4 1"
    elif c is 'p':
        return "4 2"
    elif c is '[':
        return "4 3"
    elif c is ']':
        return "4 4"
    elif c is 'l':
        return "4 5"
    elif c is ';':
        return "4 6"
    elif c is '':
        return "4 7"
    elif c is '/':
        return "4 8"
    if c is 'Q':
        return "5 1"
    elif c is 'W':
        return "5 2"
    elif c is 'E':
        return "5 3"
    elif c is 'R':
        return "5 4"
    elif c is 'T':
        return "5 5"
    elif c is 'Y':
        return "5 6"
    elif c is 'U':
        return "5 7"
    elif c is 'I':
        return "5 8"
    elif c is 'A':
        return "6 1"
    elif c is 'S':
        return "6 2"
    elif c is 'D':
        return "6 3"
    elif c is 'F':
        return "6 4"
    elif c is 'G':
        return "6 5"
    elif c is 'H':
        return "6 6"
    elif c is 'J':
        return "6 7"
    elif c is 'K':
        return "6 8"
    elif c is 'Z':
        return "7 1"
    elif c is 'X':
        return "7 2"
    elif c is 'C':
        return "7 3"
    elif c is 'V':
        return "7 4"
    elif c is 'B':
        return "7 5"
    elif c is 'N':
        return "7 6"
    elif c is 'M':
        return "7 7"
    elif c is '<':
        return "7 8"
    elif c is 'O':
        return "8 1"
    elif c is 'P':
        return "8 2"
    elif c is '{':
        return "8 3"
    elif c is '}':
        return "8 4"
    elif c is 'L':
        return "8 5"
    elif c is ':':
        return "8 6"
    elif c is '"':
        return "8 7"
    elif c is '?':
        return "8 8"
    elif c is '.':
        return "1"
    elif c is '>':
        return "1"
    elif c is ',':
        return "1"
    else:
        global pNum
        pNum=c
        #print(pNum)


def page_number(*args):
    pnum=1
    if len(args)>0:
        pnum=args
    return pnum

print("                                                                                                                                                        dddddddd")
print("lllllll                                                                           hhhhhhh                                                               d::::::d")
print("l:::::l                                                                           h:::::h                                                               d::::::d")
print("l:::::l                                                                           h:::::h                                                               d::::::d")
print("l:::::l                                                                           h:::::h                                                               d:::::d ")
print(" l::::l   aaaaaaaaaaaaa   uuuuuu    uuuuuu  nnnn  nnnnnnnn        cccccccccccccccc h::::h hhhhh       ppppp   ppppppppp     aaaaaaaaaaaaa       ddddddddd:::::d ")
print(" l::::l   a::::::::::::a  u::::u    u::::u  n:::nn::::::::nn    cc:::::::::::::::c h::::hh:::::hhh    p::::ppp:::::::::p    a::::::::::::a    dd::::::::::::::d ")
print(" l::::l   aaaaaaaaa:::::a u::::u    u::::u  n::::::::::::::nn  c:::::::::::::::::c h::::::::::::::hh  p:::::::::::::::::p   aaaaaaaaa:::::a  d::::::::::::::::d ")
print(" l::::l            a::::a u::::u    u::::u  nn:::::::::::::::nc:::::::cccccc:::::c h:::::::hhh::::::h pp::::::ppppp::::::p           a::::a d:::::::ddddd:::::d ")
print(" l::::l     aaaaaaa:::::a u::::u    u::::u    n:::::nnnn:::::nc::::::c     ccccccc h::::::h   h::::::h p:::::p     p:::::p    aaaaaaa:::::a d::::::d    d:::::d ")
print(" l::::l   aa::::::::::::a u::::u    u::::u    n::::n    n::::nc:::::c              h:::::h     h:::::h p:::::p     p:::::p  aa::::::::::::a d:::::d     d:::::d ")
print(" l::::l  a::::aaaa::::::a u::::u    u::::u    n::::n    n::::nc:::::c              h:::::h     h:::::h p:::::p     p:::::p a::::aaaa::::::a d:::::d     d:::::d ")
print(" l::::l a::::a    a:::::a u:::::uuuu:::::u    n::::n    n::::nc::::::c     ccccccc h:::::h     h:::::h p:::::p    p::::::pa::::a    a:::::a d:::::d     d:::::d ")
print("l::::::la::::a    a:::::a u:::::::::::::::uu  n::::n    n::::nc:::::::cccccc:::::c h:::::h     h:::::h p:::::ppppp:::::::pa::::a    a:::::a d::::::ddddd::::::dd")
print("l::::::la:::::aaaa::::::a  u:::::::::::::::u  n::::n    n::::n c:::::::::::::::::c h:::::h     h:::::h p::::::::::::::::p a:::::aaaa::::::a  d:::::::::::::::::d")
print("l::::::l a::::::::::aa:::a  uu::::::::uu:::u  n::::n    n::::n  cc:::::::::::::::c h:::::h     h:::::h p::::::::::::::pp   a::::::::::aa:::a  d:::::::::ddd::::d")
print("llllllll  aaaaaaaaaa  aaaa    uuuuuuuu  uuuu  nnnnnn    nnnnnn    cccccccccccccccc hhhhhhh     hhhhhhh p::::::pppppppp      aaaaaaaaaa  aaaa   ddddddddd   ddddd")
print("                                                                                                       p:::::p                                                  ")
print("                                                                                                       p:::::p                                                  ")
print("                                                                                                      p:::::::p                                                 ")
print("                                                                                                      p:::::::p                                                 ")
print("                                                                                                      p:::::::p                                                 ")
print("                                                                                                      ppppppppp                                                 ")


str1=input("enter file name: ")
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
print(x)
for b in x:
    i = b.split(':')
    d[i[0]] = i[1]
print("enter * to exit")
playSound(1)
'''s1=0
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
'''
