def quick_sort(arr):
    """Sorts the array using the Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[-1]  # Choosing the last element as pivot
    smaller, equal, larger = [], [], []

    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    # Recursively sort smaller and larger partitions
    return quick_sort(smaller) + equal + quick_sort(larger)

# Example Usage
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print("Original Array:", array)
    sorted_array = quick_sort(array)
    print("Sorted Array:", sorted_array)
