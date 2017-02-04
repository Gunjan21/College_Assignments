import glob

def bag(file):
    p=glob.glob(file)
    ff=open('stop_words.txt','r')
    sw = ff.readlines()
    ff.close()
    sw=[sw[i].replace('\n','') for i in range(0,len(sw))]
    pp=[]
    for i in p:
        pp.append(glob.glob(i+'/*'))

    pp=sum(pp,[])

    spc=[('-',' '),('*',' '),('/',' '),('%',' '),('_',' '),('#',' '),('|',' ')]
    bow = []
    for i in range(0,len(pp)):
        with open(pp[i]) as f:
            data = f.read()
            data = data.replace('\n','')
            for k, v in spc:
                data = data.replace(k, v)
            data = data.split()
            data = [data[j] for j in range(0,len(data)) if data[j] not in sw]
            data = [data[j] for j in range(0,len(data)) if len(data[j])>2]
            z=set(data)
            for k in z:
                if k not in bow:
                    bow.append(k)

    return bow

bow = bag('bare/*')
#bow = str(bow)
ff = open('output.txt', 'w')
for item in bow:  
    ff.write("%s\n" % item)