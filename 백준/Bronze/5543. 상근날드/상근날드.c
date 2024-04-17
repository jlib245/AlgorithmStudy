#include <stdio.h>

int main () {
    int burger[3];
    int beverage[2];
    int i;
    int j;
    int set;
    for (i = 0; i < 3; i++)
        scanf("%d", &burger[i]);
    for (i = 0; i < 2; i++)
        scanf("%d", &beverage[i]);
    int result = burger[0]+beverage[0];
    for (i = 0; i < 3; i++){
        for (j = 0; j <2; j++){
            set = burger[i]+beverage[j];
            if (result > set)
                result = set;
        }
    }
    printf("%d", result-50);
    return 0;
}