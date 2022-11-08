from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot, linalg

def jacobi(A,b,n=2,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed
    if x is None:
        x = zeros(len(A[0]))
    guess = x
    # Create a vector of the diagonal elements of A
    # and subtract them from A
    M = diag(A)
    # R = A -
    e = 0.000001
    test = diagflat(M)
    M_inverse = linalg.inv(diagflat(M))
    # Iterate for N times
    while 1:
        n+=1
        r = b - dot(A,x)
        t = test.transpose()
        x = x + linalg.solve(t, r)
        # x = x + dot(M_inverse,r)
        # x = (b + dot(N,x)) / M
        delta = linalg.norm(r)/ linalg.norm(guess)
        print(delta)
        if delta < e :
            break
    return x

A = array([[7,6,3],[2,5,-4],[-4,-3,8]])
b = array([16,3,1])
guess = array([1,2,3])

sol = jacobi(A,b,n=5,x=guess)

print ("A:")
pprint(A)

print ("b:")
pprint(b)

print ("x:")
pprint(sol)
