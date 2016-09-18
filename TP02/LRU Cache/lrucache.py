import time
from functools import lru_cache

def fatRecursiva(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fatRecursiva(n-1)*n

def fatIterativa(n):
    fat = 1
    for i in range (1, n+1):
        fat = fat*i
    return fat

def fibRecursiva(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibRecursiva(n-1) + fibRecursiva(n-2)

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
        return fatRecursiva2(n-1)*n

@lru_cache(maxsize=None)
def fibRecursiva2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibRecursiva2(n-1) + fibRecursiva2(n-2)

n = int(input("Digite o valor de n: "))

inicio = time.time()
for i in range (100000):
    fatRecursiva(n)
fim = time.time()
print("Duração fatorial recursiva sem lru %s" %(fim - inicio))

inicio = time.time()
fibRecursiva(n)
fim = time.time()
print("Duração fibonacci recursiva sem lru %s" %(fim - inicio))

inicio = time.time()
for i in range (100000):
    fatRecursiva2(n)
fim = time.time()
print("Duração fatorial recursivo com lru %s" %(fim - inicio))

inicio = time.time()
for i in range (100000):
    fibRecursiva2(n)
fim = time.time()
print("Duração fibonacci recursivo com lru %s" %(fim - inicio))

inicio = time.time()
for i in range (100000):
    fatIterativa(n)
fim = time.time()
print("Duração fatorial iterativo %s" %(fim - inicio))

inicio = time.time()
for i in range (100000):
    fibIterativa(n)
fim = time.time()
print("Duração fibonacci iterativo %s" %(fim - inicio))
