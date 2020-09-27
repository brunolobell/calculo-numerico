import math

# f(x) = [1 - e^(-0.5x)]sin(0.75x)

def bissec(a,b,p):
  # X => Raiz procurada
  # k => Numero de iterações
  # [a,b] => intervalo que contem apenas uma raiz
  # p => precisão
  k = 0
  while abs(a - b) > p:
    k += 1
    x = (a + b) / 2
    fa = (1 - math.exp(-0.5 * a)) * math.sin(0.75 * a)
    fx = (1 - math.exp(-0.5 * x)) * math.sin(0.75 * x)
    if fa * fx > 0:
      a = x
    else:
      b = x
  return x,k

print(bissec(0.1,2 * math.pi,10**(-3)))