from mcstatus import MinecraftServer
import os.path
import json

def que(pipeline):
    # Gets extra details on minecraft servers
    # creates a "server profile"
    while pipeline.not_empty:
        ip = pipeline.get()[0]
        server = MinecraftServer.lookup(ip)
        ServerProfile = {}
        try:
            query = server.query()
            print('%s queried!' % ip)
            ServerProfile = {
                "ServerIP": ip,
                "MOTD": query.motd,
                "Version": query.software.version,
                "Plugins": query.software.plugins,
                "PlayerNames": query.players.names,
                "PingLog":[]
            }
        except:
            print('Query failed on %s' % ip)
            ServerProfile = {
                "ServerIP": ip,
                "MOTD": 'Query failed',
                "Version": 'Query failed',
                "Plugins": 'Query failed',
                "PlayerNames": ['Query failed'],
                "PingLog":[]
            }
            
        if not os.path.isfile('ServerProfiles/'+ip+'.json'):
            with open('ServerProfiles/'+ip+'.json', 'w') as File:
                json.dump(ServerProfile, File)