Dynamic Programming on Strings: Mastering LCS and Edit Distance
1. Introduction to String DP Problems

String problems often require finding optimal substructures in sequences. DP excels here because:

    Strings have inherent ordering

    Subproblems naturally overlap

    Solutions build up from smaller to larger substrings

Key Characteristics:

    Usually involve a 2D DP table where dp[i][j] represents state comparing prefixes up to i and j

    Transition between states depends on character matches/mismatches

    Often have O(n²) time and space complexity

2. Longest Common Subsequence (LCS)
Problem Statement

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.