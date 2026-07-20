# def factorial(n):
#     if n <= 1:           # Base case
#         return 1
#     return n * factorial(n - 1)

# print(factorial(4))

def binary_search(items, target):
    lo, hi = 0, len(items) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            lo = mid + 1      # Go right
        else:
            hi = mid - 1      # Go left

    return -1
numbers = [2, 5, 8, 12, 16, 23, 38, 56]

target = 23

result = binary_search(numbers, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")