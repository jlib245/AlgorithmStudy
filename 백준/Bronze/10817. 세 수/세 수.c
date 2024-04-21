#include <stdio.h>

int main() {
    int A,B,C, r;
    
    scanf(" %d %d %d", &A, &B, &C);
    if (A > B) {
        r= A;
        A = B;
        B = r;
    }
    if (B > C) {
        r = B;
        B = C;
        C = r;
    }
    if (A > B) {
        r= A;
        A = B;
        B = r;
    }
    printf("%d", B);
}