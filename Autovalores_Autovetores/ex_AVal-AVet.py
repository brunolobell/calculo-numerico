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

#A = np.array([[-3,1,-9],[0,2,-8],[1,-1,1]])
A = np.array([[0,2],[1,1]])
r = souriau(A)
print(r)
lam = np.roots(r)
print(lam)

for i in range(np.max(np.shape(A))):
  w = lam[i]
  B1 = np.array([[A[0][0] - w, A[0][1]], [A[1][0], A[1][1] - w], [A[2][0], A[2,1]]])
  Y1 = np.array([[-A[0][2]],[-A[1][2]],[-(A[2][2] - w)]])
  M = np.dot(B1.transpose(), B1)
  B = np.dot(B1.transpose(), Y1)
  xe = np.dot(np.linalg.inv(M), B)
  x = np.insert(xe, [2], [1], axis=0)
  if i == 0:
    X = x
  else:
    X = np.concatenate((X,x), axis=1)
print(X)
#print(np.dot(lam[0],X[:,0]))