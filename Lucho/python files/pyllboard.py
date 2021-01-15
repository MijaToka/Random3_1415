#VARIABLES

DIRECTORIO_ACTUAL = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Lucho/.txt Pyllboard/'
ARCHIVO = DIRECTORIO_ACTUAL + 'artistas.txt'

#FUNCIONES

def artistas(nombreArchivo):
    artistasLst = []
    file = open(nombreArchivo, 'r')
    for line in file:
        artistasLst.append(line.strip())

    file.close()
    
    return artistasLst

def visitasCancion(nombreArchivo):
    artistasLst = artistas(nombreArchivo)
    songVews = []
    for artista in artistasLst:
        file = open(DIRECTORIO_ACTUAL + artista.replace(' ','').lower() + '.txt','r')

        for line in file:
            name = ''
            for word in line.strip().split()[:-1]:
                name += word + ' '
            
            vewsStr = line.strip().split()[-1]
            vews = int(vewsStr.replace('.',''))

            songVews.append((name[:-1],vews))

        file.close()

    return songVews

def visitasArtista(artista):
    visitas = 0
    file = open(DIRECTORIO_ACTUAL + artista.replace(' ','').lower() + '.txt','r')

    for line in file:
        vewsStr = line.strip().split()[-1]
        vews = int(vewsStr.replace('.',''))
        visitas += vews
    
    file.close()
    
    return visitas

def top10(lstVisitas):
    i1ro,i2do,i3ro,i4to,i5to,i6to,i7mo,i8vo,i9no,i10mo = [0]*10

    for i,vewStats in enumerate(lstVisitas):
        if vewStats[1] >= lstVisitas[i1ro][1]:
            i10mo = i9no
            i9no = i8vo
            i8vo = i7mo
            i7mo = i6to
            i6to = i5to
            i5to = i4to
            i4to = i3ro
            i3ro = i2do
            i2do = i1ro
            i1ro = i
        elif vewStats[1] >= lstVisitas[i2do][1]:
            i10mo = i9no
            i9no = i8vo
            i8vo = i7mo
            i7mo = i6to
            i6to = i5to
            i5to = i4to
            i4to = i3ro
            i3ro = i2do
            i2do = i
        elif vewStats[1] >= lstVisitas[i3ro][1]:
            i10mo = i9no
            i9no = i8vo
            i8vo = i7mo
            i7mo = i6to
            i6to = i5to
            i5to = i4to
            i4to = i3ro
            i3ro = i
        elif vewStats[1] >= lstVisitas[i4to][1]:
            i10mo = i9no
            i9no = i8vo
            i8vo = i7mo
            i7mo = i6to
            i6to = i5to
            i5to = i4to
            i4to = i
        elif vewStats[1] >= lstVisitas[i5to][1]:
            i10mo = i9no
            i9no = i8vo
            i8vo = i7mo
            i7mo = i6to
            i6to = i5to
            i5to = i
        elif vewStats[1] >= lstVisitas[i6to][1]:
            i10mo = i9no
            i9no = i8vo
            i8vo = i7mo
            i7mo = i6to
            i6to = i
        elif vewStats[1] >= lstVisitas[i7mo][1]:
            i10mo = i9no
            i9no = i8vo
            i8vo = i7mo
            i7mo = i
        elif vewStats[1] >= lstVisitas[i8vo][1]:
            i10mo = i9no
            i9no = i8vo
            i8vo = i
        elif vewStats[1] >= lstVisitas[i9no][1]:
            i10mo = i9no
            i9no = i
        elif vewStats[1] >= lstVisitas[i10mo][1]:
            i10mo = i

    return (lstVisitas[i1ro],lstVisitas[i2do],lstVisitas[i3ro],\
            lstVisitas[i4to],lstVisitas[i5to],lstVisitas[i6to],\
            lstVisitas[i7mo],lstVisitas[i8vo],lstVisitas[i9no],\
            lstVisitas[i10mo])

lstCancionesVisitas = visitasCancion(ARCHIVO)
top10lstCancionesVisitas = top10(lstCancionesVisitas)
print(top10lstCancionesVisitas)
#PROGRAMA


def main():

    ##Crear archivo rank_canciones.txt
    lstCancionesVisitas = visitasCancion(ARCHIVO)
    lstCancionesVisitas.sort(key= lambda tuple: tuple[1],reverse=True)
    file = open(DIRECTORIO_ACTUAL + 'rank_canciones.txt','w')

    i = 0
    for cancion,vews in lstCancionesVisitas[:10]:
        i += 1
        file.write(f'{i} {cancion} {vews}\n')

    file.close()

    ##Crear archivo rank_artistas.txt

    lstArtistas = artistas(ARCHIVO)
    lstArtistasVisitas = []
    for artista in lstArtistas:
        lstArtistasVisitas.append((artista,visitasArtista(artista)))

    lstArtistasVisitas.sort(key= lambda tuple: tuple[1],reverse=True)

    file = open(DIRECTORIO_ACTUAL + 'rank_artistas.txt','w')
    i = 0
    for artista,vews in lstArtistasVisitas[:10]:
        i += 1
        file.write(f'{i} {artista} {vews}\n')

    file.close()

    return

def main2():
    ##Crear archivo rank_canciones.txt
    lstCancionesVisitas = visitasCancion(ARCHIVO)
    top10lstCancionesVisitas = top10(lstCancionesVisitas)
    file = open(DIRECTORIO_ACTUAL + 'rank_canciones.txt','w')

    i = 0
    for cancion,vews in top10lstCancionesVisitas:
        i += 1
        file.write(f'{i} {cancion} {vews}\n')

    file.close()

    ##Crear archivo rank_artistas.txt

    lstArtistas = artistas(ARCHIVO)
    lstArtistasVisitas = []
    for artista in lstArtistas:
        lstArtistasVisitas.append((artista,visitasArtista(artista)))

    top10lstArtistasVisitas =  top10(lstArtistasVisitas)
    file = open(DIRECTORIO_ACTUAL + 'rank_artistas.txt','w')
    i = 0
    for artista,vews in top10lstArtistasVisitas:
        i += 1
        file.write(f'{i} {artista} {vews}\n')

    file.close()

    return

main()