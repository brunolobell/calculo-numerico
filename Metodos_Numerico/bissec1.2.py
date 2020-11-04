#Metodo da Bisseccao
import math

# f(x) = -2+7x-5x^2+6x^3

def bissec(a,b,p):
  # X => Raiz procurada
  # k => Numero de iterações
  # [a,b] => intervalo que contem apenas uma raiz
  # p => precisão
  k = 0
  while abs(a - b) > p:
    k += 1
    x = (a + b) / 2
    fa = (6*(a**3)) - (5*(a**2)) + (7*a) - 2
    fx = (6*(x**3)) - (5*(x**2)) + (7*x) - 2 
    if fa * fx > 0:
      a = x
    else:
      b = x
  return x,k

print(bissec(-1,1,10**(-3)))