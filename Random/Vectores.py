from math import sqrt
def prodEscalar(l,v):
  prod = []
  for elem in v:
    prod.append(l*elem)
  return prod
assert prodEscalar(2,[1,1,1]) == [2,2,2]
assert prodEscalar(1/5,[35,15,5]) == [7.0,3.0,1.0]

def vectorSum(x,y):
  assert len(x) == len(y), 'Inconcongruent vectors.'
  suma = []
  for i in range(len(x)):
    suma.append(x[i]+y[i])
  return suma
assert vectorSum([1,1,1],[1,1,1]) == [2,2,2]
assert vectorSum([1,1,1],[0,0,1]) == [1,1,2]

def prodPunto(x,y):
  assert len(x) == len(y), 'Inconcongruent vectors.'
  prod = 0
  for i in range(len(x)):
    prod += x[i] * y[i]
  return prod

def norma(x):
  return sqrt(prodPunto(x,x))

def proy(x,y):
  return prodEscalar(prodPunto(x,y)/norma(x),x)

def GSmethod(vectorlst):
  v = [0]*len(vectorlst)
  vhat = [0]*len(vectorlst)
  for i,ui in enumerate(vectorlst):
    if i == 0:
        v[0] = ui
    else:
        v[i] = [0]*len(ui)
        for j in range(i): 
            v[i] = vectorSum(v[i],proy(vhat[j],ui))
        v[i] = vectorSum(vectorlst[i],prodEscalar(-1,v[i]))
    vhat[i]=prodEscalar(1/norma(v[i]),v[i])    
  return vhat

#PROGRAM
A = [1,1,0,0]
B = [0,1,1,0]
C = [0,0,1,1]
D = [1,0,-1,0]
GS = GSmethod([A,B,C])
for i in range(len(GS)):
    print(GS[i])
for j in range(len(GS)):
  print(f'El {j}-esimo vector es de norma {norma(GS[j])}')
 

