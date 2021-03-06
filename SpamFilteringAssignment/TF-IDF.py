#TF-IDF
from numpy import array, dot, multiply
import glob
from random import shuffle
from math import log
import perceptron3
import corp

bow = corp.corpus()

def preprocessing():
    bowfinal = []
    ff=open('stop_words.txt','r')
    sw = ff.readlines()
    ff.close()
    sw=[sw[i].replace('\n','') for i in range(0,len(sw))]
    p=glob.glob('bare/*')
    spc=[('-',' '),('*',' '),('/',' '),('%',' '),('_',' '),('#',' '),('|',' ')]
    pp=[]
    for i in p:
        pp.append(glob.glob(i+'/*'))
    pp=sum(pp,[]) 
    word = [0 for o in range(len(bow))]
    D = 1
    for i in range(0,len(pp)):
        with open(pp[i]) as f:
            D += 1
            data = f.read()
            data = data.replace('\n','')
            for k, v in spc:
                data = data.replace(k, v)
            data = data.split()
            data = [data[j] for j in range(0,len(data)) if data[j] not in sw]
            data = [data[j] for j in range(0,len(data)) if len(data[j])>2]
            bowspam = [0 for o in range(len(bow))]
            bowham = [0 for o in range(len(bow))]
            z=set(data)
            for l in range(len(bow)):
                if bow[l] in z:
                    word[l] += 1
    word = array([0 if x == 0 else log(1+(D/(1+x))) for x in word])
    
    for i in range(0,len(pp)): 
        with open(pp[i]) as f:
            D += 1
            data = f.read()
            data = data.replace('\n','')
            for k, v in spc:
                data = data.replace(k, v)
            data = data.split()
            data = [data[j] for j in range(0,len(data)) if data[j] not in sw]
            data = [data[j] for j in range(0,len(data)) if len(data[j])>2]
            bowspam = [0 for o in range(len(bow))]
            bowham = [0 for o in range(len(bow))]
            z=set(data)
            if 'spmsg' in pp[i]:
                for l in range(len(bow)):
                    if bow[l] in z:
                        bowspam[l] += 1
                        word[l] += 1
                m1 = max(i for i in bowspam)
                bowspam = multiply(word,array([0 if x == 0 else (0.5 + 0.5*x/m1) for x in bowspam]))
                bowfinal.append((bowspam,0))
            else:
                for l in range(len(bow)):
                    if bow[l] in z:
                        bowham[l] += 1
                        word[l] += 1
                m2 = max(i for i in bowham)
                bowham =  multiply(word,array([0 if x == 0 else (0.5 + 0.5*x/m2) for x in bowham]))
                bowfinal.append((bowham,1))

    return bowfinal

#testing by 10-fold cross validation
def testing():
    data = preprocessing()
    shuffle(data)
    division = len(data) / 10
    #splitting the data into 10 parts
    data = [ data[int(round(division * i)): int(round(division * (i + 1)))] for i in range(10) ]
    acc = []
    for i in range(len(data)): #len(data) = 10 here
        print('Validation #', i+1)
        count = 0
        test_data = data[i]
        training_data = [data[x] for x in range(len(data)) if x!=i]
        training_data  = sum(training_data,[])
        w = perceptron3.perceptron(training_data)
        for y, _ in test_data:
            final = dot(w, y)
            errors = perceptron3.unit_step(final) - _
            if errors == 0:
                count += 1   
        total = len(test_data)
        accuracy = (count/total)*100
        print('Accuracy here :', accuracy)
        acc.append(accuracy)
    
    g = 0
    for i in acc:
        g += i
        
    AvgAcc = g / float(10)
    
    print('The average Accuracy after 10-fold cross validation is :', AvgAcc)
    
