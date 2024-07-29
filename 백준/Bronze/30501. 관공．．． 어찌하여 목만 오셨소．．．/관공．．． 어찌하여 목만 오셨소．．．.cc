#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    string s, ans;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == 'S') {
                ans = s;
                break;
            }
        }
    }
    cout << ans;
    return 0;
}