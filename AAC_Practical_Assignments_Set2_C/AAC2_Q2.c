/* Q2. Topological Sort using Kahn's Algorithm */
#include <stdio.h>

#define MAX 100

int main(void) {
    int n, graph[MAX][MAX] = {0}, indegree[MAX] = {0};
    int queue[MAX], front = 0, rear = 0, order[MAX], count = 0;
    int i, j, edges;

    printf("Enter number of vertices (max %d): ", MAX);
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX) {
        printf("Invalid number of vertices.\n");
        return 1;
    }

    printf("Enter number of directed edges: ");
    if (scanf("%d", &edges) != 1 || edges < 0) {
        printf("Invalid number of edges.\n");
        return 1;
    }

    printf("Enter each edge as: source destination (vertices numbered 0 to %d)\n", n - 1);
    for (i = 0; i < edges; i++) {
        int u, v;
        if (scanf("%d %d", &u, &v) != 2 || u < 0 || u >= n || v < 0 || v >= n) {
            printf("Invalid edge.\n");
            return 1;
        }
        if (!graph[u][v]) {
            graph[u][v] = 1;
            indegree[v]++;
        }
    }

    for (i = 0; i < n; i++)
        if (indegree[i] == 0)
            queue[rear++] = i;

    while (front < rear) {
        int u = queue[front++];
        order[count++] = u;
        for (j = 0; j < n; j++) {
            if (graph[u][j]) {
                indegree[j]--;
                if (indegree[j] == 0)
                    queue[rear++] = j;
            }
        }
    }

    if (count != n) {
        printf("Topological ordering is not possible: graph contains a cycle.\n");
    } else {
        printf("Topological order: ");
        for (i = 0; i < n; i++)
            printf("%d%s", order[i], (i == n - 1) ? "\n" : " ");
    }
    return 0;
}
