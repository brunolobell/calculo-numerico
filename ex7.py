import math

# r = 20 + (b sin(wx))/(2 - e^(ax))
# r' = (b(ae^(ax)*sin(wx)) - w(e^(ax)-2)cos(wx))/(e^(ax)-2)^2
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
    p1a = a1 * math.exp(a1*a) * math.sin(w*a)
    p2a = w * (math.exp(a1*a) - 2) * math.cos(w*a)
    p3a = (math.exp(a1 * a) - 2)**2
    fa = (b1 * (p1a - p2a)) / p3a
    
    p1x = a1 * math.exp(a1*x) * math.sin(w*x)
    p2x = w * (math.exp(a1*x) - 2) * math.cos(w*x)
    p3x = (math.exp(a1 * x) - 2)**2
    fx = (b1 * (p1x - p2x)) / p3x
    if fa * fx > 0:
      a = x
    else:
      b = x
  return x,k

print(bissec(-60,1,10**(-3)))
print(bissec(1,60,10**(-3)))