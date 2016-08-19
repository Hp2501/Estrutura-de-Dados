#include <stdio.h>

typedef struct NumeroComplexo{
    float real;
    float imaginario;
}NumeroComplexo;//Fecha Struct Numero Complexo

float somaComplexo(){
    float somaReal=0, somaImaginario=0;
    NumeroComplexo a, b;
    printf("Digite o numero real do primeiro numero complexo: ");scanf("%f", &a.real);
    printf("\nDigite o numero imaginario do primeiro numero complexo: ");scanf("%f", &a.imaginario);
    printf("\nDigite o numero real do segundo numero complexo:  ");scanf("%f", &b.real);
    printf("\n Digite o numero imaginario do segundo numero complexo: ");scanf("%f", &b.imaginario);
    somaReal=a.real+b.real;
    somaImaginario=a.imaginario+b.imaginario;
    return printf("(%.2f + %.2f i)", somaReal, somaImaginario);

}//Fecha Soma Complexo

float subComplexo(){
    float subReal=0, subImaginario=0;
    NumeroComplexo a, b;
    printf("Digite o numero real do primeiro numero complexo: ");scanf("%f", &a.real);
    printf("\nDigite o numero imaginario do primeiro numero complexo: ");scanf("%f", &a.imaginario);
    printf("\nDigite o numero real do segundo numero complexo:  ");scanf("%f", &b.real);
    printf("\n Digite o numero imaginario do segundo numero complexo: ");scanf("%f", &b.imaginario);
    subReal=a.real-b.real;
    subImaginario=a.imaginario-b.imaginario;
    return printf("(%.2f + %.2f i)", subReal, subImaginario);
}//Fecha Subtração Complexo

float multComplexo(){
    float multReal1=0, multImaginario1=0, multReal2=0, multImaginario2=0;
    NumeroComplexo a, b;
    printf("Digite o numero real do primeiro numero complexo: ");scanf("%f", &a.real);
    printf("\nDigite o numero imaginario do primeiro numero complexo: ");scanf("%f", &a.imaginario);
    printf("\nDigite o numero real do segundo numero complexo:  ");scanf("%f", &b.real);
    printf("\n Digite o numero imaginario do segundo numero complexo: ");scanf("%f", &b.imaginario);
    multReal1=a.real*b.real;
    multReal2=a.real*b.imaginario;
    multImaginario1=b.real*a.imaginario;
    multImaginario2=a.imaginario*b.imaginario;
}//Fecha Multiplicação Complexo


int main(){
int escolha;
    printf("\t========================================\n");
    printf("\t=====OPERACOES COM NUMEROS COMPLEXO=====\n");
    printf("\t========================================\n");
    printf("\tPARA SOMAR DIGITE 1\n");
    printf("\tPARA SUBTRAIR DIGITE 2\n");
    printf("\tPARA MULTIPLICAR DIGITE 3\n");
    printf("\tPARA DIVIDIR DIGITE 4\n\n");
    scanf("%d", &escolha);

    switch(escolha){
        case 1:
            somaComplexo();
            break;
        case 2:
            subComplexo();
            break;
        case 3:
        multComplexo();
        break;
    }//Fecha Switch
return 0;}//Fecha Main
