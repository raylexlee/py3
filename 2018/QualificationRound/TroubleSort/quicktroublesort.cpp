#include <iostream>
#include <algorithm>
using namespace std;

int T, N = 1;
int L[100001];
int s[100001];
void QuickTroubleSort() {
    for (int e=0; e < 2; ++e) {
        int cnt = 0;
        for (int i=e; i < N ; i += 2) {
            s[i >> 1] = L[i];
            cnt++;
        }
        sort(s, s + cnt);
        for (int i=e; i < N ; i +=2) L[i] = s[i >> 1];        
    }
}
int main() {
    scanf("%d", &T);    
    for (int i=1; i <= T; ++i) {
        scanf("%d", &N);
        for (int j=0; j < N; ++j) scanf("%d", L + j);
        QuickTroubleSort();
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