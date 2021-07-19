#Metodo da Bisseccao
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
    fa1 = -(a**2) + (0.4*math.sin(5*a)) + 3
    fx1 = -(x**2) + (0.4*math.sin(5*x)) + 3
    fa2 = (a**2) + (0.8*math.cos(3*a))
    fx2 = (x**2) + (0.8*math.cos(3*x))
    if (fa2 - fa1) * (fx2 - fx1) > 0:
      a = x
    else:
      b = x
  return x,k

print(bissec(-2,-1,10**(-4)))
print(bissec(1,2,10**(-4)))