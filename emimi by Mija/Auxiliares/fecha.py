import random

class fecha:
    def __init__(self,DDMMAAAA):
        
        self.date = DDMMAAAA
        self.dia = DDMMAAAA // 1000000
        self.mes = DDMMAAAA // 10000 % 100
        self.año = DDMMAAAA % 10000  
    
def bisiesto(AAAA):
       
      año = AAAA
      if año%4 == 0 and año%100 != 0 or año%400 == 0:
          return True
       
      else:
          return False
 
def diasDelMes(mes,año):
    if mes == 2:
        if bisiesto(año):
            return 29
        
        else:
            return 28
    
    elif mes == 1 or mes == 3 or mes == 5 \
        or mes == 7 or mes == 8 or mes == 10\
            or mes == 12:
                return 31
    
    else:
        return 30
    
def esFecha(DDMMAAAA):
    
    Fecha = fecha(DDMMAAAA)
    dia = Fecha.dia()
    mes = Fecha.mes()
    año = Fecha.año()
    

    if dia > 0 and dia <= diasDelMes(mes,año):
            
            if mes > 0 and mes <= 12:
                
                return True
            else:
                return False
            
    else:
        return False

def añosTranscurridos(DDMMAAAA1,DDMMAAAA2):
    
    fecha1 = fecha(DDMMAAAA1) ; fecha2 = fecha(DDMMAAAA2)
    
    dia1 = fecha1.dia() ; dia2 = fecha2.dia()
    mes1 = fecha1.mes() ; mes2 = fecha2.mes()
    año1 = fecha1.año() ; año2 = fecha2.año()
    
    años = abs(año1-año2)
    
    if año1 > año2:
        if mes2 > mes1:
            años -= 1
            
        else:
            if dia2 > dia1:
                años -= 1
    
    elif año1 < año2:
        if mes2 < mes1:
            años -= 1
            
        else:
            if dia2 < dia1:
                años -= 1
            
    return años

def esMenor(DDMMAAAA1,DDMMAAAA2):
    
    fecha1 = fecha(DDMMAAAA1) ; fecha2 = fecha(DDMMAAAA2)
    
    dia1 = fecha1.dia() ; dia2 = fecha2.dia()
    mes1 = fecha1.mes() ; mes2 = fecha2.mes()
    año1 = fecha1.año() ; año2 = fecha2.año()
    
    if año1 == año2:
        if mes1 == mes2:
            if dia1 == dia2:
                return False
            
            elif dia1 > dia2:
                return False
            
            else:
                return True
       
        elif mes1 > mes2:
            return False
        
        else:
            return True
        
    elif año1 > año2:
            return False
        
    else:
        return True
    
def difFechas(DDMMAAAA1,DDMMAAAA2):
    
    if esFecha(DDMMAAAA1):
        if esFecha(DDMMAAAA2):
            años = añosTranscurridos(DDMMAAAA1,DDMMAAAA2)                
            if esMenor(DDMMAAAA1,DDMMAAAA2):
              menor = DDMMAAAA1 ; mayor = DDMMAAAA2
              
            elif esMenor(DDMMAAAA2,DDMMAAAA1):
              menor = DDMMAAAA2 ; mayor = DDMMAAAA1 
            
            else:
              menor = 'Son iguales' ; mayor = 'Son iguales'
             
        print(f'Mayor fecha: {mayor}')
        print(f'Menor fecha: {menor}')
        print(f'Diferencia de años: {años}')
    
    else:
        print('Una fecha es incorrecta')

def fechaRandom():
      randfecha = random.randint(0,31122020)
      
      if esFecha(randfecha):
          if esMenor(1011900,randfecha) and esMenor(randfecha,31122020):
          
              return randfecha
          
          else:
              return fechaRandom()
      
      else:
          return fechaRandom()
     
def fechaCalendario(DDMMAAAA):
    
    Fecha = fecha(DDMMAAAA)
    dia = Fecha.dia()
    mes = Fecha.mes()
    año = Fecha.año()
    
    return [dia,mes,año]
    
  
    