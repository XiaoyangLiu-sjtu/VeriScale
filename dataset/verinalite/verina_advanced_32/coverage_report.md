# Coverage Report

Total executable lines: 9
Covered lines: 9
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def longestIncreasingSubsequence(numbers):
2: ✓     if not numbers:
3: ✓         return 0
4: ✓     dp = [1] * len(numbers)
5: ✓     for i in range(1, len(numbers)):
6: ✓         for j in range(i):
7: ✓             if numbers[i] > numbers[j]:
8: ✓                 dp[i] = max(dp[i], dp[j] + 1)
9: ✓     return max(dp)
```

## Complete Test File

```python
def longestIncreasingSubsequence(numbers):
    if not numbers:
        return 0
    dp = [1] * len(numbers)
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = longestIncreasingSubsequence([10, 22, 9, 33, 21, 50, 41, 60])
        assert result == 5, f"Test 1 failed: got {result}, expected {5}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = longestIncreasingSubsequence([3, 10, 2, 1, 20])
        assert result == 3, f"Test 2 failed: got {result}, expected {3}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = longestIncreasingSubsequence([50, 3, 10, 7, 40, 80])
        assert result == 4, f"Test 3 failed: got {result}, expected {4}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = longestIncreasingSubsequence([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == 1, f"Test 4 failed: got {result}, expected {1}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = longestIncreasingSubsequence([1, 2, 3, 4, 5])
        assert result == 5, f"Test 5 failed: got {result}, expected {5}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = longestIncreasingSubsequence([])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = longestIncreasingSubsequence([5])
        assert result == 1, f"Test 7 failed: got {result}, expected {1}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = longestIncreasingSubsequence([5, 5, 5, 5])
        assert result == 1, f"Test 8 failed: got {result}, expected {1}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = longestIncreasingSubsequence([0, -1, 2, -3, 4, -5, 6])
        assert result == 4, f"Test 9 failed: got {result}, expected {4}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = longestIncreasingSubsequence([7, 7, 1, 2, 2, 3, 3, 4])
        assert result == 4, f"Test 10 failed: got {result}, expected {4}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = longestIncreasingSubsequence([6, 5, 6, 5, 6, 5, 6])
        assert result == 2, f"Test 11 failed: got {result}, expected {2}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = longestIncreasingSubsequence([1, 5, 2, 2, 2, 3, 4])
        assert result == 4, f"Test 12 failed: got {result}, expected {4}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = longestIncreasingSubsequence([10, 22, 9, 33, 21, 50, -1, 0, 0])
        assert result == 4, f"Test 13 failed: got {result}, expected {4}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = longestIncreasingSubsequence([-10, 22, 9, 33, 21, 50, 41, 60, 8])
        assert result == 5, f"Test 14 failed: got {result}, expected {5}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = longestIncreasingSubsequence([10, 22, 9, 21, 50, 41])
        assert result == 3, f"Test 15 failed: got {result}, expected {3}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = longestIncreasingSubsequence([0, 20, 1, 2, 10, 3])
        assert result == 4, f"Test 16 failed: got {result}, expected {4}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = longestIncreasingSubsequence([3, 10, 1, 20])
        assert result == 3, f"Test 17 failed: got {result}, expected {3}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = longestIncreasingSubsequence([0, 20, 1, 15, 10, 2, 0])
        assert result == 3, f"Test 18 failed: got {result}, expected {3}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = longestIncreasingSubsequence([20, 1, 2, 11, 3])
        assert result == 3, f"Test 19 failed: got {result}, expected {3}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = longestIncreasingSubsequence([50, 3, 10, 7, 40, 80, 0])
        assert result == 4, f"Test 20 failed: got {result}, expected {4}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = longestIncreasingSubsequence([0, 40, 7, 10, 3, 50, 9223372036854775807, 98])
        assert result == 5, f"Test 21 failed: got {result}, expected {5}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = longestIncreasingSubsequence([-2, 80, 40, 7, 10, 3, 50])
        assert result == 4, f"Test 22 failed: got {result}, expected {4}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = longestIncreasingSubsequence([50, 3, 10, 40, 80])
        assert result == 4, f"Test 23 failed: got {result}, expected {4}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = longestIncreasingSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9])
        assert result == 10, f"Test 24 failed: got {result}, expected {10}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = longestIncreasingSubsequence([0, 1, 2, 3, 4, 0])
        assert result == 5, f"Test 25 failed: got {result}, expected {5}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = longestIncreasingSubsequence([1, 1, 3, 4, 5])
        assert result == 4, f"Test 26 failed: got {result}, expected {4}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = longestIncreasingSubsequence([1, 2, 3, 4, 5, 0])
        assert result == 5, f"Test 27 failed: got {result}, expected {5}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = longestIncreasingSubsequence([0, 5, 5, 5])
        assert result == 2, f"Test 28 failed: got {result}, expected {2}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = longestIncreasingSubsequence([0, 0, 0])
        assert result == 1, f"Test 29 failed: got {result}, expected {1}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = longestIncreasingSubsequence([1, 9223372036854775807, 80])
        assert result == 2, f"Test 30 failed: got {result}, expected {2}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = longestIncreasingSubsequence([-1, 8])
        assert result == 2, f"Test 31 failed: got {result}, expected {2}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = longestIncreasingSubsequence([-1, 40])
        assert result == 2, f"Test 32 failed: got {result}, expected {2}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = longestIncreasingSubsequence([1, 2, 3, 4, 5, 0, 97, 0, 0])
        assert result == 6, f"Test 33 failed: got {result}, expected {6}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = longestIncreasingSubsequence([5, 4, 3, 2, -1, 0, 20])
        assert result == 3, f"Test 34 failed: got {result}, expected {3}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = longestIncreasingSubsequence([2, 3, 4, 5, 0, 0])
        assert result == 4, f"Test 35 failed: got {result}, expected {4}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = longestIncreasingSubsequence([19, 0, 1, 2, 3, 4, 5])
        assert result == 6, f"Test 36 failed: got {result}, expected {6}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = longestIncreasingSubsequence([0, 0, 10])
        assert result == 2, f"Test 37 failed: got {result}, expected {2}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = longestIncreasingSubsequence([-1, -3, -4, 0])
        assert result == 2, f"Test 38 failed: got {result}, expected {2}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = longestIncreasingSubsequence([14, 4, -5, 3, 1, 50, 0])
        assert result == 3, f"Test 39 failed: got {result}, expected {3}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = longestIncreasingSubsequence([0, 4, 97, 4, 98, 99, 2, 1])
        assert result == 5, f"Test 40 failed: got {result}, expected {5}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = longestIncreasingSubsequence([8, 1, -3, 2, 5, 3, 4, 14, 100, 0])
        assert result == 6, f"Test 41 failed: got {result}, expected {6}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = longestIncreasingSubsequence([4, 3, 5, 2, 1, 0])
        assert result == 2, f"Test 42 failed: got {result}, expected {2}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = longestIncreasingSubsequence([5, 50, 123456789012345678901234567890, -3, 7, 3, 8, 4, 9])
        assert result == 4, f"Test 43 failed: got {result}, expected {4}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18, 0])
        assert result == 4, f"Test 44 failed: got {result}, expected {4}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = longestIncreasingSubsequence([0, 101, 11, 3, 5, 2, 9, 10])
        assert result == 5, f"Test 45 failed: got {result}, expected {5}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18, 0, 0, -8, 0, 100])
        assert result == 5, f"Test 46 failed: got {result}, expected {5}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = longestIncreasingSubsequence([9, 1, 15, 10, 10, 2, 12, 4, 8, 0, 101])
        assert result == 5, f"Test 47 failed: got {result}, expected {5}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = longestIncreasingSubsequence([9, 1, 6, 10, 2, 12, 4, 8, 0])
        assert result == 4, f"Test 48 failed: got {result}, expected {4}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = longestIncreasingSubsequence([-1000000000, 2, -999999999])
        assert result == 2, f"Test 49 failed: got {result}, expected {2}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = longestIncreasingSubsequence([2147483647, -2147483648, 2147483646, 16, 0])
        assert result == 2, f"Test 50 failed: got {result}, expected {2}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = longestIncreasingSubsequence([-2147483647, 2147483646, -4294967296, 2147483647, 0, 2, 0])
        assert result == 3, f"Test 51 failed: got {result}, expected {3}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = longestIncreasingSubsequence([-10, -10, -10, -9, -8, -9, -9223372036854775807])
        assert result == 3, f"Test 52 failed: got {result}, expected {3}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = longestIncreasingSubsequence([0, 4, 3, 2, 2, 6, 5, 1])
        assert result == 3, f"Test 53 failed: got {result}, expected {3}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = longestIncreasingSubsequence([41, 0, 5, 4, 0, -2, 2, 1, 7, 8, 9])
        assert result == 5, f"Test 54 failed: got {result}, expected {5}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = longestIncreasingSubsequence([1, 2, 3, 2, 3, 4, 0, 5])
        assert result == 5, f"Test 55 failed: got {result}, expected {5}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = longestIncreasingSubsequence([0, 5, 0, 4, 3, 2, 1, 3, 2, 0, 9223372036854775807])
        assert result == 4, f"Test 56 failed: got {result}, expected {4}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = longestIncreasingSubsequence([0, 22, 0, -123456789012345678901234567890, 123456789012345678901234567890])
        assert result == 3, f"Test 57 failed: got {result}, expected {3}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
