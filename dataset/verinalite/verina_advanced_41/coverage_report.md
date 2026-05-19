# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def maxOfThree(a, b, c):
2: ✓     return max(a, b, c)
```

## Complete Test File

```python
def maxOfThree(a, b, c):
    return max(a, b, c)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = maxOfThree(3, 2, 1)
        assert result == 3, f"Test 1 failed: got {result}, expected {3}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = maxOfThree(5, 5, 5)
        assert result == 5, f"Test 2 failed: got {result}, expected {5}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = maxOfThree(10, 20, 15)
        assert result == 20, f"Test 3 failed: got {result}, expected {20}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = maxOfThree(-1, -2, -3)
        assert result == -1, f"Test 4 failed: got {result}, expected {-1}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = maxOfThree(0, -10, -5)
        assert result == 0, f"Test 5 failed: got {result}, expected {0}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = maxOfThree(-9223372036854775808, -1, 0)
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = maxOfThree(9223372036854775807, 9223372036854775806, 9223372036854775805)
        assert result == 9223372036854775807, f"Test 7 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = maxOfThree(9223372036854775808, -9223372036854775809, 0)
        assert result == 9223372036854775808, f"Test 8 failed: got {result}, expected {9223372036854775808}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = maxOfThree(-1000000000000000000, -999999999999999999, -1000000000000000001)
        assert result == -999999999999999999, f"Test 9 failed: got {result}, expected {-999999999999999999}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = maxOfThree(-123456789, -987654321, -555555555)
        assert result == -123456789, f"Test 10 failed: got {result}, expected {-123456789}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = maxOfThree(42, -42, 0)
        assert result == 42, f"Test 11 failed: got {result}, expected {42}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = maxOfThree(8, 9, 8)
        assert result == 9, f"Test 12 failed: got {result}, expected {9}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = maxOfThree(-3, 2, 1)
        assert result == 2, f"Test 13 failed: got {result}, expected {2}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = maxOfThree(1000000000000000002, 2, 0)
        assert result == 1000000000000000002, f"Test 14 failed: got {result}, expected {1000000000000000002}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = maxOfThree(2, 0, 9223372036854775807)
        assert result == 9223372036854775807, f"Test 15 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = maxOfThree(3, 9223372036854775805, 0)
        assert result == 9223372036854775805, f"Test 16 failed: got {result}, expected {9223372036854775805}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = maxOfThree(2, 0, -1)
        assert result == 2, f"Test 17 failed: got {result}, expected {2}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = maxOfThree(9223372036854775807, 1618033988749894, 5)
        assert result == 9223372036854775807, f"Test 18 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = maxOfThree(1618033988749893, 9223372036854775808, 5)
        assert result == 9223372036854775808, f"Test 19 failed: got {result}, expected {9223372036854775808}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = maxOfThree(10, -9223372036854775809, -6)
        assert result == 10, f"Test 20 failed: got {result}, expected {10}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = maxOfThree(-1, -2, 0)
        assert result == 0, f"Test 21 failed: got {result}, expected {0}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = maxOfThree(-104, -123456790, -4)
        assert result == -4, f"Test 22 failed: got {result}, expected {-4}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = maxOfThree(0, 2, -999999999999999999)
        assert result == 2, f"Test 23 failed: got {result}, expected {2}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = maxOfThree(1, 0, 9223372036854775807)
        assert result == 9223372036854775807, f"Test 24 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = maxOfThree(1, -123456790, 4)
        assert result == 4, f"Test 25 failed: got {result}, expected {4}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = maxOfThree(0, 0, 3)
        assert result == 3, f"Test 26 failed: got {result}, expected {3}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = maxOfThree(13, 0, 2)
        assert result == 13, f"Test 27 failed: got {result}, expected {13}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = maxOfThree(9223372036854775807, 3, 2)
        assert result == 9223372036854775807, f"Test 28 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = maxOfThree(-6, -5, 4)
        assert result == 4, f"Test 29 failed: got {result}, expected {4}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = maxOfThree(-2, -7, -9)
        assert result == -2, f"Test 30 failed: got {result}, expected {-2}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = maxOfThree(0, -1, -4)
        assert result == 0, f"Test 31 failed: got {result}, expected {0}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = maxOfThree(10, -1, 13)
        assert result == 13, f"Test 32 failed: got {result}, expected {13}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = maxOfThree(-987654321, 6283185307179584, 10)
        assert result == 6283185307179584, f"Test 33 failed: got {result}, expected {6283185307179584}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = maxOfThree(101, 0, 10)
        assert result == 101, f"Test 34 failed: got {result}, expected {101}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = maxOfThree(-9223372036854775807, 7, 0)
        assert result == 7, f"Test 35 failed: got {result}, expected {7}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = maxOfThree(18446744073709551613, 0, -19)
        assert result == 18446744073709551613, f"Test 36 failed: got {result}, expected {18446744073709551613}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = maxOfThree(9223372036854775806, 9223372036854775806, -18446744073709551608)
        assert result == 9223372036854775806, f"Test 37 failed: got {result}, expected {9223372036854775806}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = maxOfThree(18446744073709551614, 9223372036854775806, 9223372036854775806)
        assert result == 18446744073709551614, f"Test 38 failed: got {result}, expected {18446744073709551614}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = maxOfThree(0, 9223372036854775807, -18446744073709551612)
        assert result == 9223372036854775807, f"Test 39 failed: got {result}, expected {9223372036854775807}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = maxOfThree(9223372036854775809, -9223372036854775808, 0)
        assert result == 9223372036854775809, f"Test 40 failed: got {result}, expected {9223372036854775809}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = maxOfThree(9223372036854775809, -9223372036854775809, 0)
        assert result == 9223372036854775809, f"Test 41 failed: got {result}, expected {9223372036854775809}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = maxOfThree(9223372036854775808, -9223372036854775809, 1)
        assert result == 9223372036854775808, f"Test 42 failed: got {result}, expected {9223372036854775808}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = maxOfThree(1000000000000000000, 1000000000000000001, 2000000000000000002)
        assert result == 2000000000000000002, f"Test 43 failed: got {result}, expected {2000000000000000002}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = maxOfThree(1000000000000000000, -4, 1000000000000000001)
        assert result == 1000000000000000001, f"Test 44 failed: got {result}, expected {1000000000000000001}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = maxOfThree(1000000000000000001, -999999999999999999, 0)
        assert result == 1000000000000000001, f"Test 45 failed: got {result}, expected {1000000000000000001}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = maxOfThree(-123456790, 987654321, 555555556)
        assert result == 987654321, f"Test 46 failed: got {result}, expected {987654321}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = maxOfThree(3141592653589793, -43, 0)
        assert result == 3141592653589793, f"Test 47 failed: got {result}, expected {3141592653589793}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = maxOfThree(42, -999999999999999998, -123456789)
        assert result == 42, f"Test 48 failed: got {result}, expected {42}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = maxOfThree(0, 2147483646, -2147483648)
        assert result == 2147483646, f"Test 49 failed: got {result}, expected {2147483646}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = maxOfThree(50, -2147483647, 20)
        assert result == 50, f"Test 50 failed: got {result}, expected {50}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = maxOfThree(0, -76, 2147483647)
        assert result == 2147483647, f"Test 51 failed: got {result}, expected {2147483647}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = maxOfThree(-2147483648, -2147483647, 2147483648)
        assert result == 2147483648, f"Test 52 failed: got {result}, expected {2147483648}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = maxOfThree(-18, 2, -18446744073709551615)
        assert result == 2, f"Test 53 failed: got {result}, expected {2}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = maxOfThree(-1000000000000000002, 0, 1)
        assert result == 1, f"Test 54 failed: got {result}, expected {1}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = maxOfThree(0, -23, 1618033988749895)
        assert result == 1618033988749895, f"Test 55 failed: got {result}, expected {1618033988749895}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
