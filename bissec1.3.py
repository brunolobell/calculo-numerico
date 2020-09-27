# Método da Bissecção
import math

# f(x) = -0.4x^2 + 2.2x + 4.7

def bissec(a,b,p):
  # X => Raiz procurada
  # k => Numero de iterações
  # [a,b] => intervalo que contem apenas uma raiz
  # p => precisão
  k = 0
  while abs(a - b) > p:
    k += 1
    x = (a + b) / 2
    fa = -(0.4*(a**2)) + (2.2*a) + 4.7
    fx = -(0.4*(x**2)) + (2.2*x) + 4.7 
    if fa * fx > 0:
      a = x
    else:
      b = x
  return x,k

print('f(x) = -0.4x^2 + 2.2x + 4.7')
print(bissec(-5,1,10**(-3)))
print(bissec(1,10,10**(-3)))