def bubble_sort(collection):
    n = len(collection)  # Upper limit per pass (dynamic)
    while True:  # Repeat until the collection is sorted (n-1 passes at most)
        last_swap = None  # Position of the last swapped element in current pass
        for i in range(0, n - 1):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]  # Swapping
                last_swap = i  # Sorted portion starts at last_swap+1
        if last_swap is None:  # The collection is sorted
            return collection
        n = last_swap + 1  # New upper limit (ignore already sorted portion)
    return collection
