#include <stdio.h>

int main () {
    long long N, M;
    scanf("%lld %lld", &N, &M);
    
    long long result = N-M;
    
    if (result < 0)
        printf("%lld", -result);
    else printf("%lld", result);
    
    return 0;
}