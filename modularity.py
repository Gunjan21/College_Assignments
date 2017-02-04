import numpy as np

#adj = np.array([[0,1,1,1,0,0,0,0,0,0],[1,0,1,1,1,0,0,0,0,0],[1,1,0,1,0,0,0,0,0,1],[1,1,1,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,1,1,1,1],[0,0,0,0,0,1,0,1,1,1],[0,0,0,0,1,1,1,0,1,1],[0,0,0,0,0,1,1,1,0,1],[0,0,1,0,0,1,1,1,1,0]])
#adj = np.array([[0,1,1,1,1,0,0,0,0,0],[1,0,1,1,1,0,0,0,0,0],[1,1,0,1,0,0,0,0,0,0],[1,1,1,0,1,1,0,0,0,0],[1,1,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,1,1,1,1],[0,0,0,0,0,1,0,1,1,1],[0,0,0,0,0,1,1,0,1,1],[0,0,0,0,0,1,1,1,0,1],[0,0,0,0,0,1,1,1,1,0]])

def numEdges(adj):
    sum = np.sum(adj)
    
    m = sum / 2
    
    return int(m)
    
def randMatrix(adj):
    M = np.array([[0 for i in range(34)]for j in range(34)], dtype=np.float)
    m = numEdges(adj)
    for i in range(len(M)):
        for j in range(len(M[i])):
            Ki = np.sum(adj[i])
            Kj = np.sum(adj[j])
            M[i][j] = float((Ki * Kj)) / (2 * m)
            
    return M
            
def modularity(adj):
    M = randMatrix(adj)
    
    B =  np.subtract(adj , M)
    
    return B
    
def maxEvalues(adj):
    
    B = modularity(adj)
    e , x = np.linalg.eigh(B)
    g = np.amax(e)
    index = np.where(e == g)
    
    return x[index[0][0]]
    
def community(adj):
    comm1 = []
    comm2 = []
    x = maxEvalues(adj)
    for i in range(len(x)):
        if x[i] > 0:
            comm1.append(i)
        else:
            comm2.append(i)
    
    return [comm1, comm2]
    
def mod(adj):
    [comm1 , comm2] = community(adj)
    B = modularity(adj)
    m = numEdges(adj)
    s = np.array([0 for i in range(34)])
    for i in range(len(s)):
        if i in comm1:
            s[i] = 1
        else:
            s[i] = -1
            
    Q = (1/(4*m))*(np.matrix.transpose(s).dot(B).dot(s))
    
    return Q
      
    
            
    
    
    