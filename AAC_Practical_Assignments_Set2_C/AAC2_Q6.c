/* Q6. Strassen's Matrix Multiplication
   This implementation pads square matrices to the next power of 2. */
#include <stdio.h>
#include <stdlib.h>

#define MAX_N 64

void add(int n, int A[n][n], int B[n][n], int C[n][n]) {
    int i, j;
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
}

void sub(int n, int A[n][n], int B[n][n], int C[n][n]) {
    int i, j;
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            C[i][j] = A[i][j] - B[i][j];
}

void strassen(int n, int A[n][n], int B[n][n], int C[n][n]) {
    int i, j;
    if (n == 1) {
        C[0][0] = A[0][0] * B[0][0];
        return;
    }

    int m = n / 2;
    int A11[m][m], A12[m][m], A21[m][m], A22[m][m];
    int B11[m][m], B12[m][m], B21[m][m], B22[m][m];
    int M1[m][m], M2[m][m], M3[m][m], M4[m][m], M5[m][m], M6[m][m], M7[m][m];
    int X[m][m], Y[m][m];
    int C11[m][m], C12[m][m], C21[m][m], C22[m][m];

    for (i = 0; i < m; i++) {
        for (j = 0; j < m; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + m];
            A21[i][j] = A[i + m][j];
            A22[i][j] = A[i + m][j + m];
            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j + m];
            B21[i][j] = B[i + m][j];
            B22[i][j] = B[i + m][j + m];
        }
    }

    add(m, A11, A22, X); add(m, B11, B22, Y); strassen(m, X, Y, M1);
    add(m, A21, A22, X); strassen(m, X, B11, M2);
    sub(m, B12, B22, Y); strassen(m, A11, Y, M3);
    sub(m, B21, B11, Y); strassen(m, A22, Y, M4);
    add(m, A11, A12, X); strassen(m, X, B22, M5);
    sub(m, A21, A11, X); add(m, B11, B12, Y); strassen(m, X, Y, M6);
    sub(m, A12, A22, X); add(m, B21, B22, Y); strassen(m, X, Y, M7);

    add(m, M1, M4, X); sub(m, X, M5, Y); add(m, Y, M7, C11);
    add(m, M3, M5, C12);
    add(m, M2, M4, C21);
    sub(m, M1, M2, X); add(m, X, M3, Y); add(m, Y, M6, C22);

    for (i = 0; i < m; i++) {
        for (j = 0; j < m; j++) {
            C[i][j] = C11[i][j];
            C[i][j + m] = C12[i][j];
            C[i + m][j] = C21[i][j];
            C[i + m][j + m] = C22[i][j];
        }
    }
}

int main(void) {
    int n, size = 1, i, j;
    printf("Enter matrix order N (1 to %d): ", MAX_N);
    if (scanf("%d", &n) != 1 || n < 1 || n > MAX_N) {
        printf("Invalid matrix order.\n");
        return 1;
    }

    while (size < n) size *= 2;

    int (*A)[size] = calloc((size_t)size, sizeof *A);
    int (*B)[size] = calloc((size_t)size, sizeof *B);
    int (*C)[size] = calloc((size_t)size, sizeof *C);
    if (!A || !B || !C) {
        printf("Memory allocation failed.\n");
        free(A); free(B); free(C);
        return 1;
    }

    printf("Enter elements of matrix A (%d x %d):\n", n, n);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            if (scanf("%d", &A[i][j]) != 1) {
                printf("Invalid input.\n");
                free(A); free(B); free(C);
                return 1;
            }

    printf("Enter elements of matrix B (%d x %d):\n", n, n);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            if (scanf("%d", &B[i][j]) != 1) {
                printf("Invalid input.\n");
                free(A); free(B); free(C);
                return 1;
            }

    strassen(size, A, B, C);
    printf("Product matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }

    free(A); free(B); free(C);
    return 0;
}
