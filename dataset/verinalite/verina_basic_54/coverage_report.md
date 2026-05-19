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
        result = CanyonSearch([1, 2, 3], [4, 5, 6])
        assert result == 1, f"Test 6 failed: got {result}, expected {1}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = CanyonSearch([4, 5, 6], [1, 2, 3])
        assert result == 1, f"Test 7 failed: got {result}, expected {1}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = CanyonSearch([-1000, -500, -100], [100, 500, 1000])
        assert result == 200, f"Test 8 failed: got {result}, expected {200}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = CanyonSearch([0, 5, 10, 15], [6])
        assert result == 1, f"Test 9 failed: got {result}, expected {1}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = CanyonSearch([6], [0, 5, 10, 15])
        assert result == 1, f"Test 10 failed: got {result}, expected {1}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = CanyonSearch([-1000000000000, 0, 1000000000000], [-999999999999, 2])
        assert result == 1, f"Test 11 failed: got {result}, expected {1}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = CanyonSearch([-2147483648, -1, 0, 1, 2147483647], [2147483646])
        assert result == 1, f"Test 12 failed: got {result}, expected {1}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = CanyonSearch([-9, -4, 2, 2, 2, 11], [-10, -4, 3, 12])
        assert result == 0, f"Test 13 failed: got {result}, expected {0}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = CanyonSearch([42], [1, 2, 3, 40, 41, 43, 44])
        assert result == 1, f"Test 14 failed: got {result}, expected {1}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = CanyonSearch([100, 200, 300, 400, 500], [-1000, -500, 0, 500, 1000])
        assert result == 0, f"Test 15 failed: got {result}, expected {0}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = CanyonSearch([-100, -50, -25, -12, -6, -3, -1], [2, 4, 8, 16, 32])
        assert result == 3, f"Test 16 failed: got {result}, expected {3}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = CanyonSearch([1, 3, 5], [-2, 4, 6, 14])
        assert result == 1, f"Test 17 failed: got {result}, expected {1}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = CanyonSearch([-5, 0], [1, 3])
        assert result == 1, f"Test 18 failed: got {result}, expected {1}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = CanyonSearch([-5, -2, 0, 0], [1, 3])
        assert result == 1, f"Test 19 failed: got {result}, expected {1}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = CanyonSearch([1, 2, 3, 4, 5], [3, 400])
        assert result == 0, f"Test 20 failed: got {result}, expected {0}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = CanyonSearch([-10, -5, 0, 5, 10], [-3, 2, 8, 8])
        assert result == 2, f"Test 21 failed: got {result}, expected {2}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = CanyonSearch([-10, -5, 0, 5, 10, 25], [-3, 2, 8])
        assert result == 2, f"Test 22 failed: got {result}, expected {2}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = CanyonSearch([-10, -5, 0, 5, 10, 12], [-3, 2, 8])
        assert result == 2, f"Test 23 failed: got {result}, expected {2}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = CanyonSearch([-10, -5, 0, 5], [-3, 2, 8])
        assert result == 2, f"Test 24 failed: got {result}, expected {2}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = CanyonSearch([0, 44], [13])
        assert result == 13, f"Test 25 failed: got {result}, expected {13}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = CanyonSearch([-1, 0], [1, 2147483646])
        assert result == 1, f"Test 26 failed: got {result}, expected {1}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = CanyonSearch([1, 2, 3], [4, 4, 6])
        assert result == 1, f"Test 27 failed: got {result}, expected {1}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = CanyonSearch([1, 2, 3, 36, 400], [4, 6])
        assert result == 1, f"Test 28 failed: got {result}, expected {1}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = CanyonSearch([-1, 3], [0, 5, 6])
        assert result == 1, f"Test 29 failed: got {result}, expected {1}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = CanyonSearch([3, 5, 6], [1, 2, 3, 18])
        assert result == 0, f"Test 30 failed: got {result}, expected {0}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = CanyonSearch([4], [2, 2, 3])
        assert result == 1, f"Test 31 failed: got {result}, expected {1}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = CanyonSearch([0, 5, 6], [1, 2, 3])
        assert result == 1, f"Test 32 failed: got {result}, expected {1}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = CanyonSearch([4, 5], [1, 2, 3])
        assert result == 1, f"Test 33 failed: got {result}, expected {1}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = CanyonSearch([-5, -3, -1], [-4, -2, 0, 5])
        assert result == 1, f"Test 34 failed: got {result}, expected {1}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = CanyonSearch([1, 1, 2, 2, 3, 3], [-2147483648, 4])
        assert result == 1, f"Test 35 failed: got {result}, expected {1}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = CanyonSearch([1, 1, 2, 2, 3, 3], [2, 4])
        assert result == 0, f"Test 36 failed: got {result}, expected {0}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = CanyonSearch([-100, 0, 100], [-50, -2])
        assert result == 2, f"Test 37 failed: got {result}, expected {2}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = CanyonSearch([-1000, -500, 0], [100, 500, 1000])
        assert result == 100, f"Test 38 failed: got {result}, expected {100}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = CanyonSearch([-1000, -500, -100, 0], [54, 500, 1000])
        assert result == 54, f"Test 39 failed: got {result}, expected {54}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = CanyonSearch([-8, -6, -4], [-7, -5, -3, -1, 300])
        assert result == 1, f"Test 40 failed: got {result}, expected {1}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = CanyonSearch([-8, -6, -2], [-7, -5, -3, -1, 0, 0, 0, 0])
        assert result == 1, f"Test 41 failed: got {result}, expected {1}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = CanyonSearch([0, 5, 10, 15, 44], [6])
        assert result == 1, f"Test 42 failed: got {result}, expected {1}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = CanyonSearch([0, 5, 10, 15], [6, 14])
        assert result == 1, f"Test 43 failed: got {result}, expected {1}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = CanyonSearch([0, 5, 10, 14], [100])
        assert result == 86, f"Test 44 failed: got {result}, expected {86}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = CanyonSearch([6], [1, 5, 10, 15])
        assert result == 1, f"Test 45 failed: got {result}, expected {1}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = CanyonSearch([3], [-3, -3, 0, 4, 50])
        assert result == 1, f"Test 46 failed: got {result}, expected {1}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = CanyonSearch([0, 1000000000000], [-999999999999, 2])
        assert result == 2, f"Test 47 failed: got {result}, expected {2}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = CanyonSearch([0, 1000000000000], [-999999999999, -2, 6])
        assert result == 2, f"Test 48 failed: got {result}, expected {2}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = CanyonSearch([400, 2147483647], [-2147483648, 0, 0])
        assert result == 400, f"Test 49 failed: got {result}, expected {400}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = CanyonSearch([100, 200, 300, 500], [-1000, -500, 0, 1000])
        assert result == 100, f"Test 50 failed: got {result}, expected {100}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = CanyonSearch([-100, -50, -25, -6, -3, -1], [2, 4, 8, 16, 32])
        assert result == 3, f"Test 51 failed: got {result}, expected {3}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = CanyonSearch([-100, -50, -25, -12, -6, -3, -1, 0], [2, 4, 8, 16, 32])
        assert result == 2, f"Test 52 failed: got {result}, expected {2}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = CanyonSearch([-101, -50, -25, -12, -6, -3, -1], [2, 4, 8, 16, 31])
        assert result == 3, f"Test 53 failed: got {result}, expected {3}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = CanyonSearch([1, 3], [4, 5])
        assert result == 1, f"Test 54 failed: got {result}, expected {1}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
