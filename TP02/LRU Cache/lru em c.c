#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 20

long long int fibLru(int n, long long int *cache);
long long int fib(int n);
long long int fatLru(int n, long long int *cache);
long long int fat(int n);
int limparCache(long long int *cache);

int main()
{
   long long int cache[MAX];
   long long int n, fibonacci, fibonacciCache, fatorialCache, fatorial, i;
   double duracao;
   limparCache(cache);
   printf("Digite o valor de n: ");scanf("%lli", &n);
   clock_t inicio, termino;

   inicio = clock();
   for(i=0;i<50000;i++)
   {
       fibonacciCache = fibLru(n, cache);
   }
   termino = clock();
   duracao = (double)(termino - inicio)/CLOCKS_PER_SEC;
   printf("\nFibonacci com cache: %lli no tempo de %fs", fibonacciCache, duracao);


   inicio = clock();
   for(i=0;i<50000;i++)
   {
       fibonacciCache = fibLru(n, cache);
   }
   termino = clock();
   duracao = (double)(termino - inicio)/CLOCKS_PER_SEC;
   printf("\nFibonacci com cache: %lli no tempo de %fs\n\n", fibonacciCache, duracao);

   limparCache(cache);


   inicio = clock();
   for (i=0;i<50000;i++)
   {
       fibonacci = fib(n);
   }

   duracao = (double)(termino - inicio)/CLOCKS_PER_SEC;
   printf("\nFibonacci sem cache: %lli no tempo de %fs\n\n", fibonacci, duracao);

   inicio = clock();
   for (i=0;i<50000;i++)
   {
       fatorial = fat(n);
   }
   termino = clock();
   duracao = (double)(termino - inicio)/CLOCKS_PER_SEC;
   printf("\nFatorial sem cache %lli no tempo de %fs\n\n", fatorial, duracao);

   inicio = clock();
   for (i=0;i<50000;i++)
   {
       fatorialCache = fatLru(n, cache);
   }
   termino = clock();
   duracao = (double)(termino - inicio)/CLOCKS_PER_SEC;
   printf("\nFatorial com cache %lli no tempo de %fs", fatorialCache, duracao);

   inicio = clock();
   for (i=0;i<50000;i++)
   {
       fatorialCache = fatLru(n, cache);
   }
   termino = clock();
   duracao = (double)(termino - inicio)/CLOCKS_PER_SEC;
   printf("\nFatorial com cache %lli no tempo de %fs\n\n", fatorialCache, duracao);
   limparCache(cache);

   return 0;
}

long long int fibLru(int n, long long int *cache)
{
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;

    if (cache[n] != 0) return cache[n];

    long long int retorno = fibLru(n-1, cache) + fibLru(n-2, cache);
    cache[n] = retorno;
    return retorno;
}

long long int fib(int n)
{
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fib(n-1) + fib(n-2);
}

long long int fatLru(int n, long long int *cache)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }

    if(cache[n] != 0)
    {
        return cache[n];
    }

    long long int retorno = fatLru(n-1, cache) * n;
    return retorno;
}

long long int fat(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }
    else
        return n*fat(n-1);
}

int limparCache(long long int *cache)
{
    int j;
    for (j = 0;j<MAX;++j)
        cache[j] = 0;
}
