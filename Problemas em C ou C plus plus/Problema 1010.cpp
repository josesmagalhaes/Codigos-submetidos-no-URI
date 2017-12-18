#include <stdio.h>
#include <math.h>
int main () {
	int codigo_1, codigo_2, numero_1, numero_2;
	float valor_1,valor_2, valor_a_pagar;
	
	scanf ("%d", &codigo_1);
	scanf ("%d", &numero_1);
	scanf ("%f", &valor_1);
	scanf ("%d", &codigo_2);
	scanf ("%d", &numero_2);
	scanf ("%f", &valor_2);
	
	valor_a_pagar = (numero_1*valor_1) + (numero_2*valor_2);
	
	printf ("VALOR A PAGAR: R$ %.2f\n", valor_a_pagar);
	return 0; 
}
