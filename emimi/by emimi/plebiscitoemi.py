import porcentajeemi as p
def plebiscito(a,r,b,n):
    totalabsoluto= a+r+b+n
    totalrelativo= a+r
    paa= p.porcentaje(a,totalabsoluto)
    pra= p.porcentaje(r,totalabsoluto)
    pba= p.porcentaje(b,totalabsoluto)
    pna= p.porcentaje(n,totalabsoluto)
    par= p.porcentaje(a,totalrelativo)
    prr= p.porcentaje(r,totalrelativo)
    
    print("resultados en porcentajes")
    print("apruebo: "+str(paa))
    print("rechazo: "+str(pra))
    print("blanco: "+str(pba))
    print("nulo: "+str(pna))
    print("Porcentajes sin blancos y nulos")
    print("apruebo: "+str(par))
    print("rechazo: "+str(prr))
    