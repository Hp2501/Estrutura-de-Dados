#include <stdio.h>
#include <stdlib.h>
int iniciarMatriz(int l, int c, int **mat);
int produtoMatriz(int l, int c, int **matA, int **matB, int **matC);
int imprimeMatriz(int l, int c, int **mat);

int main()
{
    int **matA, **matB, **matC, l1, c1, l2, c2, i;


    inicio:
    printf("\nDigite a quantidade de linhas da primeira matriz: ");scanf("%d", &l1);
    printf("\nDigite a quantidade de colunas da primeira matriz: ");scanf("%d", &c1);
    printf("\nDigite a quantidade de linhas da segunda matriz: ");scanf("%d", &l2);
    printf("\nDigite a quantidade de colunas da segunda matriz: ");scanf("%d", &c2);
        if (c1!=l2)
        {
            printf("\nERRO!! MATRIZES IMCOMPATIVEIS PARA MULTIPLICACAO");
            goto inicio;
        }

        matA = (int **)malloc(sizeof(int)*l1);
    for (i = 0; i < l1; i++)
        matA[i] = (int *)malloc(sizeof(int)*c1);

    matB = (int **)malloc(sizeof(int)*l2);
    for (i = 0; i < l2; i++)
        matB[i] = (int *)malloc(sizeof(int)*c2);

    matC = (int **)malloc(sizeof(int)*l2);
    for (i = 0; i < l2; i++)
        matC[i] = (int *)malloc(sizeof(int)*c1);

    iniciarMatriz(l1, c1, matA);
    imprimeMatriz(l1, c1, matA);
    iniciarMatriz(l2, c2, matB);
    imprimeMatriz(l2, c2, matB);
    produtoMatriz(l2, c1, matA, matB, matC);
    imprimeMatriz(l2, c1, matC);
}

int imprimeMatriz(int l, int c, int **mat)
{
    int i, j;
    for(i=0;i<l;i++)
    {
        for(j=0;j<c;j++)
    {
        printf("%d\t", mat[i][j]);

    }
    printf("\n");
    }
    printf("\n");
}

int iniciarMatriz(int l, int c, int **mat)
{
    int i, j;
    for(i=0;i<l;i++)
        for(j=0;j<c;j++)
    {
        printf("\nElemento[%d][%d]: ", i+1, j+1);scanf("%d", &mat[i][j]);
    }
}

int produtoMatriz(int l, int c, int **matA, int **matB, int **matC)
{
    int i, j, k;

    for (i=0;i<l;i++)
    {
        for (j=0;j<c;j++)
        {
            matC[i][j] = 0;
            for(k=0;k<l;k++)
                matC[i][j] += matA[i][k] * matB[k][j];
        }
    }
}
