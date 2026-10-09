/* Q8. Dijkstra's Algorithm for Single-Source Shortest Paths */
#include <stdio.h>

#define MAX 100
#define INF 1000000000

int main(void) {
    int n, graph[MAX][MAX], distance[MAX], visited[MAX] = {0};
    int source, i, j;

    printf("Enter number of vertices (max %d): ", MAX);
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX) {
        printf("Invalid number of vertices.\n");
        return 1;
    }

    printf("Enter weighted adjacency matrix (0 means no edge; weights must be non-negative):\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (scanf("%d", &graph[i][j]) != 1 || graph[i][j] < 0) {
                printf("Invalid matrix input. Use non-negative weights.\n");
                return 1;
            }
            if (i != j && graph[i][j] == 0)
                graph[i][j] = INF;
        }
    }

    printf("Enter source vertex (0 to %d): ", n - 1);
    if (scanf("%d", &source) != 1 || source < 0 || source >= n) {
        printf("Invalid source vertex.\n");
        return 1;
    }

    for (i = 0; i < n; i++)
        distance[i] = INF;
    distance[source] = 0;

    for (i = 0; i < n - 1; i++) {
        int min = INF, u = -1;
        for (j = 0; j < n; j++) {
            if (!visited[j] && distance[j] < min) {
                min = distance[j];
                u = j;
            }
        }

        if (u == -1) break;
        visited[u] = 1;

        for (j = 0; j < n; j++) {
            if (!visited[j] && graph[u][j] != INF &&
                distance[u] != INF && distance[u] + graph[u][j] < distance[j]) {
                distance[j] = distance[u] + graph[u][j];
            }
        }
    }

    printf("Shortest distances from vertex %d:\n", source);
    for (i = 0; i < n; i++) {
        if (distance[i] == INF)
            printf("To %d: Unreachable\n", i);
        else
            printf("To %d: %d\n", i, distance[i]);
    }
    return 0;
}
