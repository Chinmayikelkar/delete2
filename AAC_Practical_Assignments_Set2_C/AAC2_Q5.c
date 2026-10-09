/* Q5. Prim's Algorithm for Minimum Cost Spanning Tree */
#include <stdio.h>

#define MAX 100
#define INF 1000000000

int main(void) {
    int n, cost[MAX][MAX], selected[MAX] = {0};
    int i, j, edges = 0, totalCost = 0;

    printf("Enter number of vertices (max %d): ", MAX);
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX) {
        printf("Invalid number of vertices.\n");
        return 1;
    }

    printf("Enter adjacency matrix (0 for no edge, positive weight for an edge):\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (scanf("%d", &cost[i][j]) != 1) {
                printf("Invalid matrix input.\n");
                return 1;
            }
            if (i != j && cost[i][j] == 0)
                cost[i][j] = INF;
        }
    }

    selected[0] = 1;
    printf("Edges in minimum spanning tree:\n");
    while (edges < n - 1) {
        int min = INF, u = -1, v = -1;
        for (i = 0; i < n; i++) {
            if (selected[i]) {
                for (j = 0; j < n; j++) {
                    if (!selected[j] && cost[i][j] < min) {
                        min = cost[i][j];
                        u = i;
                        v = j;
                    }
                }
            }
        }

        if (u == -1) {
            printf("Graph is disconnected; MST does not exist.\n");
            return 1;
        }

        printf("%d - %d : %d\n", u, v, min);
        totalCost += min;
        selected[v] = 1;
        edges++;
    }

    printf("Minimum cost = %d\n", totalCost);
    return 0;
}
