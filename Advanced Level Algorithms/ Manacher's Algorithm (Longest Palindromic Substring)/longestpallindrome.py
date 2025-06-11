def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    # Step 1: Transform the string
    T = '#' + '#'.join(s) + '#'
    n = len(T)
    P = [0] * n
    C, R = 0, 0

    for i in range(n):
        # Step 2: Find the mirror of i
        mirror = 2 * C - i

        # Step 3: Initialize P[i]
        if i < R:
            P[i] = min(R - i, P[mirror])

        # Step 4: Expand around i
        a, b = i + (1 + P[i]), i - (1 + P[i])
        while a < n and b >= 0 and T[a] == T[b]:
            P[i] += 1
            a += 1
            b -= 1

        # Step 5: Update C and R if needed
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Step 6: Find the maximum radius and its center
    max_len, center = max((val, idx) for idx, val in enumerate(P))
    start = (center - max_len) // 2
    return s[start: start + max_len]