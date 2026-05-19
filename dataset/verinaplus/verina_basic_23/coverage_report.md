# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def differenceMinMax(a):
2: ✓     return max(a) - min(a)
```

## Complete Test File

```python
def differenceMinMax(a):
    return max(a) - min(a)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        assert result == 8, f"Test 1 failed: got {result}, expected {8}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = differenceMinMax([10, 20, 30, 40, 50])
        assert result == 40, f"Test 2 failed: got {result}, expected {40}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = differenceMinMax([-10, -20, -30, -40, -50])
        assert result == 40, f"Test 3 failed: got {result}, expected {40}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = differenceMinMax([7])
        assert result == 0, f"Test 4 failed: got {result}, expected {0}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = differenceMinMax([5, 5, 5, 5])
        assert result == 0, f"Test 5 failed: got {result}, expected {0}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = differenceMinMax([1, -1, 2, -2])
        assert result == 4, f"Test 6 failed: got {result}, expected {4}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = differenceMinMax([42])
        assert result == 0, f"Test 7 failed: got {result}, expected {0}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = differenceMinMax([-42])
        assert result == 0, f"Test 8 failed: got {result}, expected {0}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = differenceMinMax([5, 5])
        assert result == 0, f"Test 9 failed: got {result}, expected {0}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = differenceMinMax([1, 2])
        assert result == 1, f"Test 10 failed: got {result}, expected {1}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = differenceMinMax([2, 1])
        assert result == 1, f"Test 11 failed: got {result}, expected {1}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = differenceMinMax([-1, 1])
        assert result == 2, f"Test 12 failed: got {result}, expected {2}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = differenceMinMax([-5, -10, -3, -20])
        assert result == 17, f"Test 13 failed: got {result}, expected {17}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == 8, f"Test 14 failed: got {result}, expected {8}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = differenceMinMax([50, 40, 30, 20, 10])
        assert result == 40, f"Test 15 failed: got {result}, expected {40}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = differenceMinMax([1000000000000, -1000000000000])
        assert result == 2000000000000, f"Test 16 failed: got {result}, expected {2000000000000}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = differenceMinMax([9223372036854775807, -9223372036854775808])
        assert result == 18446744073709551615, f"Test 17 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = differenceMinMax([1, -1, 1, -1, 1, -1])
        assert result == 2, f"Test 18 failed: got {result}, expected {2}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = differenceMinMax([-2147483648, 0, 2147483647])
        assert result == 4294967295, f"Test 19 failed: got {result}, expected {4294967295}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = differenceMinMax([7, 7, 7, 7, 7])
        assert result == 0, f"Test 20 failed: got {result}, expected {0}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = differenceMinMax([0, -1, -2, -3, -4, -5])
        assert result == 5, f"Test 21 failed: got {result}, expected {5}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = differenceMinMax([0, 1, 2, 3, 4, 5])
        assert result == 5, f"Test 22 failed: got {result}, expected {5}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = differenceMinMax([999999999999999999999999, -999999999999999999999998, 0])
        assert result == 1999999999999999999999997, f"Test 23 failed: got {result}, expected {1999999999999999999999997}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = differenceMinMax([-3, -3, -3, -2, -2, -1])
        assert result == 2, f"Test 24 failed: got {result}, expected {2}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = differenceMinMax([8, -8, 8, -8, 8])
        assert result == 16, f"Test 25 failed: got {result}, expected {16}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = differenceMinMax([13, -21, 34, -55, 89, -144])
        assert result == 233, f"Test 26 failed: got {result}, expected {233}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = differenceMinMax([2, 3, 5, 7, 11, 13, 17, 19])
        assert result == 17, f"Test 27 failed: got {result}, expected {17}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = differenceMinMax([19, 17, 13, 11, 7, 5, 3, 2])
        assert result == 17, f"Test 28 failed: got {result}, expected {17}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = differenceMinMax([4, -4])
        assert result == 8, f"Test 29 failed: got {result}, expected {8}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = differenceMinMax([-100, 100, -100, 100])
        assert result == 200, f"Test 30 failed: got {result}, expected {200}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = differenceMinMax([6, 0, 6, 0, 6, 0])
        assert result == 6, f"Test 31 failed: got {result}, expected {6}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = differenceMinMax([-999999, -1000000, -999998])
        assert result == 2, f"Test 32 failed: got {result}, expected {2}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = differenceMinMax([123456789, 987654321, -123456789, -987654321])
        assert result == 1975308642, f"Test 33 failed: got {result}, expected {1975308642}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = differenceMinMax([1, 1, 2, 3, 5, 8, 13, 21, 34])
        assert result == 33, f"Test 34 failed: got {result}, expected {33}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = differenceMinMax([3, 1, 4, 5, 9, 2, 6, 5, 3, 5])
        assert result == 8, f"Test 35 failed: got {result}, expected {8}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 6, 0])
        assert result == 9, f"Test 36 failed: got {result}, expected {9}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = differenceMinMax([3, -999998, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0, 0, 50])
        assert result == 1000048, f"Test 37 failed: got {result}, expected {1000048}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = differenceMinMax([3, 2, 8, 1, 5, 9, 2, 6, 5, 3, 5, 9, 0])
        assert result == 9, f"Test 38 failed: got {result}, expected {9}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0])
        assert result == 9, f"Test 39 failed: got {result}, expected {9}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = differenceMinMax([6, 1, 4, 1, 5, 9, 2, 5, 3, 5, 6])
        assert result == 8, f"Test 40 failed: got {result}, expected {8}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = differenceMinMax([3, 4, 1, 5, 2, 6, 5, 3, 5, 0])
        assert result == 6, f"Test 41 failed: got {result}, expected {6}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = differenceMinMax([5, 3, 5, 6, 2, 9, 5, 1, 4, 1])
        assert result == 8, f"Test 42 failed: got {result}, expected {8}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = differenceMinMax([-21, 5, 3, 5, 6, 1, 9, 5, 1, 4, 1, 11])
        assert result == 32, f"Test 43 failed: got {result}, expected {32}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = differenceMinMax([0, 5, 3, 5, 6, 2, 9, 5, 4, 1, -3])
        assert result == 12, f"Test 44 failed: got {result}, expected {12}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = differenceMinMax([5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 6, 0, 0, 0])
        assert result == 9, f"Test 45 failed: got {result}, expected {9}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = differenceMinMax([5, 3, 5, 6, 9, 5, 1, 4, 3])
        assert result == 8, f"Test 46 failed: got {result}, expected {8}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 30])
        assert result == 29, f"Test 47 failed: got {result}, expected {29}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = differenceMinMax([0, 5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3])
        assert result == 9, f"Test 48 failed: got {result}, expected {9}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = differenceMinMax([10, 20, 40, 50])
        assert result == 40, f"Test 49 failed: got {result}, expected {40}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = differenceMinMax([10, 20, 30, 40, 50, -40])
        assert result == 90, f"Test 50 failed: got {result}, expected {90}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = differenceMinMax([50, 40, 30, 20])
        assert result == 30, f"Test 51 failed: got {result}, expected {30}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = differenceMinMax([-50, 21, 30, 20, 10, 0])
        assert result == 80, f"Test 52 failed: got {result}, expected {80}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = differenceMinMax([0, 50, 40, 999999999999999999999999, 20, 9, 0])
        assert result == 999999999999999999999999, f"Test 53 failed: got {result}, expected {999999999999999999999999}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = differenceMinMax([-5, 50, 40, 30, 20, 10])
        assert result == 55, f"Test 54 failed: got {result}, expected {55}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = differenceMinMax([-999999999999999999999998, 20, 30, 0, 50])
        assert result == 1000000000000000000000048, f"Test 55 failed: got {result}, expected {1000000000000000000000048}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = differenceMinMax([10, 20, 30, 40, 50, -2147483648, 0, 987654321])
        assert result == 3135137969, f"Test 56 failed: got {result}, expected {3135137969}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = differenceMinMax([50, 40, 30, 21, 10])
        assert result == 40, f"Test 57 failed: got {result}, expected {40}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = differenceMinMax([10, 20, 30, 40, 50, 0])
        assert result == 50, f"Test 58 failed: got {result}, expected {50}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = differenceMinMax([10, 20, 30, 40, 50, 10])
        assert result == 40, f"Test 59 failed: got {result}, expected {40}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = differenceMinMax([34, 50, 40, 30, 20, 10])
        assert result == 40, f"Test 60 failed: got {result}, expected {40}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = differenceMinMax([10, 20, 30, 50, -2147483648, 3])
        assert result == 2147483698, f"Test 61 failed: got {result}, expected {2147483698}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = differenceMinMax([20, 30, 40, 50, 9223372036854775807, 0, 0])
        assert result == 9223372036854775807, f"Test 62 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = differenceMinMax([-10, -20, -30, -40, -50, 0])
        assert result == 50, f"Test 63 failed: got {result}, expected {50}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = differenceMinMax([0, -40, -30, -20, -10, 11, -20])
        assert result == 51, f"Test 64 failed: got {result}, expected {51}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = differenceMinMax([-50, 40, -30, -20])
        assert result == 90, f"Test 65 failed: got {result}, expected {90}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = differenceMinMax([-10, -20, -30, -40, -50, 30, 50, 0])
        assert result == 100, f"Test 66 failed: got {result}, expected {100}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = differenceMinMax([-10, -40, -50, 0, 0])
        assert result == 50, f"Test 67 failed: got {result}, expected {50}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = differenceMinMax([-20, -20, -31, -40, -50, -10, 0])
        assert result == 50, f"Test 68 failed: got {result}, expected {50}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = differenceMinMax([0, -40, -30, -20, -11])
        assert result == 40, f"Test 69 failed: got {result}, expected {40}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = differenceMinMax([-10, -40, -50])
        assert result == 40, f"Test 70 failed: got {result}, expected {40}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = differenceMinMax([-10, -20, -30, -40, 0])
        assert result == 40, f"Test 71 failed: got {result}, expected {40}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = differenceMinMax([-8, -50, -40, -30, -20, -10])
        assert result == 42, f"Test 72 failed: got {result}, expected {42}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = differenceMinMax([-10, -20, -30, -50])
        assert result == 40, f"Test 73 failed: got {result}, expected {40}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = differenceMinMax([-2, -50, -40, -30, -20, -10])
        assert result == 48, f"Test 74 failed: got {result}, expected {48}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = differenceMinMax([-10, -20, -30, -40, -50, -2147483648])
        assert result == 2147483638, f"Test 75 failed: got {result}, expected {2147483638}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = differenceMinMax([-10, -60, -50, 0])
        assert result == 60, f"Test 76 failed: got {result}, expected {60}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = differenceMinMax([-51, -40, 11, -20, -10])
        assert result == 62, f"Test 77 failed: got {result}, expected {62}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = differenceMinMax([0, 0])
        assert result == 0, f"Test 78 failed: got {result}, expected {0}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = differenceMinMax([7, 0])
        assert result == 7, f"Test 79 failed: got {result}, expected {7}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = differenceMinMax([-40, 42, 7])
        assert result == 82, f"Test 80 failed: got {result}, expected {82}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = differenceMinMax([7, 0, 987654321, 0])
        assert result == 987654321, f"Test 81 failed: got {result}, expected {987654321}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = differenceMinMax([-6, 1, -999999])
        assert result == 1000000, f"Test 82 failed: got {result}, expected {1000000}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = differenceMinMax([7, 0, -31])
        assert result == 38, f"Test 83 failed: got {result}, expected {38}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = differenceMinMax([8, 0])
        assert result == 8, f"Test 84 failed: got {result}, expected {8}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = differenceMinMax([0, 7])
        assert result == 7, f"Test 85 failed: got {result}, expected {7}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = differenceMinMax([-123456789, 0, 7, -8, 0])
        assert result == 123456796, f"Test 86 failed: got {result}, expected {123456796}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = differenceMinMax([7, 21, 0, 9])
        assert result == 21, f"Test 87 failed: got {result}, expected {21}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = differenceMinMax([7, -19])
        assert result == 26, f"Test 88 failed: got {result}, expected {26}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = differenceMinMax([-1])
        assert result == 0, f"Test 89 failed: got {result}, expected {0}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = differenceMinMax([0, -1000000])
        assert result == 1000000, f"Test 90 failed: got {result}, expected {1000000}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = differenceMinMax([5, 5, 5, -1000000])
        assert result == 1000005, f"Test 91 failed: got {result}, expected {1000005}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = differenceMinMax([5, 5, 5, -55])
        assert result == 60, f"Test 92 failed: got {result}, expected {60}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = differenceMinMax([5, 5, 5, 5, -31])
        assert result == 36, f"Test 93 failed: got {result}, expected {36}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = differenceMinMax([5, 1, 5, 5])
        assert result == 4, f"Test 94 failed: got {result}, expected {4}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = differenceMinMax([5, 5, 5, 0, 20, 0])
        assert result == 20, f"Test 95 failed: got {result}, expected {20}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = differenceMinMax([5, 5, 6, 5, 0])
        assert result == 6, f"Test 96 failed: got {result}, expected {6}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = differenceMinMax([5, 5, 42, 4, 987654321, 0])
        assert result == 987654321, f"Test 97 failed: got {result}, expected {987654321}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = differenceMinMax([5, 5, 5, 0])
        assert result == 5, f"Test 98 failed: got {result}, expected {5}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = differenceMinMax([5, 5, -1000000000000, 0])
        assert result == 1000000000005, f"Test 99 failed: got {result}, expected {1000000000005}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = differenceMinMax([-4, 5, 5, 5, 5])
        assert result == 9, f"Test 100 failed: got {result}, expected {9}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = differenceMinMax([4, 5, 8])
        assert result == 4, f"Test 101 failed: got {result}, expected {4}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = differenceMinMax([5, 5, 0])
        assert result == 5, f"Test 102 failed: got {result}, expected {5}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = differenceMinMax([1, -1, 2, -2, 89])
        assert result == 91, f"Test 103 failed: got {result}, expected {91}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = differenceMinMax([3, -2, 0, 0, 1])
        assert result == 5, f"Test 104 failed: got {result}, expected {5}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = differenceMinMax([1, -1, 2, -2, -11])
        assert result == 13, f"Test 105 failed: got {result}, expected {13}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = differenceMinMax([0, 0, -2, 2, 1])
        assert result == 4, f"Test 106 failed: got {result}, expected {4}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = differenceMinMax([1, -1, 2, -2, 0, 89])
        assert result == 91, f"Test 107 failed: got {result}, expected {91}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = differenceMinMax([1, -1, 2, -2, 9223372036854775807])
        assert result == 9223372036854775809, f"Test 108 failed: got {result}, expected {9223372036854775809}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = differenceMinMax([-2, 2, 11])
        assert result == 13, f"Test 109 failed: got {result}, expected {13}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = differenceMinMax([-2, 2, -1, 1, 0, -3, 4, -999999999999999999999998])
        assert result == 1000000000000000000000002, f"Test 110 failed: got {result}, expected {1000000000000000000000002}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = differenceMinMax([-2, 2, -1, 1])
        assert result == 4, f"Test 111 failed: got {result}, expected {4}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = differenceMinMax([0, 1, -1, 2, -2])
        assert result == 4, f"Test 112 failed: got {result}, expected {4}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = differenceMinMax([-2, 2, -1])
        assert result == 4, f"Test 113 failed: got {result}, expected {4}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = differenceMinMax([-2, 2])
        assert result == 4, f"Test 114 failed: got {result}, expected {4}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = differenceMinMax([1, -1, 2])
        assert result == 3, f"Test 115 failed: got {result}, expected {3}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = differenceMinMax([1, 1, -2])
        assert result == 3, f"Test 116 failed: got {result}, expected {3}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = differenceMinMax([-2, 2, 0, 17])
        assert result == 19, f"Test 117 failed: got {result}, expected {19}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = differenceMinMax([1, 20, 0])
        assert result == 20, f"Test 118 failed: got {result}, expected {20}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = differenceMinMax([0, 1, 0])
        assert result == 1, f"Test 119 failed: got {result}, expected {1}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = differenceMinMax([0, 0, 50, -21])
        assert result == 71, f"Test 120 failed: got {result}, expected {71}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = differenceMinMax([-9])
        assert result == 0, f"Test 121 failed: got {result}, expected {0}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = differenceMinMax([-1000000000001, -9223372036854775808])
        assert result == 9223371036854775807, f"Test 122 failed: got {result}, expected {9223371036854775807}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = differenceMinMax([0, 0, -42])
        assert result == 42, f"Test 123 failed: got {result}, expected {42}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = differenceMinMax([0, -999998, 0])
        assert result == 999998, f"Test 124 failed: got {result}, expected {999998}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = differenceMinMax([5, 0])
        assert result == 5, f"Test 125 failed: got {result}, expected {5}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = differenceMinMax([0, 50])
        assert result == 50, f"Test 126 failed: got {result}, expected {50}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = differenceMinMax([0, -987654321, -42, 0, -42])
        assert result == 987654321, f"Test 127 failed: got {result}, expected {987654321}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = differenceMinMax([0, 0, -2147483648])
        assert result == 2147483648, f"Test 128 failed: got {result}, expected {2147483648}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = differenceMinMax([0, 0, 11])
        assert result == 11, f"Test 129 failed: got {result}, expected {11}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = differenceMinMax([-4, 0, 0])
        assert result == 4, f"Test 130 failed: got {result}, expected {4}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = differenceMinMax([0, -8])
        assert result == 8, f"Test 131 failed: got {result}, expected {8}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = differenceMinMax([0, -40])
        assert result == 40, f"Test 132 failed: got {result}, expected {40}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = differenceMinMax([-19, 0])
        assert result == 19, f"Test 133 failed: got {result}, expected {19}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = differenceMinMax([1000000000000, 0])
        assert result == 1000000000000, f"Test 134 failed: got {result}, expected {1000000000000}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = differenceMinMax([41])
        assert result == 0, f"Test 135 failed: got {result}, expected {0}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = differenceMinMax([-2147483648, 42])
        assert result == 2147483690, f"Test 136 failed: got {result}, expected {2147483690}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = differenceMinMax([42, -1, 0])
        assert result == 43, f"Test 137 failed: got {result}, expected {43}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = differenceMinMax([0, -6])
        assert result == 6, f"Test 138 failed: got {result}, expected {6}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = differenceMinMax([42, 0])
        assert result == 42, f"Test 139 failed: got {result}, expected {42}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = differenceMinMax([42, 0, 0])
        assert result == 42, f"Test 140 failed: got {result}, expected {42}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = differenceMinMax([42, 19])
        assert result == 23, f"Test 141 failed: got {result}, expected {23}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = differenceMinMax([-21])
        assert result == 0, f"Test 142 failed: got {result}, expected {0}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = differenceMinMax([42, 6])
        assert result == 36, f"Test 143 failed: got {result}, expected {36}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = differenceMinMax([13, 42, 0])
        assert result == 42, f"Test 144 failed: got {result}, expected {42}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = differenceMinMax([0, 0, 43])
        assert result == 43, f"Test 145 failed: got {result}, expected {43}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = differenceMinMax([0, 0, 42])
        assert result == 42, f"Test 146 failed: got {result}, expected {42}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = differenceMinMax([-42, -1000000, 20])
        assert result == 1000020, f"Test 147 failed: got {result}, expected {1000020}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = differenceMinMax([-42, 0])
        assert result == 42, f"Test 148 failed: got {result}, expected {42}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = differenceMinMax([-44, 0])
        assert result == 44, f"Test 149 failed: got {result}, expected {44}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = differenceMinMax([10, 0])
        assert result == 10, f"Test 150 failed: got {result}, expected {10}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = differenceMinMax([0, 123456789, 0, 0, -42])
        assert result == 123456831, f"Test 151 failed: got {result}, expected {123456831}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = differenceMinMax([0, -42])
        assert result == 42, f"Test 152 failed: got {result}, expected {42}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = differenceMinMax([-42, 0, -30])
        assert result == 42, f"Test 153 failed: got {result}, expected {42}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = differenceMinMax([-1000000000001])
        assert result == 0, f"Test 154 failed: got {result}, expected {0}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = differenceMinMax([0, 0, 5, -10])
        assert result == 15, f"Test 155 failed: got {result}, expected {15}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = differenceMinMax([5, 5, -21])
        assert result == 26, f"Test 156 failed: got {result}, expected {26}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = differenceMinMax([5, 5, 3])
        assert result == 2, f"Test 157 failed: got {result}, expected {2}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = differenceMinMax([0, 999999999999999999999999, -19])
        assert result == 1000000000000000000000018, f"Test 158 failed: got {result}, expected {1000000000000000000000018}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = differenceMinMax([-55, -1, 5, 5])
        assert result == 60, f"Test 159 failed: got {result}, expected {60}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = differenceMinMax([8, 5])
        assert result == 3, f"Test 160 failed: got {result}, expected {3}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = differenceMinMax([17, -8, 5, 5])
        assert result == 25, f"Test 161 failed: got {result}, expected {25}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = differenceMinMax([5, 5, 5])
        assert result == 0, f"Test 162 failed: got {result}, expected {0}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = differenceMinMax([5])
        assert result == 0, f"Test 163 failed: got {result}, expected {0}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = differenceMinMax([30])
        assert result == 0, f"Test 164 failed: got {result}, expected {0}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = differenceMinMax([2])
        assert result == 0, f"Test 165 failed: got {result}, expected {0}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = differenceMinMax([1, 2, 0])
        assert result == 2, f"Test 166 failed: got {result}, expected {2}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = differenceMinMax([1, 1000000000000, 0, 0])
        assert result == 1000000000000, f"Test 167 failed: got {result}, expected {1000000000000}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = differenceMinMax([1, 2, 13, -3, 0])
        assert result == 16, f"Test 168 failed: got {result}, expected {16}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = differenceMinMax([1])
        assert result == 0, f"Test 169 failed: got {result}, expected {0}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = differenceMinMax([0, 1])
        assert result == 1, f"Test 170 failed: got {result}, expected {1}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = differenceMinMax([1, 1, 0])
        assert result == 1, f"Test 171 failed: got {result}, expected {1}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = differenceMinMax([-2, 0, 0])
        assert result == 2, f"Test 172 failed: got {result}, expected {2}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = differenceMinMax([-987654321, 0, 2, 1, 0])
        assert result == 987654323, f"Test 173 failed: got {result}, expected {987654323}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = differenceMinMax([1, -2, 0, -999999999999999999999998])
        assert result == 999999999999999999999999, f"Test 174 failed: got {result}, expected {999999999999999999999999}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = differenceMinMax([1, 0, 0])
        assert result == 1, f"Test 175 failed: got {result}, expected {1}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = differenceMinMax([2, 0, -42])
        assert result == 44, f"Test 176 failed: got {result}, expected {44}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = differenceMinMax([0, 0, 2])
        assert result == 2, f"Test 177 failed: got {result}, expected {2}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = differenceMinMax([1, -2147483648])
        assert result == 2147483649, f"Test 178 failed: got {result}, expected {2147483649}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = differenceMinMax([0, 123456789, 0, 123456789, 1, 2])
        assert result == 123456789, f"Test 179 failed: got {result}, expected {123456789}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = differenceMinMax([-6, 1, 41])
        assert result == 47, f"Test 180 failed: got {result}, expected {47}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = differenceMinMax([-999999, 34])
        assert result == 1000033, f"Test 181 failed: got {result}, expected {1000033}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = differenceMinMax([2, 2, 0, -2147483648])
        assert result == 2147483650, f"Test 182 failed: got {result}, expected {2147483650}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = differenceMinMax([-44, 2147483647, 0])
        assert result == 2147483691, f"Test 183 failed: got {result}, expected {2147483691}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = differenceMinMax([2, 1, -20, 0])
        assert result == 22, f"Test 184 failed: got {result}, expected {22}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = differenceMinMax([0, 2])
        assert result == 2, f"Test 185 failed: got {result}, expected {2}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = differenceMinMax([2, 1, 0])
        assert result == 2, f"Test 186 failed: got {result}, expected {2}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = differenceMinMax([2, 100])
        assert result == 98, f"Test 187 failed: got {result}, expected {98}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = differenceMinMax([1, -11])
        assert result == 12, f"Test 188 failed: got {result}, expected {12}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = differenceMinMax([2, 1, 40])
        assert result == 39, f"Test 189 failed: got {result}, expected {39}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = differenceMinMax([-1, 0])
        assert result == 1, f"Test 190 failed: got {result}, expected {1}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = differenceMinMax([-9223372036854775808, -51, -999998, 1, -1])
        assert result == 9223372036854775809, f"Test 191 failed: got {result}, expected {9223372036854775809}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = differenceMinMax([1, -55])
        assert result == 56, f"Test 192 failed: got {result}, expected {56}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = differenceMinMax([-1, 1, -1000000000001, 0, 8])
        assert result == 1000000000009, f"Test 193 failed: got {result}, expected {1000000000009}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = differenceMinMax([-1, 1, 6, 6, 0])
        assert result == 7, f"Test 194 failed: got {result}, expected {7}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = differenceMinMax([1, -19])
        assert result == 20, f"Test 195 failed: got {result}, expected {20}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = differenceMinMax([1, -1, -55])
        assert result == 56, f"Test 196 failed: got {result}, expected {56}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = differenceMinMax([-1, -1])
        assert result == 0, f"Test 197 failed: got {result}, expected {0}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = differenceMinMax([-1, 1, -2])
        assert result == 3, f"Test 198 failed: got {result}, expected {3}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = differenceMinMax([-1, 2, -4, 0])
        assert result == 6, f"Test 199 failed: got {result}, expected {6}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = differenceMinMax([-1, 17])
        assert result == 18, f"Test 200 failed: got {result}, expected {18}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = differenceMinMax([1, -1])
        assert result == 2, f"Test 201 failed: got {result}, expected {2}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = differenceMinMax([-50, 0, 0, 0])
        assert result == 50, f"Test 202 failed: got {result}, expected {50}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = differenceMinMax([-5, 0, 0, 0, 0])
        assert result == 5, f"Test 203 failed: got {result}, expected {5}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = differenceMinMax([0, 0, 0, 0, -1, 10, 0])
        assert result == 11, f"Test 204 failed: got {result}, expected {11}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = differenceMinMax([0, 0, 0, 0, -9])
        assert result == 9, f"Test 205 failed: got {result}, expected {9}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = differenceMinMax([0, 0, 0, -19])
        assert result == 19, f"Test 206 failed: got {result}, expected {19}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = differenceMinMax([0, 0, 0, -123456789, 0, -19])
        assert result == 123456789, f"Test 207 failed: got {result}, expected {123456789}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = differenceMinMax([13, 50, 0, 0, 0, 0])
        assert result == 50, f"Test 208 failed: got {result}, expected {50}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = differenceMinMax([0, 0, 0, 1, 6, 0])
        assert result == 6, f"Test 209 failed: got {result}, expected {6}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = differenceMinMax([0, -51, 0, 0, 0, 0])
        assert result == 51, f"Test 210 failed: got {result}, expected {51}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = differenceMinMax([0, 0, -1, 0, 0])
        assert result == 1, f"Test 211 failed: got {result}, expected {1}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = differenceMinMax([0, 0, 0, 0, 0, -51])
        assert result == 51, f"Test 212 failed: got {result}, expected {51}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = differenceMinMax([1, 3, 0])
        assert result == 3, f"Test 213 failed: got {result}, expected {3}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = differenceMinMax([34, 0, 0, 0, 0])
        assert result == 34, f"Test 214 failed: got {result}, expected {34}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = differenceMinMax([-9, -20, -3, -10, -5])
        assert result == 17, f"Test 215 failed: got {result}, expected {17}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = differenceMinMax([-5, -10, -20, 0])
        assert result == 20, f"Test 216 failed: got {result}, expected {20}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = differenceMinMax([-5, -9, -21])
        assert result == 16, f"Test 217 failed: got {result}, expected {16}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = differenceMinMax([0, -3])
        assert result == 3, f"Test 218 failed: got {result}, expected {3}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = differenceMinMax([-5, -10, -3, -20, 89, -9223372036854775808, 0, 0])
        assert result == 9223372036854775897, f"Test 219 failed: got {result}, expected {9223372036854775897}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = differenceMinMax([-6, -10, -3, -20])
        assert result == 17, f"Test 220 failed: got {result}, expected {17}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = differenceMinMax([-5, -10, -3, -20, 1, 0])
        assert result == 21, f"Test 221 failed: got {result}, expected {21}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = differenceMinMax([-10, -1000000, -3, 22])
        assert result == 1000022, f"Test 222 failed: got {result}, expected {1000022}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = differenceMinMax([-20, -3, -10, 0])
        assert result == 20, f"Test 223 failed: got {result}, expected {20}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = differenceMinMax([-10, -2, -20])
        assert result == 18, f"Test 224 failed: got {result}, expected {18}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = differenceMinMax([-5, -144, -3, -20, 0, 0, 40])
        assert result == 184, f"Test 225 failed: got {result}, expected {184}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = differenceMinMax([-10, -3, 43, 19])
        assert result == 53, f"Test 226 failed: got {result}, expected {53}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = differenceMinMax([0, -20, -3, 9, -10, 0])
        assert result == 29, f"Test 227 failed: got {result}, expected {29}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = differenceMinMax([-40, -10, -3, -20, 0])
        assert result == 40, f"Test 228 failed: got {result}, expected {40}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = differenceMinMax([-5, -3, -20, 0, 9, 100])
        assert result == 120, f"Test 229 failed: got {result}, expected {120}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = differenceMinMax([3, -51, 4, 1, 9, 2, 6, 9223372036854775807])
        assert result == 9223372036854775858, f"Test 230 failed: got {result}, expected {9223372036854775858}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = differenceMinMax([9223372036854775807, 2, 9, 5, 1, 4, 1, 3])
        assert result == 9223372036854775806, f"Test 231 failed: got {result}, expected {9223372036854775806}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = differenceMinMax([3, -4, 1, 5, 9, 2, 6, -999999])
        assert result == 1000008, f"Test 232 failed: got {result}, expected {1000008}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 0, 2, 6])
        assert result == 6, f"Test 233 failed: got {result}, expected {6}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = differenceMinMax([3, 1, 4, 5, 9, 2, 6])
        assert result == 8, f"Test 234 failed: got {result}, expected {8}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = differenceMinMax([-55, 3, 1, 4, 1, 5, 9, 2, 6, 0])
        assert result == 64, f"Test 235 failed: got {result}, expected {64}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = differenceMinMax([6, 2, 5, 1, 4, 1, 3])
        assert result == 5, f"Test 236 failed: got {result}, expected {5}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = differenceMinMax([6, 2, 9, 1, 4, 1])
        assert result == 8, f"Test 237 failed: got {result}, expected {8}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = differenceMinMax([3, 4, 1, 5, 9, 2, 6, 0, 0])
        assert result == 9, f"Test 238 failed: got {result}, expected {9}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 6, -999999999999999999999998])
        assert result == 1000000000000000000000007, f"Test 239 failed: got {result}, expected {1000000000000000000000007}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = differenceMinMax([6, 2, 5, 1, 4, 1, 3, -55])
        assert result == 61, f"Test 240 failed: got {result}, expected {61}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 0, 0])
        assert result == 9, f"Test 241 failed: got {result}, expected {9}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = differenceMinMax([3, -1, 4, 2, 5, 9, 6, 0, 0])
        assert result == 10, f"Test 242 failed: got {result}, expected {10}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = differenceMinMax([1, 4, 1, 5, 7, 2, 6, 0])
        assert result == 7, f"Test 243 failed: got {result}, expected {7}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 2, 6, 2147483647])
        assert result == 2147483646, f"Test 244 failed: got {result}, expected {2147483646}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = differenceMinMax([-44, 30, 20, 10])
        assert result == 74, f"Test 245 failed: got {result}, expected {74}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = differenceMinMax([50, 40, 30, 20, 10, 2147483647])
        assert result == 2147483637, f"Test 246 failed: got {result}, expected {2147483637}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = differenceMinMax([-100, 10, 20, 30, 40, 50])
        assert result == 150, f"Test 247 failed: got {result}, expected {150}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = differenceMinMax([10, 30, 0, -100, -1000000000001])
        assert result == 1000000000031, f"Test 248 failed: got {result}, expected {1000000000031}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = differenceMinMax([50, 40, 30, 20, 10, 0, 0, 0])
        assert result == 50, f"Test 249 failed: got {result}, expected {50}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = differenceMinMax([50, 40, 30, 20, 10, 0, -50])
        assert result == 100, f"Test 250 failed: got {result}, expected {100}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = differenceMinMax([40, 30, 20, 10])
        assert result == 30, f"Test 251 failed: got {result}, expected {30}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = differenceMinMax([-1, 10, 20, 30, 40, 50])
        assert result == 51, f"Test 252 failed: got {result}, expected {51}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = differenceMinMax([0, 0, 10, 20, 30, 40, 50])
        assert result == 50, f"Test 253 failed: got {result}, expected {50}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = differenceMinMax([40, 30, 20, 10, -50, 0])
        assert result == 90, f"Test 254 failed: got {result}, expected {90}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = differenceMinMax([100, 10, 20, 30, 40, 50])
        assert result == 90, f"Test 255 failed: got {result}, expected {90}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = differenceMinMax([50, 40, 30, 20, 10, 0, -60])
        assert result == 110, f"Test 256 failed: got {result}, expected {110}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = differenceMinMax([50, 40, 30, 20, 10, -999998])
        assert result == 1000048, f"Test 257 failed: got {result}, expected {1000048}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = differenceMinMax([1000000000000, -1000000000000, 0, 0])
        assert result == 2000000000000, f"Test 258 failed: got {result}, expected {2000000000000}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = differenceMinMax([1000000000000, -1000000000000, 0])
        assert result == 2000000000000, f"Test 259 failed: got {result}, expected {2000000000000}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = differenceMinMax([-1000000000000])
        assert result == 0, f"Test 260 failed: got {result}, expected {0}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = differenceMinMax([-42, 17, 7])
        assert result == 59, f"Test 261 failed: got {result}, expected {59}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = differenceMinMax([1000000000000, -1000000000000, 0, 0, 0])
        assert result == 2000000000000, f"Test 262 failed: got {result}, expected {2000000000000}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = differenceMinMax([-1000000000000, 1000000000000])
        assert result == 2000000000000, f"Test 263 failed: got {result}, expected {2000000000000}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = differenceMinMax([1000000000000, -1000000000000, 11])
        assert result == 2000000000000, f"Test 264 failed: got {result}, expected {2000000000000}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = differenceMinMax([-19, 1000000000000])
        assert result == 1000000000019, f"Test 265 failed: got {result}, expected {1000000000019}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = differenceMinMax([1000000000000, -1000000000000, -999999999999999999999998])
        assert result == 1000000000000999999999998, f"Test 266 failed: got {result}, expected {1000000000000999999999998}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = differenceMinMax([-55])
        assert result == 0, f"Test 267 failed: got {result}, expected {0}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = differenceMinMax([9, 1000000000000])
        assert result == 999999999991, f"Test 268 failed: got {result}, expected {999999999991}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = differenceMinMax([9223372036854775808, -9223372036854775808, 0])
        assert result == 18446744073709551616, f"Test 269 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = differenceMinMax([9223372036854775806, -18446744073709551616])
        assert result == 27670116110564327422, f"Test 270 failed: got {result}, expected {27670116110564327422}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = differenceMinMax([9223372036854775807, -9223372036854775808, 9223372036854775806, 0])
        assert result == 18446744073709551615, f"Test 271 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = differenceMinMax([0, -9223372036854775808, 9223372036854775807, 19, 0, 9223372036854775807])
        assert result == 18446744073709551615, f"Test 272 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = differenceMinMax([9223372036854775807, 0])
        assert result == 9223372036854775807, f"Test 273 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = differenceMinMax([9223372036854775807, -1000000, -999999])
        assert result == 9223372036855775807, f"Test 274 failed: got {result}, expected {9223372036855775807}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = differenceMinMax([-9223372036854775809, 9223372036854775807, 0])
        assert result == 18446744073709551616, f"Test 275 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = differenceMinMax([0, -9223372036854775808])
        assert result == 9223372036854775808, f"Test 276 failed: got {result}, expected {9223372036854775808}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = differenceMinMax([9223372036854775808, 9223372036854775808])
        assert result == 0, f"Test 277 failed: got {result}, expected {0}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = differenceMinMax([-20, 0])
        assert result == 20, f"Test 278 failed: got {result}, expected {20}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = differenceMinMax([-9223372036854775807])
        assert result == 0, f"Test 279 failed: got {result}, expected {0}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = differenceMinMax([9223372036854775807, -18446744073709551616, 50])
        assert result == 27670116110564327423, f"Test 280 failed: got {result}, expected {27670116110564327423}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = differenceMinMax([9223372036854775808, 43, 0])
        assert result == 9223372036854775808, f"Test 281 failed: got {result}, expected {9223372036854775808}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = differenceMinMax([9223372036854775807, -9223372036854775808, 0])
        assert result == 18446744073709551615, f"Test 282 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = differenceMinMax([-42, -9223372036854775808])
        assert result == 9223372036854775766, f"Test 283 failed: got {result}, expected {9223372036854775766}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = differenceMinMax([-51, -1, 1, -1, 1, -1, 1])
        assert result == 52, f"Test 284 failed: got {result}, expected {52}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = differenceMinMax([1, -1, -1, 0, -1, 0])
        assert result == 2, f"Test 285 failed: got {result}, expected {2}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = differenceMinMax([1, -1, -999998, -1, 1, -1])
        assert result == 999999, f"Test 286 failed: got {result}, expected {999999}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = differenceMinMax([-1, 1, -1, 0, -1, 1, 0, -3, 0])
        assert result == 4, f"Test 287 failed: got {result}, expected {4}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = differenceMinMax([1, -1, 1, -1, 1, -2])
        assert result == 3, f"Test 288 failed: got {result}, expected {3}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = differenceMinMax([-5, -3, 1, -1, 1, -1, 1])
        assert result == 6, f"Test 289 failed: got {result}, expected {6}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = differenceMinMax([-1, 1, -1, 1, -1, 1])
        assert result == 2, f"Test 290 failed: got {result}, expected {2}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = differenceMinMax([-1, 1, -1, -1, 1])
        assert result == 2, f"Test 291 failed: got {result}, expected {2}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = differenceMinMax([-1, 1, -1, 1, -1, 1, 9, 8])
        assert result == 10, f"Test 292 failed: got {result}, expected {10}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = differenceMinMax([1, -1, 1, 1, -1, -123456789])
        assert result == 123456790, f"Test 293 failed: got {result}, expected {123456790}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = differenceMinMax([1, -1, 1, -1, 1, -1, -123456789])
        assert result == 123456790, f"Test 294 failed: got {result}, expected {123456790}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = differenceMinMax([-1, 1, -1, 1, -1, -999998, -51])
        assert result == 999999, f"Test 295 failed: got {result}, expected {999999}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = differenceMinMax([1, -1, 1, -1, 1, -1, -44, 0])
        assert result == 45, f"Test 296 failed: got {result}, expected {45}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = differenceMinMax([0, 2147483647])
        assert result == 2147483647, f"Test 297 failed: got {result}, expected {2147483647}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = differenceMinMax([2147483647, 0, -2147483648])
        assert result == 4294967295, f"Test 298 failed: got {result}, expected {4294967295}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = differenceMinMax([2147483648, 17, 2147483645, -30, -4])
        assert result == 2147483678, f"Test 299 failed: got {result}, expected {2147483678}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = differenceMinMax([2147483647, 0])
        assert result == 2147483647, f"Test 300 failed: got {result}, expected {2147483647}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = differenceMinMax([-2147483648, 0, 2147483647, 0])
        assert result == 4294967295, f"Test 301 failed: got {result}, expected {4294967295}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = differenceMinMax([0, 0, 2147483647, 0, -2147483648])
        assert result == 4294967295, f"Test 302 failed: got {result}, expected {4294967295}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = differenceMinMax([0, 2147483647, 0])
        assert result == 2147483647, f"Test 303 failed: got {result}, expected {2147483647}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = differenceMinMax([-2147483648, 0, 2147483647, -2147483648, 987654321, 2147483647])
        assert result == 4294967295, f"Test 304 failed: got {result}, expected {4294967295}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = differenceMinMax([-2147483648, 2147483647, 21])
        assert result == 4294967295, f"Test 305 failed: got {result}, expected {4294967295}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = differenceMinMax([34, 0, 2147483648, -999999999999999999999998, 0])
        assert result == 1000000000000002147483646, f"Test 306 failed: got {result}, expected {1000000000000002147483646}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = differenceMinMax([-2147483648, 0, 2147483647, -55])
        assert result == 4294967295, f"Test 307 failed: got {result}, expected {4294967295}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = differenceMinMax([7, 7, 6, 7, 7])
        assert result == 1, f"Test 308 failed: got {result}, expected {1}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = differenceMinMax([20, 7, 7, 7, 7, -3])
        assert result == 23, f"Test 309 failed: got {result}, expected {23}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = differenceMinMax([7, 7, 7, 7, 7, 21, 0, 0])
        assert result == 21, f"Test 310 failed: got {result}, expected {21}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = differenceMinMax([7, 7, 7, 7, 7, 0])
        assert result == 7, f"Test 311 failed: got {result}, expected {7}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = differenceMinMax([0, 7, 7, 7, 7])
        assert result == 7, f"Test 312 failed: got {result}, expected {7}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = differenceMinMax([7, 7, 7, 7])
        assert result == 0, f"Test 313 failed: got {result}, expected {0}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = differenceMinMax([7, 7, 7])
        assert result == 0, f"Test 314 failed: got {result}, expected {0}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = differenceMinMax([6, 7, 7, 7])
        assert result == 1, f"Test 315 failed: got {result}, expected {1}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = differenceMinMax([7, 7, 7, 8, 7, 0])
        assert result == 8, f"Test 316 failed: got {result}, expected {8}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = differenceMinMax([7, 7, 43, 7, 7])
        assert result == 36, f"Test 317 failed: got {result}, expected {36}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = differenceMinMax([7, 7, -7, 7, 6])
        assert result == 14, f"Test 318 failed: got {result}, expected {14}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = differenceMinMax([7, 7, 7, 7, 0])
        assert result == 7, f"Test 319 failed: got {result}, expected {7}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = differenceMinMax([7, 7, 9223372036854775807, 0, 7])
        assert result == 9223372036854775807, f"Test 320 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = differenceMinMax([7, 7, 7, 14, 7, -2147483648, 123456789])
        assert result == 2270940437, f"Test 321 failed: got {result}, expected {2270940437}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = differenceMinMax([0, -1, -2, -3, -4, -5, -20])
        assert result == 20, f"Test 322 failed: got {result}, expected {20}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = differenceMinMax([-5, -4, -3, -2, -1, 0])
        assert result == 5, f"Test 323 failed: got {result}, expected {5}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = differenceMinMax([0, -1, -2, -3, -4, -5, -2147483648, 0])
        assert result == 2147483648, f"Test 324 failed: got {result}, expected {2147483648}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = differenceMinMax([0, -1, -2, -3, -4, -5, 0])
        assert result == 5, f"Test 325 failed: got {result}, expected {5}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = differenceMinMax([0, -5, -4, -4, -2, -1, 0, 0])
        assert result == 5, f"Test 326 failed: got {result}, expected {5}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = differenceMinMax([0, -1, -2, 123456789, -4, -5, 11, 43])
        assert result == 123456794, f"Test 327 failed: got {result}, expected {123456794}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = differenceMinMax([0, -1, -2, -2, 0])
        assert result == 2, f"Test 328 failed: got {result}, expected {2}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = differenceMinMax([0, -1, -2, -3, -4, -5, 9223372036854775806])
        assert result == 9223372036854775811, f"Test 329 failed: got {result}, expected {9223372036854775811}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = differenceMinMax([0, 9223372036854775806, -2, -3, -8, -5, 0])
        assert result == 9223372036854775814, f"Test 330 failed: got {result}, expected {9223372036854775814}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = differenceMinMax([0, -1, -4, -4, -10, 17])
        assert result == 27, f"Test 331 failed: got {result}, expected {27}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = differenceMinMax([0, -1, -3, -4, -5, 0, -21])
        assert result == 21, f"Test 332 failed: got {result}, expected {21}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = differenceMinMax([50, 9223372036854775808, -2, -5, -4, 6, -2, -1, 0])
        assert result == 9223372036854775813, f"Test 333 failed: got {result}, expected {9223372036854775813}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = differenceMinMax([0, -1, 6, -4, -44, 0, -19])
        assert result == 50, f"Test 334 failed: got {result}, expected {50}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = differenceMinMax([0, -1, -2, -3, -4, 34])
        assert result == 38, f"Test 335 failed: got {result}, expected {38}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = differenceMinMax([0, 1, 2, 2, 4, 5, 42])
        assert result == 42, f"Test 336 failed: got {result}, expected {42}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = differenceMinMax([5, 4, 3, 2, 1, 0, -123456789, 0, 0])
        assert result == 123456794, f"Test 337 failed: got {result}, expected {123456794}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = differenceMinMax([0, 1, 2, 3, 4, 5, 0])
        assert result == 5, f"Test 338 failed: got {result}, expected {5}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = differenceMinMax([4, 3, 1, 0])
        assert result == 4, f"Test 339 failed: got {result}, expected {4}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = differenceMinMax([0, 1, 2, 3, 8, 19])
        assert result == 19, f"Test 340 failed: got {result}, expected {19}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = differenceMinMax([5, 4, 3, 1, 0])
        assert result == 5, f"Test 341 failed: got {result}, expected {5}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = differenceMinMax([0, 1, 2, 3, 0])
        assert result == 3, f"Test 342 failed: got {result}, expected {3}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = differenceMinMax([1, 2, 3, 4, 5, 0, 43])
        assert result == 43, f"Test 343 failed: got {result}, expected {43}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = differenceMinMax([-987654321, 4, 1, 0])
        assert result == 987654325, f"Test 344 failed: got {result}, expected {987654325}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = differenceMinMax([0, 1, 2, 3, 4, 6])
        assert result == 6, f"Test 345 failed: got {result}, expected {6}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = differenceMinMax([0, 1, 2, 3, 4, 5, 2147483645])
        assert result == 2147483645, f"Test 346 failed: got {result}, expected {2147483645}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    # Test case 347
    try:
        result = differenceMinMax([5, 4, 3, 2, -100, 0, -60])
        assert result == 105, f"Test 347 failed: got {result}, expected {105}"
        print(f"Test 347 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 347 failed: {e}")
        test_results.append(False)

    # Test case 348
    try:
        result = differenceMinMax([5, 4, 3, 2, 1, 0, -60])
        assert result == 65, f"Test 348 failed: got {result}, expected {65}"
        print(f"Test 348 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 348 failed: {e}")
        test_results.append(False)

    # Test case 349
    try:
        result = differenceMinMax([5, 4, 3, 2, 1, 0])
        assert result == 5, f"Test 349 failed: got {result}, expected {5}"
        print(f"Test 349 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 349 failed: {e}")
        test_results.append(False)

    # Test case 350
    try:
        result = differenceMinMax([-3, 0, -999999999999999999999998, 999999999999999999999999, -9223372036854775809])
        assert result == 1999999999999999999999997, f"Test 350 failed: got {result}, expected {1999999999999999999999997}"
        print(f"Test 350 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 350 failed: {e}")
        test_results.append(False)

    # Test case 351
    try:
        result = differenceMinMax([999999999999999999999999, -999999999999999999999998])
        assert result == 1999999999999999999999997, f"Test 351 failed: got {result}, expected {1999999999999999999999997}"
        print(f"Test 351 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 351 failed: {e}")
        test_results.append(False)

    # Test case 352
    try:
        result = differenceMinMax([-999999999999999999999998, 0])
        assert result == 999999999999999999999998, f"Test 352 failed: got {result}, expected {999999999999999999999998}"
        print(f"Test 352 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 352 failed: {e}")
        test_results.append(False)

    # Test case 353
    try:
        result = differenceMinMax([999999999999999999999999, -999999999999999999999998, 0, 0])
        assert result == 1999999999999999999999997, f"Test 353 failed: got {result}, expected {1999999999999999999999997}"
        print(f"Test 353 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 353 failed: {e}")
        test_results.append(False)

    # Test case 354
    try:
        result = differenceMinMax([0, 1000000000000, -999999999999999999999998])
        assert result == 1000000000000999999999998, f"Test 354 failed: got {result}, expected {1000000000000999999999998}"
        print(f"Test 354 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 354 failed: {e}")
        test_results.append(False)

    # Test case 355
    try:
        result = differenceMinMax([999999999999999999999999, -999999999999999999999998, 0, -18446744073709551616, 34, 2])
        assert result == 1999999999999999999999997, f"Test 355 failed: got {result}, expected {1999999999999999999999997}"
        print(f"Test 355 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 355 failed: {e}")
        test_results.append(False)

    # Test case 356
    try:
        result = differenceMinMax([0, 0, 0, -999999999999999999999997, 13])
        assert result == 1000000000000000000000010, f"Test 356 failed: got {result}, expected {1000000000000000000000010}"
        print(f"Test 356 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 356 failed: {e}")
        test_results.append(False)

    # Test case 357
    try:
        result = differenceMinMax([1, 999999999999999999999999, -999999999999999999999998, 0, 0])
        assert result == 1999999999999999999999997, f"Test 357 failed: got {result}, expected {1999999999999999999999997}"
        print(f"Test 357 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 357 failed: {e}")
        test_results.append(False)

    # Test case 358
    try:
        result = differenceMinMax([0, 999999999999999999999999, -999999999999999999999998, 0])
        assert result == 1999999999999999999999997, f"Test 358 failed: got {result}, expected {1999999999999999999999997}"
        print(f"Test 358 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 358 failed: {e}")
        test_results.append(False)

    # Test case 359
    try:
        result = differenceMinMax([-999999999999999999999997, 0])
        assert result == 999999999999999999999997, f"Test 359 failed: got {result}, expected {999999999999999999999997}"
        print(f"Test 359 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 359 failed: {e}")
        test_results.append(False)

    # Test case 360
    try:
        result = differenceMinMax([1999999999999999999999998, -999999999999999999999998, -2147483648])
        assert result == 2999999999999999999999996, f"Test 360 failed: got {result}, expected {2999999999999999999999996}"
        print(f"Test 360 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 360 failed: {e}")
        test_results.append(False)

    # Test case 361
    try:
        result = differenceMinMax([17, 999999999999999999999999])
        assert result == 999999999999999999999982, f"Test 361 failed: got {result}, expected {999999999999999999999982}"
        print(f"Test 361 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 361 failed: {e}")
        test_results.append(False)

    # Test case 362
    try:
        result = differenceMinMax([0, 999999999999999999999998, 999999999999999999999999])
        assert result == 999999999999999999999999, f"Test 362 failed: got {result}, expected {999999999999999999999999}"
        print(f"Test 362 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 362 failed: {e}")
        test_results.append(False)

    # Test case 363
    try:
        result = differenceMinMax([999999999999999999999999, -4, 0, 13, 0, -1000000000001])
        assert result == 1000000000001000000000000, f"Test 363 failed: got {result}, expected {1000000000001000000000000}"
        print(f"Test 363 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 363 failed: {e}")
        test_results.append(False)

    # Test case 364
    try:
        result = differenceMinMax([-3, -3, -3, -3, -2, -1, 0, -20])
        assert result == 20, f"Test 364 failed: got {result}, expected {20}"
        print(f"Test 364 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 364 failed: {e}")
        test_results.append(False)

    # Test case 365
    try:
        result = differenceMinMax([-1, -2, -2, -3, -3, -3])
        assert result == 2, f"Test 365 failed: got {result}, expected {2}"
        print(f"Test 365 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 365 failed: {e}")
        test_results.append(False)

    # Test case 366
    try:
        result = differenceMinMax([0, -2, -2, -3, -3, -3])
        assert result == 3, f"Test 366 failed: got {result}, expected {3}"
        print(f"Test 366 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 366 failed: {e}")
        test_results.append(False)

    # Test case 367
    try:
        result = differenceMinMax([-1, -2, -2, -3, -3, -3, -1000000000000])
        assert result == 999999999999, f"Test 367 failed: got {result}, expected {999999999999}"
        print(f"Test 367 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 367 failed: {e}")
        test_results.append(False)

    # Test case 368
    try:
        result = differenceMinMax([0, 0, -1, -2, -2, -3, -3, -3])
        assert result == 3, f"Test 368 failed: got {result}, expected {3}"
        print(f"Test 368 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 368 failed: {e}")
        test_results.append(False)

    # Test case 369
    try:
        result = differenceMinMax([-1, -2, -2, -3, -3, -3, 0])
        assert result == 3, f"Test 369 failed: got {result}, expected {3}"
        print(f"Test 369 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 369 failed: {e}")
        test_results.append(False)

    # Test case 370
    try:
        result = differenceMinMax([0, -2, -3, -3, -4])
        assert result == 4, f"Test 370 failed: got {result}, expected {4}"
        print(f"Test 370 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 370 failed: {e}")
        test_results.append(False)

    # Test case 371
    try:
        result = differenceMinMax([-3, -3, -3, -2, -2])
        assert result == 1, f"Test 371 failed: got {result}, expected {1}"
        print(f"Test 371 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 371 failed: {e}")
        test_results.append(False)

    # Test case 372
    try:
        result = differenceMinMax([3, -3, -2, -2])
        assert result == 6, f"Test 372 failed: got {result}, expected {6}"
        print(f"Test 372 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 372 failed: {e}")
        test_results.append(False)

    # Test case 373
    try:
        result = differenceMinMax([-1, -2, -2, -3, 0])
        assert result == 3, f"Test 373 failed: got {result}, expected {3}"
        print(f"Test 373 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 373 failed: {e}")
        test_results.append(False)

    # Test case 374
    try:
        result = differenceMinMax([-3, -3, -3, -4, -2, -1])
        assert result == 3, f"Test 374 failed: got {result}, expected {3}"
        print(f"Test 374 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 374 failed: {e}")
        test_results.append(False)

    # Test case 375
    try:
        result = differenceMinMax([-1, -2, -2, -3, -3, -3, 0, 0, 0, 0])
        assert result == 3, f"Test 375 failed: got {result}, expected {3}"
        print(f"Test 375 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 375 failed: {e}")
        test_results.append(False)

    # Test case 376
    try:
        result = differenceMinMax([-3, -3, -3, -2, -2, -1, 8, 0])
        assert result == 11, f"Test 376 failed: got {result}, expected {11}"
        print(f"Test 376 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 376 failed: {e}")
        test_results.append(False)

    # Test case 377
    try:
        result = differenceMinMax([0, -1, -2, -3, -3, -44])
        assert result == 44, f"Test 377 failed: got {result}, expected {44}"
        print(f"Test 377 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 377 failed: {e}")
        test_results.append(False)

    # Test case 378
    try:
        result = differenceMinMax([8, -8, -8, 8, 0, 0, 1999999999999999999999998, 0])
        assert result == 2000000000000000000000006, f"Test 378 failed: got {result}, expected {2000000000000000000000006}"
        print(f"Test 378 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 378 failed: {e}")
        test_results.append(False)

    # Test case 379
    try:
        result = differenceMinMax([0, 8, -8, 7, -8, 8, 0])
        assert result == 16, f"Test 379 failed: got {result}, expected {16}"
        print(f"Test 379 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 379 failed: {e}")
        test_results.append(False)

    # Test case 380
    try:
        result = differenceMinMax([8, -8, 8, -8, 8, 987654321, 7])
        assert result == 987654329, f"Test 380 failed: got {result}, expected {987654329}"
        print(f"Test 380 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 380 failed: {e}")
        test_results.append(False)

    # Test case 381
    try:
        result = differenceMinMax([8, -8, 8, 8, 0, 0])
        assert result == 16, f"Test 381 failed: got {result}, expected {16}"
        print(f"Test 381 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 381 failed: {e}")
        test_results.append(False)

    # Test case 382
    try:
        result = differenceMinMax([8, -8, 8, -9, -31, 0, -999999999999999999999998, 0])
        assert result == 1000000000000000000000006, f"Test 382 failed: got {result}, expected {1000000000000000000000006}"
        print(f"Test 382 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 382 failed: {e}")
        test_results.append(False)

    # Test case 383
    try:
        result = differenceMinMax([8, -8, 8, -8, 8, 0, -123456789])
        assert result == 123456797, f"Test 383 failed: got {result}, expected {123456797}"
        print(f"Test 383 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 383 failed: {e}")
        test_results.append(False)

    # Test case 384
    try:
        result = differenceMinMax([8, -9, 8, -8, 8, 0])
        assert result == 17, f"Test 384 failed: got {result}, expected {17}"
        print(f"Test 384 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 384 failed: {e}")
        test_results.append(False)

    # Test case 385
    try:
        result = differenceMinMax([8, -8, -8, -8, 8, -9223372036854775809, -144])
        assert result == 9223372036854775817, f"Test 385 failed: got {result}, expected {9223372036854775817}"
        print(f"Test 385 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 385 failed: {e}")
        test_results.append(False)

    # Test case 386
    try:
        result = differenceMinMax([0, 8, -8, 8, -8, -8, 0, 0])
        assert result == 16, f"Test 386 failed: got {result}, expected {16}"
        print(f"Test 386 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 386 failed: {e}")
        test_results.append(False)

    # Test case 387
    try:
        result = differenceMinMax([8, -8, 34, -8, 8, 0])
        assert result == 42, f"Test 387 failed: got {result}, expected {42}"
        print(f"Test 387 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 387 failed: {e}")
        test_results.append(False)

    # Test case 388
    try:
        result = differenceMinMax([8, -8, -8, 8, 0, 0])
        assert result == 16, f"Test 388 failed: got {result}, expected {16}"
        print(f"Test 388 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 388 failed: {e}")
        test_results.append(False)

    # Test case 389
    try:
        result = differenceMinMax([8, -8, 8, 8])
        assert result == 16, f"Test 389 failed: got {result}, expected {16}"
        print(f"Test 389 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 389 failed: {e}")
        test_results.append(False)

    # Test case 390
    try:
        result = differenceMinMax([8, -8, 9, -8, 8, 0])
        assert result == 17, f"Test 390 failed: got {result}, expected {17}"
        print(f"Test 390 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 390 failed: {e}")
        test_results.append(False)

    # Test case 391
    try:
        result = differenceMinMax([0, 0, 8, -8, 8, -8, 8])
        assert result == 16, f"Test 391 failed: got {result}, expected {16}"
        print(f"Test 391 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 391 failed: {e}")
        test_results.append(False)

    # Test case 392
    try:
        result = differenceMinMax([8, -8, 8, -8, 8, -144])
        assert result == 152, f"Test 392 failed: got {result}, expected {152}"
        print(f"Test 392 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 392 failed: {e}")
        test_results.append(False)

    # Test case 393
    try:
        result = differenceMinMax([22, 19, 34, -55, 89, -143])
        assert result == 232, f"Test 393 failed: got {result}, expected {232}"
        print(f"Test 393 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 393 failed: {e}")
        test_results.append(False)

    # Test case 394
    try:
        result = differenceMinMax([0, -144, 89, 34, -21, 13])
        assert result == 233, f"Test 394 failed: got {result}, expected {233}"
        print(f"Test 394 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 394 failed: {e}")
        test_results.append(False)

    # Test case 395
    try:
        result = differenceMinMax([-21, 34, -55, 89, -1000000000001, 0])
        assert result == 1000000000090, f"Test 395 failed: got {result}, expected {1000000000090}"
        print(f"Test 395 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 395 failed: {e}")
        test_results.append(False)

    # Test case 396
    try:
        result = differenceMinMax([13, -21, 34, 89, -144])
        assert result == 233, f"Test 396 failed: got {result}, expected {233}"
        print(f"Test 396 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 396 failed: {e}")
        test_results.append(False)

    # Test case 397
    try:
        result = differenceMinMax([13, -21, 34, -55, 89, -144, -51, 123456789])
        assert result == 123456933, f"Test 397 failed: got {result}, expected {123456933}"
        print(f"Test 397 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 397 failed: {e}")
        test_results.append(False)

    # Test case 398
    try:
        result = differenceMinMax([-4, -21, 34, -55, 89, -144, 0, 0])
        assert result == 233, f"Test 398 failed: got {result}, expected {233}"
        print(f"Test 398 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 398 failed: {e}")
        test_results.append(False)

    # Test case 399
    try:
        result = differenceMinMax([13, 34, -55, 89, -144, -1, 9223372036854775808, 0, 13])
        assert result == 9223372036854775952, f"Test 399 failed: got {result}, expected {9223372036854775952}"
        print(f"Test 399 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 399 failed: {e}")
        test_results.append(False)

    # Test case 400
    try:
        result = differenceMinMax([13, -21, 34, -55, 89, -144, 0, 0])
        assert result == 233, f"Test 400 failed: got {result}, expected {233}"
        print(f"Test 400 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 400 failed: {e}")
        test_results.append(False)

    # Test case 401
    try:
        result = differenceMinMax([13, -21, -6, -55, 89, -144])
        assert result == 233, f"Test 401 failed: got {result}, expected {233}"
        print(f"Test 401 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 401 failed: {e}")
        test_results.append(False)

    # Test case 402
    try:
        result = differenceMinMax([-144, 89, 55, 34])
        assert result == 233, f"Test 402 failed: got {result}, expected {233}"
        print(f"Test 402 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 402 failed: {e}")
        test_results.append(False)

    # Test case 403
    try:
        result = differenceMinMax([13, -21, 40, 89, -144, 0])
        assert result == 233, f"Test 403 failed: got {result}, expected {233}"
        print(f"Test 403 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 403 failed: {e}")
        test_results.append(False)

    # Test case 404
    try:
        result = differenceMinMax([13, 34, -55, -144])
        assert result == 178, f"Test 404 failed: got {result}, expected {178}"
        print(f"Test 404 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 404 failed: {e}")
        test_results.append(False)

    # Test case 405
    try:
        result = differenceMinMax([12, -21, 34, -55, 89, 0])
        assert result == 144, f"Test 405 failed: got {result}, expected {144}"
        print(f"Test 405 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 405 failed: {e}")
        test_results.append(False)

    # Test case 406
    try:
        result = differenceMinMax([13, -21, 34, -55, 89, -144, 0])
        assert result == 233, f"Test 406 failed: got {result}, expected {233}"
        print(f"Test 406 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 406 failed: {e}")
        test_results.append(False)

    # Test case 407
    try:
        result = differenceMinMax([-31, -7, -100, 19, 17, 13, 11, 7, 5, 3, 2, 0])
        assert result == 119, f"Test 407 failed: got {result}, expected {119}"
        print(f"Test 407 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 407 failed: {e}")
        test_results.append(False)

    # Test case 408
    try:
        result = differenceMinMax([2, 3, 5, 7, 11, 13, 17, 19, 0])
        assert result == 19, f"Test 408 failed: got {result}, expected {19}"
        print(f"Test 408 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 408 failed: {e}")
        test_results.append(False)

    # Test case 409
    try:
        result = differenceMinMax([19, 17, 13, 11, 7, 5, 3, 2, -10])
        assert result == 29, f"Test 409 failed: got {result}, expected {29}"
        print(f"Test 409 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 409 failed: {e}")
        test_results.append(False)

    # Test case 410
    try:
        result = differenceMinMax([2, -100, 7, -11, 13, 17, 19])
        assert result == 119, f"Test 410 failed: got {result}, expected {119}"
        print(f"Test 410 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 410 failed: {e}")
        test_results.append(False)

    # Test case 411
    try:
        result = differenceMinMax([19, 17, -9223372036854775808, 11, 7, 3, 2, 0])
        assert result == 9223372036854775827, f"Test 411 failed: got {result}, expected {9223372036854775827}"
        print(f"Test 411 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 411 failed: {e}")
        test_results.append(False)

    # Test case 412
    try:
        result = differenceMinMax([19, 17, 11, 7, 5, 3, 2])
        assert result == 17, f"Test 412 failed: got {result}, expected {17}"
        print(f"Test 412 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 412 failed: {e}")
        test_results.append(False)

    # Test case 413
    try:
        result = differenceMinMax([0, 19, 17, 13, 11, 7, 5, 3, 2, 9, 19, -100])
        assert result == 119, f"Test 413 failed: got {result}, expected {119}"
        print(f"Test 413 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 413 failed: {e}")
        test_results.append(False)

    # Test case 414
    try:
        result = differenceMinMax([0, -50, 0, 17, 13, 11, 7, 5, 3, 2, 5])
        assert result == 67, f"Test 414 failed: got {result}, expected {67}"
        print(f"Test 414 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 414 failed: {e}")
        test_results.append(False)

    # Test case 415
    try:
        result = differenceMinMax([2, 3, 5, 7, 11, 13, 17, 19, -2, 0])
        assert result == 21, f"Test 415 failed: got {result}, expected {21}"
        print(f"Test 415 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 415 failed: {e}")
        test_results.append(False)

    # Test case 416
    try:
        result = differenceMinMax([2, 3, 5, 7, 11, 13, 17, 19, 55, 0])
        assert result == 55, f"Test 416 failed: got {result}, expected {55}"
        print(f"Test 416 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 416 failed: {e}")
        test_results.append(False)

    # Test case 417
    try:
        result = differenceMinMax([2, 5, 7, 11, 13, 17, 19, -51])
        assert result == 70, f"Test 417 failed: got {result}, expected {70}"
        print(f"Test 417 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 417 failed: {e}")
        test_results.append(False)

    # Test case 418
    try:
        result = differenceMinMax([2, 3, 5, 7, 11, 13, 17, 19, 0, 0, -144, 0, -999999])
        assert result == 1000018, f"Test 418 failed: got {result}, expected {1000018}"
        print(f"Test 418 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 418 failed: {e}")
        test_results.append(False)

    # Test case 419
    try:
        result = differenceMinMax([-20, 3, 5, 7, 11, 13, 17, 19, -9223372036854775809, -30, 0])
        assert result == 9223372036854775828, f"Test 419 failed: got {result}, expected {9223372036854775828}"
        print(f"Test 419 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 419 failed: {e}")
        test_results.append(False)

    # Test case 420
    try:
        result = differenceMinMax([17, 11, 7, 5, 3, 2, -5])
        assert result == 22, f"Test 420 failed: got {result}, expected {22}"
        print(f"Test 420 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 420 failed: {e}")
        test_results.append(False)

    # Test case 421
    try:
        result = differenceMinMax([19, 14, 11, 7, 6, 3])
        assert result == 16, f"Test 421 failed: got {result}, expected {16}"
        print(f"Test 421 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 421 failed: {e}")
        test_results.append(False)

    # Test case 422
    try:
        result = differenceMinMax([19, 17, 13, 11, 7, 5, 3, 2, 123456789])
        assert result == 123456787, f"Test 422 failed: got {result}, expected {123456787}"
        print(f"Test 422 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 422 failed: {e}")
        test_results.append(False)

    # Test case 423
    try:
        result = differenceMinMax([0, 2, 5, 7, 11, 14, 17, 19])
        assert result == 19, f"Test 423 failed: got {result}, expected {19}"
        print(f"Test 423 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 423 failed: {e}")
        test_results.append(False)

    # Test case 424
    try:
        result = differenceMinMax([19, 17, 13, 11, 7, 5, 3, 2, 0, -1000000])
        assert result == 1000019, f"Test 424 failed: got {result}, expected {1000019}"
        print(f"Test 424 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 424 failed: {e}")
        test_results.append(False)

    # Test case 425
    try:
        result = differenceMinMax([3, 5, 11, 13, 20, 19, -19])
        assert result == 39, f"Test 425 failed: got {result}, expected {39}"
        print(f"Test 425 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 425 failed: {e}")
        test_results.append(False)

    # Test case 426
    try:
        result = differenceMinMax([19, -1000000, 13, 11, 7, 5, 3, 2])
        assert result == 1000019, f"Test 426 failed: got {result}, expected {1000019}"
        print(f"Test 426 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 426 failed: {e}")
        test_results.append(False)

    # Test case 427
    try:
        result = differenceMinMax([-1000000000001, 0, 2, 3, 5, 7, 11, 13, 17, 19, -9223372036854775808])
        assert result == 9223372036854775827, f"Test 427 failed: got {result}, expected {9223372036854775827}"
        print(f"Test 427 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 427 failed: {e}")
        test_results.append(False)

    # Test case 428
    try:
        result = differenceMinMax([19, 17, 13, 7, 5, 3, 2, 9223372036854775807])
        assert result == 9223372036854775805, f"Test 428 failed: got {result}, expected {9223372036854775805}"
        print(f"Test 428 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 428 failed: {e}")
        test_results.append(False)

    # Test case 429
    try:
        result = differenceMinMax([19, 17, 13, 11, 7, 5, 2, 0, 0])
        assert result == 19, f"Test 429 failed: got {result}, expected {19}"
        print(f"Test 429 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 429 failed: {e}")
        test_results.append(False)

    # Test case 430
    try:
        result = differenceMinMax([19, 17, 13, 11, 8, 5, 3, 2])
        assert result == 17, f"Test 430 failed: got {result}, expected {17}"
        print(f"Test 430 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 430 failed: {e}")
        test_results.append(False)

    # Test case 431
    try:
        result = differenceMinMax([0, 2, 5, 11, 13, 17, 19, 0])
        assert result == 19, f"Test 431 failed: got {result}, expected {19}"
        print(f"Test 431 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 431 failed: {e}")
        test_results.append(False)

    # Test case 432
    try:
        result = differenceMinMax([19, 13, 11, 7, 5, 3, 2, 0, 0, 0])
        assert result == 19, f"Test 432 failed: got {result}, expected {19}"
        print(f"Test 432 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 432 failed: {e}")
        test_results.append(False)

    # Test case 433
    try:
        result = differenceMinMax([2, 3, 5, 7, 11, 13, 17, 19, 0, -144])
        assert result == 163, f"Test 433 failed: got {result}, expected {163}"
        print(f"Test 433 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 433 failed: {e}")
        test_results.append(False)

    # Test case 434
    try:
        result = differenceMinMax([19, 17, 13, 11, 7, 5, -3, 2])
        assert result == 22, f"Test 434 failed: got {result}, expected {22}"
        print(f"Test 434 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 434 failed: {e}")
        test_results.append(False)

    # Test case 435
    try:
        result = differenceMinMax([-4, 4, 0])
        assert result == 8, f"Test 435 failed: got {result}, expected {8}"
        print(f"Test 435 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 435 failed: {e}")
        test_results.append(False)

    # Test case 436
    try:
        result = differenceMinMax([-8])
        assert result == 0, f"Test 436 failed: got {result}, expected {0}"
        print(f"Test 436 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 436 failed: {e}")
        test_results.append(False)

    # Test case 437
    try:
        result = differenceMinMax([4, 30, 42, 43, 8])
        assert result == 39, f"Test 437 failed: got {result}, expected {39}"
        print(f"Test 437 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 437 failed: {e}")
        test_results.append(False)

    # Test case 438
    try:
        result = differenceMinMax([-4, 4])
        assert result == 8, f"Test 438 failed: got {result}, expected {8}"
        print(f"Test 438 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 438 failed: {e}")
        test_results.append(False)

    # Test case 439
    try:
        result = differenceMinMax([0, -4, 4, 0])
        assert result == 8, f"Test 439 failed: got {result}, expected {8}"
        print(f"Test 439 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 439 failed: {e}")
        test_results.append(False)

    # Test case 440
    try:
        result = differenceMinMax([0, -4, 4])
        assert result == 8, f"Test 440 failed: got {result}, expected {8}"
        print(f"Test 440 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 440 failed: {e}")
        test_results.append(False)

    # Test case 441
    try:
        result = differenceMinMax([4, 12, 0])
        assert result == 12, f"Test 441 failed: got {result}, expected {12}"
        print(f"Test 441 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 441 failed: {e}")
        test_results.append(False)

    # Test case 442
    try:
        result = differenceMinMax([-50, 4, 0])
        assert result == 54, f"Test 442 failed: got {result}, expected {54}"
        print(f"Test 442 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 442 failed: {e}")
        test_results.append(False)

    # Test case 443
    try:
        result = differenceMinMax([-3, 4])
        assert result == 7, f"Test 443 failed: got {result}, expected {7}"
        print(f"Test 443 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 443 failed: {e}")
        test_results.append(False)

    # Test case 444
    try:
        result = differenceMinMax([4, -4, -30, -50])
        assert result == 54, f"Test 444 failed: got {result}, expected {54}"
        print(f"Test 444 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 444 failed: {e}")
        test_results.append(False)

    # Test case 445
    try:
        result = differenceMinMax([-4, 0])
        assert result == 4, f"Test 445 failed: got {result}, expected {4}"
        print(f"Test 445 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 445 failed: {e}")
        test_results.append(False)

    # Test case 446
    try:
        result = differenceMinMax([0, -4])
        assert result == 4, f"Test 446 failed: got {result}, expected {4}"
        print(f"Test 446 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 446 failed: {e}")
        test_results.append(False)

    # Test case 447
    try:
        result = differenceMinMax([-100, 100, 100])
        assert result == 200, f"Test 447 failed: got {result}, expected {200}"
        print(f"Test 447 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 447 failed: {e}")
        test_results.append(False)

    # Test case 448
    try:
        result = differenceMinMax([100, -100, 101, 0])
        assert result == 201, f"Test 448 failed: got {result}, expected {201}"
        print(f"Test 448 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 448 failed: {e}")
        test_results.append(False)

    # Test case 449
    try:
        result = differenceMinMax([-100, 100, 100, 0])
        assert result == 200, f"Test 449 failed: got {result}, expected {200}"
        print(f"Test 449 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 449 failed: {e}")
        test_results.append(False)

    # Test case 450
    try:
        result = differenceMinMax([41, 0, -100, 100, -100])
        assert result == 200, f"Test 450 failed: got {result}, expected {200}"
        print(f"Test 450 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 450 failed: {e}")
        test_results.append(False)

    # Test case 451
    try:
        result = differenceMinMax([-100, 100, 0])
        assert result == 200, f"Test 451 failed: got {result}, expected {200}"
        print(f"Test 451 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 451 failed: {e}")
        test_results.append(False)

    # Test case 452
    try:
        result = differenceMinMax([-31, -100, 100, -100, 2, 50, 21])
        assert result == 200, f"Test 452 failed: got {result}, expected {200}"
        print(f"Test 452 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 452 failed: {e}")
        test_results.append(False)

    # Test case 453
    try:
        result = differenceMinMax([0, -98, -100, 100, -100, -9223372036854775808])
        assert result == 9223372036854775908, f"Test 453 failed: got {result}, expected {9223372036854775908}"
        print(f"Test 453 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 453 failed: {e}")
        test_results.append(False)

    # Test case 454
    try:
        result = differenceMinMax([100, -200, 100, -100])
        assert result == 300, f"Test 454 failed: got {result}, expected {300}"
        print(f"Test 454 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 454 failed: {e}")
        test_results.append(False)

    # Test case 455
    try:
        result = differenceMinMax([-100, 100, -100, 100, 0, -9223372036854775808, 0, 0, 0])
        assert result == 9223372036854775908, f"Test 455 failed: got {result}, expected {9223372036854775908}"
        print(f"Test 455 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 455 failed: {e}")
        test_results.append(False)

    # Test case 456
    try:
        result = differenceMinMax([101, -100, 0, -100])
        assert result == 201, f"Test 456 failed: got {result}, expected {201}"
        print(f"Test 456 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 456 failed: {e}")
        test_results.append(False)

    # Test case 457
    try:
        result = differenceMinMax([101, -999999999999999999999998, 100, -100, -9223372036854775807])
        assert result == 1000000000000000000000099, f"Test 457 failed: got {result}, expected {1000000000000000000000099}"
        print(f"Test 457 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 457 failed: {e}")
        test_results.append(False)

    # Test case 458
    try:
        result = differenceMinMax([55, 100, -100, 100, -100])
        assert result == 200, f"Test 458 failed: got {result}, expected {200}"
        print(f"Test 458 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 458 failed: {e}")
        test_results.append(False)

    # Test case 459
    try:
        result = differenceMinMax([100, 13, 100, -100, 123456789])
        assert result == 123456889, f"Test 459 failed: got {result}, expected {123456889}"
        print(f"Test 459 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 459 failed: {e}")
        test_results.append(False)

    # Test case 460
    try:
        result = differenceMinMax([8, 100, -100, 100])
        assert result == 200, f"Test 460 failed: got {result}, expected {200}"
        print(f"Test 460 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 460 failed: {e}")
        test_results.append(False)

    # Test case 461
    try:
        result = differenceMinMax([-100, 100, -100, -60, -50, 9223372036854775807])
        assert result == 9223372036854775907, f"Test 461 failed: got {result}, expected {9223372036854775907}"
        print(f"Test 461 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 461 failed: {e}")
        test_results.append(False)

    # Test case 462
    try:
        result = differenceMinMax([0, 6, 8, 0])
        assert result == 8, f"Test 462 failed: got {result}, expected {8}"
        print(f"Test 462 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 462 failed: {e}")
        test_results.append(False)

    # Test case 463
    try:
        result = differenceMinMax([50, 0, 6, 0, 6, 0, 5, 4])
        assert result == 50, f"Test 463 failed: got {result}, expected {50}"
        print(f"Test 463 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 463 failed: {e}")
        test_results.append(False)

    # Test case 464
    try:
        result = differenceMinMax([0, -6, 0, 6, 0, 6])
        assert result == 12, f"Test 464 failed: got {result}, expected {12}"
        print(f"Test 464 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 464 failed: {e}")
        test_results.append(False)

    # Test case 465
    try:
        result = differenceMinMax([6, 0, 6, 0, 6, 0, -9223372036854775809])
        assert result == 9223372036854775815, f"Test 465 failed: got {result}, expected {9223372036854775815}"
        print(f"Test 465 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 465 failed: {e}")
        test_results.append(False)

    # Test case 466
    try:
        result = differenceMinMax([-1, 6, 0, 6, 0, 6, 20])
        assert result == 21, f"Test 466 failed: got {result}, expected {21}"
        print(f"Test 466 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 466 failed: {e}")
        test_results.append(False)

    # Test case 467
    try:
        result = differenceMinMax([-6, 0, 6, 0, 6, 0, -31])
        assert result == 37, f"Test 467 failed: got {result}, expected {37}"
        print(f"Test 467 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 467 failed: {e}")
        test_results.append(False)

    # Test case 468
    try:
        result = differenceMinMax([-1, 6, 0, 6, 0, 0])
        assert result == 7, f"Test 468 failed: got {result}, expected {7}"
        print(f"Test 468 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 468 failed: {e}")
        test_results.append(False)

    # Test case 469
    try:
        result = differenceMinMax([6, 0, 6, 0, 6, 0, 0, 0])
        assert result == 6, f"Test 469 failed: got {result}, expected {6}"
        print(f"Test 469 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 469 failed: {e}")
        test_results.append(False)

    # Test case 470
    try:
        result = differenceMinMax([0, 0, 100, 0, 6, 0, 6, 0, 2])
        assert result == 100, f"Test 470 failed: got {result}, expected {100}"
        print(f"Test 470 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 470 failed: {e}")
        test_results.append(False)

    # Test case 471
    try:
        result = differenceMinMax([6, 0, 6, 0, 6, 0, 0, -20, 0])
        assert result == 26, f"Test 471 failed: got {result}, expected {26}"
        print(f"Test 471 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 471 failed: {e}")
        test_results.append(False)

    # Test case 472
    try:
        result = differenceMinMax([4, 0, 6, 6, 0])
        assert result == 6, f"Test 472 failed: got {result}, expected {6}"
        print(f"Test 472 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 472 failed: {e}")
        test_results.append(False)

    # Test case 473
    try:
        result = differenceMinMax([6, 30, 6, 0, 0, 0])
        assert result == 30, f"Test 473 failed: got {result}, expected {30}"
        print(f"Test 473 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 473 failed: {e}")
        test_results.append(False)

    # Test case 474
    try:
        result = differenceMinMax([6, 0, 9, 0, 6, 0])
        assert result == 9, f"Test 474 failed: got {result}, expected {9}"
        print(f"Test 474 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 474 failed: {e}")
        test_results.append(False)

    # Test case 475
    try:
        result = differenceMinMax([6, 0, 6, 0, 6, 0, 0])
        assert result == 6, f"Test 475 failed: got {result}, expected {6}"
        print(f"Test 475 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 475 failed: {e}")
        test_results.append(False)

    # Test case 476
    try:
        result = differenceMinMax([-999999, -1000000, -98, -20])
        assert result == 999980, f"Test 476 failed: got {result}, expected {999980}"
        print(f"Test 476 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 476 failed: {e}")
        test_results.append(False)

    # Test case 477
    try:
        result = differenceMinMax([-999999, -1000000, -999999, 0])
        assert result == 1000000, f"Test 477 failed: got {result}, expected {1000000}"
        print(f"Test 477 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 477 failed: {e}")
        test_results.append(False)

    # Test case 478
    try:
        result = differenceMinMax([-999999, -1000000, 9223372036854775808, 0, -19])
        assert result == 9223372036855775808, f"Test 478 failed: got {result}, expected {9223372036855775808}"
        print(f"Test 478 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 478 failed: {e}")
        test_results.append(False)

    # Test case 479
    try:
        result = differenceMinMax([0, -999998])
        assert result == 999998, f"Test 479 failed: got {result}, expected {999998}"
        print(f"Test 479 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 479 failed: {e}")
        test_results.append(False)

    # Test case 480
    try:
        result = differenceMinMax([-999999, -999998, 35])
        assert result == 1000034, f"Test 480 failed: got {result}, expected {1000034}"
        print(f"Test 480 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 480 failed: {e}")
        test_results.append(False)

    # Test case 481
    try:
        result = differenceMinMax([999999, -43])
        assert result == 1000042, f"Test 481 failed: got {result}, expected {1000042}"
        print(f"Test 481 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 481 failed: {e}")
        test_results.append(False)

    # Test case 482
    try:
        result = differenceMinMax([-999999, -1000000, -999998, 0, 0])
        assert result == 1000000, f"Test 482 failed: got {result}, expected {1000000}"
        print(f"Test 482 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 482 failed: {e}")
        test_results.append(False)

    # Test case 483
    try:
        result = differenceMinMax([0, -999998, -1000000, -1999998])
        assert result == 1999998, f"Test 483 failed: got {result}, expected {1999998}"
        print(f"Test 483 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 483 failed: {e}")
        test_results.append(False)

    # Test case 484
    try:
        result = differenceMinMax([-999998, -1000000, -999999, 0])
        assert result == 1000000, f"Test 484 failed: got {result}, expected {1000000}"
        print(f"Test 484 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 484 failed: {e}")
        test_results.append(False)

    # Test case 485
    try:
        result = differenceMinMax([-999998, -999999, -1000000, 6])
        assert result == 1000006, f"Test 485 failed: got {result}, expected {1000006}"
        print(f"Test 485 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 485 failed: {e}")
        test_results.append(False)

    # Test case 486
    try:
        result = differenceMinMax([-1000000, -999998, 0])
        assert result == 1000000, f"Test 486 failed: got {result}, expected {1000000}"
        print(f"Test 486 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 486 failed: {e}")
        test_results.append(False)

    # Test case 487
    try:
        result = differenceMinMax([0, 17, -999998, -1000000, -999999, 0])
        assert result == 1000017, f"Test 487 failed: got {result}, expected {1000017}"
        print(f"Test 487 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 487 failed: {e}")
        test_results.append(False)

    # Test case 488
    try:
        result = differenceMinMax([9, -999998, -1000000, -999999])
        assert result == 1000009, f"Test 488 failed: got {result}, expected {1000009}"
        print(f"Test 488 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 488 failed: {e}")
        test_results.append(False)

    # Test case 489
    try:
        result = differenceMinMax([987654321, -1975308642])
        assert result == 2962962963, f"Test 489 failed: got {result}, expected {2962962963}"
        print(f"Test 489 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 489 failed: {e}")
        test_results.append(False)

    # Test case 490
    try:
        result = differenceMinMax([0, -987654321, -123456789, 987654321, 123456789, 2147483648])
        assert result == 3135137969, f"Test 490 failed: got {result}, expected {3135137969}"
        print(f"Test 490 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 490 failed: {e}")
        test_results.append(False)

    # Test case 491
    try:
        result = differenceMinMax([987654321, -123456789, -987654321])
        assert result == 1975308642, f"Test 491 failed: got {result}, expected {1975308642}"
        print(f"Test 491 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 491 failed: {e}")
        test_results.append(False)

    # Test case 492
    try:
        result = differenceMinMax([123456789, 987654321, -123456789, -987654321, -5, 0])
        assert result == 1975308642, f"Test 492 failed: got {result}, expected {1975308642}"
        print(f"Test 492 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 492 failed: {e}")
        test_results.append(False)

    # Test case 493
    try:
        result = differenceMinMax([-123456789, -987654324])
        assert result == 864197535, f"Test 493 failed: got {result}, expected {864197535}"
        print(f"Test 493 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 493 failed: {e}")
        test_results.append(False)

    # Test case 494
    try:
        result = differenceMinMax([987654321, -987654321])
        assert result == 1975308642, f"Test 494 failed: got {result}, expected {1975308642}"
        print(f"Test 494 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 494 failed: {e}")
        test_results.append(False)

    # Test case 495
    try:
        result = differenceMinMax([0, 2147483648, -987654321, -123456789, 1975308642, 123456789, 2])
        assert result == 3135137969, f"Test 495 failed: got {result}, expected {3135137969}"
        print(f"Test 495 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 495 failed: {e}")
        test_results.append(False)

    # Test case 496
    try:
        result = differenceMinMax([123456789, 987654321, -987654319, 0])
        assert result == 1975308640, f"Test 496 failed: got {result}, expected {1975308640}"
        print(f"Test 496 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 496 failed: {e}")
        test_results.append(False)

    # Test case 497
    try:
        result = differenceMinMax([123456789, 987654321, -123456789, -987654321, -123456789, 9223372036854775807, 0])
        assert result == 9223372037842430128, f"Test 497 failed: got {result}, expected {9223372037842430128}"
        print(f"Test 497 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 497 failed: {e}")
        test_results.append(False)

    # Test case 498
    try:
        result = differenceMinMax([0, -987654321, -123456789, 987654321, 123456789, 0])
        assert result == 1975308642, f"Test 498 failed: got {result}, expected {1975308642}"
        print(f"Test 498 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 498 failed: {e}")
        test_results.append(False)

    # Test case 499
    try:
        result = differenceMinMax([100, 0, -10, -987654321, -123456789, 987654321, 123456789, 0])
        assert result == 1975308642, f"Test 499 failed: got {result}, expected {1975308642}"
        print(f"Test 499 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 499 failed: {e}")
        test_results.append(False)

    # Test case 500
    try:
        result = differenceMinMax([9223372036854775806, 987654321, -123456789])
        assert result == 9223372036978232595, f"Test 500 failed: got {result}, expected {9223372036978232595}"
        print(f"Test 500 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 500 failed: {e}")
        test_results.append(False)

    # Test case 501
    try:
        result = differenceMinMax([-987654321, -123456789, 987654321, 123456789, 30, 9223372036854775808, 0])
        assert result == 9223372037842430129, f"Test 501 failed: got {result}, expected {9223372037842430129}"
        print(f"Test 501 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 501 failed: {e}")
        test_results.append(False)

    # Test case 502
    try:
        result = differenceMinMax([987654321, -123456789, -987654321, 0, 0, -6, -1])
        assert result == 1975308642, f"Test 502 failed: got {result}, expected {1975308642}"
        print(f"Test 502 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 502 failed: {e}")
        test_results.append(False)

    # Test case 503
    try:
        result = differenceMinMax([-987654321, -123456789, -123456789, 20, 4])
        assert result == 987654341, f"Test 503 failed: got {result}, expected {987654341}"
        print(f"Test 503 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 503 failed: {e}")
        test_results.append(False)

    # Test case 504
    try:
        result = differenceMinMax([1, 1, 0, 3, 5, 8, 13, 34])
        assert result == 34, f"Test 504 failed: got {result}, expected {34}"
        print(f"Test 504 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 504 failed: {e}")
        test_results.append(False)

    # Test case 505
    try:
        result = differenceMinMax([34, 21, 13, 8, 5, 3, 2, 1, 1, 0])
        assert result == 34, f"Test 505 failed: got {result}, expected {34}"
        print(f"Test 505 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 505 failed: {e}")
        test_results.append(False)

    # Test case 506
    try:
        result = differenceMinMax([0, 1, 1, 0, 3, 5, 8, 13, 21, 34])
        assert result == 34, f"Test 506 failed: got {result}, expected {34}"
        print(f"Test 506 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 506 failed: {e}")
        test_results.append(False)

    # Test case 507
    try:
        result = differenceMinMax([1, 1, 2, 3, 5, 8, 13, 21, 34, 0])
        assert result == 34, f"Test 507 failed: got {result}, expected {34}"
        print(f"Test 507 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 507 failed: {e}")
        test_results.append(False)

    # Test case 508
    try:
        result = differenceMinMax([1, 1, 2, 3, 5, 8, 13, 34])
        assert result == 33, f"Test 508 failed: got {result}, expected {33}"
        print(f"Test 508 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 508 failed: {e}")
        test_results.append(False)

    # Test case 509
    try:
        result = differenceMinMax([34, 13, 8, 5, 3, 2, 1, 1, 0, 0])
        assert result == 34, f"Test 509 failed: got {result}, expected {34}"
        print(f"Test 509 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 509 failed: {e}")
        test_results.append(False)

    # Test case 510
    try:
        result = differenceMinMax([-999999, 1, 2, 3, 5, 13, 21, 34])
        assert result == 1000033, f"Test 510 failed: got {result}, expected {1000033}"
        print(f"Test 510 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 510 failed: {e}")
        test_results.append(False)

    # Test case 511
    try:
        result = differenceMinMax([1, 0, 2, 3, 5, 8, 13, 21, 33])
        assert result == 33, f"Test 511 failed: got {result}, expected {33}"
        print(f"Test 511 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 511 failed: {e}")
        test_results.append(False)

    # Test case 512
    try:
        result = differenceMinMax([34, 21, 8, 5, 3, 1, 1, 1, 9223372036854775806])
        assert result == 9223372036854775805, f"Test 512 failed: got {result}, expected {9223372036854775805}"
        print(f"Test 512 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 512 failed: {e}")
        test_results.append(False)

    # Test case 513
    try:
        result = differenceMinMax([1, 1, 2, 3, 5, 8, 13, 0, 34, 0, 33])
        assert result == 34, f"Test 513 failed: got {result}, expected {34}"
        print(f"Test 513 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 513 failed: {e}")
        test_results.append(False)

    # Test case 514
    try:
        result = differenceMinMax([1, 1, 2, 3, 5, 8, 13, 21, 34, -8])
        assert result == 42, f"Test 514 failed: got {result}, expected {42}"
        print(f"Test 514 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 514 failed: {e}")
        test_results.append(False)

    # Test case 515
    try:
        result = differenceMinMax([1, -12, 3, 5, 8, 13, 21, 34])
        assert result == 46, f"Test 515 failed: got {result}, expected {46}"
        print(f"Test 515 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 515 failed: {e}")
        test_results.append(False)

    # Test case 516
    try:
        result = differenceMinMax([-44])
        assert result == 0, f"Test 516 failed: got {result}, expected {0}"
        print(f"Test 516 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 516 failed: {e}")
        test_results.append(False)

    # Test case 517
    try:
        result = differenceMinMax([123456789, 0])
        assert result == 123456789, f"Test 517 failed: got {result}, expected {123456789}"
        print(f"Test 517 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 517 failed: {e}")
        test_results.append(False)

    # Test case 518
    try:
        result = differenceMinMax([0, 1000000000000])
        assert result == 1000000000000, f"Test 518 failed: got {result}, expected {1000000000000}"
        print(f"Test 518 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 518 failed: {e}")
        test_results.append(False)

    # Test case 519
    try:
        result = differenceMinMax([-1, 1000000000000])
        assert result == 1000000000001, f"Test 519 failed: got {result}, expected {1000000000001}"
        print(f"Test 519 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 519 failed: {e}")
        test_results.append(False)

    # Test case 520
    try:
        result = differenceMinMax([1000001, -987654324, 14])
        assert result == 988654325, f"Test 520 failed: got {result}, expected {988654325}"
        print(f"Test 520 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 520 failed: {e}")
        test_results.append(False)

    # Test case 521
    try:
        result = differenceMinMax([-40])
        assert result == 0, f"Test 521 failed: got {result}, expected {0}"
        print(f"Test 521 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 521 failed: {e}")
        test_results.append(False)

    # Test case 522
    try:
        result = differenceMinMax([14, 0])
        assert result == 14, f"Test 522 failed: got {result}, expected {14}"
        print(f"Test 522 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 522 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
