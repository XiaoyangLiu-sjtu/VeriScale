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
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == 8, f"Test 7 failed: got {result}, expected {8}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = differenceMinMax([1, -1, 1, -1, 1, -1])
        assert result == 2, f"Test 8 failed: got {result}, expected {2}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = differenceMinMax([0, -1, -2, -3, -4, -5])
        assert result == 5, f"Test 9 failed: got {result}, expected {5}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = differenceMinMax([8, -8, 8, -8, 8])
        assert result == 16, f"Test 10 failed: got {result}, expected {16}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = differenceMinMax([-999999, -1000000, -999998])
        assert result == 2, f"Test 11 failed: got {result}, expected {2}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = differenceMinMax([3, 1, 4, 5, 9, 2, 6, 5, 3, 5])
        assert result == 8, f"Test 12 failed: got {result}, expected {8}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = differenceMinMax([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0])
        assert result == 9, f"Test 13 failed: got {result}, expected {9}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = differenceMinMax([6, 1, 4, 1, 5, 9, 2, 5, 3, 5, 6])
        assert result == 8, f"Test 14 failed: got {result}, expected {8}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = differenceMinMax([5, 3, 5, 6, 2, 9, 5, 1, 4, 1])
        assert result == 8, f"Test 15 failed: got {result}, expected {8}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = differenceMinMax([10, 20, 30, 40, 50, -2147483648, 0, 987654321])
        assert result == 3135137969, f"Test 16 failed: got {result}, expected {3135137969}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = differenceMinMax([34, 50, 40, 30, 20, 10])
        assert result == 40, f"Test 17 failed: got {result}, expected {40}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = differenceMinMax([0, -1000000])
        assert result == 1000000, f"Test 18 failed: got {result}, expected {1000000}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = differenceMinMax([5, 5, 5, -1000000])
        assert result == 1000005, f"Test 19 failed: got {result}, expected {1000005}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = differenceMinMax([5, 5, 5, 5, -31])
        assert result == 36, f"Test 20 failed: got {result}, expected {36}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = differenceMinMax([5, 5, -1000000000000, 0])
        assert result == 1000000000005, f"Test 21 failed: got {result}, expected {1000000000005}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = differenceMinMax([-2, 2, 11])
        assert result == 13, f"Test 22 failed: got {result}, expected {13}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = differenceMinMax([1, -1, 2])
        assert result == 3, f"Test 23 failed: got {result}, expected {3}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = differenceMinMax([0, 1, 0])
        assert result == 1, f"Test 24 failed: got {result}, expected {1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = differenceMinMax([0, -999998, 0])
        assert result == 999998, f"Test 25 failed: got {result}, expected {999998}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = differenceMinMax([0, -987654321, -42, 0, -42])
        assert result == 987654321, f"Test 26 failed: got {result}, expected {987654321}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = differenceMinMax([0, 0, 5, -10])
        assert result == 15, f"Test 27 failed: got {result}, expected {15}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = differenceMinMax([1, 2, 0])
        assert result == 2, f"Test 28 failed: got {result}, expected {2}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = differenceMinMax([1, 1000000000000, 0, 0])
        assert result == 1000000000000, f"Test 29 failed: got {result}, expected {1000000000000}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = differenceMinMax([2, 1, -20, 0])
        assert result == 22, f"Test 30 failed: got {result}, expected {22}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = differenceMinMax([1, -11])
        assert result == 12, f"Test 31 failed: got {result}, expected {12}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = differenceMinMax([0, 0, 0, -19])
        assert result == 19, f"Test 32 failed: got {result}, expected {19}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = differenceMinMax([3, -51, 4, 1, 9, 2, 6, 9223372036854775807])
        assert result == 9223372036854775858, f"Test 33 failed: got {result}, expected {9223372036854775858}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = differenceMinMax([6, 2, 5, 1, 4, 1, 3])
        assert result == 5, f"Test 34 failed: got {result}, expected {5}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = differenceMinMax([1000000000000, -1000000000000, -999999999999999999999998])
        assert result == 1000000000000999999999998, f"Test 35 failed: got {result}, expected {1000000000000999999999998}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = differenceMinMax([9223372036854775808, -9223372036854775808, 0])
        assert result == 18446744073709551616, f"Test 36 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = differenceMinMax([-5, -3, 1, -1, 1, -1, 1])
        assert result == 6, f"Test 37 failed: got {result}, expected {6}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = differenceMinMax([34, 0, 2147483648, -999999999999999999999998, 0])
        assert result == 1000000000000002147483646, f"Test 38 failed: got {result}, expected {1000000000000002147483646}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = differenceMinMax([7, 7, 6, 7, 7])
        assert result == 1, f"Test 39 failed: got {result}, expected {1}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = differenceMinMax([7, 7, 7, 7, 7, 21, 0, 0])
        assert result == 21, f"Test 40 failed: got {result}, expected {21}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = differenceMinMax([7, 7, 7, 7, 7, 0])
        assert result == 7, f"Test 41 failed: got {result}, expected {7}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = differenceMinMax([-5, -4, -3, -2, -1, 0])
        assert result == 5, f"Test 42 failed: got {result}, expected {5}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = differenceMinMax([0, -5, -4, -4, -2, -1, 0, 0])
        assert result == 5, f"Test 43 failed: got {result}, expected {5}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = differenceMinMax([0, 1, 2, 2, 4, 5, 42])
        assert result == 42, f"Test 44 failed: got {result}, expected {42}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = differenceMinMax([5, 4, 3, 2, 1, 0, -123456789, 0, 0])
        assert result == 123456794, f"Test 45 failed: got {result}, expected {123456794}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = differenceMinMax([0, 1, 2, 3, 4, 5, 0])
        assert result == 5, f"Test 46 failed: got {result}, expected {5}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = differenceMinMax([0, 1000000000000, -999999999999999999999998])
        assert result == 1000000000000999999999998, f"Test 47 failed: got {result}, expected {1000000000000999999999998}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = differenceMinMax([0, 999999999999999999999999, -999999999999999999999998, 0])
        assert result == 1999999999999999999999997, f"Test 48 failed: got {result}, expected {1999999999999999999999997}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = differenceMinMax([13, -21, 34, -55, 89, -144, 0, 0])
        assert result == 233, f"Test 49 failed: got {result}, expected {233}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = differenceMinMax([13, -21, -6, -55, 89, -144])
        assert result == 233, f"Test 50 failed: got {result}, expected {233}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = differenceMinMax([100, -100, 101, 0])
        assert result == 201, f"Test 51 failed: got {result}, expected {201}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = differenceMinMax([4, 0, 6, 6, 0])
        assert result == 6, f"Test 52 failed: got {result}, expected {6}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = differenceMinMax([-999998, -999999, -1000000, 6])
        assert result == 1000006, f"Test 53 failed: got {result}, expected {1000006}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = differenceMinMax([0, 17, -999998, -1000000, -999999, 0])
        assert result == 1000017, f"Test 54 failed: got {result}, expected {1000017}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = differenceMinMax([34, 13, 8, 5, 3, 2, 1, 1, 0, 0])
        assert result == 34, f"Test 55 failed: got {result}, expected {34}"
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
