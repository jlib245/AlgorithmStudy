#include <stdio.h>

int main() {
    int arr[7] = {0};
    int i;
    int top = 0;
    int input;
    for (i = 0; i<3; i++){
        scanf("%d", &input);
        arr[input] += 1;
    }
    
    for (i = 1; i<7; i++) {
        if (arr[i] == 3){
            printf("%d", 10000+1000*i);
            return 0;
        }
        else if (arr[i]==2) {
            printf("%d", 1000+100*i);
            return 0;
        }
        else if (arr[i] == 1) top = i;
    }
    printf("%d", 100*top);
    return 0;
}