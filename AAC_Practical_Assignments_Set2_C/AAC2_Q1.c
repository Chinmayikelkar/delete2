/* Q1. Fractional Knapsack using Greedy Method */
#include <stdio.h>

typedef struct {
    float profit, weight, ratio;
} Item;

int main(void) {
    int n, i, j;
    float capacity, totalProfit = 0.0f;

    printf("Enter number of items: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid number of items.\n");
        return 1;
    }

    Item items[n];
    for (i = 0; i < n; i++) {
        printf("Enter profit and weight of item %d: ", i + 1);
        if (scanf("%f %f", &items[i].profit, &items[i].weight) != 2 ||
            items[i].weight <= 0 || items[i].profit < 0) {
            printf("Invalid profit or weight.\n");
            return 1;
        }
        items[i].ratio = items[i].profit / items[i].weight;
    }

    printf("Enter knapsack capacity: ");
    if (scanf("%f", &capacity) != 1 || capacity < 0) {
        printf("Invalid capacity.\n");
        return 1;
    }

    /* Sort items by profit/weight ratio in descending order. */
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (items[j].ratio > items[i].ratio) {
                Item temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }
    }

    for (i = 0; i < n && capacity > 0; i++) {
        if (items[i].weight <= capacity) {
            capacity -= items[i].weight;
            totalProfit += items[i].profit;
        } else {
            totalProfit += items[i].ratio * capacity;
            capacity = 0;
        }
    }

    printf("Maximum profit = %.2f\n", totalProfit);
    return 0;
}
