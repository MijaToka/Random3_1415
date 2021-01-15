#%%IMPORTS
import sys
from collections import namedtuple
from keyword import iskeyword

#%%DICCIONARIO MORSE
def create_unmutable(name: str, fields: str) -> None:
    """Creates an unmutable C like structure given the name of the 
    structure and it's fields. The fields are a string separated by
    a blank space, one word is one field on the structure.

    Arguments:
        name {str} -- [The name of the structure]
        fields {str} -- [A string containing the fields of the structure]

    Returns:
        None -- [Adds the new structure to the global variables of the workspace]
    """
    frame = sys._getframe(1)
    frame.f_globals[name] = namedtuple(name, fields)
    
create_unmutable("NodoBinario", "value left right")
cinco = NodoBinario('5', None, None)
cuatro = NodoBinario('4', None, None)
H = NodoBinario('H', cinco, cuatro)
s_tilda = NodoBinario('S^', None, None)
tres = NodoBinario('3', None, None)
V = NodoBinario('V', s_tilda, tres)
S = NodoBinario('S', H, V)
E_tilda = NodoBinario('É', None, None)
F = NodoBinario('F', E_tilda, None)
pregunta = NodoBinario('?', None, None)
guion_bajo = NodoBinario('_', None, None)
D_tilda = NodoBinario('Đ', pregunta, guion_bajo)
dos = NodoBinario('2', None, None)
U_puntitos = NodoBinario('Ü', D_tilda, dos)
U = NodoBinario('U', F, U_puntitos)
I = NodoBinario('I', S, U)
comillas = NodoBinario('\"', None, None)
È = NodoBinario('È', comillas , None)
L = NodoBinario('L', None, È)
punto = NodoBinario('.', None, None)
mas = NodoBinario('+', None, punto)
Ä = NodoBinario('Ä', mas, None)
R = NodoBinario('R', L, Ä)
arroba = NodoBinario('@', None, None)
À = NodoBinario('À', arroba, None)
P = NodoBinario('P', None, À)
J_tilda = NodoBinario('J^', None, None)
tilde = NodoBinario('´', None, None)
uno = NodoBinario('1', tilde, None)
J = NodoBinario('J',J_tilda, uno)
W = NodoBinario('W', P, J)
A = NodoBinario('A', R, W)
E = NodoBinario('E', I, A)
guion = NodoBinario('-', None, None)
seis = NodoBinario('6', None, guion)
igual = NodoBinario('=', None, None)
B = NodoBinario('B', seis, igual)
slash = NodoBinario('/', None, None)
X = NodoBinario('X', slash, None)
D = NodoBinario('D', B, X)
Ç = NodoBinario('Ç', None, None)
punto_y_coma = NodoBinario(';', None, None)
exclamacion = NodoBinario('!', None, None)
vacio1 = NodoBinario(None, punto_y_coma, exclamacion)
C = NodoBinario('C', Ç, vacio1)
H_Tilda = NodoBinario('H^', None, None)
Y = NodoBinario('Y', None, None)
K = NodoBinario('K', C, Y)
N = NodoBinario('N', D, K)
siete = NodoBinario('7', None, None)
coma = NodoBinario(',', None, None)
vacio2 = NodoBinario(None, None, coma)
Z = NodoBinario('Z', siete, vacio2)
Ğ = NodoBinario('Ğ', None, None)
Ñ = NodoBinario('Ñ', None, None)
Q = NodoBinario('Q', Ğ, Ñ)
G = NodoBinario('G', Z, Q)
puntos = NodoBinario('dos puntos',None,None)
ocho = NodoBinario('8', puntos, None)
Ö = NodoBinario('Ö', ocho, None)
nueve = NodoBinario('9', None, None)
cero = NodoBinario('0', None, None)
CH = NodoBinario('CH', nueve, cero)
O = NodoBinario('O', Ö, CH)
M = NodoBinario('M', G, O)
T = NodoBinario('T', N, M)
#Nodo Final
arbolMorse = NodoBinario('', E, T)

#%%FUNCIONES
def Buscar_en_arbol(texto, a):
  """ Busca a que simbolo/letra en el arbol _a_ a que simbolo/letra
      corresponde el código morse entregado en _texto_"""
  if texto == '':
    return a.value
  if texto[0] == '-':
    return Buscar_en_arbol(texto[1:],a.right)
  elif texto[0] == '.':
    return Buscar_en_arbol(texto[1:],a.left)

def MorseATexto(m,a):
  """Traduce una secuencia de codigos Morse _m_ a un texto 'en claro' usando el arbol _a_."""
  morsechars = m.split(' ')
  txt = ''
  for char in morsechars:
    chartxt = Buscar_en_arbol(char,a)
    if chartxt == '':
      chartxt = ' '
    txt += chartxt
  return txt

#%% MAIN
print(MorseATexto(input(),arbolMorse), end='')

#%%