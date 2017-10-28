def merge_sort(collection):
    def _merge(left, right):
        i = j = k = 0
        left_length, right_length = len(left), len(right)
        while i < left_length and j < right_length:  # While both sides have elements
            if left[i] < right[j]:  # Element from left side is smaller..
                collection[k] = left[i]  # ..add it to the result
                i += 1
            else:  # Element from right side is smaller..
                collection[k] = right[j]  # ..add it to the result
                j += 1
            k += 1
        # Add the remaining elements to the result (if any)
        while i < left_length:  # Look on left side
            collection[k] = left[i]
            i += 1
            k += 1
        while j < right_length:  # Look on right side
            collection[k] = right[j]
            j += 1
            k += 1

    n = len(collection)
    if n > 1:  # Recursion base case (collection of size <= 1 is sorted)
        mid = n // 2
        left, right = merge_sort(collection[:mid]), merge_sort(collection[mid:])  # merge_sort both sides recursively
        _merge(left, right)  # Merge each side together
    return collection
