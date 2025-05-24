Knuth-Morris-Pratt (KMP) Algorithm: Efficient Pattern Matching
1. Core Concept

The KMP algorithm improves upon naive string matching by eliminating unnecessary comparisons through a preprocessed prefix table (LPS array). It achieves O(n + m) time complexity (vs. naive O(n×m)).
Key Components

    Longest Prefix Suffix (LPS) Array: Stores lengths of longest proper prefix which is also suffix

    Two-Phase Process:

        Preprocessing (LPS construction) → O(m)

        Pattern matching → O(n)

2. Real-World Analogies
DNA Sequence Matching

    Pattern: A gene sequence (e.g., "AGCTAG")

    Text: Full DNA strand

    KMP Benefit: Skips irrelevant nucleotides during matching

Text Search (Ctrl+F)

    Pattern: Search term

    Document: Full text

    KMP Advantage: Jumps ahead after mismatches

3. Problem Statement

Given a text T and pattern P, find all starting indices where P occurs in T.

Example:
python

Text: "ABABDABACDABABCABAB"
Pattern: "ABABCABAB"
Output: [10]  # Pattern starts at index 10

5. Complexity Analysis
Phase	Time Complexity	Space Complexity
LPS Construction	O(m)	O(m)
Pattern Matching	O(n)	O(1)
Total	O(n + m)	O(m)
6. Why KMP Beats Naive Matching
Naive Approach

    Compares pattern at every text position

    Worst case: O(m×n) (e.g., searching "AAAAA" in "AAAAAAAAAB")

KMP Optimization

    LPS Array: Knows how much to skip after mismatch

    No Backtracking: Text pointer (i) never moves backward

7. Key Insights

    LPS Array Magic:

        Tracks the longest prefix that's also a suffix

        Enables "intelligent jumps" during matching

    Efficiency Gain:

        Avoids re-checking known matches

        Particularly effective for patterns with repetitions

8. When to Use KMP

    Searching large texts for repetitive patterns

    DNA/Protein sequence alignment

    Plagiarism detection systems

    Implementations of str.find() in some languages

9. Practice Problems

    Implement strStr() (LeetCode #28)

    Repeated Substring Pattern (LeetCode #459)

    Shortest Palindrome (LeetCode #214)

10. Comparison with Other Algorithms
Algorithm	Time	Best For
Naive	O(mn)	Small strings
KMP	O(n + m)	Texts with repetitions
Boyer-Moore	O(n/m) avg	English text
Rabin-Karp	O(n + m)	Multiple pattern search