Problem Statement: 0/1 Knapsack

Given:

    Weights [1, 2, 3]

    Values [10, 15, 40]

    Capacity W = 5

Goal:
Maximize value without exceeding weight 5.

Optimal Subset:

    [2, 3] → Weight = 5, Value = 15 + 40 = 55 (Best possible).

Solution: DP for 0/1 Knapsack
DP State:

    dp[i][w] = Max value achievable with first i items and weight limit w.

Transitions:

    Exclude i-th item:

        dp[i][w] = dp[i-1][w]

    Include i-th item (if weight ≤ w):

        dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i]] + value[i])