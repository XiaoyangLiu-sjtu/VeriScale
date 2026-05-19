# Coverage Report

Total executable lines: 9
Covered lines: 9
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def LongestIncreasingSubsequence(a):
2: ✓     import bisect
3: ✓     sub = []
4: ✓     for num in a:
5: ✓         pos = bisect.bisect_left(sub, num)
6: ✓         if pos == len(sub):
7: ✓             sub.append(num)
8:           else:
9: ✓             sub[pos] = num
10: ✓     return len(sub)
```

## Complete Test File

```python
def LongestIncreasingSubsequence(a):
    import bisect
    sub = []
    for num in a:
        pos = bisect.bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num
    return len(sub)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = LongestIncreasingSubsequence([5, 2, 8, 6, 3, 6, 9, 7])
        assert result == 4, f"Test 1 failed: got {result}, expected {4}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = LongestIncreasingSubsequence([3, 1, 2, 1, 0])
        assert result == 2, f"Test 2 failed: got {result}, expected {2}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = LongestIncreasingSubsequence([2, 3, -2, -1, 7, 19, 3, 6, -4, 6, -7, 0, 9, 12, 10])
        assert result == 6, f"Test 3 failed: got {result}, expected {6}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = LongestIncreasingSubsequence([5, -5, -3, 2, 4, 1, 0, -1, 3, 2, 0])
        assert result == 4, f"Test 4 failed: got {result}, expected {4}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = LongestIncreasingSubsequence([1, 7, 23, 14, -4, 21, 8, 2, -1, 9, 12, 2])
        assert result == 5, f"Test 5 failed: got {result}, expected {5}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = LongestIncreasingSubsequence([])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = LongestIncreasingSubsequence([4, 4, 4, 5, 5, 6, 6, 6])
        assert result == 3, f"Test 7 failed: got {result}, expected {3}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = LongestIncreasingSubsequence([1, 3, 5, 7, 6, 4, 2])
        assert result == 4, f"Test 8 failed: got {result}, expected {4}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = LongestIncreasingSubsequence([1, 3, 2, 4, 3, 5, 4, 6])
        assert result == 5, f"Test 9 failed: got {result}, expected {5}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = LongestIncreasingSubsequence([8, 1, 6, 2, 7, 3, 9, 4, 10, 5, 11, -1, 12, -2, 13, -3, 14, -4, 15, -5])
        assert result == 10, f"Test 10 failed: got {result}, expected {10}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = LongestIncreasingSubsequence([1, 2, 3, 100, 4, 5, 6, 7])
        assert result == 7, f"Test 11 failed: got {result}, expected {7}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = LongestIncreasingSubsequence([5, 2, 8, 6, 3, 6, 23, 0, 0])
        assert result == 4, f"Test 12 failed: got {result}, expected {4}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = LongestIncreasingSubsequence([-9, 21, 2, 1, 3, 0])
        assert result == 3, f"Test 13 failed: got {result}, expected {3}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = LongestIncreasingSubsequence([-4, -9, 2, 0, -999999999])
        assert result == 2, f"Test 14 failed: got {result}, expected {2}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = LongestIncreasingSubsequence([1, 2, 1, 0, 9223372036854775807, 0, 0])
        assert result == 3, f"Test 15 failed: got {result}, expected {3}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = LongestIncreasingSubsequence([0, 10, 12, 9, 0, -7, -4, 6, 3, 19, 7, -1, -2, 3, 2, 13, -8])
        assert result == 5, f"Test 16 failed: got {result}, expected {5}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = LongestIncreasingSubsequence([2, 3, -2, -1, 7, 19, 3, 7, 13, 6, -7, 0, 9, 12])
        assert result == 6, f"Test 17 failed: got {result}, expected {6}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = LongestIncreasingSubsequence([2, 3, -2, -1, 7, 19, 3, 6, -4, 6, -7, 0, 12, 10])
        assert result == 5, f"Test 18 failed: got {result}, expected {5}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = LongestIncreasingSubsequence([0, 2, 3, -1, 0, 1, 4, 2, -3, -10, 5])
        assert result == 5, f"Test 19 failed: got {result}, expected {5}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = LongestIncreasingSubsequence([-1000000000000, 1, 0, 2, 3, -1, 0, 1, 4, -2, -3, -5, 5, 0])
        assert result == 6, f"Test 20 failed: got {result}, expected {6}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = LongestIncreasingSubsequence([5, -5, -3, 2, 4, 1, 0, -1, 3, 2, 0, 0, -5])
        assert result == 4, f"Test 21 failed: got {result}, expected {4}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = LongestIncreasingSubsequence([2, 12, 9, -1, -2, 21, 14, 23, 0, 1])
        assert result == 4, f"Test 22 failed: got {result}, expected {4}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = LongestIncreasingSubsequence([1, 7, 23, 14, -4, 21, 8, 2, 9, 12, 1, 4, 0])
        assert result == 5, f"Test 23 failed: got {result}, expected {5}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = LongestIncreasingSubsequence([2, 12, 9, -1, 2, 8, 21, -4, 14, 23, 7, 1])
        assert result == 5, f"Test 24 failed: got {result}, expected {5}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = LongestIncreasingSubsequence([1, 7, 23, 14, 21, 8, 2, -1, 9, 12, 2, 0])
        assert result == 5, f"Test 25 failed: got {result}, expected {5}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = LongestIncreasingSubsequence([4, 6, 2, 1, 0])
        assert result == 2, f"Test 26 failed: got {result}, expected {2}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = LongestIncreasingSubsequence([5, -4, 3, 2, 1, 0])
        assert result == 2, f"Test 27 failed: got {result}, expected {2}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = LongestIncreasingSubsequence([1, 0, 2, 3, 3, 21])
        assert result == 4, f"Test 28 failed: got {result}, expected {4}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = LongestIncreasingSubsequence([102, -4, -3, -2, -1, 9223372036854775806])
        assert result == 5, f"Test 29 failed: got {result}, expected {5}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = LongestIncreasingSubsequence([21, -4, -3, -2, -1, 0, 102])
        assert result == 6, f"Test 30 failed: got {result}, expected {6}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = LongestIncreasingSubsequence([6, 0, 5, 2, 4, 1, 16])
        assert result == 4, f"Test 31 failed: got {result}, expected {4}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = LongestIncreasingSubsequence([3, 1, 4, 2, 5, 0, 6, 12, 0, 6])
        assert result == 5, f"Test 32 failed: got {result}, expected {5}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = LongestIncreasingSubsequence([3, 1, 2, 5, 0, -2])
        assert result == 3, f"Test 33 failed: got {result}, expected {3}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = LongestIncreasingSubsequence([0, 0, -999999999, 999999999, -1000000000, 1000000000])
        assert result == 3, f"Test 34 failed: got {result}, expected {3}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = LongestIncreasingSubsequence([1000000000, -1000000000, -999999999, 0, 0])
        assert result == 3, f"Test 35 failed: got {result}, expected {3}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = LongestIncreasingSubsequence([10, 9, 7, 6, 4, 3, 2, 1])
        assert result == 1, f"Test 36 failed: got {result}, expected {1}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = LongestIncreasingSubsequence([1, 2, 5, 6, 7, 8, 9, 10, 0, 1000000000000])
        assert result == 9, f"Test 37 failed: got {result}, expected {9}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = LongestIncreasingSubsequence([11, 0, 8, 7, 5, 0, 3, 2, 1, 19])
        assert result == 3, f"Test 38 failed: got {result}, expected {3}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = LongestIncreasingSubsequence([18, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        assert result == 1, f"Test 39 failed: got {result}, expected {1}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = LongestIncreasingSubsequence([1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, 0])
        assert result == 2, f"Test 40 failed: got {result}, expected {2}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = LongestIncreasingSubsequence([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, -999999999])
        assert result == 12, f"Test 41 failed: got {result}, expected {12}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = LongestIncreasingSubsequence([4, 4, 4, 5, 5, 6, 6, 6, -888888888888])
        assert result == 3, f"Test 42 failed: got {result}, expected {3}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = LongestIncreasingSubsequence([9223372036854775806, 4, 4, 5, 5, 6, 7, 6])
        assert result == 4, f"Test 43 failed: got {result}, expected {4}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = LongestIncreasingSubsequence([1, 3, 5, 999999999, 6, -4, 2])
        assert result == 4, f"Test 44 failed: got {result}, expected {4}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = LongestIncreasingSubsequence([1, 3, 5, 7, 6, 4, 4, 1000000000])
        assert result == 5, f"Test 45 failed: got {result}, expected {5}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = LongestIncreasingSubsequence([10, 9223372036854775806, -9223372036854775808, 9223372036854775807, -9223372036854775808])
        assert result == 3, f"Test 46 failed: got {result}, expected {3}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = LongestIncreasingSubsequence([-9223372036854775808, -9223372036854775807, -9223372036854775806, -8, 2, 0])
        assert result == 5, f"Test 47 failed: got {result}, expected {5}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = LongestIncreasingSubsequence([-5, 15, -4, 14, -3, 13, -2, -1, 11, 5, 10, 4, 9, 3, 7, 2, 6, 2, 8])
        assert result == 8, f"Test 48 failed: got {result}, expected {8}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = LongestIncreasingSubsequence([5, -1, 4, -2, -1999999999, -3, 2, -4, 1, -5])
        assert result == 3, f"Test 49 failed: got {result}, expected {3}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = LongestIncreasingSubsequence([4, 2])
        assert result == 1, f"Test 50 failed: got {result}, expected {1}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = LongestIncreasingSubsequence([1, 9, 2, 8, 3, 7, 4, 6, 5, 50])
        assert result == 6, f"Test 51 failed: got {result}, expected {6}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = LongestIncreasingSubsequence([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 0])
        assert result == 6, f"Test 52 failed: got {result}, expected {6}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = LongestIncreasingSubsequence([9223372036854775808, -5, 4, -4, 3, -3, 2, -2, 1, -1, 0, -3])
        assert result == 6, f"Test 53 failed: got {result}, expected {6}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = LongestIncreasingSubsequence([2000000000000, -1000000000000, 999999999999, 888888888888, -888888888888])
        assert result == 2, f"Test 54 failed: got {result}, expected {2}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = LongestIncreasingSubsequence([7, -3, 0, -1, 6, -2, 8, -4, 9, 0])
        assert result == 5, f"Test 55 failed: got {result}, expected {5}"
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
