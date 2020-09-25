import math

# X[k+1] = X[k] - f(X[k])/f'(X[k])
# E(x) = e^(-cx)[sin(wx)-dx^2]+k
# E'(x) = -e^(-cx)[csin(wx)-wcos(wx)-cdx^2+2dx] 
# c = 0.3; w = 3; d = 0.6; k = 6

def f(x):
  p1 = math.exp(-0.3 * x)
  p2 = math.sin(3 * x)
  p3 = 0.6 * (x**2) 
  r = p1 * (p2-p3) + 6
  return r

def fl(x):
  p1 = math.exp(-0.3 * x)
  p2 = math.sin(3 * x)
  p3 = math.cos(3*x)
  p4 = 0.6 * (x**2)
  r = -p1 * ((0.3 * p2) - (3 * p3) - (0.3 * p4) + (2 * 0.6 * x))
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