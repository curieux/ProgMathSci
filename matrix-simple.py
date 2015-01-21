#!/usr/bin/env python


""" A sample python module for working with matrices.  
    Really this should become a Matrix class, but that may be too many steps at once. 
    Abraham D. Smith """



def dimension(matrix):
    """ compute the dimension of a matrix, with minimal error correction.
        To us, matrices are lists-of-lists, packed row-by-row """
    nRows = len(matrix)
    nCols = len(matrix[0])

    if not all( [ len(row) == nCols for row in matrix ] ):
        raise ValueError("List-of-lists has mismatched rows, so it cannot be a matrix.")

    return (nRows,nCols)  ## note, this is a tuple (an immutable list)


def add_matrix(matrixA, matrixB):
    """ compute the element-by-element sum of two matrices. """

    nRows,nCols=dimension(matrixA)
    if not dimension(matrixB) == (nRows,nCols):
        raise ValueError("Cannot add matrices of different dimensions.")

    newMatrix=[]
    for i in range(nRows):
        newMatrix.append([])
        for j in range(nCols):
            newMatrix[i].append(0)
            newMatrix[i][j] = matrixA[i][j] + matrixB[i][j]
            
    return newMatrix

def scale_matrix(num,matrix):
    """ scalar multplication of a matrix """
    return [ [ num*elem for elem in row ] for row in matrix ]


def mult_matrix(matrixA, matrixB):
    """ compute the matrix product """
    nRows,nInner=dimension(matrixA)
    nInnerB,nCols=dimension(matrixB)
    nCols=dimension(matrixB)[1]

    if not nInner == nInnerB:
        raise ValueError("Dimension mismatch for matrix multiplication.")

    newMatrix=[]
    for i in range(nRows):
        newMatrix.append([])
        for j in range(nCols):
            newMatrix[i].append(0)
            products=[matrixA[i][k]*matrixB[k][j] for k in range(nInner)]
            newMatrix[i][j] = sum(products)

    return newMatrix

def transpose(matrix):
    """ construct the transpose of a matrix.  This could be cleverer. """
    nCols,nRows=dimension(matrix)  ## SWAPPED!

    newMatrix=[]
    for i in range(nRows):
        newMatrix.append([])
        for j in range(nCols):
            newMatrix[i].append(0)
            newMatrix[i][j] = matrix[j][i]
 
    return newMatrix

def pow_matrix(matrix,num):
    """ scalar multplication of a matrix """
    nRows,nCols=dimension(matrix)
    if not nRows==nCols:
        raise ValueError("Cannot take a power of a non-square matrix.")
    if not type(num) == int and num >= 1:
        raise ValueError("Can only take positive integer powers.")
    
    if num==1:
        return matrix
    
    #print "... descending to {nn}".format(nn=num-1) 
    return mult_matrix(matrix,pow_matrix(matrix,num-1))


def print_matrix(matrix):
    """ pretty-print the matrix, just to show some neat functions """
    for row in matrix:
        print "\t".join(map(str,row))


if __name__ == "__main__":
    # This is called if we run as "./test.py" 
    A = [[ 12, 45, 167], [3, 6, 2]]
    A1= "abcdef"
    A2= [["a", "b", "c"], ["d", "e", "f"]]
    A3= [["a", "b", "c"], ["d", "e"]]

    B=[[ 4, 3, 1], [6, 7, 3] ]
    B1= "xyzpqr"
    B2=[["x", "y", "z"], ["p", "q", "r" ]]

    C = [[ 1, 2, 3, 4], [9, 2, 2, 1], [ 5, 4, 3, 2]]

    D= [[ 1,0],[0,2]]

    print dimension(A)
    print dimension(A1)
    print dimension(A2)
    #print dimension(A3)  ## throws exception

    print add_matrix(A,B)
    print add_matrix(A1,B1)  ## I find this hillarious,too
    print add_matrix(A2,B2)  ## I find this hillarious


    #print mult_matrix(A,B)  ## throws exception
    print mult_matrix(A,C)
    #print mult_matrix(A2,C)  ## throws exception

    print scale_matrix(3.5,A)

    print pow_matrix(D,10)    

    print_matrix(transpose(A))
