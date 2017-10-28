def counting_sort(collection, maxval):
    n = maxval + 1
    count = [0] * n  # Initialize counter
    for i in collection:
        count[i] += 1
    j = 0
    for i in range(n):  # Iterate through possible values
        while count[i] > 0:
            collection[j] = i  # in-place sort
            j += 1
            count[i] -= 1
    return collection
