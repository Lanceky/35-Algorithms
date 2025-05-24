def build_lps_table(pattern):
    # Initialize the LPS array to store the prefix-suffix lengths for the pattern.
    lps = [0] * len(pattern)
    # Track the length of the current prefix that is also a suffix.
    prefix_len = 0

    # Iterate through the pattern starting from the second character.
    for i in range(1, len(pattern)):
        # Handle mismatch by falling back to a shorter prefix.
        while prefix_len > 0 and pattern[i] != pattern[prefix_len]:
            # Update prefix length using the LPS value of the previous prefix.
            prefix_len = lps[prefix_len - 1]

        # If characters match, extend the prefix length.
        if pattern[i] == pattern[prefix_len]:
            # Increment the prefix length by 1.
            prefix_len += 1
            # Store the prefix length at the current index in the LPS array.
            lps[i] = prefix_len

    # Return the completed LPS array.
    return lps


def find_pattern_matches(text, pattern):
    # If the pattern is empty, return an empty list.
    if not pattern:
        return []

    # Preprocess the pattern to construct its LPS table.
    lps_table = build_lps_table(pattern)
    # Create a list to store the starting indices of pattern matches in the text.
    matches = []
    # Track the current position in the pattern being matched.
    pattern_idx = 0

    # Loop through each character in the text.
    for text_idx, char in enumerate(text):
        # Handle mismatch by using the LPS table to skip comparisons.
        while pattern_idx > 0 and char != pattern[pattern_idx]:
            # Move the pattern index to the length of the longest prefix-suffix.
            pattern_idx = lps_table[pattern_idx - 1]

        # If characters match, move to the next character in the pattern.
        if char == pattern[pattern_idx]:
            # Increment the pattern index.
            pattern_idx += 1

            # If a complete match is found, record its starting index.
            if pattern_idx == len(pattern):
                # Add the start index of the match to the results.
                matches.append(text_idx - pattern_idx + 1)
                # Reset the pattern index for the next potential match.
                pattern_idx = lps_table[pattern_idx - 1]

    # Return the list of match starting indices.
    return matches


# Demonstration
if __name__ == "__main__":
    sample_text = "ABABDABACDABABCABAB"
    sample_pattern = "ABABCABAB"
    print(find_pattern_matches(sample_text, sample_pattern))  # Output: [10]
