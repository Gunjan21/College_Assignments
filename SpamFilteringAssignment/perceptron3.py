from numpy import dot, random
from random import shuffle
import corp

unit_step = lambda x: 0 if x < 0 else 1  #if result is < 0 its in class 0, else its in class 1
bow = corp.corpus()

def perceptron(training_data):   
    w = random.rand(len(bow)) 
    eta = 0.5   
    for r in range(1,101):
        for t in range(len(training_data)):
            x, expected = training_data[t]
            result = dot(w, x)
            error = expected - unit_step(result)
            '''
            This is an online perceptron. Each time there is a missclassified
            vector, it updates the hyperplane.
            '''
            if error != 0:  # means missclassified : update!
                if result <= 0:
                    w += (eta/float(r)) * x
                else:
                    w -= (eta/float(r)) * x
    return w
    
