def polinomiosDeHermite(n,x):
    if n==0:
        return 1
    elif n == 1:
        return 2*x
    else:
        return 2 * x * polinomiosDeHermite(n-1,x) - 2 * (n-1) *polinomiosDeHermite(n-2,x)

def interesCompuesto(inicio,interes,periodos):
    if periodos == 0:
        return inicio
    else:
        postPeriodo = inicio * (1 + interes /100)
        return interesCompuesto(postPeriodo,interes,periodos-1)
    
def producto(x,y):
    if y == 0:
        return 0
    else:
        return x + producto(x,y-1)
    
def cuociente(x,y,n= 0):
    if y == 0:
        return 'Error'
    elif y == 1:
        return x
    elif x-y < 0:
        return 0 
    else:
        return 1 + cuociente(x-y,y)