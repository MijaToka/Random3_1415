import porcentaje as per

def plebicito(apruebo,rechazo,blanco,nulo):
    
    total = apruebo + rechazo + blanco + nulo
    totPar = apruebo + rechazo
    
    # % c/u vs total
    aTot = per.porcentaje(apruebo,total)
    rTot = per.porcentaje(rechazo,total)
    bTot = per.porcentaje(blanco,total)
    nTot = per.porcentaje(nulo,total)
    
    # % relativos de apruebo y rechazo
    aPar = per.porcentaje(apruebo,totPar)
    rPar = per.porcentaje(rechazo,totPar)
    
    print('')
    print('El porcentaje absoluto fue:')
    print(' ')
    print('-Apruebo: '+ str(aTot))
    print('-Rechazo: ' + str(rTot))
    print('-Blanco: ' + str(bTot))
    print('-Nulo: ' + str(nTot))
    print('')
    print('El porcentaje relativo fue:')
    print(' ')
    print('-Apruebo:' + str(aPar))
    print('-Rechazo:' + str(rPar))
    
    return

print('Ingrese cantidad total de votos para cada opción')
a = int(input('Apruebo '))
r = int(input('Rechazo '))
b = int(input('Blanco '))
n = int(input('Nulo '))
plebicito(a,r,b,n)