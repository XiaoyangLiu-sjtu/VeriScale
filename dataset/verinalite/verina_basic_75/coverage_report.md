# Coverage Report

Total executable lines: 6
Covered lines: 6
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def minArray(a):
2: ✓     def helper(i, current_min):
3: ✓         if i == len(a):
4: ✓             return current_min
5: ✓         return helper(i + 1, a[i] if a[i] < current_min else current_min)
6: ✓     return helper(1, a[0])
```

## Complete Test File

```python
def minArray(a):
    def helper(i, current_min):
        if i == len(a):
            return current_min
        return helper(i + 1, a[i] if a[i] < current_min else current_min)
    return helper(1, a[0])

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = minArray([5, 3, 8, 2, 7])
        assert result == 2, f"Test 1 failed: got {result}, expected {2}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = minArray([10, 10, 10])
        assert result == 10, f"Test 2 failed: got {result}, expected {10}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = minArray([-1, -5, 3, 0])
        assert result == -5, f"Test 3 failed: got {result}, expected {-5}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = minArray([42])
        assert result == 42, f"Test 4 failed: got {result}, expected {42}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = minArray([3, -2, 0, -2, 5])
        assert result == -2, f"Test 5 failed: got {result}, expected {-2}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = minArray([8, -3, 15, -3, 8, 0])
        assert result == -3, f"Test 6 failed: got {result}, expected {-3}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = minArray([0, 3, -5, -1, 15, -10])
        assert result == -10, f"Test 7 failed: got {result}, expected {-10}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = minArray([-1, 3, 0, 2])
        assert result == -1, f"Test 8 failed: got {result}, expected {-1}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = minArray([0, 3, -5, -2])
        assert result == -5, f"Test 9 failed: got {result}, expected {-5}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = minArray([85, 1, -42, 0])
        assert result == -42, f"Test 10 failed: got {result}, expected {-42}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = minArray([-5, 0, 42, -20, 0])
        assert result == -20, f"Test 11 failed: got {result}, expected {-20}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = minArray([3, -2, 0, -2, 5, -68, 0])
        assert result == -68, f"Test 12 failed: got {result}, expected {-68}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = minArray([5, -2, 0, -2, 3])
        assert result == -2, f"Test 13 failed: got {result}, expected {-2}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = minArray([-2, -10, -2, 3])
        assert result == -10, f"Test 14 failed: got {result}, expected {-10}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = minArray([0, -2, 5, 0])
        assert result == -2, f"Test 15 failed: got {result}, expected {-2}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = minArray([0, 0, -2147483648, 0, 0])
        assert result == -2147483648, f"Test 16 failed: got {result}, expected {-2147483648}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = minArray([0, -20, 2147483647])
        assert result == -20, f"Test 17 failed: got {result}, expected {-20}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = minArray([0, -7, 0])
        assert result == -7, f"Test 18 failed: got {result}, expected {-7}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = minArray([0, 0, -2, 1])
        assert result == -2, f"Test 19 failed: got {result}, expected {-2}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = minArray([-2147483649, 2])
        assert result == -2147483649, f"Test 20 failed: got {result}, expected {-2147483649}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = minArray([4, -19, 0])
        assert result == -19, f"Test 21 failed: got {result}, expected {-19}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = minArray([0, -1, 0, 1])
        assert result == -1, f"Test 22 failed: got {result}, expected {-1}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = minArray([998, 0, 0, -1])
        assert result == -1, f"Test 23 failed: got {result}, expected {-1}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = minArray([-1, 0, 1, 0, 10])
        assert result == -1, f"Test 24 failed: got {result}, expected {-1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = minArray([100, 3, 3, 9])
        assert result == 3, f"Test 25 failed: got {result}, expected {3}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = minArray([-10, -19, -30, -40, 42])
        assert result == -40, f"Test 26 failed: got {result}, expected {-40}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = minArray([-10, -20, -30, 17, 123456789])
        assert result == -30, f"Test 27 failed: got {result}, expected {-30}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = minArray([-10, -20, -30, -6, 0])
        assert result == -30, f"Test 28 failed: got {result}, expected {-30}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = minArray([-40, 0, 0])
        assert result == -40, f"Test 29 failed: got {result}, expected {-40}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = minArray([1, 3, 6, -12, 25, 50, 100, 0])
        assert result == -12, f"Test 30 failed: got {result}, expected {-12}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = minArray([100, 50, 25, 12, 3, 3])
        assert result == 3, f"Test 31 failed: got {result}, expected {3}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = minArray([1, 3, 6, 12, 25, 50, 8])
        assert result == 1, f"Test 32 failed: got {result}, expected {1}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = minArray([0, -9223372036854775808, 0, -1, 999999999999999999999999, -2, 0])
        assert result == -9223372036854775808, f"Test 33 failed: got {result}, expected {-9223372036854775808}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = minArray([25, -1, -1, -1, 0, 0])
        assert result == -1, f"Test 34 failed: got {result}, expected {-1}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = minArray([1000, 0, 0, -1, 1000, -1, 0])
        assert result == -1, f"Test 35 failed: got {result}, expected {-1}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = minArray([13, -1, -1, 0, 5])
        assert result == -1, f"Test 36 failed: got {result}, expected {-1}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = minArray([0, 0, 0, -1, -1, -1, 0, 17])
        assert result == -1, f"Test 37 failed: got {result}, expected {-1}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = minArray([0, -1, -1, 0, 0])
        assert result == -1, f"Test 38 failed: got {result}, expected {-1}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = minArray([9223372036854775807, 11])
        assert result == 11, f"Test 39 failed: got {result}, expected {11}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = minArray([1, -9223372036854775808, 26])
        assert result == -9223372036854775808, f"Test 40 failed: got {result}, expected {-9223372036854775808}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = minArray([-9223372036854775808, 0, 0])
        assert result == -9223372036854775808, f"Test 41 failed: got {result}, expected {-9223372036854775808}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = minArray([0, 0, 7, -999999999999999999999998, 999999999999999999999999])
        assert result == -999999999999999999999998, f"Test 42 failed: got {result}, expected {-999999999999999999999998}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = minArray([999999999999999999999999, -999999999999999999999998, 7, 15])
        assert result == -999999999999999999999998, f"Test 43 failed: got {result}, expected {-999999999999999999999998}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = minArray([123456789, 998, -998, 999, 1000, -1000, 100])
        assert result == -1000, f"Test 44 failed: got {result}, expected {-1000}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = minArray([-1000, 1000, -999, 999, -998, 998, 1])
        assert result == -1000, f"Test 45 failed: got {result}, expected {-1000}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = minArray([2, -9223372036854775807, 2, 4, 2, 2])
        assert result == -9223372036854775807, f"Test 46 failed: got {result}, expected {-9223372036854775807}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = minArray([17, 85, 51, -34, 17])
        assert result == -34, f"Test 47 failed: got {result}, expected {-34}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = minArray([17, -34, 51, -68, 85, -102, 999, 0, -35])
        assert result == -102, f"Test 48 failed: got {result}, expected {-102}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = minArray([3, -1, 4, -1, 4, 0])
        assert result == -1, f"Test 49 failed: got {result}, expected {-1}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = minArray([4, -1, 4, -1, 4, -1, 0, 0])
        assert result == -1, f"Test 50 failed: got {result}, expected {-1}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = minArray([-999999999, -10, -998, 42])
        assert result == -999999999, f"Test 51 failed: got {result}, expected {-999999999}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = minArray([-999999999, 0, 0, -999999999999999999999999, 51, 0])
        assert result == -999999999999999999999999, f"Test 52 failed: got {result}, expected {-999999999999999999999999}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = minArray([8, -3, 15, -3, 9, 0, -12, 0])
        assert result == -12, f"Test 53 failed: got {result}, expected {-12}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = minArray([8, -3, -3, 8, 0, 0])
        assert result == -3, f"Test 54 failed: got {result}, expected {-3}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = minArray([0, 8, -3, 15, -3, 8, 2, 49])
        assert result == -3, f"Test 55 failed: got {result}, expected {-3}"
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
