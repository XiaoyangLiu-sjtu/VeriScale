# Coverage Report

Total executable lines: 7
Covered lines: 7
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def twoSum(nums, target):
2: ✓     seen = {}
3: ✓     for i, num in enumerate(nums):
4: ✓         complement = target - num
5: ✓         if complement in seen:
6: ✓             return sorted([seen[complement], i])
7: ✓         seen[num] = i
```

## Complete Test File

```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return sorted([seen[complement], i])
        seen[num] = i

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = twoSum([2, 7, 11, 15], 9)
        assert result == [0, 1], f"Test 1 failed: got {result}, expected {[0, 1]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = twoSum([3, 2, 4], 6)
        assert result == [1, 2], f"Test 2 failed: got {result}, expected {[1, 2]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = twoSum([3, 3], 6)
        assert result == [0, 1], f"Test 3 failed: got {result}, expected {[0, 1]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = twoSum([1, 2, 3, 4, 5], 9)
        assert result == [3, 4], f"Test 4 failed: got {result}, expected {[3, 4]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = twoSum([0, 4, 3, 0], 0)
        assert result == [0, 3], f"Test 5 failed: got {result}, expected {[0, 3]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = twoSum([1, 2], 3)
        assert result == [0, 1], f"Test 6 failed: got {result}, expected {[0, 1]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = twoSum([-1, 4], 3)
        assert result == [0, 1], f"Test 7 failed: got {result}, expected {[0, 1]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = twoSum([0, 0], 0)
        assert result == [0, 1], f"Test 8 failed: got {result}, expected {[0, 1]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = twoSum([5, -2, 9], 7)
        assert result == [1, 2], f"Test 9 failed: got {result}, expected {[1, 2]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = twoSum([-3, 1, 4, 2], -2)
        assert result == [0, 1], f"Test 10 failed: got {result}, expected {[0, 1]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = twoSum([10, -10, 20, 30], 10)
        assert result == [1, 2], f"Test 11 failed: got {result}, expected {[1, 2]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = twoSum([8, 1, 6, 14], 9)
        assert result == [0, 1], f"Test 12 failed: got {result}, expected {[0, 1]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = twoSum([-5, -2, -3, -8], -10)
        assert result == [1, 3], f"Test 13 failed: got {result}, expected {[1, 3]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = twoSum([1000000, -999999, 5], 1)
        assert result == [0, 1], f"Test 14 failed: got {result}, expected {[0, 1]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = twoSum([7, 14, 21, 28, 35], 56)
        assert result == [2, 4], f"Test 15 failed: got {result}, expected {[2, 4]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = twoSum([-10, 0, 10, 5], -5)
        assert result == [0, 3], f"Test 16 failed: got {result}, expected {[0, 3]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = twoSum([2, 2, 3, 9], 4)
        assert result == [0, 1], f"Test 17 failed: got {result}, expected {[0, 1]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = twoSum([6, 6, 1, 13], 12)
        assert result == [0, 1], f"Test 18 failed: got {result}, expected {[0, 1]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = twoSum([-1, -1, 2, 5], -2)
        assert result == [0, 1], f"Test 19 failed: got {result}, expected {[0, 1]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = twoSum([9, -4, 13, 0, 5], 18)
        assert result == [2, 4], f"Test 20 failed: got {result}, expected {[2, 4]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = twoSum([-7, 3, 11, -2, 6], 1)
        assert result == [1, 3], f"Test 21 failed: got {result}, expected {[1, 3]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = twoSum([0, 1, 2, 3, 4], 1)
        assert result == [0, 1], f"Test 22 failed: got {result}, expected {[0, 1]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = twoSum([0, 1, 2, 3, 4], 7)
        assert result == [3, 4], f"Test 23 failed: got {result}, expected {[3, 4]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = twoSum([-100, 50, 49, 1], -50)
        assert result == [0, 1], f"Test 24 failed: got {result}, expected {[0, 1]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = twoSum([-100, 50, 49, 1], 50)
        assert result == [2, 3], f"Test 25 failed: got {result}, expected {[2, 3]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = twoSum([12, -5, 7, -1, 20], 6)
        assert result == [2, 3], f"Test 26 failed: got {result}, expected {[2, 3]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = twoSum([2147483647, -2147483648, 1, 0], -1)
        assert result == [0, 1], f"Test 27 failed: got {result}, expected {[0, 1]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = twoSum([-2147483648, -1, 2147483647], -1)
        assert result == [0, 2], f"Test 28 failed: got {result}, expected {[0, 2]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = twoSum([5, 1, 5], 10)
        assert result == [0, 2], f"Test 29 failed: got {result}, expected {[0, 2]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = twoSum([8, -3, 4, 9, -1], 6)
        assert result == [1, 3], f"Test 30 failed: got {result}, expected {[1, 3]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = twoSum([2, 9, 11, -7, 4], 4)
        assert result == [2, 3], f"Test 31 failed: got {result}, expected {[2, 3]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = twoSum([30, 10, -20, 5, 15], 20)
        assert result == [3, 4], f"Test 32 failed: got {result}, expected {[3, 4]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = twoSum([2, 7, 11, 15, 21], 9)
        assert result == [0, 1], f"Test 33 failed: got {result}, expected {[0, 1]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = twoSum([2, 7, 11, 2147483647], 9)
        assert result == [0, 1], f"Test 34 failed: got {result}, expected {[0, 1]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = twoSum([2, 7, 0], 9)
        assert result == [0, 1], f"Test 35 failed: got {result}, expected {[0, 1]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = twoSum([2, 15, 4], 6)
        assert result == [0, 2], f"Test 36 failed: got {result}, expected {[0, 2]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = twoSum([2, 4, 0], 6)
        assert result == [0, 1], f"Test 37 failed: got {result}, expected {[0, 1]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = twoSum([3, 2, 4], 7)
        assert result == [0, 2], f"Test 38 failed: got {result}, expected {[0, 2]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = twoSum([0, 0, 0, 49, 4, 2, 3], 6)
        assert result == [4, 5], f"Test 39 failed: got {result}, expected {[4, 5]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = twoSum([3, 2, 4, 0], 6)
        assert result == [1, 2], f"Test 40 failed: got {result}, expected {[1, 2]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = twoSum([4, 2, 3, 0], 5)
        assert result == [1, 2], f"Test 41 failed: got {result}, expected {[1, 2]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = twoSum([1, 3, 5, 9], 10)
        assert result == [0, 3], f"Test 42 failed: got {result}, expected {[0, 3]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = twoSum([1, 1, 3, 4, 5], 9)
        assert result == [3, 4], f"Test 43 failed: got {result}, expected {[3, 4]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = twoSum([1, 2, 3, 4, 5], 8)
        assert result == [2, 4], f"Test 44 failed: got {result}, expected {[2, 4]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = twoSum([0, 4, 3, 0, 98], 0)
        assert result == [0, 3], f"Test 45 failed: got {result}, expected {[0, 3]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = twoSum([16, 0, 3, 4, 0], 0)
        assert result == [1, 4], f"Test 46 failed: got {result}, expected {[1, 4]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = twoSum([-1, 0, 2, 1], 2)
        assert result == [1, 2], f"Test 47 failed: got {result}, expected {[1, 2]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = twoSum([2, 1], 3)
        assert result == [0, 1], f"Test 48 failed: got {result}, expected {[0, 1]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = twoSum([1, 2, -9], 3)
        assert result == [0, 1], f"Test 49 failed: got {result}, expected {[0, 1]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = twoSum([4, -1], 3)
        assert result == [0, 1], f"Test 50 failed: got {result}, expected {[0, 1]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = twoSum([-3, 1, 2], -2)
        assert result == [0, 1], f"Test 51 failed: got {result}, expected {[0, 1]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = twoSum([2, 4, 1, -3, 0], -1)
        assert result == [0, 3], f"Test 52 failed: got {result}, expected {[0, 3]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = twoSum([2, 4, 1, -3], -2)
        assert result == [2, 3], f"Test 53 failed: got {result}, expected {[2, 3]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = twoSum([0, 2, 4, 1, -3, 0], 0)
        assert result == [0, 5], f"Test 54 failed: got {result}, expected {[0, 5]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = twoSum([10, -10, 19, 30, 0, -101], 0)
        assert result == [0, 1], f"Test 55 failed: got {result}, expected {[0, 1]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = twoSum([10, -10, 20, 30, 10, 48], 10)
        assert result == [1, 2], f"Test 56 failed: got {result}, expected {[1, 2]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = twoSum([10, 20, 30, 0], 20)
        assert result == [1, 3], f"Test 57 failed: got {result}, expected {[1, 3]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = twoSum([11, -10, 20, 30], 10)
        assert result == [1, 2], f"Test 58 failed: got {result}, expected {[1, 2]}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = twoSum([10, -10, 20, 30, 21], 0)
        assert result == [0, 1], f"Test 59 failed: got {result}, expected {[0, 1]}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = twoSum([30, 20, -10, 10], 10)
        assert result == [1, 2], f"Test 60 failed: got {result}, expected {[1, 2]}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = twoSum([30, 20, -10, 10], 0)
        assert result == [2, 3], f"Test 61 failed: got {result}, expected {[2, 3]}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = twoSum([14, 6, 1, 8], 20)
        assert result == [0, 1], f"Test 62 failed: got {result}, expected {[0, 1]}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = twoSum([14, 1, 8, 0], 8)
        assert result == [2, 3], f"Test 63 failed: got {result}, expected {[2, 3]}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = twoSum([8, 1, 6, 14, 0], 9)
        assert result == [0, 1], f"Test 64 failed: got {result}, expected {[0, 1]}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = twoSum([3, 3, 14, 6, 1, 8, 0], 8)
        assert result == [5, 6], f"Test 65 failed: got {result}, expected {[5, 6]}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = twoSum([-5, -2, -3, -8], -11)
        assert result == [2, 3], f"Test 66 failed: got {result}, expected {[2, 3]}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = twoSum([-5, -2, -3, -8, -12, 0], -20)
        assert result == [3, 4], f"Test 67 failed: got {result}, expected {[3, 4]}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = twoSum([1000000, -999999, 5, 0], 1)
        assert result == [0, 1], f"Test 68 failed: got {result}, expected {[0, 1]}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = twoSum([5, -999999, 1000000, 0], 1)
        assert result == [1, 2], f"Test 69 failed: got {result}, expected {[1, 2]}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = twoSum([6, 14, 21, 28, 35], 56)
        assert result == [2, 4], f"Test 70 failed: got {result}, expected {[2, 4]}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = twoSum([7, 14, 21, 28, 35, 0, 0], 56)
        assert result == [2, 4], f"Test 71 failed: got {result}, expected {[2, 4]}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = twoSum([7, 14, 21, 28, 35, 0], 56)
        assert result == [2, 4], f"Test 72 failed: got {result}, expected {[2, 4]}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = twoSum([5, 5, 10, 0, -10], -10)
        assert result == [3, 4], f"Test 73 failed: got {result}, expected {[3, 4]}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = twoSum([5, 10, 0, -10, 18], -5)
        assert result == [0, 3], f"Test 74 failed: got {result}, expected {[0, 3]}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = twoSum([-10, 0, 10, 5, 1000000], -5)
        assert result == [0, 3], f"Test 75 failed: got {result}, expected {[0, 3]}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = twoSum([-10, 0, 10, 5], 0)
        assert result == [0, 2], f"Test 76 failed: got {result}, expected {[0, 2]}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = twoSum([-10, 0, 10, 5, 0, 0, 0], -5)
        assert result == [0, 3], f"Test 77 failed: got {result}, expected {[0, 3]}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = twoSum([-10, 0, 10, 5], 5)
        assert result == [1, 3], f"Test 78 failed: got {result}, expected {[1, 3]}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = twoSum([-10, 0, 9, 5], 5)
        assert result == [1, 3], f"Test 79 failed: got {result}, expected {[1, 3]}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = twoSum([2, 2, 3, 9, 56], 4)
        assert result == [0, 1], f"Test 80 failed: got {result}, expected {[0, 1]}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = twoSum([2, 2, 3, 9, 0], 4)
        assert result == [0, 1], f"Test 81 failed: got {result}, expected {[0, 1]}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = twoSum([1000001, 9, 3, 2, 2], 4)
        assert result == [3, 4], f"Test 82 failed: got {result}, expected {[3, 4]}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = twoSum([13, 1, 6, 6], 12)
        assert result == [2, 3], f"Test 83 failed: got {result}, expected {[2, 3]}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = twoSum([6, 6, 2, 13], 12)
        assert result == [0, 1], f"Test 84 failed: got {result}, expected {[0, 1]}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = twoSum([13, 1, 6], 14)
        assert result == [0, 1], f"Test 85 failed: got {result}, expected {[0, 1]}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = twoSum([-1, -1, 2, 5, 11], 7)
        assert result == [2, 3], f"Test 86 failed: got {result}, expected {[2, 3]}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = twoSum([-2, -1, 2, 5, -4], -3)
        assert result == [0, 1], f"Test 87 failed: got {result}, expected {[0, 1]}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = twoSum([-1, -1, 2, 5, 0], -2)
        assert result == [0, 1], f"Test 88 failed: got {result}, expected {[0, 1]}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = twoSum([35, 0, 5, 2, -1, -1], -2)
        assert result == [4, 5], f"Test 89 failed: got {result}, expected {[4, 5]}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = twoSum([5, 0, 13, -4, 9], 18)
        assert result == [0, 2], f"Test 90 failed: got {result}, expected {[0, 2]}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = twoSum([9, -4, 13, 0, 5, 0], 0)
        assert result == [3, 5], f"Test 91 failed: got {result}, expected {[3, 5]}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = twoSum([9, 13, 0, 5], 18)
        assert result == [1, 3], f"Test 92 failed: got {result}, expected {[1, 3]}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = twoSum([9, -4, 13, 5], 18)
        assert result == [2, 3], f"Test 93 failed: got {result}, expected {[2, 3]}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = twoSum([-9, -4, 0, 18, 100], 18)
        assert result == [2, 3], f"Test 94 failed: got {result}, expected {[2, 3]}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = twoSum([5, 0, 13, -4], 18)
        assert result == [0, 2], f"Test 95 failed: got {result}, expected {[0, 2]}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = twoSum([9, -4, 13, 0, 5, 0], 18)
        assert result == [2, 4], f"Test 96 failed: got {result}, expected {[2, 4]}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = twoSum([0, -2, 11, 3, -7], 1)
        assert result == [1, 3], f"Test 97 failed: got {result}, expected {[1, 3]}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = twoSum([-7, 3, 11, -2, 6, -200], 1)
        assert result == [1, 3], f"Test 98 failed: got {result}, expected {[1, 3]}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = twoSum([0, 6, -2, 11, 3, -1000000], 11)
        assert result == [0, 3], f"Test 99 failed: got {result}, expected {[0, 3]}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = twoSum([0, 1, 2, 21, 4], 1)
        assert result == [0, 1], f"Test 100 failed: got {result}, expected {[0, 1]}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = twoSum([0, 1, 2, 3, 4, 0], 0)
        assert result == [0, 5], f"Test 101 failed: got {result}, expected {[0, 5]}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = twoSum([4, 3, 2, 1, 0], 1)
        assert result == [3, 4], f"Test 102 failed: got {result}, expected {[3, 4]}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = twoSum([0, 1, 2, 3, 4, 56], 1)
        assert result == [0, 1], f"Test 103 failed: got {result}, expected {[0, 1]}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = twoSum([0, 1, 2, 3, 4, 49], 6)
        assert result == [2, 4], f"Test 104 failed: got {result}, expected {[2, 4]}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = twoSum([0, 1, 2, 3, 4], 6)
        assert result == [2, 4], f"Test 105 failed: got {result}, expected {[2, 4]}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = twoSum([0, 1, 2, 3, 4, 40], 6)
        assert result == [2, 4], f"Test 106 failed: got {result}, expected {[2, 4]}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = twoSum([4, 3, 2, 1, 0, 0], 0)
        assert result == [4, 5], f"Test 107 failed: got {result}, expected {[4, 5]}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = twoSum([-2, 4, 3, 2, 1, 0, -24], 7)
        assert result == [1, 2], f"Test 108 failed: got {result}, expected {[1, 2]}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = twoSum([-100, 50, 48, 1], -50)
        assert result == [0, 1], f"Test 109 failed: got {result}, expected {[0, 1]}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = twoSum([1, 49, 50, -100], 50)
        assert result == [0, 1], f"Test 110 failed: got {result}, expected {[0, 1]}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = twoSum([-1, 1, 49, 50, -100], 51)
        assert result == [1, 3], f"Test 111 failed: got {result}, expected {[1, 3]}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = twoSum([-100, 50, 49, 1], 51)
        assert result == [1, 3], f"Test 112 failed: got {result}, expected {[1, 3]}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = twoSum([12, -5, 7, -1, 20, 0], 6)
        assert result == [2, 3], f"Test 113 failed: got {result}, expected {[2, 3]}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = twoSum([12, -5, 7, -1, 20], 7)
        assert result == [0, 1], f"Test 114 failed: got {result}, expected {[0, 1]}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = twoSum([12, -5, 7, -1, 20, 0], 12)
        assert result == [0, 5], f"Test 115 failed: got {result}, expected {[0, 5]}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = twoSum([12, -5, 7, -1], 6)
        assert result == [2, 3], f"Test 116 failed: got {result}, expected {[2, 3]}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = twoSum([12, -5, 7, -1, 20, 0, 0], 15)
        assert result == [1, 4], f"Test 117 failed: got {result}, expected {[1, 4]}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = twoSum([2147483647, -2147483648, 1, 0, -101], 1)
        assert result == [2, 3], f"Test 118 failed: got {result}, expected {[2, 3]}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = twoSum([-3, -2147483648, 1, 0], 1)
        assert result == [2, 3], f"Test 119 failed: got {result}, expected {[2, 3]}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = twoSum([1, 0, -2], -1)
        assert result == [0, 2], f"Test 120 failed: got {result}, expected {[0, 2]}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = twoSum([2147483647, -2147483648, 1, 0, 0], -1)
        assert result == [0, 1], f"Test 121 failed: got {result}, expected {[0, 1]}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = twoSum([0, 0, 1, -2147483648, 2147483647], -1)
        assert result == [3, 4], f"Test 122 failed: got {result}, expected {[3, 4]}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = twoSum([2147483647, -2147483648, 0, 0, -22], 0)
        assert result == [2, 3], f"Test 123 failed: got {result}, expected {[2, 3]}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = twoSum([5, 1, 5, -49], 10)
        assert result == [0, 2], f"Test 124 failed: got {result}, expected {[0, 2]}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = twoSum([8, -3, 4, 9, -1], 3)
        assert result == [2, 4], f"Test 125 failed: got {result}, expected {[2, 4]}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = twoSum([-1, 9, 4, -3, 8, 0], 1)
        assert result == [2, 3], f"Test 126 failed: got {result}, expected {[2, 3]}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = twoSum([-1, 9, 4, -3, 8, -200], 6)
        assert result == [1, 3], f"Test 127 failed: got {result}, expected {[1, 3]}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = twoSum([0, -1, 9, 4, -3, 8], 13)
        assert result == [2, 3], f"Test 128 failed: got {result}, expected {[2, 3]}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = twoSum([8, -3, 4, 9, -1], 12)
        assert result == [0, 2], f"Test 129 failed: got {result}, expected {[0, 2]}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = twoSum([8, -3, 4, 9, -1, 100], 6)
        assert result == [1, 3], f"Test 130 failed: got {result}, expected {[1, 3]}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = twoSum([2, 9, 11, -7, 4], 15)
        assert result == [2, 4], f"Test 131 failed: got {result}, expected {[2, 4]}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = twoSum([4, -7, 11, 2], 4)
        assert result == [1, 2], f"Test 132 failed: got {result}, expected {[1, 2]}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = twoSum([50, 4, 11, 18, 2], 6)
        assert result == [1, 4], f"Test 133 failed: got {result}, expected {[1, 4]}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = twoSum([9, 11, -7, 0], 4)
        assert result == [1, 2], f"Test 134 failed: got {result}, expected {[1, 2]}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = twoSum([15, 5, -20, 10, 30, 0], 20)
        assert result == [0, 1], f"Test 135 failed: got {result}, expected {[0, 1]}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = twoSum([30, 10, -20, 5, 15, 0, 0], 0)
        assert result == [5, 6], f"Test 136 failed: got {result}, expected {[5, 6]}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = twoSum([30, 10, -20, 5, 15, 0], 20)
        assert result == [3, 4], f"Test 137 failed: got {result}, expected {[3, 4]}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = twoSum([30, 10, -20, 5, 15, -21], 20)
        assert result == [3, 4], f"Test 138 failed: got {result}, expected {[3, 4]}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = twoSum([0, 0, 18], 0)
        assert result == [0, 1], f"Test 139 failed: got {result}, expected {[0, 1]}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = twoSum([1, 2, 3, 4], 6)
        assert result == [1, 3], f"Test 140 failed: got {result}, expected {[1, 3]}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = twoSum([2, 3, 4], 5)
        assert result == [0, 1], f"Test 141 failed: got {result}, expected {[0, 1]}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = twoSum([3, 4, 0, -49], 4)
        assert result == [1, 2], f"Test 142 failed: got {result}, expected {[1, 2]}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = twoSum([1, 2, 4], 5)
        assert result == [0, 2], f"Test 143 failed: got {result}, expected {[0, 2]}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = twoSum([0, 4, 3, 52, 1], 5)
        assert result == [1, 4], f"Test 144 failed: got {result}, expected {[1, 4]}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = twoSum([1, 2, 3, 4], 4)
        assert result == [0, 2], f"Test 145 failed: got {result}, expected {[0, 2]}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = twoSum([0, 0, 1], 0)
        assert result == [0, 1], f"Test 146 failed: got {result}, expected {[0, 1]}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = twoSum([-5, -4, -3, 0, 0], 0)
        assert result == [3, 4], f"Test 147 failed: got {result}, expected {[3, 4]}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = twoSum([11, -1, 1, -1, 0, 12], 1)
        assert result == [2, 4], f"Test 148 failed: got {result}, expected {[2, 4]}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = twoSum([2, 7, 11, 0, -2, 0, 0, 0], 18)
        assert result == [1, 2], f"Test 149 failed: got {result}, expected {[1, 2]}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = twoSum([-2, 15, 11], 9)
        assert result == [0, 2], f"Test 150 failed: got {result}, expected {[0, 2]}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = twoSum([-2, 15, 11, 2], 9)
        assert result == [0, 2], f"Test 151 failed: got {result}, expected {[0, 2]}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = twoSum([55, -2, 15, 11, 7, 2], 0)
        assert result == [1, 5], f"Test 152 failed: got {result}, expected {[1, 5]}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
