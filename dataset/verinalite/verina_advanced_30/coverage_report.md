# Coverage Report

Total executable lines: 11
Covered lines: 11
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def longestIncreasingStreak(nums):
2: ✓     if not nums:
3: ✓         return 0
4: ✓     max_streak = 1
5: ✓     current_streak = 1
6: ✓     for i in range(1, len(nums)):
7: ✓         if nums[i] > nums[i - 1]:
8: ✓             current_streak += 1
9:           else:
10: ✓             max_streak = max(max_streak, current_streak)
11: ✓             current_streak = 1
12: ✓     return max(max_streak, current_streak)
```

## Complete Test File

```python
def longestIncreasingStreak(nums):
    if not nums:
        return 0
    max_streak = 1
    current_streak = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 1
    return max(max_streak, current_streak)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = longestIncreasingStreak([1, 2, 3, 2, 4, 5, 6])
        assert result == 4, f"Test 1 failed: got {result}, expected {4}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = longestIncreasingStreak([10, 20, 30, 40])
        assert result == 4, f"Test 2 failed: got {result}, expected {4}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = longestIncreasingStreak([5, 5, 5, 5])
        assert result == 1, f"Test 3 failed: got {result}, expected {1}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = longestIncreasingStreak([10, 9, 8, 7])
        assert result == 1, f"Test 4 failed: got {result}, expected {1}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = longestIncreasingStreak([])
        assert result == 0, f"Test 5 failed: got {result}, expected {0}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = longestIncreasingStreak([1, 2, 1, 2, 3, 0, 1, 2, 3, 4])
        assert result == 5, f"Test 6 failed: got {result}, expected {5}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = longestIncreasingStreak([2, 2, 2, 3, 4, 5, 1, 2, 3])
        assert result == 4, f"Test 7 failed: got {result}, expected {4}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = longestIncreasingStreak([9, 1, 2, 3, 0, 1, 2, 3, 4])
        assert result == 5, f"Test 8 failed: got {result}, expected {5}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = longestIncreasingStreak([1, 2, 1, 2, 1, 2, 1, 2])
        assert result == 2, f"Test 9 failed: got {result}, expected {2}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = longestIncreasingStreak([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        assert result == 10, f"Test 10 failed: got {result}, expected {10}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = longestIncreasingStreak([14, 13, 12, 11, 10, 9, 8, 7, 6, 5])
        assert result == 1, f"Test 11 failed: got {result}, expected {1}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = longestIncreasingStreak([8, 8, 9, 10, 10, 11, 12, 12, 13])
        assert result == 3, f"Test 12 failed: got {result}, expected {3}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = longestIncreasingStreak([1, 3, 2, 4, 5, 6])
        assert result == 4, f"Test 13 failed: got {result}, expected {4}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = longestIncreasingStreak([10, 20, 30])
        assert result == 3, f"Test 14 failed: got {result}, expected {3}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = longestIncreasingStreak([5, 5, 5, 0, 21, 0])
        assert result == 2, f"Test 15 failed: got {result}, expected {2}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = longestIncreasingStreak([10, 5, 5, 5, 0, 0])
        assert result == 1, f"Test 16 failed: got {result}, expected {1}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = longestIncreasingStreak([2147483645, 3, 7, 8, -9, 10, 0])
        assert result == 3, f"Test 17 failed: got {result}, expected {3}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = longestIncreasingStreak([4, 3, 2, 0, 3, 2, 1, 2, 1])
        assert result == 2, f"Test 18 failed: got {result}, expected {2}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = longestIncreasingStreak([1, 2, 1, 2, 3, 0, 1, 2, 3, 4, 0, 998])
        assert result == 5, f"Test 19 failed: got {result}, expected {5}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = longestIncreasingStreak([4, 2, 1, 0, 3, 2, 2, 1])
        assert result == 2, f"Test 20 failed: got {result}, expected {2}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = longestIncreasingStreak([0, -2147483646, 27])
        assert result == 2, f"Test 21 failed: got {result}, expected {2}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = longestIncreasingStreak([0, 20, 0, 4, 3, 2, 1])
        assert result == 2, f"Test 22 failed: got {result}, expected {2}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = longestIncreasingStreak([1, 2, 3, 2, 3, 4, 0, 2, 0])
        assert result == 3, f"Test 23 failed: got {result}, expected {3}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = longestIncreasingStreak([1, 2, 3, 2, 3, 4, 1, 2, 18, 101])
        assert result == 4, f"Test 24 failed: got {result}, expected {4}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = longestIncreasingStreak([10, 21, 30, 40, -40])
        assert result == 4, f"Test 25 failed: got {result}, expected {4}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = longestIncreasingStreak([10, -4, 8, 7])
        assert result == 2, f"Test 26 failed: got {result}, expected {2}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = longestIncreasingStreak([1, 1, 2, 0, 3, 3, 4, -8, 0, 50, 0])
        assert result == 3, f"Test 27 failed: got {result}, expected {3}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = longestIncreasingStreak([2, 2, 3, 3, 4, 4, 0, 0])
        assert result == 2, f"Test 28 failed: got {result}, expected {2}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = longestIncreasingStreak([1, 1, 0, 2, 3, 2, 4, 4, 0])
        assert result == 3, f"Test 29 failed: got {result}, expected {3}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = longestIncreasingStreak([-5, -4, -3, -2, -1, 22])
        assert result == 6, f"Test 30 failed: got {result}, expected {6}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = longestIncreasingStreak([-5, -4, -3, -2, -1, 0])
        assert result == 6, f"Test 31 failed: got {result}, expected {6}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = longestIncreasingStreak([0, 16, -1000000000, -4, 30, -2, -1])
        assert result == 3, f"Test 32 failed: got {result}, expected {3}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = longestIncreasingStreak([24, -6, -2, -1, 0])
        assert result == 4, f"Test 33 failed: got {result}, expected {4}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = longestIncreasingStreak([0, -1, 0, 1, 2, 0, 1, 0, 0, 0, 0])
        assert result == 4, f"Test 34 failed: got {result}, expected {4}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = longestIncreasingStreak([0, -1, 0, 1, 2, -1, 0, 1, -6])
        assert result == 4, f"Test 35 failed: got {result}, expected {4}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = longestIncreasingStreak([100, 101, 102, 50, 51, 52, 53, 10, 102])
        assert result == 4, f"Test 36 failed: got {result}, expected {4}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = longestIncreasingStreak([-2147483647, -5, 4, 3, 2, 1, 0, 4, 4, 2, 1, 3])
        assert result == 3, f"Test 37 failed: got {result}, expected {3}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = longestIncreasingStreak([0, 4, 3, 2, 1, 0, 4, 3, -2, 2, 3])
        assert result == 3, f"Test 38 failed: got {result}, expected {3}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = longestIncreasingStreak([1, 3, 5, 7, 9, 102, -8, 6, 8, 10])
        assert result == 6, f"Test 39 failed: got {result}, expected {6}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = longestIncreasingStreak([16, 2, 4, 5, 1, 2, 3, 0])
        assert result == 3, f"Test 40 failed: got {result}, expected {3}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = longestIncreasingStreak([9, 1, 2, 3, 0, 1, 2, 3, 4, 0, 12])
        assert result == 5, f"Test 41 failed: got {result}, expected {5}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = longestIncreasingStreak([0, 2, 1, 2, 1, 2, 1, 2, 1, 0, 0])
        assert result == 2, f"Test 42 failed: got {result}, expected {2}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = longestIncreasingStreak([5, 6, 7, 1000000000, 9, 10, 11, 12, 13, 14, 13])
        assert result == 6, f"Test 43 failed: got {result}, expected {6}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = longestIncreasingStreak([-10, 0, 10, 20, -5, -4, -3, -2, -1, 0, 0, 0])
        assert result == 6, f"Test 44 failed: got {result}, expected {6}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = longestIncreasingStreak([-10, 0, 20, -4, -3, -2, -1, 0, 0, 999999999])
        assert result == 5, f"Test 45 failed: got {result}, expected {5}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = longestIncreasingStreak([5, -4, 4, -3, 3, -2, 2, -1, 1])
        assert result == 2, f"Test 46 failed: got {result}, expected {2}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = longestIncreasingStreak([-999999998, -3, -6, -12, -25, -50, -100, 0])
        assert result == 2, f"Test 47 failed: got {result}, expected {2}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = longestIncreasingStreak([8, 9, 10, 20, 11, 12, 12, 13, 41])
        assert result == 4, f"Test 48 failed: got {result}, expected {4}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = longestIncreasingStreak([12, 12, 11, 10, 10, 9, 8, 8, 0, 1001])
        assert result == 2, f"Test 49 failed: got {result}, expected {2}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = longestIncreasingStreak([0, 23, 1000, 999, 998, 1002, 2002, 1000, 999, 1000, 2])
        assert result == 3, f"Test 50 failed: got {result}, expected {3}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = longestIncreasingStreak([2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8])
        assert result == 8, f"Test 51 failed: got {result}, expected {8}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = longestIncreasingStreak([0, 8, 7, 6, 5, 4, 3, 2, 1, 6, 5, -4, 3, 2])
        assert result == 2, f"Test 52 failed: got {result}, expected {2}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = longestIncreasingStreak([2, -999999998, -999999999, -1000000000, 11, 24])
        assert result == 3, f"Test 53 failed: got {result}, expected {3}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = longestIncreasingStreak([8, 7, 7, 6, 5, 4, 4, 3, 2, 1, 1, 1, 2147483644, 100, -999999998])
        assert result == 2, f"Test 54 failed: got {result}, expected {2}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = longestIncreasingStreak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 0, 30, 0])
        assert result == 26, f"Test 55 failed: got {result}, expected {26}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = longestIncreasingStreak([30, 29, 28, 27, 26, 24, 23, 22, 21, 20, 19, 18, 17, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -2])
        assert result == 1, f"Test 56 failed: got {result}, expected {1}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
