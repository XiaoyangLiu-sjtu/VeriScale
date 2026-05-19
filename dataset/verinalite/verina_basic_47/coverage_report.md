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
        result = arraySum([-1, -2, -3, -4, -5])
        assert result == -15, f"Test 5 failed: got {result}, expected {-15}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = arraySum([3, 3, 3, 3, 3, 3, 3])
        assert result == 21, f"Test 6 failed: got {result}, expected {21}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = arraySum([12345678901234567890, -12345678901234567889])
        assert result == 1, f"Test 7 failed: got {result}, expected {1}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = arraySum([9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == 45, f"Test 8 failed: got {result}, expected {45}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = arraySum([1, 3, 4, 5])
        assert result == 13, f"Test 9 failed: got {result}, expected {13}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = arraySum([1, 2, 6, 4, 5, 0, 0, -21, 33])
        assert result == 30, f"Test 10 failed: got {result}, expected {30}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = arraySum([5, 4, 3, 2, 1, -42, 9, 0])
        assert result == -18, f"Test 11 failed: got {result}, expected {-18}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = arraySum([1, 2, 3, 4, 5, 0, 0])
        assert result == 15, f"Test 12 failed: got {result}, expected {15}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = arraySum([1, 2, 3, 4, -42])
        assert result == -32, f"Test 13 failed: got {result}, expected {-32}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = arraySum([1, 2, 4, 5])
        assert result == 12, f"Test 14 failed: got {result}, expected {12}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = arraySum([0, 17, 16, 42, 14, 12, 0])
        assert result == 101, f"Test 15 failed: got {result}, expected {101}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = arraySum([13, 14, 15, 16, 17, 0])
        assert result == 75, f"Test 16 failed: got {result}, expected {75}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = arraySum([17, 16, 15, 14, 13])
        assert result == 75, f"Test 17 failed: got {result}, expected {75}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = arraySum([-1, -2, -3, 0, 0])
        assert result == -6, f"Test 18 failed: got {result}, expected {-6}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = arraySum([-2, -3, -3, -123456789, 0])
        assert result == -123456797, f"Test 19 failed: got {result}, expected {-123456797}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = arraySum([-1, -2, -2])
        assert result == -5, f"Test 20 failed: got {result}, expected {-5}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = arraySum([-3, -2, -2])
        assert result == -7, f"Test 21 failed: got {result}, expected {-7}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = arraySum([-3, 99, -3, -2, -1])
        assert result == 90, f"Test 22 failed: got {result}, expected {90}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = arraySum([-3, -1, 0])
        assert result == -4, f"Test 23 failed: got {result}, expected {-4}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = arraySum([-10, -11, 3, -400])
        assert result == -418, f"Test 24 failed: got {result}, expected {-418}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = arraySum([-10, 10, 0, 0])
        assert result == 0, f"Test 25 failed: got {result}, expected {0}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = arraySum([10, -10, 21])
        assert result == 21, f"Test 26 failed: got {result}, expected {21}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = arraySum([11, -10, 0, -1000000000000000000000000])
        assert result == -999999999999999999999999, f"Test 27 failed: got {result}, expected {-999999999999999999999999}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = arraySum([-400, 0, -123456789])
        assert result == -123457189, f"Test 28 failed: got {result}, expected {-123457189}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = arraySum([-1, -2, -3, -4, -5, 0])
        assert result == -15, f"Test 29 failed: got {result}, expected {-15}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = arraySum([5, -2, 7, 0, 0, 0, 9223372036854775806])
        assert result == 9223372036854775816, f"Test 30 failed: got {result}, expected {9223372036854775816}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = arraySum([5, -2, 7, -2, 0])
        assert result == 8, f"Test 31 failed: got {result}, expected {8}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = arraySum([2147483647, 1, 0])
        assert result == 2147483648, f"Test 32 failed: got {result}, expected {2147483648}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = arraySum([999999999, -999999999, 123456789, -123456789, 0, 99])
        assert result == 99, f"Test 33 failed: got {result}, expected {99}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = arraySum([-2, -1, 1, -1, 1, -1, 1, -1, 1])
        assert result == -2, f"Test 34 failed: got {result}, expected {-2}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = arraySum([1, -1, 1, -1, 1, -1, 1, -1, -42])
        assert result == -42, f"Test 35 failed: got {result}, expected {-42}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = arraySum([-43, 0, -99, 0, 12345678901234567890])
        assert result == 12345678901234567748, f"Test 36 failed: got {result}, expected {12345678901234567748}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = arraySum([0, -1000000000000000000000001, 3, 3, 3, 3, 3, 3, 17])
        assert result == -999999999999999999999966, f"Test 37 failed: got {result}, expected {-999999999999999999999966}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = arraySum([-3, -3, -3, -3, -3, -3, -3, -9223372036854775810])
        assert result == -9223372036854775831, f"Test 38 failed: got {result}, expected {-9223372036854775831}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = arraySum([10, 1000000000000000000000000, 4, -2, 2, -5, 8])
        assert result == 1000000000000000000000017, f"Test 39 failed: got {result}, expected {1000000000000000000000017}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = arraySum([100, 200, 300, 400, 500, 32])
        assert result == 1532, f"Test 40 failed: got {result}, expected {1532}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = arraySum([100, 200, 300, -400, 500, 0, 1618033988749894])
        assert result == 1618033988750594, f"Test 41 failed: got {result}, expected {1618033988750594}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = arraySum([-44, 0, -21, 21, -14, 14, -7, 0])
        assert result == -51, f"Test 42 failed: got {result}, expected {-51}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = arraySum([9223372036854775808, -12345678901234567889])
        assert result == -3122306864379792081, f"Test 43 failed: got {result}, expected {-3122306864379792081}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = arraySum([65, 0, -500, 256, 128, 32, 16, 8, 4, 2])
        assert result == 11, f"Test 44 failed: got {result}, expected {11}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = arraySum([0, -256, -128, -64, -32, -16, -8, -4, -2])
        assert result == -510, f"Test 45 failed: got {result}, expected {-510}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = arraySum([11, 1, 33, 55, -66, 77])
        assert result == 111, f"Test 46 failed: got {result}, expected {111}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = arraySum([1, 0, 0, 0, 0, 0, 0, 0, -1999999997, 18446744073709551616, 0])
        assert result == 18446744071709551620, f"Test 47 failed: got {result}, expected {18446744071709551620}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = arraySum([42, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert result == 87, f"Test 48 failed: got {result}, expected {87}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = arraySum([9, 7, 6, 5, 6, 3, 2, 1])
        assert result == 39, f"Test 49 failed: got {result}, expected {39}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = arraySum([-12345678901234567890, -2, -3, -4, -5, -6, 7, -7, -9])
        assert result == -12345678901234567919, f"Test 50 failed: got {result}, expected {-12345678901234567919}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = arraySum([-9, -8, -7, -6, -5, -4, -3, -1, -134, 0])
        assert result == -177, f"Test 51 failed: got {result}, expected {-177}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = arraySum([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0])
        assert result == -45, f"Test 52 failed: got {result}, expected {-45}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = arraySum([3141592653589793, -2718281828459045, 1618033988749894, -14, 0, 0, -200])
        assert result == 2041344813880428, f"Test 53 failed: got {result}, expected {2041344813880428}"
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
