import numpy as np

def souriau(A):
  # A = Matriz para Calcular o Polinomio
  # c = Coefs. do polinomio
  n = np.max(np.shape(A))
  A1 = A.copy()
  d = np.zeros(n)
  d[0] = -A1.trace()
  for k in range(1,n):
    A2 = (A1 + (d[k-1] * np.identity(n))).dot(A)
    d[k] = - (1/(k+1)) * A2.trace()
    A1 = A2.copy()
  return np.append(1, d)

# Variavies segundo enunciado
A = np.array([[0,1],[0]])
print(A)
r = souriau(A)
print("Coeficientes: ", r)
lam = np.roots(r)
print("\nAutovalores:\n", lam)

n = np.max(np.shape(A))
X = np.zeros((n,1))
for i in range(n):
  w = lam[i]
  aux = A - np.identity(n, float) * w
  B1 = np.delete(aux, n-1, 1)
  Y1 = np.delete(aux, range(n-1), 1) * (-1)
  M = np.dot(B1.transpose(), B1)
  B = np.dot(B1.transpose(), Y1)
  xe = np.dot(np.linalg.inv(M), B)
  aux = np.reshape(np.ones(1),(1,1))
  x = np.concatenate((xe,aux), axis=0)
  X = np.concatenate((X,x), axis=1)
X = np.delete(X, 0, 1)
print("\nAutovetores: \n", X)
#print(np.dot(lam[0],X[:,0]))'''  