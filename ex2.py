import mpmath

# X[k+1] = X[k] - f(X[k])/f'(X[k])
# f(x) = 1/x[sinh(ax)-sinh(bx)]-L=0
# f'(x) = (sinh(30x) - 15x(2cosh(30x)) + cosh(15x) + sinh(15x)) / x^2

def f(x):
  r = ((1/x)*(mpmath.sinh(-30*x) - mpmath.sinh(15*x))) - 120
  return r

def fl(x):
  p1 = mpmath.sinh(30 * x)
  p2 = 15 * x * (2 * mpmath.cosh(30 * x))
  p3 = mpmath.cosh(15 * x)
  p4 = mpmath.sinh(15 * x)
  r = (p1 - p2 + p3 + p4) / (x**2)
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
  return x,k

print(nr(0.01,10**(-3)))