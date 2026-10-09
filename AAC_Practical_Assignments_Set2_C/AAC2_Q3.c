/* Q3. All-Pairs Shortest Paths using Floyd-Warshall Algorithm */
#include <stdio.h>

#define MAX 100
#define INF 1000000000

int main(void) {
    int n, dist[MAX][MAX], i, j, k;

    printf("Enter number of vertices (max %d): ", MAX);
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX) {
        printf("Invalid number of vertices.\n");
        return 1;
    }

    printf("Enter adjacency matrix (%d for no edge; diagonal should be 0):\n", INF);
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (scanf("%d", &dist[i][j]) != 1) {
                printf("Invalid matrix input.\n");
                return 1;
            }
        }
    }

    for (k = 0; k < n; k++)
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
                if (dist[i][k] != INF && dist[k][j] != INF &&
                    dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];

    printf("All-pairs shortest distance matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (dist[i][j] == INF)
                printf("INF ");
            else
                printf("%d ", dist[i][j]);
        }
        printf("\n");
    }
    return 0;
}
