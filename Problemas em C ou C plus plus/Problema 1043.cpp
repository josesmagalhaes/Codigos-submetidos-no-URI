#include<stdio.h>
int main()
{
    float entrada_a,entrada_b,entrada_c,perimetro,area;
      while(scanf("%f %f %f",&entrada_a,&entrada_b,&entrada_c)==3){
            if(entrada_a+entrada_b>entrada_c && entrada_b+entrada_c>entrada_a && entrada_a+entrada_c>entrada_b ){
            perimetro=entrada_a+entrada_b+entrada_c;
            printf("Perimetro = %.1f\n",perimetro);
      }
            else{
                  area=.5*(entrada_a+entrada_b)*entrada_c;
                  printf("Area = %.1f\n",area);
      }
      }
      return 0;
}
