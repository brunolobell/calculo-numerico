import math

# f(x) = cosh(x)-2e^(-0.3x)

def bissec(a,b,p):
  # X => Raiz procurada
  # k => Numero de iterações
  # [a,b] => intervalo que contem apenas uma raiz
  # p => precisão
  k = 0
  while abs(a - b) > p:
    k += 1
    x = (a + b) / 2
    fa = math.cosh(a) - (2*math.exp(-0.3*a))
    fx = math.cosh(x) - (2*math.exp(-0.3*x)) 
    if fa * fx > 0:
      a = x
    else:
      b = x
  return x,k

print(bissec(0,2,10**(-4)))