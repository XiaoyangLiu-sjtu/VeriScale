# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def arraySum(a, b):
2: ✓     return [x + y for x, y in zip(a, b)]
```

## Complete Test File

```python
def arraySum(a, b):
    return [x + y for x, y in zip(a, b)]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = arraySum([1, 2, 3], [4, 5, 6])
        assert result == [5, 7, 9], f"Test 1 failed: got {result}, expected {[5, 7, 9]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = arraySum([0, 0, 0], [0, 0, 0])
        assert result == [0, 0, 0], f"Test 2 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = arraySum([-1, 2, 3], [1, -2, 4])
        assert result == [0, 0, 7], f"Test 3 failed: got {result}, expected {[0, 0, 7]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = arraySum([10], [-10])
        assert result == [0], f"Test 4 failed: got {result}, expected {[0]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = arraySum([100, 200, 300], [100, 200, 300])
        assert result == [200, 400, 600], f"Test 5 failed: got {result}, expected {[200, 400, 600]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = arraySum([42], [-42])
        assert result == [0], f"Test 6 failed: got {result}, expected {[0]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = arraySum([1, 2], [3, 4])
        assert result == [4, 6], f"Test 7 failed: got {result}, expected {[4, 6]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = arraySum([-5, -10], [5, 10])
        assert result == [0, 0], f"Test 8 failed: got {result}, expected {[0, 0]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = arraySum([-1, 2, -3], [1, -2, 3])
        assert result == [0, 0, 0], f"Test 9 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = arraySum([1, 2, 3, 4], [10, 20, 30, 40])
        assert result == [11, 22, 33, 44], f"Test 10 failed: got {result}, expected {[11, 22, 33, 44]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = arraySum([9, 7, 5, 3], [-9, -7, -5, -3])
        assert result == [0, 0, 0, 0], f"Test 11 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = arraySum([1, -1, 1, -1, 1], [-1, 1, -1, 1, -1])
        assert result == [0, 0, 0, 0, 0], f"Test 12 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = arraySum([1000000, 2000000, 3000000, 4000000, 5000000], [-5000000, -4000000, -3000000, -2000000, -1000000])
        assert result == [-4000000, -2000000, 0, 2000000, 4000000], f"Test 13 failed: got {result}, expected {[-4000000, -2000000, 0, 2000000, 4000000]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = arraySum([13, -8, 0, 21, -34, 55], [-13, 8, 0, -21, 34, -55])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 14 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = arraySum([2, 3, 5, 7, 11, 13, 17], [19, 23, 29, 31, 37, 41, 43])
        assert result == [21, 26, 34, 38, 48, 54, 60], f"Test 15 failed: got {result}, expected {[21, 26, 34, 38, 48, 54, 60]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = arraySum([4, 4, 4, 4, 4, 4, 4, 4], [1, 2, 3, 4, 5, 6, 7, 8])
        assert result == [5, 6, 7, 8, 9, 10, 11, 12], f"Test 16 failed: got {result}, expected {[5, 6, 7, 8, 9, 10, 11, 12]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = arraySum([9223372036854775807], [-9223372036854775807])
        assert result == [0], f"Test 17 failed: got {result}, expected {[0]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = arraySum([-9223372036854775808], [9223372036854775808])
        assert result == [0], f"Test 18 failed: got {result}, expected {[0]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = arraySum([999999999999999999999, -999999999999999999999], [1, -1])
        assert result == [1000000000000000000000, -1000000000000000000000], f"Test 19 failed: got {result}, expected {[1000000000000000000000, -1000000000000000000000]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = arraySum([123456789012345678901234567890, -123456789012345678901234567890, 0], [-1, 1, 999999999999999999999999999999])
        assert result == [123456789012345678901234567889, -123456789012345678901234567889, 999999999999999999999999999999], f"Test 20 failed: got {result}, expected {[123456789012345678901234567889, -123456789012345678901234567889, 999999999999999999999999999999]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = arraySum([1, 1, 1, 1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 21 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = arraySum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        assert result == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], f"Test 22 failed: got {result}, expected {[9, 9, 9, 9, 9, 9, 9, 9, 9, 9]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = arraySum([7, 7, 7], [7, 7, 7])
        assert result == [14, 14, 14], f"Test 23 failed: got {result}, expected {[14, 14, 14]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = arraySum([9223372036854775807, -9223372036854775808, 3141592653589793, -2718281828459045], [1, -1, -3141592653589793, 2718281828459045])
        assert result == [9223372036854775808, -9223372036854775809, 0, 0], f"Test 24 failed: got {result}, expected {[9223372036854775808, -9223372036854775809, 0, 0]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = arraySum([-100, 0, 100, 200], [300, -200, 0, -100])
        assert result == [200, -200, 100, 100], f"Test 25 failed: got {result}, expected {[200, -200, 100, 100]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = arraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13], f"Test 26 failed: got {result}, expected {[13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = arraySum([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], [377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0])
        assert result == [377, 234, 145, 91, 58, 39, 29, 26, 29, 39, 58, 91, 145, 234, 377], f"Test 27 failed: got {result}, expected {[377, 234, 145, 91, 58, 39, 29, 26, 29, 39, 58, 91, 145, 234, 377]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = arraySum([0], [123456])
        assert result == [123456], f"Test 28 failed: got {result}, expected {[123456]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = arraySum([-2147483648, 2147483647], [2147483647, -2147483648])
        assert result == [-1, -1], f"Test 29 failed: got {result}, expected {[-1, -1]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = arraySum([5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5])
        assert result == [10, 10, 10, 10, 10, 10], f"Test 30 failed: got {result}, expected {[10, 10, 10, 10, 10, 10]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = arraySum([-3, -3, -3, -3, -3, -3], [9, 8, 7, 6, 5, 4])
        assert result == [6, 5, 4, 3, 2, 1], f"Test 31 failed: got {result}, expected {[6, 5, 4, 3, 2, 1]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = arraySum([100000000000000000000000000000000000000000000000000, -100000000000000000000000000000000000000000000000000, 42], [-99999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999, -42])
        assert result == [1, -1, 0], f"Test 32 failed: got {result}, expected {[1, -1, 0]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = arraySum([2, -4, 6, -8], [-2, 4, -6, 8])
        assert result == [0, 0, 0, 0], f"Test 33 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = arraySum([11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121], [-11, -22, -33, -44, -55, -66, -77, -88, -99, -110, -121])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 34 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = arraySum([1, 2, 3, 0], [4, 5, 6, 0])
        assert result == [5, 7, 9, 0], f"Test 35 failed: got {result}, expected {[5, 7, 9, 0]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = arraySum([0, -1, 0], [0, 0, 0])
        assert result == [0, -1, 0], f"Test 36 failed: got {result}, expected {[0, -1, 0]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = arraySum([0, 0, 0, 0], [0, 0, 0, 2000000])
        assert result == [0, 0, 0, 2000000], f"Test 37 failed: got {result}, expected {[0, 0, 0, 2000000]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = arraySum([0, 1, 0], [0, 0, 0])
        assert result == [0, 1, 0], f"Test 38 failed: got {result}, expected {[0, 1, 0]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = arraySum([0, 0, 23, 0], [0, 0, 0, 0])
        assert result == [0, 0, 23, 0], f"Test 39 failed: got {result}, expected {[0, 0, 23, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = arraySum([0, 0, 0, 0], [0, 0, 41, -1000000])
        assert result == [0, 0, 41, -1000000], f"Test 40 failed: got {result}, expected {[0, 0, 41, -1000000]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = arraySum([-1, 2, 0], [13, -2, 4])
        assert result == [12, 0, 4], f"Test 41 failed: got {result}, expected {[12, 0, 4]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = arraySum([-1, 2, 66], [-2, 5, 0])
        assert result == [-3, 7, 66], f"Test 42 failed: got {result}, expected {[-3, 7, 66]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = arraySum([-1, 41, 2], [4, -2, 1])
        assert result == [3, 39, 3], f"Test 43 failed: got {result}, expected {[3, 39, 3]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = arraySum([10, 0], [-10, 999999999999999999999999999999])
        assert result == [0, 999999999999999999999999999999], f"Test 44 failed: got {result}, expected {[0, 999999999999999999999999999999]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = arraySum([10, 0], [-10, -66])
        assert result == [0, -66], f"Test 45 failed: got {result}, expected {[0, -66]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = arraySum([10], [0])
        assert result == [10], f"Test 46 failed: got {result}, expected {[10]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = arraySum([10, 0], [0, -10])
        assert result == [10, -10], f"Test 47 failed: got {result}, expected {[10, -10]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = arraySum([10, 0], [-10, 0])
        assert result == [0, 0], f"Test 48 failed: got {result}, expected {[0, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = arraySum([300, 100, 0], [100, 200, 300])
        assert result == [400, 300, 300], f"Test 49 failed: got {result}, expected {[400, 300, 300]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = arraySum([2, 200, 300], [100, 200, 300])
        assert result == [102, 400, 600], f"Test 50 failed: got {result}, expected {[102, 400, 600]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = arraySum([0, 200, 300], [100, 200, 300])
        assert result == [100, 400, 600], f"Test 51 failed: got {result}, expected {[100, 400, 600]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = arraySum([200, 300], [300, -999999999999999999])
        assert result == [500, -999999999999999699], f"Test 52 failed: got {result}, expected {[500, -999999999999999699]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = arraySum([300, 31], [99999999999999999999999999999999999999999999999999, 200])
        assert result == [100000000000000000000000000000000000000000000000299, 231], f"Test 53 failed: got {result}, expected {[100000000000000000000000000000000000000000000000299, 231]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = arraySum([1, 2, 0, 5], [6, 7, 6, 5])
        assert result == [7, 9, 6, 10], f"Test 54 failed: got {result}, expected {[7, 9, 6, 10]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = arraySum([4, 3, 2], [-66, 6, 7])
        assert result == [-62, 9, 9], f"Test 55 failed: got {result}, expected {[-62, 9, 9]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = arraySum([4, 3, 1], [7, 8, 5])
        assert result == [11, 11, 6], f"Test 56 failed: got {result}, expected {[11, 11, 6]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = arraySum([-5000000], [0])
        assert result == [-5000000], f"Test 57 failed: got {result}, expected {[-5000000]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = arraySum([0, 0], [0, 0])
        assert result == [0, 0], f"Test 58 failed: got {result}, expected {[0, 0]}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = arraySum([41], [0])
        assert result == [41], f"Test 59 failed: got {result}, expected {[41]}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = arraySum([42], [-43])
        assert result == [-1], f"Test 60 failed: got {result}, expected {[-1]}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = arraySum([42, 0], [-42, 100])
        assert result == [0, 100], f"Test 61 failed: got {result}, expected {[0, 100]}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = arraySum([42, 42], [-41, 0])
        assert result == [1, 42], f"Test 62 failed: got {result}, expected {[1, 42]}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = arraySum([-1, 0], [4, 4])
        assert result == [3, 4], f"Test 63 failed: got {result}, expected {[3, 4]}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = arraySum([2, 0], [4, 9])
        assert result == [6, 9], f"Test 64 failed: got {result}, expected {[6, 9]}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = arraySum([9223372036854775807, 2], [3, 4])
        assert result == [9223372036854775810, 6], f"Test 65 failed: got {result}, expected {[9223372036854775810, 6]}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = arraySum([2, 0], [3, -42])
        assert result == [5, -42], f"Test 66 failed: got {result}, expected {[5, -42]}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = arraySum([1, 4], [-4, 3])
        assert result == [-3, 7], f"Test 67 failed: got {result}, expected {[-3, 7]}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = arraySum([1, 2, 0], [3, 4, 20])
        assert result == [4, 6, 20], f"Test 68 failed: got {result}, expected {[4, 6, 20]}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = arraySum([-10, -5], [5, 9])
        assert result == [-5, 4], f"Test 69 failed: got {result}, expected {[-5, 4]}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = arraySum([-5], [10])
        assert result == [5], f"Test 70 failed: got {result}, expected {[5]}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = arraySum([-5, -10], [233, 10])
        assert result == [228, 0], f"Test 71 failed: got {result}, expected {[228, 0]}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = arraySum([-10, -5], [10, 10])
        assert result == [0, 5], f"Test 72 failed: got {result}, expected {[0, 5]}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = arraySum([-5, 0], [5, 10])
        assert result == [0, 10], f"Test 73 failed: got {result}, expected {[0, 10]}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = arraySum([-5, -10], [10, 5])
        assert result == [5, -5], f"Test 74 failed: got {result}, expected {[5, -5]}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = arraySum([-8, -10], [10, 5])
        assert result == [2, -5], f"Test 75 failed: got {result}, expected {[2, -5]}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = arraySum([-1, 3, -3], [1, -2, 3])
        assert result == [0, 1, 0], f"Test 76 failed: got {result}, expected {[0, 1, 0]}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = arraySum([-1, 0], [-2, 3])
        assert result == [-3, 3], f"Test 77 failed: got {result}, expected {[-3, 3]}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = arraySum([-1, 2, -3], [1, -2, 0])
        assert result == [0, 0, -3], f"Test 78 failed: got {result}, expected {[0, 0, -3]}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = arraySum([-1, 1], [3, -2])
        assert result == [2, -1], f"Test 79 failed: got {result}, expected {[2, -1]}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = arraySum([-1, 2, -3], [1, -2, 12])
        assert result == [0, 0, 9], f"Test 80 failed: got {result}, expected {[0, 0, 9]}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = arraySum([-1, 1, 0], [3, -2, 1])
        assert result == [2, -1, 1], f"Test 81 failed: got {result}, expected {[2, -1, 1]}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = arraySum([1000000, -3, 2, -1], [3, -2, 1, 0])
        assert result == [1000003, -5, 3, -1], f"Test 82 failed: got {result}, expected {[1000003, -5, 3, -1]}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = arraySum([4, 0, 2, 1], [30, 20, 10, 70])
        assert result == [34, 20, 12, 71], f"Test 83 failed: got {result}, expected {[34, 20, 12, 71]}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = arraySum([4, 3, 2, 1], [10, 20, 30, 40])
        assert result == [14, 23, 32, 41], f"Test 84 failed: got {result}, expected {[14, 23, 32, 41]}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = arraySum([1, 2, 3, 41], [40, 30, 20, 378])
        assert result == [41, 32, 23, 419], f"Test 85 failed: got {result}, expected {[41, 32, 23, 419]}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = arraySum([66, 2, 3, 4, 12], [10, 20, 40, 29, 0])
        assert result == [76, 22, 43, 33, 12], f"Test 86 failed: got {result}, expected {[76, 22, 43, 33, 12]}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = arraySum([-1, 3, 5, 7, 9], [-9, -7, -5, -3, -10])
        assert result == [-10, -4, 0, 4, -1], f"Test 87 failed: got {result}, expected {[-10, -4, 0, 4, -1]}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = arraySum([3, 5, 7, 9], [-3, -5, 300, -9])
        assert result == [0, 0, 307, 0], f"Test 88 failed: got {result}, expected {[0, 0, 307, 0]}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = arraySum([3, 5, 7, 9], [-9, -7, -5, -3])
        assert result == [-6, -2, 2, 6], f"Test 89 failed: got {result}, expected {[-6, -2, 2, 6]}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = arraySum([1, -1, 1, 0, 1], [-1, 1, 1, 1, -1])
        assert result == [0, 0, 2, 1, 0], f"Test 90 failed: got {result}, expected {[0, 0, 2, 1, 0]}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = arraySum([1, -1, 1, -1, 1, -66, 0], [-1, 1, -1, 1, -1, 0, 0])
        assert result == [0, 0, 0, 0, 0, -66, 0], f"Test 91 failed: got {result}, expected {[0, 0, 0, 0, 0, -66, 0]}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = arraySum([0, -1, 1, -1, 378, 30], [-1, 1, -1, 1, -1, 43])
        assert result == [-1, 0, 0, 0, 377, 73], f"Test 92 failed: got {result}, expected {[-1, 0, 0, 0, 377, 73]}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = arraySum([1, -1, 1, 0, 1], [-1, 1, -1, 1, -1])
        assert result == [0, 0, 0, 1, 0], f"Test 93 failed: got {result}, expected {[0, 0, 0, 1, 0]}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = arraySum([1, -1, 1, -1, 1, 999999999999999999], [-1, 1, -1, 1, -1, -11])
        assert result == [0, 0, 0, 0, 0, 999999999999999988], f"Test 94 failed: got {result}, expected {[0, 0, 0, 0, 0, 999999999999999988]}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = arraySum([0, 1, -1, 1, -1, 1], [1, -1, 1, -1, 0, 55])
        assert result == [1, 0, 0, 0, -1, 56], f"Test 95 failed: got {result}, expected {[1, 0, 0, 0, -1, 56]}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = arraySum([1000000, 2000000, 3000000, 4000000, 5000000], [-1000000, -2000000, -3000000, -4000000, -5000000])
        assert result == [0, 0, 0, 0, 0], f"Test 96 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = arraySum([1000000, 2000000, 3000000, 4000000, 5000000], [-5000000, -4000000, -3000000, -1000000, 3141592653589793])
        assert result == [-4000000, -2000000, 0, 3000000, 3141592658589793], f"Test 97 failed: got {result}, expected {[-4000000, -2000000, 0, 3000000, 3141592658589793]}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = arraySum([5000000, 4000000, 3000000, 2000000, 1000000], [0, -1000000, -2000000, -4000000, -5000000])
        assert result == [5000000, 3000000, 1000000, -2000000, -4000000], f"Test 98 failed: got {result}, expected {[5000000, 3000000, 1000000, -2000000, -4000000]}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = arraySum([5000000, 4000000, 3000000, 1000000], [-5000000, -3000000, -2000000, 0])
        assert result == [0, 1000000, 1000000, 1000000], f"Test 99 failed: got {result}, expected {[0, 1000000, 1000000, 1000000]}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = arraySum([999999, 2000000, 3000000, 4000000, 5000000], [-5000000, -4000000, -3000000, -2000000, -1000000])
        assert result == [-4000001, -2000000, 0, 2000000, 4000000], f"Test 100 failed: got {result}, expected {[-4000001, -2000000, 0, 2000000, 4000000]}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = arraySum([0, 55, -34, 21, 999999999999999999999, -8, 13], [-13, 8, 0, -21, 34, -55, 999999999999999999999])
        assert result == [-13, 63, -34, 0, 1000000000000000000033, -63, 1000000000000000000012], f"Test 101 failed: got {result}, expected {[-13, 63, -34, 0, 1000000000000000000033, -63, 1000000000000000000012]}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = arraySum([13, -8, 0, 21, -34, 55], [4000000, 34, -21, 0, 8, -13])
        assert result == [4000013, 26, -21, 21, -26, 42], f"Test 102 failed: got {result}, expected {[4000013, 26, -21, 21, -26, 42]}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = arraySum([13, -8, 0, 21, -34, 55], [-55, 34, -21, 0, 8, -13])
        assert result == [-42, 26, -21, 21, -26, 42], f"Test 103 failed: got {result}, expected {[-42, 26, -21, 21, -26, 42]}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = arraySum([13, 0, 0, 21, -34, 55], [-13, 8, 0, -21, 34, -55])
        assert result == [0, 8, 0, 0, 0, 0], f"Test 104 failed: got {result}, expected {[0, 8, 0, 0, 0, 0]}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = arraySum([55, 13, -8, 0, 21, -34, 55], [-13, 8, 0, -21, 34, -55, 0])
        assert result == [42, 21, -8, -21, 55, -89, 55], f"Test 105 failed: got {result}, expected {[42, 21, -8, -21, 55, -89, 55]}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = arraySum([55, -34, 21, 0, -8, 13], [-13, 8, 0, -21, 34, 0])
        assert result == [42, -26, 21, -21, 26, 13], f"Test 106 failed: got {result}, expected {[42, -26, 21, -21, 26, 13]}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = arraySum([17, 13, 11, 7, 5, 3, 2], [43, 41, 37, 31, 29, 23, 19])
        assert result == [60, 54, 48, 38, 34, 26, 21], f"Test 107 failed: got {result}, expected {[60, 54, 48, 38, 34, 26, 21]}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = arraySum([17, 13, 11, 7, 5, 3, 2], [19, 23, 29, 31, 37, 41, 43])
        assert result == [36, 36, 40, 38, 42, 44, 45], f"Test 108 failed: got {result}, expected {[36, 36, 40, 38, 42, 44, 45]}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = arraySum([29, 17, 11, 7, 5, 3, 2], [43, 41, 37, 31, -20, 23, 19])
        assert result == [72, 58, 48, 38, -15, 26, 21], f"Test 109 failed: got {result}, expected {[72, 58, 48, 38, -15, 26, 21]}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = arraySum([2, 3, 5, 7, 11, 13, 17], [43, 41, 37, 31, 29, 23, 19])
        assert result == [45, 44, 42, 38, 40, 36, 36], f"Test 110 failed: got {result}, expected {[45, 44, 42, 38, 40, 36, 36]}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = arraySum([4, 4, 4, 4, 4, 4, 4, 4, 60], [1, 2, 3, 4, 5, 6, 7, 8, 0])
        assert result == [5, 6, 7, 8, 9, 10, 11, 12, 60], f"Test 111 failed: got {result}, expected {[5, 6, 7, 8, 9, 10, 11, 12, 60]}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = arraySum([4, 4, 4, 4, 4, 4, 4, 4, -2718281828459045], [1, 2, 3, 4, 5, 6, 7, 8, 0])
        assert result == [5, 6, 7, 8, 9, 10, 11, 12, -2718281828459045], f"Test 112 failed: got {result}, expected {[5, 6, 7, 8, 9, 10, 11, 12, -2718281828459045]}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = arraySum([4, 4, 4, 4, 4, 4, 4, 4], [1, 2, 3, -68, 5, 6, 7, 8])
        assert result == [5, 6, 7, -64, 9, 10, 11, 12], f"Test 113 failed: got {result}, expected {[5, 6, 7, -64, 9, 10, 11, 12]}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = arraySum([4, 4, 4, 4, 4, 4, 4, 4, -1], [1, 2, 3, 4, -5, 6, 7, 8, 0])
        assert result == [5, 6, 7, 8, -1, 10, 11, 12, -1], f"Test 114 failed: got {result}, expected {[5, 6, 7, 8, -1, 10, 11, 12, -1]}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = arraySum([4, 4, 4, 4, 4, 4, 4, 4, -99999999999999999999999999999999999999999999999999], [1, 2, 3, 4, 5, 6, 7, 8, -1000000])
        assert result == [5, 6, 7, 8, 9, 10, 11, 12, -100000000000000000000000000000000000000000000999999], f"Test 115 failed: got {result}, expected {[5, 6, 7, 8, 9, 10, 11, 12, -100000000000000000000000000000000000000000000999999]}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = arraySum([9223372036854775807], [999999])
        assert result == [9223372036855775806], f"Test 116 failed: got {result}, expected {[9223372036855775806]}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = arraySum([0], [-9223372036854775807])
        assert result == [-9223372036854775807], f"Test 117 failed: got {result}, expected {[-9223372036854775807]}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = arraySum([9223372036854775806], [-9223372036854775808])
        assert result == [-2], f"Test 118 failed: got {result}, expected {[-2]}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = arraySum([-9223372036854775807], [-9223372036854775807])
        assert result == [-18446744073709551614], f"Test 119 failed: got {result}, expected {[-18446744073709551614]}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = arraySum([9223372036854775807, 0], [-9223372036854775807, 42])
        assert result == [0, 42], f"Test 120 failed: got {result}, expected {[0, 42]}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = arraySum([9223372036854775807], [0])
        assert result == [9223372036854775807], f"Test 121 failed: got {result}, expected {[9223372036854775807]}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = arraySum([98], [4999998])
        assert result == [5000096], f"Test 122 failed: got {result}, expected {[5000096]}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = arraySum([-18446744073709551616], [9223372036854775808])
        assert result == [-9223372036854775808], f"Test 123 failed: got {result}, expected {[-9223372036854775808]}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = arraySum([-9223372036854775808], [9223372036854775807])
        assert result == [-1], f"Test 124 failed: got {result}, expected {[-1]}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = arraySum([-9223372036854775808], [0])
        assert result == [-9223372036854775808], f"Test 125 failed: got {result}, expected {[-9223372036854775808]}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = arraySum([999999999999999999999, -999999999999999999999, -99], [1, -1, 0])
        assert result == [1000000000000000000000, -1000000000000000000000, -99], f"Test 126 failed: got {result}, expected {[1000000000000000000000, -1000000000000000000000, -99]}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = arraySum([999999999999999999999, -999999999999999999999], [-1, 1])
        assert result == [999999999999999999998, -999999999999999999998], f"Test 127 failed: got {result}, expected {[999999999999999999998, -999999999999999999998]}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = arraySum([-999999999999999999999, 999999999999999999999, -3141592653589793], [-1, 1, -100])
        assert result == [-1000000000000000000000, 1000000000000000000000, -3141592653589893], f"Test 128 failed: got {result}, expected {[-1000000000000000000000, 1000000000000000000000, -3141592653589893]}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = arraySum([99, -123456789012345678901234567890, 123456789012345678901234567890, 0], [-1, 1, -999999999999999999999999999999, -2])
        assert result == [98, -123456789012345678901234567889, -876543210987654321098765432109, -2], f"Test 129 failed: got {result}, expected {[98, -123456789012345678901234567889, -876543210987654321098765432109, -2]}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = arraySum([123456789012345678901234567890, -123456789012345678901234567890, 0], [-1, 0, 999999999999999999999999999999])
        assert result == [123456789012345678901234567889, -123456789012345678901234567890, 999999999999999999999999999999], f"Test 130 failed: got {result}, expected {[123456789012345678901234567889, -123456789012345678901234567890, 999999999999999999999999999999]}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = arraySum([123456789012345678901234567890, -123456789012345678901234567890, 0, 0], [-1, 1, 999999999999999999999999999999, 0])
        assert result == [123456789012345678901234567889, -123456789012345678901234567889, 999999999999999999999999999999, 0], f"Test 131 failed: got {result}, expected {[123456789012345678901234567889, -123456789012345678901234567889, 999999999999999999999999999999, 0]}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = arraySum([0, -123456789012345678901234567890, 123456789012345678901234567890], [-1, 1, 999999999999999999999999999999])
        assert result == [-1, -123456789012345678901234567889, 1123456789012345678901234567889], f"Test 132 failed: got {result}, expected {[-1, -123456789012345678901234567889, 1123456789012345678901234567889]}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = arraySum([123456789012345678901234567890, 0], [1, 999999999999999999999999999999])
        assert result == [123456789012345678901234567891, 999999999999999999999999999999], f"Test 133 failed: got {result}, expected {[123456789012345678901234567891, 999999999999999999999999999999]}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = arraySum([1, 1, 1, 1, -5000000, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert result == [0, 0, 0, 0, -5000001, 0, 0, 0, 0], f"Test 134 failed: got {result}, expected {[0, 0, 0, 0, -5000001, 0, 0, 0, 0]}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = arraySum([1, 1, 1, 1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1, -1, -1, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 1], f"Test 135 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 1]}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = arraySum([1, 1, 1, 1, 1, 9223372036854775808, 0, 1, 1], [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert result == [0, 0, 0, 0, 0, 9223372036854775807, -1, 0, 0], f"Test 136 failed: got {result}, expected {[0, 0, 0, 0, 0, 9223372036854775807, -1, 0, 0]}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = arraySum([1, 1, 1, 1, 1, 1, 1, 1, 1, 999999], [-1, -1, -1, -1, -1, -1, -1, -2, -1, 22])
        assert result == [0, 0, 0, 0, 0, 0, 0, -1, 0, 1000021], f"Test 137 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, -1, 0, 1000021]}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = arraySum([1, 1, 1, 1, 1, 1, 1, 1, 1, 22], [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0, 22], f"Test 138 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0, 22]}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = arraySum([0, 1, 2, 3, 4, 5, 6, 6, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert result == [0, 2, 4, 6, 8, 10, 12, 13, 16, 18], f"Test 139 failed: got {result}, expected {[0, 2, 4, 6, 8, 10, 12, 13, 16, 18]}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = arraySum([7, -121], [7, 7])
        assert result == [14, -114], f"Test 140 failed: got {result}, expected {[14, -114]}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = arraySum([7, 7, 7], [7, 7, 8])
        assert result == [14, 14, 15], f"Test 141 failed: got {result}, expected {[14, 14, 15]}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = arraySum([7, 7, 7], [7, 7, 7])
        assert result == [14, 14, 14], f"Test 142 failed: got {result}, expected {[14, 14, 14]}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = arraySum([18446744073709551614, 8, 7, 0], [0, 7, 7, 7])
        assert result == [18446744073709551614, 15, 14, 7], f"Test 143 failed: got {result}, expected {[18446744073709551614, 15, 14, 7]}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = arraySum([-2718281828459045, 3141592653589793, -9223372036854775808, 9223372036854775807], [1, -1, 3141592653589793, 2718281828459045])
        assert result == [-2718281828459044, 3141592653589792, -9220230444201186015, 9226090318683234852], f"Test 144 failed: got {result}, expected {[-2718281828459044, 3141592653589792, -9220230444201186015, 9226090318683234852]}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = arraySum([-2718281828459045, 3141592653589793, -9223372036854775808, 9223372036854775807], [1, -1, -3141592653589793, 2718281828459045])
        assert result == [-2718281828459044, 3141592653589792, -9226513629508365601, 9226090318683234852], f"Test 145 failed: got {result}, expected {[-2718281828459044, 3141592653589792, -9226513629508365601, 9226090318683234852]}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = arraySum([-2718281828459045, 3141592653589793, -9223372036854775808, 9223372036854775807], [300, -1, -3141592653589793, 2718281828459045])
        assert result == [-2718281828458745, 3141592653589792, -9226513629508365601, 9226090318683234852], f"Test 146 failed: got {result}, expected {[-2718281828458745, 3141592653589792, -9226513629508365601, 9226090318683234852]}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = arraySum([-100, 0, 100, 200], [34, 0, -200, 300])
        assert result == [-66, 0, -100, 500], f"Test 147 failed: got {result}, expected {[-66, 0, -100, 500]}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = arraySum([200, 100, 0, -100, 0, 0], [300, -200, 0, -100, 0, 0])
        assert result == [500, -100, 0, -200, 0, 0], f"Test 148 failed: got {result}, expected {[500, -100, 0, -200, 0, 0]}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = arraySum([-100, 0, 100, 200, 29], [300, -200, 0, -100, 0])
        assert result == [200, -200, 100, 100, 29], f"Test 149 failed: got {result}, expected {[200, -200, 100, 100, 29]}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = arraySum([-100, 0, 100, -1000001], [0, -100, 0, 300])
        assert result == [-100, -100, 100, -999701], f"Test 150 failed: got {result}, expected {[-100, -100, 100, -999701]}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = arraySum([-100, 0, 100, -2147483648, 0], [0, -100, 1, -200, 300])
        assert result == [-100, -100, 101, -2147483848, 300], f"Test 151 failed: got {result}, expected {[-100, -100, 101, -2147483848, 300]}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = arraySum([-100, 0, 100, 200, -4000000], [300, -200, 0, -100, 0])
        assert result == [200, -200, 100, 100, -4000000], f"Test 152 failed: got {result}, expected {[200, -200, 100, 100, -4000000]}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = arraySum([-100, 1, 100, 123456789012345678901234567890], [300, -200, 0, -100])
        assert result == [200, -199, 100, 123456789012345678901234567790], f"Test 153 failed: got {result}, expected {[200, -199, 100, 123456789012345678901234567790]}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = arraySum([-100, 0, 100, 200], [-100, 0, -200, 300])
        assert result == [-200, 0, -100, 500], f"Test 154 failed: got {result}, expected {[-200, 0, -100, 500]}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = arraySum([12, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [24, 11, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2], f"Test 155 failed: got {result}, expected {[24, 11, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = arraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -99999999999999999999999999999999999999999999999999], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 4000000])
        assert result == [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, -99999999999999999999999999999999999999999995999999], f"Test 156 failed: got {result}, expected {[13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, -99999999999999999999999999999999999999999995999999]}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = arraySum([-99999999999999999999999999999999999999999999999999, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 0], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [-99999999999999999999999999999999999999999999999987, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 1], f"Test 157 failed: got {result}, expected {[-99999999999999999999999999999999999999999999999987, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 1]}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = arraySum([1, 2, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        assert result == [13, 13, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 0], f"Test 158 failed: got {result}, expected {[13, 13, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 0]}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = arraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [12, 11, 10, 9, -4, 7, 6, 5, 4, 3, 2, 1])
        assert result == [13, 13, 13, 13, 1, 13, 13, 13, 13, 13, 13, 13], f"Test 159 failed: got {result}, expected {[13, 13, 13, 13, 1, 13, 13, 13, 13, 13, 13, 13]}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = arraySum([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], [4999998, 0, 1, 1, 2, 3, 5, 8, 13, 34, 55, 89, 144, 233, 377])
        assert result == [4999998, 1, 2, 3, 5, 8, 13, 21, 34, 68, 110, 178, 288, 466, 754], f"Test 160 failed: got {result}, expected {[4999998, 1, 2, 3, 5, 8, 13, 21, 34, 68, 110, 178, 288, 466, 754]}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = arraySum([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])
        assert result == [0, 2, 2, 4, 6, 10, 16, 26, 42, 68, 110, 178, 288, 466, 754], f"Test 161 failed: got {result}, expected {[0, 2, 2, 4, 6, 10, 16, 26, 42, 68, 110, 178, 288, 466, 754]}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = arraySum([0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 144, 233, 377, -5436563656918090], [377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0])
        assert result == [377, 234, 145, 91, 58, 39, 29, 26, 29, 60, 92, 146, 234, 378, -5436563656918090], f"Test 162 failed: got {result}, expected {[377, 234, 145, 91, 58, 39, 29, 26, 29, 60, 92, 146, 234, 378, -5436563656918090]}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = arraySum([1000000], [123456])
        assert result == [1123456], f"Test 163 failed: got {result}, expected {[1123456]}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = arraySum([-3, 0], [123456, 22])
        assert result == [123453, 22], f"Test 164 failed: got {result}, expected {[123453, 22]}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = arraySum([0], [123457])
        assert result == [123457], f"Test 165 failed: got {result}, expected {[123457]}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = arraySum([0, 0], [123456, 0])
        assert result == [123456, 0], f"Test 166 failed: got {result}, expected {[123456, 0]}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = arraySum([2147483647, -2147483648], [2147483647, -2147483648])
        assert result == [4294967294, -4294967296], f"Test 167 failed: got {result}, expected {[4294967294, -4294967296]}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = arraySum([0, 2147483647, -2147483648], [2147483647, -2147483648, 0])
        assert result == [2147483647, -1, -2147483648], f"Test 168 failed: got {result}, expected {[2147483647, -1, -2147483648]}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = arraySum([5, 5, 5, 5, 5, 99], [5, 5, 5, 5, 5, 5])
        assert result == [10, 10, 10, 10, 10, 104], f"Test 169 failed: got {result}, expected {[10, 10, 10, 10, 10, 104]}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = arraySum([5, 0, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5])
        assert result == [10, 5, 10, 10, 10, 10], f"Test 170 failed: got {result}, expected {[10, 5, 10, 10, 10, 10]}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = arraySum([5, 5, 5, 5, 5, 5], [5, 5, 6, 5, 5, 0])
        assert result == [10, 10, 11, 10, 10, 5], f"Test 171 failed: got {result}, expected {[10, 10, 11, 10, 10, 5]}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = arraySum([5, 5, 5, 5, 5, 5, 4999998], [89, 5, 5, 0, 5, 5, 0])
        assert result == [94, 10, 10, 5, 10, 10, 4999998], f"Test 172 failed: got {result}, expected {[94, 10, 10, 5, 10, 10, 4999998]}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = arraySum([5, 5, 5, 6, 5, 5], [5, 5, 5, 5, 5, 5])
        assert result == [10, 10, 10, 11, 10, 10], f"Test 173 failed: got {result}, expected {[10, 10, 10, 11, 10, 10]}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = arraySum([10, 5, 6, 5, 5, 5, -9], [121, 5, 5, 5, 5, 5, 5])
        assert result == [131, 10, 11, 10, 10, 10, -4], f"Test 174 failed: got {result}, expected {[131, 10, 11, 10, 10, 10, -4]}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = arraySum([-3, -3, -3, -5436563656918090, -3, -3, 23], [9, 8, 7, 6, 5, 4, -999999])
        assert result == [6, 5, 4, -5436563656918084, 2, 1, -999976], f"Test 175 failed: got {result}, expected {[6, 5, 4, -5436563656918084, 2, 1, -999976]}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = arraySum([-3, -3, -1, -3, -3], [9, 8, 7, 5, 4])
        assert result == [6, 5, 6, 2, 1], f"Test 176 failed: got {result}, expected {[6, 5, 6, 2, 1]}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = arraySum([2000000, -3, -3, -3, -3, -3, -3], [8, 8, 7, 6, 5, 4, 8])
        assert result == [2000008, 5, 4, 3, 2, 1, 5], f"Test 177 failed: got {result}, expected {[2000008, 5, 4, 3, 2, 1, 5]}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = arraySum([-3, -3, -3, -3, -3, -3], [4, -5, 6, 7, 8, 9])
        assert result == [1, -8, 3, 4, 5, 6], f"Test 178 failed: got {result}, expected {[1, -8, 3, 4, 5, 6]}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = arraySum([-3, -6, -3, -3, -3, -3], [9, 8, 7, 6, 5, 4])
        assert result == [6, 2, 4, 3, 2, 1], f"Test 179 failed: got {result}, expected {[6, 2, 4, 3, 2, 1]}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = arraySum([100000000000000000000000000000000000000000000000000, -100000000000000000000000000000000000000000000000000, 42], [-23, 99999999999999999999999999999999999999999999999999, -42])
        assert result == [99999999999999999999999999999999999999999999999977, -1, 0], f"Test 180 failed: got {result}, expected {[99999999999999999999999999999999999999999999999977, -1, 0]}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = arraySum([100000000000000000000000000000000000000000000000000, -100000000000000000000000000000000000000000000000000, -33], [-99999999999999999999999999999999999999999999999999, -41, 5])
        assert result == [1, -100000000000000000000000000000000000000000000000041, -28], f"Test 181 failed: got {result}, expected {[1, -100000000000000000000000000000000000000000000000041, -28]}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = arraySum([6283185307179586, -100000000000000000000000000000000000000000000000000, 0], [-99999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999, -42])
        assert result == [-99999999999999999999999999999999993716814692820413, -1, -42], f"Test 182 failed: got {result}, expected {[-99999999999999999999999999999999993716814692820413, -1, -42]}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = arraySum([-33, 42, -100000000000000000000000000000000000000000000000000], [-99999999999999999999999999999999999999999999999999, 16, -42])
        assert result == [-100000000000000000000000000000000000000000000000032, 58, -100000000000000000000000000000000000000000000000042], f"Test 183 failed: got {result}, expected {[-100000000000000000000000000000000000000000000000032, 58, -100000000000000000000000000000000000000000000000042]}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = arraySum([100000000000000000000000000000000000000000000000000, -100000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000, 0], [-99999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999, -42, 0])
        assert result == [1, -1, 99999999999999999999999999999999999999999999999958, 0], f"Test 184 failed: got {result}, expected {[1, -1, 99999999999999999999999999999999999999999999999958, 0]}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = arraySum([100000000000000000000000000000000000000000000000000, -100000000000000000000000000000000000000000000000000, 42, 0], [-99999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999, -42, 0])
        assert result == [1, -1, 0, 0], f"Test 185 failed: got {result}, expected {[1, -1, 0, 0]}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = arraySum([-8, 6, -4, 2, 70], [-2, 4, -6, 8, 0])
        assert result == [-10, 10, -10, 10, 70], f"Test 186 failed: got {result}, expected {[-10, 10, -10, 10, 70]}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = arraySum([2, -4, 6, -8, -9], [-2, 4, -6, 8, 0])
        assert result == [0, 0, 0, 0, -9], f"Test 187 failed: got {result}, expected {[0, 0, 0, 0, -9]}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = arraySum([11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 6283185307179586], [-121, -110, -99, -88, -77, -66, -55, -44, -33, -22, -11, 70])
        assert result == [-110, -88, -66, -44, -22, 0, 22, 44, 66, 88, 110, 6283185307179656], f"Test 188 failed: got {result}, expected {[-110, -88, -66, -44, -22, 0, 22, 44, 66, 88, 110, 6283185307179656]}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = arraySum([0], [1])
        assert result == [1], f"Test 189 failed: got {result}, expected {[1]}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = arraySum([0, 41], [2, 0])
        assert result == [2, 41], f"Test 190 failed: got {result}, expected {[2, 41]}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = arraySum([0, -2147483648], [0, 0])
        assert result == [0, -2147483648], f"Test 191 failed: got {result}, expected {[0, -2147483648]}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = arraySum([0, 0], [2, 34])
        assert result == [2, 34], f"Test 192 failed: got {result}, expected {[2, 34]}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = arraySum([33], [1])
        assert result == [34], f"Test 193 failed: got {result}, expected {[34]}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = arraySum([1], [0])
        assert result == [1], f"Test 194 failed: got {result}, expected {[1]}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = arraySum([9, 5000000], [0, 0])
        assert result == [9, 5000000], f"Test 195 failed: got {result}, expected {[9, 5000000]}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = arraySum([1], [50])
        assert result == [51], f"Test 196 failed: got {result}, expected {[51]}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = arraySum([16, 1], [12, 0])
        assert result == [28, 1], f"Test 197 failed: got {result}, expected {[28, 1]}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = arraySum([1], [2])
        assert result == [3], f"Test 198 failed: got {result}, expected {[3]}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = arraySum([1, 0], [2, 1])
        assert result == [3, 1], f"Test 199 failed: got {result}, expected {[3, 1]}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = arraySum([1], [1])
        assert result == [2], f"Test 200 failed: got {result}, expected {[2]}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = arraySum([1, 40], [1, 2])
        assert result == [2, 42], f"Test 201 failed: got {result}, expected {[2, 42]}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = arraySum([1, 2, 3], [4, 5, 0])
        assert result == [5, 7, 3], f"Test 202 failed: got {result}, expected {[5, 7, 3]}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = arraySum([1, 2, 2], [0, 4, 0])
        assert result == [1, 6, 2], f"Test 203 failed: got {result}, expected {[1, 6, 2]}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = arraySum([1, 2, 3], [5, 4, -1000001])
        assert result == [6, 6, -999998], f"Test 204 failed: got {result}, expected {[6, 6, -999998]}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = arraySum([-1, -2, -3, -4, -5, 0], [5, 4, 3, 2, 1, 0])
        assert result == [4, 2, 0, -2, -4, 0], f"Test 205 failed: got {result}, expected {[4, 2, 0, -2, -4, 0]}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = arraySum([-1, -2, -3, -4, -5, 0, -99999999999999999999999999999999999999999999999999], [5, 4, 3, 2, 1, 0, 246913578024691357802469135780])
        assert result == [4, 2, 0, -2, -4, 0, -99999999999999999999753086421975308642197530864219], f"Test 206 failed: got {result}, expected {[4, 2, 0, -2, -4, 0, -99999999999999999999753086421975308642197530864219]}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = arraySum([-1, -2, -3, -4, -5, 2000000], [0, 1, 2, 3, 4, 5])
        assert result == [-1, -1, -1, -1, -1, 2000005], f"Test 207 failed: got {result}, expected {[-1, -1, -1, -1, -1, 2000005]}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = arraySum([-1, -2, -3, -4, -5], [5, 4, 3, 1, 0])
        assert result == [4, 2, 0, -3, -5], f"Test 208 failed: got {result}, expected {[4, 2, 0, -3, -5]}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = arraySum([-1, -2, -3, -4, -5, 0], [5, 0, 3, 2, 1, 0])
        assert result == [4, -2, 0, -2, -4, 0], f"Test 209 failed: got {result}, expected {[4, -2, 0, -2, -4, 0]}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = arraySum([-1, -2, -3, -4, -5], [4, 3, 2, 1, 0])
        assert result == [3, 1, -1, -3, -5], f"Test 210 failed: got {result}, expected {[3, 1, -1, -3, -5]}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = arraySum([9, 8, 7, 6, 5, 4, 2, 1, 0], [9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [18, 16, 14, 12, 10, 8, 5, 3, 1], f"Test 211 failed: got {result}, expected {[18, 16, 14, 12, 10, 8, 5, 3, 1]}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = arraySum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 40])
        assert result == [9, 9, 9, 9, 9, 9, 9, 9, 9, 49], f"Test 212 failed: got {result}, expected {[9, 9, 9, 9, 9, 9, 9, 9, 9, 49]}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = arraySum([0, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [9, 10, 10, 10, 10, 10, 10, 10, 10], f"Test 213 failed: got {result}, expected {[9, 10, 10, 10, 10, 10, 10, 10, 10]}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = arraySum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, -100000000000000000000000000000000000000000000000000])
        assert result == [9, 9, 9, 9, 9, 9, 9, 9, 9, -99999999999999999999999999999999999999999999999991], f"Test 214 failed: got {result}, expected {[9, 9, 9, 9, 9, 9, 9, 9, 9, -99999999999999999999999999999999999999999999999991]}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = arraySum([10, 20, 30, 40, 49, 60, 70, 0], [70, 0, 50, 40, 30, 20, 10, 0])
        assert result == [80, 20, 80, 80, 79, 80, 80, 0], f"Test 215 failed: got {result}, expected {[80, 20, 80, 80, 79, 80, 80, 0]}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = arraySum([70, 60, 50, 40, 30, 20, 10, 0], [70, 60, 50, 5, 30, 20, 10, 0])
        assert result == [140, 120, 100, 45, 60, 40, 20, 0], f"Test 216 failed: got {result}, expected {[140, 120, 100, 45, 60, 40, 20, 0]}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = arraySum([10, 20, 40, 50, 60, 70, 43, 31], [70, 60, 50, 40, 30, 20, 10, 0])
        assert result == [80, 80, 90, 90, 90, 90, 53, 31], f"Test 217 failed: got {result}, expected {[80, 80, 90, 90, 90, 90, 53, 31]}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
