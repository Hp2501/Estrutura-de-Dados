#include <stdio.h>
#include <stdlib.h>
void criarMatriz(){
    int *mat1, *mat2;
    int c1, l1, c2, l2;
    printf("Digite o tamanho da coluna da primeira matriz\n");scanf("%d", &c1);
    printf("Digite o tamanho da linha da primeira matriz\n");scanf("%d", &l1);
    printf("Digite o tamanho da coluna da segunda matriz\n");scanf("%d", &c2);
    printf("Digite o tamanho da linha da segunda matriz\n");scanf("%d", &l2);
    if(l1==c2)
    {
        mat1 = malloc(l1 * c1 * sizeof(int));
        mat2 = malloc(l2 * c2 * sizeof(int));
    }
    else
    {
        printf("ERRO!! DIMENSOES IMCOMPATIVEIS\n\n ");
        criarMatriz();

    }
}

int main(){
    int i, j;
    criarMatriz();
    for (i=0; i<3; i++)
        for (j=0; j<3; j++)
    {
        printf("%d", mat1[i][j]);
        printf("%d", mat1[i][j]);
    }


}
