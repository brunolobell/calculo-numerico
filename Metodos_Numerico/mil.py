import math

# f(x) = x - Φ(x) = 0
# f(x) = x^2 - e^(-x) = 0
# Φ(x) = e^(-x/2)

def fi(x):
  r = math.exp(-x/2)
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

print(mil(0,10**(-8)))