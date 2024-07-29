#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    bool TF = true;
    for (int i = 0; i < s.length()/2; i++) {
        if (s[i] != s[s.length()-i-1]) {
            cout << 0 << endl;
            TF = false;
            break;
        }   
    }
    if (TF) {
        cout << 1 << endl;
    }
    return 0;
}