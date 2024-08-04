#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    int lst[3];
    for (int i = 0; i < 3; i++) {
      cin >> lst[i];
    }
    sort(lst, lst+3);
    cout << lst[1];
    return 0;
}