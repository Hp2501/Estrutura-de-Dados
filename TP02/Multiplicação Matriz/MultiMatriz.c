#include <stdio.h>
#include <stdlib.h>
float iniciarMatriz(int l, int c, float **mat);
float produtoMatriz(float l, float c, float **matA, float **matB, float **matC);
float imprimeMatriz(float l, float c, float **mat);

float main()
{
    float **matA, **matB, **matC;
    int l1, c1, l2, c2, i;


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

        matA = (float **)malloc(sizeof(float)*l1);
    for (i = 0; i < l1; i++)
        matA[i] = (float *)malloc(sizeof(float)*c1);

    matB = (float **)malloc(sizeof(float)*l2);
    for (i = 0; i < l2; i++)
        matB[i] = (float *)malloc(sizeof(float)*c2);

    matC = (float **)malloc(sizeof(float)*l2);
    for (i = 0; i < l2; i++)
        matC[i] = (float *)malloc(sizeof(float)*c1);

    iniciarMatriz(l1, c1, matA);
    imprimeMatriz(l1, c1, matA);
    iniciarMatriz(l2, c2, matB);
    imprimeMatriz(l2, c2, matB);
    produtoMatriz(l2, c1, matA, matB, matC);
    imprimeMatriz(l2, c1, matC);

    return 0;
}

float imprimeMatriz(float l, float c, float **mat)
{
    int i, j;
    for(i=0;i<l;i++)
    {
        for(j=0;j<c;j++)
    {
        printf("%.2f\t", mat[i][j]);

    }
    printf("\n");
    }
    printf("\n");
}

float iniciarMatriz(int l, int c, float **mat)
{
    int i, j;
    for(i=0;i<l;i++)
        for(j=0;j<c;j++)
    {
        printf("\nElemento[%d][%d]: ", i+1, j+1);scanf("%f", &mat[i][j]);
    }
}

float produtoMatriz(float l, float c, float **matA, float **matB, float **matC)
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
