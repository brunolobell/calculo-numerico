#Metodo da iteracao linear
import math

# f(x) = x - Φ(x) = 0
# f(x) = cosh(x)-2e^(-0.3x)
# Φ(x) = -10/3(ln(cosh(x)) - ln(2))

def fi(x):
  r = -(10/3)*(math.log(math.cosh(x)) - math.log(2))
  return r

def mil(x0,p):
  # X => Raiz procurada
  # k => Numero de iteracoes
  # x0 => Aproximacao inicial
  # p => Precisão
  x = fi(x0)
  k = 1
  
  while abs(x - x0) > p:
    k += 1
    x0 = x
    x = fi(x0)
  
  return x,k

print(mil(0,10**(-4)))