import time

def fatRecursiva(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fat(n-1)*n

def fatIterativa(n):
    fat = 1
    for i in range (1, n+1):
        fat = fat*i
    return fat

def fibRecursiva(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibIterativa(n):
    if n == 0:
        return 1
    else:
        x = 0
        y = 1
        for i in range(1,n):
            z = (x+y)
            x = y
            y = z
        return y

@lru_cache(maxsize=None)
def fatRecursiva2(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fat(n-1)*n

@lru_cache(maxsize=None)
def fibRecursiva2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Digite o valor de n"))

inicio = time.time()
for i in range (50000):
    fatRecursiva(n)
fim = time.time()
print("Duração %s" %(fim - inicio))

inicio = time.time()
for i in range (50000):
    fibRecursiva(n)
fim = time.time()
print("Duração %s" %(fim - inicio))

inicio = time.time()
for i in range (50000):
    fatRecursiva2(n)
fim = time.time()
print("Duração %s" %(fim - inicio))

inicio = time.time()
for i in range (50000):
    fibRecursiva2(n)
fim = time.time()
print("Duração %s" %(fim - inicio))
