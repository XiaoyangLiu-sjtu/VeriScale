# Coverage Report

Total executable lines: 4
Covered lines: 4
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def swapFirstAndLast(a):
2: ✓     res = a.copy()
3: ✓     res[0], res[-1] = res[-1], res[0]
4: ✓     return res
```

## Complete Test File

```python
def swapFirstAndLast(a):
    res = a.copy()
    res[0], res[-1] = res[-1], res[0]
    return res

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = swapFirstAndLast([1, 2, 3, 4, 5])
        assert result == [5, 2, 3, 4, 1], f"Test 1 failed: got {result}, expected {[5, 2, 3, 4, 1]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = swapFirstAndLast([10])
        assert result == [10], f"Test 2 failed: got {result}, expected {[10]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = swapFirstAndLast([1, 2])
        assert result == [2, 1], f"Test 3 failed: got {result}, expected {[2, 1]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = swapFirstAndLast([1, 2, 3])
        assert result == [3, 2, 1], f"Test 4 failed: got {result}, expected {[3, 2, 1]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = swapFirstAndLast([-3, -2, -1])
        assert result == [-1, -2, -3], f"Test 5 failed: got {result}, expected {[-1, -2, -3]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = swapFirstAndLast([5, 4, 3, 2, 1])
        assert result == [1, 4, 3, 2, 5], f"Test 6 failed: got {result}, expected {[1, 4, 3, 2, 5]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = swapFirstAndLast([11, 9, 7, 5, 3, 1])
        assert result == [1, 9, 7, 5, 3, 11], f"Test 7 failed: got {result}, expected {[1, 9, 7, 5, 3, 11]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = swapFirstAndLast([1, 3, 4, 5])
        assert result == [5, 3, 4, 1], f"Test 8 failed: got {result}, expected {[5, 3, 4, 1]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = swapFirstAndLast([1, 2, 4, 5, 0, -9223372036854775809, 12345678901234567890])
        assert result == [12345678901234567890, 2, 4, 5, 0, -9223372036854775809, 1], f"Test 9 failed: got {result}, expected {[12345678901234567890, 2, 4, 5, 0, -9223372036854775809, 1]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = swapFirstAndLast([-2, 3, 3, 2])
        assert result == [2, 3, 3, -2], f"Test 10 failed: got {result}, expected {[2, 3, 3, -2]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = swapFirstAndLast([10, 0, 4, 0])
        assert result == [0, 0, 4, 10], f"Test 11 failed: got {result}, expected {[0, 0, 4, 10]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = swapFirstAndLast([1, 2, 3, 17])
        assert result == [17, 2, 3, 1], f"Test 12 failed: got {result}, expected {[17, 2, 3, 1]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = swapFirstAndLast([0, 1, 2, 3, 4])
        assert result == [4, 1, 2, 3, 0], f"Test 13 failed: got {result}, expected {[4, 1, 2, 3, 0]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = swapFirstAndLast([3, 0, -9223372036854775808, 0])
        assert result == [0, 0, -9223372036854775808, 3], f"Test 14 failed: got {result}, expected {[0, 0, -9223372036854775808, 3]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = swapFirstAndLast([0, 9223372036854775807])
        assert result == [9223372036854775807, 0], f"Test 15 failed: got {result}, expected {[9223372036854775807, 0]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = swapFirstAndLast([-1, 8])
        assert result == [8, -1], f"Test 16 failed: got {result}, expected {[8, -1]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = swapFirstAndLast([2, 1, 10, 0])
        assert result == [0, 1, 10, 2], f"Test 17 failed: got {result}, expected {[0, 1, 10, 2]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = swapFirstAndLast([8, -10, 0, 0])
        assert result == [0, -10, 0, 8], f"Test 18 failed: got {result}, expected {[0, -10, 0, 8]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = swapFirstAndLast([-5, -5, 0, -20])
        assert result == [-20, -5, 0, -5], f"Test 19 failed: got {result}, expected {[-20, -5, 0, -5]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = swapFirstAndLast([7, 7, 7, 0, 0])
        assert result == [0, 7, 7, 0, 7], f"Test 20 failed: got {result}, expected {[0, 7, 7, 0, 7]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = swapFirstAndLast([7, 7, 8, 0, 1])
        assert result == [1, 7, 8, 0, 7], f"Test 21 failed: got {result}, expected {[1, 7, 8, 0, 7]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = swapFirstAndLast([7, 7, 0, 0])
        assert result == [0, 7, 0, 7], f"Test 22 failed: got {result}, expected {[0, 7, 0, 7]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = swapFirstAndLast([7, 7, 17, 0])
        assert result == [0, 7, 17, 7], f"Test 23 failed: got {result}, expected {[0, 7, 17, 7]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = swapFirstAndLast([7, 7, 7, -2147483648, 0, 6])
        assert result == [6, 7, 7, -2147483648, 0, 7], f"Test 24 failed: got {result}, expected {[6, 7, 7, -2147483648, 0, 7]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = swapFirstAndLast([3, 2])
        assert result == [2, 3], f"Test 25 failed: got {result}, expected {[2, 3]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = swapFirstAndLast([3, 2, 2, 0, 8, -10])
        assert result == [-10, 2, 2, 0, 8, 3], f"Test 26 failed: got {result}, expected {[-10, 2, 2, 0, 8, 3]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = swapFirstAndLast([1, 2, 3, 0, -2, 0])
        assert result == [0, 2, 3, 0, -2, 1], f"Test 27 failed: got {result}, expected {[0, 2, 3, 0, -2, 1]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = swapFirstAndLast([3, 2, 1, -9223372036854775809, -9223372036854775809])
        assert result == [-9223372036854775809, 2, 1, -9223372036854775809, 3], f"Test 28 failed: got {result}, expected {[-9223372036854775809, 2, 1, -9223372036854775809, 3]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = swapFirstAndLast([-2147483648, -3, -1, 0])
        assert result == [0, -3, -1, -2147483648], f"Test 29 failed: got {result}, expected {[0, -3, -1, -2147483648]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = swapFirstAndLast([-1, 1, 0, 4, 12345678901234567890])
        assert result == [12345678901234567890, 1, 0, 4, -1], f"Test 30 failed: got {result}, expected {[12345678901234567890, 1, 0, 4, -1]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = swapFirstAndLast([0, 0, -20, 20, -10, 10, 23])
        assert result == [23, 0, -20, 20, -10, 10, 0], f"Test 31 failed: got {result}, expected {[23, 0, -20, 20, -10, 10, 0]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = swapFirstAndLast([10, 20, -20])
        assert result == [-20, 20, 10], f"Test 32 failed: got {result}, expected {[-20, 20, 10]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = swapFirstAndLast([42, 10, -10, 20, -20, 0])
        assert result == [0, 10, -10, 20, -20, 42], f"Test 33 failed: got {result}, expected {[0, 10, -10, 20, -20, 42]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = swapFirstAndLast([10, -10, 20, 0, 0])
        assert result == [0, -10, 20, 0, 10], f"Test 34 failed: got {result}, expected {[0, -10, 20, 0, 10]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = swapFirstAndLast([-10, 20, -22, 0])
        assert result == [0, 20, -22, -10], f"Test 35 failed: got {result}, expected {[0, 20, -22, -10]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = swapFirstAndLast([5, 4, 3, 2, 1, 0, 43])
        assert result == [43, 4, 3, 2, 1, 0, 5], f"Test 36 failed: got {result}, expected {[43, 4, 3, 2, 1, 0, 5]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = swapFirstAndLast([-7, 1, 2, 3, 4, 5])
        assert result == [5, 1, 2, 3, 4, -7], f"Test 37 failed: got {result}, expected {[5, 1, 2, 3, 4, -7]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = swapFirstAndLast([1, 3, 5, 7, 9, 11, 0])
        assert result == [0, 3, 5, 7, 9, 11, 1], f"Test 38 failed: got {result}, expected {[0, 3, 5, 7, 9, 11, 1]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = swapFirstAndLast([1, 3, 5, 7, 9, 0])
        assert result == [0, 3, 5, 7, 9, 1], f"Test 39 failed: got {result}, expected {[0, 3, 5, 7, 9, 1]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = swapFirstAndLast([0, 1, 3, 5, 7, 9, 11, 9, 0, 5])
        assert result == [5, 1, 3, 5, 7, 9, 11, 9, 0, 0], f"Test 40 failed: got {result}, expected {[5, 1, 3, 5, 7, 9, 11, 9, 0, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = swapFirstAndLast([11, 10, 7, 5, 3, 1, 28, 0])
        assert result == [0, 10, 7, 5, 3, 1, 28, 11], f"Test 41 failed: got {result}, expected {[0, 10, 7, 5, 3, 1, 28, 11]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = swapFirstAndLast([-1000000, 1000000, 4, -6])
        assert result == [-6, 1000000, 4, -1000000], f"Test 42 failed: got {result}, expected {[-6, 1000000, 4, -1000000]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = swapFirstAndLast([-22, 8, 6, 7, 5, 3, 1, 9])
        assert result == [9, 8, 6, 7, 5, 3, 1, -22], f"Test 43 failed: got {result}, expected {[9, 8, 6, 7, 5, 3, 1, -22]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = swapFirstAndLast([8, 6, 7, 5, 3, 0, 9, -8, 17])
        assert result == [17, 6, 7, 5, 3, 0, 9, -8, 8], f"Test 44 failed: got {result}, expected {[17, 6, 7, 5, 3, 0, 9, -8, 8]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = swapFirstAndLast([8, 6, 7, 4, 3, 0, 0, 9223372036854775807])
        assert result == [9223372036854775807, 6, 7, 4, 3, 0, 0, 8], f"Test 45 failed: got {result}, expected {[9223372036854775807, 6, 7, 4, 3, 0, 0, 8]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = swapFirstAndLast([1, 0, 0, 0, 1, 0])
        assert result == [0, 0, 0, 0, 1, 1], f"Test 46 failed: got {result}, expected {[0, 0, 0, 0, 1, 1]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = swapFirstAndLast([1, 0, 0, 1, 2, 7])
        assert result == [7, 0, 0, 1, 2, 1], f"Test 47 failed: got {result}, expected {[7, 0, 0, 1, 2, 1]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = swapFirstAndLast([4, -1, 4, 43, 11, 0, 7])
        assert result == [7, -1, 4, 43, 11, 0, 4], f"Test 48 failed: got {result}, expected {[7, -1, 4, 43, 11, 0, 4]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = swapFirstAndLast([0, 0, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [1, 0, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0], f"Test 49 failed: got {result}, expected {[1, 0, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = swapFirstAndLast([10, 9, 9, 12, 6, 5, 4, 3, 2, 1, -12345678901234567890])
        assert result == [-12345678901234567890, 9, 9, 12, 6, 5, 4, 3, 2, 1, 10], f"Test 50 failed: got {result}, expected {[-12345678901234567890, 9, 9, 12, 6, 5, 4, 3, 2, 1, 10]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = swapFirstAndLast([-5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
        assert result == [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -5], f"Test 51 failed: got {result}, expected {[0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -5]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = swapFirstAndLast([0, 0, -9223372036854775808, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 10])
        assert result == [10, 0, -9223372036854775808, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 0], f"Test 52 failed: got {result}, expected {[10, 0, -9223372036854775808, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 0]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = swapFirstAndLast([10, 9, 8, 7, 5, 4, 3, 2, 1, 0])
        assert result == [0, 9, 8, 7, 5, 4, 3, 2, 1, 10], f"Test 53 failed: got {result}, expected {[0, 9, 8, 7, 5, 4, 3, 2, 1, 10]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = swapFirstAndLast([-5, 0, -2, -2, -1, 0, -8])
        assert result == [-8, 0, -2, -2, -1, 0, -5], f"Test 54 failed: got {result}, expected {[-8, 0, -2, -2, -1, 0, -5]}"
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
