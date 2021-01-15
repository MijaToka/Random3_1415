#%%FUNCIONES
def diff_tiempo(tiempo1,tiempo2):
    strhora1,strminuto1=tiempo1.split(':')
    strhora2,strminuto2=tiempo2.split(':')
    hora1=int(strhora1);minuto1=int(strminuto1)
    hora2=int(strhora2);minuto2=int(strminuto2)
    #TIEMPO1<TIEMPO2
    diff_horas=hora2-hora1
    if minuto1>minuto2:
        diff_minutos=minuto2-minuto1+60
        diff_horas-=1
    else:
        diff_minutos=minuto2-minuto1
    return diff_horas*60+diff_minutos
def datos(archivo):
    registro=open(archivo,'r')
    nombre=[]
    tipo=[]
    patente=[]
    hora_ingreso=[]
    hora_salida=[]
    for line in registro:
        linelst=line.strip().split(';')
        nombre.append(linelst[0])
        tipo.append(linelst[1])
        patente.append(linelst[2])
        hora_ingreso.append(linelst[3])
        hora_salida.append(linelst[4])
    registro.close()
    return (nombre,tipo,patente,hora_ingreso,hora_salida)
def tipo_vehiculos(archivo):
    nombre,tipos,patente,hora_ingreso,hora_salida=datos(archivo)
    lista_tipos=[]
    for tipo in tipos:
        if tipo not in lista_tipos:
            lista_tipos.append(tipo)
    dicc={}
    for tipo in lista_tipos:
        dicc[tipo]=[]
    for i,tipo in enumerate(tipos):
        dicc[tipo].append([nombre[i],tipos[i],patente[i],hora_ingreso[i],hora_salida[i]])
    for tipo in dicc:
        dicc[tipo].sort(key=lambda x:diff_tiempo(x[-2],x[-1]))
        dicc[tipo].reverse()
        file=open(tipo+'.txt','w')
        j=0
        for i in range(len(dicc[tipo])):
            j+=1
            file.write(f'{j} - El vehiculo de {dicc[tipo][i][0]} con patente {dicc[tipo][i][2]} estuvo estacionado {diff_tiempo(dicc[tipo][i][-2],dicc[tipo][i][-1])} minutos.\n')
        file.close() 
    return dicc
def vehiculos_max_tiempo(dicc,archivo):
    lista_max=[]
    for tipo in dicc:
        max_diff_tiempo=0;index=0
        for i in range(len(dicc[tipo])):
            _,_,_,Hora_ingreso,Hora_salida=dicc[tipo][i]
            diff_time=diff_tiempo(Hora_ingreso,Hora_salida)
            if diff_time>max_diff_tiempo:
                max_diff_tiempo=diff_time
                index=i
        lista_max.append(dicc[tipo][index])
    return lista_max
def total_vehiculos(registro):
    nombre,_,_,_,_=datos(registro)
    return len(nombre)

#%%DEFINICIONES
registro = 'registros.txt'
(nombre,tipo,patente,hora_ingreso,hora_salida)=datos(registro)


#%%PROGRAMA
lista_tipos=tipo_vehiculos(registro)
tiempos_max=vehiculos_max_tiempo(lista_tipos,registro)
total=total_vehiculos(registro)
print("Vehículos con mayor tiempo de estacionamiento, por tipo:")
for i in range(len(tiempos_max)):
    print(f'{tiempos_max[i][1]}: {tiempos_max[i][2]} ({tiempos_max[i][0]})')
print(f'Total de vehículos en el día: {total}')
