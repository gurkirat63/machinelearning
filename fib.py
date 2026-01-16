from commonutils import timeit, funcname


@timeit
@funcname
def fib_seq_classic(x):
    if x ==1 :
        return [0]
    if x == 2:
        return [1]
    a,b = 0,1
    seq = [0,1]
    for i in range(2,x):
        c = a+b
        a = b
        b = c
        seq.append(c)
    return seq    
        
def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib(x-1)+fib(x-2)
    
@timeit
@funcname
def fib_seq_recursion(x):
    seq = []
    for i in range(x):
        seq.append(fib(i))
    return seq    

def fib_dynamic(x, memo=None):
    if memo is None:
        memo = {}
    if x in memo:
        return memo[x]
    if x == 0:
        memo[x] = 0
        return 0
    if x == 1:
        memo[x] = 1
        return 1
    memo[x] = fib_dynamic(x-1, memo) + fib_dynamic(x-2, memo)
    return memo[x]
    
@timeit
@funcname
def fib_seq_recursion_dynamic(x):
    seq = []
    for i in range(x):
        seq.append(fib_dynamic(i))
    return seq  


print(fib_seq_classic(10))

print(fib_seq_recursion(10))

print(fib_seq_recursion_dynamic(10))