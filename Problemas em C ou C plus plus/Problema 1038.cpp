#include<stdio.h>
#include<stdlib.h>

int main(){
int id,qt;
float val=0;

scanf("%d %d",&id,&qt);
if(id==1)
val=qt*4.00;
if(id==2)
val=qt*4.50;
if(id==3)
val=qt*5.00;
if(id==4)
val=qt*2.00;
if(id==5)
val=qt*1.50;
printf("Total: R$ %.2f\n",val);
return 0;
}
