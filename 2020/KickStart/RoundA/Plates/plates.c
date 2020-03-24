#include <stdio.h>
#include <string.h>
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define NONE 0
int main() {
    int T;
    scanf("%d", &T);
    for (int i=1; i <= T; ++i){
        int N, K, P;
        scanf("%d %d %d", &N, &K, &P);
        int a[P], w[P], ps[P];
        for (int j=0; j<N; ++j) {
            int r[K];
            for (int k=0; k<K; ++k) scanf("%d", &r[k]);
            for (int k=1; k<K; ++k) r[k] += r[k-1];
            memset(ps, NONE, sizeof(ps));
            memcpy(ps, r, sizeof(int)*MIN(P, K));
            if (j == 0) {
                memcpy(w, ps, P*sizeof(int));
                memcpy(a, ps, P*sizeof(int));
                continue;
            }
            for (int l=0; l < P; ++l) {
                if (l == 0) {
                    a[0] = MAX(w[0], ps[0]);
                    continue;
                }
                if (ps[l] != NONE) a[l] = MAX(ps[l], w[l]);
                for (int k=0; k<l; ++k) 
                    if (a[l] == NONE) {
                        a[l] = w[k] + ps[l-1-k];
                    }
                    else { 
                        a[l] = MAX(a[l], w[k]+ps[l-1-k]);
                    }
            }
            memcpy(w, a, P*sizeof(int));            
        }
        printf("Case #%d: %d\n", i, a[P-1]);
    }
    return 0;
}