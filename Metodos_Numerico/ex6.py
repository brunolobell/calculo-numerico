import math

# f(m) = v - gm(1 - e^(-c/m * t))/c
v = 35
c = 14
t = 7
g = 9.8

def bissec(a,b,p):
  # X => Raiz procurada
  # k => Numero de iterações
  # [a,b] => intervalo que contem apenas uma raiz
  # p => precisão
  k = 0
  while abs(a - b) > p:
    k += 1
    m = (a + b) / 2
    fa = v - (g * a * (1 - math.exp((-c/a) * t))/c)
    fx = v - (g * m * (1 - math.exp((-c/m) * t))/c)
    if fa * fx > 0:
      a = m
    else:
      b = m
  return m,k

print(bissec(1,100,10**(-3)))