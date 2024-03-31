#include <iostream>
using namespace std;
bool num[10001];

int d (int n ) {
	int temp;
	temp = n + n/1000 + n%1000/100 + n%100/10 + n%10;
	return temp;
}
void selfnum() {
	int temp;
	num[1] = false;
	for (int i = 0; i < 10000; i ++) {
		
		temp = d(i);
		if (temp < 10000)
			num[temp] = true;
		
	}
}

int main () {
	selfnum();
	for (int i = 1; i < 10000; i ++) {
		if (!num[i])
			printf("%d\n", i);
	}
	
	return 0;
}