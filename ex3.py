import math

# X[k+1] = X[k] - f(X[k])/f'(X[k])
# E(x) = e^(-cx)[sin(wx)-dx^2]+k
# E'(x) = e^(-cx)(wcos(wx)-2dx)-ce^(-cx)(sin(wx)-dx^2)
# E''(x) = -e^(-cx)[(w^2-c^2)sin(wx)+2cwcos(wx)+dc^2x^2-4dcx+2d] 
c = 0.3
w = 3
d = 0.6
k = 6

def f(x):
  p1 = math.exp(-c * x)
  p2 = math.cos(w * x)
  p3 = math.sin(w * x)
  r = (p1 * ((w * p2) - (2 * d * x))) - (c * p1 * (p3 - (d * (x**2))))
  return r

def fl(x):
  p1 = math.exp(-c * x)
  p2 = (w**2) - (c**2)
  p3 = math.sin(w * x)
  p4 = math.cos(w * x)
  p5 = 2 * c * w * p4
  p6 = d * (c**2) * (x**2)
  p7 = 4 * d * c * x
  r = -p1*((p2 * p3) + p5 + p6 - p7)
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

print(nr(2,10**(-3)))
print(nr(0.1,10**(-3)))