def pertenece(x,lst):
    for i in range(len(lst)):
        if lst[i] == x:
            return True
    return False

def perteneceSimple(x,lst):
    return x in lst

def esConjunto(lst):
    if len(lst) < 2:
        return True
    return not pertenece(lst[0], lst[1:]) and esConjunto(lst[1:])

def union(lst1,lst2):
    exit = []
    for elem in lst2:
        exit += [elem]
    for item in lst1:
        if not pertenece(item,lst2):
            exit += [item]
    return exit

def inter(lst1,lst2):
    endlst = []
    for item in lst1:
        if pertenece(item,lst2):
            endlst += [item]
    return endlst

def resta(lst1,lst2):
    endlst = []
    for item in lst1:
        if not pertenece(item,lst2):
            endlst += [item]
    return endlst

def iguales(lst1,lst2):
    return resta(lst1,lst2) == resta(lst2,lst1) and resta(lst1,lst2) == []

##PARTE 2
def leer(dir):
    file = open(dir,'r')
    lst = []
    for line in file:
        lst.append(line[:-1])
    file.close()
    return lst

def grabarConjunto(lst,dir):
    file = open(dir,'w')
    for elem in lst:
        file.write(str(elem)+'\n')

