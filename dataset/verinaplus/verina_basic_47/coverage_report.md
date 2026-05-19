# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def arraySum(a):
2: ✓     return sum(a)
```

## Complete Test File

```python
def arraySum(a):
    return sum(a)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = arraySum([1, 2, 3, 4, 5])
        assert result == 15, f"Test 1 failed: got {result}, expected {15}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = arraySum([13, 14, 15, 16, 17])
        assert result == 75, f"Test 2 failed: got {result}, expected {75}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = arraySum([-1, -2, -3])
        assert result == -6, f"Test 3 failed: got {result}, expected {-6}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = arraySum([10, -10])
        assert result == 0, f"Test 4 failed: got {result}, expected {0}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = arraySum([1])
        assert result == 1, f"Test 5 failed: got {result}, expected {1}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = arraySum([-1])
        assert result == -1, f"Test 6 failed: got {result}, expected {-1}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = arraySum([9223372036854775807])
        assert result == 9223372036854775807, f"Test 7 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = arraySum([-9223372036854775808])
        assert result == -9223372036854775808, f"Test 8 failed: got {result}, expected {-9223372036854775808}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = arraySum([1000000000000000000000000])
        assert result == 1000000000000000000000000, f"Test 9 failed: got {result}, expected {1000000000000000000000000}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = arraySum([-1000000000000000000000000])
        assert result == -1000000000000000000000000, f"Test 10 failed: got {result}, expected {-1000000000000000000000000}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = arraySum([-1, -2, -3, -4, -5])
        assert result == -15, f"Test 11 failed: got {result}, expected {-15}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = arraySum([0, 0, 0, 0])
        assert result == 0, f"Test 12 failed: got {result}, expected {0}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = arraySum([5, -2, 7, -3, 0])
        assert result == 7, f"Test 13 failed: got {result}, expected {7}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = arraySum([-2147483648, 2147483647])
        assert result == -1, f"Test 14 failed: got {result}, expected {-1}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = arraySum([999999999, -999999999, 123456789, -123456789])
        assert result == 0, f"Test 15 failed: got {result}, expected {0}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = arraySum([1, -1, 1, -1, 1, -1, 1, -1])
        assert result == 0, f"Test 16 failed: got {result}, expected {0}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = arraySum([42])
        assert result == 42, f"Test 17 failed: got {result}, expected {42}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = arraySum([-42])
        assert result == -42, f"Test 18 failed: got {result}, expected {-42}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = arraySum([3, 3, 3, 3, 3, 3, 3])
        assert result == 21, f"Test 19 failed: got {result}, expected {21}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = arraySum([-3, -3, -3, -3, -3, -3, -3])
        assert result == -21, f"Test 20 failed: got {result}, expected {-21}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = arraySum([8, -5, 2, -1, 4, -8, 10])
        assert result == 10, f"Test 21 failed: got {result}, expected {10}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = arraySum([100, 200, 300, 400, 500])
        assert result == 1500, f"Test 22 failed: got {result}, expected {1500}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = arraySum([-100, -200, -300, -400, -500])
        assert result == -1500, f"Test 23 failed: got {result}, expected {-1500}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = arraySum([12345678901234567890, -12345678901234567889])
        assert result == 1, f"Test 24 failed: got {result}, expected {1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = arraySum([2, 4, 8, 16, 32, 64, 128, 256])
        assert result == 510, f"Test 25 failed: got {result}, expected {510}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = arraySum([-2, -4, -8, -16, -32, -64, -128, -256])
        assert result == -510, f"Test 26 failed: got {result}, expected {-510}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = arraySum([11, -22, 33, -44, 55, -66, 77, -88, 99])
        assert result == 55, f"Test 27 failed: got {result}, expected {55}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = arraySum([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        assert result == 1, f"Test 28 failed: got {result}, expected {1}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = arraySum([9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == 45, f"Test 29 failed: got {result}, expected {45}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = arraySum([-9, -8, -7, -6, -5, -4, -3, -2, -1])
        assert result == -45, f"Test 30 failed: got {result}, expected {-45}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = arraySum([3141592653589793, -2718281828459045, 1618033988749894])
        assert result == 2041344813880642, f"Test 31 failed: got {result}, expected {2041344813880642}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = arraySum([1, 3, 4, 5])
        assert result == 13, f"Test 32 failed: got {result}, expected {13}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = arraySum([-10, 2, 3, 4, -22])
        assert result == -23, f"Test 33 failed: got {result}, expected {-23}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = arraySum([1, 2, 6, 4, 5, 0, 0, -21, 33])
        assert result == 30, f"Test 34 failed: got {result}, expected {30}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = arraySum([1, 2, 3, 0, 5, 0])
        assert result == 11, f"Test 35 failed: got {result}, expected {11}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = arraySum([5, 4, 3, 2, 1, -42, 9, 0])
        assert result == -18, f"Test 36 failed: got {result}, expected {-18}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = arraySum([1, 2, 3, 4, 5, 0, 0])
        assert result == 15, f"Test 37 failed: got {result}, expected {15}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = arraySum([-1, 2, 3, 4, 5, 17])
        assert result == 30, f"Test 38 failed: got {result}, expected {30}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = arraySum([1, 2, 0, 4, 5, 0, 0])
        assert result == 12, f"Test 39 failed: got {result}, expected {12}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = arraySum([1, 2, 3, 4, 5, 0])
        assert result == 15, f"Test 40 failed: got {result}, expected {15}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = arraySum([1, 2, 3, 4, -42])
        assert result == -32, f"Test 41 failed: got {result}, expected {-32}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = arraySum([0, 5, 4, 3, 2, 1])
        assert result == 15, f"Test 42 failed: got {result}, expected {15}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = arraySum([1, 2, 4, 5])
        assert result == 12, f"Test 43 failed: got {result}, expected {12}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = arraySum([17, 16, 15, 14])
        assert result == 62, f"Test 44 failed: got {result}, expected {62}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = arraySum([0, 17, 16, 42, 14, 12, 0])
        assert result == 101, f"Test 45 failed: got {result}, expected {101}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = arraySum([13, 14, 15, 16, 17, -400, -500])
        assert result == -825, f"Test 46 failed: got {result}, expected {-825}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = arraySum([13, 14, 15, 17])
        assert result == 59, f"Test 47 failed: got {result}, expected {59}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = arraySum([999999999, 14, 15, 16, 17, -100, 0, 100])
        assert result == 1000000061, f"Test 48 failed: got {result}, expected {1000000061}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = arraySum([17, 16, 15, 15, 13])
        assert result == 76, f"Test 49 failed: got {result}, expected {76}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = arraySum([13, 14, 15, 16, 17, 0])
        assert result == 75, f"Test 50 failed: got {result}, expected {75}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = arraySum([13, 14, 15, 16, 17, 123456789])
        assert result == 123456864, f"Test 51 failed: got {result}, expected {123456864}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = arraySum([-42, 17, 16, 15, 14, 13])
        assert result == 33, f"Test 52 failed: got {result}, expected {33}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = arraySum([13, 14, 15, 17, -100, 7])
        assert result == -34, f"Test 53 failed: got {result}, expected {-34}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = arraySum([14, 15, 16, 17, 128, 0, 0])
        assert result == 190, f"Test 54 failed: got {result}, expected {190}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = arraySum([17, 16, 15, 14, 13])
        assert result == 75, f"Test 55 failed: got {result}, expected {75}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = arraySum([0, 16, 15, 14, 13, 256, -66])
        assert result == 248, f"Test 56 failed: got {result}, expected {248}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = arraySum([-2])
        assert result == -2, f"Test 57 failed: got {result}, expected {-2}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = arraySum([-1, -2, -3, 0, 0])
        assert result == -6, f"Test 58 failed: got {result}, expected {-6}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = arraySum([13, 0, 0])
        assert result == 13, f"Test 59 failed: got {result}, expected {13}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = arraySum([-2, -3, -3, -123456789, 0])
        assert result == -123456797, f"Test 60 failed: got {result}, expected {-123456797}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = arraySum([-1, -2, -2])
        assert result == -5, f"Test 61 failed: got {result}, expected {-5}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = arraySum([-1, -2, -3, 0])
        assert result == -6, f"Test 62 failed: got {result}, expected {-6}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = arraySum([-3, -2, -1, 13, 0, 0])
        assert result == 7, f"Test 63 failed: got {result}, expected {7}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = arraySum([-1, -4, -3, 21])
        assert result == 13, f"Test 64 failed: got {result}, expected {13}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = arraySum([-2, -3, -21])
        assert result == -26, f"Test 65 failed: got {result}, expected {-26}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = arraySum([-2, -3, 3141592653589793, -256])
        assert result == 3141592653589532, f"Test 66 failed: got {result}, expected {3141592653589532}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = arraySum([-2, -2, -3, 0, 0])
        assert result == -7, f"Test 67 failed: got {result}, expected {-7}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = arraySum([-3, -2, -2])
        assert result == -7, f"Test 68 failed: got {result}, expected {-7}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = arraySum([-3, 99, -3, -2, -1])
        assert result == 90, f"Test 69 failed: got {result}, expected {90}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = arraySum([-3, -1, 0])
        assert result == -4, f"Test 70 failed: got {result}, expected {-4}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = arraySum([-10, -11, 3, -400])
        assert result == -418, f"Test 71 failed: got {result}, expected {-418}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = arraySum([-10, 10, 0, 0])
        assert result == 0, f"Test 72 failed: got {result}, expected {0}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = arraySum([10, -10, 21])
        assert result == 21, f"Test 73 failed: got {result}, expected {21}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = arraySum([11, -10, 0, -1000000000000000000000000])
        assert result == -999999999999999999999999, f"Test 74 failed: got {result}, expected {-999999999999999999999999}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = arraySum([10, -10, 200, 55, 0])
        assert result == 255, f"Test 75 failed: got {result}, expected {255}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = arraySum([10, -10, -88])
        assert result == -88, f"Test 76 failed: got {result}, expected {-88}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = arraySum([0, 10, -10, -2147483648])
        assert result == -2147483648, f"Test 77 failed: got {result}, expected {-2147483648}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = arraySum([-10, 10])
        assert result == 0, f"Test 78 failed: got {result}, expected {0}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = arraySum([-11, -21, 0])
        assert result == -32, f"Test 79 failed: got {result}, expected {-32}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = arraySum([-10, 0])
        assert result == -10, f"Test 80 failed: got {result}, expected {-10}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = arraySum([7, 0])
        assert result == 7, f"Test 81 failed: got {result}, expected {7}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = arraySum([10, -10, -1000000000000000000000000, 0])
        assert result == -1000000000000000000000000, f"Test 82 failed: got {result}, expected {-1000000000000000000000000}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = arraySum([10, -10, 65, -999999999])
        assert result == -999999934, f"Test 83 failed: got {result}, expected {-999999934}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = arraySum([0, 1])
        assert result == 1, f"Test 84 failed: got {result}, expected {1}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = arraySum([-1000000000000000000000000, 0])
        assert result == -1000000000000000000000000, f"Test 85 failed: got {result}, expected {-1000000000000000000000000}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = arraySum([0, 15])
        assert result == 15, f"Test 86 failed: got {result}, expected {15}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = arraySum([0, 55])
        assert result == 55, f"Test 87 failed: got {result}, expected {55}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = arraySum([-200, 0, 0])
        assert result == -200, f"Test 88 failed: got {result}, expected {-200}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = arraySum([0, 9223372036854775807])
        assert result == 9223372036854775807, f"Test 89 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = arraySum([-5])
        assert result == -5, f"Test 90 failed: got {result}, expected {-5}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = arraySum([15, 0, 0])
        assert result == 15, f"Test 91 failed: got {result}, expected {15}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = arraySum([0, 1618033988749894, 0, 0])
        assert result == 1618033988749894, f"Test 92 failed: got {result}, expected {1618033988749894}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = arraySum([-400, 0, -123456789])
        assert result == -123457189, f"Test 93 failed: got {result}, expected {-123457189}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = arraySum([0, 0, 0])
        assert result == 0, f"Test 94 failed: got {result}, expected {0}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = arraySum([-4, 0, -21])
        assert result == -25, f"Test 95 failed: got {result}, expected {-25}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = arraySum([-1, 0, 0])
        assert result == -1, f"Test 96 failed: got {result}, expected {-1}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = arraySum([0, 0, -11, 0])
        assert result == -11, f"Test 97 failed: got {result}, expected {-11}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = arraySum([17, -123456789])
        assert result == -123456772, f"Test 98 failed: got {result}, expected {-123456772}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = arraySum([0, -16, 0, 1])
        assert result == -15, f"Test 99 failed: got {result}, expected {-15}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = arraySum([2147483647, 0, 0])
        assert result == 2147483647, f"Test 100 failed: got {result}, expected {2147483647}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = arraySum([2])
        assert result == 2, f"Test 101 failed: got {result}, expected {2}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = arraySum([1618033988749894, 1])
        assert result == 1618033988749895, f"Test 102 failed: got {result}, expected {1618033988749895}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = arraySum([1, 2147483647, -64])
        assert result == 2147483584, f"Test 103 failed: got {result}, expected {2147483584}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = arraySum([1, 0])
        assert result == 1, f"Test 104 failed: got {result}, expected {1}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = arraySum([2, 0, 0, 0, 200])
        assert result == 202, f"Test 105 failed: got {result}, expected {202}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = arraySum([12345678901234567890])
        assert result == 12345678901234567890, f"Test 106 failed: got {result}, expected {12345678901234567890}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = arraySum([1, 77, 0, 6])
        assert result == 84, f"Test 107 failed: got {result}, expected {84}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = arraySum([1, 0, -22])
        assert result == -21, f"Test 108 failed: got {result}, expected {-21}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = arraySum([-1, 300, -198])
        assert result == 101, f"Test 109 failed: got {result}, expected {101}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = arraySum([-1, 0])
        assert result == -1, f"Test 110 failed: got {result}, expected {-1}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = arraySum([-4])
        assert result == -4, f"Test 111 failed: got {result}, expected {-4}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = arraySum([-1, -1])
        assert result == -2, f"Test 112 failed: got {result}, expected {-2}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = arraySum([9223372036854775806])
        assert result == 9223372036854775806, f"Test 113 failed: got {result}, expected {9223372036854775806}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = arraySum([-500, 9223372036854775807])
        assert result == 9223372036854775307, f"Test 114 failed: got {result}, expected {9223372036854775307}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = arraySum([9223372036854775807, -1, 0])
        assert result == 9223372036854775806, f"Test 115 failed: got {result}, expected {9223372036854775806}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = arraySum([0, 4294967294])
        assert result == 4294967294, f"Test 116 failed: got {result}, expected {4294967294}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = arraySum([9223372036854775807, 0])
        assert result == 9223372036854775807, f"Test 117 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = arraySum([9223372036854775807, 0, 0])
        assert result == 9223372036854775807, f"Test 118 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = arraySum([9223372036854775807, 1000000000000000000000000])
        assert result == 1000009223372036854775807, f"Test 119 failed: got {result}, expected {1000009223372036854775807}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = arraySum([300])
        assert result == 300, f"Test 120 failed: got {result}, expected {300}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = arraySum([0, 0, -9223372036854775807])
        assert result == -9223372036854775807, f"Test 121 failed: got {result}, expected {-9223372036854775807}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = arraySum([0, 0, 9223372036854775808])
        assert result == 9223372036854775808, f"Test 122 failed: got {result}, expected {9223372036854775808}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = arraySum([-123456789])
        assert result == -123456789, f"Test 123 failed: got {result}, expected {-123456789}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = arraySum([-9223372036854775808, 65, -6])
        assert result == -9223372036854775749, f"Test 124 failed: got {result}, expected {-9223372036854775749}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = arraySum([-3, -9223372036854775808])
        assert result == -9223372036854775811, f"Test 125 failed: got {result}, expected {-9223372036854775811}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = arraySum([-9223372036854775810])
        assert result == -9223372036854775810, f"Test 126 failed: got {result}, expected {-9223372036854775810}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = arraySum([-9223372036854775808, 256, 0, 0])
        assert result == -9223372036854775552, f"Test 127 failed: got {result}, expected {-9223372036854775552}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = arraySum([-9223372036854775808, -64, 0])
        assert result == -9223372036854775872, f"Test 128 failed: got {result}, expected {-9223372036854775872}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = arraySum([-7])
        assert result == -7, f"Test 129 failed: got {result}, expected {-7}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = arraySum([-18446744073709551616, -8])
        assert result == -18446744073709551624, f"Test 130 failed: got {result}, expected {-18446744073709551624}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = arraySum([-9223372036854775808, 0])
        assert result == -9223372036854775808, f"Test 131 failed: got {result}, expected {-9223372036854775808}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = arraySum([9223372036854775808, -21])
        assert result == 9223372036854775787, f"Test 132 failed: got {result}, expected {9223372036854775787}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = arraySum([11])
        assert result == 11, f"Test 133 failed: got {result}, expected {11}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = arraySum([0, 12, 0, 0, 1000000000000000000000000])
        assert result == 1000000000000000000000012, f"Test 134 failed: got {result}, expected {1000000000000000000000012}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = arraySum([1000000000000000000000000, 0])
        assert result == 1000000000000000000000000, f"Test 135 failed: got {result}, expected {1000000000000000000000000}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = arraySum([0, 1000000000000000000000000])
        assert result == 1000000000000000000000000, f"Test 136 failed: got {result}, expected {1000000000000000000000000}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = arraySum([1000000000000000000000000, 0, -12345678901234567889])
        assert result == 999987654321098765432111, f"Test 137 failed: got {result}, expected {999987654321098765432111}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = arraySum([1000000000000000000000000, -200])
        assert result == 999999999999999999999800, f"Test 138 failed: got {result}, expected {999999999999999999999800}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = arraySum([1000000000000000000000000, 3])
        assert result == 1000000000000000000000003, f"Test 139 failed: got {result}, expected {1000000000000000000000003}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = arraySum([4, 0, 1000000000000000000000000])
        assert result == 1000000000000000000000004, f"Test 140 failed: got {result}, expected {1000000000000000000000004}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = arraySum([0, -100, 0, -400])
        assert result == -500, f"Test 141 failed: got {result}, expected {-500}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = arraySum([0, 0, 500, 10])
        assert result == 510, f"Test 142 failed: got {result}, expected {510}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = arraySum([999999999999999999999999, 17])
        assert result == 1000000000000000000000016, f"Test 143 failed: got {result}, expected {1000000000000000000000016}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = arraySum([32])
        assert result == 32, f"Test 144 failed: got {result}, expected {32}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = arraySum([3141592653589793, 0])
        assert result == 3141592653589793, f"Test 145 failed: got {result}, expected {3141592653589793}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = arraySum([-4, 0])
        assert result == -4, f"Test 146 failed: got {result}, expected {-4}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = arraySum([0, -1000000000000000000000000])
        assert result == -1000000000000000000000000, f"Test 147 failed: got {result}, expected {-1000000000000000000000000}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = arraySum([-1000000000000000000000001, 0])
        assert result == -1000000000000000000000001, f"Test 148 failed: got {result}, expected {-1000000000000000000000001}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = arraySum([1000000000000000000000000, 0, 123456789, 0])
        assert result == 1000000000000000123456789, f"Test 149 failed: got {result}, expected {1000000000000000123456789}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = arraySum([200, 0, -5, -4, -3, -2, -1, 0])
        assert result == 185, f"Test 150 failed: got {result}, expected {185}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = arraySum([-1, -2, -3, -4, 21, 0, -88])
        assert result == -77, f"Test 151 failed: got {result}, expected {-77}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = arraySum([-1, -2, -1000000000000000000000001, -4, -5, 256])
        assert result == -999999999999999999999757, f"Test 152 failed: got {result}, expected {-999999999999999999999757}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = arraySum([-1, -2, -3, -4, 0, 0])
        assert result == -10, f"Test 153 failed: got {result}, expected {-10}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = arraySum([-5, -2, -3, -4, -5, -3, 0, -14, 0])
        assert result == -36, f"Test 154 failed: got {result}, expected {-36}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = arraySum([-1, -2, -3, -4, -5, 0])
        assert result == -15, f"Test 155 failed: got {result}, expected {-15}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = arraySum([-5, -4, -3, -2, -1])
        assert result == -15, f"Test 156 failed: got {result}, expected {-15}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = arraySum([-1, -2, -3, -4, -5, -66])
        assert result == -81, f"Test 157 failed: got {result}, expected {-81}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = arraySum([-2, -4, -5])
        assert result == -11, f"Test 158 failed: got {result}, expected {-11}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = arraySum([-1, -3, -4, -5, 0])
        assert result == -13, f"Test 159 failed: got {result}, expected {-13}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = arraySum([-1, -2, -3, -500, 12])
        assert result == -494, f"Test 160 failed: got {result}, expected {-494}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = arraySum([0, 12, -5, -4, -3, -2, -1])
        assert result == -3, f"Test 161 failed: got {result}, expected {-3}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = arraySum([-11, -2, -3, -4, -5, 18446744073709551614])
        assert result == 18446744073709551589, f"Test 162 failed: got {result}, expected {18446744073709551589}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = arraySum([0, -5, 65, -1000000000000000000000000, -2, -1])
        assert result == -999999999999999999999943, f"Test 163 failed: got {result}, expected {-999999999999999999999943}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = arraySum([-1, -2, -3, -3, -5, 0])
        assert result == -14, f"Test 164 failed: got {result}, expected {-14}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = arraySum([0, 0, 0, -500, 32])
        assert result == -468, f"Test 165 failed: got {result}, expected {-468}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = arraySum([12345678901234567890, 0, 0, 0, 0, -10])
        assert result == 12345678901234567880, f"Test 166 failed: got {result}, expected {12345678901234567880}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = arraySum([0, 0, 0, 0, 0, 0])
        assert result == 0, f"Test 167 failed: got {result}, expected {0}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = arraySum([0, 0, 0, -4])
        assert result == -4, f"Test 168 failed: got {result}, expected {-4}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = arraySum([0, 0, 0, 9223372036854775806, 0, 2])
        assert result == 9223372036854775808, f"Test 169 failed: got {result}, expected {9223372036854775808}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = arraySum([0, 1, 0, 0, -128])
        assert result == -127, f"Test 170 failed: got {result}, expected {-127}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = arraySum([0, 0, 0, 77, -400])
        assert result == -323, f"Test 171 failed: got {result}, expected {-323}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = arraySum([0, 0, 0, 100])
        assert result == 100, f"Test 172 failed: got {result}, expected {100}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = arraySum([0, 0, 0, -21, 0])
        assert result == -21, f"Test 173 failed: got {result}, expected {-21}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = arraySum([9223372036854775807, 0, 0, -1, 0])
        assert result == 9223372036854775806, f"Test 174 failed: got {result}, expected {9223372036854775806}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = arraySum([0, 0, 0, 0, 100])
        assert result == 100, f"Test 175 failed: got {result}, expected {100}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = arraySum([5, -2, 7, -3])
        assert result == 7, f"Test 176 failed: got {result}, expected {7}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = arraySum([5, 0, 0, -32])
        assert result == -27, f"Test 177 failed: got {result}, expected {-27}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = arraySum([-9, 1, -3, 7, -2, 5])
        assert result == -1, f"Test 178 failed: got {result}, expected {-1}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = arraySum([0, 3, 7, -2, 5, 0])
        assert result == 13, f"Test 179 failed: got {result}, expected {13}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = arraySum([5, -2, 128])
        assert result == 131, f"Test 180 failed: got {result}, expected {131}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = arraySum([5, -2, 7, -3, 0, 0])
        assert result == 7, f"Test 181 failed: got {result}, expected {7}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = arraySum([-2, 17, 0, -3, 7, -2, 5])
        assert result == 22, f"Test 182 failed: got {result}, expected {22}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = arraySum([5, -2, 7, -3, 1, -9223372036854775807, -300, 0])
        assert result == -9223372036854776099, f"Test 183 failed: got {result}, expected {-9223372036854776099}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = arraySum([0, 0, -3, 7, -2, 5])
        assert result == 7, f"Test 184 failed: got {result}, expected {7}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = arraySum([5, -2, 7, -128, 0, -9223372036854775807])
        assert result == -9223372036854775925, f"Test 185 failed: got {result}, expected {-9223372036854775925}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = arraySum([5, -2, 7, 0, 0, 0, 9223372036854775806])
        assert result == 9223372036854775816, f"Test 186 failed: got {result}, expected {9223372036854775816}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = arraySum([0, -2, 7, -3, -11, 77, 33])
        assert result == 101, f"Test 187 failed: got {result}, expected {101}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = arraySum([5, -2, 7, -2, 0])
        assert result == 8, f"Test 188 failed: got {result}, expected {8}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = arraySum([2147483647, 1, -1, -32, -14])
        assert result == 2147483601, f"Test 189 failed: got {result}, expected {2147483601}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = arraySum([0, -400, -1, 1, 2147483647])
        assert result == 2147483247, f"Test 190 failed: got {result}, expected {2147483247}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = arraySum([-2, 0, 2147483647])
        assert result == 2147483645, f"Test 191 failed: got {result}, expected {2147483645}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = arraySum([-1, 1, 2147483647, -400, -21, 42])
        assert result == 2147483268, f"Test 192 failed: got {result}, expected {2147483268}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = arraySum([0, 2147483647, 1, -1])
        assert result == 2147483647, f"Test 193 failed: got {result}, expected {2147483647}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = arraySum([2, 2147483650])
        assert result == 2147483652, f"Test 194 failed: got {result}, expected {2147483652}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = arraySum([6, 2147483647, -1, 0])
        assert result == 2147483652, f"Test 195 failed: got {result}, expected {2147483652}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = arraySum([2147483647, -1, 0])
        assert result == 2147483646, f"Test 196 failed: got {result}, expected {2147483646}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = arraySum([2147483647, 0, -21])
        assert result == 2147483626, f"Test 197 failed: got {result}, expected {2147483626}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = arraySum([2147483647, 1, 0])
        assert result == 2147483648, f"Test 198 failed: got {result}, expected {2147483648}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = arraySum([0, -2147483648, -1, 2, 2147483647])
        assert result == 0, f"Test 199 failed: got {result}, expected {0}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = arraySum([2147483647, 1, -1, 0])
        assert result == 2147483647, f"Test 200 failed: got {result}, expected {2147483647}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = arraySum([4294967294, 1, -2, 13, 0, 6])
        assert result == 4294967312, f"Test 201 failed: got {result}, expected {4294967312}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = arraySum([1, 100])
        assert result == 101, f"Test 202 failed: got {result}, expected {101}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = arraySum([2147483647, 0, 0, 18446744073709551614])
        assert result == 18446744075857035261, f"Test 203 failed: got {result}, expected {18446744075857035261}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = arraySum([-2147483648, 2147483647, 0])
        assert result == -1, f"Test 204 failed: got {result}, expected {-1}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = arraySum([-9223372036854775807, 2147483647, -2147483648, 0])
        assert result == -9223372036854775808, f"Test 205 failed: got {result}, expected {-9223372036854775808}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = arraySum([2147483647, -1])
        assert result == 2147483646, f"Test 206 failed: got {result}, expected {2147483646}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = arraySum([-4294967296])
        assert result == -4294967296, f"Test 207 failed: got {result}, expected {-4294967296}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = arraySum([-2147483647, 2147483647])
        assert result == 0, f"Test 208 failed: got {result}, expected {0}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = arraySum([2147483650, 0])
        assert result == 2147483650, f"Test 209 failed: got {result}, expected {2147483650}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = arraySum([2147483647])
        assert result == 2147483647, f"Test 210 failed: got {result}, expected {2147483647}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = arraySum([77, -2147483648, 2147483647, 0])
        assert result == 76, f"Test 211 failed: got {result}, expected {76}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = arraySum([-2147483648])
        assert result == -2147483648, f"Test 212 failed: got {result}, expected {-2147483648}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = arraySum([0, -2147483648, 2147483648])
        assert result == 0, f"Test 213 failed: got {result}, expected {0}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = arraySum([-123456789, 123456789, -999999999])
        assert result == -999999999, f"Test 214 failed: got {result}, expected {-999999999}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = arraySum([-123456789, 123456789, -999999999, 999999999, 0, 0, 0])
        assert result == 0, f"Test 215 failed: got {result}, expected {0}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = arraySum([-44, -1999999998, 123456789, 0, 0])
        assert result == -1876543253, f"Test 216 failed: got {result}, expected {-1876543253}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = arraySum([-999999999, 123456789, -123456791, 0])
        assert result == -1000000001, f"Test 217 failed: got {result}, expected {-1000000001}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = arraySum([999999999, -999999999, -123456789, 4294967294])
        assert result == 4171510505, f"Test 218 failed: got {result}, expected {4171510505}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = arraySum([-999999999, 123456789, 128])
        assert result == -876543082, f"Test 219 failed: got {result}, expected {-876543082}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = arraySum([999999999, -999999999, 123456789, -123456789, 4294967294])
        assert result == 4294967294, f"Test 220 failed: got {result}, expected {4294967294}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = arraySum([999999999, -999999999, 123456789, 123456789])
        assert result == 246913578, f"Test 221 failed: got {result}, expected {246913578}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = arraySum([-123456789, 0, -999999999, 999999999])
        assert result == -123456789, f"Test 222 failed: got {result}, expected {-123456789}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = arraySum([-42, -123456789, -999999999, 999999999])
        assert result == -123456831, f"Test 223 failed: got {result}, expected {-123456831}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = arraySum([-123456789, 123456789, -999999999, 999999999])
        assert result == 0, f"Test 224 failed: got {result}, expected {0}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = arraySum([999999999, -999999999, -123456789, 0, 0, 0, 0])
        assert result == -123456789, f"Test 225 failed: got {result}, expected {-123456789}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = arraySum([999999999, -999999999, 123456789, -123456789, 0, 99])
        assert result == 99, f"Test 226 failed: got {result}, expected {99}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = arraySum([1, 1, -1, 1, -1, 1, -1])
        assert result == 1, f"Test 227 failed: got {result}, expected {1}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = arraySum([-2, -1, 1, -1, 1, -1, 1, -1, 1])
        assert result == -2, f"Test 228 failed: got {result}, expected {-2}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = arraySum([0, 0, -1, 1, -1, 1, -1, 1, -1, 1])
        assert result == 0, f"Test 229 failed: got {result}, expected {0}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = arraySum([256, -1, 1, -1, 1, -1, 1, -1, 1])
        assert result == 256, f"Test 230 failed: got {result}, expected {256}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = arraySum([1, -1, 1, -1, 1, -1, 1, -1, 0, 65])
        assert result == 65, f"Test 231 failed: got {result}, expected {65}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = arraySum([1, -1, 1, -1, 1, -1, 1, -1, -42])
        assert result == -42, f"Test 232 failed: got {result}, expected {-42}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = arraySum([1, -1, 1, -1, 1, -1, 1, -1, 0])
        assert result == 0, f"Test 233 failed: got {result}, expected {0}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = arraySum([1, -1, 1, -1, 1, -1, 1, -1, 1618033988749894])
        assert result == 1618033988749894, f"Test 234 failed: got {result}, expected {1618033988749894}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = arraySum([1, -1, 1, -1, 1, 1, -1])
        assert result == 1, f"Test 235 failed: got {result}, expected {1}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = arraySum([1, -1, 1, -21, 1, -1, 1, -1])
        assert result == -20, f"Test 236 failed: got {result}, expected {-20}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = arraySum([1, -1, 1, -1, 1, -1, 1, -1, -1000000000000000000000000, 33, 0])
        assert result == -999999999999999999999967, f"Test 237 failed: got {result}, expected {-999999999999999999999967}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = arraySum([1, -1, 1, -1, -1, 1, -1, 0, 0])
        assert result == -1, f"Test 238 failed: got {result}, expected {-1}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = arraySum([1, -1, -1, 1, -1, 1, -1, 3141592653589793, 1000000000000000000000000])
        assert result == 1000000003141592653589792, f"Test 239 failed: got {result}, expected {1000000003141592653589792}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = arraySum([2147483647, 42])
        assert result == 2147483689, f"Test 240 failed: got {result}, expected {2147483689}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = arraySum([0, 41, 0])
        assert result == 41, f"Test 241 failed: got {result}, expected {41}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = arraySum([-12345678901234567889, 0, 42])
        assert result == -12345678901234567847, f"Test 242 failed: got {result}, expected {-12345678901234567847}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = arraySum([42, 0, 0, 0])
        assert result == 42, f"Test 243 failed: got {result}, expected {42}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = arraySum([-1999999997, 500, 9223372036854775806])
        assert result == 9223372034854776309, f"Test 244 failed: got {result}, expected {9223372034854776309}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = arraySum([42, 0])
        assert result == 42, f"Test 245 failed: got {result}, expected {42}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = arraySum([42, 9223372036854775807])
        assert result == 9223372036854775849, f"Test 246 failed: got {result}, expected {9223372036854775849}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = arraySum([-999999999, -12345678901234567889, 0, 0])
        assert result == -12345678902234567888, f"Test 247 failed: got {result}, expected {-12345678902234567888}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = arraySum([0, -123456789])
        assert result == -123456789, f"Test 248 failed: got {result}, expected {-123456789}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = arraySum([-42, -14])
        assert result == -56, f"Test 249 failed: got {result}, expected {-56}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = arraySum([-1000000000000000000000000, 42, 8, 15])
        assert result == -999999999999999999999935, f"Test 250 failed: got {result}, expected {-999999999999999999999935}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = arraySum([0, 0, 42])
        assert result == 42, f"Test 251 failed: got {result}, expected {42}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = arraySum([41, 0])
        assert result == 41, f"Test 252 failed: got {result}, expected {41}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = arraySum([1618033988749894])
        assert result == 1618033988749894, f"Test 253 failed: got {result}, expected {1618033988749894}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = arraySum([-42, 4294967294])
        assert result == 4294967252, f"Test 254 failed: got {result}, expected {4294967252}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = arraySum([-42, 0])
        assert result == -42, f"Test 255 failed: got {result}, expected {-42}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = arraySum([-43, 0, -99, 0, 12345678901234567890])
        assert result == 12345678901234567748, f"Test 256 failed: got {result}, expected {12345678901234567748}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = arraySum([-128, 42, 0, -3])
        assert result == -89, f"Test 257 failed: got {result}, expected {-89}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = arraySum([-42, 9223372036854775808, 0, 99])
        assert result == 9223372036854775865, f"Test 258 failed: got {result}, expected {9223372036854775865}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = arraySum([-42, -11])
        assert result == -53, f"Test 259 failed: got {result}, expected {-53}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = arraySum([-42, -64])
        assert result == -106, f"Test 260 failed: got {result}, expected {-106}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = arraySum([-84])
        assert result == -84, f"Test 261 failed: got {result}, expected {-84}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = arraySum([-42, -42, 0])
        assert result == -84, f"Test 262 failed: got {result}, expected {-84}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = arraySum([-42, 0, -5])
        assert result == -47, f"Test 263 failed: got {result}, expected {-47}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = arraySum([0, 0, -64])
        assert result == -64, f"Test 264 failed: got {result}, expected {-64}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = arraySum([-42, -7])
        assert result == -49, f"Test 265 failed: got {result}, expected {-49}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = arraySum([3, 4, 3, 3, 3, 3, 0])
        assert result == 19, f"Test 266 failed: got {result}, expected {19}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = arraySum([3, 3, 3, 3, 3, 3])
        assert result == 18, f"Test 267 failed: got {result}, expected {18}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = arraySum([3, 3, 3, 3, 3, 3, 3, -999999999, -2718281828459045])
        assert result == -2718282828459023, f"Test 268 failed: got {result}, expected {-2718282828459023}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = arraySum([3, 6, 3, 3, 3, 3, 3])
        assert result == 24, f"Test 269 failed: got {result}, expected {24}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = arraySum([3, 3, 3, 0, 3, 3, 99])
        assert result == 114, f"Test 270 failed: got {result}, expected {114}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = arraySum([3, 3, 3, 3, 3, 3, 3, 0])
        assert result == 21, f"Test 271 failed: got {result}, expected {21}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = arraySum([-3, 3, 3, 17, 1, 3, 3, -256, -1000000000000000000000000])
        assert result == -1000000000000000000000229, f"Test 272 failed: got {result}, expected {-1000000000000000000000229}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = arraySum([6, 3, 3, 18446744073709551616, 3, 3, 3])
        assert result == 18446744073709551637, f"Test 273 failed: got {result}, expected {18446744073709551637}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = arraySum([55, 3, 3, 0, 3, 3, 3, 3])
        assert result == 73, f"Test 274 failed: got {result}, expected {73}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = arraySum([0, -1000000000000000000000001, 3, 3, 3, 3, 3, 3, 17])
        assert result == -999999999999999999999966, f"Test 275 failed: got {result}, expected {-999999999999999999999966}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = arraySum([3, 3, 3, 3, 3, 3, 3, -500, 9, -42])
        assert result == -512, f"Test 276 failed: got {result}, expected {-512}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = arraySum([-3, -3, -3, -3, -3, -3, 9223372036854775808, 0, 0])
        assert result == 9223372036854775790, f"Test 277 failed: got {result}, expected {9223372036854775790}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = arraySum([-3, -3, -3, -3, -3, 100, -2718281828459045])
        assert result == -2718281828458960, f"Test 278 failed: got {result}, expected {-2718281828458960}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = arraySum([12, -3, -3, -3, -3, -3, -3, -9])
        assert result == -15, f"Test 279 failed: got {result}, expected {-15}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = arraySum([-14, -3, -3, -3, -3, 0, -3, -9223372036854775810])
        assert result == -9223372036854775839, f"Test 280 failed: got {result}, expected {-9223372036854775839}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = arraySum([0, -3, -3, -3, -3, -3, -3])
        assert result == -18, f"Test 281 failed: got {result}, expected {-18}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = arraySum([-3, -3, -3, -3, -3])
        assert result == -15, f"Test 282 failed: got {result}, expected {-15}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = arraySum([-3, -3, -3, -3, -3, -3])
        assert result == -18, f"Test 283 failed: got {result}, expected {-18}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = arraySum([-3, -3, -3, 0, -3, -3, -3])
        assert result == -18, f"Test 284 failed: got {result}, expected {-18}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = arraySum([-3, -3, -3, -3, 18446744073709551616, 12345678901234567890, -3, -200])
        assert result == 30792422974944119291, f"Test 285 failed: got {result}, expected {30792422974944119291}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = arraySum([-3, -3, -3, -3, -3, -3, -3, -9223372036854775810])
        assert result == -9223372036854775831, f"Test 286 failed: got {result}, expected {-9223372036854775831}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = arraySum([4, -3, -3, -3, -3, -3, 0])
        assert result == -11, f"Test 287 failed: got {result}, expected {-11}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = arraySum([8, -5, 8, -1, 4, -8, 10, 0, -500, 21])
        assert result == -463, f"Test 288 failed: got {result}, expected {-463}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = arraySum([-5, 2, -1, 4, -8, 10])
        assert result == 2, f"Test 289 failed: got {result}, expected {2}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = arraySum([10, 8, 4, -1, 2, -5, 8])
        assert result == 26, f"Test 290 failed: got {result}, expected {26}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = arraySum([8, -5, 2, -1, 4, 0, 10, 9, -3, 0])
        assert result == 24, f"Test 291 failed: got {result}, expected {24}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = arraySum([8, -5, 2, -1, 4, -8, 10, 0])
        assert result == 10, f"Test 292 failed: got {result}, expected {10}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = arraySum([0, 10, -8, 4, -1, 2, -6, 8, 0])
        assert result == 9, f"Test 293 failed: got {result}, expected {9}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = arraySum([8, -5, 2, -1, 4, -8, -10, 16, -32])
        assert result == -26, f"Test 294 failed: got {result}, expected {-26}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = arraySum([0, -5, 2, -1, -8, 11])
        assert result == -1, f"Test 295 failed: got {result}, expected {-1}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = arraySum([-43, 8, -5, 2, -1, 4, -7, 10])
        assert result == -32, f"Test 296 failed: got {result}, expected {-32}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = arraySum([10, 1000000000000000000000000, 4, -2, 2, -5, 8])
        assert result == 1000000000000000000000017, f"Test 297 failed: got {result}, expected {1000000000000000000000017}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = arraySum([-8, 4, -1, 2, -5, 8])
        assert result == 0, f"Test 298 failed: got {result}, expected {0}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = arraySum([8, -4, 4, -8, 10])
        assert result == 10, f"Test 299 failed: got {result}, expected {10}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = arraySum([300, 10, -8, 4, -1, 2, -5, 8, 0])
        assert result == 310, f"Test 300 failed: got {result}, expected {310}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = arraySum([55, 6, -66, 10, -8, 4, 9223372036854775807, 2, -5, 8])
        assert result == 9223372036854775813, f"Test 301 failed: got {result}, expected {9223372036854775813}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = arraySum([8, -5, -1, 4, 9223372036854775807, 10, 0, -1999999997])
        assert result == 9223372034854775826, f"Test 302 failed: got {result}, expected {9223372034854775826}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = arraySum([100, 200, 300, 400, 500, -1000000000000000000000001, 9])
        assert result == -999999999999999999998492, f"Test 303 failed: got {result}, expected {-999999999999999999998492}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = arraySum([100, 200, 300, 500, 0, 42])
        assert result == 1142, f"Test 304 failed: got {result}, expected {1142}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = arraySum([100, 200, 300, 400, 500, 0])
        assert result == 1500, f"Test 305 failed: got {result}, expected {1500}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = arraySum([200, 300, 500])
        assert result == 1000, f"Test 306 failed: got {result}, expected {1000}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = arraySum([100, 200, 300, 400, 1000, -168])
        assert result == 1832, f"Test 307 failed: got {result}, expected {1832}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = arraySum([500, 300, 200, 101])
        assert result == 1101, f"Test 308 failed: got {result}, expected {1101}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = arraySum([200, 300, 400, -9223372036854775808, -8, 0])
        assert result == -9223372036854774916, f"Test 309 failed: got {result}, expected {-9223372036854774916}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = arraySum([500, 400, 300, 199, 100])
        assert result == 1499, f"Test 310 failed: got {result}, expected {1499}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = arraySum([100, 200, 300, 400])
        assert result == 1000, f"Test 311 failed: got {result}, expected {1000}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = arraySum([500, 400, 300, 200, 100])
        assert result == 1500, f"Test 312 failed: got {result}, expected {1500}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = arraySum([100, 200, 300, 400, 500, 32])
        assert result == 1532, f"Test 313 failed: got {result}, expected {1532}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = arraySum([100, 200, 300, -400, 500, 0, 1618033988749894])
        assert result == 1618033988750594, f"Test 314 failed: got {result}, expected {1618033988750594}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = arraySum([0, 500, -6, 300, 200, 100])
        assert result == 1094, f"Test 315 failed: got {result}, expected {1094}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = arraySum([-101, -200, -299, -400, -500])
        assert result == -1500, f"Test 316 failed: got {result}, expected {-1500}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = arraySum([-100, 101, -300, -400, -500, 13])
        assert result == -1186, f"Test 317 failed: got {result}, expected {-1186}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = arraySum([-500, -400, -300, -200, -100, 21])
        assert result == -1479, f"Test 318 failed: got {result}, expected {-1479}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = arraySum([-100, -200, -300, -400, -500, -4294967295, 500, 0])
        assert result == -4294968295, f"Test 319 failed: got {result}, expected {-4294968295}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = arraySum([0, -500, -400, -200, -100, -9223372036854775808])
        assert result == -9223372036854777008, f"Test 320 failed: got {result}, expected {-9223372036854777008}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = arraySum([-100, -200, -300, -400, -500, 0])
        assert result == -1500, f"Test 321 failed: got {result}, expected {-1500}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = arraySum([0, -100, -200, -300, -400, 0])
        assert result == -1000, f"Test 322 failed: got {result}, expected {-1000}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = arraySum([-100, -300, -400, -500, 5, 14])
        assert result == -1281, f"Test 323 failed: got {result}, expected {-1281}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = arraySum([-100, -400, 0, 8])
        assert result == -492, f"Test 324 failed: got {result}, expected {-492}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = arraySum([-101, -200, -300, -400, -500])
        assert result == -1501, f"Test 325 failed: got {result}, expected {-1501}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = arraySum([-100, -200, 300, -500])
        assert result == -500, f"Test 326 failed: got {result}, expected {-500}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = arraySum([-500, -400, -300, -200, -100])
        assert result == -1500, f"Test 327 failed: got {result}, expected {-1500}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = arraySum([-500, -400, -300, -201, -100])
        assert result == -1501, f"Test 328 failed: got {result}, expected {-1501}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = arraySum([-44, 0, -21, 21, -14, 14, -7, 0])
        assert result == -51, f"Test 329 failed: got {result}, expected {-51}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = arraySum([7, -7, 14, -14, 21, -21, 0, -201])
        assert result == -201, f"Test 330 failed: got {result}, expected {-201}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = arraySum([7, 0, 0, 14, -14, 21, -21, -1, -999999999])
        assert result == -999999993, f"Test 331 failed: got {result}, expected {-999999993}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = arraySum([10, 77, -21, 21, -14, 0, -7, 0, 7])
        assert result == 73, f"Test 332 failed: got {result}, expected {73}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = arraySum([-42, 21, -14, 15, -7, 0, 8, 0])
        assert result == -19, f"Test 333 failed: got {result}, expected {-19}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = arraySum([-21, 21, -14, 14, -7, 0, 3141592653589793])
        assert result == 3141592653589786, f"Test 334 failed: got {result}, expected {3141592653589786}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = arraySum([7, 0, -7, 14, -14, 21, -21, 0])
        assert result == 0, f"Test 335 failed: got {result}, expected {0}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = arraySum([-21, 21, 14, -7, 0, 0])
        assert result == 7, f"Test 336 failed: got {result}, expected {7}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = arraySum([0, -7, 14, -14, 21, 0])
        assert result == 14, f"Test 337 failed: got {result}, expected {14}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = arraySum([0, 7, 0, -7, 14, -14, 21, -21, 0])
        assert result == 0, f"Test 338 failed: got {result}, expected {0}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = arraySum([7, 0, -7, 14, -14, 21, -21, 0, 0, 13, 0])
        assert result == 13, f"Test 339 failed: got {result}, expected {13}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = arraySum([0, -21, 21, 14, -7, 7, 12345678901234567890])
        assert result == 12345678901234567904, f"Test 340 failed: got {result}, expected {12345678901234567904}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = arraySum([7, 0, 14, -14, 21, -21, 0, 0, 33, 0])
        assert result == 40, f"Test 341 failed: got {result}, expected {40}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = arraySum([0, -12345678901234567888, 12345678901234567890, 2147483647])
        assert result == 2147483649, f"Test 342 failed: got {result}, expected {2147483649}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = arraySum([12345678901234567890, -12345678901234567889, 0])
        assert result == 1, f"Test 343 failed: got {result}, expected {1}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = arraySum([12345678901234567890, -12345678901234567890, -9, 0])
        assert result == -9, f"Test 344 failed: got {result}, expected {-9}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = arraySum([-12345678901234567889, 0, 2147483647, 9223372036854775808])
        assert result == -3122306862232308434, f"Test 345 failed: got {result}, expected {-3122306862232308434}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = arraySum([12345678901234567890, -12345678901234567889, 0, 12])
        assert result == 13, f"Test 346 failed: got {result}, expected {13}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    # Test case 347
    try:
        result = arraySum([0, 18446744073709551614, -12345678901234567889])
        assert result == 6101065172474983725, f"Test 347 failed: got {result}, expected {6101065172474983725}"
        print(f"Test 347 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 347 failed: {e}")
        test_results.append(False)

    # Test case 348
    try:
        result = arraySum([12345678901234567890, 0, 0])
        assert result == 12345678901234567890, f"Test 348 failed: got {result}, expected {12345678901234567890}"
        print(f"Test 348 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 348 failed: {e}")
        test_results.append(False)

    # Test case 349
    try:
        result = arraySum([12345678901234567890, -12345678901234567888, 0])
        assert result == 2, f"Test 349 failed: got {result}, expected {2}"
        print(f"Test 349 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 349 failed: {e}")
        test_results.append(False)

    # Test case 350
    try:
        result = arraySum([0, 0, -12345678901234567889, 12345678901234567890])
        assert result == 1, f"Test 350 failed: got {result}, expected {1}"
        print(f"Test 350 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 350 failed: {e}")
        test_results.append(False)

    # Test case 351
    try:
        result = arraySum([12345678901234567890, -12345678901234567889, 1618033988749894])
        assert result == 1618033988749895, f"Test 351 failed: got {result}, expected {1618033988749895}"
        print(f"Test 351 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 351 failed: {e}")
        test_results.append(False)

    # Test case 352
    try:
        result = arraySum([9223372036854775808, -12345678901234567889])
        assert result == -3122306864379792081, f"Test 352 failed: got {result}, expected {-3122306864379792081}"
        print(f"Test 352 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 352 failed: {e}")
        test_results.append(False)

    # Test case 353
    try:
        result = arraySum([0, 256, 64, 32, 16, 8, 4, 2])
        assert result == 382, f"Test 353 failed: got {result}, expected {382}"
        print(f"Test 353 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 353 failed: {e}")
        test_results.append(False)

    # Test case 354
    try:
        result = arraySum([4, 8, 16, 32, -1000000000000000000000001, 128, 256, 0])
        assert result == -999999999999999999999557, f"Test 354 failed: got {result}, expected {-999999999999999999999557}"
        print(f"Test 354 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 354 failed: {e}")
        test_results.append(False)

    # Test case 355
    try:
        result = arraySum([2, 4, 8, 16, 32, 64, 128])
        assert result == 254, f"Test 355 failed: got {result}, expected {254}"
        print(f"Test 355 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 355 failed: {e}")
        test_results.append(False)

    # Test case 356
    try:
        result = arraySum([2, 4, 8, 16, 32, 64, 128, 256, -14, 0])
        assert result == 496, f"Test 356 failed: got {result}, expected {496}"
        print(f"Test 356 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 356 failed: {e}")
        test_results.append(False)

    # Test case 357
    try:
        result = arraySum([-66, 4, 8, 16, 32, 128, 256, 0])
        assert result == 378, f"Test 357 failed: got {result}, expected {378}"
        print(f"Test 357 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 357 failed: {e}")
        test_results.append(False)

    # Test case 358
    try:
        result = arraySum([2, 4, 8, 32, 64, 128, 256, 12345678901234567890, 999999999999999999999999, 0])
        assert result == 1000012345678901234568383, f"Test 358 failed: got {result}, expected {1000012345678901234568383}"
        print(f"Test 358 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 358 failed: {e}")
        test_results.append(False)

    # Test case 359
    try:
        result = arraySum([2, 4, 9, 16, 32, 64, 128, 256, 0, 0])
        assert result == 511, f"Test 359 failed: got {result}, expected {511}"
        print(f"Test 359 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 359 failed: {e}")
        test_results.append(False)

    # Test case 360
    try:
        result = arraySum([2, 4, 8, 16, -1000000000000000000000001, 64, 128, 256])
        assert result == -999999999999999999999523, f"Test 360 failed: got {result}, expected {-999999999999999999999523}"
        print(f"Test 360 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 360 failed: {e}")
        test_results.append(False)

    # Test case 361
    try:
        result = arraySum([65, 0, -500, 256, 128, 32, 16, 8, 4, 2])
        assert result == 11, f"Test 361 failed: got {result}, expected {11}"
        print(f"Test 361 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 361 failed: {e}")
        test_results.append(False)

    # Test case 362
    try:
        result = arraySum([2, 4, 8, 16, 32, 64, 256, 0, 0])
        assert result == 382, f"Test 362 failed: got {result}, expected {382}"
        print(f"Test 362 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 362 failed: {e}")
        test_results.append(False)

    # Test case 363
    try:
        result = arraySum([256, 128, 64, 32, 8, 4, 2])
        assert result == 494, f"Test 363 failed: got {result}, expected {494}"
        print(f"Test 363 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 363 failed: {e}")
        test_results.append(False)

    # Test case 364
    try:
        result = arraySum([2, 4, 8, 16, 32, 64, 128, 256, -9223372036854775810])
        assert result == -9223372036854775300, f"Test 364 failed: got {result}, expected {-9223372036854775300}"
        print(f"Test 364 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 364 failed: {e}")
        test_results.append(False)

    # Test case 365
    try:
        result = arraySum([256, 128, 32, 16, 8, 4, 2, -42])
        assert result == 404, f"Test 365 failed: got {result}, expected {404}"
        print(f"Test 365 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 365 failed: {e}")
        test_results.append(False)

    # Test case 366
    try:
        result = arraySum([2, 8, 16, 32, 65, 128, 258, 0, -400])
        assert result == 109, f"Test 366 failed: got {result}, expected {109}"
        print(f"Test 366 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 366 failed: {e}")
        test_results.append(False)

    # Test case 367
    try:
        result = arraySum([-2, -4, -8, -16, -32, -64, -128, -256, 0])
        assert result == -510, f"Test 367 failed: got {result}, expected {-510}"
        print(f"Test 367 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 367 failed: {e}")
        test_results.append(False)

    # Test case 368
    try:
        result = arraySum([-256, -128, -64, -32, -16, -8, -4, -2, -101])
        assert result == -611, f"Test 368 failed: got {result}, expected {-611}"
        print(f"Test 368 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 368 failed: {e}")
        test_results.append(False)

    # Test case 369
    try:
        result = arraySum([-2, -9, -16, 32, -64, -128, -256])
        assert result == -443, f"Test 369 failed: got {result}, expected {-443}"
        print(f"Test 369 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 369 failed: {e}")
        test_results.append(False)

    # Test case 370
    try:
        result = arraySum([-256, -128, -64, -32, -16, -8, -4, -4])
        assert result == -512, f"Test 370 failed: got {result}, expected {-512}"
        print(f"Test 370 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 370 failed: {e}")
        test_results.append(False)

    # Test case 371
    try:
        result = arraySum([0, 0, -256, -128, -64, -32, -16, -8, -4, -2, 0])
        assert result == -510, f"Test 371 failed: got {result}, expected {-510}"
        print(f"Test 371 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 371 failed: {e}")
        test_results.append(False)

    # Test case 372
    try:
        result = arraySum([0, 0, -128, -64, -32, -16, -8, -4, -2])
        assert result == -254, f"Test 372 failed: got {result}, expected {-254}"
        print(f"Test 372 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 372 failed: {e}")
        test_results.append(False)

    # Test case 373
    try:
        result = arraySum([-2, -8, -16, 999999999999999999999999, -64, -128, -256])
        assert result == 999999999999999999999525, f"Test 373 failed: got {result}, expected {999999999999999999999525}"
        print(f"Test 373 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 373 failed: {e}")
        test_results.append(False)

    # Test case 374
    try:
        result = arraySum([-256, -128, -64, -32, -16, -8, -2])
        assert result == -506, f"Test 374 failed: got {result}, expected {-506}"
        print(f"Test 374 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 374 failed: {e}")
        test_results.append(False)

    # Test case 375
    try:
        result = arraySum([0, -256, -128, -64, -32, -16, -8, -4, -2, 5, 0])
        assert result == -505, f"Test 375 failed: got {result}, expected {-505}"
        print(f"Test 375 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 375 failed: {e}")
        test_results.append(False)

    # Test case 376
    try:
        result = arraySum([-2, 999999999999999999999999, -16, -32, -64, -128, -256, 4294967294, 0, 0])
        assert result == 1000000000000004294966795, f"Test 376 failed: got {result}, expected {1000000000000004294966795}"
        print(f"Test 376 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 376 failed: {e}")
        test_results.append(False)

    # Test case 377
    try:
        result = arraySum([0, -256, -128, -64, -32, -16, -8, -4, -2])
        assert result == -510, f"Test 377 failed: got {result}, expected {-510}"
        print(f"Test 377 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 377 failed: {e}")
        test_results.append(False)

    # Test case 378
    try:
        result = arraySum([-256, -128, -64, -32, -16, -8, -4, -2, 0])
        assert result == -510, f"Test 378 failed: got {result}, expected {-510}"
        print(f"Test 378 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 378 failed: {e}")
        test_results.append(False)

    # Test case 379
    try:
        result = arraySum([-9223372036854775808, -256, -128, -64, -32, -16, -8, -4, -2])
        assert result == -9223372036854776318, f"Test 379 failed: got {result}, expected {-9223372036854776318}"
        print(f"Test 379 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 379 failed: {e}")
        test_results.append(False)

    # Test case 380
    try:
        result = arraySum([-2, -4, -8, -16, -32, -64, -128, -256, 199, 13, -198, -66, -12345678901234567890])
        assert result == -12345678901234568452, f"Test 380 failed: got {result}, expected {-12345678901234568452}"
        print(f"Test 380 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 380 failed: {e}")
        test_results.append(False)

    # Test case 381
    try:
        result = arraySum([-255, -128, -64, -32, -16, -8, -4, -2, -8])
        assert result == -517, f"Test 381 failed: got {result}, expected {-517}"
        print(f"Test 381 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 381 failed: {e}")
        test_results.append(False)

    # Test case 382
    try:
        result = arraySum([11, 33, -44, 55, -66, 77, -88, 99, 41])
        assert result == 118, f"Test 382 failed: got {result}, expected {118}"
        print(f"Test 382 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 382 failed: {e}")
        test_results.append(False)

    # Test case 383
    try:
        result = arraySum([11, 1, 33, 55, -66, 77])
        assert result == 111, f"Test 383 failed: got {result}, expected {111}"
        print(f"Test 383 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 383 failed: {e}")
        test_results.append(False)

    # Test case 384
    try:
        result = arraySum([99, -88, 77, -134, -44, 33, -22, 11, 200])
        assert result == 132, f"Test 384 failed: got {result}, expected {132}"
        print(f"Test 384 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 384 failed: {e}")
        test_results.append(False)

    # Test case 385
    try:
        result = arraySum([11, -22, 33, -44, 55, -66, 77, -88, 99, 3141592653589793])
        assert result == 3141592653589848, f"Test 385 failed: got {result}, expected {3141592653589848}"
        print(f"Test 385 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 385 failed: {e}")
        test_results.append(False)

    # Test case 386
    try:
        result = arraySum([0, 99, -88, 77, -66, 55, -44, 33, 128, 11, 0, 0])
        assert result == 205, f"Test 386 failed: got {result}, expected {205}"
        print(f"Test 386 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 386 failed: {e}")
        test_results.append(False)

    # Test case 387
    try:
        result = arraySum([99, -88, 77, -66, 55, -44, 33, -22, 11])
        assert result == 55, f"Test 387 failed: got {result}, expected {55}"
        print(f"Test 387 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 387 failed: {e}")
        test_results.append(False)

    # Test case 388
    try:
        result = arraySum([11, -22, 33, -44, 55, 0, 77, -88, 99, -4, 4, 0])
        assert result == 121, f"Test 388 failed: got {result}, expected {121}"
        print(f"Test 388 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 388 failed: {e}")
        test_results.append(False)

    # Test case 389
    try:
        result = arraySum([99, -88, -66, 55, -44, 33, -22, 11])
        assert result == -22, f"Test 389 failed: got {result}, expected {-22}"
        print(f"Test 389 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 389 failed: {e}")
        test_results.append(False)

    # Test case 390
    try:
        result = arraySum([11, -23, 33, -44, -66, 77, -88, 99, 0, 0])
        assert result == -1, f"Test 390 failed: got {result}, expected {-1}"
        print(f"Test 390 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 390 failed: {e}")
        test_results.append(False)

    # Test case 391
    try:
        result = arraySum([11, 33, -44, 55, -66, 77, -88, 99, 0, 0, 0])
        assert result == 77, f"Test 391 failed: got {result}, expected {77}"
        print(f"Test 391 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 391 failed: {e}")
        test_results.append(False)

    # Test case 392
    try:
        result = arraySum([-1000000000000000000000001, 0, 11, -22, 33, -44, 55, -66, 77, -88, 99, 0])
        assert result == -999999999999999999999946, f"Test 392 failed: got {result}, expected {-999999999999999999999946}"
        print(f"Test 392 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 392 failed: {e}")
        test_results.append(False)

    # Test case 393
    try:
        result = arraySum([11, -22, 33, -44, -2, -66, 77, -88, 99])
        assert result == -2, f"Test 393 failed: got {result}, expected {-2}"
        print(f"Test 393 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 393 failed: {e}")
        test_results.append(False)

    # Test case 394
    try:
        result = arraySum([11, -22, 33, -44, 55, -66, -88, 99, 0])
        assert result == -22, f"Test 394 failed: got {result}, expected {-22}"
        print(f"Test 394 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 394 failed: {e}")
        test_results.append(False)

    # Test case 395
    try:
        result = arraySum([0, 0, 0, 0, 0, 0, 0, 0, 1])
        assert result == 1, f"Test 395 failed: got {result}, expected {1}"
        print(f"Test 395 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 395 failed: {e}")
        test_results.append(False)

    # Test case 396
    try:
        result = arraySum([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        assert result == 1, f"Test 396 failed: got {result}, expected {1}"
        print(f"Test 396 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 396 failed: {e}")
        test_results.append(False)

    # Test case 397
    try:
        result = arraySum([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 199])
        assert result == 200, f"Test 397 failed: got {result}, expected {200}"
        print(f"Test 397 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 397 failed: {e}")
        test_results.append(False)

    # Test case 398
    try:
        result = arraySum([1, 0, 0, 0, 0, 0, 0, 0, -1999999997, 18446744073709551616, 0])
        assert result == 18446744071709551620, f"Test 398 failed: got {result}, expected {18446744071709551620}"
        print(f"Test 398 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 398 failed: {e}")
        test_results.append(False)

    # Test case 399
    try:
        result = arraySum([-123456791, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
        assert result == -123456790, f"Test 399 failed: got {result}, expected {-123456790}"
        print(f"Test 399 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 399 failed: {e}")
        test_results.append(False)

    # Test case 400
    try:
        result = arraySum([0, 0, 0, 0, 0, 1, 0, 0, 0, 1])
        assert result == 2, f"Test 400 failed: got {result}, expected {2}"
        print(f"Test 400 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 400 failed: {e}")
        test_results.append(False)

    # Test case 401
    try:
        result = arraySum([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3141592653589793, -123456791])
        assert result == 3141592530133003, f"Test 401 failed: got {result}, expected {3141592530133003}"
        print(f"Test 401 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 401 failed: {e}")
        test_results.append(False)

    # Test case 402
    try:
        result = arraySum([1, 0, 0, 0, 0, 0, 0, 0, 0])
        assert result == 1, f"Test 402 failed: got {result}, expected {1}"
        print(f"Test 402 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 402 failed: {e}")
        test_results.append(False)

    # Test case 403
    try:
        result = arraySum([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
        assert result == 1, f"Test 403 failed: got {result}, expected {1}"
        print(f"Test 403 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 403 failed: {e}")
        test_results.append(False)

    # Test case 404
    try:
        result = arraySum([-2, -2147483647, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        assert result == -2147483648, f"Test 404 failed: got {result}, expected {-2147483648}"
        print(f"Test 404 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 404 failed: {e}")
        test_results.append(False)

    # Test case 405
    try:
        result = arraySum([1, 3, 4, 5, 6, 7, 8, 9, -4, -22, -300])
        assert result == -283, f"Test 405 failed: got {result}, expected {-283}"
        print(f"Test 405 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 405 failed: {e}")
        test_results.append(False)

    # Test case 406
    try:
        result = arraySum([-8589934590, 1, 2, 3, 4, 6, 6, 7, 8, 9, -198])
        assert result == -8589934742, f"Test 406 failed: got {result}, expected {-8589934742}"
        print(f"Test 406 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 406 failed: {e}")
        test_results.append(False)

    # Test case 407
    try:
        result = arraySum([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, -32, 0])
        assert result == 13, f"Test 407 failed: got {result}, expected {13}"
        print(f"Test 407 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 407 failed: {e}")
        test_results.append(False)

    # Test case 408
    try:
        result = arraySum([9, 8, 7, 6, 5, 4, 3, 0, 0, 0, 2147483650])
        assert result == 2147483692, f"Test 408 failed: got {result}, expected {2147483692}"
        print(f"Test 408 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 408 failed: {e}")
        test_results.append(False)

    # Test case 409
    try:
        result = arraySum([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        assert result == 45, f"Test 409 failed: got {result}, expected {45}"
        print(f"Test 409 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 409 failed: {e}")
        test_results.append(False)

    # Test case 410
    try:
        result = arraySum([1, 3, 4, 5, 6, 7, 8, 9])
        assert result == 43, f"Test 410 failed: got {result}, expected {43}"
        print(f"Test 410 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 410 failed: {e}")
        test_results.append(False)

    # Test case 411
    try:
        result = arraySum([0, 2, 4, 4, 5, 6, 7, 8, 9, 2147483647])
        assert result == 2147483692, f"Test 411 failed: got {result}, expected {2147483692}"
        print(f"Test 411 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 411 failed: {e}")
        test_results.append(False)

    # Test case 412
    try:
        result = arraySum([42, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert result == 87, f"Test 412 failed: got {result}, expected {87}"
        print(f"Test 412 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 412 failed: {e}")
        test_results.append(False)

    # Test case 413
    try:
        result = arraySum([1, 2, 14, 4, 5, 6, 7, 8, 9, 65])
        assert result == 121, f"Test 413 failed: got {result}, expected {121}"
        print(f"Test 413 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 413 failed: {e}")
        test_results.append(False)

    # Test case 414
    try:
        result = arraySum([9, 8, 7, 6, 5, 4, 3, 2, 13])
        assert result == 57, f"Test 414 failed: got {result}, expected {57}"
        print(f"Test 414 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 414 failed: {e}")
        test_results.append(False)

    # Test case 415
    try:
        result = arraySum([9, 8, 7, 1, 5, 4, 3, 2, 1, 2147483647, 77])
        assert result == 2147483764, f"Test 415 failed: got {result}, expected {2147483764}"
        print(f"Test 415 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 415 failed: {e}")
        test_results.append(False)

    # Test case 416
    try:
        result = arraySum([9, 7, 6, 5, 6, 3, 2, 1])
        assert result == 39, f"Test 416 failed: got {result}, expected {39}"
        print(f"Test 416 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 416 failed: {e}")
        test_results.append(False)

    # Test case 417
    try:
        result = arraySum([-7, 1, 2, 2, 4, 5, 6, 7, 8, 9])
        assert result == 37, f"Test 417 failed: got {result}, expected {37}"
        print(f"Test 417 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 417 failed: {e}")
        test_results.append(False)

    # Test case 418
    try:
        result = arraySum([1, 2, 4, 5, 6, 7, 8, 9])
        assert result == 42, f"Test 418 failed: got {result}, expected {42}"
        print(f"Test 418 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 418 failed: {e}")
        test_results.append(False)

    # Test case 419
    try:
        result = arraySum([-9, -8, -7, -6, -5, -4, -3, -1])
        assert result == -43, f"Test 419 failed: got {result}, expected {-43}"
        print(f"Test 419 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 419 failed: {e}")
        test_results.append(False)

    # Test case 420
    try:
        result = arraySum([-8, -7, -6, -10, -4, -3, -2, -1, -9223372036854775807])
        assert result == -9223372036854775848, f"Test 420 failed: got {result}, expected {-9223372036854775848}"
        print(f"Test 420 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 420 failed: {e}")
        test_results.append(False)

    # Test case 421
    try:
        result = arraySum([-2, -2, -3, -4, -5, -6, -7, -8, -9, 0])
        assert result == -46, f"Test 421 failed: got {result}, expected {-46}"
        print(f"Test 421 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 421 failed: {e}")
        test_results.append(False)

    # Test case 422
    try:
        result = arraySum([9, -8, -7, 8, -5, -4, -3, -2, -1])
        assert result == -13, f"Test 422 failed: got {result}, expected {-13}"
        print(f"Test 422 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 422 failed: {e}")
        test_results.append(False)

    # Test case 423
    try:
        result = arraySum([-12345678901234567890, -2, -3, -4, -5, -6, 7, -7, -9])
        assert result == -12345678901234567919, f"Test 423 failed: got {result}, expected {-12345678901234567919}"
        print(f"Test 423 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 423 failed: {e}")
        test_results.append(False)

    # Test case 424
    try:
        result = arraySum([-9, -8, -7, -6, -5, -4, -3, -1, -134, 0])
        assert result == -177, f"Test 424 failed: got {result}, expected {-177}"
        print(f"Test 424 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 424 failed: {e}")
        test_results.append(False)

    # Test case 425
    try:
        result = arraySum([0, 9223372036854775806, -2, -3, -4, -5, -6, -7, -8, -9])
        assert result == 9223372036854775762, f"Test 425 failed: got {result}, expected {9223372036854775762}"
        print(f"Test 425 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 425 failed: {e}")
        test_results.append(False)

    # Test case 426
    try:
        result = arraySum([-9, -8, -7, -6, -5, -4, -3, -2, -1, 999999999])
        assert result == 999999954, f"Test 426 failed: got {result}, expected {999999954}"
        print(f"Test 426 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 426 failed: {e}")
        test_results.append(False)

    # Test case 427
    try:
        result = arraySum([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0])
        assert result == -45, f"Test 427 failed: got {result}, expected {-45}"
        print(f"Test 427 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 427 failed: {e}")
        test_results.append(False)

    # Test case 428
    try:
        result = arraySum([-9, -8, -7, -6, -5, -4, -3, -2, 1, 0])
        assert result == -43, f"Test 428 failed: got {result}, expected {-43}"
        print(f"Test 428 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 428 failed: {e}")
        test_results.append(False)

    # Test case 429
    try:
        result = arraySum([-9, -10, -7, -6, -5, -4, -2, -1])
        assert result == -44, f"Test 429 failed: got {result}, expected {-44}"
        print(f"Test 429 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 429 failed: {e}")
        test_results.append(False)

    # Test case 430
    try:
        result = arraySum([-9, -8, -7, 6, -5, -4, -2, -2, -1])
        assert result == -32, f"Test 430 failed: got {result}, expected {-32}"
        print(f"Test 430 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 430 failed: {e}")
        test_results.append(False)

    # Test case 431
    try:
        result = arraySum([-8, -7, -5, -5, 2147483647, -3, -2, 0])
        assert result == 2147483617, f"Test 431 failed: got {result}, expected {2147483617}"
        print(f"Test 431 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 431 failed: {e}")
        test_results.append(False)

    # Test case 432
    try:
        result = arraySum([-9, -7, -6, -5, -4, -3, -2, -1])
        assert result == -37, f"Test 432 failed: got {result}, expected {-37}"
        print(f"Test 432 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 432 failed: {e}")
        test_results.append(False)

    # Test case 433
    try:
        result = arraySum([-9, -8, -7, 6, -5, -4, -3, -2, -1, 0])
        assert result == -33, f"Test 433 failed: got {result}, expected {-33}"
        print(f"Test 433 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 433 failed: {e}")
        test_results.append(False)

    # Test case 434
    try:
        result = arraySum([3141592653589793, -2718281828459045, 1618033988749893, 0])
        assert result == 2041344813880641, f"Test 434 failed: got {result}, expected {2041344813880641}"
        print(f"Test 434 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 434 failed: {e}")
        test_results.append(False)

    # Test case 435
    try:
        result = arraySum([3141592653589793, -2718281828459045, 1618033988749894, -14, 0, 0, -200])
        assert result == 2041344813880428, f"Test 435 failed: got {result}, expected {2041344813880428}"
        print(f"Test 435 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 435 failed: {e}")
        test_results.append(False)

    # Test case 436
    try:
        result = arraySum([0, 0, 3141592653589793])
        assert result == 3141592653589793, f"Test 436 failed: got {result}, expected {3141592653589793}"
        print(f"Test 436 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 436 failed: {e}")
        test_results.append(False)

    # Test case 437
    try:
        result = arraySum([3141592653589794, 18446744073709551614])
        assert result == 18449885666363141408, f"Test 437 failed: got {result}, expected {18449885666363141408}"
        print(f"Test 437 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 437 failed: {e}")
        test_results.append(False)

    # Test case 438
    try:
        result = arraySum([1618033988749894, -2718281828459045, 3141592653589793, 0])
        assert result == 2041344813880642, f"Test 438 failed: got {result}, expected {2041344813880642}"
        print(f"Test 438 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 438 failed: {e}")
        test_results.append(False)

    # Test case 439
    try:
        result = arraySum([0, 1618033988749894, -2718281828459045, 6283185307179586])
        assert result == 5182937467470435, f"Test 439 failed: got {result}, expected {5182937467470435}"
        print(f"Test 439 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 439 failed: {e}")
        test_results.append(False)

    # Test case 440
    try:
        result = arraySum([12345678901234567890, 3141592653589793, -2718281828459045, 9223372036854775807])
        assert result == 21569474248914474445, f"Test 440 failed: got {result}, expected {21569474248914474445}"
        print(f"Test 440 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 440 failed: {e}")
        test_results.append(False)

    # Test case 441
    try:
        result = arraySum([-2718281828459045, 1618033988749894, 0])
        assert result == -1100247839709151, f"Test 441 failed: got {result}, expected {-1100247839709151}"
        print(f"Test 441 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 441 failed: {e}")
        test_results.append(False)

    # Test case 442
    try:
        result = arraySum([-2718281828459045, 1618033988749894])
        assert result == -1100247839709151, f"Test 442 failed: got {result}, expected {-1100247839709151}"
        print(f"Test 442 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 442 failed: {e}")
        test_results.append(False)

    # Test case 443
    try:
        result = arraySum([3141592653589793, -2718281828459045, 1618033988749894, -23, 0])
        assert result == 2041344813880619, f"Test 443 failed: got {result}, expected {2041344813880619}"
        print(f"Test 443 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 443 failed: {e}")
        test_results.append(False)

    # Test case 444
    try:
        result = arraySum([-999999999, 1618033988749894, -2718281828459045, 3141592653589793])
        assert result == 2041343813880643, f"Test 444 failed: got {result}, expected {2041343813880643}"
        print(f"Test 444 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 444 failed: {e}")
        test_results.append(False)

    # Test case 445
    try:
        result = arraySum([3141592653589793, -2718281828459045, 3236067977499788, 65, 0])
        assert result == 3659378802630601, f"Test 445 failed: got {result}, expected {3659378802630601}"
        print(f"Test 445 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 445 failed: {e}")
        test_results.append(False)

    # Test case 446
    try:
        result = arraySum([3141592653589793, -2718281828459045, 1618033988749894, 1618033988749894])
        assert result == 3659378802630536, f"Test 446 failed: got {result}, expected {3659378802630536}"
        print(f"Test 446 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 446 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
