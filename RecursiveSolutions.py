def printN (n) :
    if n>0 :
        printN(n-1)
        print(n , end=" ")

def printNreverse (n) :
    if n>0 :
        print(n , end=" ")
        printNreverse(n-1)

def printNOdd (n) :
    if n>0 :
        printNOdd(n-1)
        print(2*n-1, end=" ")

def printNOddReverse (n) :
    if n>0 :
        print(2*n-1, end=" ")
        printNOddReverse(n-1)

def printNEven (n) :
    if n>0 :
        printNEven(n-1)
        print(2*n, end=" ")

def printNEvenReverse (n) :
    if n>0 :
        print(2*n, end=" ")
        printNEvenReverse(n-1)

# printN(10)
# printNreverse(10)
# printNOdd(10)