import math

# X[k+1] = X[k] - f(X[k])/f'(X[k])
# f(x) = -2+7x-5x^2+6x^3
# f'(x) = 18x^2-10x+7

def f(x):
  r = (6*(x**3)) - (5*(x**2)) + (7*x) - 2 
  return r

def fl(x):
  r = (18*(x**2)) - (10*x) + 7
  return r

def nr(x0,p):
  # X => Raiz procurada
  # k => Numero de iteracoes
  # x0 => Aproximacao inicial
  # p => Precisão
  x = x0 - (f(x0)/fl(x0))
  k = 1
  while abs(x - x0) > p:
    k += 1
    x0 = x
    x = x0 - (f(x0)/fl(x0))
  return x,k

print(nr(-1,10**(-3)))