def insertion_sort(collection):
    for i in range(1, len(collection)):
        current_elem = collection[i]
        j = i
        while j > 0 and current_elem < collection[j - 1]:
            collection[j] = collection[j - 1]  # Make space to insert the current element
            j -= 1
        collection[j] = current_elem  # Insert the current element on the right place
    return collection
