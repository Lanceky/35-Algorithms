def merge_sort(arr):
    #Base case: If array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    #Step 1 : Divide array into halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    #Step 2: Recursively sort each half
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    #Step 3: Merge the two sorted halves
    return merge(left_sorted , right_sorted) #function definintion below:

def merge(left, right):
    merged = []
    i = j = 0

    #Compare elements and add the smaller one to merged
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements ( if any_)
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged