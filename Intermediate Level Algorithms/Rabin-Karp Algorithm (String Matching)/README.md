Rabin-Karp Algorithm: Efficient String Matching with Hashing
1. Core Concept

Rabin-Karp is a string matching algorithm that uses hashing to find patterns in text. Unlike naive matching, it compares hash values first before doing character-by-character comparison.
Key Features

    Average case O(n + m) time complexity (n = text length, m = pattern length)

    Worst case O(n×m) (when hash collisions are frequent)

    Uses rolling hash for efficient hash recomputation

2. Real-World Analogies
1. Library Book Search

Imagine searching for a book with call number "510.23" in a library:

    First check: Compare shelf labels (hash values)

    Second check: Only inspect books with matching labels (full comparison)

2. DNA Sequence Alignment

    Pattern: Gene segment "GATTACA"

    Text: Full DNA sequence

    Benefit: Quickly skips non-matching regions using hash values

3. Problem Statement

Given:

    text (string to search through)

    pattern (string to find)

Find all starting indices where pattern appears in text.

Example:
python

text = "GATTACAGATTACAGATTACA"
pattern = "GATTACA"
# Output: [0, 7, 14] (matches at positions 0, 7, and 14)