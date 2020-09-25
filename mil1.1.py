import math

# f(x) = x - Φ(x) = 0
# f(x) = -2+7x-5x^2+6x^3
# Φ(x) = 1/7 * (-6x^3 + 5x^2 + 2)

def fi(x):
  r = -((6*(x**3))/7) + ((5*(x**2))/7) + (2/7)
  return r

def mil(x0,p):
  # X => Raiz procurada
  # k => Numero de iteracoes
  # x0 => Aproximacao inicial
  # p => Precisão
  x = fi(x0)
  k = 1
  
  while abs(x - x0) > p:
    k += 1
    x0 = x
    x = fi(x0)
  
  return x,k

print(mil(0,10**(-4)))