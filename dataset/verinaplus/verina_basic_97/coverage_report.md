# Coverage Report

Total executable lines: 3
Covered lines: 3
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def TestArrayElements(a, j):
2: ✓     a[j] = 60
3: ✓     return a
```

## Complete Test File

```python
def TestArrayElements(a, j):
    a[j] = 60
    return a

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = TestArrayElements([1, 2, 3, 4, 5], 2)
        assert result == [1, 2, 60, 4, 5], f"Test 1 failed: got {result}, expected {[1, 2, 60, 4, 5]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = TestArrayElements([60, 30, 20], 1)
        assert result == [60, 60, 20], f"Test 2 failed: got {result}, expected {[60, 60, 20]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = TestArrayElements([10, 20, 30], 0)
        assert result == [60, 20, 30], f"Test 3 failed: got {result}, expected {[60, 20, 30]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = TestArrayElements([5, 10, 15], 2)
        assert result == [5, 10, 60], f"Test 4 failed: got {result}, expected {[5, 10, 60]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = TestArrayElements([0], 0)
        assert result == [60], f"Test 5 failed: got {result}, expected {[60]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = TestArrayElements([1], 0)
        assert result == [60], f"Test 6 failed: got {result}, expected {[60]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = TestArrayElements([60], 0)
        assert result == [60], f"Test 7 failed: got {result}, expected {[60]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = TestArrayElements([-1], 0)
        assert result == [60], f"Test 8 failed: got {result}, expected {[60]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = TestArrayElements([1, 2], 0)
        assert result == [60, 2], f"Test 9 failed: got {result}, expected {[60, 2]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = TestArrayElements([1, 2], 1)
        assert result == [1, 60], f"Test 10 failed: got {result}, expected {[1, 60]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = TestArrayElements([60, 2], 0)
        assert result == [60, 2], f"Test 11 failed: got {result}, expected {[60, 2]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = TestArrayElements([1, 60], 1)
        assert result == [1, 60], f"Test 12 failed: got {result}, expected {[1, 60]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = TestArrayElements([-5, -10], 1)
        assert result == [-5, 60], f"Test 13 failed: got {result}, expected {[-5, 60]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = TestArrayElements([3, 3, 3], 2)
        assert result == [3, 3, 60], f"Test 14 failed: got {result}, expected {[3, 3, 60]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = TestArrayElements([10, 20, 30], 1)
        assert result == [10, 60, 30], f"Test 15 failed: got {result}, expected {[10, 60, 30]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = TestArrayElements([10, 20, 30], 2)
        assert result == [10, 20, 60], f"Test 16 failed: got {result}, expected {[10, 20, 60]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = TestArrayElements([5, 10, 15, 20], 3)
        assert result == [5, 10, 15, 60], f"Test 17 failed: got {result}, expected {[5, 10, 15, 60]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = TestArrayElements([5, 10, 15, 20], 2)
        assert result == [5, 10, 60, 20], f"Test 18 failed: got {result}, expected {[5, 10, 60, 20]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = TestArrayElements([100, 200, 300, 400, 500], 4)
        assert result == [100, 200, 300, 400, 60], f"Test 19 failed: got {result}, expected {[100, 200, 300, 400, 60]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = TestArrayElements([100, 200, 300, 400, 500], 0)
        assert result == [60, 200, 300, 400, 500], f"Test 20 failed: got {result}, expected {[60, 200, 300, 400, 500]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = TestArrayElements([9, 8, 7, 6, 5], 1)
        assert result == [9, 60, 7, 6, 5], f"Test 21 failed: got {result}, expected {[9, 60, 7, 6, 5]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = TestArrayElements([0, 0, 0, 0, 0, 0], 5)
        assert result == [0, 0, 0, 0, 0, 60], f"Test 22 failed: got {result}, expected {[0, 0, 0, 0, 0, 60]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = TestArrayElements([1, -1, 1, -1, 1, -1], 4)
        assert result == [1, -1, 1, -1, 60, -1], f"Test 23 failed: got {result}, expected {[1, -1, 1, -1, 60, -1]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = TestArrayElements([2147483647, -2147483648], 1)
        assert result == [2147483647, 60], f"Test 24 failed: got {result}, expected {[2147483647, 60]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = TestArrayElements([42, 60, 42], 1)
        assert result == [42, 60, 42], f"Test 25 failed: got {result}, expected {[42, 60, 42]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = TestArrayElements([42, 60, 42], 0)
        assert result == [60, 60, 42], f"Test 26 failed: got {result}, expected {[60, 60, 42]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = TestArrayElements([42, 60, 42], 2)
        assert result == [42, 60, 60], f"Test 27 failed: got {result}, expected {[42, 60, 60]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 66, 77], 6)
        assert result == [11, 22, 33, 44, 55, 66, 60], f"Test 28 failed: got {result}, expected {[11, 22, 33, 44, 55, 66, 60]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 66, 77], 3)
        assert result == [11, 22, 33, 60, 55, 66, 77], f"Test 29 failed: got {result}, expected {[11, 22, 33, 60, 55, 66, 77]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = TestArrayElements([7, 14, 21, 28, 35, 42, 49, 56], 7)
        assert result == [7, 14, 21, 28, 35, 42, 49, 60], f"Test 30 failed: got {result}, expected {[7, 14, 21, 28, 35, 42, 49, 60]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = TestArrayElements([7, 14, 21, 28, 35, 42, 49, 56], 0)
        assert result == [60, 14, 21, 28, 35, 42, 49, 56], f"Test 31 failed: got {result}, expected {[60, 14, 21, 28, 35, 42, 49, 56]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = TestArrayElements([99, 98, 97, 96, 95, 94, 93, 92, 91], 8)
        assert result == [99, 98, 97, 96, 95, 94, 93, 92, 60], f"Test 32 failed: got {result}, expected {[99, 98, 97, 96, 95, 94, 93, 92, 60]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = TestArrayElements([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 9)
        assert result == [2, 4, 6, 8, 10, 12, 14, 16, 18, 60], f"Test 33 failed: got {result}, expected {[2, 4, 6, 8, 10, 12, 14, 16, 18, 60]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = TestArrayElements([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 5)
        assert result == [2, 4, 6, 8, 10, 60, 14, 16, 18, 20], f"Test 34 failed: got {result}, expected {[2, 4, 6, 8, 10, 60, 14, 16, 18, 20]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = TestArrayElements([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 10)
        assert result == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 60], f"Test 35 failed: got {result}, expected {[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 60]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = TestArrayElements([1, 3, 4, 5], 2)
        assert result == [1, 3, 60, 5], f"Test 36 failed: got {result}, expected {[1, 3, 60, 5]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = TestArrayElements([55, 2, 3, 4, 35], 2)
        assert result == [55, 2, 60, 4, 35], f"Test 37 failed: got {result}, expected {[55, 2, 60, 4, 35]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = TestArrayElements([0, 0, 5, 4, 3, 2, 1], 0)
        assert result == [60, 0, 5, 4, 3, 2, 1], f"Test 38 failed: got {result}, expected {[60, 0, 5, 4, 3, 2, 1]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = TestArrayElements([1, 2, 3, 92, 5], 2)
        assert result == [1, 2, 60, 92, 5], f"Test 39 failed: got {result}, expected {[1, 2, 60, 92, 5]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = TestArrayElements([2, 4, 5, 0], 2)
        assert result == [2, 4, 60, 0], f"Test 40 failed: got {result}, expected {[2, 4, 60, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = TestArrayElements([92, 5, 4, 3, 2, 1], 3)
        assert result == [92, 5, 4, 60, 2, 1], f"Test 41 failed: got {result}, expected {[92, 5, 4, 60, 2, 1]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = TestArrayElements([1, 2, 3, 4, 5], 3)
        assert result == [1, 2, 3, 60, 5], f"Test 42 failed: got {result}, expected {[1, 2, 3, 60, 5]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = TestArrayElements([1, 2, 3, 4, 5], 0)
        assert result == [60, 2, 3, 4, 5], f"Test 43 failed: got {result}, expected {[60, 2, 3, 4, 5]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = TestArrayElements([1, 2, 3, 4, 5, 0], 3)
        assert result == [1, 2, 3, 60, 5, 0], f"Test 44 failed: got {result}, expected {[1, 2, 3, 60, 5, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = TestArrayElements([20, 30], 1)
        assert result == [20, 60], f"Test 45 failed: got {result}, expected {[20, 60]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = TestArrayElements([60, 66, 0], 0)
        assert result == [60, 66, 0], f"Test 46 failed: got {result}, expected {[60, 66, 0]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = TestArrayElements([60, 15, -20], 1)
        assert result == [60, 60, -20], f"Test 47 failed: got {result}, expected {[60, 60, -20]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = TestArrayElements([120, 30, 20, 11, 0], 0)
        assert result == [60, 30, 20, 11, 0], f"Test 48 failed: got {result}, expected {[60, 30, 20, 11, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = TestArrayElements([-20, 61], 1)
        assert result == [-20, 60], f"Test 49 failed: got {result}, expected {[-20, 60]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = TestArrayElements([60, 30, 20, 0, 4], 1)
        assert result == [60, 60, 20, 0, 4], f"Test 50 failed: got {result}, expected {[60, 60, 20, 0, 4]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = TestArrayElements([0, 0, 0, 33, 20, 30, 60], 1)
        assert result == [0, 60, 0, 33, 20, 30, 60], f"Test 51 failed: got {result}, expected {[0, 60, 0, 33, 20, 30, 60]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = TestArrayElements([30, 20, 0], 0)
        assert result == [60, 20, 0], f"Test 52 failed: got {result}, expected {[60, 20, 0]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = TestArrayElements([10, 0, 30, 120], 0)
        assert result == [60, 0, 30, 120], f"Test 53 failed: got {result}, expected {[60, 0, 30, 120]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = TestArrayElements([30, 20, 10, 97], 0)
        assert result == [60, 20, 10, 97], f"Test 54 failed: got {result}, expected {[60, 20, 10, 97]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = TestArrayElements([10, 20, 21], 1)
        assert result == [10, 60, 21], f"Test 55 failed: got {result}, expected {[10, 60, 21]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = TestArrayElements([10, 400, 29], 1)
        assert result == [10, 60, 29], f"Test 56 failed: got {result}, expected {[10, 60, 29]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = TestArrayElements([20, 0], 0)
        assert result == [60, 0], f"Test 57 failed: got {result}, expected {[60, 0]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = TestArrayElements([10, 19, 30], 0)
        assert result == [60, 19, 30], f"Test 58 failed: got {result}, expected {[60, 19, 30]}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = TestArrayElements([10, 30], 0)
        assert result == [60, 30], f"Test 59 failed: got {result}, expected {[60, 30]}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = TestArrayElements([9, 15, 10, 5, 4], 2)
        assert result == [9, 15, 60, 5, 4], f"Test 60 failed: got {result}, expected {[9, 15, 60, 5, 4]}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = TestArrayElements([5, 10, 15, 0], 0)
        assert result == [60, 10, 15, 0], f"Test 61 failed: got {result}, expected {[60, 10, 15, 0]}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = TestArrayElements([0, 5, 10, 35], 2)
        assert result == [0, 5, 60, 35], f"Test 62 failed: got {result}, expected {[0, 5, 60, 35]}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = TestArrayElements([5, 10, 15, 11], 2)
        assert result == [5, 10, 60, 11], f"Test 63 failed: got {result}, expected {[5, 10, 60, 11]}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = TestArrayElements([5, 10, 15, 8], 2)
        assert result == [5, 10, 60, 8], f"Test 64 failed: got {result}, expected {[5, 10, 60, 8]}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = TestArrayElements([15, 10, 5, 0], 0)
        assert result == [60, 10, 5, 0], f"Test 65 failed: got {result}, expected {[60, 10, 5, 0]}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = TestArrayElements([0, 0], 0)
        assert result == [60, 0], f"Test 66 failed: got {result}, expected {[60, 0]}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = TestArrayElements([0, 99], 0)
        assert result == [60, 99], f"Test 67 failed: got {result}, expected {[60, 99]}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = TestArrayElements([0, 400], 0)
        assert result == [60, 400], f"Test 68 failed: got {result}, expected {[60, 400]}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = TestArrayElements([0, -2147483648], 0)
        assert result == [60, -2147483648], f"Test 69 failed: got {result}, expected {[60, -2147483648]}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = TestArrayElements([-20, 4, 3, 2, 1, 300], 0)
        assert result == [60, 4, 3, 2, 1, 300], f"Test 70 failed: got {result}, expected {[60, 4, 3, 2, 1, 300]}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = TestArrayElements([1, 2, 3, 4], 0)
        assert result == [60, 2, 3, 4], f"Test 71 failed: got {result}, expected {[60, 2, 3, 4]}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = TestArrayElements([1, 2, 3, 8, 0], 0)
        assert result == [60, 2, 3, 8, 0], f"Test 72 failed: got {result}, expected {[60, 2, 3, 8, 0]}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = TestArrayElements([1, 2, 3, -4], 0)
        assert result == [60, 2, 3, -4], f"Test 73 failed: got {result}, expected {[60, 2, 3, -4]}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = TestArrayElements([1, 0, 0], 0)
        assert result == [60, 0, 0], f"Test 74 failed: got {result}, expected {[60, 0, 0]}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = TestArrayElements([95, 1], 0)
        assert result == [60, 1], f"Test 75 failed: got {result}, expected {[60, 1]}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = TestArrayElements([1, 0, 2], 0)
        assert result == [60, 0, 2], f"Test 76 failed: got {result}, expected {[60, 0, 2]}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = TestArrayElements([1, 200], 0)
        assert result == [60, 200], f"Test 77 failed: got {result}, expected {[60, 200]}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = TestArrayElements([-8, 0, 55], 1)
        assert result == [-8, 60, 55], f"Test 78 failed: got {result}, expected {[-8, 60, 55]}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = TestArrayElements([2, 0, 0], 1)
        assert result == [2, 60, 0], f"Test 79 failed: got {result}, expected {[2, 60, 0]}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = TestArrayElements([0, 1], 0)
        assert result == [60, 1], f"Test 80 failed: got {result}, expected {[60, 1]}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = TestArrayElements([120], 0)
        assert result == [60], f"Test 81 failed: got {result}, expected {[60]}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = TestArrayElements([60, 0], 0)
        assert result == [60, 0], f"Test 82 failed: got {result}, expected {[60, 0]}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = TestArrayElements([-60], 0)
        assert result == [60], f"Test 83 failed: got {result}, expected {[60]}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = TestArrayElements([-60, 0], 0)
        assert result == [60, 0], f"Test 84 failed: got {result}, expected {[60, 0]}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = TestArrayElements([60, 0, 0], 0)
        assert result == [60, 0, 0], f"Test 85 failed: got {result}, expected {[60, 0, 0]}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = TestArrayElements([21, 0], 1)
        assert result == [21, 60], f"Test 86 failed: got {result}, expected {[21, 60]}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = TestArrayElements([-1, 0, 0], 0)
        assert result == [60, 0, 0], f"Test 87 failed: got {result}, expected {[60, 0, 0]}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = TestArrayElements([-1, -20], 0)
        assert result == [60, -20], f"Test 88 failed: got {result}, expected {[60, -20]}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = TestArrayElements([-1, 0], 0)
        assert result == [60, 0], f"Test 89 failed: got {result}, expected {[60, 0]}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = TestArrayElements([-1, 240], 0)
        assert result == [60, 240], f"Test 90 failed: got {result}, expected {[60, 240]}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = TestArrayElements([-4, 1], 1)
        assert result == [-4, 60], f"Test 91 failed: got {result}, expected {[-4, 60]}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = TestArrayElements([2, 1], 1)
        assert result == [2, 60], f"Test 92 failed: got {result}, expected {[2, 60]}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = TestArrayElements([2, 1], 0)
        assert result == [60, 1], f"Test 93 failed: got {result}, expected {[60, 1]}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = TestArrayElements([0, 2, 1, 0], 1)
        assert result == [0, 60, 1, 0], f"Test 94 failed: got {result}, expected {[0, 60, 1, 0]}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = TestArrayElements([1, 2, 42], 0)
        assert result == [60, 2, 42], f"Test 95 failed: got {result}, expected {[60, 2, 42]}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = TestArrayElements([1, 4], 0)
        assert result == [60, 4], f"Test 96 failed: got {result}, expected {[60, 4]}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = TestArrayElements([1, 2, 0, 2], 1)
        assert result == [1, 60, 0, 2], f"Test 97 failed: got {result}, expected {[1, 60, 0, 2]}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = TestArrayElements([60, 2, -1, 0], 0)
        assert result == [60, 2, -1, 0], f"Test 98 failed: got {result}, expected {[60, 2, -1, 0]}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = TestArrayElements([60, 2, 6], 0)
        assert result == [60, 2, 6], f"Test 99 failed: got {result}, expected {[60, 2, 6]}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = TestArrayElements([60, 2, 0, 0], 3)
        assert result == [60, 2, 0, 60], f"Test 100 failed: got {result}, expected {[60, 2, 0, 60]}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = TestArrayElements([2, 60], 0)
        assert result == [60, 60], f"Test 101 failed: got {result}, expected {[60, 60]}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = TestArrayElements([2, 60, 10], 1)
        assert result == [2, 60, 10], f"Test 102 failed: got {result}, expected {[2, 60, 10]}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = TestArrayElements([60, 2, 0], 0)
        assert result == [60, 2, 0], f"Test 103 failed: got {result}, expected {[60, 2, 0]}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = TestArrayElements([60, 94], 0)
        assert result == [60, 94], f"Test 104 failed: got {result}, expected {[60, 94]}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = TestArrayElements([60, 1], 0)
        assert result == [60, 1], f"Test 105 failed: got {result}, expected {[60, 1]}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = TestArrayElements([1, 60, 0], 1)
        assert result == [1, 60, 0], f"Test 106 failed: got {result}, expected {[1, 60, 0]}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = TestArrayElements([1, 60], 0)
        assert result == [60, 60], f"Test 107 failed: got {result}, expected {[60, 60]}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = TestArrayElements([1, 0], 0)
        assert result == [60, 0], f"Test 108 failed: got {result}, expected {[60, 0]}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = TestArrayElements([28, 60], 1)
        assert result == [28, 60], f"Test 109 failed: got {result}, expected {[28, 60]}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = TestArrayElements([60, 1, 0], 1)
        assert result == [60, 60, 0], f"Test 110 failed: got {result}, expected {[60, 60, 0]}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = TestArrayElements([1, 60, 0, 2], 0)
        assert result == [60, 60, 0, 2], f"Test 111 failed: got {result}, expected {[60, 60, 0, 2]}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = TestArrayElements([-6, -10], 1)
        assert result == [-6, 60], f"Test 112 failed: got {result}, expected {[-6, 60]}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = TestArrayElements([-5, -10, 1, 0], 1)
        assert result == [-5, 60, 1, 0], f"Test 113 failed: got {result}, expected {[-5, 60, 1, 0]}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = TestArrayElements([0, -11, 56], 0)
        assert result == [60, -11, 56], f"Test 114 failed: got {result}, expected {[60, -11, 56]}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = TestArrayElements([-5, -10], 0)
        assert result == [60, -10], f"Test 115 failed: got {result}, expected {[60, -10]}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = TestArrayElements([56, 3, 3, 3], 3)
        assert result == [56, 3, 3, 60], f"Test 116 failed: got {result}, expected {[56, 3, 3, 60]}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = TestArrayElements([0, 0, 3, 3, 3], 4)
        assert result == [0, 0, 3, 3, 60], f"Test 117 failed: got {result}, expected {[0, 0, 3, 3, 60]}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = TestArrayElements([3, 3, 3], 0)
        assert result == [60, 3, 3], f"Test 118 failed: got {result}, expected {[60, 3, 3]}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = TestArrayElements([6, 3, 3, 0, 0], 2)
        assert result == [6, 3, 60, 0, 0], f"Test 119 failed: got {result}, expected {[6, 3, 60, 0, 0]}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = TestArrayElements([3, 2, -11], 2)
        assert result == [3, 2, 60], f"Test 120 failed: got {result}, expected {[3, 2, 60]}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = TestArrayElements([3, 3], 0)
        assert result == [60, 3], f"Test 121 failed: got {result}, expected {[60, 3]}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = TestArrayElements([3, 3, 0], 2)
        assert result == [3, 3, 60], f"Test 122 failed: got {result}, expected {[3, 3, 60]}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = TestArrayElements([10, 20, 30, 66, 61, 94], 1)
        assert result == [10, 60, 30, 66, 61, 94], f"Test 123 failed: got {result}, expected {[10, 60, 30, 66, 61, 94]}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = TestArrayElements([10, 20, 30, 33, 0, 33], 0)
        assert result == [60, 20, 30, 33, 0, 33], f"Test 124 failed: got {result}, expected {[60, 20, 30, 33, 0, 33]}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = TestArrayElements([70, 30, 20, 10], 1)
        assert result == [70, 60, 20, 10], f"Test 125 failed: got {result}, expected {[70, 60, 20, 10]}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = TestArrayElements([0, 31, 20, 10, 60], 0)
        assert result == [60, 31, 20, 10, 60], f"Test 126 failed: got {result}, expected {[60, 31, 20, 10, 60]}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = TestArrayElements([30, 20, 20, 8, 0], 2)
        assert result == [30, 20, 60, 8, 0], f"Test 127 failed: got {result}, expected {[30, 20, 60, 8, 0]}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = TestArrayElements([10, 20, 30, 15], 2)
        assert result == [10, 20, 60, 15], f"Test 128 failed: got {result}, expected {[10, 20, 60, 15]}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = TestArrayElements([0, 398, 20, 10], 2)
        assert result == [0, 398, 60, 10], f"Test 129 failed: got {result}, expected {[0, 398, 60, 10]}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = TestArrayElements([0, 20, 49], 0)
        assert result == [60, 20, 49], f"Test 130 failed: got {result}, expected {[60, 20, 49]}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = TestArrayElements([30, 20, 10], 2)
        assert result == [30, 20, 60], f"Test 131 failed: got {result}, expected {[30, 20, 60]}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = TestArrayElements([20, 10, 5], 0)
        assert result == [60, 10, 5], f"Test 132 failed: got {result}, expected {[60, 10, 5]}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = TestArrayElements([200, 10, 15, 20, 0, -60], 3)
        assert result == [200, 10, 15, 60, 0, -60], f"Test 133 failed: got {result}, expected {[200, 10, 15, 60, 0, -60]}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = TestArrayElements([34, 0, 20, 15, 10, 5], 3)
        assert result == [34, 0, 20, 60, 10, 5], f"Test 134 failed: got {result}, expected {[34, 0, 20, 60, 10, 5]}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = TestArrayElements([5, 10, 15, 20, 0], 0)
        assert result == [60, 10, 15, 20, 0], f"Test 135 failed: got {result}, expected {[60, 10, 15, 20, 0]}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = TestArrayElements([20, 15, 10, 5], 3)
        assert result == [20, 15, 10, 60], f"Test 136 failed: got {result}, expected {[20, 15, 10, 60]}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = TestArrayElements([5, 10, 20], 2)
        assert result == [5, 10, 60], f"Test 137 failed: got {result}, expected {[5, 10, 60]}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = TestArrayElements([34, 10, 15, 20], 2)
        assert result == [34, 10, 60, 20], f"Test 138 failed: got {result}, expected {[34, 10, 60, 20]}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = TestArrayElements([5, 20], 0)
        assert result == [60, 20], f"Test 139 failed: got {result}, expected {[60, 20]}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = TestArrayElements([5, 10, 15, 20, 42, -6], 0)
        assert result == [60, 10, 15, 20, 42, -6], f"Test 140 failed: got {result}, expected {[60, 10, 15, 20, 42, -6]}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = TestArrayElements([5, 10, 15, 20, 0], 3)
        assert result == [5, 10, 15, 60, 0], f"Test 141 failed: got {result}, expected {[5, 10, 15, 60, 0]}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = TestArrayElements([5, 10, 15, 20, 0], 1)
        assert result == [5, 60, 15, 20, 0], f"Test 142 failed: got {result}, expected {[5, 60, 15, 20, 0]}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = TestArrayElements([100, 200, 300, 400, 500, 0], 4)
        assert result == [100, 200, 300, 400, 60, 0], f"Test 143 failed: got {result}, expected {[100, 200, 300, 400, 60, 0]}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = TestArrayElements([0, 500, 400, 300, 200], 4)
        assert result == [0, 500, 400, 300, 60], f"Test 144 failed: got {result}, expected {[0, 500, 400, 300, 60]}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = TestArrayElements([100, 200, 300, 400, 500, 121], 0)
        assert result == [60, 200, 300, 400, 500, 121], f"Test 145 failed: got {result}, expected {[60, 200, 300, 400, 500, 121]}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = TestArrayElements([500, 400, 300, 200, 100], 0)
        assert result == [60, 400, 300, 200, 100], f"Test 146 failed: got {result}, expected {[60, 400, 300, 200, 100]}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = TestArrayElements([16, 100, 21, 300, 400, 500], 4)
        assert result == [16, 100, 21, 300, 60, 500], f"Test 147 failed: got {result}, expected {[16, 100, 21, 300, 60, 500]}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = TestArrayElements([100, 200, 300, 400, 500, 58], 0)
        assert result == [60, 200, 300, 400, 500, 58], f"Test 148 failed: got {result}, expected {[60, 200, 300, 400, 500, 58]}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = TestArrayElements([100, 6, 300, 500, 28], 3)
        assert result == [100, 6, 300, 60, 28], f"Test 149 failed: got {result}, expected {[100, 6, 300, 60, 28]}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = TestArrayElements([500, 400, 300, 200, 100, -6], 0)
        assert result == [60, 400, 300, 200, 100, -6], f"Test 150 failed: got {result}, expected {[60, 400, 300, 200, 100, -6]}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = TestArrayElements([100, 200, 300, 400], 0)
        assert result == [60, 200, 300, 400], f"Test 151 failed: got {result}, expected {[60, 200, 300, 400]}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = TestArrayElements([100, 200, 300, 400, 500, 0], 0)
        assert result == [60, 200, 300, 400, 500, 0], f"Test 152 failed: got {result}, expected {[60, 200, 300, 400, 500, 0]}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = TestArrayElements([9, 8, 7, 6, 5], 0)
        assert result == [60, 8, 7, 6, 5], f"Test 153 failed: got {result}, expected {[60, 8, 7, 6, 5]}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = TestArrayElements([9, 8, 7, 5, 89], 0)
        assert result == [60, 8, 7, 5, 89], f"Test 154 failed: got {result}, expected {[60, 8, 7, 5, 89]}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = TestArrayElements([0, 5, 6, 7, 8, 9, 70], 0)
        assert result == [60, 5, 6, 7, 8, 9, 70], f"Test 155 failed: got {result}, expected {[60, 5, 6, 7, 8, 9, 70]}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = TestArrayElements([-9, 5, 6, 7, 8, 9, -4], 1)
        assert result == [-9, 60, 6, 7, 8, 9, -4], f"Test 156 failed: got {result}, expected {[-9, 60, 6, 7, 8, 9, -4]}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = TestArrayElements([-9, 8, 7, 6], 0)
        assert result == [60, 8, 7, 6], f"Test 157 failed: got {result}, expected {[60, 8, 7, 6]}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = TestArrayElements([6, 7, 8, 9, 0], 1)
        assert result == [6, 60, 8, 9, 0], f"Test 158 failed: got {result}, expected {[6, 60, 8, 9, 0]}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = TestArrayElements([0, 0, 0, 0, 0], 0)
        assert result == [60, 0, 0, 0, 0], f"Test 159 failed: got {result}, expected {[60, 0, 0, 0, 0]}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = TestArrayElements([0, 0, 0, 0, 0, 0, 66], 5)
        assert result == [0, 0, 0, 0, 0, 60, 66], f"Test 160 failed: got {result}, expected {[0, 0, 0, 0, 0, 60, 66]}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = TestArrayElements([0, 0, 0, 0, 0, 0, 0], 0)
        assert result == [60, 0, 0, 0, 0, 0, 0], f"Test 161 failed: got {result}, expected {[60, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = TestArrayElements([0, 0, 0, 0, -1, 0], 0)
        assert result == [60, 0, 0, 0, -1, 0], f"Test 162 failed: got {result}, expected {[60, 0, 0, 0, -1, 0]}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = TestArrayElements([0, 0, 0, 0, 0, 0, 0], 5)
        assert result == [0, 0, 0, 0, 0, 60, 0], f"Test 163 failed: got {result}, expected {[0, 0, 0, 0, 0, 60, 0]}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = TestArrayElements([-1, 1, -1, 1, -1, 1], 4)
        assert result == [-1, 1, -1, 1, 60, 1], f"Test 164 failed: got {result}, expected {[-1, 1, -1, 1, 60, 1]}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = TestArrayElements([-1, 1, -1, 1, -1, 1, 0, 0], 5)
        assert result == [-1, 1, -1, 1, -1, 60, 0, 0], f"Test 165 failed: got {result}, expected {[-1, 1, -1, 1, -1, 60, 0, 0]}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = TestArrayElements([-1, 1, 1, -1, 1], 0)
        assert result == [60, 1, 1, -1, 1], f"Test 166 failed: got {result}, expected {[60, 1, 1, -1, 1]}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = TestArrayElements([1, -1, 1, -1, 1, -1, 30, 0], 0)
        assert result == [60, -1, 1, -1, 1, -1, 30, 0], f"Test 167 failed: got {result}, expected {[60, -1, 1, -1, 1, -1, 30, 0]}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = TestArrayElements([1, -1, 1, -1, 1, -1], 5)
        assert result == [1, -1, 1, -1, 1, 60], f"Test 168 failed: got {result}, expected {[1, -1, 1, -1, 1, 60]}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = TestArrayElements([-2147483647], 0)
        assert result == [60], f"Test 169 failed: got {result}, expected {[60]}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = TestArrayElements([0, 2147483647, 0], 2)
        assert result == [0, 2147483647, 60], f"Test 170 failed: got {result}, expected {[0, 2147483647, 60]}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = TestArrayElements([2147483647, -2147483648, 0], 1)
        assert result == [2147483647, 60, 0], f"Test 171 failed: got {result}, expected {[2147483647, 60, 0]}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = TestArrayElements([2147483647, -2147483648, 0], 0)
        assert result == [60, -2147483648, 0], f"Test 172 failed: got {result}, expected {[60, -2147483648, 0]}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = TestArrayElements([-8, -2147483648, 0], 2)
        assert result == [-8, -2147483648, 60], f"Test 173 failed: got {result}, expected {[-8, -2147483648, 60]}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = TestArrayElements([-2147483648, 0], 0)
        assert result == [60, 0], f"Test 174 failed: got {result}, expected {[60, 0]}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = TestArrayElements([2147483647, 59, 0], 0)
        assert result == [60, 59, 0], f"Test 175 failed: got {result}, expected {[60, 59, 0]}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = TestArrayElements([0, -6, 42, 60, 42], 1)
        assert result == [0, 60, 42, 60, 42], f"Test 176 failed: got {result}, expected {[0, 60, 42, 60, 42]}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = TestArrayElements([0, 42, 60, 42], 1)
        assert result == [0, 60, 60, 42], f"Test 177 failed: got {result}, expected {[0, 60, 60, 42]}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = TestArrayElements([42, 60, 41, 200], 0)
        assert result == [60, 60, 41, 200], f"Test 178 failed: got {result}, expected {[60, 60, 41, 200]}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = TestArrayElements([42, 60, 42, -5, 0], 1)
        assert result == [42, 60, 42, -5, 0], f"Test 179 failed: got {result}, expected {[42, 60, 42, -5, 0]}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = TestArrayElements([42, 60, 42, 42, 0], 1)
        assert result == [42, 60, 42, 42, 0], f"Test 180 failed: got {result}, expected {[42, 60, 42, 42, 0]}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = TestArrayElements([239, 61, 42], 1)
        assert result == [239, 60, 42], f"Test 181 failed: got {result}, expected {[239, 60, 42]}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = TestArrayElements([43, 60, 42], 0)
        assert result == [60, 60, 42], f"Test 182 failed: got {result}, expected {[60, 60, 42]}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = TestArrayElements([42, 121, 42, 99, 91], 0)
        assert result == [60, 121, 42, 99, 91], f"Test 183 failed: got {result}, expected {[60, 121, 42, 99, 91]}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = TestArrayElements([42, 10, 42, -5], 0)
        assert result == [60, 10, 42, -5], f"Test 184 failed: got {result}, expected {[60, 10, 42, -5]}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = TestArrayElements([42, 42], 0)
        assert result == [60, 42], f"Test 185 failed: got {result}, expected {[60, 42]}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = TestArrayElements([60, 42], 1)
        assert result == [60, 60], f"Test 186 failed: got {result}, expected {[60, 60]}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = TestArrayElements([0, 42, 60, 42], 0)
        assert result == [60, 42, 60, 42], f"Test 187 failed: got {result}, expected {[60, 42, 60, 42]}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = TestArrayElements([42], 0)
        assert result == [60], f"Test 188 failed: got {result}, expected {[60]}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = TestArrayElements([42, 60, 43, 0, 0], 0)
        assert result == [60, 60, 43, 0, 0], f"Test 189 failed: got {result}, expected {[60, 60, 43, 0, 0]}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = TestArrayElements([42, 120, 42, -6], 1)
        assert result == [42, 60, 42, -6], f"Test 190 failed: got {result}, expected {[42, 60, 42, -6]}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = TestArrayElements([42, 60, 42, -2], 1)
        assert result == [42, 60, 42, -2], f"Test 191 failed: got {result}, expected {[42, 60, 42, -2]}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = TestArrayElements([42, 60, 42, 0], 0)
        assert result == [60, 60, 42, 0], f"Test 192 failed: got {result}, expected {[60, 60, 42, 0]}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 66, 77, 12], 6)
        assert result == [11, 22, 33, 44, 55, 66, 60, 12], f"Test 193 failed: got {result}, expected {[11, 22, 33, 44, 55, 66, 60, 12]}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = TestArrayElements([0, 11, 22, 33, 44, 55, 66, 77], 4)
        assert result == [0, 11, 22, 33, 60, 55, 66, 77], f"Test 194 failed: got {result}, expected {[0, 11, 22, 33, 60, 55, 66, 77]}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 66, 77], 5)
        assert result == [11, 22, 33, 44, 55, 60, 77], f"Test 195 failed: got {result}, expected {[11, 22, 33, 44, 55, 60, 77]}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 65, 77, 140, 0], 0)
        assert result == [60, 22, 33, 44, 55, 65, 77, 140, 0], f"Test 196 failed: got {result}, expected {[60, 22, 33, 44, 55, 65, 77, 140, 0]}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 77, 120], 6)
        assert result == [11, 22, 33, 44, 55, 77, 60], f"Test 197 failed: got {result}, expected {[11, 22, 33, 44, 55, 77, 60]}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 66, 77, 0, 49], 7)
        assert result == [11, 22, 33, 44, 55, 66, 77, 60, 49], f"Test 198 failed: got {result}, expected {[11, 22, 33, 44, 55, 66, 77, 60, 49]}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 77, -77, 179], 3)
        assert result == [11, 22, 33, 60, 55, 77, -77, 179], f"Test 199 failed: got {result}, expected {[11, 22, 33, 60, 55, 77, -77, 179]}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 66, 77, 0], 4)
        assert result == [11, 22, 33, 44, 60, 66, 77, 0], f"Test 200 failed: got {result}, expected {[11, 22, 33, 44, 60, 66, 77, 0]}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 66, 77, 0], 3)
        assert result == [11, 22, 33, 60, 55, 66, 77, 0], f"Test 201 failed: got {result}, expected {[11, 22, 33, 60, 55, 66, 77, 0]}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = TestArrayElements([77, 66, 55, 44, 33, 22, 11], 0)
        assert result == [60, 66, 55, 44, 33, 22, 11], f"Test 202 failed: got {result}, expected {[60, 66, 55, 44, 33, 22, 11]}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = TestArrayElements([11, 22, 33, 44, 66, 77], 3)
        assert result == [11, 22, 33, 60, 66, 77], f"Test 203 failed: got {result}, expected {[11, 22, 33, 60, 66, 77]}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = TestArrayElements([22, 33, 44, 55, 66, 77], 3)
        assert result == [22, 33, 44, 60, 66, 77], f"Test 204 failed: got {result}, expected {[22, 33, 44, 60, 66, 77]}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = TestArrayElements([11, 22, 44, -55, 66, 77, 55], 3)
        assert result == [11, 22, 44, 60, 66, 77, 55], f"Test 205 failed: got {result}, expected {[11, 22, 44, 60, 66, 77, 55]}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 66, 77, 0], 0)
        assert result == [60, 22, 33, 44, 55, 66, 77, 0], f"Test 206 failed: got {result}, expected {[60, 22, 33, 44, 55, 66, 77, 0]}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = TestArrayElements([11, 22, 33, 44, 55, 0, 77], 2)
        assert result == [11, 22, 60, 44, 55, 0, 77], f"Test 207 failed: got {result}, expected {[11, 22, 60, 44, 55, 0, 77]}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = TestArrayElements([56, 49, 42, 35, 28, 21, 14, 7], 7)
        assert result == [56, 49, 42, 35, 28, 21, 14, 60], f"Test 208 failed: got {result}, expected {[56, 49, 42, 35, 28, 21, 14, 60]}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = TestArrayElements([56, 49, 42, 35, 28, 14, 7], 0)
        assert result == [60, 49, 42, 35, 28, 14, 7], f"Test 209 failed: got {result}, expected {[60, 49, 42, 35, 28, 14, 7]}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = TestArrayElements([7, 14, 21, 28, 35, 42, 49, 56, -6], 7)
        assert result == [7, 14, 21, 28, 35, 42, 49, 60, -6], f"Test 210 failed: got {result}, expected {[7, 14, 21, 28, 35, 42, 49, 60, -6]}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = TestArrayElements([239, 56, 49, 42, 35, 21, 14, 7], 0)
        assert result == [60, 56, 49, 42, 35, 21, 14, 7], f"Test 211 failed: got {result}, expected {[60, 56, 49, 42, 35, 21, 14, 7]}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = TestArrayElements([56, 49, 42, 35, 28, 7], 2)
        assert result == [56, 49, 60, 35, 28, 7], f"Test 212 failed: got {result}, expected {[56, 49, 60, 35, 28, 7]}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = TestArrayElements([7, 14, 21, 28, 35, 42, 49, 56, 0], 0)
        assert result == [60, 14, 21, 28, 35, 42, 49, 56, 0], f"Test 213 failed: got {result}, expected {[60, 14, 21, 28, 35, 42, 49, 56, 0]}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = TestArrayElements([7, 14, 21, 28, 35, 42, 49, 56, 400, 50], 7)
        assert result == [7, 14, 21, 28, 35, 42, 49, 60, 400, 50], f"Test 214 failed: got {result}, expected {[7, 14, 21, 28, 35, 42, 49, 60, 400, 50]}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = TestArrayElements([56, 42, 35, 28, 21, 0, 7, 0, 55], 0)
        assert result == [60, 42, 35, 28, 21, 0, 7, 0, 55], f"Test 215 failed: got {result}, expected {[60, 42, 35, 28, 21, 0, 7, 0, 55]}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = TestArrayElements([0, 56, 49, 42, 35, 28, 21, 14, 7], 1)
        assert result == [0, 60, 49, 42, 35, 28, 21, 14, 7], f"Test 216 failed: got {result}, expected {[0, 60, 49, 42, 35, 28, 21, 14, 7]}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = TestArrayElements([22, 56, 49, 42, 35, 28, 21, 14, 7], 0)
        assert result == [60, 56, 49, 42, 35, 28, 21, 14, 7], f"Test 217 failed: got {result}, expected {[60, 56, 49, 42, 35, 28, 21, 14, 7]}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = TestArrayElements([7, 14, 21, 28, 35, 42, 49, 56, 0], 1)
        assert result == [7, 60, 21, 28, 35, 42, 49, 56, 0], f"Test 218 failed: got {result}, expected {[7, 60, 21, 28, 35, 42, 49, 56, 0]}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = TestArrayElements([14, 21, 28, 35, 40, 49, 56, 200, 18], 0)
        assert result == [60, 21, 28, 35, 40, 49, 56, 200, 18], f"Test 219 failed: got {result}, expected {[60, 21, 28, 35, 40, 49, 56, 200, 18]}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = TestArrayElements([-78, 91, 92, 93, 94, 95, 96, 97, 98, 99], 0)
        assert result == [60, 91, 92, 93, 94, 95, 96, 97, 98, 99], f"Test 220 failed: got {result}, expected {[60, 91, 92, 93, 94, 95, 96, 97, 98, 99]}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = TestArrayElements([98, 98, 97, 190, 94, 93, 92, 91], 1)
        assert result == [98, 60, 97, 190, 94, 93, 92, 91], f"Test 221 failed: got {result}, expected {[98, 60, 97, 190, 94, 93, 92, 91]}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = TestArrayElements([99, 98, 97, 96, 95, 94, 93, 92, 91], 6)
        assert result == [99, 98, 97, 96, 95, 94, 60, 92, 91], f"Test 222 failed: got {result}, expected {[99, 98, 97, 96, 95, 94, 60, 92, 91]}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = TestArrayElements([99, 98, 97, 96, 95, 93, 92, 91], 6)
        assert result == [99, 98, 97, 96, 95, 93, 60, 91], f"Test 223 failed: got {result}, expected {[99, 98, 97, 96, 95, 93, 60, 91]}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = TestArrayElements([99, 98, 97, 96, 95, 94, 93, 0, 91], 8)
        assert result == [99, 98, 97, 96, 95, 94, 93, 0, 60], f"Test 224 failed: got {result}, expected {[99, 98, 97, 96, 95, 94, 93, 0, 60]}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = TestArrayElements([99, 97, 96, 95, 94, 93, 92, 91, 0], 8)
        assert result == [99, 97, 96, 95, 94, 93, 92, 91, 60], f"Test 225 failed: got {result}, expected {[99, 97, 96, 95, 94, 93, 92, 91, 60]}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = TestArrayElements([91, 92, 93, 94, 95, 96, 97, 98, 99], 8)
        assert result == [91, 92, 93, 94, 95, 96, 97, 98, 60], f"Test 226 failed: got {result}, expected {[91, 92, 93, 94, 95, 96, 97, 98, 60]}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = TestArrayElements([0, 20, 18, 16, 14, 12, 10, 49, 6, 4, 2], 0)
        assert result == [60, 20, 18, 16, 14, 12, 10, 49, 6, 4, 2], f"Test 227 failed: got {result}, expected {[60, 20, 18, 16, 14, 12, 10, 49, 6, 4, 2]}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = TestArrayElements([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0], 0)
        assert result == [60, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0], f"Test 228 failed: got {result}, expected {[60, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0]}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = TestArrayElements([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0], 9)
        assert result == [2, 4, 6, 8, 10, 12, 14, 16, 18, 60, 0], f"Test 229 failed: got {result}, expected {[2, 4, 6, 8, 10, 12, 14, 16, 18, 60, 0]}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = TestArrayElements([-42, 0, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2], 8)
        assert result == [-42, 0, 20, 18, 16, 14, 12, 10, 60, 6, 4, 2], f"Test 230 failed: got {result}, expected {[-42, 0, 20, 18, 16, 14, 12, 10, 60, 6, 4, 2]}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = TestArrayElements([2, 4, 6, 8, 12, 14, 16, 18, 20], 1)
        assert result == [2, 60, 6, 8, 12, 14, 16, 18, 20], f"Test 231 failed: got {result}, expected {[2, 60, 6, 8, 12, 14, 16, 18, 20]}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = TestArrayElements([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1], 0)
        assert result == [60, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1], f"Test 232 failed: got {result}, expected {[60, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1]}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = TestArrayElements([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, -9], 9)
        assert result == [2, 4, 6, 8, 10, 12, 14, 16, 18, 60, -9], f"Test 233 failed: got {result}, expected {[2, 4, 6, 8, 10, 12, 14, 16, 18, 60, -9]}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = TestArrayElements([2, 6, 8, 10, 12, 14, 16, 18, 20, 0], 5)
        assert result == [2, 6, 8, 10, 12, 60, 16, 18, 20, 0], f"Test 234 failed: got {result}, expected {[2, 6, 8, 10, 12, 60, 16, 18, 20, 0]}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = TestArrayElements([20, 18, 16, 14, 12, 10, 8, 6, 4, 2], 0)
        assert result == [60, 18, 16, 14, 12, 10, 8, 6, 4, 2], f"Test 235 failed: got {result}, expected {[60, 18, 16, 14, 12, 10, 8, 6, 4, 2]}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = TestArrayElements([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 95], 5)
        assert result == [2, 4, 6, 8, 10, 60, 14, 16, 18, 20, 95], f"Test 236 failed: got {result}, expected {[2, 4, 6, 8, 10, 60, 14, 16, 18, 20, 95]}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = TestArrayElements([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0], 10)
        assert result == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 60], f"Test 237 failed: got {result}, expected {[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 60]}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = TestArrayElements([20, 18, 16, 14, 12, 10, 8, 6, 11, -2], 3)
        assert result == [20, 18, 16, 60, 12, 10, 8, 6, 11, -2], f"Test 238 failed: got {result}, expected {[20, 18, 16, 60, 12, 10, 8, 6, 11, -2]}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = TestArrayElements([20, 18, 16, 14, 12, 10, 8, 95, -4, 2], 5)
        assert result == [20, 18, 16, 14, 12, 60, 8, 95, -4, 2], f"Test 239 failed: got {result}, expected {[20, 18, 16, 14, 12, 60, 8, 95, -4, 2]}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = TestArrayElements([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 0], 10)
        assert result == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 60, 0], f"Test 240 failed: got {result}, expected {[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 60, 0]}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = TestArrayElements([0, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0], 9)
        assert result == [0, 89, 55, 34, 21, 13, 8, 5, 3, 60, 1, 1, 0], f"Test 241 failed: got {result}, expected {[0, 89, 55, 34, 21, 13, 8, 5, 3, 60, 1, 1, 0]}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = TestArrayElements([1, 1, 2, 3, 5, 8, 0, 21, 34, 55, 89, 0, 0, 0], 9)
        assert result == [1, 1, 2, 3, 5, 8, 0, 21, 34, 60, 89, 0, 0, 0], f"Test 242 failed: got {result}, expected {[1, 1, 2, 3, 5, 8, 0, 21, 34, 60, 89, 0, 0, 0]}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = TestArrayElements([89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1], 10)
        assert result == [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 60], f"Test 243 failed: got {result}, expected {[89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 60]}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = TestArrayElements([0, 89, 55, 34, 21, 13, -9, 5, 3, 2, 1, 1], 0)
        assert result == [60, 89, 55, 34, 21, 13, -9, 5, 3, 2, 1, 1], f"Test 244 failed: got {result}, expected {[60, 89, 55, 34, 21, 13, -9, 5, 3, 2, 1, 1]}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = TestArrayElements([0, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 0, 500], 10)
        assert result == [0, 89, 55, 34, 21, 13, 8, 5, 3, 2, 60, 0, 500], f"Test 245 failed: got {result}, expected {[0, 89, 55, 34, 21, 13, 8, 5, 3, 2, 60, 0, 500]}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = TestArrayElements([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, -91], 10)
        assert result == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 60], f"Test 246 failed: got {result}, expected {[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 60]}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = TestArrayElements([1, 2, 2, 2, 5, 8, 13, 21, 34, 55, 89, 0], 11)
        assert result == [1, 2, 2, 2, 5, 8, 13, 21, 34, 55, 89, 60], f"Test 247 failed: got {result}, expected {[1, 2, 2, 2, 5, 8, 13, 21, 34, 55, 89, 60]}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = TestArrayElements([0, 18], 0)
        assert result == [60, 18], f"Test 248 failed: got {result}, expected {[60, 18]}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = TestArrayElements([0, 0, 0], 1)
        assert result == [0, 60, 0], f"Test 249 failed: got {result}, expected {[0, 60, 0]}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = TestArrayElements([14], 0)
        assert result == [60], f"Test 250 failed: got {result}, expected {[60]}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = TestArrayElements([1, 0], 1)
        assert result == [1, 60], f"Test 251 failed: got {result}, expected {[1, 60]}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = TestArrayElements([1, -6], 1)
        assert result == [1, 60], f"Test 252 failed: got {result}, expected {[1, 60]}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = TestArrayElements([1, 2, 19, 2147483647], 0)
        assert result == [60, 2, 19, 2147483647], f"Test 253 failed: got {result}, expected {[60, 2, 19, 2147483647]}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = TestArrayElements([1, 2, 16], 2)
        assert result == [1, 2, 60], f"Test 254 failed: got {result}, expected {[1, 2, 60]}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = TestArrayElements([0, 12, 2, 0], 2)
        assert result == [0, 12, 60, 0], f"Test 255 failed: got {result}, expected {[0, 12, 60, 0]}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = TestArrayElements([1, 1, 1, 42, 0], 2)
        assert result == [1, 1, 60, 42, 0], f"Test 256 failed: got {result}, expected {[1, 1, 60, 42, 0]}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = TestArrayElements([2, 56], 0)
        assert result == [60, 56], f"Test 257 failed: got {result}, expected {[60, 56]}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = TestArrayElements([0, 2, 1], 0)
        assert result == [60, 2, 1], f"Test 258 failed: got {result}, expected {[60, 2, 1]}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = TestArrayElements([1, 3, 3], 0)
        assert result == [60, 3, 3], f"Test 259 failed: got {result}, expected {[60, 3, 3]}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = TestArrayElements([1, 2, 3, 140], 3)
        assert result == [1, 2, 3, 60], f"Test 260 failed: got {result}, expected {[1, 2, 3, 60]}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = TestArrayElements([3, 2, 1], 0)
        assert result == [60, 2, 1], f"Test 261 failed: got {result}, expected {[60, 2, 1]}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = TestArrayElements([3, 1, 400], 2)
        assert result == [3, 1, 60], f"Test 262 failed: got {result}, expected {[3, 1, 60]}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = TestArrayElements([1, 2, 3], 0)
        assert result == [60, 2, 3], f"Test 263 failed: got {result}, expected {[60, 2, 3]}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = TestArrayElements([1, 2, 3, 0, 0], 0)
        assert result == [60, 2, 3, 0, 0], f"Test 264 failed: got {result}, expected {[60, 2, 3, 0, 0]}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = TestArrayElements([10, 20], 0)
        assert result == [60, 20], f"Test 265 failed: got {result}, expected {[60, 20]}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = TestArrayElements([10, 30, 12, 41], 0)
        assert result == [60, 30, 12, 41], f"Test 266 failed: got {result}, expected {[60, 30, 12, 41]}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = TestArrayElements([0, 30, 20, 10], 0)
        assert result == [60, 30, 20, 10], f"Test 267 failed: got {result}, expected {[60, 30, 20, 10]}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = TestArrayElements([20, 30, 88], 0)
        assert result == [60, 30, 88], f"Test 268 failed: got {result}, expected {[60, 30, 88]}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = TestArrayElements([30, 20, 9], 0)
        assert result == [60, 20, 9], f"Test 269 failed: got {result}, expected {[60, 20, 9]}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = TestArrayElements([5, 10, 15, 20], 0)
        assert result == [60, 10, 15, 20], f"Test 270 failed: got {result}, expected {[60, 10, 15, 20]}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = TestArrayElements([5, 10, 15, 20, 0], 4)
        assert result == [5, 10, 15, 20, 60], f"Test 271 failed: got {result}, expected {[5, 10, 15, 20, 60]}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = TestArrayElements([5, 10, 0, 20, 0], 0)
        assert result == [60, 10, 0, 20, 0], f"Test 272 failed: got {result}, expected {[60, 10, 0, 20, 0]}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = TestArrayElements([-1, 9, 8, 7, 6, 5, 0], 6)
        assert result == [-1, 9, 8, 7, 6, 5, 60], f"Test 273 failed: got {result}, expected {[-1, 9, 8, 7, 6, 5, 60]}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = TestArrayElements([8, 7, 5], 0)
        assert result == [60, 7, 5], f"Test 274 failed: got {result}, expected {[60, 7, 5]}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = TestArrayElements([9, 8, 7, 23, 5], 0)
        assert result == [60, 8, 7, 23, 5], f"Test 275 failed: got {result}, expected {[60, 8, 7, 23, 5]}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
