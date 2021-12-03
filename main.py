from ipgen import *
import concurrent.futures
from mcstatus import MinecraftServer
from queryboi import que
from repinger import BetterReping
from time import sleep
from namey import namey
import queue

def pwn(id, pipeline):
    #looks for minecraft servers
    while True:
        ip = ipgen() + ':25565'
        server = MinecraftServer.lookup(ip)
        try:
            status = server.status()
            print("%s has %s players and replied in %s ms" % (ip,status.players.online,status.latency))
            pipeline.put([ip,status.players.online,status.latency])
        except ConnectionRefusedError and OSError:
            pass
            print(f"Thread {id}: Server {ip} didn't respond :(")

def rep():
    while True:
        BetterReping()
        sleep(100)

def querer(pipeline):
    while True:
        que(pipeline)
        sleep(100)

def namer(pipeline):
    while True:
        namey(pipeline)
        sleep(100)
    
def BetterThreader(workers):
    pipeline = queue.Queue(maxsize=1000)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as exicutor:
        exicutor.submit(rep); print('Starting "rep"')
        exicutor.submit(querer, pipeline); print('Starting "querer')
        exicutor.submit(namer, pipeline); print('Starting "namer"')
        for i in range(workers-3): # the negative 3 is to take into account the other threads
            ii = i
            if i < 10:
                ii = str(i)+' '
            exicutor.submit(pwn, ii, pipeline); print(f'Starting Thread {i}: "pwn"')
    
BetterThreader(400)
