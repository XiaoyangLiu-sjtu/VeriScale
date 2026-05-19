# Coverage Report

Total executable lines: 13
Covered lines: 13
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def lengthOfLIS(nums):
2: ✓     tails = []
3: ✓     for num in nums:
4: ✓         left, right = 0, len(tails)
5: ✓         while left < right:
6: ✓             mid = (left + right) // 2
7: ✓             if tails[mid] < num:
8: ✓                 left = mid + 1
9:               else:
10: ✓                 right = mid
11: ✓         if left == len(tails):
12: ✓             tails.append(num)
13:           else:
14: ✓             tails[left] = num
15: ✓     return len(tails)
```

## Complete Test File

```python
def lengthOfLIS(nums):
    tails = []
    for num in nums:
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    return len(tails)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
        assert result == 4, f"Test 1 failed: got {result}, expected {4}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = lengthOfLIS([0, 1, 0, 3, 2, 3])
        assert result == 4, f"Test 2 failed: got {result}, expected {4}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
        assert result == 1, f"Test 3 failed: got {result}, expected {1}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = lengthOfLIS([])
        assert result == 0, f"Test 4 failed: got {result}, expected {0}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = lengthOfLIS([4, 10, 4, 3, 8, 9])
        assert result == 3, f"Test 5 failed: got {result}, expected {3}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])
        assert result == 6, f"Test 6 failed: got {result}, expected {6}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = lengthOfLIS([10, 22, 9, 33, 21, 50, 41, 60, 80])
        assert result == 6, f"Test 7 failed: got {result}, expected {6}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
        assert result == 6, f"Test 8 failed: got {result}, expected {6}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = lengthOfLIS([-2, -1])
        assert result == 2, f"Test 9 failed: got {result}, expected {2}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = lengthOfLIS([2, 5, 3, 7, 11, 8, 10, 13, 6])
        assert result == 6, f"Test 10 failed: got {result}, expected {6}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = lengthOfLIS([4, 2, 4, 5, 3, 7])
        assert result == 4, f"Test 11 failed: got {result}, expected {4}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = lengthOfLIS([10, 20, 10, 30, 20, 50])
        assert result == 4, f"Test 12 failed: got {result}, expected {4}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = lengthOfLIS([10, 9, 2, 3, 7, 101, 18])
        assert result == 4, f"Test 13 failed: got {result}, expected {4}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = lengthOfLIS([10, 9, 4, 5, 3, 7, 101, 18, 0, 0, -999999999, 13])
        assert result == 4, f"Test 14 failed: got {result}, expected {4}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = lengthOfLIS([10, 9, 2, 5, 3, 7, -2147483647, 0, 0])
        assert result == 3, f"Test 15 failed: got {result}, expected {3}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = lengthOfLIS([10, 9, 5, 3, 7, 101, 18])
        assert result == 3, f"Test 16 failed: got {result}, expected {3}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = lengthOfLIS([10, 9, 2, 5, 0, 7, 101, 18, -1, 0])
        assert result == 4, f"Test 17 failed: got {result}, expected {4}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = lengthOfLIS([0, 9, 8, 3, 15, 10, 4])
        assert result == 3, f"Test 18 failed: got {result}, expected {3}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 11, 5, 13, 3, 11, 7, 15, -1, 0, -1, 5])
        assert result == 6, f"Test 19 failed: got {result}, expected {6}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = lengthOfLIS([0, 0, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
        assert result == 6, f"Test 20 failed: got {result}, expected {6}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15, 80])
        assert result == 7, f"Test 21 failed: got {result}, expected {7}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = lengthOfLIS([15, 7, 11, 3, 13, 5, 9, 1, 14, 6, 10, 2, 12, 4, 8, 0, 0])
        assert result == 5, f"Test 22 failed: got {result}, expected {5}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = lengthOfLIS([15, 7, 11, 3, 13, 5, 9, 1, 14, 6, 10, 2, 12, 4, 8, 0])
        assert result == 5, f"Test 23 failed: got {result}, expected {5}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = lengthOfLIS([0, 999999999, 3, 4, 5, 0])
        assert result == 4, f"Test 24 failed: got {result}, expected {4}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = lengthOfLIS([7, 7, 7, 7, 60])
        assert result == 2, f"Test 25 failed: got {result}, expected {2}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = lengthOfLIS([0, 1, 4, 2, 2])
        assert result == 3, f"Test 26 failed: got {result}, expected {3}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = lengthOfLIS([-4, -3, -1, 0, 0])
        assert result == 4, f"Test 27 failed: got {result}, expected {4}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = lengthOfLIS([0, -1999999998, 6, 4, 5, 3, 4, 2, 8, 1])
        assert result == 4, f"Test 28 failed: got {result}, expected {4}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = lengthOfLIS([9, 1, 8, 2, 7, 5, 0, 4, 5])
        assert result == 4, f"Test 29 failed: got {result}, expected {4}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = lengthOfLIS([8, 1, -1999999997, 2, 5, 3, 4])
        assert result == 4, f"Test 30 failed: got {result}, expected {4}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = lengthOfLIS([0, 4, 3, 5, 2, 6, 1, 8])
        assert result == 5, f"Test 31 failed: got {result}, expected {5}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = lengthOfLIS([8, 1, 6, 2, 5, 3, 4, 0])
        assert result == 4, f"Test 32 failed: got {result}, expected {4}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = lengthOfLIS([1, 1, 1, 2, 2, 2, 3, 3, 3, 0, 0, -2147483648])
        assert result == 3, f"Test 33 failed: got {result}, expected {3}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = lengthOfLIS([2, 3, 2, 2, 1, 1, 1000000000])
        assert result == 3, f"Test 34 failed: got {result}, expected {3}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = lengthOfLIS([5, 4, 5, 3, 5, 2, 5, 1, 5])
        assert result == 2, f"Test 35 failed: got {result}, expected {2}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = lengthOfLIS([100, 14, 4, 0, 3, 5, 2, 5, 1, 5])
        assert result == 3, f"Test 36 failed: got {result}, expected {3}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = lengthOfLIS([1, 5, 2, 6, 3, 7, 4, 9])
        assert result == 5, f"Test 37 failed: got {result}, expected {5}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = lengthOfLIS([8, 5, -2, 3, 6, 2, 5, 1, -1999999998])
        assert result == 3, f"Test 38 failed: got {result}, expected {3}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = lengthOfLIS([50, 3, 10, 7, 40, 80, 0, 0, 67, 0])
        assert result == 4, f"Test 39 failed: got {result}, expected {4}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = lengthOfLIS([-7, 2, 5, 1, 7, 8, 3])
        assert result == 5, f"Test 40 failed: got {result}, expected {5}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = lengthOfLIS([1, 4, 2, 3, 9, 0, 0])
        assert result == 4, f"Test 41 failed: got {result}, expected {4}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = lengthOfLIS([2, 4, 3, 3, -10])
        assert result == 2, f"Test 42 failed: got {result}, expected {2}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = lengthOfLIS([6, 13, 10, 8, 11, 7, 5])
        assert result == 3, f"Test 43 failed: got {result}, expected {3}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = lengthOfLIS([4, 2, 4, 5, 3, 7, -6])
        assert result == 4, f"Test 44 failed: got {result}, expected {4}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = lengthOfLIS([0, 4, 3, 2, 2, 1, 2, 2, 0, 12])
        assert result == 4, f"Test 45 failed: got {result}, expected {4}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = lengthOfLIS([9, 0, 7, 1, 2, 4, 5, 0])
        assert result == 5, f"Test 46 failed: got {result}, expected {5}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = lengthOfLIS([5, 4, 0, 3, 2, 1, 7, 8, 9, 204])
        assert result == 6, f"Test 47 failed: got {result}, expected {6}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = lengthOfLIS([3, 10, 2, 20, 0, 0])
        assert result == 3, f"Test 48 failed: got {result}, expected {3}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = lengthOfLIS([-999999998, 20, 1, 2, 10, 3])
        assert result == 4, f"Test 49 failed: got {result}, expected {4}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = lengthOfLIS([8, -7, 6, -5, 4, -3, 2, -1, 0, 0])
        assert result == 5, f"Test 50 failed: got {result}, expected {5}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = lengthOfLIS([0, -1, 2, -8, -5, 6, -7, 8, 0])
        assert result == 4, f"Test 51 failed: got {result}, expected {4}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = lengthOfLIS([8, -7, 16, -5, 4, -3, 60, -1, 0, 0])
        assert result == 5, f"Test 52 failed: got {result}, expected {5}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
