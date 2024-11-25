#This is a file that comptes the first fibonacci numbers
# The Fibonacci numbers are the numbers in the following integer sequence.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.

def fibonacci_numbers(n):
    """
    Generate and print the Fibonacci sequence up to the n-th term.
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1.
    Parameters:
    n (int): The number of terms in the Fibonacci sequence to generate. Must be a positive integer.
    Returns:
    None
    Example:
    >>> fibonacci_numbers(5)
    0
    1
    1
    2
    3
    """
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

if __name__ == "__main__":
    fibonacci_numbers(10)