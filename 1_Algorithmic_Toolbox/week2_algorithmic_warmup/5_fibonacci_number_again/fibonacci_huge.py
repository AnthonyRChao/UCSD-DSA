# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge(n, m):
    # Find the periodic_length
    # Find the remainder, r of n when divided by periodic_length 
    # Return Fr mod m 
     
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        print(previous, current)
        previous, current = current, previous + current
        if previous % m == 0 and current % m == 1:
            print('found the periodic length')
            periodic_length = i + 1
            remainder = n % periodic_length
            print('periodic_length:', periodic_length)
            print('remainder:', remainder)
            break
    
    return True 

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
