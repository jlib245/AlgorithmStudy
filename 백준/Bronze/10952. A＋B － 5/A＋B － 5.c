#include <stdio.h>

int main () {
    int A, B;
    int C = 1;
    scanf("%d %d", &A, &B);
    if (A==0 && B==0) C = 0;
    
    while (C) {
        printf("%d\n", A+B);
        
        scanf("%d %d", &A, &B);
        if (A==0 && B==0) C = 0;
    }
    
    
    return 0;
}