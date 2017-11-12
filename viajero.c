#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* DEFINICION FUNCIONES */
void Lectura();
void ArreglarNodo();

char Buffer[9999];

void Lectura(){
	int i=0;
	FILE *Arch;
	Arch = fopen("data.txt", "r");
	while(i < 6){
		fgets(Buffer, 9999, Arch);
		i++;
	}

	while (!feof(Arch)){
		if(i>6){
 			fgets(Buffer, 9999, Arch);
 			printf("%s\n", Buffer);
 			ArreglarNodo();
		}
		i++;
 	}

	fclose(Arch);
}

void ArreglarNodo(){
	char Separador[] = " ";
	int ejeX, ejeY;
	char *trozo = NULL;
	int i=0;
	trozo = strtok(Buffer, Separador);

	while(trozo != NULL){
		trozo = strtok(NULL, Separador);
		if(i == 0){
			ejeX = atoi(trozo);
		}
		if(i == 1){
			ejeY = atoi(trozo);
		}
		i++;
	}
}

int main(){
	Lectura();
	//ArreglarNodo();
	return 0;
}
