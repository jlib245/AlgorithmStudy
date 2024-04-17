#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    
    int result = 1;
    
    for (int i = 1; i < N+1; i++)
        result *= i;
    
    printf("%d", result);
    
    return 0;
}