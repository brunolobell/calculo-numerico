import math

# f(x) = [1 - e^(-0.5x)]sin(0.75x)
# f'(x) = (1/2)(sin(3x/4)e^(-x/2)) + (3/4)cos(3x/4)(1-e^(-x/2))

def bissec(a,b,p):
  # X => Raiz procurada
  # k => Numero de iterações
  # [a,b] => intervalo que contem apenas uma raiz
  # p => precisão
  k = 0
  while abs(a - b) > p:
    k += 1
    x = (a + b) / 2
    fa = ((1/2)*(math.sin((3*a)/4)*math.exp(-a/2))) + ((3/4)*math.cos((3*a)/4)*(1 - math.exp(-a/2)))
    fx = ((1/2)*(math.sin((3*x)/4)*math.exp(-x/2))) + ((3/4)*math.cos((3*x)/4)*(1 - math.exp(-x/2)))
    if fa * fx > 0:
      a = x
    else:
      b = x
  return x,k

print(bissec(-1,1,10**(-3)))
print(bissec(1,4,10**(-3)))
print(bissec(4,2*math.pi,10**(-6)))