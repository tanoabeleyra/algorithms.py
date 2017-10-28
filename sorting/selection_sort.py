def selection_sort(collection):
    n = len(collection)
    for i in range(n):
        minimum = i  # Assume the min is the first element
        for j in range(i + 1, n):  # Test against elements after i (right) to find the minimum
            if collection[j] < collection[minimum]:
                minimum = j  # Found new minimum, remember it's index
        collection[i], collection[minimum] = collection[minimum], collection[i]  # Swapping
    return collection
