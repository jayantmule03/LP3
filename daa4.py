
def knapsack(capacity, weights, values, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items: "))
values = list(map(int, input("Enter values separated by spaces: ").split()))
weights = list(map(int, input("Enter weights separated by spaces: ").split()))

if len(values) != n or len(weights) != n:
    print("Error: Enter exactly", n, "values and weights.")
else:
    capacity = int(input("Enter knapsack capacity: "))
    print("Maximum value:", knapsack(capacity, weights, values, n))
