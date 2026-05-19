# Coverage Report

Total executable lines: 4
Covered lines: 4
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def MoveZeroesToEnd(arr):
2: ✓     non_zeroes = [x for x in arr if x != 0]
3: ✓     zeros_count = len(arr) - len(non_zeroes)
4: ✓     return non_zeroes + [0] * zeros_count
```

## Complete Test File

```python
def MoveZeroesToEnd(arr):
    non_zeroes = [x for x in arr if x != 0]
    zeros_count = len(arr) - len(non_zeroes)
    return non_zeroes + [0] * zeros_count

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = MoveZeroesToEnd([0, 1, 0, 3, 12])
        assert result == [1, 3, 12, 0, 0], f"Test 1 failed: got {result}, expected {[1, 3, 12, 0, 0]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = MoveZeroesToEnd([0, 0, 1])
        assert result == [1, 0, 0], f"Test 2 failed: got {result}, expected {[1, 0, 0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = MoveZeroesToEnd([1, 2, 3])
        assert result == [1, 2, 3], f"Test 3 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = MoveZeroesToEnd([0, 0, 0])
        assert result == [0, 0, 0], f"Test 4 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = MoveZeroesToEnd([])
        assert result == [], f"Test 5 failed: got {result}, expected {[]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = MoveZeroesToEnd([4, 0, 5, 0, 0, 3, 0, 1])
        assert result == [4, 5, 3, 1, 0, 0, 0, 0], f"Test 6 failed: got {result}, expected {[4, 5, 3, 1, 0, 0, 0, 0]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = MoveZeroesToEnd([1, 2, 3, 0, 0])
        assert result == [1, 2, 3, 0, 0], f"Test 7 failed: got {result}, expected {[1, 2, 3, 0, 0]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = MoveZeroesToEnd([1000000, 0, -1000000, 0, 999999, -999999])
        assert result == [1000000, -1000000, 999999, -999999, 0, 0], f"Test 8 failed: got {result}, expected {[1000000, -1000000, 999999, -999999, 0, 0]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = MoveZeroesToEnd([2147483647, 0, -2147483648, 0])
        assert result == [2147483647, -2147483648, 0, 0], f"Test 9 failed: got {result}, expected {[2147483647, -2147483648, 0, 0]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = MoveZeroesToEnd([0, 0, 1, -2147483648])
        assert result == [1, -2147483648, 0, 0], f"Test 10 failed: got {result}, expected {[1, -2147483648, 0, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = MoveZeroesToEnd([0, 1, 12, 3])
        assert result == [1, 12, 3, 0], f"Test 11 failed: got {result}, expected {[1, 12, 3, 0]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = MoveZeroesToEnd([2, 1, 0, 0, 1000000])
        assert result == [2, 1, 1000000, 0, 0], f"Test 12 failed: got {result}, expected {[2, 1, 1000000, 0, 0]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = MoveZeroesToEnd([1, 2, 3, 0, 0])
        assert result == [1, 2, 3, 0, 0], f"Test 13 failed: got {result}, expected {[1, 2, 3, 0, 0]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = MoveZeroesToEnd([3, 2, 1, 6, 0, 0])
        assert result == [3, 2, 1, 6, 0, 0], f"Test 14 failed: got {result}, expected {[3, 2, 1, 6, 0, 0]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = MoveZeroesToEnd([0, 1, 0])
        assert result == [1, 0, 0], f"Test 15 failed: got {result}, expected {[1, 0, 0]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = MoveZeroesToEnd([0, 2147483647])
        assert result == [2147483647, 0], f"Test 16 failed: got {result}, expected {[2147483647, 0]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = MoveZeroesToEnd([22, 0, 33])
        assert result == [22, 33, 0], f"Test 17 failed: got {result}, expected {[22, 33, 0]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = MoveZeroesToEnd([0, 1, 0])
        assert result == [1, 0, 0], f"Test 18 failed: got {result}, expected {[1, 0, 0]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = MoveZeroesToEnd([0, 0, 14, 0])
        assert result == [14, 0, 0, 0], f"Test 19 failed: got {result}, expected {[14, 0, 0, 0]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = MoveZeroesToEnd([-3, 0, 0])
        assert result == [-3, 0, 0], f"Test 20 failed: got {result}, expected {[-3, 0, 0]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = MoveZeroesToEnd([-1, 0, 0])
        assert result == [-1, 0, 0], f"Test 21 failed: got {result}, expected {[-1, 0, 0]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = MoveZeroesToEnd([0, -2147483648, 0, -2147483648, 1, 0])
        assert result == [-2147483648, -2147483648, 1, 0, 0, 0], f"Test 22 failed: got {result}, expected {[-2147483648, -2147483648, 1, 0, 0, 0]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = MoveZeroesToEnd([0, 101112, 0])
        assert result == [101112, 0, 0], f"Test 23 failed: got {result}, expected {[101112, 0, 0]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = MoveZeroesToEnd([55, 2, 3, 0, -5])
        assert result == [55, 2, 3, -5, 0], f"Test 24 failed: got {result}, expected {[55, 2, 3, -5, 0]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = MoveZeroesToEnd([3, 2, 1, 0, 0])
        assert result == [3, 2, 1, 0, 0], f"Test 25 failed: got {result}, expected {[3, 2, 1, 0, 0]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = MoveZeroesToEnd([0, 0, 0, 456, 0, 0])
        assert result == [456, 0, 0, 0, 0, 0], f"Test 26 failed: got {result}, expected {[456, 0, 0, 0, 0, 0]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = MoveZeroesToEnd([4, 0, 5, 0, 0, 3, 0, 1, 0])
        assert result == [4, 5, 3, 1, 0, 0, 0, 0, 0], f"Test 27 failed: got {result}, expected {[4, 5, 3, 1, 0, 0, 0, 0, 0]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = MoveZeroesToEnd([-9223372036854775806, 44, 0, 3, 0, 0, 5, 0, 4, 0])
        assert result == [-9223372036854775806, 44, 3, 5, 4, 0, 0, 0, 0, 0], f"Test 28 failed: got {result}, expected {[-9223372036854775806, 44, 3, 5, 4, 0, 0, 0, 0, 0]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = MoveZeroesToEnd([33, 4, 0, 5, 0, 0, 3, 0, 1, 0])
        assert result == [33, 4, 5, 3, 1, 0, 0, 0, 0, 0], f"Test 29 failed: got {result}, expected {[33, 4, 5, 3, 1, 0, 0, 0, 0, 0]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = MoveZeroesToEnd([4, 0, 5, 0, 0, 3, 0, 1, 131416])
        assert result == [4, 5, 3, 1, 131416, 0, 0, 0, 0], f"Test 30 failed: got {result}, expected {[4, 5, 3, 1, 131416, 0, 0, 0, 0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = MoveZeroesToEnd([1, 2, 0, 3, 0, 4, 0])
        assert result == [1, 2, 3, 4, 0, 0, 0], f"Test 31 failed: got {result}, expected {[1, 2, 3, 4, 0, 0, 0]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = MoveZeroesToEnd([0, 3, 0])
        assert result == [3, 0, 0], f"Test 32 failed: got {result}, expected {[3, 0, 0]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = MoveZeroesToEnd([0, -1, 2, 10, 0, 0])
        assert result == [-1, 2, 10, 0, 0, 0], f"Test 33 failed: got {result}, expected {[-1, 2, 10, 0, 0, 0]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = MoveZeroesToEnd([14, 0, 3, 2, 1, 0, 0])
        assert result == [14, 3, 2, 1, 0, 0, 0], f"Test 34 failed: got {result}, expected {[14, 3, 2, 1, 0, 0, 0]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = MoveZeroesToEnd([-3, 0, -2, 0, -1, 0])
        assert result == [-3, -2, -1, 0, 0, 0], f"Test 35 failed: got {result}, expected {[-3, -2, -1, 0, 0, 0]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = MoveZeroesToEnd([-1, 0, -2, 0, -3, -1])
        assert result == [-1, -2, -3, -1, 0, 0], f"Test 36 failed: got {result}, expected {[-1, -2, -3, -1, 0, 0]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = MoveZeroesToEnd([9, 8, 0, 7, 0, 6, 5, 0, 4, 3, 2, 1, 0, 6, -2147483648])
        assert result == [9, 8, 7, 6, 5, 4, 3, 2, 1, 6, -2147483648, 0, 0, 0, 0], f"Test 37 failed: got {result}, expected {[9, 8, 7, 6, 5, 4, 3, 2, 1, 6, -2147483648, 0, 0, 0, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = MoveZeroesToEnd([9, 8, 0, 7, 0, 6, 5, 0, 4, 3, 3, 1, 0, 21, -3, 0])
        assert result == [9, 8, 7, 6, 5, 4, 3, 3, 1, 21, -3, 0, 0, 0, 0, 0], f"Test 38 failed: got {result}, expected {[9, 8, 7, 6, 5, 4, 3, 3, 1, 21, -3, 0, 0, 0, 0, 0]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = MoveZeroesToEnd([1000000, -1000000, 0, 999999, 999999])
        assert result == [1000000, -1000000, 999999, 999999, 0], f"Test 39 failed: got {result}, expected {[1000000, -1000000, 999999, 999999, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = MoveZeroesToEnd([0, -999999, 999999, 0, -1000000, 0, -9223372036854775806])
        assert result == [-999999, 999999, -1000000, -9223372036854775806, 0, 0, 0], f"Test 40 failed: got {result}, expected {[-999999, 999999, -1000000, -9223372036854775806, 0, 0, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = MoveZeroesToEnd([2147483647, 0, -2147483648, 0, 0, 0, 6, 0])
        assert result == [2147483647, -2147483648, 6, 0, 0, 0, 0, 0], f"Test 41 failed: got {result}, expected {[2147483647, -2147483648, 6, 0, 0, 0, 0, 0]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = MoveZeroesToEnd([9223372036854775807, 0, -9223372036854775808, -9223372036854775808])
        assert result == [9223372036854775807, -9223372036854775808, -9223372036854775808, 0], f"Test 42 failed: got {result}, expected {[9223372036854775807, -9223372036854775808, -9223372036854775808, 0]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = MoveZeroesToEnd([0, 0, 2, 0, 2, 2, 2])
        assert result == [2, 2, 2, 2, 0, 0, 0], f"Test 43 failed: got {result}, expected {[2, 2, 2, 2, 0, 0, 0]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = MoveZeroesToEnd([0, 2, 2, 2, 2, 2, 0, 0, 0])
        assert result == [2, 2, 2, 2, 2, 0, 0, 0, 0], f"Test 44 failed: got {result}, expected {[2, 2, 2, 2, 2, 0, 0, 0, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = MoveZeroesToEnd([0, 2, 2, 2, 2, 2, 0, 0])
        assert result == [2, 2, 2, 2, 2, 0, 0, 0], f"Test 45 failed: got {result}, expected {[2, 2, 2, 2, 2, 0, 0, 0]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = MoveZeroesToEnd([2, 2, 2, 2, 2, 0, 0, 21, 0])
        assert result == [2, 2, 2, 2, 2, 21, 0, 0, 0], f"Test 46 failed: got {result}, expected {[2, 2, 2, 2, 2, 21, 0, 0, 0]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = MoveZeroesToEnd([2, 2, 2, 2, 3, 0, -18446744073709551616, 0])
        assert result == [2, 2, 2, 2, 3, -18446744073709551616, 0, 0], f"Test 47 failed: got {result}, expected {[2, 2, 2, 2, 3, -18446744073709551616, 0, 0]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = MoveZeroesToEnd([0, 0, 0, 1, 1, 0, 0, 0])
        assert result == [1, 1, 0, 0, 0, 0, 0, 0], f"Test 48 failed: got {result}, expected {[1, 1, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = MoveZeroesToEnd([1, 2, 0, 0, 0, 2, 2, -5])
        assert result == [1, 2, 2, 2, -5, 0, 0, 0], f"Test 49 failed: got {result}, expected {[1, 2, 2, 2, -5, 0, 0, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = MoveZeroesToEnd([0, 0, 3, 0, 3, 0, 3, 0])
        assert result == [3, 3, 3, 0, 0, 0, 0, 0], f"Test 50 failed: got {result}, expected {[3, 3, 3, 0, 0, 0, 0, 0]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = MoveZeroesToEnd([131416, -9, 0, 10, -10, 0, 5, 0, -5, 0, 0])
        assert result == [131416, -9, 10, -10, 5, -5, 0, 0, 0, 0, 0], f"Test 51 failed: got {result}, expected {[131416, -9, 10, -10, 5, -5, 0, 0, 0, 0, 0]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = MoveZeroesToEnd([0, 11, 22, 33, 44, 0, 55, 0, 0, 0, 0])
        assert result == [11, 22, 33, 44, 55, 0, 0, 0, 0, 0, 0], f"Test 52 failed: got {result}, expected {[11, 22, 33, 44, 55, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = MoveZeroesToEnd([123, 0, 456, 789, 0, 101112, 0, 10])
        assert result == [123, 456, 789, 101112, 10, 0, 0, 0], f"Test 53 failed: got {result}, expected {[123, 456, 789, 101112, 10, 0, 0, 0]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
