#include <stdio.h>

int main () {
    int N;
    scanf("%d", &N);
    int arr[N];
    int i;
    for (i = 0; i < N; i++)
        scanf("%d", &arr[i]);
    int v;
    scanf("%d", &v);
    
    int cnt = 0;
    for (i = 0; i < N; i++)
        if (arr[i] == v)
            cnt += 1;
    
    printf("%d", cnt);
    return 0;
}