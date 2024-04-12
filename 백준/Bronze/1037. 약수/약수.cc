#include <iostream>
#include <algorithm>
using namespace std;
int main () {
	int NN;
	cin >> NN;
	int* array = new int[NN];
	for (int i= 0; i < NN; i++) 
		cin >> array[i];
	sort (array, array + NN);
	int A = array[NN-1] * array[0];
	cout << A;
	return 0;
}
