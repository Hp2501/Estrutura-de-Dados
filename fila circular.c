#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int conteudo;
    struct Node *proximo
}No;

void iniciarLista(No ** lista)
{
	(*lista) = NULL;
}

int estaVazia(No *lista)
{
	if ( lista == NULL)
		return 1;
	else
		return 0;
}

void adicionarLista(No **lista, int conteudo)
{
	No *no = malloc(sizeof(No)); /*Criação do novo nó*/
	no->conteudo = conteudo;
	if (!estaVazia(*lista)) /* Lista não está vazia*/
	{
		no->proximo = (*lista);
		/* Início da lista passsa a apontar
		 * para o nó adicionado. */
		(*lista) = no;
	}
	else /* Lista está vazia.*/
	{
		no->proximo = NULL;
		(*lista) = no;
	}
}
