#include <iostream>
#include <set>
using namespace std;

int main() {
    int nA, nB, d;
    cin >> nA >> nB;
    set<int> set_;
    for (int i = 0; i < nA; i++) {
        cin >> d;
        set_.insert(d);
    }
    for (int i = 0; i < nB; i++) {
        cin >> d;
        if (set_.find(d) != set_.end()) {
            set_.erase(set_.find(d));
        }
    }
    cout << set_.size() << endl;
    if (set_.size()) {
        for (set<int>::iterator iter = set_.begin(); iter != set_.end(); iter++) {
            cout << *iter << " ";
        }
    }
    return 0;
}