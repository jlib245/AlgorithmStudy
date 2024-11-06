#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    vector <int> lst(9, 0);
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '9') {
            lst[6]++;
            continue;
        }
        lst[s[i]-48]++;
    }

    int ans = 0;
    if (lst[6] % 2) {
        lst[6] = lst[6]/2 + 1;
    }
    else {
        lst[6] = lst[6]/2;
    } 
    
    for (int i = 0; i < 9; i++) {
        if (ans < lst[i]) {
            ans = lst[i];
        }
    }

    cout << ans;
    
    return 0;
}