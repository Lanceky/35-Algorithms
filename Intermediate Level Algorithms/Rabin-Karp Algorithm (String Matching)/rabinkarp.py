def rabin_karp_search(text, pattern):
    """Find all starting indices of pattern in text using Rabin-Karp algorithm."""
    n, m = len(text), len(pattern)
    if n < m:
        return []

    # Prime number for hashing and base (number of characters in alphabet)
    prime = 101
    base = 256
    pattern_hash = 0
    window_hash = 0
    h = 1  # hash multiplier for leading digit

    # Calculate h = pow(base, m-1) % prime
    for _ in range(m - 1):
        h = (h * base) % prime

    # Compute initial hash values for pattern and first window
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    matches = []

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if current window's hash matches pattern's hash
        if pattern_hash == window_hash:
            # Verify characters one by one to prevent hash collision
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                matches.append(i)

        # Compute hash for next window
        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Ensure hash is positive
            if window_hash < 0:
                window_hash += prime

    return matches


# Test
text = "GATTACAGATTACAGATTACA"
pattern = "GATTACA"
print(rabin_karp_search(text, pattern))  # Output: [0, 7, 14]