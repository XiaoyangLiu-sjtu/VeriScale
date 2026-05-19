# Coverage Report

Total executable lines: 11
Covered lines: 11
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def firstEvenOddDifference(a):
2: ✓     first_even = None
3: ✓     first_odd = None
4: ✓     for num in a:
5: ✓         if first_even is None and num % 2 == 0:
6: ✓             first_even = num
7: ✓         if first_odd is None and num % 2 != 0:
8: ✓             first_odd = num
9: ✓         if first_even is not None and first_odd is not None:
10: ✓             break
11: ✓     return first_even - first_odd
```

## Complete Test File

```python
def firstEvenOddDifference(a):
    first_even = None
    first_odd = None
    for num in a:
        if first_even is None and num % 2 == 0:
            first_even = num
        if first_odd is None and num % 2 != 0:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    return first_even - first_odd

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = firstEvenOddDifference([2, 3, 4, 5])
        assert result == -1, f"Test 1 failed: got {result}, expected {-1}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = firstEvenOddDifference([1, 4, 6, 8])
        assert result == 3, f"Test 2 failed: got {result}, expected {3}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = firstEvenOddDifference([7, 2, 9, 4])
        assert result == -5, f"Test 3 failed: got {result}, expected {-5}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = firstEvenOddDifference([2, 2, 3, 3])
        assert result == -1, f"Test 4 failed: got {result}, expected {-1}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = firstEvenOddDifference([1, 1, 2, 2])
        assert result == 1, f"Test 5 failed: got {result}, expected {1}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = firstEvenOddDifference([0, -1, -2, -3])
        assert result == 1, f"Test 6 failed: got {result}, expected {1}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = firstEvenOddDifference([2, -5, 7, 9, 10])
        assert result == 7, f"Test 7 failed: got {result}, expected {7}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = firstEvenOddDifference([-7, 14, 21, 28])
        assert result == 21, f"Test 8 failed: got {result}, expected {21}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = firstEvenOddDifference([0, 3, 4, 5, 14])
        assert result == -3, f"Test 9 failed: got {result}, expected {-3}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = firstEvenOddDifference([6, 4, 1])
        assert result == 5, f"Test 10 failed: got {result}, expected {5}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = firstEvenOddDifference([0, 999999999999999999999999999999, 15, 8, 0, 0])
        assert result == -999999999999999999999999999999, f"Test 11 failed: got {result}, expected {-999999999999999999999999999999}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = firstEvenOddDifference([4, 6, 8, 0, 11, 0])
        assert result == -7, f"Test 12 failed: got {result}, expected {-7}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = firstEvenOddDifference([8, 2, 9, 4, 0])
        assert result == -1, f"Test 13 failed: got {result}, expected {-1}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = firstEvenOddDifference([14, 2, 9, 4, 0, 0])
        assert result == 5, f"Test 14 failed: got {result}, expected {5}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = firstEvenOddDifference([-2, -3, 0, -1000000000000000001, 6])
        assert result == 1, f"Test 15 failed: got {result}, expected {1}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = firstEvenOddDifference([-3, -2, 7, -8, 0])
        assert result == 1, f"Test 16 failed: got {result}, expected {1}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = firstEvenOddDifference([42, 0, -2, -3, 0])
        assert result == 45, f"Test 17 failed: got {result}, expected {45}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = firstEvenOddDifference([2, 1, 1, 1, -2147483648])
        assert result == 1, f"Test 18 failed: got {result}, expected {1}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = firstEvenOddDifference([0, -2147483647, 14, 11, 9, 7])
        assert result == 2147483647, f"Test 19 failed: got {result}, expected {2147483647}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = firstEvenOddDifference([0, 1, 2, 3, 4, 5])
        assert result == -1, f"Test 20 failed: got {result}, expected {-1}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = firstEvenOddDifference([-2147483648, 4, 2, 1, 5])
        assert result == -2147483649, f"Test 21 failed: got {result}, expected {-2147483649}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = firstEvenOddDifference([11, 12, 13, 0, 0])
        assert result == 1, f"Test 22 failed: got {result}, expected {1}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = firstEvenOddDifference([13, 11, 10, -2147483648])
        assert result == -3, f"Test 23 failed: got {result}, expected {-3}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = firstEvenOddDifference([10, 11, 12, 13, -8])
        assert result == -1, f"Test 24 failed: got {result}, expected {-1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = firstEvenOddDifference([-10, 15, 7, 0, 0, 0, 0])
        assert result == -25, f"Test 25 failed: got {result}, expected {-25}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = firstEvenOddDifference([-10, 15, -8, 7, 28])
        assert result == -25, f"Test 26 failed: got {result}, expected {-25}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = firstEvenOddDifference([-1000000000000000001, 15, -10, 7, -8, 0, 5])
        assert result == 999999999999999991, f"Test 27 failed: got {result}, expected {999999999999999991}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = firstEvenOddDifference([42, 3])
        assert result == 39, f"Test 28 failed: got {result}, expected {39}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = firstEvenOddDifference([2, 3, 1000000000000000000])
        assert result == -1, f"Test 29 failed: got {result}, expected {-1}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = firstEvenOddDifference([-2147483648, 10, 8, -13])
        assert result == -2147483635, f"Test 30 failed: got {result}, expected {-2147483635}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = firstEvenOddDifference([20, 12, -1000000000000000001, -3, 8, 3, 6])
        assert result == 1000000000000000021, f"Test 31 failed: got {result}, expected {1000000000000000021}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = firstEvenOddDifference([-1, 8, -3, 2147483647])
        assert result == 9, f"Test 32 failed: got {result}, expected {9}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = firstEvenOddDifference([0, -1, 6, -3, 0])
        assert result == 1, f"Test 33 failed: got {result}, expected {1}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = firstEvenOddDifference([2, -11, 4, 1, 2, 2])
        assert result == 13, f"Test 34 failed: got {result}, expected {13}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = firstEvenOddDifference([9, 8, 7, 6, 5, 4, 3, 2, 2147483647, 0])
        assert result == -1, f"Test 35 failed: got {result}, expected {-1}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = firstEvenOddDifference([-16, 8, 7, 6, 5, 3, 2, 0])
        assert result == -23, f"Test 36 failed: got {result}, expected {-23}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = firstEvenOddDifference([4, 9, 2, 7, 6, 5, 2147483646])
        assert result == -5, f"Test 37 failed: got {result}, expected {-5}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = firstEvenOddDifference([5, 6, 7, 2, 9, 4])
        assert result == 1, f"Test 38 failed: got {result}, expected {1}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = firstEvenOddDifference([4, 9, 2, 7, 6, 5, 0, 0])
        assert result == -5, f"Test 39 failed: got {result}, expected {-5}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = firstEvenOddDifference([-999999999999999999999999999998, -3, 1000000000000000001, 5, 6, 7, 2, 9, 4, 0])
        assert result == -999999999999999999999999999995, f"Test 40 failed: got {result}, expected {-999999999999999999999999999995}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = firstEvenOddDifference([4, 9, 2, -12, 5])
        assert result == -5, f"Test 41 failed: got {result}, expected {-5}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = firstEvenOddDifference([0, 5, 6, 7, 2, 9, 4, 4, 9, 1000000000000000001])
        assert result == -5, f"Test 42 failed: got {result}, expected {-5}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = firstEvenOddDifference([0, 2000000000000000000, 5, 6, 0, 2, 9, 4, 2])
        assert result == -5, f"Test 43 failed: got {result}, expected {-5}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = firstEvenOddDifference([0, 0, 0, 12, 11])
        assert result == -11, f"Test 44 failed: got {result}, expected {-11}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = firstEvenOddDifference([30, -3, -1, -1, 0, -1000000000000000000])
        assert result == 33, f"Test 45 failed: got {result}, expected {33}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = firstEvenOddDifference([0, -1, -2, -3, 0, 0, -11, 0])
        assert result == 1, f"Test 46 failed: got {result}, expected {1}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = firstEvenOddDifference([3, -7, 0, -1, -10])
        assert result == -3, f"Test 47 failed: got {result}, expected {-3}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = firstEvenOddDifference([999999999999999999999999999999, -2, 0, -9, 0])
        assert result == -1000000000000000000000000000001, f"Test 48 failed: got {result}, expected {-1000000000000000000000000000001}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = firstEvenOddDifference([0, 5, -1999999999999999999999999999996])
        assert result == -5, f"Test 49 failed: got {result}, expected {-5}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = firstEvenOddDifference([2, -5, 7, 9, 10, -1999999999999999999999999999996, 5, 0])
        assert result == 7, f"Test 50 failed: got {result}, expected {7}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = firstEvenOddDifference([10, 9, 7, -5, 2, 12, -12])
        assert result == 1, f"Test 51 failed: got {result}, expected {1}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = firstEvenOddDifference([-7, 14, 21, 28, 0])
        assert result == 21, f"Test 52 failed: got {result}, expected {21}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = firstEvenOddDifference([-11, 2147483647, -7, 14, 22, 28])
        assert result == 25, f"Test 53 failed: got {result}, expected {25}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = firstEvenOddDifference([1000000000000000000, 5, 3, 1])
        assert result == 999999999999999995, f"Test 54 failed: got {result}, expected {999999999999999995}"
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
