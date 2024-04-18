#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
    int N, M;
    int i, j, k, nw;
    int result;
    scanf("%d%d", &N, &M);

    int arr[100];
    for (i = 0; i < N; i++)
        scanf("%d", &arr[i]);
    
    result = arr[0] + arr[1] + arr[2];
    if (result > M)
        result = -1;

    for (i = 0; i < N; i++) 
        for (j = 0; j < N; j++) 
            if (j > i)
                for (k = 0; k < N; k++)
                    if (k > j) {
                        nw = arr[i] + arr[j] + arr[k];
                        if (result < nw && nw<= M)
                            result = nw;
                    }
    printf("%d", result);
                

    return 0;
}