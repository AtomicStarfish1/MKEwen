from mcstatus import MinecraftServer

def reping():
    bruh = []
    ruh = []
    f = open('out.txt', 'r+')
    lines = f.readlines()
    f.close()
    fs = open('rout.txt', 'w').close()
    fs = open('rout.txt', 'a')
    for line in lines:
        bruh.append(line.split('|')[0])
    [ruh.append(x) for x in bruh if x not in ruh]
    for line in ruh:
        bruh = line
        #print(bruh)
        server = MinecraftServer.lookup(bruh)
        try:
            status = server.status()
            #print("%s has %s players and replied in %s ms" % (bruh,status.players.online,status.latency))
            fs.write("%s|%s|%s\n" % (bruh,status.players.online,status.latency))
        except ConnectionRefusedError and OSError:
            #print("Server didn't respond :(")
            fs.write("%s|DOWN\n" % (bruh))
    fs.close()