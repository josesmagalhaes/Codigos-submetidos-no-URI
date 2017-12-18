#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

struct Lista {
	int numero;
	int *proximo;
};

void ordenar(Lista vetor[], int comeco, int termino){
    Lista pivo, aux;
    int i, j, centro;

    i = comeco;
    j = termino;

    centro = (int) ((i + j) / 2);
    pivo = vetor[centro];

    do{
        while (vetor[i].numero < pivo.numero) i = i + 1;
        while (vetor[j].numero > pivo.numero) j = j - 1;

        if(i <= j){
            aux = vetor[i];
            vetor[i] = vetor[j];
            vetor[j] = aux;
            i = i + 1;
            j = j - 1;
        }
    }while(j > i);

    if(comeco < j) ordenar(vetor, comeco, j);
    if(i < termino) ordenar(vetor, i, termino);

}

int main(){

	cout << fixed << setprecision(3);
	int n, x, y, cidade = 1, *individuos, Total_de_Individuos;
	Lista *consumo;
	double consumoMedio, consumoTotal;

	bool flag = false;

	while(cin >> n) {

		if(n == 0) 
			break;
		else if(flag)
			cout << endl;


		cout << "Cidade# " << cidade << endl;

		consumo = new Lista[n];
		individuos = new int[n];
		consumoTotal = 0;
		Total_de_Individuos = 0;

		for(int i = 0; i < n; i++){
			cin >> x;
			Total_de_Individuos += x;

			cin >> y;
			consumoTotal += y;
			
			individuos[i] = x;
			consumo[i].numero = y/x;
			consumo[i].proximo = &individuos[i];
		}

		ordenar(consumo, 0, n-1);

		for(int i = 0; i < n; i++) {
			cout << *consumo[i].proximo  << "-" << consumo[i].numero;
			if(i == n-1)
				cout << endl;
			else
				cout << " ";
		}

		double int_part;
        int frac_part;
        frac_part = (int) (modf ((double)consumoTotal/Total_de_Individuos, &int_part) *100);

		if(frac_part < 10)
            cout << "Consumo medio: " << (int)int_part <<  ".0" << (int)frac_part << " m3.\n";
        else
            cout << "Consumo medio: " << (int)int_part <<  "." << (int)frac_part << " m3.\n";

		flag = true;

		cidade++;

		delete consumo;
		delete individuos;
	}

}

