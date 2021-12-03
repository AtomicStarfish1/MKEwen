from mcstatus import MinecraftServer

def que(pipeline):
    # Gets extra details on minecraft servers
    # Will create a "server profile" in the future
    fs = open('qout.txt', 'a')
    while pipeline.not_empty:
        bruh = pipeline.get()[0]
        print(bruh)
        server = MinecraftServer.lookup(bruh)
        try:
            query = server.query()
            print('%s queried!' % bruh)
            fs.write('%s|%s|%s|%s|%s\n' % (bruh,query.motd,query.software.version,query.software.plugins,query.players.names))
        except:
            print('Query failed on %s' % bruh)
            fs.write('%s|failed query\n' % bruh)
    fs.close()

if __name__ == "__main__":
    que()
