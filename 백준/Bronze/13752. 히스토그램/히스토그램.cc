#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int k[n];
    for (int i = 0; i < n; i++) {
        cin >> k[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k[i]; j++) {
            cout << '=';
        }
        cout << '\n';
    }  
    return 0;
}