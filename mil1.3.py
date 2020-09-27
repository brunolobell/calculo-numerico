#Método da Iteração Lineal
import mpmath

# f(x) = x - Φ(x) = 0
# f(x) = -0.4x^2 + 2.2x + 4.7
# Φ(x) = (4/22)x^2 - (47/22)

def fi(x):
  r = ((4/22)*(mpmath.power(x,2))) - (47/22)
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
print(mil(8,10**(-4)))