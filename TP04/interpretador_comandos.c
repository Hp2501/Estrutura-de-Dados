#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

struct StrNo{
	char dado;
	struct StrNo *proximo;
};

typedef struct StrNo No;

/* Inicializar uma pilha vazia: */
void iniciarPilha(No ** pilha)
{
	*pilha = NULL;
}

int estaVazia(No * pilha)
{
	if (pilha == NULL)
		return 1;
	else
		return 0;
}

void empilhar(No **pilha, char c)
{
	No *novoNo = malloc(sizeof(No));
	novoNo->dado = c;
	novoNo->proximo = *pilha;
	*pilha = novoNo;
}

char desempilhar(No **pilha)
{
	if (!estaVazia(*pilha))
	{
		No *no = (*pilha);
		char c = (*pilha)->dado;
		(*pilha) = (*pilha)->proximo;
		free(no);
		return c;
	}
	else
		return ' ';

int main()
{
    char comando[50];
    while(comando)
}

