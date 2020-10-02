import math

# r = 20 + (b sin(wx))/(2 - e^(ax))
# r' = (abe^(ax)sin(wx))/(2-e^(ax))^2 + (bwcos(wx))/(2 - e^(ax))
a1 = -0.001
b1 = 1.6
w = 0.01 * math.pi

def bissec(a,b,p):
  # X => Raiz procurada
  # k => Numero de iterações
  # [a,b] => intervalo que contem apenas uma raiz
  # p => precisão
  k = 0
  while abs(a - b) > p:
    k += 1
    x = (a + b) / 2
    p1a = a1 * b1 * math.exp(a1 * a) * math.sin(w * a)
    p2a = 2 - math.exp(a1 * a)
    p3a = b1 * w * math.cos(w * a)
    fa = (p1a / (p2a**2)) + (p3a / p2a)
    p1x = a1 * b1 * math.exp(a1 * x) * math.sin(w * x)
    p2x = 2 - math.exp(a1 * x)
    p3x = b1 * w * math.cos(w * x)
    fx = (p1x / (p2x**2)) + (p3x / p2x)
    if fa * fx > 0:
      a = x
    else:
      b = x
  return x,k

print(bissec(100,1000,10**(-3)))