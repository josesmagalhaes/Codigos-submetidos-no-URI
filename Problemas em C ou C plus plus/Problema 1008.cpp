#include <stdio.h>
int main () {
	int NUMBER, HOURS;
	float SALARY, VALOR;
	
	scanf ("%d", &NUMBER);
	scanf ("%d", &HOURS);
	scanf ("%f", &VALOR);
	
	SALARY = HOURS*VALOR;
	printf ("NUMBER = %d \nSALARY = U$ %.2f\n", NUMBER, SALARY);
	return 0;
}
