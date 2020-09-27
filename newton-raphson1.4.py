#Metodo de Newton-Raphson
import math

# X[k+1] = X[k] - f(X[k])/f'(X[k])
# f(x) = (0.9-0.4x)/x
# f'(x) = -(9/10)x^2

def f(x):
  r = (0.9 - (0.4*x)) / x 
  return r

def fl(x):
  r = -(9/10)*(x**2)
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

print(nr(3,10**(-10)))