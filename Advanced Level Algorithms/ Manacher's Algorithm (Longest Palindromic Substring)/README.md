Manacher's Algorithm: Finding the Longest Palindromic Substring
1. What is Manacher's Algorithm?

Manacher's Algorithm is an O(n) solution for finding the longest palindromic substring in a given string. Unlike brute-force (O(n³)) or dynamic programming (O(n²)) approaches, it achieves linear time by exploiting palindrome symmetry.
Key Features

    Linear Time (O(n)): Much faster than DP (O(n²))

    Space Efficient (O(n)): Uses an array to store palindrome radii

    Handles Even & Odd Palindromes: By inserting special characters (e.g., #)

2. Why Use Manacher's Algorithm?
Applications

    DNA Sequence Analysis

        Finding palindromic sequences in genomes.

    Plagiarism Detection

        Identifying mirrored text patterns.

    Cybersecurity

        Detecting symmetric malware signatures.

    Text Processing

        Searching for mirrored words or phrases.

Real-World Analogy: Mirror Checking

Imagine standing between two mirrors:

    The center is where you stand (palindrome midpoint).

    The reflections extend symmetrically (palindrome expansion).

    Manacher's algorithm efficiently tracks how far each reflection goes without recalculating.

3. Problem Statement

Given a string s, return the longest palindromic substring in s.

Example:
text

Input: "babad"
Output: "bab" (or "aba")

Constraints:

    1 <= s.length <= 1000

    s consists of only digits and English letters.

4. Intuition Behind Manacher's Algorithm

    Transform the String

        Insert # between characters to handle even-length palindromes uniformly.
        Example: "babad" → "#b#a#b#a#d#"

    Palindrome Radius Array (P)

        P[i] = radius of the longest palindrome centered at i.

        Example: For "#a#b#a#", P[3] = 3 (palindrome "aba").

    Exploit Symmetry

        Use previously computed P values to avoid redundant checks.

5. Step-by-Step Algorithm
Phase 1: String Transformation
python

def preprocess(s):
    return '#' + '#'.join(s) + '#'

Example:
"babad" → "#b#a#b#a#d#"
Phase 2: Compute Palindrome Radii (P)

Initialize:

    C = 0 (center of the current longest palindrome)

    R = 0 (right boundary of the current longest palindrome)

    P = [0] * n (stores radii)

For each i from 1 to n-1:

    Mirror Index (mirror)
    mirror = 2 * C - i (symmetric position of i around C)

    Initialize P[i]

        If i < R, P[i] = min(R - i, P[mirror])

        Else, P[i] = 0

    Expand Around i
    While T[i + P[i] + 1] == T[i - P[i] - 1], increment P[i].

    Update C and R
    If i + P[i] > R, set C = i and R = i + P[i].

Phase 3: Extract Longest Palindrome

Find max(P) and reconstruct the substring.