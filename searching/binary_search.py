def binary_search(sorted_collection, target_elem):
    lo, hi = 0, len(sorted_collection) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        current_elem = sorted_collection[mid]
        if target_elem == current_elem:  # Element found!
            return mid
        if target_elem < current_elem:  # Search on the left side
            hi = mid - 1
        else:  # Search on the right side
            lo = mid + 1
    return None  # The element doesn't exist
