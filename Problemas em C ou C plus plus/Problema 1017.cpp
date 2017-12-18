#include <stdio.h>
int main () {
	int tempo_gasto, velocidade_media;
	float litros_gastos, distancia_percorrida;
	
	scanf ("%d", &tempo_gasto);
	scanf ("%d", &velocidade_media);
	
	distancia_percorrida = tempo_gasto*velocidade_media;
	litros_gastos = distancia_percorrida/12;
	
	printf ("%.3f\n", litros_gastos);
	return 0;
}
