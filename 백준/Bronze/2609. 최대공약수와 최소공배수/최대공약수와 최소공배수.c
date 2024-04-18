#include <stdio.h>

int main() {
    int A, B, r;
    scanf("%d%d", &A, &B);
    
    int C = A;
    int D = B;
    if (C < D) {
        r = C;
        C = D;
        D = r;
    }
    while (D) {
        r = C%D;
        C = D;
        D = r;
    }
    printf("%d\n", C);
    
    printf("%d\n", (A*B)/C);
    
    return 0;
}