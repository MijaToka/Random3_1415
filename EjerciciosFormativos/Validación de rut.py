
def calcular_dv(rut):
  """
   Calcula el DV correspondiente al RUT entregado.
    
   rut : string
      rut sin digito verificador
  """
  lista = [2,3,4,5,6,7]
  sumDv = 0
  for i in reversed(range(len(rut))):
    
    j = len(rut) - i - 1
    sumDv += int(rut[i]) * lista[j % len(lista)]

  floorDv = sumDv // 11
  upDv = floorDv * 11
  preDv = sumDv  - upDv
  Dv = 11 - preDv


  if Dv == 11:
    return 0 
  
  elif Dv == 10:
    return 'K'

  else:
    return Dv

def parsear_rut(rut):
    """
    Parsea el rut entregado.
    
    rut : string
        rut con digito verificador
    """  
    output = [rut[-1]]
    section = ''

    for i in reversed(range(len(rut)-1)):
      x = rut[i]

      if (x == '-' or x == '.') and len(section) > 0 or len(section) > 2:
        output = [section] + output
        section = ''

      if ord(x)>= ord('0') and ord(x) <= ord('9') + 1:
        section = x + section
    
    output = [section] + output
    return output

def parsear_rut_while(rut):
    """
    Parsea el rut entregado.
    
    rut : string
        rut con digito verificador
    """  
    output = [rut[-1]]
    section = ''
    i = len(rut)-2
    while i >= 0:
      x = rut[i]

      if (x == '-' or x == '.') and len(section) > 0 or len(section) > 2:
        output = [section] + output
        section = ''

      if ord(x)>= ord('0') and ord(x) <= ord('9') + 1:
        section = x + section
      i -= 1
    output = [section] + output
    return output

def parsear_rut_replace(rut):
    """
    Parsea el rut entregado.
    
    rut : string
        rut con digito verificador
    """
    rutLimpio = rut.replace('.','')  
    rutLimpio = rut.replace(',','')
    rutLimpio = rut.replace('-','')
    output = [rut[-1]]
    section = ''
    i = len(rutLimpio)-2
    while i >= 0:
      x = rutLimpio[i]

      if len(section) > 2:
        output = [section] + output
        section = ''

      if ord(x)>= ord('0') and ord(x) <= ord('9') + 1:
        section = x + section
      i -= 1
    output = [section] + output
    return output

def validar_rut(rut):
    """
    Valida el RUT entregado, sin importar formato.
    
    rut : string
        rut con digito verificador
    """
    #primero transformar el rut a un string "puro" que solo contiene numeros
    parseado = parsear_rut(rut)
    rutLimpio = ''

    for i in range(len(parseado)):
      rutLimpio += parseado[i]

    #luego evaluar el DV

    rutSinDv = rutLimpio[:-1]
    DvPresentado = rutLimpio[-1]
    Dv = calcular_dv(rutSinDv)

    if DvPresentado == str(Dv):
      return True

    else:
      return False

'''
# APPENDICE

## Notas

1. Para verificar, es necesario, que el rut tenga el digito verificador y que el resto del rut esté bien ingresado.


2. Proyecto Avanzado: 
    - Obtener nombre y dirección de las personas a quién pertenecen los ruts con un "scraper" de páginas web. 
    - Librerias de interes: Scrapy, Selenium
    - Conocimientos que aprenderas: entender código de páginas web (HTML), hacer solicitudes (requests) de internet, manejo de Python y programación orientada a objetos.

## Referencias

Paginas de interes:
- https://nombrerutyfirma.cl 
- https://genealog.cl
- https://validarutchile.cl/que-es-el-rut.php
- https://validarutchile.cl/calcular-digito-verificador.php
- https://www.google.com/search?client=firefox-b-m&q=Validador+de+rut&sa=X&ved=2ahUKEwiS0tH_vYHsAhUKIrkGHcOmDikQ1QJ6BAgEEAo
- http://www.sii.cl/pagina/jurisprudencia/dfl3rut.htm
'''