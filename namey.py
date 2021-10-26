def namey():
    bruh = []
    f = open('qout.txt', 'r+')
    lines = f.readlines()
    f.close()
    fs = open('nout.txt', 'a')
    for line in lines:
        bruh.append(line.split('|')[4])
    for name in bruh:
        fs.write(name+'\n')
    fs.close()