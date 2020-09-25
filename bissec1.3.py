import math

# f(x) = (0.9-0.4x)/x

def bissec(a,b,p):
  # X => Raiz procurada
  # k => Numero de iterações
  # [a,b] => intervalo que contem apenas uma raiz
  # p => precisão
  k = 0
  while abs(a - b) > p:
    k += 1
    x = (a + b) / 2
    fa = (0.9 - (0.4*a)) / a
    fx = (0.9 - (0.4*x)) / x
    if fa * fx > 0:
      a = x
    else:
      b = x
  return x,k

print(bissec(1,3,10**(-4)))