# Coverage Report

Total executable lines: 19
Covered lines: 19
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def mergeSort(lst):
2: ✓     if len(lst) <= 1:
3: ✓         return lst
4: ✓     mid = len(lst) // 2
5: ✓     left = mergeSort(lst[:mid])
6: ✓     right = mergeSort(lst[mid:])
7: ✓     return merge(left, right)
8:   
9: ✓ def merge(left, right):
10: ✓     result = []
11: ✓     i, j = 0, 0
12: ✓     while i < len(left) and j < len(right):
13: ✓         if left[i] < right[j]:
14: ✓             result.append(left[i])
15: ✓             i += 1
16:           else:
17: ✓             result.append(right[j])
18: ✓             j += 1
19: ✓     result.extend(left[i:])
20: ✓     result.extend(right[j:])
21: ✓     return result
```

## Complete Test File

```python
def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = mergeSort([5, 2, 9, 1, 5, 6])
        assert result == [1, 2, 5, 5, 6, 9], f"Test 1 failed: got {result}, expected {[1, 2, 5, 5, 6, 9]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = mergeSort([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == [1, 1, 2, 3, 4, 5, 6, 9], f"Test 2 failed: got {result}, expected {[1, 1, 2, 3, 4, 5, 6, 9]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = mergeSort([])
        assert result == [], f"Test 3 failed: got {result}, expected {[]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = mergeSort([1])
        assert result == [1], f"Test 4 failed: got {result}, expected {[1]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = mergeSort([5, 5, 5, 5])
        assert result == [5, 5, 5, 5], f"Test 5 failed: got {result}, expected {[5, 5, 5, 5]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = mergeSort([9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Test 6 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7, 8, 9]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = mergeSort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5], f"Test 7 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = mergeSort([-3, -1, -5, -2])
        assert result == [-5, -3, -2, -1], f"Test 8 failed: got {result}, expected {[-5, -3, -2, -1]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = mergeSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], f"Test 9 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = mergeSort([42, -42, 42, -42, 42, -42])
        assert result == [-42, -42, -42, 42, 42, 42], f"Test 10 failed: got {result}, expected {[-42, -42, -42, 42, 42, 42]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = mergeSort([8, 1, 6, 3, 5, 7, 4, 9, 2])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Test 11 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7, 8, 9]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = mergeSort([1, 2, 3, 4, 5, 6, 7, 9, 8])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Test 12 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7, 8, 9]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = mergeSort([99, 1, 98, 2, 97, 3, 96, 4, 95, 5])
        assert result == [1, 2, 3, 4, 5, 95, 96, 97, 98, 99], f"Test 13 failed: got {result}, expected {[1, 2, 3, 4, 5, 95, 96, 97, 98, 99]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = mergeSort([2147483647, 2147483647, -2147483648, -2147483648, 0, 0])
        assert result == [-2147483648, -2147483648, 0, 0, 2147483647, 2147483647], f"Test 14 failed: got {result}, expected {[-2147483648, -2147483648, 0, 0, 2147483647, 2147483647]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = mergeSort([-16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        assert result == '14, 15]', f"Test 15 failed: got {result}, expected {'14, 15]'}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = mergeSort([5, 2, 9, 1, 5, 6, 0])
        assert result == [0, 1, 2, 5, 5, 6, 9], f"Test 16 failed: got {result}, expected {[0, 1, 2, 5, 5, 6, 9]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = mergeSort([-42, 11, 6, 5, 1, 9, 2, 5])
        assert result == [-42, 1, 2, 5, 5, 6, 9, 11], f"Test 17 failed: got {result}, expected {[-42, 1, 2, 5, 5, 6, 9, 11]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = mergeSort([3, 1, 4, 1, 5, 9, 2, -42])
        assert result == [-42, 1, 1, 2, 3, 4, 5, 9], f"Test 18 failed: got {result}, expected {[-42, 1, 1, 2, 3, 4, 5, 9]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = mergeSort([6, 2, 9, 5, 1, 4, 1, 3])
        assert result == [1, 1, 2, 3, 4, 5, 6, 9], f"Test 19 failed: got {result}, expected {[1, 1, 2, 3, 4, 5, 6, 9]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = mergeSort([3, 1, 4, 1, 5, 9, 2])
        assert result == [1, 1, 2, 3, 4, 5, 9], f"Test 20 failed: got {result}, expected {[1, 1, 2, 3, 4, 5, 9]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = mergeSort([3, 1, 4, 1, 5, 9, 2, 6, 0, 24, 7])
        assert result == [0, 1, 1, 2, 3, 4, 5, 6, 7, 9, 24], f"Test 21 failed: got {result}, expected {[0, 1, 1, 2, 3, 4, 5, 6, 7, 9, 24]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = mergeSort([3, 1, 4, 1, 5, 9, 2, 6, 0])
        assert result == [0, 1, 1, 2, 3, 4, 5, 6, 9], f"Test 22 failed: got {result}, expected {[0, 1, 1, 2, 3, 4, 5, 6, 9]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = mergeSort([1, 0, 9007199254740991])
        assert result == [0, 1, 9007199254740991], f"Test 23 failed: got {result}, expected {[0, 1, 9007199254740991]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = mergeSort([-100, 5, 5, 5])
        assert result == [-100, 5, 5, 5], f"Test 24 failed: got {result}, expected {[-100, 5, 5, 5]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = mergeSort([9, 8, 7, 6, 5, 4, 3, 2, 1, 37])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 37], f"Test 25 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7, 8, 9, 37]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = mergeSort([1, 2, 3, 4, 5, 9007199254740991, -18])
        assert result == [-18, 1, 2, 3, 4, 5, 9007199254740991], f"Test 26 failed: got {result}, expected {[-18, 1, 2, 3, 4, 5, 9007199254740991]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = mergeSort([3, 3, 2, 1])
        assert result == [1, 2, 3, 3], f"Test 27 failed: got {result}, expected {[1, 2, 3, 3]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = mergeSort([1, 2, 0, 4, 5])
        assert result == [0, 1, 2, 4, 5], f"Test 28 failed: got {result}, expected {[0, 1, 2, 4, 5]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = mergeSort([-2, -5, -1, -3])
        assert result == [-5, -3, -2, -1], f"Test 29 failed: got {result}, expected {[-5, -3, -2, -1]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = mergeSort([1, 32, -8])
        assert result == [-8, 1, 32], f"Test 30 failed: got {result}, expected {[-8, 1, 32]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = mergeSort([2, 0, 0])
        assert result == [0, 0, 2], f"Test 31 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = mergeSort([1, 0, 9007199254740991])
        assert result == [0, 1, 9007199254740991], f"Test 32 failed: got {result}, expected {[0, 1, 9007199254740991]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = mergeSort([3, 3, 3, 3, 3, 12, -17, 28])
        assert result == [-17, 3, 3, 3, 3, 3, 12, 28], f"Test 33 failed: got {result}, expected {[-17, 3, 3, 3, 3, 3, 12, 28]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = mergeSort([1, 2, 3, -4, 32])
        assert result == [-4, 1, 2, 3, 32], f"Test 34 failed: got {result}, expected {[-4, 1, 2, 3, 32]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = mergeSort([0, 0, -2, -1, -3])
        assert result == [-3, -2, -1, 0, 0], f"Test 35 failed: got {result}, expected {[-3, -2, -1, 0, 0]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = mergeSort([6, 2, 9, 5, 1, 4, 1, 3])
        assert result == [1, 1, 2, 3, 4, 5, 6, 9], f"Test 36 failed: got {result}, expected {[1, 1, 2, 3, 4, 5, 6, 9]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = mergeSort([0, -3, 1, 2, 3, 4, 5, 6, 7, 8, 17, 10])
        assert result == [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 17], f"Test 37 failed: got {result}, expected {[-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 17]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = mergeSort([7, -3, 7, -3, 7, -3, 0, 0])
        assert result == [-3, -3, -3, 0, 0, 7, 7, 7], f"Test 38 failed: got {result}, expected {[-3, -3, -3, 0, 0, 7, 7, 7]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = mergeSort([0, -3, 7, -3, 7, -3, 7, -123456789, 0, 0, -5])
        assert result == [-123456789, -5, -3, -3, -3, 0, 0, 0, 7, 7, 7], f"Test 39 failed: got {result}, expected {[-123456789, -5, -3, -3, -3, 0, 0, 0, 7, 7, 7]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = mergeSort([1, 0, -1, 0, 1])
        assert result == [-1, 0, 0, 1, 1], f"Test 40 failed: got {result}, expected {[-1, 0, 0, 1, 1]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = mergeSort([100, 50, -50, 25, -25, 0, 74])
        assert result == [-50, -25, 0, 25, 50, 74, 100], f"Test 41 failed: got {result}, expected {[-50, -25, 0, 25, 50, 74, 100]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = mergeSort([2, 4, 7, 5, 3, 6, 1, 8])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8], f"Test 42 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7, 8]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = mergeSort([2, 3, 4, 1, 6, 7, 8, 9, 1, 2147483646, 72])
        assert result == [1, 1, 2, 3, 4, 6, 7, 8, 9, 72, 2147483646], f"Test 43 failed: got {result}, expected {[1, 1, 2, 3, 4, 6, 7, 8, 9, 72, 2147483646]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = mergeSort([42, 0, -11, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 0])
        assert result == [-11, 0, 0, 11, 13, 17, 19, 23, 29, 31, 37, 41, 42, 43], f"Test 44 failed: got {result}, expected {[-11, 0, 0, 11, 13, 17, 19, 23, 29, 31, 37, 41, 42, 43]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = mergeSort([43, 41, 37, 31, 29, 23, 19, 17, 13, 11, -9007199254740991, 3, 0])
        assert result == [-9007199254740991, 0, 3, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43], f"Test 45 failed: got {result}, expected {[-9007199254740991, 0, 3, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = mergeSort([43, 41, 0, 31, 29, 23, 19, 13, 11])
        assert result == [0, 11, 13, 19, 23, 29, 31, 41, 43], f"Test 46 failed: got {result}, expected {[0, 11, 13, 19, 23, 29, 31, 41, 43]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = mergeSort([0, 43, 41, 0, 31, 29, 23, 19, 17, 13, 11])
        assert result == [0, 0, 11, 13, 17, 19, 23, 29, 31, 41, 43], f"Test 47 failed: got {result}, expected {[0, 0, 11, 13, 17, 19, 23, 29, 31, 41, 43]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = mergeSort([0, -20, 0, 0, -5, 1, -4, 2, -3, 4, -2, 3, -1, 5])
        assert result == [-20, -5, -4, -3, -2, -1, 0, 0, 0, 1, 2, 3, 4, 5], f"Test 48 failed: got {result}, expected {[-20, -5, -4, -3, -2, -1, 0, 0, 0, 1, 2, 3, 4, 5]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = mergeSort([0, 2147483647, -2147483648, -2147483648, -1, 0, 0])
        assert result == [-2147483648, -2147483648, -1, 0, 0, 0, 2147483647], f"Test 49 failed: got {result}, expected {[-2147483648, -2147483648, -1, 0, 0, 0, 2147483647]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = mergeSort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0, 32, 0])
        assert result == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32], f"Test 50 failed: got {result}, expected {[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = mergeSort([-16, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 0])
        assert result == [-16, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15], f"Test 51 failed: got {result}, expected {[-16, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = mergeSort([12, -4, 7, 7, -30, 23, -1, 5, -9, 12, 8, -3, 14, -7, 6, 2, -11, 19, -2, 4, -6, 10, -8, 1, 0])
        assert result == [-30, -11, -9, -8, -7, -6, -4, -3, -2, -1, 0, 1, 2, 4, 5, 6, 7, 7, 8, 10, 12, 12, 14, 19, 23], f"Test 52 failed: got {result}, expected {[-30, -11, -9, -8, -7, -6, -4, -3, -2, -1, 0, 1, 2, 4, 5, 6, 7, 7, 8, 10, 12, 12, 14, 19, 23]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = mergeSort([41, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15, 16, -16, 17, -17, 18, -18, 19, -19, 20, -20, 21, -21, 22, -22, 23, -23, 24, -24, 25, -25])
        assert result == '2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 41]', f"Test 53 failed: got {result}, expected {'2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 41]'}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = mergeSort([-25, 25, -24, 24, -23, 23, -22, 22, -21, 21, -20, 20, -19, 19, -18, 18, -17, 17, -16, 16, -15, 15, -14, 14, -13, -12, -11, 11, -10, 10, -9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2, -1, 1])
        assert result == '2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]', f"Test 54 failed: got {result}, expected {'2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]'}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = mergeSort([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, 15, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15, 16, -16, 17, -17, 18, -18, 19, 20, -20, 21, -21, 22, -22, 23, -23, 24, -24, 25, -25, 31])
        assert result == '5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 31]', f"Test 55 failed: got {result}, expected {'5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 31]'}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
