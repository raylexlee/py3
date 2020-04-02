#include <stdio.h>
#include <string.h>
#define false 0
#define true 1

int T, N = 1;
int L[100001];
void TroubleSort() {
    int done = false;
    while (!done) {
        done = true;    
        for (int i=0; i < N-2; ++i)
            if (L[i] > L[i+2]) {
                done = false;
                int t = L[i];
                L[i] = L[i+2];
                L[i+2] = t;
            }
    }
}
int main() {
    scanf("%d", &T);    
    for (int i=1; i <= T; ++i) {
        scanf("%d", &N);
        for (int j=0; j < N; ++j) scanf("%d", L + j);
        TroubleSort();
        int j;
        for (j=0; j < N-1; ++j)
            if (L[j] > L[j+1]) break;
        if (j == N-1) {
            printf("Case #%d: OK\n", i);
        } else {
            printf("Case #%d: %d\n", i, j);
        }    
    }
}