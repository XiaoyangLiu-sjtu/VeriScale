# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def kthElement(arr, k):
2: ✓     return arr[k-1]
```

## Complete Test File

```python
def kthElement(arr, k):
    return arr[k-1]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = kthElement([10, 20, 30, 40, 50], 1)
        assert result == 10, f"Test 1 failed: got {result}, expected {10}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = kthElement([10, 20, 30, 40, 50], 3)
        assert result == 30, f"Test 2 failed: got {result}, expected {30}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = kthElement([10, 20, 30, 40, 50], 5)
        assert result == 50, f"Test 3 failed: got {result}, expected {50}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = kthElement([5], 1)
        assert result == 5, f"Test 4 failed: got {result}, expected {5}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = kthElement([1, 2, 3], 3)
        assert result == 3, f"Test 5 failed: got {result}, expected {3}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = kthElement([1, 2, 3], 2)
        assert result == 2, f"Test 6 failed: got {result}, expected {2}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = kthElement([9, 9, 9], 2)
        assert result == 9, f"Test 7 failed: got {result}, expected {9}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = kthElement([0, -1, -2], 1)
        assert result == 0, f"Test 8 failed: got {result}, expected {0}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = kthElement([0, -1, -2], 2)
        assert result == -1, f"Test 9 failed: got {result}, expected {-1}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = kthElement([0, -1, -2], 3)
        assert result == -2, f"Test 10 failed: got {result}, expected {-2}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = kthElement([10], 1)
        assert result == 10, f"Test 11 failed: got {result}, expected {10}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = kthElement([0], 1)
        assert result == 0, f"Test 12 failed: got {result}, expected {0}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = kthElement([-1], 1)
        assert result == -1, f"Test 13 failed: got {result}, expected {-1}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = kthElement([1, 2], 1)
        assert result == 1, f"Test 14 failed: got {result}, expected {1}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = kthElement([1, 2], 2)
        assert result == 2, f"Test 15 failed: got {result}, expected {2}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = kthElement([7, 7, 7], 2)
        assert result == 7, f"Test 16 failed: got {result}, expected {7}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = kthElement([3, 1, 4], 3)
        assert result == 4, f"Test 17 failed: got {result}, expected {4}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = kthElement([-5, 0, 5], 1)
        assert result == -5, f"Test 18 failed: got {result}, expected {-5}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = kthElement([-5, 0, 5], 2)
        assert result == 0, f"Test 19 failed: got {result}, expected {0}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = kthElement([-5, 0, 5], 3)
        assert result == 5, f"Test 20 failed: got {result}, expected {5}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = kthElement([10, 20, 30, 40], 4)
        assert result == 40, f"Test 21 failed: got {result}, expected {40}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = kthElement([10, 20, 30, 40], 1)
        assert result == 10, f"Test 22 failed: got {result}, expected {10}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = kthElement([10, 20, 30, 40], 2)
        assert result == 20, f"Test 23 failed: got {result}, expected {20}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = kthElement([10, 20, 30, 40], 3)
        assert result == 30, f"Test 24 failed: got {result}, expected {30}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = kthElement([9, 8, 7, 6, 5], 5)
        assert result == 5, f"Test 25 failed: got {result}, expected {5}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = kthElement([9, 8, 7, 6, 5], 4)
        assert result == 6, f"Test 26 failed: got {result}, expected {6}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = kthElement([100, -100, 200, -200, 300, -300], 6)
        assert result == -300, f"Test 27 failed: got {result}, expected {-300}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = kthElement([100, -100, 200, -200, 300, -300], 1)
        assert result == 100, f"Test 28 failed: got {result}, expected {100}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13], 7)
        assert result == 13, f"Test 29 failed: got {result}, expected {13}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13], 4)
        assert result == 3, f"Test 30 failed: got {result}, expected {3}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = kthElement([42, 0, -42, 84, -84, 168], 5)
        assert result == -84, f"Test 31 failed: got {result}, expected {-84}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = kthElement([2147483647, -2147483648, 0], 2)
        assert result == -2147483648, f"Test 32 failed: got {result}, expected {-2147483648}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = kthElement([999999999999, -999999999999], 2)
        assert result == -999999999999, f"Test 33 failed: got {result}, expected {-999999999999}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = kthElement([6, 5, 4, 3, 2, 1], 3)
        assert result == 4, f"Test 34 failed: got {result}, expected {4}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = kthElement([11, 22, 33, 44, 55, 66, 77, 88], 8)
        assert result == 88, f"Test 35 failed: got {result}, expected {88}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = kthElement([11, 22, 33, 44, 55, 66, 77, 88], 1)
        assert result == 11, f"Test 36 failed: got {result}, expected {11}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = kthElement([2, 4, 6, 8, 10, 12, 14, 16, 18], 9)
        assert result == 18, f"Test 37 failed: got {result}, expected {18}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = kthElement([2, 4, 6, 8, 10, 12, 14, 16, 18], 5)
        assert result == 10, f"Test 38 failed: got {result}, expected {10}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = kthElement([0, 0, 0, 0, 0], 3)
        assert result == 0, f"Test 39 failed: got {result}, expected {0}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = kthElement([-10, -20, -30, -40], 2)
        assert result == -20, f"Test 40 failed: got {result}, expected {-20}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = kthElement([1, 3, 3, 7, 9, 9, 9, 10], 6)
        assert result == 9, f"Test 41 failed: got {result}, expected {9}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = kthElement([123, -456, 789, -1011, 1213, -1415, 1617], 7)
        assert result == 1617, f"Test 42 failed: got {result}, expected {1617}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = kthElement([10, 30, 40, 50], 1)
        assert result == 10, f"Test 43 failed: got {result}, expected {10}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = kthElement([44, 20, 30, 40, 168], 1)
        assert result == 44, f"Test 44 failed: got {result}, expected {44}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = kthElement([100, 40, 30, 20, 10, 0], 2)
        assert result == 40, f"Test 45 failed: got {result}, expected {40}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = kthElement([10, 20, 30, 200, 50], 1)
        assert result == 10, f"Test 46 failed: got {result}, expected {10}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = kthElement([20, 40, 50, 0], 1)
        assert result == 20, f"Test 47 failed: got {result}, expected {20}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = kthElement([66, 50, 40, 30, 20, 10], 3)
        assert result == 40, f"Test 48 failed: got {result}, expected {40}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = kthElement([10, 20, 30, 40, 50], 2)
        assert result == 20, f"Test 49 failed: got {result}, expected {20}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = kthElement([10, 20, 30, 40, 50, 0], 2)
        assert result == 20, f"Test 50 failed: got {result}, expected {20}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = kthElement([50, 40, 30, 20], 3)
        assert result == 30, f"Test 51 failed: got {result}, expected {30}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = kthElement([10, 20, 41, 50, 0], 1)
        assert result == 10, f"Test 52 failed: got {result}, expected {10}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = kthElement([20, 30, 40, 50], 3)
        assert result == 40, f"Test 53 failed: got {result}, expected {40}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = kthElement([10, 20, 30, 50, 0, 0], 6)
        assert result == 0, f"Test 54 failed: got {result}, expected {0}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = kthElement([20, 20, 30, 40, 50, -999999999999, 0], 2)
        assert result == 20, f"Test 55 failed: got {result}, expected {20}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = kthElement([-50, 40, 30, 11], 3)
        assert result == 30, f"Test 56 failed: got {result}, expected {30}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = kthElement([10, 20, 30, 40, 50, 0], 3)
        assert result == 30, f"Test 57 failed: got {result}, expected {30}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = kthElement([10, 20, 30, 40, -2147483648, 0, 32, 0], 3)
        assert result == 30, f"Test 58 failed: got {result}, expected {30}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = kthElement([0, 50, 40, 30, 20, 10], 3)
        assert result == 40, f"Test 59 failed: got {result}, expected {40}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = kthElement([10, 20, 30, 40, 50], 4)
        assert result == 40, f"Test 60 failed: got {result}, expected {40}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = kthElement([50, 40, 30, 21, 10], 5)
        assert result == 10, f"Test 61 failed: got {result}, expected {10}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = kthElement([5, 0], 1)
        assert result == 5, f"Test 62 failed: got {result}, expected {5}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = kthElement([0, -20], 1)
        assert result == 0, f"Test 63 failed: got {result}, expected {0}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = kthElement([5, 0], 2)
        assert result == 0, f"Test 64 failed: got {result}, expected {0}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = kthElement([2], 1)
        assert result == 2, f"Test 65 failed: got {result}, expected {2}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = kthElement([0, 0], 1)
        assert result == 0, f"Test 66 failed: got {result}, expected {0}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = kthElement([1, 2, 3, 0, 30], 5)
        assert result == 30, f"Test 67 failed: got {result}, expected {30}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = kthElement([1, 2, 3, 39, 0, 0], 3)
        assert result == 3, f"Test 68 failed: got {result}, expected {3}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = kthElement([1, 2, 3, 999999999999], 3)
        assert result == 3, f"Test 69 failed: got {result}, expected {3}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = kthElement([3, 2, 1], 3)
        assert result == 1, f"Test 70 failed: got {result}, expected {1}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = kthElement([1, 0, 3], 2)
        assert result == 0, f"Test 71 failed: got {result}, expected {0}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = kthElement([2, 3], 2)
        assert result == 3, f"Test 72 failed: got {result}, expected {3}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = kthElement([1, 2, 3], 1)
        assert result == 1, f"Test 73 failed: got {result}, expected {1}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = kthElement([9, 9, 9], 1)
        assert result == 9, f"Test 74 failed: got {result}, expected {9}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = kthElement([9, 18, 9, 0, 0], 3)
        assert result == 9, f"Test 75 failed: got {result}, expected {9}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = kthElement([-999999999999, 9, 9], 1)
        assert result == -999999999999, f"Test 76 failed: got {result}, expected {-999999999999}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = kthElement([0, -1, -2, 0], 1)
        assert result == 0, f"Test 77 failed: got {result}, expected {0}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = kthElement([6, 0], 2)
        assert result == 0, f"Test 78 failed: got {result}, expected {0}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = kthElement([0, 1, 1617], 1)
        assert result == 0, f"Test 79 failed: got {result}, expected {0}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = kthElement([-2, 1, 0, 0], 1)
        assert result == -2, f"Test 80 failed: got {result}, expected {-2}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = kthElement([-1, 0], 2)
        assert result == 0, f"Test 81 failed: got {result}, expected {0}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = kthElement([-2, -1, 0], 1)
        assert result == -2, f"Test 82 failed: got {result}, expected {-2}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = kthElement([21, -1, -2], 1)
        assert result == 21, f"Test 83 failed: got {result}, expected {21}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = kthElement([0, -2, 16], 2)
        assert result == -2, f"Test 84 failed: got {result}, expected {-2}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = kthElement([0, -1, 0], 1)
        assert result == 0, f"Test 85 failed: got {result}, expected {0}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = kthElement([0, -1, -2, 0], 3)
        assert result == -2, f"Test 86 failed: got {result}, expected {-2}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = kthElement([0, -1, -2, 88, 8], 3)
        assert result == -2, f"Test 87 failed: got {result}, expected {-2}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = kthElement([3, 2, 1, 88], 4)
        assert result == 88, f"Test 88 failed: got {result}, expected {88}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = kthElement([10, 0, -300], 3)
        assert result == -300, f"Test 89 failed: got {result}, expected {-300}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = kthElement([10, 10], 1)
        assert result == 10, f"Test 90 failed: got {result}, expected {10}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = kthElement([10, 0], 1)
        assert result == 10, f"Test 91 failed: got {result}, expected {10}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = kthElement([-2], 1)
        assert result == -2, f"Test 92 failed: got {result}, expected {-2}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = kthElement([-1, 1, 0], 1)
        assert result == -1, f"Test 93 failed: got {result}, expected {-1}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = kthElement([41, 1, 2], 1)
        assert result == 41, f"Test 94 failed: got {result}, expected {41}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = kthElement([0, 0, 2, 1], 3)
        assert result == 2, f"Test 95 failed: got {result}, expected {2}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = kthElement([1, 1, -20, 0], 2)
        assert result == 1, f"Test 96 failed: got {result}, expected {1}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = kthElement([0, 2, 1], 2)
        assert result == 2, f"Test 97 failed: got {result}, expected {2}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = kthElement([1, 2, 33, 0], 2)
        assert result == 2, f"Test 98 failed: got {result}, expected {2}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = kthElement([6, 7], 2)
        assert result == 7, f"Test 99 failed: got {result}, expected {7}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = kthElement([-7, 7, 7], 2)
        assert result == 7, f"Test 100 failed: got {result}, expected {7}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = kthElement([7, 14, 7], 2)
        assert result == 14, f"Test 101 failed: got {result}, expected {14}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = kthElement([7, 7, 7, 14], 2)
        assert result == 7, f"Test 102 failed: got {result}, expected {7}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = kthElement([7, 7, 7, 0], 2)
        assert result == 7, f"Test 103 failed: got {result}, expected {7}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = kthElement([7, 7], 2)
        assert result == 7, f"Test 104 failed: got {result}, expected {7}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = kthElement([100, 1, 4], 3)
        assert result == 4, f"Test 105 failed: got {result}, expected {4}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = kthElement([3, 1, 4, -40], 3)
        assert result == 4, f"Test 106 failed: got {result}, expected {4}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = kthElement([4, 1, 4, 0], 2)
        assert result == 1, f"Test 107 failed: got {result}, expected {1}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = kthElement([4, 1, 3], 3)
        assert result == 3, f"Test 108 failed: got {result}, expected {3}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = kthElement([3, 4], 2)
        assert result == 4, f"Test 109 failed: got {result}, expected {4}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = kthElement([5, 0, -5], 2)
        assert result == 0, f"Test 110 failed: got {result}, expected {0}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = kthElement([40, 0, 5], 1)
        assert result == 40, f"Test 111 failed: got {result}, expected {40}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = kthElement([5, 0, -5], 3)
        assert result == -5, f"Test 112 failed: got {result}, expected {-5}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = kthElement([-5, 0, 5, 0], 2)
        assert result == 0, f"Test 113 failed: got {result}, expected {0}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = kthElement([0, 84, -4], 1)
        assert result == 0, f"Test 114 failed: got {result}, expected {0}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = kthElement([-5, 0, 5, 0], 1)
        assert result == -5, f"Test 115 failed: got {result}, expected {-5}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = kthElement([0, 5], 2)
        assert result == 5, f"Test 116 failed: got {result}, expected {5}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = kthElement([5, 0, 65], 1)
        assert result == 5, f"Test 117 failed: got {result}, expected {5}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = kthElement([-5, 0, 5, -1011], 4)
        assert result == -1011, f"Test 118 failed: got {result}, expected {-1011}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = kthElement([-5, 6, 5], 3)
        assert result == 5, f"Test 119 failed: got {result}, expected {5}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = kthElement([-5, 0, 5, 32], 2)
        assert result == 0, f"Test 120 failed: got {result}, expected {0}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = kthElement([10, 20, 30, 40, 0], 3)
        assert result == 30, f"Test 121 failed: got {result}, expected {30}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = kthElement([30, 20, 10, 0], 1)
        assert result == 30, f"Test 122 failed: got {result}, expected {30}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = kthElement([10, 20, 30, 40, 78], 1)
        assert result == 10, f"Test 123 failed: got {result}, expected {10}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = kthElement([40, 30, 20, 10], 1)
        assert result == 40, f"Test 124 failed: got {result}, expected {40}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = kthElement([10, 20, 30, 40, 0], 1)
        assert result == 10, f"Test 125 failed: got {result}, expected {10}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = kthElement([10, 20, 30, 40, 31, 0], 1)
        assert result == 10, f"Test 126 failed: got {result}, expected {10}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = kthElement([10, 20, 30, 40, 0], 2)
        assert result == 20, f"Test 127 failed: got {result}, expected {20}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = kthElement([9, 20, 30], 2)
        assert result == 20, f"Test 128 failed: got {result}, expected {20}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = kthElement([40, 30, 20, 10], 3)
        assert result == 20, f"Test 129 failed: got {result}, expected {20}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = kthElement([20, 30, 40], 3)
        assert result == 40, f"Test 130 failed: got {result}, expected {40}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = kthElement([0, -7, 5, 6, 7, 8, 9], 5)
        assert result == 7, f"Test 131 failed: got {result}, expected {7}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = kthElement([0, 5, 6, 7, 8, 9], 5)
        assert result == 8, f"Test 132 failed: got {result}, expected {8}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = kthElement([9, 8, 6, 6, 5, 789], 3)
        assert result == 6, f"Test 133 failed: got {result}, expected {6}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = kthElement([5, 6, 7, 8, 9], 2)
        assert result == 6, f"Test 134 failed: got {result}, expected {6}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = kthElement([9, 8, 7, 6, 5, -5, 0], 5)
        assert result == 5, f"Test 135 failed: got {result}, expected {5}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = kthElement([9, 8, 7, 6, 5, 44, 0], 5)
        assert result == 5, f"Test 136 failed: got {result}, expected {5}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = kthElement([9, 8, 7, 6, 5, 0], 1)
        assert result == 9, f"Test 137 failed: got {result}, expected {9}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = kthElement([5, 6, 10, 8, 9, -4], 3)
        assert result == 10, f"Test 138 failed: got {result}, expected {10}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = kthElement([100, -100, 200, -200, 300, 0], 6)
        assert result == 0, f"Test 139 failed: got {result}, expected {0}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = kthElement([100, -200, 200, -200, 300, -300, -5], 1)
        assert result == 100, f"Test 140 failed: got {result}, expected {100}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = kthElement([100, -100, 200, -200, 300, -300, -2], 1)
        assert result == 100, f"Test 141 failed: got {result}, expected {100}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = kthElement([100, -100, 200, -200, -300, -300], 2)
        assert result == -100, f"Test 142 failed: got {result}, expected {-100}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = kthElement([100, -100, 200, -200, 300, -300, 0, -456], 8)
        assert result == -456, f"Test 143 failed: got {result}, expected {-456}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = kthElement([-300, 300, -200, -100, 100], 1)
        assert result == -300, f"Test 144 failed: got {result}, expected {-300}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = kthElement([100, 0, 200, 300, -300], 1)
        assert result == 100, f"Test 145 failed: got {result}, expected {100}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = kthElement([100, -100, 200, -200, 300, -300, 200, 0], 1)
        assert result == 100, f"Test 146 failed: got {result}, expected {100}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = kthElement([100, -100, 200, -200, 300, -299], 2)
        assert result == -100, f"Test 147 failed: got {result}, expected {-100}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = kthElement([100, -200, 200, -200, 300, -300], 1)
        assert result == 100, f"Test 148 failed: got {result}, expected {100}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = kthElement([100, -100, 200, -200, -300], 1)
        assert result == 100, f"Test 149 failed: got {result}, expected {100}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = kthElement([100, -100, 200, -200, 300, -300], 5)
        assert result == 300, f"Test 150 failed: got {result}, expected {300}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = kthElement([1, 1, 2, 3, 5, 13, -300], 6)
        assert result == 13, f"Test 151 failed: got {result}, expected {13}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, 0, -456], 8)
        assert result == 0, f"Test 152 failed: got {result}, expected {0}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = kthElement([1, 1, 2, 3, 5, 102, -13, 301], 7)
        assert result == -13, f"Test 153 failed: got {result}, expected {-13}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, 0], 8)
        assert result == 0, f"Test 154 failed: got {result}, expected {0}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, 0], 7)
        assert result == 13, f"Test 155 failed: got {result}, expected {13}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = kthElement([1, 1, 3, -5, 8, 13, 67], 7)
        assert result == 67, f"Test 156 failed: got {result}, expected {67}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, 0], 4)
        assert result == 3, f"Test 157 failed: got {result}, expected {3}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13], 5)
        assert result == 5, f"Test 158 failed: got {result}, expected {5}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = kthElement([1, 1, 2, 3, 8, 13, 6], 5)
        assert result == 8, f"Test 159 failed: got {result}, expected {8}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, 0, 9], 1)
        assert result == 1, f"Test 160 failed: got {result}, expected {1}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = kthElement([13, 8, 5, 3, 2, 1, 1], 4)
        assert result == 3, f"Test 161 failed: got {result}, expected {3}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, -5], 4)
        assert result == 3, f"Test 162 failed: got {result}, expected {3}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = kthElement([13, 8, 5, 3, 1], 2)
        assert result == 8, f"Test 163 failed: got {result}, expected {8}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = kthElement([1, 1, 2, 3, 5, 8], 4)
        assert result == 3, f"Test 164 failed: got {result}, expected {3}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = kthElement([13, 8, 5, 2, 1, 1, 30], 3)
        assert result == 5, f"Test 165 failed: got {result}, expected {5}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = kthElement([168, -84, 84, -42, 0, 42], 6)
        assert result == 42, f"Test 166 failed: got {result}, expected {42}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = kthElement([42, 0, -42, 84, -84, 168, -50, 66], 5)
        assert result == -84, f"Test 167 failed: got {result}, expected {-84}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = kthElement([-84, 84, -42, 0, 42, 0, 0], 5)
        assert result == 42, f"Test 168 failed: got {result}, expected {42}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = kthElement([42, 0, -42, 84, -84, 168, 0], 5)
        assert result == -84, f"Test 169 failed: got {result}, expected {-84}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = kthElement([0, 168, -84, 84, -42, 0, 42], 6)
        assert result == 0, f"Test 170 failed: got {result}, expected {0}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = kthElement([42, 0, -42, 84, -84, 168, 0], 6)
        assert result == 168, f"Test 171 failed: got {result}, expected {168}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = kthElement([2147483647, -2147483648, 0], 3)
        assert result == 0, f"Test 172 failed: got {result}, expected {0}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = kthElement([2147483647, -2147483648, 0, 50, 0], 4)
        assert result == 50, f"Test 173 failed: got {result}, expected {50}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = kthElement([2147483647, 0, 0], 2)
        assert result == 0, f"Test 174 failed: got {result}, expected {0}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = kthElement([2147483647, 4, 0, 1617], 3)
        assert result == 0, f"Test 175 failed: got {result}, expected {0}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = kthElement([0, -999999999999], 2)
        assert result == -999999999999, f"Test 176 failed: got {result}, expected {-999999999999}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = kthElement([0, -999999999999, 999999999999], 2)
        assert result == -999999999999, f"Test 177 failed: got {result}, expected {-999999999999}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = kthElement([999999999999, -999999999999, 0, 2147483645], 2)
        assert result == -999999999999, f"Test 178 failed: got {result}, expected {-999999999999}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = kthElement([-999999999999, 999999999999], 2)
        assert result == 999999999999, f"Test 179 failed: got {result}, expected {999999999999}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = kthElement([0, 1213, 1, 2, 3, 4, 5, 6], 1)
        assert result == 0, f"Test 180 failed: got {result}, expected {0}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = kthElement([6, 5, 4, 3, 2, 1, 0], 5)
        assert result == 2, f"Test 181 failed: got {result}, expected {2}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = kthElement([6, 5, 4, 3, 2, 1], 6)
        assert result == 1, f"Test 182 failed: got {result}, expected {1}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = kthElement([6, 5, 4, 3, 2, 1, 0], 3)
        assert result == 4, f"Test 183 failed: got {result}, expected {4}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = kthElement([6, 5, 4, 3, 2, 1, 169], 3)
        assert result == 4, f"Test 184 failed: got {result}, expected {4}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = kthElement([6, 5, 4, 3, 2, 1, 0], 6)
        assert result == 1, f"Test 185 failed: got {result}, expected {1}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = kthElement([88, 77, 66, 54, 44, 33, 11, 11], 3)
        assert result == 66, f"Test 186 failed: got {result}, expected {66}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = kthElement([11, 22, 32, 44, 55, 66, 77, 88], 8)
        assert result == 88, f"Test 187 failed: got {result}, expected {88}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = kthElement([11, 22, 33, 44, 55, 66, 0, 88], 8)
        assert result == 88, f"Test 188 failed: got {result}, expected {88}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = kthElement([11, 22, 33, 44, 55, 66, 77, 88], 6)
        assert result == 66, f"Test 189 failed: got {result}, expected {66}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = kthElement([88, 77, 66, 55, -999999999999, 33, 22, 11], 8)
        assert result == 11, f"Test 190 failed: got {result}, expected {11}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = kthElement([11, 22, 33, 44, 55, 66, 77, 88, 0], 8)
        assert result == 88, f"Test 191 failed: got {result}, expected {88}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = kthElement([0, 88, 77, 66, 55, 44, 33, 22, 0, -1], 8)
        assert result == 22, f"Test 192 failed: got {result}, expected {22}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = kthElement([11, 33, 44, 55, 66, 77, 88, -42], 1)
        assert result == 11, f"Test 193 failed: got {result}, expected {11}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = kthElement([11, 23, 33, 43, 55, 66, 77, 88, 0], 2)
        assert result == 23, f"Test 194 failed: got {result}, expected {23}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = kthElement([88, 77, 66, 56, 44, 33, 22, 11], 1)
        assert result == 88, f"Test 195 failed: got {result}, expected {88}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = kthElement([11, 22, 44, 55, 66, 77, 88], 2)
        assert result == 22, f"Test 196 failed: got {result}, expected {22}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = kthElement([11, 22, 44, 55, 66, 77, 88], 1)
        assert result == 11, f"Test 197 failed: got {result}, expected {11}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = kthElement([18, 16, 14, 12, 10, 8, 6, 5, 2], 9)
        assert result == 2, f"Test 198 failed: got {result}, expected {2}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = kthElement([2, 4, 6, 8, 10, 12, 14, 16, 18], 8)
        assert result == 16, f"Test 199 failed: got {result}, expected {16}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = kthElement([0, 57, 0, 18, 16, 14, 12, 10, 8, 6, 4, 2, 56], 9)
        assert result == 8, f"Test 200 failed: got {result}, expected {8}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = kthElement([18, 16, 14, 12, 10, 8, 6, 4, 2], 8)
        assert result == 4, f"Test 201 failed: got {result}, expected {4}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = kthElement([123, 18, 16, 28, 12, 10, 8, 2147483645, 4, 2], 8)
        assert result == 2147483645, f"Test 202 failed: got {result}, expected {2147483645}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = kthElement([2, 4, 6, 8, 10, 12, 16, 18, 0], 9)
        assert result == 0, f"Test 203 failed: got {result}, expected {0}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = kthElement([-18, 16, 14, 12, 10, 8, 6, 4, 2], 9)
        assert result == 2, f"Test 204 failed: got {result}, expected {2}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = kthElement([2, 4, 6, 8, 10, 12, 14, 16, 18], 3)
        assert result == 6, f"Test 205 failed: got {result}, expected {6}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = kthElement([2, 4, 6, 8, 10, 12, 14, 16, 18, 30], 2)
        assert result == 4, f"Test 206 failed: got {result}, expected {4}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = kthElement([2, 4, 6, 8, 10, 12, 14, 16, 18], 6)
        assert result == 12, f"Test 207 failed: got {result}, expected {12}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = kthElement([2, 4, 8, 10, 12, 14, 16, 18], 8)
        assert result == 18, f"Test 208 failed: got {result}, expected {18}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = kthElement([0, 0, 0, 0, 0, 16], 3)
        assert result == 0, f"Test 209 failed: got {result}, expected {0}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = kthElement([0, 0, 0, 0, 10], 3)
        assert result == 0, f"Test 210 failed: got {result}, expected {0}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = kthElement([0, 13, 0, 0, 0, 0, 0], 3)
        assert result == 0, f"Test 211 failed: got {result}, expected {0}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = kthElement([0, 0, 0, 0, 29], 3)
        assert result == 0, f"Test 212 failed: got {result}, expected {0}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = kthElement([0, 0, 0, -1, 1, 0, 44, 0], 3)
        assert result == 0, f"Test 213 failed: got {result}, expected {0}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = kthElement([0, 0, 0, 0], 3)
        assert result == 0, f"Test 214 failed: got {result}, expected {0}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = kthElement([-1, 0, 0, 0, 0, 0], 6)
        assert result == 0, f"Test 215 failed: got {result}, expected {0}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = kthElement([-10, -20, -30, -40, -301], 2)
        assert result == -20, f"Test 216 failed: got {result}, expected {-20}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = kthElement([-10, -20, -40], 2)
        assert result == -20, f"Test 217 failed: got {result}, expected {-20}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = kthElement([-30, -20, -10, -100], 1)
        assert result == -30, f"Test 218 failed: got {result}, expected {-30}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = kthElement([-10, -20, -30, -40], 4)
        assert result == -40, f"Test 219 failed: got {result}, expected {-40}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = kthElement([-10, -20, -30, 15], 4)
        assert result == 15, f"Test 220 failed: got {result}, expected {15}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = kthElement([1, 3, 3, 7, 9, 9, 9, 10, 40], 6)
        assert result == 9, f"Test 221 failed: got {result}, expected {9}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = kthElement([123, -456, -789, -1011, 1213, 1617], 6)
        assert result == 1617, f"Test 222 failed: got {result}, expected {1617}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = kthElement([-11, 123, -456, 789, -1011, 1213, -1415, 1617, 0], 7)
        assert result == -1415, f"Test 223 failed: got {result}, expected {-1415}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = kthElement([1, 2, 3, 0], 4)
        assert result == 0, f"Test 224 failed: got {result}, expected {0}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = kthElement([5, -2], 1)
        assert result == 5, f"Test 225 failed: got {result}, expected {5}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = kthElement([6], 1)
        assert result == 6, f"Test 226 failed: got {result}, expected {6}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = kthElement([0, 0, 0], 1)
        assert result == 0, f"Test 227 failed: got {result}, expected {0}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = kthElement([49], 1)
        assert result == 49, f"Test 228 failed: got {result}, expected {49}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = kthElement([1], 1)
        assert result == 1, f"Test 229 failed: got {result}, expected {1}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = kthElement([0, 43, 999999999999], 3)
        assert result == 999999999999, f"Test 230 failed: got {result}, expected {999999999999}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = kthElement([0, 28, -7], 1)
        assert result == 0, f"Test 231 failed: got {result}, expected {0}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = kthElement([10, 20, 101, 0], 3)
        assert result == 101, f"Test 232 failed: got {result}, expected {101}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = kthElement([10, 20, 54], 3)
        assert result == 54, f"Test 233 failed: got {result}, expected {54}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = kthElement([-4, -3, -2, -1], 4)
        assert result == -1, f"Test 234 failed: got {result}, expected {-1}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = kthElement([-1, -2, -3, -4], 2)
        assert result == -2, f"Test 235 failed: got {result}, expected {-2}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
