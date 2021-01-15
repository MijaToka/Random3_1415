# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:29:26 2020

@author: Admin
"""

def decimalABinario(n10,n2= ''):
  """Traduce una representacion decimal de un valor a su representacion binaria."""
  if n10 == '0' and n2 == '':
    return '0'
  
  elif n10 == '0' or n10 == '':
    return ''
  
  else:
    if int(n10) % 2 == 1:
      n2 = n2 + '1'
      return  decimalABinario( str((int(n10)//2)),n2 ) + '1'
    
    elif int(n10) % 2 == 0:
      n2 = n2 + '0'
      return decimalABinario( str((int(n10)//2)),n2 ) + '0'

print(decimalABinario(input()), end='')