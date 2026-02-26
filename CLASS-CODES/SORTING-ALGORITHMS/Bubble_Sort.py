# ============================================================
# BUBBLE SORT — Python Implementation with Line-by-Line Notes
# ============================================================

# HOW IT WORKS:
# Compare adjacent pairs; if left > right, swap them.
# After each pass, the largest unsorted element 'bubbles' to its correct end.
# Repeat until no swaps occur (array is sorted).

def bubble_sort(arr):  # arr = list of numbers to sort
    # len() returns the total number of elements in the list
    n = len(arr)

    # OUTER LOOP: controls how many passes we make
    # We need at most (n-1) passes to fully sort
    for i in range(n - 1):   # i = 0, 1, 2 ... n-2

        # Optimization: track whether any swap happened this pass
        # If no swaps → array is already sorted → stop early
        swapped = False

        # INNER LOOP: compare adjacent elements
        # After i passes, last i elements are already sorted
        # So we only compare up to index (n-1-i)
        for j in range(0, n - 1 - i): # j = 0 to n-2-i

            # Compare current element with the next one
            if arr[j] > arr[j + 1]:  # Wrong order?

                # SWAP: Python's elegant simultaneous swap
                # Same as: temp=arr[j]; arr[j]=arr[j+1]; arr[j+1]=temp
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True   # A swap occurred!

        # No swaps in this entire pass → already sorted!
        if not swapped:
            break  # Early exit — saves time on nearly-sorted arrays

    return arr  # Return the sorted list

# ── TEST ──────────────────────────────────────────────────────
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numbers)  # [64,34,25,12,22,11,90]
result = bubble_sort(numbers)
print("Sorted:  ", result)   # [11,12,22,25,34,64,90]
