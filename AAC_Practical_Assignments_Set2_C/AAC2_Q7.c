/* Q7. 0/1 Knapsack using Dynamic Programming */
#include <stdio.h>

#define MAX_N 100
#define MAX_CAPACITY 10000

int main(void) {
    int n, capacity, i, w;
    int weight[MAX_N], profit[MAX_N];

    printf("Enter number of items (max %d): ", MAX_N);
    if (scanf("%d", &n) != 1 || n < 1 || n > MAX_N) {
        printf("Invalid number of items.\n");
        return 1;
    }

    for (i = 0; i < n; i++) {
        printf("Enter weight and profit of item %d: ", i + 1);
        if (scanf("%d %d", &weight[i], &profit[i]) != 2 ||
            weight[i] <= 0 || profit[i] < 0) {
            printf("Invalid weight or profit.\n");
            return 1;
        }
    }

    printf("Enter knapsack capacity (max %d): ", MAX_CAPACITY);
    if (scanf("%d", &capacity) != 1 || capacity < 0 || capacity > MAX_CAPACITY) {
        printf("Invalid capacity.\n");
        return 1;
    }

    int dp[MAX_N + 1][MAX_CAPACITY + 1] = {{0}};
    for (i = 1; i <= n; i++) {
        for (w = 0; w <= capacity; w++) {
            if (weight[i - 1] <= w) {
                int include = profit[i - 1] + dp[i - 1][w - weight[i - 1]];
                int exclude = dp[i - 1][w];
                dp[i][w] = include > exclude ? include : exclude;
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    printf("Maximum profit = %d\n", dp[n][capacity]);
    printf("Selected items (item numbers): ");
    w = capacity;
    for (i = n; i > 0; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            printf("%d ", i);
            w -= weight[i - 1];
        }
    }
    printf("\n");
    return 0;
}
