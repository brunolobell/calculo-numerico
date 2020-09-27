#Métode de Newton-Raphson
import math

# X[k+1] = X[k] - f(X[k])/f'(X[k])
# f(x) = -0.4x^2 + 2.2x + 4.7
# f'(x) = (22-8x)/10

def f(x):
  r = -(0.4 * (x**2)) + (2.2 * x) + 4.7
  return r

def fl(x):
  r = (22 - 8 * x) / 10
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

print(nr(0,10**(-10)))
print(nr(10,10**(-10)))