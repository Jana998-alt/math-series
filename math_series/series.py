def fibonacci (n):
    """ DocString
        this function calculates the fibonacci series elements. it takes in the one parameter (index) value and returns the element of the series for that index.
    """

    if n == 0:
        return 0
    if n== 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    if n < 0:
        return None


def Lucas(n):
    """ DocString
        this function calculates the fibonacci series elements. it takes in the one parameter (index) value and returns the element of the series for that index.
    """
    if n == 0:
        return 2
    if n== 1:
        return 1
    if n > 1:
        return Lucas(n-1) + Lucas(n-2)
    if n < 0:
        return None
    
    

def sum_series(n, i=None, j=None):
    """ DocString
        this function calculates a series elements for a series similar to Fibonacci series but with different initial value. it takes in the three parameter (index, index 0 value, index 1 value) value and returns the element of the series for that index.
    """
    if n < 0:
        return None
    
    if not (i or j):
        i = 0
        j = 1
    
    elif not i:
        i = 0

    elif not j:
        j = 1

    if n== 0:
        return i
    if n ==1:
        return j
    else:
        return sum_series(n-1, i, j) + sum_series(n-2, i, j)

    