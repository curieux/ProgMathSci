import matrix
import abe

X=matrix.Matrix(abe.X)
Y=matrix.Matrix(abe.Y)
P=matrix.Matrix(abe.P)
I=matrix.Matrix(abe.I)
print P.transpose()*P  == I   # verify P is orthogonal
## This may be FALSE!  depending on how test is done.
print P.transpose()*P
print I
print P.transpose()*P == (1.0)*I  ## Maybe this is True, depending on implementation
print P.transpose()*P + (-1.0)*I  ## maybe this shows machine erroe


print P*P.transpose() + (-1.0)*I   # verify P is orthogonal, again

print Y
print P*X
print Y  == P*X
print Y + (-1.0)*P*X           # verfiy P is coordinate change from X to Y


n=X.dimension()[1]
CX = (1.0/float(n-1))*(X*X.transpose())  # correlation matrix, n = X.dimension()[1]
print CX
CY = (1.0/float(n-1))*(Y*Y.transpose())  # correlation matrix, same n
print CY
print CY + (-1)*P*CX*P.transpose()          # verify coordinate change works for correlation, bottom of left side of page 7
variances = [ CY[i,i] for i in range(CY.dimension()[0] ) ] ## CY is diagonal, its entries are variances
print variances



## finally, let's import numpy to see the "allclose" routine
from numpy import allclose
print allclose([0.00000000000001], [0])
