/* Q4. N-Queens Problem using Backtracking */
#include <stdio.h>
#include <stdlib.h>

#define MAX 20

int n, position[MAX], solutions = 0;

int safe(int row, int col) {
    int i;
    for (i = 0; i < row; i++) {
        if (position[i] == col ||
            abs(position[i] - col) == abs(i - row))
            return 0;
    }
    return 1;
}

void print_solution(void) {
    int i, j;
    solutions++;
    printf("\nSolution %d:\n", solutions);
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%c ", position[i] == j ? 'Q' : '.');
        printf("\n");
    }
}

void solve(int row) {
    int col;
    if (row == n) {
        print_solution();
        return;
    }
    for (col = 0; col < n; col++) {
        if (safe(row, col)) {
            position[row] = col;
            solve(row + 1);
        }
    }
}

int main(void) {
    printf("Enter N (1 to %d): ", MAX);
    if (scanf("%d", &n) != 1 || n < 1 || n > MAX) {
        printf("Invalid N.\n");
        return 1;
    }
    solve(0);
    if (solutions == 0)
        printf("No solution exists for N = %d.\n", n);
    else
        printf("\nTotal solutions: %d\n", solutions);
    return 0;
}
