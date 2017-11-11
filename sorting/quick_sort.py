def quick_sort(collection):
    def _quick_sort(collection, lo, hi):
        if lo < hi:
            p = partition(collection, lo, hi)
            _quick_sort(collection, lo, p)
            _quick_sort(collection, p + 1, hi)
            return collection

    def partition(collection, lo, hi):
        """Hoare partition scheme"""
        pivot = collection[lo]
        while True:
            while collection[lo] < pivot:  # Find index of element bigger than pivot (left-to-right)
                lo += 1
            while collection[hi] > pivot:  # Find index of element smaller than pivot (right-to-left)
                hi -= 1
            if lo >= hi:  # If elements are in the right order we are done
                return hi  # Return pivot index
            # Elements are in the wrong order
            collection[lo], collection[hi] = collection[hi], collection[lo]  # Swap elements

    return _quick_sort(collection, 0, len(collection) - 1)
