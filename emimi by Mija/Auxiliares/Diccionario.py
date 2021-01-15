#representacion de un objeto de clase Diccionario
#self.__D={ palabra:significado, � }
class Diccionario:
  # __init__ :  str -> Diccionario
  #crea diccionario con datos grabados en archivo
  #ej: D=Diccionario()
  def __init__(self,archivo="diccionario.txt"):
    assert type(archivo)==str
    self.__D={}
    A=open(archivo)
    for linea in A:
        i=linea.index(".")
        palabra=linea[0:i]
        significado=linea[i+1:-1]
        self.__D[palabra]=significado
    A.close()

  #buscar: str -> str
  #significado de palabra (None si no esta)
  #ej: D.buscar('hola')->"hello"
  def buscar(self,palabra):
    assert type(palabra)==str
    if palabra in self.__D:     #if self.__D.__contains__(palabra):
      return self.__D[palabra]  #return self.__D.__getitem__(palabra)
    else: 
      return None

  #agregar: str str -> bool
  #True si se agrega palabra con significado 
  #ej: D.agregar('hola','hello')->True
  def agregar(self,palabra,significado):
    assert type(palabra)==str
    assert type(significado)==str
    if palabra in self.__D:
      return False
    else:
      self.__D[palabra]=significado 
      return True

  #borrar: str -> bool
  #True si se borra palabra  
  #ej: D.borrar('hola')->True
  def borrar(self,palabra):
    assert type(palabra)==str
    if palabra in self.__D:
        del self.__D[palabra]
        return True
    else: 
        return False

  #cambiar: str str -> bool
  #True si se cambia significado de palabra 
  #ej: D.cambiar('hola','hi')->True
  def cambiar(self,palabra,significado):
    assert type(palabra)==str
    assert type(significado)==str
    if palabra in self.__D: 
      self.__D[palabra]=significado #self.__D.__setitem__(palabra,significado)
      return True
    else:
      return False
  
  #grabar: str ->
  #grabar self en archivo ordenado por palabras
  #ej: D.grabar()
  def grabar(self,archivo="diccionario.txt"):
        assert type(archivo)==str
        L=list(self.__D.keys())
        L.sort()
        A=open(archivo,"w")
        for palabra in L:
            A.write(palabra+"."+self.__D[palabra]+"\n")
        A.close()

class TestDiccionario:
  def __init__(self):
    A=open("diccionario.txt","w")
    A.write("a.A\nc.C\n")
    A.close()   
    self.D=Diccionario()
  def test(self):
    #prueba de m�todos constructor y buscar
    assert self.D.buscar("a")=="A"
    assert self.D.buscar("c")=="C"
    assert self.D.buscar("b")==None
    #prueba de metodo agregar
    assert self.D.agregar("b","B") 
    assert self.D.buscar("b")=="B"
    assert not self.D.agregar("b","B")
    #prueba de m�todo cambiar
    assert self.D.cambiar("b","BB")
    assert self.D.buscar("b")=="BB"
    assert not self.D.cambiar("d","DD")
    #prueba de metodo borrar
    assert self.D.borrar("b")
    assert self.D.buscar("b")==None
    assert not self.D.borrar("b")
    #prueba de metodo grabar
    self.D.grabar()
    s=""
    for linea in open("diccionario.txt"):
        s += linea
    assert s=="a.A\nc.C\n"
TestDiccionario().test()
 
  



