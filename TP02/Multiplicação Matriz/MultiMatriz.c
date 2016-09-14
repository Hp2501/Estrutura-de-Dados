#include <stdio.h>
#include <stdlib.h>
int soma, int i, int linha, int coluna, int diml1, int diml2, int dimc1, int dimc2;
void iniciarMatriz(int linha, int coluna, int diml1, int diml2, int dimc1, int dimc2)
{
    for(linha=0;linha<diml1;linha++)
        for(coluna=0;coluna<dimc1;coluna++)
    {
        printf("Elemento[%d][%d]\n", linha+1, coluna+1);
        scanf("%d", *mat1[linha][coluna]);
    }

    for(linha=0;linha<diml2;linha++)
        for(coluna=0;coluna<dimc2;coluna++)
    {
        printf("Elemento[%d][%d]\n", linha+1, coluna+1);
        scanf("%d", *mat1[linha][coluna]);
    }
}

void checarMatriz(int diml2, int dimc1)
{
    if(dimc1!=diml2)
    {
        printf("Matriz imcompativel\n");
    }
    else
    {
        iniciarMatriz(mat1, mat2, int linha, int coluna, int diml1, int diml2, int dimc1, int dimc2);
    }
}

int produtoMatriz(mat1, mat2, mf, int soma, int i, int linha, int coluna, int diml1, int diml2, int dimc1, int dimc2)
{
    mf = malloc(sizeof(int) * dimc1 * diml2)
    for (linha=0;linha<diml1;linha++)
        for (coluna=0;linha<dimc2;coluna++)
    {
        soma=0;
        for (i=0;i<diml1;i++)
        {
            soma += mat1[linha][i]*mat2[i][coluna];
            *mf[linha][coluna]=soma
        }

    }
}

int main()
{
    int soma, int i, int linha, int coluna, int diml1, int diml2, int dimc1, int dimc2
    printf("\nDigite a quantidade de linhas da primeira matriz: ");scanf("%d", &diml1);
    printf("\nDigite a quantidade de colunas da primeira matriz: ");scanf("%d", &dimc1);
    printf("\nDigite a quantidade de linhas da segunda matriz: ");scanf("%d", &diml2);
    printf("\nDigite a quantidade de colunas da segunda matriz: ");scanf("%d", &dimc2);

    checarMatriz(diml1, diml2);

}
