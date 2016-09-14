#include <stdio.h>
#include <stdlib.h>
void iniciarMatriz(mat1, mat2 int l1, int l2, int c1, int c2, int diml1, int diml2, int dimc1, int dimc2)
{
    for(l1=0;l1<diml1;l1++)
        for(c1=0;c1<dimc1;c1++)
    {
        printf("Elemento[%d][%d]", l1+1, c1+1);
        scanf("%d", *mat1[l1][c1]);
    }

    for(l2=0;l2<diml2;l2++)
        for(c2=0;c2<dimc2;c2++)
    {
        printf("Elemento[%d][%d]", l2+1, c2+1);
        scanf("%d", *mat1[l2][c2]);
    }
}

void checarMatriz(int diml2, int dimc1)
{
    if(dimc1!=diml2)
    {
        printf("Matriz imcompativel");
    }
    else
    {
        iniciarMatriz(mat1, mat2 int l1, int l2, int c1, int c2, int diml1, int diml2, int dimc1, int dimc2)
    }
}

int produtoMatriz(mat1, mat2 int l1, int l2, int c1, int c2, int diml1, int diml2, int dimc1, int dimc2)
{
    mf = malloc(sizeof(int) * dimc1 * diml2)

}
