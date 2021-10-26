from mcstatus import MinecraftServer

def que():
    f = open('out.txt', 'r+')
    lines = f.readlines()
    f.close()
    fs = open('qout.txt', 'w').close()
    fs = open('qout.txt', 'a')
    for line in lines:
        bruh = line.split('|')[0]
        #print(bruh)
        server = MinecraftServer.lookup(bruh)
        try:
            query = server.query()
            #print('%s queried!' % bruh)
            fs.write('%s|%s|%s|%s|%s\n' % (bruh,query.motd,query.software.version,query.software.plugins,query.players.names))
        except:
            #print('Query failed on %s' % bruh)
            fs.write('%s|failed query\n' % bruh)
    fs.close()

if __name__ == "__main__":
    que()
