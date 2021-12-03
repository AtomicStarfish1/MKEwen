def namey(pipeline):
    bruh = []
    f = open('qout.txt', 'r+')
    lines = f.readlines()
    f.close()
    fs = open('nout.txt', 'w').close()
    fs = open('nout.txt', 'a')
    for line in lines:
        try:
            cuh = line.split('|')[4].replace("[]","")
            if cuh != '\n':
                bruh.append('%s|%s' % (line.split('|')[0],cuh))
        except IndexError:
            pass 
    for name in bruh:
        fs.write(name)
    fs.close()

if __name__ == "__main__":
    namey()
