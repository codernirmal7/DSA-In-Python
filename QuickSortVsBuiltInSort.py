# import random, time

# arr = [random.randint(0, 1000000) for _ in range(100000)]

# # Built-in sort
# start = time.time()
# sorted_arr = sorted(arr)
# print("Built-in sort:", time.time() - start)

# # Custom quicksort
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     less = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)

# start = time.time()
# sorted_arr2 = quicksort(arr)
# print("Quicksort:", time.time() - start)

import time
from typing import List

def counting_sort(arr: List[int], max_value: int = None) -> List[int]:
    """
    Sorts a list of non‑negative integers using counting sort.
    Time: O(n + k), where k = max_value
    """
    if not arr:
        return []
    if max_value is None:
        max_value = max(arr)
    count = [0] * (max_value + 1)
    for x in arr:
        count[x] += 1
    # accumulate counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    # place elements in output (stable)
    for x in reversed(arr):
        count[x] -= 1
        output[count[x]] = x
    return output

def radix_sort(arr: List[int], base: int = 10) -> List[int]:
    """
    Sorts a list of non‑negative integers using LSD radix sort.
    Time: O(d * (n + base)), where d = number of digits in the largest number.
    """
    if not arr:
        return []
    # find the maximum to know number of digits
    max_val = max(arr)
    exp = 1
    output = list(arr)
    # process each digit position
    while max_val // exp > 0:
        # counting sort by current digit
        buckets = [0] * base
        for x in output:
            digit = (x // exp) % base
            buckets[digit] += 1
        for i in range(1, base):
            buckets[i] += buckets[i - 1]
        temp = [0] * len(output)
        for x in reversed(output):
            digit = (x // exp) % base
            buckets[digit] -= 1
            temp[buckets[digit]] = x
        output = temp
        exp *= base
    return output

if __name__ == "__main__":
    import random
    
    # Generate test data
    N = 300_000
    MAX_VAL = 10_000
    data = [random.randint(0, MAX_VAL) for _ in range(N)]
    
    # Benchmark counting sort (only if MAX_VAL not too large)
    if MAX_VAL < 1_000_000:
        start = time.time()
        sorted_by_count = counting_sort(data, max_value=MAX_VAL)
        print(f"Counting sort: {time.time() - start:.4f}s")
    
    # Benchmark radix sort
    start = time.time()
    sorted_by_radix = radix_sort(data, base=256)  # base=256 reduces digit passes
    print(f"Radix sort (base=256): {time.time() - start:.4f}s")
    
    # Benchmark built-in
    start = time.time()
    builtin = sorted(data)
    print(f"Built-in sort(): {time.time() - start:.4f}s")
    
    # Verify correctness
    assert builtin == sorted_by_radix
    if MAX_VAL < 1_000_000:
        assert builtin == sorted_by_count
    print("All sorts produce the same result.")
