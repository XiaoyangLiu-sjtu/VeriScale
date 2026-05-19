# Coverage Report

Total executable lines: 9
Covered lines: 9
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def BubbleSort(a):
2: ✓     def swap(arr, i, j):
3: ✓         arr[i], arr[j] = arr[j], arr[i]
4: ✓     n = len(a)
5: ✓     for i in range(n):
6: ✓         for j in range(0, n - i - 1):
7: ✓             if a[j] > a[j + 1]:
8: ✓                 swap(a, j, j + 1)
9: ✓     return a
```

## Complete Test File

```python
def BubbleSort(a):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                swap(a, j, j + 1)
    return a

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = BubbleSort([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5], f"Test 1 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = BubbleSort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5], f"Test 2 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = BubbleSort([3, 1, 2, 1, 5])
        assert result == [1, 1, 2, 3, 5], f"Test 3 failed: got {result}, expected {[1, 1, 2, 3, 5]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = BubbleSort([10])
        assert result == [10], f"Test 4 failed: got {result}, expected {[10]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = BubbleSort([4, 4, 4, 2, 2, 8])
        assert result == [2, 2, 4, 4, 4, 8], f"Test 5 failed: got {result}, expected {[2, 2, 4, 4, 4, 8]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = BubbleSort([5, 1, 2, 1, 3, 11, 0, 0])
        assert result == [0, 0, 1, 1, 2, 3, 5, 11], f"Test 6 failed: got {result}, expected {[0, 0, 1, 1, 2, 3, 5, 11]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = BubbleSort([3, 1, 2, 1, 5, 33])
        assert result == [1, 1, 2, 3, 5, 33], f"Test 7 failed: got {result}, expected {[1, 1, 2, 3, 5, 33]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = BubbleSort([0, 5, 1, 2, 1, 12])
        assert result == [0, 1, 1, 2, 5, 12], f"Test 8 failed: got {result}, expected {[0, 1, 1, 2, 5, 12]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = BubbleSort([-2, 997, 5, 1, 2, 1, 3])
        assert result == [-2, 1, 1, 2, 3, 5, 997], f"Test 9 failed: got {result}, expected {[-2, 1, 1, 2, 3, 5, 997]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = BubbleSort([8, 2, 4, 4, 4])
        assert result == [2, 4, 4, 4, 8], f"Test 10 failed: got {result}, expected {[2, 4, 4, 4, 8]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = BubbleSort([2, 4, 4, 15])
        assert result == [2, 4, 4, 15], f"Test 11 failed: got {result}, expected {[2, 4, 4, 15]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = BubbleSort([4, 4, 4, 100, 2, 8, 0, 20, 0])
        assert result == [0, 0, 2, 4, 4, 4, 8, 20, 100], f"Test 12 failed: got {result}, expected {[0, 0, 2, 4, 4, 4, 8, 20, 100]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = BubbleSort([4, 4, 4, 2, 2, 8, -1002])
        assert result == [-1002, 2, 2, 4, 4, 4, 8], f"Test 13 failed: got {result}, expected {[-1002, 2, 2, 4, 4, 4, 8]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = BubbleSort([0, 41, 0, -1002])
        assert result == [-1002, 0, 0, 41], f"Test 14 failed: got {result}, expected {[-1002, 0, 0, 41]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = BubbleSort([0, 0, 1001])
        assert result == [0, 0, 1001], f"Test 15 failed: got {result}, expected {[0, 0, 1001]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = BubbleSort([5, 1, 2, 1, 6, -30])
        assert result == [-30, 1, 1, 2, 5, 6], f"Test 16 failed: got {result}, expected {[-30, 1, 1, 2, 5, 6]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = BubbleSort([0, 0, 5, 1, 2, 1, 3])
        assert result == [0, 0, 1, 1, 2, 3, 5], f"Test 17 failed: got {result}, expected {[0, 0, 1, 1, 2, 3, 5]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = BubbleSort([3, 1, 1, 1, 5, 0])
        assert result == [0, 1, 1, 1, 3, 5], f"Test 18 failed: got {result}, expected {[0, 1, 1, 1, 3, 5]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = BubbleSort([97, 5, 1, 2, 1, 3, 0, -8, -33])
        assert result == [-33, -8, 0, 1, 1, 2, 3, 5, 97], f"Test 19 failed: got {result}, expected {[-33, -8, 0, 1, 1, 2, 3, 5, 97]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = BubbleSort([10, -10, 0, 30, 0, 11])
        assert result == [-10, 0, 0, 10, 11, 30], f"Test 20 failed: got {result}, expected {[-10, 0, 0, 10, 11, 30]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = BubbleSort([2147483647, -2147483648, 0, 2147483646, -2147483647, 0])
        assert result == [-2147483648, -2147483647, 0, 0, 2147483646, 2147483647], f"Test 21 failed: got {result}, expected {[-2147483648, -2147483647, 0, 0, 2147483646, 2147483647]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = BubbleSort([0, 1, -1, 0, 1, -1, 0, 0, 20, 0, 9])
        assert result == [-1, -1, 0, 0, 0, 0, 0, 1, 1, 9, 20], f"Test 22 failed: got {result}, expected {[-1, -1, 0, 0, 0, 0, 0, 1, 1, 9, 20]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = BubbleSort([42, 1, -1, -3, 2, -1, 0, 0])
        assert result == [-3, -1, -1, 0, 0, 1, 2, 42], f"Test 23 failed: got {result}, expected {[-3, -1, -1, 0, 0, 1, 2, 42]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = BubbleSort([0, -1, 1, 0, -1, 1])
        assert result == [-1, -1, 0, 0, 1, 1], f"Test 24 failed: got {result}, expected {[-1, -1, 0, 0, 1, 1]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = BubbleSort([0, 0, -1, 1, 0, -1, 1, 0])
        assert result == [-1, -1, 0, 0, 0, 0, 1, 1], f"Test 25 failed: got {result}, expected {[-1, -1, 0, 0, 0, 0, 1, 1]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = BubbleSort([9, 8, 7, 6, 4, 3, 2, 1, 0, 0])
        assert result == [0, 0, 1, 2, 3, 4, 6, 7, 8, 9], f"Test 26 failed: got {result}, expected {[0, 0, 1, 2, 3, 4, 6, 7, 8, 9]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = BubbleSort([0, 1, 0, -50, 0, 1, 0, 1])
        assert result == [-50, 0, 0, 0, 0, 1, 1, 1], f"Test 27 failed: got {result}, expected {[-50, 0, 0, 0, 0, 1, 1, 1]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = BubbleSort([0, 1, 1, 0, 1, 0, 1, 24])
        assert result == [0, 0, 0, 1, 1, 1, 1, 24], f"Test 28 failed: got {result}, expected {[0, 0, 0, 1, 1, 1, 1, 24]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = BubbleSort([0, 1, 0, 1, 0, 1, 0, 1, 100])
        assert result == [0, 0, 0, 0, 1, 1, 1, 1, 100], f"Test 29 failed: got {result}, expected {[0, 0, 0, 0, 1, 1, 1, 1, 100]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = BubbleSort([-10, 11, -9, -8, 8, 7, 7, -2147483648])
        assert result == [-2147483648, -10, -9, -8, 7, 7, 8, 11], f"Test 30 failed: got {result}, expected {[-2147483648, -10, -9, -8, 7, 7, 8, 11]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = BubbleSort([-10, 10, -9, 9, -8, 9, 0, 7])
        assert result == [-10, -9, -8, 0, 7, 9, 9, 10], f"Test 31 failed: got {result}, expected {[-10, -9, -8, 0, 7, 9, 9, 10]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = BubbleSort([100, -100, 50, -50, 25, -25, 20, 0, 0])
        assert result == [-100, -50, -25, 0, 0, 20, 25, 50, 100], f"Test 32 failed: got {result}, expected {[-100, -50, -25, 0, 0, 20, 25, 50, 100]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = BubbleSort([100, -100, -2147483648, 25, -25, 0, 997, 0])
        assert result == [-2147483648, -100, -25, 0, 0, 25, 100, 997], f"Test 33 failed: got {result}, expected {[-2147483648, -100, -25, 0, 0, 25, 100, 997]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = BubbleSort([3, 5, 3, 3, 3, 5, 0])
        assert result == [0, 3, 3, 3, 3, 5, 5], f"Test 34 failed: got {result}, expected {[0, 3, 3, 3, 3, 5, 5]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = BubbleSort([1, 3, 4, 4, 6, 5, 7, 6, -33])
        assert result == [-33, 1, 3, 4, 4, 5, 6, 6, 7], f"Test 35 failed: got {result}, expected {[-33, 1, 3, 4, 4, 5, 6, 6, 7]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = BubbleSort([3, 0, 6, 5, 7, 9, 8, 7, 0])
        assert result == [0, 0, 3, 5, 6, 7, 7, 8, 9], f"Test 36 failed: got {result}, expected {[0, 0, 3, 5, 6, 7, 7, 8, 9]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = BubbleSort([-3, -2, -2, 1, -1, -1])
        assert result == [-3, -2, -2, -1, -1, 1], f"Test 37 failed: got {result}, expected {[-3, -2, -2, -1, -1, 1]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = BubbleSort([-1, -1, -1, -2, -2, -3, 0, 11, 0, 0])
        assert result == [-3, -2, -2, -1, -1, -1, 0, 0, 0, 11], f"Test 38 failed: got {result}, expected {[-3, -2, -2, -1, -1, -1, 0, 0, 0, 11]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = BubbleSort([-1, -1, -1, -3, 0, -50])
        assert result == [-50, -3, -1, -1, -1, 0], f"Test 39 failed: got {result}, expected {[-50, -3, -1, -1, -1, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = BubbleSort([-1, -2, -1, -2, -2, -3, 0])
        assert result == [-3, -2, -2, -2, -1, -1, 0], f"Test 40 failed: got {result}, expected {[-3, -2, -2, -2, -1, -1, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = BubbleSort([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, 0, 0, 100, 0, -100])
        assert result == [-100, -3, -2, -1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 100], f"Test 41 failed: got {result}, expected {[-100, -3, -2, -1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 100]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = BubbleSort([-3, -2, 0, -2, 1, 2, 3, 4, 5, 6, -84])
        assert result == [-84, -3, -2, -2, 0, 1, 2, 3, 4, 5, 6], f"Test 42 failed: got {result}, expected {[-84, -3, -2, -2, 0, 1, 2, 3, 4, 5, 6]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = BubbleSort([11, 22, 22, 11, -11, -22, -33, 1001, 50, 0])
        assert result == [-33, -22, -11, 0, 11, 11, 22, 22, 50, 1001], f"Test 43 failed: got {result}, expected {[-33, -22, -11, 0, 11, 11, 22, 22, 50, 1001]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = BubbleSort([0, 0, 9, 0, 3, 5, 7, 6])
        assert result == [0, 0, 0, 3, 5, 6, 7, 9], f"Test 44 failed: got {result}, expected {[0, 0, 0, 3, 5, 6, 7, 9]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = BubbleSort([1, -1, -1, 1, -1, 1, -1, 0, 999999, 0, 0, -1])
        assert result == [-1, -1, -1, -1, -1, 0, 0, 0, 1, 1, 1, 999999], f"Test 45 failed: got {result}, expected {[-1, -1, -1, -1, -1, 0, 0, 0, 1, 1, 1, 999999]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = BubbleSort([1, -1, 2147483644, -1, 1, -1, -123456788, -1, 0, 0])
        assert result == [-123456788, -1, -1, -1, -1, 0, 0, 1, 1, 2147483644], f"Test 46 failed: got {result}, expected {[-123456788, -1, -1, -1, -1, 0, 0, 1, 1, 2147483644]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = BubbleSort([50, 30, 20, 10, 0, -10, -20, -30, -40, -50, 0, 43])
        assert result == [-50, -40, -30, -20, -10, 0, 0, 10, 20, 30, 43, 50], f"Test 47 failed: got {result}, expected {[-50, -40, -30, -20, -10, 0, 0, 10, 20, 30, 43, 50]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = BubbleSort([3, 3, 2, 2, 1, 1, 0, 0, -1, 0, -84, 0, 0])
        assert result == [-84, -1, 0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3], f"Test 48 failed: got {result}, expected {[-84, -1, 0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = BubbleSort([3, 2, 2, 1, 1, 0, 0, -1, -1, 0])
        assert result == [-1, -1, 0, 0, 0, 1, 1, 2, 2, 3], f"Test 49 failed: got {result}, expected {[-1, -1, 0, 0, 0, 1, 1, 2, 2, 3]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = BubbleSort([4, 1, 3, 2, 6, 0, -1, 8, 7, 6, 0, 0])
        assert result == [-1, 0, 0, 0, 1, 2, 3, 4, 6, 6, 7, 8], f"Test 50 failed: got {result}, expected {[-1, 0, 0, 0, 1, 2, 3, 4, 6, 6, 7, 8]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = BubbleSort([0, -9223372036854775808, -1, 1, 0, -8])
        assert result == [-9223372036854775808, -8, -1, 0, 0, 1], f"Test 51 failed: got {result}, expected {[-9223372036854775808, -8, -1, 0, 0, 1]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
