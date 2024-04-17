#include <stdio.h>

int main() {
    int i;
    int arr[31] = {0};
    int a;
    
    for (i = 0; i<28; i++){
        scanf("%d", &a);
        arr[a] = 1;
    }
    for (i = 1; i<31; i++)
        if (arr[i]==0)
            printf("%d\n", i);
  
   return 0;  
}