#include <stdio.h>

int main() {
    int D;
    scanf(" %d", &D);
    int carNum;
    int cnt = 0;
    for (int i =0; i < 5; i++) {
        scanf(" %d", &carNum);
        if (carNum == D) {
            cnt += 1;
        }
    }
    printf("%d\n", cnt);
}