import estructura

estructura.crear('tiempo','horas minutos')

[t1,t2,t3,t4] = [tiempo(23,59),tiempo(0,0),tiempo(12,0),tiempo(0,1)]

def aString(tiempo):
    return str(tiempo.horas)+':'+str(tiempo.minutos)

#Casos de prueba
assert aString(t1) == '23:59'
assert aString(t2) == '0:0'
assert aString(t3) == '12:0'
assert aString(t4) == '0:1'

def enMinutos(tiempo):
    return tiempo.horas*60 + tiempo.minutos

#Casos de prueba
assert enMinutos(t1) == 1439
assert enMinutos(t2) == 0
assert enMinutos(t3) == 720
assert enMinutos(t4) == 1

def sumar(tiempo1,tiempo2):
    if tiempo1.minutos + tiempo2.minutos >= 60:
        minutos = tiempo1.minutos + tiempo2.minutos - 60
        horas = (tiempo1.horas + tiempo2.horas + 1) % 24
        
    else:
        minutos = tiempo1.minutos + tiempo2.minutos
        horas = (tiempo1.horas + tiempo2.horas) % 24
        
    return tiempo(horas,minutos)

#Casos de prueba
assert sumar(t1,t4) == t2
assert sumar(t2,t3) == t3

def restar(tiempo1,tiempo2):
    if tiempo1.minutos - tiempo2.minutos < 0:
        minutos = tiempo1.minutos - tiempo2.minutos + 60
        horas = (tiempo1.horas - tiempo2.horas - 1)
        
    else:
        minutos = tiempo1.minutos - tiempo2.minutos
        horas = (tiempo1.horas - tiempo2.horas) 
        
    return tiempo(horas,minutos)

#Casos de prueba
assert restar(t1,t1) == t2
assert restar(t3,t1) == tiempo(-12,1)

def comparar(tiempo1,tiempo2):
    if tiempo1.horas == tiempo2.horas:
        if tiempo1.minutos == tiempo2.minutos:
            return 0
        
        elif tiempo1.minutos > tiempo2.minutos:
            return 1
        
        else:
            return -1
        
    elif tiempo1.horas > tiempo2.horas:
        return 1
    
    else:
        return -1
        
#Casos de prueba
assert comparar(t1,t1) == 0
assert comparar(t3,t1) == -1
assert comparar(t4,t2) == 1      
        
        
estructura.crear('punto2D','x y')

[p0,p1,p2,p3,p4] = [punto2D(0,0),punto2D(0,1),punto2D(1,0),punto2D(3,4),punto2D(8,15)]      

def distancia(punto1,punto2):
    dx = punto2.x - punto1.x
    dy = punto2.y - punto1.y
    
    return (dx**2 + dy**2) **.5

#Casos de prueba
assert distancia(p0,p2) == 1
assert distancia(p1,p2) == 2 **.5
assert distancia(p0,p3) == 5
assert distancia(p0,p4) == 17

def pertenece(centro,radio,punto):
    [h,k,x,y,r] = [centro.x,centro.y,punto.x,punto.y,radio]
    if (x-h)**2 + (y-k)**2 == r**2:
        return 'Pertenece a la circunferencia'
    
    elif (x-h)**2 + (y-k)**2 < r**2:
        return 'Está dentro de la circunferencia'
    
    else:
        return 'Está fuera de la circunferencia'
    
#Casos de prueba
onCirc= 'Pertenece a la circunferencia'
inCirc = 'Está dentro de la circunferencia'
outCirc = 'Está fuera de la circunferencia'
assert pertenece(p0,1,p1) == onCirc
assert pertenece(p0,1,p2) == onCirc
assert pertenece(p3,2,p4) == outCirc
assert pertenece(p0,15,p3) == inCirc
            