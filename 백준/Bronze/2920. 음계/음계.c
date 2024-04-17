#include <stdio.h>

int main() {
    int arr[8] = {0};
    int i;
    int break_ = 0;
    for (i = 0; i < 8; i++)
        scanf("%d", &arr[i]);

    if (arr[0] == 1) {
        for (i=1; i<8; i++) 
            if (arr[i] != i+1)
                break_ = 1;
        if (break_ == 0)
            printf("ascending\n");
        else printf("mixed\n");
        
    }
    else if (arr[0] == 8) {
        for (i=1; i<8; i++) 
            if (arr[i] != 8-i)
                break_ = 1;
        if (break_ == 0)
            printf("descending\n");
        else printf("mixed\n");
    }
    else printf("mixed\n");
    
    return 0;
}