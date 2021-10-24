from ipgen import *
import socket
from mcstatus import MinecraftServer
from threading import Thread
from queryboi import que
from repinger import reping
from time import sleep

def pwn():
    while True:
        gen = ipgen() + ':25565'
        #print('Contacting ' + gen)
        server = MinecraftServer.lookup(gen)
        fs = open("out.txt", "a")
        try:
            status = server.status()
            print("%s has %s players and replied in %s ms" % (gen,status.players.online,status.latency))
            fs.write("%s|%s|%s\n" % (gen,status.players.online,status.latency))
            fs.close()
            que()
        except ConnectionRefusedError and OSError:
            pass
            #print("Server didn't respond :(")
    try:
        fs.close()
    except:
        pass

def rep():
    while True:
        reping()
        sleep(1200000)

def throod():
    boi = int(input("Give number of threads: "))
    threads = []
    for boi in range(boi):
        threads = Thread(target=pwn)
        threads.start()
    repper = Thread(target=rep)
    repper.start()

throod()
