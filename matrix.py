#!/usr/bin/env python


""" A sample python module for working with matrices.  
    Abraham D. Smith """

import numbers


class Matrix:

    def __init__(self, listOfLists):
        """ Construct a Matrix object from a list-of-lists, packed by row.  
            Some minimal sanity checks are in place. """
       
        if not isinstance(listOfLists,list): 
            raise ValueError("listOfLists must be a list of lists")

        if not all([ isinstance(row,list) for row in listOfLists]):
            raise ValueError("listOfLists must be a list of lists")
       
        nRows = len(listOfLists)
        nCols = len(listOfLists[0])

        if not all( [ len(row) == nCols for row in listOfLists ] ):
            raise ValueError("List-of-lists has mismatched rows, so it cannot be a Matrix.")
   
        if not all( [ all([ isinstance(elem,numbers.Number) for elem in row ])
                for row in listOfLists ]):
            raise(ValueError("A Matrix must contain Numbers"))
 
        ## give ourselves some attributes.
        self._nRows=nRows
        self._nCols=nCols
        self._dict = dict()
        for i in range(self._nRows):
            for j in range(self._nCols):
                self._dict[(i,j)]=listOfLists[i][j]
         

    def __getitem__(self,key):
        rowKey,colKey=key
        """ Get row or element """
        if not  (rowKey,colKey) in self:
            raise IndexError("Row or Column out of range for a {r} by {c} Matrix".format(r=self._nRows,c=self._nCols))
        return self._dict[(rowKey,colKey)]
        
    def __setitem__(self,key,value):
        rowKey,colKey=key
        if not (rowKey,colKey) in self:
            raise IndexError("Row or Column out of range for a {r} by {c} Matrix".format(r=self._nRows,c=self._nCols))
        if not isinstance(value,numbers.Number):
            raise ValueError("Matrix entry must be a Number")
        self._dict[(rowKey,colKey)]=value


    def __iter__(self):
        return ( keypair for keypair in sorted(self._dict) )

    def __contains__(self,(rowKey,colKey)):
        return (rowKey,colKey) in self._dict.keys()


    def dimension(self):
        """ compute the dimension of a Matrix, with minimal error correction.
            To us, matrices are lists-of-lists, packed row-by-row """
        return (self._nRows,self._nCols)  ## note, this is a tuple 


    def __add__(self,other):
        """ compute the element-by-element sum of two matrices. """
        
        if not other.dimension() == self.dimension():
            raise ValueError("Cannot add matrices of different dimensions.")

        nRows,nCols=self.dimension()
        newMatrix=Matrix( [ [0]*nCols ]*nRows )
        for i,j in newMatrix:
            newMatrix[i,j] = self[i,j] + other[i,j]

        return newMatrix

    def __rmul__(self,num):
        """ scalar multplication of a matrix """
        nRows,nCols=self.dimension()
        newMatrix=Matrix( [ [0]*nCols ]*nRows )
        for i,j in newMatrix:
            newMatrix[i,j] = num*self[i,j]
        return newMatrix

    def __equals__(self,other):
        if not other.dimension() == self.dimension():
            return False
        
        return all( [ self[i,j] == other[i,j] for (i,j) in self ])
            

    def __mul__(self, other):
        """ compute the matrix product """
        nRows,nInner=self.dimension()
        nInnerB,nCols=other.dimension()

        if not nInner == nInnerB:
            raise ValueError("Dimension mismatch for matrix multiplication.")

        newMatrix=Matrix( [ [0]*nCols ]*nRows )
        for i,j in newMatrix:
            products=[self[i,k]*other[k,j] for k in range(nInner)]
            newMatrix[i,j] = sum(products)

        return newMatrix

    def transpose(self):
        """ construct the transpose of a matrix.  This could be cleverer. """
        nCols,nRows=self.dimension()  ## SWAPPED!

        newMatrix=Matrix( [ [0]*nCols ]*nRows )
        for i,j in newMatrix:
            newMatrix[i,j] = self[j,i]
 
        return newMatrix

    def __pow__(self,num):
        """ scalar multplication of a matrix """
        nRows,nCols=self.dimension()
        if not nRows==nCols:
            raise ValueError("Cannot take a power of a non-square matrix.")
        if not type(num) == int and num >= 1:
            raise ValueError("Can only take positive integer powers.")
    
        if num==1:
            return self
    
        #print "... descending to {nn}".format(nn=num-1) 
        return self.__pow__(num-1)*self


    def __str__(self):
        """ pretty-print the matrix """
        nRows,nCols=self.dimension()
        string=""
        for i in range(nRows):
            string+="|"
            for j in range(nCols):
                string+="\t{}\t".format(self[i,j])

            string+="|\n"

        string+="\n"
        return string
        

if __name__ == "__main__":
    # This is called if we run as "./test.py" 
    print "Running example tests for Matrix class."

    A = Matrix([[ 12, 45, 167], [3, 6, 2]])
    try: 
        A1= Matrix("abcdef")
        A2= Matrix( [["a", "b", "c"], ["d", "e", "f"]] )
        A3= Matrix( [["a", "b", "c"], ["d", "e"]] )
    except Exception as e:
        print e
        pass

    B=Matrix([[ 4, 3, 1], [6, 7, 3] ])

    C=Matrix([[ 1, 2, 3, 4], [9, 2, 2, 1], [ 5, 4, 3, 2]])

    D=Matrix([[ 1,0],[0,2]])

    print A.dimension()
    print "A"
    print A
    print "B"
    print B
    print "A+B"
    print A+B
    #print add_matrix(A1,B1)  ## I find this hillarious,too
    #print add_matrix(A2,B2)  ## I find this hillarious


    #print mult_matrix(A,B)  ## throws exception
    #print mult_matrix(A,C)
    #print mult_matrix(A2,C)  ## throws exception
    print "3A"
    print 3*A

    print "At"
    print A.transpose()

    print "C"
    print C

    print "AC"
    print A*C
    #print_matrix(transpose(A))

    print "D"
    print D

    print "D**10"
    print D**10


