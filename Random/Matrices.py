def fila0(n):
    '''Entrga una lista de largo n llena de 0'''
    fila = list(range(n))
    for i in range(n):
        fila[i] = 0
    return fila

def matriz0(m,n):
    '''Entrga una matriz nula de m (fila) x n (columnas) la cual se
    puede indexar de manera: 
    A[i][j] := Elemento de la fila i, columna j 
    Nota: len(A) := m y len(A[0]) := n''' 
    matrix = []
    for _ in range(m):
        matrix.append(fila0(n))
    return matrix

def mescalar(l,A):
    '''Multiplica una matriz A por un escalar l'''
    for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = l* A[i][j]
    return A 
                
def msum(A,B):
   '''Suma matricialmente A + B '''
   if len(A) != len(B) or len(A[0]) != len(B[0]):
        return 'Sum is undefined'
   else:
        C = matriz0(len(A),len(A[0]))
        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] + B[i][j]    
        return C
    
def mprod(A,B):
    '''Multiplica matricialmente A * B ''' 
    if len(A[0]) != len(B):
       return 'Product is undefined'
    else:
        C = matriz0(len(A),len(B[0]))
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]                
    return C
        
def Identidad(n):
    '''Entrega la matriz identidad de tamaño n x n'''
    In = matriz0(n,n) 
    for i in range(n):
                In[i][i] = 1            
    return In

def ElementalE(n,p,q,a):
    '''Entrega la matriz elemental de tipo E de tamaño n x n'''
    EpqA =  Identidad(n)
    EpqA[q-1][p-1] = a
    return EpqA

def ElementalI(n,p,q):
    '''Entrega la matriz elemental de tipo I de tamaño n x n'''
    Ipq = Identidad(n)
    p -= 1; q -= 1
    
    Ipq[p][p] = 0; Ipq[q][q] = 0
    Ipq[p][q] = 1; Ipq[q][p] = 1
    
    return Ipq

