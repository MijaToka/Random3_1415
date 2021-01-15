def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
def raizIter(x,n):
    '''entrega r_n (raiz de x despues de n<=0 aproximaciones)'''
    r = x/2  
    if x < 0:
         return 'Out of Dom'
     
    else:
      for i in range(n):
        r = .5*(r + (x/r))
    
    return r

def raizRecur(x,n):
   '''entrega r_n (raiz de x despues de n<=0 aproximaciones)'''
   #x_n = 1/2 * (r_n-1 + x/r_n)
   if n == 0:
       return x/2
     
   elif n != 0:
       return .5 * (raizRecur(x,n-1) + (x / raizRecur(x,n-1)))
           
def permutacion(x,y):
    
    permutation = factorial(x)//factorial(x-y)
    
    return permutation

def combinaciones(x,y):
    
    combinacion = factorial(x)//(factorial(x-y)*factorial(y))
    
    return combinacion

def divisionesRecur(x,y,n=0):
    
    if x%y != 0:
        return n
        
    else:
        n += 1
        return divisionesRecur(x//y,y,n)
    
def divisionesIter(x,y,n=0):
    
    while x%y == 0:
        n += 1
        x = x//y
        
    return n