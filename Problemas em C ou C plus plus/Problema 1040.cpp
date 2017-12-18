#include <iostream>
#include <iomanip>

using namespace std;

int main(){

	cout << fixed << setprecision(1);

	double n1, n2, n3, n4, media;

	cin >> n1;
	cin >> n2;
	cin >> n3;
	cin >> n4;

	media = (n1*2+n2*3+n3*4+n4)/10;

	cout << "Media: " << media << endl;

	if(media >= 7)
		cout << "Aluno aprovado.\n";
	else if(media < 5)
		cout << "Aluno reprovado.\n";
	else {
		cout << "Aluno em exame.\n";
		double rec;
			cin >> rec;
			cout << "Nota do exame: " << rec << endl;
			media = (media+rec)/2;
			if(media >= 5)
				cout << "Aluno aprovado.\n";
			else
				cout << "Aluno reprovado.\n";
			cout << "Media final: " << media << endl;
	}
}
