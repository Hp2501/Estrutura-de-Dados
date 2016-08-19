#include <stdio.h>
#include<stdlib.h>

struct Pessoa{
    char nome[200];
    char cpf[11];
    char rg[10];
    char uf[2];
    char dia[2];
    char mes[2];
    char ano[4];
};

int main (){
    FILE *agenda;
    agenda = fopen("agenda.txt", "w");
    int i, p;
    printf("Digite a quantidade de pessoas a ser cadastrada: ");scanf("%d", &p);
    struct Pessoa cadastro[p];
    for(i=0; i<p; i++){

        printf("\nDigite o nome: ");scanf("%s", cadastro[i].nome);
        printf("\nDigite o dia do nascimento: ");scanf("%d", cadastro.dia);
        printf("\nDigite o mês do nascimento: ");scanf("%d", cadastro.mes);
        printf("\nDigite o ano do nascimento: ");scanf("%d", cadastro.ano);
        printf("\nDigite o cpf: ");scanf("%s", cadastro[i].cpf);
        printf("\nDigite o rg: ");scanf("%s", cadastro[i].rg);
        printf("\nDigite a UF: ");scanf("%s", cadastro[i].uf);
        fprintf(agenda, "Nome: %s; Data Nascimento: %d %d %d; CPF: %s; RG: %s; UF: %s\n", cadastro[i].nome, cadastro.dia, cadastro.mes, cadastro.ano, cadastro[i].cpf, cadastro[i].rg, cadastro[i].uf);
        }

    return 0;
}

