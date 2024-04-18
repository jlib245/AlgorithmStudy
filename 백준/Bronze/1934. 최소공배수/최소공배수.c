#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    int i;
    int arr[T][2];
    int a, b, s;
    for (i = 0; i < T; i++) {
        scanf("%d%d", &arr[i][0], &arr[i][1]);
    }
    
    for (i = 0; i < T; i++) {
        a = arr[i][0];
        b = arr[i][1];
        if (a < b) {
            s = a;
            a = b;
            b = s;
        }
        while (b != 0) {
            s = a%b;
            a = b;
            b = s;
        }
        
        printf("%d\n", (arr[i][0]*arr[i][1])/a);
        
    }
    return 0;
}