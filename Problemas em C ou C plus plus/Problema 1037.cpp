#include <stdio.h>
int main () {
	float entrada;
	scanf ("%f", &entrada);
	if ((entrada >=0) && (entrada <=25.00)) {printf ("Intervalo (0,25]\n");}
	else if ((entrada >=25.01) && (entrada <=50.00)) {printf ("Intervalo [25,50]\n");}
	else if ((entrada >=50.01) && (entrada <=100.00)) {printf ("Intervalo (75,100]\n");}
	else if ((entrada<0)) {printf ("Fora de intervalo\n");}	
	return 0;
}
