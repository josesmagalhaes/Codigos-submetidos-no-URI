#include<stdio.h> 

main() 
{ 
char nome[50]; 
double salFixo, totalVendas; 

scanf("%s",&nome); 
scanf("%lf",&salFixo); 
scanf("%lf",&totalVendas); 

printf("TOTAL = R$ %.2lf\n", (0.15*totalVendas) + salFixo); 

return 0;
} 
