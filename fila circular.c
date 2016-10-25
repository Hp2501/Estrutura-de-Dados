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
	No *no = malloc(sizeof(No)); /*Cria��o do novo n�*/
	no->conteudo = conteudo;
	if (!estaVazia(*lista)) /* Lista n�o est� vazia*/
	{
		no->proximo = (*lista);
		/* In�cio da lista passsa a apontar
		 * para o n� adicionado. */
		(*lista) = no;
	}
	else /* Lista est� vazia.*/
	{
		no->proximo = NULL;
		(*lista) = no;
	}
}
