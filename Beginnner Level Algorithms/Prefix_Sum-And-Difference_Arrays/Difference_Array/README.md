2. Difference Array (For Range Updates)
Problem Statement

Given an array, you need to efficiently apply multiple range updates (e.g., "add x to all elements between indices l and r") and then retrieve the final array. A brute-force approach would take O(n) per update, but with a difference array, we can apply each update in O(1) and reconstruct the final array in O(n).

Example:

    Initial Array: [1, 2, 3, 4, 5]

    Updates:

        Add 2 to indices 1 to 3

        Subtract 1 from indices 2 to 4

    Expected Final Array: [1, 4, 4, 5, 4]

How Difference Array Works

    Preprocessing:

        Construct a diff array where:

            diff[0] = arr[0]

            diff[i] = arr[i] - arr[i-1] for i > 0

    Applying Range Updates in O(1):

        To add x to elements from l to r:

            diff[l] += x

            diff[r + 1] -= x (if r + 1 < n)

    Reconstructing the Final Array:

        Compute the prefix sum of diff to get the modified array.

Example Calculation:

    Initial array: [1, 2, 3, 4, 5]

    diff = [1, 1, 1, 1, 1]

    Update 1: Add 2 to indices 1 to 3:

        diff[1] += 2 → diff = [1, 3, 1, 1, 1]

        diff[4] -= 2 → diff = [1, 3, 1, 1, -1]

    Update 2: Subtract 1 from indices 2 to 4:

        diff[2] -= 1 → diff = [1, 3, 0, 1, -1]

        diff[5] is out of bounds (ignored).

    Reconstructing the final array:

        arr[0] = diff[0] = 1

        arr[1] = arr[0] + diff[1] = 1 + 3 = 4

        arr[2] = arr[1] + diff[2] = 4 + 0 = 4

        arr[3] = arr[2] + diff[3] = 4 + 1 = 5

        arr[4] = arr[3] + diff[4] = 5 - 1 = 4

    Final Array: [1, 4, 4, 5, 4]