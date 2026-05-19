# Coverage Report

Total executable lines: 11
Covered lines: 11
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def CanyonSearch(a, b):
2: ✓     i, j = 0, 0
3: ✓     min_diff = abs(a[0] - b[0])
4: ✓     while i < len(a) and j < len(b):
5: ✓         current_diff = abs(a[i] - b[j])
6: ✓         if current_diff < min_diff:
7: ✓             min_diff = current_diff
8: ✓         if a[i] < b[j]:
9: ✓             i += 1
10:           else:
11: ✓             j += 1
12: ✓     return min_diff
```

## Complete Test File

```python
def CanyonSearch(a, b):
    i, j = 0, 0
    min_diff = abs(a[0] - b[0])
    while i < len(a) and j < len(b):
        current_diff = abs(a[i] - b[j])
        if current_diff < min_diff:
            min_diff = current_diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = CanyonSearch([1, 3, 5], [2, 4, 6])
        assert result == 1, f"Test 1 failed: got {result}, expected {1}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = CanyonSearch([-5, -2, 0], [1, 3])
        assert result == 1, f"Test 2 failed: got {result}, expected {1}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = CanyonSearch([10, 20, 30], [5, 15, 25])
        assert result == 5, f"Test 3 failed: got {result}, expected {5}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = CanyonSearch([1, 2, 3, 4, 5], [3])
        assert result == 0, f"Test 4 failed: got {result}, expected {0}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = CanyonSearch([-10, -5, 0, 5, 10], [-3, 2, 8])
        assert result == 2, f"Test 5 failed: got {result}, expected {2}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = CanyonSearch([0], [0])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = CanyonSearch([1], [2])
        assert result == 1, f"Test 7 failed: got {result}, expected {1}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = CanyonSearch([-1], [1])
        assert result == 2, f"Test 8 failed: got {result}, expected {2}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = CanyonSearch([1, 2, 3], [4, 5, 6])
        assert result == 1, f"Test 9 failed: got {result}, expected {1}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = CanyonSearch([4, 5, 6], [1, 2, 3])
        assert result == 1, f"Test 10 failed: got {result}, expected {1}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = CanyonSearch([-5, -3, -1], [-4, -2, 0])
        assert result == 1, f"Test 11 failed: got {result}, expected {1}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = CanyonSearch([-10, -10, -5, 0], [-10, -9, -9, 3])
        assert result == 0, f"Test 12 failed: got {result}, expected {0}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = CanyonSearch([1, 1, 1, 1], [1, 1])
        assert result == 0, f"Test 13 failed: got {result}, expected {0}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = CanyonSearch([1, 1, 2, 2, 3, 3], [0, 2, 4])
        assert result == 0, f"Test 14 failed: got {result}, expected {0}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = CanyonSearch([-100, 0, 100], [-50, 50])
        assert result == 50, f"Test 15 failed: got {result}, expected {50}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = CanyonSearch([-1000, -500, -100], [100, 500, 1000])
        assert result == 200, f"Test 16 failed: got {result}, expected {200}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = CanyonSearch([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
        assert result == 1, f"Test 17 failed: got {result}, expected {1}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = CanyonSearch([-8, -6, -4, -2], [-7, -5, -3, -1])
        assert result == 1, f"Test 18 failed: got {result}, expected {1}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = CanyonSearch([0, 5, 10, 15], [6])
        assert result == 1, f"Test 19 failed: got {result}, expected {1}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = CanyonSearch([6], [0, 5, 10, 15])
        assert result == 1, f"Test 20 failed: got {result}, expected {1}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = CanyonSearch([3, 3, 3, 7, 9], [3])
        assert result == 0, f"Test 21 failed: got {result}, expected {0}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = CanyonSearch([-3], [-3, -3, 0, 4])
        assert result == 0, f"Test 22 failed: got {result}, expected {0}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = CanyonSearch([-1000000000000, 0, 1000000000000], [-999999999999, 2])
        assert result == 1, f"Test 23 failed: got {result}, expected {1}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = CanyonSearch([2147483647], [-2147483648])
        assert result == 4294967295, f"Test 24 failed: got {result}, expected {4294967295}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = CanyonSearch([-2147483648, -1, 0, 1, 2147483647], [2147483646])
        assert result == 1, f"Test 25 failed: got {result}, expected {1}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = CanyonSearch([-9, -4, 2, 2, 2, 11], [-10, -4, 3, 12])
        assert result == 0, f"Test 26 failed: got {result}, expected {0}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = CanyonSearch([5, 10, 15, 20, 25, 30], [0, 30])
        assert result == 0, f"Test 27 failed: got {result}, expected {0}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = CanyonSearch([-20, -15, -10, -5], [-5])
        assert result == 0, f"Test 28 failed: got {result}, expected {0}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = CanyonSearch([42], [1, 2, 3, 40, 41, 43, 44])
        assert result == 1, f"Test 29 failed: got {result}, expected {1}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = CanyonSearch([-50, -25, 0, 25, 50], [-49, -24, 1, 26, 51])
        assert result == 1, f"Test 30 failed: got {result}, expected {1}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = CanyonSearch([7, 14, 21, 28], [7, 14, 21, 28])
        assert result == 0, f"Test 31 failed: got {result}, expected {0}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = CanyonSearch([-2, -2, -2, -2], [-3, -2, -1])
        assert result == 0, f"Test 32 failed: got {result}, expected {0}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = CanyonSearch([0, 0, 0, 0, 0], [1])
        assert result == 1, f"Test 33 failed: got {result}, expected {1}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = CanyonSearch([-1, 0, 1], [-1, 0, 1])
        assert result == 0, f"Test 34 failed: got {result}, expected {0}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = CanyonSearch([100, 200, 300, 400, 500], [-1000, -500, 0, 500, 1000])
        assert result == 0, f"Test 35 failed: got {result}, expected {0}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = CanyonSearch([-100, -50, -25, -12, -6, -3, -1], [2, 4, 8, 16, 32])
        assert result == 3, f"Test 36 failed: got {result}, expected {3}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = CanyonSearch([9, 18, 27, 36, 45, 54], [8, 17, 26, 35, 44, 53, 62])
        assert result == 1, f"Test 37 failed: got {result}, expected {1}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = CanyonSearch([3, 5], [2, 4, 6])
        assert result == 1, f"Test 38 failed: got {result}, expected {1}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = CanyonSearch([1, 3, 5], [-2, 4, 6, 14])
        assert result == 1, f"Test 39 failed: got {result}, expected {1}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = CanyonSearch([1, 3, 200], [2, 4, 6])
        assert result == 1, f"Test 40 failed: got {result}, expected {1}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = CanyonSearch([-5, 0], [1, 3])
        assert result == 1, f"Test 41 failed: got {result}, expected {1}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = CanyonSearch([-5, -2, 0, 0], [1, 3])
        assert result == 1, f"Test 42 failed: got {result}, expected {1}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = CanyonSearch([20], [6, 15, 25])
        assert result == 5, f"Test 43 failed: got {result}, expected {5}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = CanyonSearch([10, 20, 31], [5, 15, 25])
        assert result == 5, f"Test 44 failed: got {result}, expected {5}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = CanyonSearch([1, 2, 3, 4, 5], [3, 400])
        assert result == 0, f"Test 45 failed: got {result}, expected {0}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = CanyonSearch([1, 2, 3, 4, 5], [0, 3])
        assert result == 0, f"Test 46 failed: got {result}, expected {0}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = CanyonSearch([-10, -5, 0, 5, 10], [-3, 2, 8, 8])
        assert result == 2, f"Test 47 failed: got {result}, expected {2}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = CanyonSearch([-10, -5, 0, 5, 10, 25], [-3, 2, 8])
        assert result == 2, f"Test 48 failed: got {result}, expected {2}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = CanyonSearch([-10, -5, 0, 5, 10, 12], [-3, 2, 8])
        assert result == 2, f"Test 49 failed: got {result}, expected {2}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = CanyonSearch([-10, -5, 0, 5], [-3, 2, 8])
        assert result == 2, f"Test 50 failed: got {result}, expected {2}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = CanyonSearch([0], [0, 15])
        assert result == 0, f"Test 51 failed: got {result}, expected {0}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = CanyonSearch([0, 0], [62])
        assert result == 62, f"Test 52 failed: got {result}, expected {62}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = CanyonSearch([0], [6])
        assert result == 6, f"Test 53 failed: got {result}, expected {6}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = CanyonSearch([0], [2147483647])
        assert result == 2147483647, f"Test 54 failed: got {result}, expected {2147483647}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = CanyonSearch([27], [0])
        assert result == 27, f"Test 55 failed: got {result}, expected {27}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = CanyonSearch([41], [0, 0])
        assert result == 41, f"Test 56 failed: got {result}, expected {41}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = CanyonSearch([0, 0], [0, 0])
        assert result == 0, f"Test 57 failed: got {result}, expected {0}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = CanyonSearch([0], [-1, 0, 0])
        assert result == 0, f"Test 58 failed: got {result}, expected {0}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = CanyonSearch([0], [11])
        assert result == 11, f"Test 59 failed: got {result}, expected {11}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = CanyonSearch([0, 44], [13])
        assert result == 13, f"Test 60 failed: got {result}, expected {13}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = CanyonSearch([0, 0], [0, 1000])
        assert result == 0, f"Test 61 failed: got {result}, expected {0}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = CanyonSearch([0], [1])
        assert result == 1, f"Test 62 failed: got {result}, expected {1}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = CanyonSearch([0], [0, 0])
        assert result == 0, f"Test 63 failed: got {result}, expected {0}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = CanyonSearch([43], [0])
        assert result == 43, f"Test 64 failed: got {result}, expected {43}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = CanyonSearch([0, 0], [0])
        assert result == 0, f"Test 65 failed: got {result}, expected {0}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = CanyonSearch([1], [0])
        assert result == 1, f"Test 66 failed: got {result}, expected {1}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = CanyonSearch([0, 1], [2])
        assert result == 1, f"Test 67 failed: got {result}, expected {1}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = CanyonSearch([0], [2])
        assert result == 2, f"Test 68 failed: got {result}, expected {2}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = CanyonSearch([-1, 0], [1])
        assert result == 1, f"Test 69 failed: got {result}, expected {1}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = CanyonSearch([-1], [2, 15])
        assert result == 3, f"Test 70 failed: got {result}, expected {3}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = CanyonSearch([0, 0], [1])
        assert result == 1, f"Test 71 failed: got {result}, expected {1}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = CanyonSearch([-2, 0, 0], [1])
        assert result == 1, f"Test 72 failed: got {result}, expected {1}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = CanyonSearch([-2], [0])
        assert result == 2, f"Test 73 failed: got {result}, expected {2}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = CanyonSearch([-1], [0])
        assert result == 1, f"Test 74 failed: got {result}, expected {1}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = CanyonSearch([-1, 0], [1, 2147483646])
        assert result == 1, f"Test 75 failed: got {result}, expected {1}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = CanyonSearch([1, 2, 3], [4, 4, 6])
        assert result == 1, f"Test 76 failed: got {result}, expected {1}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = CanyonSearch([1, 2, 3, 36, 400], [4, 6])
        assert result == 1, f"Test 77 failed: got {result}, expected {1}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = CanyonSearch([1, 2, 3, 6], [4, 5, 6])
        assert result == 0, f"Test 78 failed: got {result}, expected {0}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = CanyonSearch([-1, 3], [0, 5, 6])
        assert result == 1, f"Test 79 failed: got {result}, expected {1}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = CanyonSearch([3, 5, 6], [1, 2, 3, 18])
        assert result == 0, f"Test 80 failed: got {result}, expected {0}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = CanyonSearch([4], [2, 2, 3])
        assert result == 1, f"Test 81 failed: got {result}, expected {1}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = CanyonSearch([0, 5, 6], [1, 2, 3])
        assert result == 1, f"Test 82 failed: got {result}, expected {1}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = CanyonSearch([6], [3, 16])
        assert result == 3, f"Test 83 failed: got {result}, expected {3}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = CanyonSearch([4, 5], [1, 2, 3])
        assert result == 1, f"Test 84 failed: got {result}, expected {1}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = CanyonSearch([-3, 0], [-4, -2, 0, 0])
        assert result == 0, f"Test 85 failed: got {result}, expected {0}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = CanyonSearch([-5, -3, -1], [-4, 0])
        assert result == 1, f"Test 86 failed: got {result}, expected {1}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = CanyonSearch([-5, -3, -1], [-4, -2, 0, 5])
        assert result == 1, f"Test 87 failed: got {result}, expected {1}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = CanyonSearch([-5, -1], [-4, -2, 0, 0])
        assert result == 1, f"Test 88 failed: got {result}, expected {1}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = CanyonSearch([-5, -3, -2], [-4, -2])
        assert result == 0, f"Test 89 failed: got {result}, expected {0}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = CanyonSearch([-10, -10, -5, 0], [-10, -9, -9])
        assert result == 0, f"Test 90 failed: got {result}, expected {0}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = CanyonSearch([-10, -10, -5], [-10, -9, -9, 3])
        assert result == 0, f"Test 91 failed: got {result}, expected {0}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = CanyonSearch([1, 1, 1, 1], [-20, 1, 27])
        assert result == 0, f"Test 92 failed: got {result}, expected {0}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = CanyonSearch([1, 1, 1], [0, 1, 1])
        assert result == 0, f"Test 93 failed: got {result}, expected {0}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = CanyonSearch([1, 1, 1, 1, 40], [1, 43])
        assert result == 0, f"Test 94 failed: got {result}, expected {0}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = CanyonSearch([1, 1, 2, 2, 3, 3], [-2147483648, 4])
        assert result == 1, f"Test 95 failed: got {result}, expected {1}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = CanyonSearch([1, 2, 3, 3, 3], [0, 4])
        assert result == 1, f"Test 96 failed: got {result}, expected {1}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = CanyonSearch([1, 1, 2, 2, 3], [0, 2, 7])
        assert result == 0, f"Test 97 failed: got {result}, expected {0}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = CanyonSearch([1, 1, 2, 2, 3, 3], [2, 4])
        assert result == 0, f"Test 98 failed: got {result}, expected {0}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = CanyonSearch([-100, 0, 100], [-50, -2])
        assert result == 2, f"Test 99 failed: got {result}, expected {2}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = CanyonSearch([-100, 100], [50])
        assert result == 50, f"Test 100 failed: got {result}, expected {50}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = CanyonSearch([-1000, -500, 0], [100, 500, 1000])
        assert result == 100, f"Test 101 failed: got {result}, expected {100}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = CanyonSearch([-1000, -500, -100, 0], [54, 500, 1000])
        assert result == 54, f"Test 102 failed: got {result}, expected {54}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = CanyonSearch([2, 4, 6, 8, 10], [1, 3, 7, 9, 999])
        assert result == 1, f"Test 103 failed: got {result}, expected {1}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = CanyonSearch([-8, -6, -4, -2, 999], [-7, -5, -3, -1])
        assert result == 1, f"Test 104 failed: got {result}, expected {1}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = CanyonSearch([-8, -6, -4], [-7, -5, -3, -1, 300])
        assert result == 1, f"Test 105 failed: got {result}, expected {1}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = CanyonSearch([-8, -6, -2], [-7, -5, -3, -1, 0, 0, 0, 0])
        assert result == 1, f"Test 106 failed: got {result}, expected {1}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = CanyonSearch([-8, -6, -4, -2, 49], [-7, -5, -3, -1, 0])
        assert result == 1, f"Test 107 failed: got {result}, expected {1}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = CanyonSearch([-6, -4, -2], [-7, -5, -3, -1])
        assert result == 1, f"Test 108 failed: got {result}, expected {1}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = CanyonSearch([-6, -4, -2, 49], [-7, -5, -3, -1, 0])
        assert result == 1, f"Test 109 failed: got {result}, expected {1}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = CanyonSearch([-8, -6, -4, -2, 0, 43], [-7, -5, -3, -1])
        assert result == 1, f"Test 110 failed: got {result}, expected {1}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = CanyonSearch([0, 5, 10, 15, 44], [6])
        assert result == 1, f"Test 111 failed: got {result}, expected {1}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = CanyonSearch([0, 5, 10, 15], [6, 14])
        assert result == 1, f"Test 112 failed: got {result}, expected {1}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = CanyonSearch([0, 10, 15], [6])
        assert result == 4, f"Test 113 failed: got {result}, expected {4}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = CanyonSearch([0, 5, 10, 14], [100])
        assert result == 86, f"Test 114 failed: got {result}, expected {86}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = CanyonSearch([6], [1, 5, 10, 15])
        assert result == 1, f"Test 115 failed: got {result}, expected {1}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = CanyonSearch([12], [0, 5, 10, 15])
        assert result == 2, f"Test 116 failed: got {result}, expected {2}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = CanyonSearch([0], [0, 5, 10, 15])
        assert result == 0, f"Test 117 failed: got {result}, expected {0}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = CanyonSearch([3, 3, 3, 7, 9], [3, 6])
        assert result == 0, f"Test 118 failed: got {result}, expected {0}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = CanyonSearch([0], [-3, -3, 0, 4])
        assert result == 0, f"Test 119 failed: got {result}, expected {0}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = CanyonSearch([3], [-3, -3, 0, 4, 50])
        assert result == 1, f"Test 120 failed: got {result}, expected {1}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = CanyonSearch([-3], [-3, -3, -1, 4])
        assert result == 0, f"Test 121 failed: got {result}, expected {0}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = CanyonSearch([-3, 0], [-3, 0, 4])
        assert result == 0, f"Test 122 failed: got {result}, expected {0}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = CanyonSearch([0, 0], [-999999999999, 2])
        assert result == 2, f"Test 123 failed: got {result}, expected {2}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = CanyonSearch([0, 1000000000000], [-999999999999, 2])
        assert result == 2, f"Test 124 failed: got {result}, expected {2}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = CanyonSearch([0, 1000000000000], [-999999999999, -2, 6])
        assert result == 2, f"Test 125 failed: got {result}, expected {2}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = CanyonSearch([-1000000000000, 0, 1000000000000], [-999999999999, 0])
        assert result == 0, f"Test 126 failed: got {result}, expected {0}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = CanyonSearch([-1000000000000, -2147483648, 1000000000000], [-999999999999, 2])
        assert result == 1, f"Test 127 failed: got {result}, expected {1}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = CanyonSearch([-1000000000000, 0, 2000000000000], [-999999999999, -10, 0])
        assert result == 0, f"Test 128 failed: got {result}, expected {0}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = CanyonSearch([-1000000000000, 0, 2000000000000], [18])
        assert result == 18, f"Test 129 failed: got {result}, expected {18}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = CanyonSearch([400, 2147483647], [-2147483648, 0, 0])
        assert result == 400, f"Test 130 failed: got {result}, expected {400}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = CanyonSearch([2147483648], [-1, 0])
        assert result == 2147483648, f"Test 131 failed: got {result}, expected {2147483648}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = CanyonSearch([4294967292], [-2147483648, 17])
        assert result == 4294967275, f"Test 132 failed: got {result}, expected {4294967275}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = CanyonSearch([0], [-2147483648, 0])
        assert result == 0, f"Test 133 failed: got {result}, expected {0}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = CanyonSearch([2147483647], [-2147483649, -1])
        assert result == 2147483648, f"Test 134 failed: got {result}, expected {2147483648}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = CanyonSearch([2147483647], [-5])
        assert result == 2147483652, f"Test 135 failed: got {result}, expected {2147483652}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = CanyonSearch([2147483647], [-2147483648, 45])
        assert result == 2147483602, f"Test 136 failed: got {result}, expected {2147483602}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = CanyonSearch([-2147483648, -1, 1, 2147483647], [0, 8, 2147483646])
        assert result == 1, f"Test 137 failed: got {result}, expected {1}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = CanyonSearch([-9, -4, 2, 2, 2, 11], [-4, 3, 12])
        assert result == 0, f"Test 138 failed: got {result}, expected {0}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = CanyonSearch([-9, -4, 2, 2, 2, 50], [-10, -4])
        assert result == 0, f"Test 139 failed: got {result}, expected {0}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = CanyonSearch([-9, 2, 2, 2, 11], [-10, -4, 3, 12])
        assert result == 1, f"Test 140 failed: got {result}, expected {1}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = CanyonSearch([5, 10, 15, 20, 30], [0, 30])
        assert result == 0, f"Test 141 failed: got {result}, expected {0}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = CanyonSearch([5, 10, 15, 20, 25, 30], [0, 30, 44])
        assert result == 0, f"Test 142 failed: got {result}, expected {0}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = CanyonSearch([-20, -15, -10, -5], [-5, 0])
        assert result == 0, f"Test 143 failed: got {result}, expected {0}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = CanyonSearch([-20, -15, -10, -5, 43], [-5, 0])
        assert result == 0, f"Test 144 failed: got {result}, expected {0}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = CanyonSearch([-20, -15, -10, -5, 0], [-5, 0, 0])
        assert result == 0, f"Test 145 failed: got {result}, expected {0}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = CanyonSearch([-20, -15, -10, -5, 0], [-5, 0])
        assert result == 0, f"Test 146 failed: got {result}, expected {0}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = CanyonSearch([-20, -15, -10, -5, 0], [-5])
        assert result == 0, f"Test 147 failed: got {result}, expected {0}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = CanyonSearch([-49], [1, 2, 3, 40, 44])
        assert result == 50, f"Test 148 failed: got {result}, expected {50}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = CanyonSearch([0, 42], [1, 2, 3, 40, 43, 401])
        assert result == 1, f"Test 149 failed: got {result}, expected {1}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = CanyonSearch([7, 14, 21, 28], [7, 14, 28])
        assert result == 0, f"Test 150 failed: got {result}, expected {0}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = CanyonSearch([-2, -2, -2, -2, 0], [-3, -2, 2147483648])
        assert result == 0, f"Test 151 failed: got {result}, expected {0}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = CanyonSearch([-2, -2, -2, -2, 0, 11], [-3, -2, -1])
        assert result == 0, f"Test 152 failed: got {result}, expected {0}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = CanyonSearch([-2, -2, -2, 0], [-2, -1, 52])
        assert result == 0, f"Test 153 failed: got {result}, expected {0}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = CanyonSearch([0, 0, 0, 0], [1])
        assert result == 1, f"Test 154 failed: got {result}, expected {1}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = CanyonSearch([0, 0, 0, 0, 0], [1, 1])
        assert result == 1, f"Test 155 failed: got {result}, expected {1}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = CanyonSearch([0, 0, 0, 0, 0], [2147483648])
        assert result == 2147483648, f"Test 156 failed: got {result}, expected {2147483648}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = CanyonSearch([0, 0, 0, 0, 400], [2])
        assert result == 2, f"Test 157 failed: got {result}, expected {2}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = CanyonSearch([0, 0, 0, 0, 0, 0], [1])
        assert result == 1, f"Test 158 failed: got {result}, expected {1}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = CanyonSearch([0, 0, 0, 0, 40], [0, 1])
        assert result == 0, f"Test 159 failed: got {result}, expected {0}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = CanyonSearch([0, 0, 0, 0, 0], [1, 2])
        assert result == 1, f"Test 160 failed: got {result}, expected {1}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = CanyonSearch([0, 0, 0, 0, 0, 4], [-1])
        assert result == 1, f"Test 161 failed: got {result}, expected {1}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = CanyonSearch([0, 0, 0, 0, 0, 0], [0])
        assert result == 0, f"Test 162 failed: got {result}, expected {0}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = CanyonSearch([1, 1], [-1, 0, 2, 27])
        assert result == 1, f"Test 163 failed: got {result}, expected {1}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = CanyonSearch([-1, 0, 6, 1000000000000], [-1, 0, 1])
        assert result == 0, f"Test 164 failed: got {result}, expected {0}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = CanyonSearch([-1, 0, 1], [0, 1])
        assert result == 0, f"Test 165 failed: got {result}, expected {0}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = CanyonSearch([-1, 0, 1], [-1, 0, 1, 50])
        assert result == 0, f"Test 166 failed: got {result}, expected {0}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = CanyonSearch([100, 200, 300, 400, 500], [-1000, -500, 0, 500, 1000, 2147483646])
        assert result == 0, f"Test 167 failed: got {result}, expected {0}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = CanyonSearch([100, 200, 300, 500], [-1000, -500, 0, 1000])
        assert result == 100, f"Test 168 failed: got {result}, expected {100}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = CanyonSearch([-100, -50, -25, -6, -3, -1], [2, 4, 8, 16, 32])
        assert result == 3, f"Test 169 failed: got {result}, expected {3}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = CanyonSearch([-100, -50, -25, -12, -6, -3, -1, 0], [2, 4, 8, 16, 32])
        assert result == 2, f"Test 170 failed: got {result}, expected {2}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = CanyonSearch([-101, -50, -25, -12, -6, -3, -1], [2, 4, 8, 16, 31])
        assert result == 3, f"Test 171 failed: got {result}, expected {3}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = CanyonSearch([9, 18, 27, 35, 45, 54], [8, 17, 26, 35, 44, 53, 62])
        assert result == 0, f"Test 172 failed: got {result}, expected {0}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = CanyonSearch([0], [-2147483649, 0])
        assert result == 0, f"Test 173 failed: got {result}, expected {0}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = CanyonSearch([0, 18], [0, 0])
        assert result == 0, f"Test 174 failed: got {result}, expected {0}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = CanyonSearch([-20, 0], [1, 1])
        assert result == 1, f"Test 175 failed: got {result}, expected {1}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = CanyonSearch([-20, -8, 0], [1])
        assert result == 1, f"Test 176 failed: got {result}, expected {1}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = CanyonSearch([1], [40])
        assert result == 39, f"Test 177 failed: got {result}, expected {39}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = CanyonSearch([0, 0, 1], [0])
        assert result == 0, f"Test 178 failed: got {result}, expected {0}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = CanyonSearch([1, 1], [3])
        assert result == 2, f"Test 179 failed: got {result}, expected {2}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = CanyonSearch([-49, 1, 2], [2, 3])
        assert result == 0, f"Test 180 failed: got {result}, expected {0}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = CanyonSearch([2], [3, 4])
        assert result == 1, f"Test 181 failed: got {result}, expected {1}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = CanyonSearch([1, 2, 3], [0, 4, 2147483647])
        assert result == 1, f"Test 182 failed: got {result}, expected {1}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = CanyonSearch([1, 2, 3], [5])
        assert result == 2, f"Test 183 failed: got {result}, expected {2}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = CanyonSearch([1, 3], [4, 5])
        assert result == 1, f"Test 184 failed: got {result}, expected {1}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = CanyonSearch([2, 3], [1, 2, 3])
        assert result == 0, f"Test 185 failed: got {result}, expected {0}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = CanyonSearch([0], [9])
        assert result == 9, f"Test 186 failed: got {result}, expected {9}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
