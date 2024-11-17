#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int T, x1, x2, y1, y2, r1, r2;
    double d;
    cin >> T;
    int ans[T];
    for (int i = 0; i < T; i++) {
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        if (x1 == x2 and y1 == y2 and r1 == r2) {
            ans[i] = -1;
        }
        else {
            d = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
            if (abs(r1-r2) < d and d < r1 + r2) {
                ans[i] = 2;
            }
            else if (r1 + r2 == d or abs(r1-r2) == d) {
                ans[i] = 1;
            }
            else {
                ans[i] = 0;
            }
        }
    }
    for (int i = 0; i < T; i++) {
        cout << ans[i] << "\n";
    }
}