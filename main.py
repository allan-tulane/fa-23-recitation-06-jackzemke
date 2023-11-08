def fib_recursive(n, counts):
    # print(counts)
    counts[n] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib_recursive(n-1,counts) + fib_recursive(n-2,counts))

    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    

n = 10
counts = [0] * (n+1)
# print(fib_recursive(n, counts))
# print(counts)
# print(sum(counts))


    
def fib_top_down(n, fibs):
    if fibs[n] != -1:
        return fibs[n]
    elif n == 0:
        fibs[n] = 0
        return 0
    elif n == 1:
        fibs[n] = 1
        return 1
    else:
        fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
        return fibs[n]

# n = 10
# fibs = [-1] * (n+1)
# print(fib_top_down(n, fibs))
# print(fibs)



def fib_bottom_up(n):
    fibs = [0] * (n+1)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(len(fibs)):
        if i == 0 or i == 1:
            continue
        fibs[i] = fibs[i-1] + fibs[i-2]
    print(fibs)
    return fibs[n]

print(fib_bottom_up(10))

