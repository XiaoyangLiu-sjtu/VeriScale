# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def elementWiseModulo(a, b):
2: ✓     return [x % y for x, y in zip(a, b)]
```

## Complete Test File

```python
def elementWiseModulo(a, b):
    return [x % y for x, y in zip(a, b)]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = elementWiseModulo([10, 20, 30], [3, 7, 5])
        assert result == [1, 6, 0], f"Test 1 failed: got {result}, expected {[1, 6, 0]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = elementWiseModulo([100, 200, 300, 400], [10, 20, 30, 50])
        assert result == [0, 0, 0, 0], f"Test 2 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = elementWiseModulo([-10, -20, 30], [3, -7, 5])
        assert result == [2, 1, 0], f"Test 3 failed: got {result}, expected {[2, 1, 0]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = elementWiseModulo([5], [2])
        assert result == [1], f"Test 4 failed: got {result}, expected {[1]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = elementWiseModulo([-5], [-2])
        assert result == [1], f"Test 5 failed: got {result}, expected {[1]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = elementWiseModulo([0, 14], [3, 5])
        assert result == [0, 4], f"Test 6 failed: got {result}, expected {[0, 4]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = elementWiseModulo([-13, 27], [5, -4])
        assert result == [2, 3], f"Test 7 failed: got {result}, expected {[2, 3]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = elementWiseModulo([10, -20, 30], [3, 7, -5])
        assert result == [1, 1, 0], f"Test 8 failed: got {result}, expected {[1, 1, 0]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = elementWiseModulo([1000000, -999999, 123456789], [97, -31, 1000])
        assert result == [27, 30, 789], f"Test 9 failed: got {result}, expected {[27, 30, 789]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = elementWiseModulo([1, 2, 3, 4], [1, 1, 1, 1])
        assert result == [0, 0, 0, 0], f"Test 10 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = elementWiseModulo([9, -8, 7, -6], [-2, -3, -4, -5])
        assert result == [1, 1, 3, 4], f"Test 11 failed: got {result}, expected {[1, 1, 3, 4]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = elementWiseModulo([11, -22, 33, -44, 55], [6, 7, -8, 9, -10])
        assert result == [5, 6, 1, 1, 5], f"Test 12 failed: got {result}, expected {[5, 6, 1, 1, 5]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = elementWiseModulo([101, 103, 107, 109, 113], [2, 3, 5, 7, 11])
        assert result == [1, 1, 2, 4, 3], f"Test 13 failed: got {result}, expected {[1, 1, 2, 4, 3]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = elementWiseModulo([-9223372036854775808, 9223372036854775807, 0, 42, -42, 999999999999], [3, -7, 5, -9, 11, 13])
        assert result == [1, 0, 0, 6, 2, 0], f"Test 14 failed: got {result}, expected {[1, 0, 0, 6, 2, 0]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = elementWiseModulo([15, 30, 45, 60, 75, 90], [-1, 2, -3, 4, -5, 6])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 15 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = elementWiseModulo([7, 14, 21, 28, 35, 42, 49], [5, 6, 7, 8, 9, 10, 11])
        assert result == [2, 2, 0, 4, 8, 2, 5], f"Test 16 failed: got {result}, expected {[2, 2, 0, 4, 8, 2, 5]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = elementWiseModulo([3, 6, 9, 12, 15, 18, 21, 24], [2, -5, 4, -7, 6, -9, 8, -11])
        assert result == [1, 1, 1, 5, 3, 0, 5, 2], f"Test 17 failed: got {result}, expected {[1, 1, 1, 5, 3, 0, 5, 2]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = elementWiseModulo([12, 24, 36], [6, 8, 9])
        assert result == [0, 0, 0], f"Test 18 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = elementWiseModulo([1, 2, 3], [10, 10, 10])
        assert result == [1, 2, 3], f"Test 19 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = elementWiseModulo([12345678901234567890, -12345678901234567890], [97, -97])
        assert result == [3, 94], f"Test 20 failed: got {result}, expected {[3, 94]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = elementWiseModulo([8, 16, 24, 32, 40, 48, 56, 64, 72], [3, 5, 7, 9, 11, 13, 15, 17, 19])
        assert result == [2, 1, 3, 5, 7, 9, 11, 13, 15], f"Test 21 failed: got {result}, expected {[2, 1, 3, 5, 7, 9, 11, 13, 15]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = elementWiseModulo([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], f"Test 22 failed: got {result}, expected {[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = elementWiseModulo([999], [1000000000])
        assert result == [999], f"Test 23 failed: got {result}, expected {[999]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = elementWiseModulo([42, -42], [42, -42])
        assert result == [0, 0], f"Test 24 failed: got {result}, expected {[0, 0]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = elementWiseModulo([0, -1, 1], [-2, 3, -4])
        assert result == [0, 2, 1], f"Test 25 failed: got {result}, expected {[0, 2, 1]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = elementWiseModulo([-100, -50, 50, 100], [9, -8, 7, -6])
        assert result == [8, 6, 1, 4], f"Test 26 failed: got {result}, expected {[8, 6, 1, 4]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = elementWiseModulo([13, 26, 39, 52, 65], [-1, -1, -1, -1, -1])
        assert result == [0, 0, 0, 0, 0], f"Test 27 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = elementWiseModulo([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12])
        assert result == [1, 3, 5, 7, 9, 11], f"Test 28 failed: got {result}, expected {[1, 3, 5, 7, 9, 11]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = elementWiseModulo([-9, -18, -27], [-4, -5, -6])
        assert result == [3, 2, 3], f"Test 29 failed: got {result}, expected {[3, 2, 3]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = elementWiseModulo([-1000, -2000], [256, 512])
        assert result == [24, 48], f"Test 30 failed: got {result}, expected {[24, 48]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = elementWiseModulo([17, 19, 23, 29], [4, 6, 8, 10])
        assert result == [1, 1, 7, 9], f"Test 31 failed: got {result}, expected {[1, 1, 7, 9]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = elementWiseModulo([5, 5, 5, 5, 5], [2, 3, 4, 5, 6])
        assert result == [1, 2, 1, 0, 5], f"Test 32 failed: got {result}, expected {[1, 2, 1, 0, 5]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = elementWiseModulo([1, 1, 2, 3, 5, 8, 13], [2, 3, 5, 7, 11, 13, 17])
        assert result == [1, 1, 2, 3, 5, 8, 13], f"Test 33 failed: got {result}, expected {[1, 1, 2, 3, 5, 8, 13]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = elementWiseModulo([2, 4, 8, 16, 32, 64, 128, 256], [3, 5, 7, 9, 11, 13, 15, 17])
        assert result == [2, 4, 1, 7, 10, 12, 8, 1], f"Test 34 failed: got {result}, expected {[2, 4, 1, 7, 10, 12, 8, 1]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = elementWiseModulo([12, -24, 36, -48, 60, -72, 84, -96, 108, -120, 132, -144], [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27])
        assert result == [2, 4, 0, 7, 8, 3, 16, 18, 3, 18, 7, 18], f"Test 35 failed: got {result}, expected {[2, 4, 0, 7, 8, 3, 16, 18, 3, 18, 7, 18]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = elementWiseModulo([100, 200, 300, 399], [10, 20, 30, 50])
        assert result == [0, 0, 0, 49], f"Test 36 failed: got {result}, expected {[0, 0, 0, 49]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = elementWiseModulo([100, 200, 300, 400, 0], [10, 20, 30, 50, 75])
        assert result == [0, 0, 0, 0, 0], f"Test 37 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = elementWiseModulo([100, 200, 300, 401], [50, 30, 20, 10])
        assert result == [0, 20, 0, 1], f"Test 38 failed: got {result}, expected {[0, 20, 0, 1]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = elementWiseModulo([0, 30, -20, -10], [-7, 5, 33, -72])
        assert result == [0, 0, 13, 62], f"Test 39 failed: got {result}, expected {[0, 0, 13, 62]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = elementWiseModulo([-10, -20, 0], [13, -7, 5])
        assert result == [3, 1, 0], f"Test 40 failed: got {result}, expected {[3, 1, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = elementWiseModulo([-10, 33, 29], [5, -7, 3])
        assert result == [0, 5, 2], f"Test 41 failed: got {result}, expected {[0, 5, 2]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = elementWiseModulo([1], [4])
        assert result == [1], f"Test 42 failed: got {result}, expected {[1]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = elementWiseModulo([0], [2])
        assert result == [0], f"Test 43 failed: got {result}, expected {[0]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = elementWiseModulo([2], [2])
        assert result == [0], f"Test 44 failed: got {result}, expected {[0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = elementWiseModulo([5, 0], [2, 15])
        assert result == [1, 0], f"Test 45 failed: got {result}, expected {[1, 0]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = elementWiseModulo([-5], [-3])
        assert result == [1], f"Test 46 failed: got {result}, expected {[1]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = elementWiseModulo([0, 14], [5, 3])
        assert result == [0, 2], f"Test 47 failed: got {result}, expected {[0, 2]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = elementWiseModulo([0, 25], [5, 3])
        assert result == [0, 1], f"Test 48 failed: got {result}, expected {[0, 1]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = elementWiseModulo([14, 0], [3, 5])
        assert result == [2, 0], f"Test 49 failed: got {result}, expected {[2, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = elementWiseModulo([0, 14, 0], [90, 3, -48])
        assert result == [0, 2, 0], f"Test 50 failed: got {result}, expected {[0, 2, 0]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = elementWiseModulo([-13, 27, 0], [5, -4, 399])
        assert result == [2, 3, 0], f"Test 51 failed: got {result}, expected {[2, 3, 0]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = elementWiseModulo([0, 27, 0], [5, -4, 11])
        assert result == [0, 3, 0], f"Test 52 failed: got {result}, expected {[0, 3, 0]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = elementWiseModulo([27, -13], [5, 113])
        assert result == [2, 100], f"Test 53 failed: got {result}, expected {[2, 100]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = elementWiseModulo([13, 27], [-4, 4])
        assert result == [1, 3], f"Test 54 failed: got {result}, expected {[1, 3]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = elementWiseModulo([10, -20, 30], [3, 7, 401])
        assert result == [1, 1, 30], f"Test 55 failed: got {result}, expected {[1, 1, 30]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = elementWiseModulo([-20, 30], [8, -5])
        assert result == [4, 0], f"Test 56 failed: got {result}, expected {[4, 0]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = elementWiseModulo([-40, 10, 0], [3, 7, -5])
        assert result == [2, 3, 0], f"Test 57 failed: got {result}, expected {[2, 3, 0]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = elementWiseModulo([30, -20, 10], [1, 7, -5])
        assert result == [0, 1, 0], f"Test 58 failed: got {result}, expected {[0, 1, 0]}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = elementWiseModulo([0, 30, -20], [-5, 8, 3])
        assert result == [0, 6, 1], f"Test 59 failed: got {result}, expected {[0, 6, 1]}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = elementWiseModulo([-999999, 1000000], [-31, 1000])
        assert result == [30, 0], f"Test 60 failed: got {result}, expected {[30, 0]}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = elementWiseModulo([1000000, 123456790, 13], [97, -31, 1000])
        assert result == [27, 3, 13], f"Test 61 failed: got {result}, expected {[27, 3, 13]}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = elementWiseModulo([1000000, 0, 0], [97, -31, 1000])
        assert result == [27, 0, 0], f"Test 62 failed: got {result}, expected {[27, 0, 0]}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = elementWiseModulo([1000000, 123456791, 16], [1000, 31, 97])
        assert result == [0, 4, 16], f"Test 63 failed: got {result}, expected {[0, 4, 16]}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = elementWiseModulo([1, 2, 3, 4], [1, -7, 1, 1])
        assert result == [0, 2, 0, 0], f"Test 64 failed: got {result}, expected {[0, 2, 0, 0]}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = elementWiseModulo([-21, 2, 3, 4], [1, 1, 1, 1])
        assert result == [0, 0, 0, 0], f"Test 65 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = elementWiseModulo([1, 2, 4, 4], [1, 1, 1, 1])
        assert result == [0, 0, 0, 0], f"Test 66 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = elementWiseModulo([1, 2, 3, 4], [1, 1, 1, 256])
        assert result == [0, 0, 0, 4], f"Test 67 failed: got {result}, expected {[0, 0, 0, 4]}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = elementWiseModulo([1, 2, 4], [1, 1, 1])
        assert result == [0, 0, 0], f"Test 68 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = elementWiseModulo([9, 0, 7, -6], [-5, -4, -3, -2])
        assert result == [4, 0, 1, 0], f"Test 69 failed: got {result}, expected {[4, 0, 1, 0]}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = elementWiseModulo([11, -22, 33, -44, 55], [6, 7, 9, -10, -42])
        assert result == [5, 6, 6, 6, 13], f"Test 70 failed: got {result}, expected {[5, 6, 6, 6, 13]}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = elementWiseModulo([101, 103, 107, 0, 23], [2, 3, 5, 7, 11])
        assert result == [1, 1, 2, 0, 1], f"Test 71 failed: got {result}, expected {[1, 1, 2, 0, 1]}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = elementWiseModulo([101, 103, 107, 109, -113], [2, 3, 5, 7, 11])
        assert result == [1, 1, 2, 4, 8], f"Test 72 failed: got {result}, expected {[1, 1, 2, 4, 8]}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = elementWiseModulo([101, 103, 109, 113, 1000000], [-11, 7, 5, 3, 2])
        assert result == [2, 5, 4, 2, 0], f"Test 73 failed: got {result}, expected {[2, 5, 4, 2, 0]}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = elementWiseModulo([101, 103, 107, 0, 113], [2, 3, -5, 7, 11])
        assert result == [1, 1, 2, 0, 3], f"Test 74 failed: got {result}, expected {[1, 1, 2, 0, 3]}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = elementWiseModulo([999999999999, -42, 42, 0, 9223372036854775807, -9223372036854775808], [13, 11, -9, 5, -7, 3])
        assert result == [0, 2, 6, 0, 0, 1], f"Test 75 failed: got {result}, expected {[0, 2, 6, 0, 0, 1]}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = elementWiseModulo([0, 9223372036854775807, 0, 42, 202, 999999999999, 26], [3, -7, 5, -9, 11, 13, 35])
        assert result == [0, 0, 0, 6, 4, 0, 26], f"Test 76 failed: got {result}, expected {[0, 0, 0, 6, 4, 0, 26]}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = elementWiseModulo([-9223372036854775808, 9223372036854775807, 0, 43, -42, 999999999999], [3, -7, 5, -9, 11, 13])
        assert result == [1, 0, 0, 7, 2, 0], f"Test 77 failed: got {result}, expected {[1, 0, 0, 7, 2, 0]}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = elementWiseModulo([-9223372036854775808, 9223372036854775807, 0, 42, -42, 999999999999, 99], [3, -7, 5, -9, 11, 13, -30])
        assert result == [1, 0, 0, 6, 2, 0, 9], f"Test 78 failed: got {result}, expected {[1, 0, 0, 6, 2, 0, 9]}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = elementWiseModulo([-9223372036854775808, 9223372036854775807, 0, 42, -42, 999999999999], [13, 11, -9, 5, -7, 3])
        assert result == [5, 7, 0, 2, 0, 0], f"Test 79 failed: got {result}, expected {[5, 7, 0, 2, 0, 0]}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = elementWiseModulo([-9223372036854775808, 9223372036854775807, 0, 42, -42, 999999999999], [3, -7, 5, 11, 13, 109])
        assert result == [1, 0, 0, 9, 10, 65], f"Test 80 failed: got {result}, expected {[1, 0, 0, 9, 10, 65]}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = elementWiseModulo([14, 30, 45, 60, 75, 90], [-1, 2, -3, 4, -5, 6])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 81 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = elementWiseModulo([15, 30, 45, 60, 75, 90], [6, -5, 4, -3, 2, -1])
        assert result == [3, 0, 1, 0, 1, 0], f"Test 82 failed: got {result}, expected {[3, 0, 1, 0, 1, 0]}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = elementWiseModulo([49, 42, 35, 28, 21, 14, 7], [11, 10, 9, 8, 7, 6, 5])
        assert result == [5, 2, 8, 4, 0, 2, 2], f"Test 83 failed: got {result}, expected {[5, 2, 8, 4, 0, 2, 2]}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = elementWiseModulo([24, 21, 18, 15, 12, 9, 6, 3], [2, -5, 4, -7, 6, -9, 8, -11])
        assert result == [0, 1, 2, 1, 0, 0, 6, 3], f"Test 84 failed: got {result}, expected {[0, 1, 2, 1, 0, 0, 6, 3]}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = elementWiseModulo([60, 24, 21, 15, 12, 9, 6, 3], [-11, 9, -9, 6, -7, 4, -5, 2])
        assert result == [5, 6, 3, 3, 5, 1, 1, 1], f"Test 85 failed: got {result}, expected {[5, 6, 3, 3, 5, 1, 1, 1]}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = elementWiseModulo([3, 6, 9, 12, 15, 18, 21, 24], [-11, 8, -9, 6, -7, 4, -5, 2])
        assert result == [3, 6, 0, 0, 1, 2, 1, 0], f"Test 86 failed: got {result}, expected {[3, 6, 0, 0, 1, 2, 1, 0]}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = elementWiseModulo([24, 21, 18, 15, 12, 9, 6, 3], [-11, 8, -9, 6, -7, 4, -5, 2])
        assert result == [2, 5, 0, 3, 5, 1, 1, 1], f"Test 87 failed: got {result}, expected {[2, 5, 0, 3, 5, 1, 1, 1]}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = elementWiseModulo([12, 24, 36], [399, 8, 9])
        assert result == [12, 0, 0], f"Test 88 failed: got {result}, expected {[12, 0, 0]}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = elementWiseModulo([0, 36, 24, 12], [6, 8, 9, 1000])
        assert result == [0, 4, 6, 12], f"Test 89 failed: got {result}, expected {[0, 4, 6, 12]}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = elementWiseModulo([36, 24, 12], [6, 8, 9])
        assert result == [0, 0, 3], f"Test 90 failed: got {result}, expected {[0, 0, 3]}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = elementWiseModulo([17, 1, 1], [10, 10, 10])
        assert result == [7, 1, 1], f"Test 91 failed: got {result}, expected {[7, 1, 1]}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = elementWiseModulo([1, 4, 3], [9, 10, 10])
        assert result == [1, 4, 3], f"Test 92 failed: got {result}, expected {[1, 4, 3]}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = elementWiseModulo([1, 2, 3, 0], [10, 10, 10, 36])
        assert result == [1, 2, 3, 0], f"Test 93 failed: got {result}, expected {[1, 2, 3, 0]}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = elementWiseModulo([1, 2, 6], [10, 10, 10])
        assert result == [1, 2, 6], f"Test 94 failed: got {result}, expected {[1, 2, 6]}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = elementWiseModulo([1, 2, 3], [11, 52, 90])
        assert result == [1, 2, 3], f"Test 95 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = elementWiseModulo([3, 2, 1], [10, 10, 10])
        assert result == [3, 2, 1], f"Test 96 failed: got {result}, expected {[3, 2, 1]}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = elementWiseModulo([24691357802469135780, -12345678901234567890], [97, -97])
        assert result == [6, 94], f"Test 97 failed: got {result}, expected {[6, 94]}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = elementWiseModulo([-100, -12345678901234567890], [97, -97])
        assert result == [94, 94], f"Test 98 failed: got {result}, expected {[94, 94]}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = elementWiseModulo([-12345678901234567890, 12345678901234567890], [97, -97])
        assert result == [94, 3], f"Test 99 failed: got {result}, expected {[94, 3]}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = elementWiseModulo([12345678901234567890, -12345678901234567890, 27], [-97, 97, 17])
        assert result == [3, 94, 10], f"Test 100 failed: got {result}, expected {[3, 94, 10]}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = elementWiseModulo([8, 16, 24, 32, 40, 48, 56, 64, 72], [19, 17, 15, 13, 11, 9, 7, 5, 3])
        assert result == [8, 16, 9, 6, 7, 3, 0, 4, 0], f"Test 101 failed: got {result}, expected {[8, 16, 9, 6, 7, 3, 0, 4, 0]}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = elementWiseModulo([72, 64, 56, 48, 40, 32, 24, 16, 8, 107], [19, 17, 15, 13, 11, 9, 7, 5, 3, 399])
        assert result == [15, 13, 11, 9, 7, 5, 3, 1, 2, 107], f"Test 102 failed: got {result}, expected {[15, 13, 11, 9, 7, 5, 3, 1, 2, 107]}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = elementWiseModulo([1, 2, 3, 4, 5, 6, 7, 8, 300, 36], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [1, 0, 1, 0, 1, 0, 1, 0, 0, 0], f"Test 103 failed: got {result}, expected {[1, 0, 1, 0, 1, 0, 1, 0, 0, 0]}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = elementWiseModulo([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 2, 2, 2, 2, 1, 2, 2, 2, 2])
        assert result == [0, 1, 0, 1, 0, 0, 0, 1, 0, 1], f"Test 104 failed: got {result}, expected {[0, 1, 0, 1, 0, 0, 0, 1, 0, 1]}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = elementWiseModulo([0, 8, 7, 6, 5, 4, 3, 2, 1, 0], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [0, 0, 1, 0, 1, 0, 1, 0, 1, 0], f"Test 105 failed: got {result}, expected {[0, 0, 1, 0, 1, 0, 1, 0, 1, 0]}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = elementWiseModulo([0, 1, 2, 3, 4, 5, 6, 8, 9], [2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [0, 1, 0, 1, 0, 1, 0, 0, 1], f"Test 106 failed: got {result}, expected {[0, 1, 0, 1, 0, 1, 0, 0, 1]}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = elementWiseModulo([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], f"Test 107 failed: got {result}, expected {[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = elementWiseModulo([9, 8, 7, 6, 99, 4, 3, 2, 1, 0], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], f"Test 108 failed: got {result}, expected {[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = elementWiseModulo([1000, 0], [-1000000000, 13])
        assert result == [1000, 0], f"Test 109 failed: got {result}, expected {[1000, 0]}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = elementWiseModulo([999999999999], [1000000000])
        assert result == [999999999], f"Test 110 failed: got {result}, expected {[999999999]}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = elementWiseModulo([44], [1000000000])
        assert result == [44], f"Test 111 failed: got {result}, expected {[44]}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = elementWiseModulo([42, -42], [-1, 42])
        assert result == [0, 0], f"Test 112 failed: got {result}, expected {[0, 0]}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = elementWiseModulo([42, -42], [42, 200])
        assert result == [0, 158], f"Test 113 failed: got {result}, expected {[0, 158]}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = elementWiseModulo([1, -1, 0], [-2, 3, -4])
        assert result == [1, 2, 0], f"Test 114 failed: got {result}, expected {[1, 2, 0]}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = elementWiseModulo([100, 50, -50, -100], [9, -8, -7, -6])
        assert result == [1, 2, 6, 2], f"Test 115 failed: got {result}, expected {[1, 2, 6, 2]}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = elementWiseModulo([100, 50, -50, -100], [9, -8, 7, -6])
        assert result == [1, 2, 6, 2], f"Test 116 failed: got {result}, expected {[1, 2, 6, 2]}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = elementWiseModulo([100, 50, -50, -100], [12345678901234567890, -8, 7, -6])
        assert result == [100, 2, 6, 2], f"Test 117 failed: got {result}, expected {[100, 2, 6, 2]}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = elementWiseModulo([-100, -50, 50, 100], [29, 7, -8, 9])
        assert result == [16, 6, 2, 1], f"Test 118 failed: got {result}, expected {[16, 6, 2, 1]}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = elementWiseModulo([13, 27, 39, 65, 97], [-1, -1, -1, -1, -1])
        assert result == [0, 0, 0, 0, 0], f"Test 119 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = elementWiseModulo([13, -27, 39, 52, 65], [-1, -2, -1, -1, -1])
        assert result == [0, 1, 0, 0, 0], f"Test 120 failed: got {result}, expected {[0, 1, 0, 0, 0]}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = elementWiseModulo([1, 3, 5, 7, 9, 11], [12, 10, 8, 6, 4, 2])
        assert result == [1, 3, 5, 1, 1, 1], f"Test 121 failed: got {result}, expected {[1, 3, 5, 1, 1, 1]}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = elementWiseModulo([1, 3, 5, 7, 10, 11], [2, 4, 6, 8, 10, 12])
        assert result == [1, 3, 5, 7, 0, 11], f"Test 122 failed: got {result}, expected {[1, 3, 5, 7, 0, 11]}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = elementWiseModulo([1, 3, 5, 7, 9, 11], [2, 4, -11, 8, 10, 12])
        assert result == [1, 3, 5, 7, 9, 11], f"Test 123 failed: got {result}, expected {[1, 3, 5, 7, 9, 11]}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = elementWiseModulo([1, 3, 5, 7, 9, 11], [123456789, 12, 10, 8, 6, 4])
        assert result == [1, 3, 5, 7, 3, 3], f"Test 124 failed: got {result}, expected {[1, 3, 5, 7, 3, 3]}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = elementWiseModulo([-9, -18, -27, 0], [-4, -5, -6, 65])
        assert result == [3, 2, 3, 0], f"Test 125 failed: got {result}, expected {[3, 2, 3, 0]}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = elementWiseModulo([-2000, -27, -18], [-4, -5, -6])
        assert result == [0, 3, 0], f"Test 126 failed: got {result}, expected {[0, 3, 0]}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = elementWiseModulo([50, -18, -27], [-4, -5, -6])
        assert result == [2, 2, 3], f"Test 127 failed: got {result}, expected {[2, 2, 3]}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = elementWiseModulo([-27, -18, -7, 0], [-4, -5, -6, 24])
        assert result == [1, 2, 5, 0], f"Test 128 failed: got {result}, expected {[1, 2, 5, 0]}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = elementWiseModulo([0], [512])
        assert result == [0], f"Test 129 failed: got {result}, expected {[0]}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = elementWiseModulo([-1000, -2000], [513, 256])
        assert result == [26, 48], f"Test 130 failed: got {result}, expected {[26, 48]}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = elementWiseModulo([-2000, -1000], [256, 512])
        assert result == [48, 24], f"Test 131 failed: got {result}, expected {[48, 24]}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = elementWiseModulo([-1000, -2000], [256, -512])
        assert result == [24, 48], f"Test 132 failed: got {result}, expected {[24, 48]}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = elementWiseModulo([29, 23, 19, 17], [4, 6, 8, 10])
        assert result == [1, 5, 3, 7], f"Test 133 failed: got {result}, expected {[1, 5, 3, 7]}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = elementWiseModulo([17, 19, 24, 29], [10, 8, 6, 4])
        assert result == [7, 3, 0, 1], f"Test 134 failed: got {result}, expected {[7, 3, 0, 1]}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = elementWiseModulo([5, 5, 10, 5, 5], [6, 5, 4, 3, 2])
        assert result == [5, 0, 2, 2, 1], f"Test 135 failed: got {result}, expected {[5, 0, 2, 2, 1]}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = elementWiseModulo([26, 5, 5, 5], [2, 3, 5, 6])
        assert result == [0, 2, 0, 5], f"Test 136 failed: got {result}, expected {[0, 2, 0, 5]}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = elementWiseModulo([5, 5, 5, 5, 0], [2, 3, 4, 5, 6])
        assert result == [1, 2, 1, 0, 0], f"Test 137 failed: got {result}, expected {[1, 2, 1, 0, 0]}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = elementWiseModulo([84, 5, 5, 5, 5, 5], [1, 3, 4, 5, 6, 9223372036854775807])
        assert result == [0, 2, 1, 0, 5, 5], f"Test 138 failed: got {result}, expected {[0, 2, 1, 0, 5, 5]}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = elementWiseModulo([5, 5, 5, 5, 5], [-6, 5, 4, 3, 2])
        assert result == [5, 0, 1, 2, 1], f"Test 139 failed: got {result}, expected {[5, 0, 1, 2, 1]}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = elementWiseModulo([1, 2, 2, 3, 5, 8, 13], [2, 3, 5, 7, 11, 13, 17])
        assert result == [1, 2, 2, 3, 5, 8, 13], f"Test 140 failed: got {result}, expected {[1, 2, 2, 3, 5, 8, 13]}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = elementWiseModulo([1, 1, 2, 3, 5, 8, 13], [-2, 512, 5, 7, 11, 13, 17])
        assert result == [1, 1, 2, 3, 5, 8, 13], f"Test 141 failed: got {result}, expected {[1, 1, 2, 3, 5, 8, 13]}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = elementWiseModulo([1, 1, 2, 3, 5, 13, -20], [2, 3, 7, 12, 13, 17, 5])
        assert result == [1, 1, 2, 3, 5, 13, 0], f"Test 142 failed: got {result}, expected {[1, 1, 2, 3, 5, 13, 0]}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = elementWiseModulo([1, 52, 2, 3, 0, 8, 13], [2, 3, 5, 7, 11, 13, 17])
        assert result == [1, 1, 2, 3, 0, 8, 13], f"Test 143 failed: got {result}, expected {[1, 1, 2, 3, 0, 8, 13]}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = elementWiseModulo([-4, 13, 8, 5, 3, 2, 1], [2, 3, 18, 7, 11, 13, 17])
        assert result == [0, 1, 8, 5, 3, 2, 1], f"Test 144 failed: got {result}, expected {[0, 1, 8, 5, 3, 2, 1]}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = elementWiseModulo([2, 4, 16, -32, 64, 128, 256], [3, 5, 7, 11, 13, 15, 17])
        assert result == [2, 4, 2, 1, 12, 8, 1], f"Test 145 failed: got {result}, expected {[2, 4, 2, 1, 12, 8, 1]}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = elementWiseModulo([12, -24, 36, -48, 60, -72, 84, -96, 108, -120, 132, -144], [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, -113, -4])
        assert result == [2, 4, 0, 7, 8, 3, 16, 18, 3, 18, 19, 0], f"Test 146 failed: got {result}, expected {[2, 4, 0, 7, 8, 3, 16, 18, 3, 18, 19, 0]}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = elementWiseModulo([12, -24, 36, -48, 60, -72, 84, -96, 108, -120, 132, -144, -2000], [27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 51])
        assert result == [12, 1, 13, 15, 3, 13, 9, 8, 9, 6, 6, 1, 40], f"Test 147 failed: got {result}, expected {[12, 1, 13, 15, 3, 13, 9, 8, 9, 6, 6, 1, 40]}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = elementWiseModulo([0, 1], [2, 3])
        assert result == [0, 1], f"Test 148 failed: got {result}, expected {[0, 1]}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = elementWiseModulo([30, 0], [2, 3])
        assert result == [0, 0], f"Test 149 failed: got {result}, expected {[0, 0]}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = elementWiseModulo([1, 0], [3, 2])
        assert result == [1, 0], f"Test 150 failed: got {result}, expected {[1, 0]}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = elementWiseModulo([1, -2000], [3, 4])
        assert result == [1, 0], f"Test 151 failed: got {result}, expected {[1, 0]}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = elementWiseModulo([1, 0], [2, 3])
        assert result == [1, 0], f"Test 152 failed: got {result}, expected {[1, 0]}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = elementWiseModulo([9, 18], [-6, -22])
        assert result == [3, 18], f"Test 153 failed: got {result}, expected {[3, 18]}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = elementWiseModulo([9, 36], [3, 802])
        assert result == [0, 36], f"Test 154 failed: got {result}, expected {[0, 36]}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = elementWiseModulo([0], [1])
        assert result == [0], f"Test 155 failed: got {result}, expected {[0]}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = elementWiseModulo([-999999], [1])
        assert result == [0], f"Test 156 failed: got {result}, expected {[0]}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = elementWiseModulo([0, 19], [1, 54])
        assert result == [0, 19], f"Test 157 failed: got {result}, expected {[0, 19]}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = elementWiseModulo([28, 21, 14, 7], [1, 2, 3, -41])
        assert result == [0, 1, 2, 7], f"Test 158 failed: got {result}, expected {[0, 1, 2, 7]}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
