#include <stdio.h>
int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    int n, p;
    scanf("%d %d", &n, &p);
    int a[n], r[10001], d[n];
    for (int j = 0; j < n; j++) 
      scanf("%d", &a[j]);
    for (int k = 1; k <= 10000; k++)
      r[k] = 0;
    for (int j = 0; j < n; j++)
      r[a[j]]++;
    int c = 0;
    for (int k = 10000; k >=1; k--) {
      if (r[k] > 0) {
        while (r[k] > 0) {
          d[c] = k;
          c++;
          r[k]--;
        }
      }
    }
    int p_sum = 0;
    for (int j = 0; j < p; j++) p_sum += d[j];
    int m = p * d[0] - p_sum;
    for (int j = 1; j < n - p + 1; j++) {
      p_sum = p_sum - d[j-1] + d[j + p - 1];
      int train_hrs = p * d[j] - p_sum;
      m = (train_hrs < m) ? train_hrs : m;
    }
    printf("Case #%d: %d\n", i, m);
  }
  return 0;
} 
