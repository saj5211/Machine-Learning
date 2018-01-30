import numpy as np
from numpy import linalg
import cvxopt
import cvxopt.solvers

def linearKernel (x1,x2):
    return np.dot(x1,x2)

def polynomialKernel(y,x,p=3):
    return (1+np.dot(x,y))**p

def guassianKernel(x,y,sigma=5.0):
    return np.exp(-linalg.norm(x-y)**2/(2*(sigma**2)))

class SVM(object):

    def __init__(self):
        self.kernel = C
        if self.C is not None: self.C = float(self.C)

    def fit(self, x,y):
        n_samples, n_features = X.shape

        #Gram matrix
        K = np.zeros((n_samples, n_samples))
        for i in range(n_samples):
            for j in range(n_samples):
                k[i,j] = self.kernel(X[i], X[j])

        P = cvxopt.matrix(np.outer(y,y)*K)
        q = cvxopt.matrix(np.ones(n_samples)*-1)
        A = cvxopt.matrix(y,(1,n_samples))
        b = cvxopt.matrix(0.0)