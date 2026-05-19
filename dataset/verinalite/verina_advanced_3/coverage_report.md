# Coverage Report

Total executable lines: 9
Covered lines: 9
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def LongestCommonSubsequence(a, b):
2: ✓     m, n = len(a), len(b)
3: ✓     dp = [[0] * (n + 1) for _ in range(m + 1)]
4: ✓     for i in range(1, m + 1):
5: ✓         for j in range(1, n + 1):
6: ✓             if a[i - 1] == b[j - 1]:
7: ✓                 dp[i][j] = dp[i - 1][j - 1] + 1
8:               else:
9: ✓                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
10: ✓     return dp[m][n]
```

## Complete Test File

```python
def LongestCommonSubsequence(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = LongestCommonSubsequence([1, 2, 3], [1, 2, 3])
        assert result == 3, f"Test 1 failed: got {result}, expected {3}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = LongestCommonSubsequence([1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7])
        assert result == 4, f"Test 2 failed: got {result}, expected {4}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = LongestCommonSubsequence([1, 2, 3], [4, 5, 6])
        assert result == 0, f"Test 3 failed: got {result}, expected {0}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = LongestCommonSubsequence([], [1, 2, 3])
        assert result == 0, f"Test 4 failed: got {result}, expected {0}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = LongestCommonSubsequence([1, 2, 3, 4], [2, 4, 6, 8])
        assert result == 2, f"Test 5 failed: got {result}, expected {2}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = LongestCommonSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10])
        assert result == 5, f"Test 6 failed: got {result}, expected {5}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = LongestCommonSubsequence([7, 8, 1, 2, 3, 9], [1, 2, 3])
        assert result == 3, f"Test 7 failed: got {result}, expected {3}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = LongestCommonSubsequence([-1, 0, -1, 0, -1], [0, -1, 0, -1, 0])
        assert result == 4, f"Test 8 failed: got {result}, expected {4}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = LongestCommonSubsequence([-10, -20, -30, -40], [-40, -30, -20, -10])
        assert result == 1, f"Test 9 failed: got {result}, expected {1}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = LongestCommonSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == 1, f"Test 10 failed: got {result}, expected {1}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = LongestCommonSubsequence([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 2, 4, 6, 8])
        assert result == 1, f"Test 11 failed: got {result}, expected {1}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = LongestCommonSubsequence([11, 22, 33, 44, 55, 66, 77, 88, 99], [99, 88, 77, 66, 55, 44, 33, 22, 11])
        assert result == 1, f"Test 12 failed: got {result}, expected {1}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = LongestCommonSubsequence([1, 2, 3], [4, 2, 3, 0, 0])
        assert result == 2, f"Test 13 failed: got {result}, expected {2}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = LongestCommonSubsequence([0, 2, 3, 4, 5, 0], [5, 4, 3, 2, 1, 5])
        assert result == 2, f"Test 14 failed: got {result}, expected {2}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = LongestCommonSubsequence([5, 4, 3, 2, 1, -1], [4, 3, 2, 1, 0])
        assert result == 4, f"Test 15 failed: got {result}, expected {4}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = LongestCommonSubsequence([5, 1, 0, -1, -5], [-5, -1, 5])
        assert result == 1, f"Test 16 failed: got {result}, expected {1}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = LongestCommonSubsequence([2, 2, 2, 3, 3], [2, 3, 3, 2, -40])
        assert result == 3, f"Test 17 failed: got {result}, expected {3}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = LongestCommonSubsequence([2147483647, -2147483648, 0], [-2147483648, -9223372036854775809, 0])
        assert result == 2, f"Test 18 failed: got {result}, expected {2}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = LongestCommonSubsequence([0, -9223372036854775808, 300], [1])
        assert result == 0, f"Test 19 failed: got {result}, expected {0}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = LongestCommonSubsequence([0, 1, 0, 1, 0, 1], [2147483647, 1, 0, 1, 0, 1])
        assert result == 5, f"Test 20 failed: got {result}, expected {5}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = LongestCommonSubsequence([0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, -24])
        assert result == 5, f"Test 21 failed: got {result}, expected {5}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = LongestCommonSubsequence([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [55, 6, 4, 2])
        assert result == 3, f"Test 22 failed: got {result}, expected {3}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = LongestCommonSubsequence([2, 4, 6, 8, 10, 0, 43], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert result == 5, f"Test 23 failed: got {result}, expected {5}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = LongestCommonSubsequence([2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 7, 8, 9, 10])
        assert result == 4, f"Test 24 failed: got {result}, expected {4}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = LongestCommonSubsequence([2, 4, 6, 8, 10], [1, 2, 3, 700, 5, 6, 7, 8, 9, 10])
        assert result == 4, f"Test 25 failed: got {result}, expected {4}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = LongestCommonSubsequence([1, 4, 2, 5, 3, 6, 0], [2, 4, 5, 6])
        assert result == 3, f"Test 26 failed: got {result}, expected {3}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = LongestCommonSubsequence([1, 4, 4, 5, 3, 6], [1, 1, 3, 4, 5, 6])
        assert result == 4, f"Test 27 failed: got {result}, expected {4}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = LongestCommonSubsequence([-5, 0, 0, 0], [0, -2, 0, 0])
        assert result == 3, f"Test 28 failed: got {result}, expected {3}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = LongestCommonSubsequence([0, 11, 0, -40, -9223372036854775809], [0, 0, -2, 0])
        assert result == 2, f"Test 29 failed: got {result}, expected {2}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = LongestCommonSubsequence([0, -1, 0, 55, 12], [0, -1, 0, -1, 0])
        assert result == 3, f"Test 30 failed: got {result}, expected {3}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = LongestCommonSubsequence([-1, 0, 0, -1], [20, 0, -1, 0, -1, 0, 2147483647])
        assert result == 3, f"Test 31 failed: got {result}, expected {3}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = LongestCommonSubsequence([-1, 0, -1, 0, -1], [0, -1, 0, 0, 0, 0])
        assert result == 3, f"Test 32 failed: got {result}, expected {3}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = LongestCommonSubsequence([5, 6, 7, 14], [5, 6, 7, 16, 9, 10])
        assert result == 3, f"Test 33 failed: got {result}, expected {3}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = LongestCommonSubsequence([5, 6, 7], [5, 12, 7, 9, 0])
        assert result == 2, f"Test 34 failed: got {result}, expected {2}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = LongestCommonSubsequence([5, 6, 7, 8, 9], [5, 200, 6, -4])
        assert result == 2, f"Test 35 failed: got {result}, expected {2}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = LongestCommonSubsequence([5, 6, 7, 8, 9], [7, 6, 5, -20, 0, 0])
        assert result == 1, f"Test 36 failed: got {result}, expected {1}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = LongestCommonSubsequence([9, 8, 7, 6, 5, 0], [7, 6, 5])
        assert result == 3, f"Test 37 failed: got {result}, expected {3}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = LongestCommonSubsequence([-1, 2, 1, 2, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2])
        assert result == 6, f"Test 38 failed: got {result}, expected {6}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = LongestCommonSubsequence([123456789012345678901234567890, 2, 1, 2, 3, 2, 1, 2], [1, 2, 1, 2, -1, 2, 1, 2, 0])
        assert result == 6, f"Test 39 failed: got {result}, expected {6}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = LongestCommonSubsequence([0, 1, 2, 1, 2, 1, 2, 2, 0], [2, 1, 2, 1, 2, 1, 2, 1])
        assert result == 6, f"Test 40 failed: got {result}, expected {6}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = LongestCommonSubsequence([1, 2, 3, 2, 4, 1, 2, 18, 0], [2, 4, 1, 2, 1, 0, 0])
        assert result == 5, f"Test 41 failed: got {result}, expected {5}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = LongestCommonSubsequence([1, 1, 3, 2, 4, 1, 2], [2, 4, 3, 1, 2, 1, 0])
        assert result == 4, f"Test 42 failed: got {result}, expected {4}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = LongestCommonSubsequence([1, 2, 3, 2, 4, 1, 2, 0], [2, 4, 1, 2, 1, 0])
        assert result == 5, f"Test 43 failed: got {result}, expected {5}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = LongestCommonSubsequence([10, 21, 30, 40, 50, 0], [15, 25, 35, 45, 55, 0])
        assert result == 1, f"Test 44 failed: got {result}, expected {1}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = LongestCommonSubsequence([-40, -30, -20, 500, 0], [-40, -30, -20, -10, 10])
        assert result == 3, f"Test 45 failed: got {result}, expected {3}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = LongestCommonSubsequence([100, 200, 300, 400], [100, 300, 500, 700, 900, 0, 123456789012345678901234567890])
        assert result == 2, f"Test 46 failed: got {result}, expected {2}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = LongestCommonSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -11, 14, 15, 16, 17, 18, 19, 20, -20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        assert result == 19, f"Test 47 failed: got {result}, expected {19}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = LongestCommonSubsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 0], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == 1, f"Test 48 failed: got {result}, expected {1}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = LongestCommonSubsequence([1, 3, 4, 5, 6, 7, 8, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 42], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == 2, f"Test 49 failed: got {result}, expected {2}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = LongestCommonSubsequence([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
        assert result == 13, f"Test 50 failed: got {result}, expected {13}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = LongestCommonSubsequence([9, 8, 7, 6, 5, 4, 3, 2, 0, 6, -123456789012345678901234567890], [0, 2, 4, 6, 8])
        assert result == 2, f"Test 51 failed: got {result}, expected {2}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = LongestCommonSubsequence([6, 5, 4, 3, 2, 1], [1, 3, 5, 0])
        assert result == 1, f"Test 52 failed: got {result}, expected {1}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = LongestCommonSubsequence([2, 7, 2, 7, 2, 7, 2, 7, 2], [0, 0, 7, 2, 7, 2, 7, 2, 7])
        assert result == 7, f"Test 53 failed: got {result}, expected {7}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = LongestCommonSubsequence([11, 22, 33, 44, 55, 66, -1, 88, 99], [11, -10, 33, 44, 55, 66, 77, 88, 99])
        assert result == 7, f"Test 54 failed: got {result}, expected {7}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = LongestCommonSubsequence([11, 22, 33, 44, 55, 66, 77, 88, 99], [99, 88, 77, 66, 55, 44, 33, 22, 11, 14])
        assert result == 1, f"Test 55 failed: got {result}, expected {1}"
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
