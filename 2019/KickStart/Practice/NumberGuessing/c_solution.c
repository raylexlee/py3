#include <stdio.h>
#include <string.h>

int main() {
  int T; scanf("%d", &T);

  for (int id = 1; id <= T; ++id) {
    int A, B, N, done = 0;
    scanf("%d %d %d", &A, &B, &N);
    for (++A; !done;) {
      int mid = A + B >> 1;
      char result[32];
      printf("%d\n", mid);
      fflush(stdout);
      scanf("%s", result);
      if (!strcmp(result, "CORRECT")) done = 1;
      else if (!strcmp(result, "TOO_SMALL")) A = mid + 1;
      else B = mid - 1;
    }
  }
  return 0;
}