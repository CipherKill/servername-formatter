file=open('servers.txt','r')
rawdata=file.read().split('\n')

outputfile=open('output.txt','w')

def padzero(data):
    return "vw{}{}apppr01.ngco.com\n".format('0'*(5-len(data)),data)


# print(padzero('2'))
for server in rawdata:
    outputfile.write(padzero(server))
outputfile.close()
