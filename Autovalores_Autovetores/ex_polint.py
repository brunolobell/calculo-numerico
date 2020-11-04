import numpy as np

def polint(x,fx):
  # a = Coeficiente do Polinomio
  # [x,fx] = pontos conhecidos
  nc = np.max(np.shape(x))
  A = np.zeros((nc,nc))
  for i in range(nc):
    for j in range(nc):
      A[i][j] = x[i]**(j)
  return np.dot(np.linalg.inv(A),fx)

x = np.array([[-1],[0],[2]])
fx = np.array([[4],[1],[-1]])
print(polint(x,fx))