# Coverage Report

Total executable lines: 14
Covered lines: 14
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def mergeSortedLists(arr1, arr2):
2: ✓     i, j = 0, 0
3: ✓     merged = []
4: ✓     while i < len(arr1) and j < len(arr2):
5: ✓         if arr1[i] <= arr2[j]:
6: ✓             merged.append(arr1[i])
7: ✓             i += 1
8:           else:
9: ✓             merged.append(arr2[j])
10: ✓             j += 1
11: ✓     if i < len(arr1):
12: ✓         merged.extend(arr1[i:])
13: ✓     if j < len(arr2):
14: ✓         merged.extend(arr2[j:])
15: ✓     return merged
```

## Complete Test File

```python
def mergeSortedLists(arr1, arr2):
    i, j = 0, 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    if i < len(arr1):
        merged.extend(arr1[i:])
    if j < len(arr2):
        merged.extend(arr2[j:])
    return merged

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = mergeSortedLists([1, 3, 5], [2, 4, 6])
        assert result == [1, 2, 3, 4, 5, 6], f"Test 1 failed: got {result}, expected {[1, 2, 3, 4, 5, 6]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = mergeSortedLists([], [])
        assert result == [], f"Test 2 failed: got {result}, expected {[]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = mergeSortedLists([-2, 0, 1], [-3, -1])
        assert result == [-3, -2, -1, 0, 1], f"Test 3 failed: got {result}, expected {[-3, -2, -1, 0, 1]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = mergeSortedLists([10, 20, 30], [5, 25, 35])
        assert result == [5, 10, 20, 25, 30, 35], f"Test 4 failed: got {result}, expected {[5, 10, 20, 25, 30, 35]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = mergeSortedLists([1, 2, 2], [2, 3, 3])
        assert result == [1, 2, 2, 2, 3, 3], f"Test 5 failed: got {result}, expected {[1, 2, 2, 2, 3, 3]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = mergeSortedLists([1, 2, 2, 4], [2, 2, 3, 5])
        assert result == [1, 2, 2, 2, 2, 3, 4, 5], f"Test 6 failed: got {result}, expected {[1, 2, 2, 2, 2, 3, 4, 5]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = mergeSortedLists([-10, -3, 0, 8], [-9, -4, 1, 2])
        assert result == [-10, -9, -4, -3, 0, 1, 2, 8], f"Test 7 failed: got {result}, expected {[-10, -9, -4, -3, 0, 1, 2, 8]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = mergeSortedLists([1, 2, 3], [10, 20, 30])
        assert result == [1, 2, 3, 10, 20, 30], f"Test 8 failed: got {result}, expected {[1, 2, 3, 10, 20, 30]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = mergeSortedLists([0, 10, 20, 30, 40], [5, 15, 25, 35, 45])
        assert result == [0, 5, 10, 15, 20, 25, 30, 35, 40, 45], f"Test 9 failed: got {result}, expected {[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = mergeSortedLists([-5, -5, -1, 3], [-6, -2, -2, 4])
        assert result == [-6, -5, -5, -2, -2, -1, 3, 4], f"Test 10 failed: got {result}, expected {[-6, -5, -5, -2, -2, -1, 3, 4]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = mergeSortedLists([-2147483648, -1, 0], [1, 2147483647])
        assert result == [-2147483648, -1, 0, 1, 2147483647], f"Test 11 failed: got {result}, expected {[-2147483648, -1, 0, 1, 2147483647]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = mergeSortedLists([-1000, 0, 1000, 2000], [-999, -500, 1500, 2500])
        assert result == [-1000, -999, -500, 0, 1000, 1500, 2000, 2500], f"Test 12 failed: got {result}, expected {[-1000, -999, -500, 0, 1000, 1500, 2000, 2500]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = mergeSortedLists([-7, -3, 2, 2, 9], [-8, -3, 0, 10])
        assert result == [-8, -7, -3, -3, 0, 2, 2, 9, 10], f"Test 13 failed: got {result}, expected {[-8, -7, -3, -3, 0, 2, 2, 9, 10]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = mergeSortedLists([-2, 0, 2], [-2, 0, 2])
        assert result == [-2, -2, 0, 0, 2, 2], f"Test 14 failed: got {result}, expected {[-2, -2, 0, 0, 2, 2]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = mergeSortedLists([1, 4], [2, 3, 5, 6, 7])
        assert result == [1, 2, 3, 4, 5, 6, 7], f"Test 15 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = mergeSortedLists([-10, -5, 0, 5, 10], [6])
        assert result == [-10, -5, 0, 5, 6, 10], f"Test 16 failed: got {result}, expected {[-10, -5, 0, 5, 6, 10]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = mergeSortedLists([9, 9], [9, 10])
        assert result == [9, 9, 9, 10], f"Test 17 failed: got {result}, expected {[9, 9, 9, 10]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = mergeSortedLists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8, 10])
        assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], f"Test 18 failed: got {result}, expected {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = mergeSortedLists([-1, 0, 1], [1, 1, 2, 3])
        assert result == [-1, 0, 1, 1, 1, 2, 3], f"Test 19 failed: got {result}, expected {[-1, 0, 1, 1, 1, 2, 3]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = mergeSortedLists([-1000000000, 0, 1000000000], [-999999999, 999999999])
        assert result == [-1000000000, -999999999, 0, 999999999, 1000000000], f"Test 20 failed: got {result}, expected {[-1000000000, -999999999, 0, 999999999, 1000000000]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = mergeSortedLists([-20, -15, -15, -1], [-30, -10, -10, 0])
        assert result == [-30, -20, -15, -15, -10, -10, -1, 0], f"Test 21 failed: got {result}, expected {[-30, -20, -15, -15, -10, -10, -1, 0]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = mergeSortedLists([1, 1, 1, 2], [2, 2, 2])
        assert result == [1, 1, 1, 2, 2, 2, 2], f"Test 22 failed: got {result}, expected {[1, 1, 1, 2, 2, 2, 2]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = mergeSortedLists([3, 5], [2, 4, 6])
        assert result == [2, 3, 4, 5, 6], f"Test 23 failed: got {result}, expected {[2, 3, 4, 5, 6]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = mergeSortedLists([2, 3, 5, 6], [2, 6])
        assert result == [2, 2, 3, 5, 6, 6], f"Test 24 failed: got {result}, expected {[2, 2, 3, 5, 6, 6]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = mergeSortedLists([1], [2, 4, 6])
        assert result == [1, 2, 4, 6], f"Test 25 failed: got {result}, expected {[1, 2, 4, 6]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = mergeSortedLists([1, 5], [2, 4, 6])
        assert result == [1, 2, 4, 5, 6], f"Test 26 failed: got {result}, expected {[1, 2, 4, 5, 6]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = mergeSortedLists([0], [1000])
        assert result == [0, 1000], f"Test 27 failed: got {result}, expected {[0, 1000]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = mergeSortedLists([-999999999, 0], [0])
        assert result == [-999999999, 0, 0], f"Test 28 failed: got {result}, expected {[-999999999, 0, 0]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = mergeSortedLists([-2, 1, 25], [-3, -1])
        assert result == [-3, -2, -1, 1, 25], f"Test 29 failed: got {result}, expected {[-3, -2, -1, 1, 25]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = mergeSortedLists([-2, 0], [-3, -1, 0])
        assert result == [-3, -2, -1, 0, 0], f"Test 30 failed: got {result}, expected {[-3, -2, -1, 0, 0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = mergeSortedLists([-2, 0, 1, 9], [-6, -1])
        assert result == [-6, -2, -1, 0, 1, 9], f"Test 31 failed: got {result}, expected {[-6, -2, -1, 0, 1, 9]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = mergeSortedLists([-2, 0, 1, 2500], [-1, 20])
        assert result == [-2, -1, 0, 1, 20, 2500], f"Test 32 failed: got {result}, expected {[-2, -1, 0, 1, 20, 2500]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = mergeSortedLists([20, 30], [5, 25, 35])
        assert result == [5, 20, 25, 30, 35], f"Test 33 failed: got {result}, expected {[5, 20, 25, 30, 35]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = mergeSortedLists([10, 20, 30], [5, 35])
        assert result == [5, 10, 20, 30, 35], f"Test 34 failed: got {result}, expected {[5, 10, 20, 30, 35]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = mergeSortedLists([1, 2], [2, 3, 3, 2000])
        assert result == [1, 2, 2, 3, 3, 2000], f"Test 35 failed: got {result}, expected {[1, 2, 2, 3, 3, 2000]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = mergeSortedLists([0, 2, 2], [2, 3, 3])
        assert result == [0, 2, 2, 2, 3, 3], f"Test 36 failed: got {result}, expected {[0, 2, 2, 2, 3, 3]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = mergeSortedLists([2, 2], [3, 7])
        assert result == [2, 2, 3, 7], f"Test 37 failed: got {result}, expected {[2, 2, 3, 7]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = mergeSortedLists([1, 15], [-1000000000, 5])
        assert result == [-1000000000, 1, 5, 15], f"Test 38 failed: got {result}, expected {[-1000000000, 1, 5, 15]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = mergeSortedLists([0, 1, 2, 3], [0, 4, 5, 6])
        assert result == [0, 0, 1, 2, 3, 4, 5, 6], f"Test 39 failed: got {result}, expected {[0, 0, 1, 2, 3, 4, 5, 6]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = mergeSortedLists([1, 2, 3], [4])
        assert result == [1, 2, 3, 4], f"Test 40 failed: got {result}, expected {[1, 2, 3, 4]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = mergeSortedLists([0, 0], [1])
        assert result == [0, 0, 1], f"Test 41 failed: got {result}, expected {[0, 0, 1]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = mergeSortedLists([7], [8])
        assert result == [7, 8], f"Test 42 failed: got {result}, expected {[7, 8]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = mergeSortedLists([1, 6], [2, 4, 6, 36])
        assert result == [1, 2, 4, 6, 6, 36], f"Test 43 failed: got {result}, expected {[1, 2, 4, 6, 6, 36]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = mergeSortedLists([1], [4, 4, 6])
        assert result == [1, 4, 4, 6], f"Test 44 failed: got {result}, expected {[1, 4, 4, 6]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = mergeSortedLists([0, 3, 5], [2, 4, 6])
        assert result == [0, 2, 3, 4, 5, 6], f"Test 45 failed: got {result}, expected {[0, 2, 3, 4, 5, 6]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = mergeSortedLists([1, 3, 5], [2, 4])
        assert result == [1, 2, 3, 4, 5], f"Test 46 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = mergeSortedLists([1], [2, 4, 6])
        assert result == [1, 2, 4, 6], f"Test 47 failed: got {result}, expected {[1, 2, 4, 6]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = mergeSortedLists([1, 2, 3, 4], [2, 2, 3, 5])
        assert result == [1, 2, 2, 2, 3, 3, 4, 5], f"Test 48 failed: got {result}, expected {[1, 2, 2, 2, 3, 3, 4, 5]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = mergeSortedLists([1], [2, 3, 5])
        assert result == [1, 2, 3, 5], f"Test 49 failed: got {result}, expected {[1, 2, 3, 5]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = mergeSortedLists([1, 2, 4], [2, 3, 5])
        assert result == [1, 2, 2, 3, 4, 5], f"Test 50 failed: got {result}, expected {[1, 2, 2, 3, 4, 5]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
