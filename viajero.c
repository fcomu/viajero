#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

char Buffer[9999];
int contnodo;

struct Nodo
{
	int nodo;
	int ejeX;
	int ejeY;
	struct Nodo *sgte;
};

typedef struct Nodo tNodo;
typedef tNodo *Lista;

Lista CrearLista(int _nodo, int _ejeX, int _ejeY)
{

	Lista Aux;
	Aux = (Lista)malloc(sizeof(tNodo));

	if (Aux != NULL)
	{
		Aux->nodo = _nodo;
		Aux->ejeX = _ejeX;
		Aux->ejeY = _ejeY;
		Aux->sgte = NULL;
	}

	return Aux;
}
Lista L = NULL;
Lista L2 = NULL;

Lista InsertarFinal(Lista L, int _nodo, float _ejeX, float _ejeY)
{

	Lista pNodo, Aux;
	pNodo = CrearLista(_nodo, _ejeX, _ejeY);

	if (L == NULL)
	{
		L = pNodo;
	}
	else
	{
		Aux = L;
		while (Aux->sgte != NULL)
		{
			Aux = Aux->sgte;
		}
		Aux->sgte = pNodo;
		Aux = NULL;
	}

	pNodo = NULL;
	return L;
}


/* DEFINICION DE LAS FUNCIONES */
void Imprimir(Lista L);
void Lectura();
void ArreglarNodo();
/* FIN DEFINICIONES */

void Imprimir(Lista L)
{

	Lista Aux;
	Aux = L;

	while (Aux != NULL)
	{
		printf("Nodo: %d, X: %d, Y: %d \n", Aux->nodo, Aux->ejeX, Aux->ejeY);
		Aux = Aux->sgte;
	}
}

void Lectura() {
	int i = 0;
	FILE *Arch;
	Arch = fopen("archivo.txt", "r");
	while (i < 6) {
		fgets(Buffer, 9999, Arch);
		i++;
	}

	while (!feof(Arch)) {
		if (i>6) {
			fgets(Buffer, 9999, Arch);
			//printf("%s\n", Buffer);
			ArreglarNodo();
		}
		i++;
	}

	fclose(Arch);
}

void ArreglarNodo() {
	char Separador[] = " ";
	int ejeX, ejeY;
	char *trozo = NULL;
	int i = 0;
	trozo = strtok(Buffer, Separador);

	while (trozo != NULL) {
		trozo = strtok(NULL, Separador);
		if (i == 0) {
			ejeX = atoi(trozo);
		}
		if (i == 1) {
			ejeY = atoi(trozo);
		}
		i++;
	}
	contnodo+=1;
    if((ejeX != 0) && (ejeY <5000000)){
        L = InsertarFinal(L, contnodo, ejeX, ejeY);
        L2 = InsertarFinal(L2, contnodo, ejeX, ejeY);
    }
}


int main ()
{
	Lectura();
	Imprimir(L);

	system("\npause");
	return 0;
}
