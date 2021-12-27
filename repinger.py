from mcstatus import MinecraftServer
import os
import datetime
import json
    
def BetterReping():
    ips = os.listdir('ServerProfiles') # the names of the files are the ips, so we can use them to reping
    print(ips)
    for ip in ips:
        ip = ip[:-5]
        server = MinecraftServer.lookup(ip)
        Time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        try:
            status = server.status()
            PingLog = {"Time": Time,
                       "Players Online": status.players.online,
                       "Latency": status.latency, 
                       "Status":'ONLINE'}
        except:
            PingLog = {"Time": Time,
                       "Players Online": 0,
                       "Latency": 0, 
                       "Status":'DOWN'}
            
        with open('ServerProfiles/'+ip+'.json', 'r') as File:
            ServerProfile = json.load(File)
            ServerProfile['PingLog'].append(PingLog)
            
        with open('ServerProfiles/'+ip+'.json', 'w') as File:
            json.dump(ServerProfile, File)


