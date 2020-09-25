import math

# X[k+1] = X[k] - f(X[k])/f'(X[k])
# f(x) = cosh(x)-2e^(-0.3x)
# f'(x) = sinh(x) + 3/5 * e^(-3x/10)

def f(x):
  r = math.cosh(x) - (2*math.exp(-0.3*x))
  return r

def fl(x):
  r = math.sinh(x) + ((3/5) * (math.exp(-0.3*x)))
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

print(nr(0,10**(-3)))