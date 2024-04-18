#include <stdio.h>

int main() {
    int C[3],D[3], H;
    int i;
    int sec = 0;
    for (i=0; i<3; i++)
        scanf("%d%d",&C[i],&D[i]);
    scanf("%d", &H);
    H -= D[0]+D[1]+D[2];
    int Co[3] = {C[0], C[1], C[2]};
    while (H> 0) {
        sec += 1;
        for (i=0; i<3; i++){
            Co[i] -= 1;
            if (Co[i] == 0) {
                Co[i] = C[i];
                H -= D[i];
            }
        }
    }
    printf("%d", sec);
    return 0;
}