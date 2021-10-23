f = open('out.txt', 'r+')
lines = f.readlines()
f.close()
bruh = []
ruh = []
for line in lines:
    bruh.append(line.split('|')[0])
[ruh.append(x) for x in bruh if x not in ruh]
for line in ruh:
    
