import mpmath

# X[k+1] = X[k] - f(X[k])/f'(X[k])
# f(x) = 1/x[sinh(ax)-sinh(bx)]-L=0
# f'(x) = (acosh(ax)-bcosh(bx))/x - (sinh(ax)-sinh(bx))/x^2
a = -30
b = 15
L = 120

def f(x):
  r = ((1/x)*(mpmath.sinh(a*x) - mpmath.sinh(b*x))) - L
  return r

def fl(x):
  p1 = a*mpmath.cosh(a*x)
  p2 = b*mpmath.cosh(b*x)
  p3 = mpmath.sinh(a*x)
  p4 = mpmath.sinh(b*x)
  r = ((p1 - p2)/x) - ((p3 - p4)/(x**2))
  return r

def nr(x0,p):
  # X => Raiz procurada
  # k => Numero de iteracoes
  # x0 => Aproximacao inicial
  # p => Precisão
  x = x0 - (f(x0)/fl(x0))
  k = 1
  while abs(x - x0) > p:
    k += 1
    x0 = x
    x = x0 - (f(x0)/fl(x0))
    print(k)
  return x,k

print(nr(0.1,10**(-5)))