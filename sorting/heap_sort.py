def sift_down(collection, start, end):
    def left_child(root):
        return root * 2 + 1
    root = start
    while left_child(root) <= end:  # While root has at least one child
        # Find greatest child
        child = left_child(root)  # Left child is the greatest child
        # If there is a right child and it's greater than the left one
        if child + 1 <= end and collection[child + 1] > collection[child]:
            child += 1  # Right child is the greatest child
        if collection[child] <= collection[root]:  # If root holds the greatest element..
            break  # ..we are done, heap is valid.
        collection[root], collection[child] = collection[child], collection[root]  # Swap root with greatest child
        root = child  # Continue sifting down the child now


def heap_sort(collection):
    def _heapify(collection, n):
        """Build MaxHeap in-place"""
        start = n // 2 - 1  # Last parent node
        while start >= 0:
            sift_down(collection, start, n - 1)  # Sift down node at index 'start' to the proper place
            start -= 1  # Continue with next parent node

    n = len(collection)
    _heapify(collection, n)
    heap_end = n - 1
    # collection[:heap_end + 1] is the heap
    # collection[heap_end + 1:] is the sorted collection
    while heap_end > 0:
        # Swap max heap element in front of sorted collection
        collection[0], collection[heap_end] = collection[heap_end], collection[0]
        heap_end -= 1  # Reduce heap size by one
        sift_down(collection, 0, heap_end)  # Restore heap property
    return collection
