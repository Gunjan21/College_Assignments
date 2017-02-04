def corpus():
    f = open('output.txt','r')
    bow = f.readlines()
    f.close()
    bow=[bow[i].replace('\n','') for i in range(0,len(bow))]

    return bow

