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
6: ✓             return (seen[complement], i)
7: ✓         seen[num] = i
```

## Complete Test File

```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = twoSum([2, 7, 11, 15], 9)
        assert result == (0, 1), f"Test 1 failed: got {result}, expected {(0, 1)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = twoSum([3, 2, 4], 6)
        assert result == (1, 2), f"Test 2 failed: got {result}, expected {(1, 2)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = twoSum([3, 3], 6)
        assert result == (0, 1), f"Test 3 failed: got {result}, expected {(0, 1)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = twoSum([1, 2, 3, 4], 7)
        assert result == (2, 3), f"Test 4 failed: got {result}, expected {(2, 3)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = twoSum([0, 4, 3, 0], 0)
        assert result == (0, 3), f"Test 5 failed: got {result}, expected {(0, 3)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = twoSum([-1, -2, -3, -4, -5], -8)
        assert result == (2, 4), f"Test 6 failed: got {result}, expected {(2, 4)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = twoSum([10, -2, 8, 1], 9)
        assert result == (2, 3), f"Test 7 failed: got {result}, expected {(2, 3)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = twoSum([1, 5, 1, 5], 10)
        assert result == (1, 3), f"Test 8 failed: got {result}, expected {(1, 3)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = twoSum([-10, 21, 30, -20, 5], 10)
        assert result == (2, 3), f"Test 9 failed: got {result}, expected {(2, 3)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = twoSum([6, 1, 8, 14], 15)
        assert result == (1, 3), f"Test 10 failed: got {result}, expected {(1, 3)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = twoSum([0, 1, 2, 3], 1)
        assert result == (0, 1), f"Test 11 failed: got {result}, expected {(0, 1)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = twoSum([11, 22, 33, 44, 55], 99)
        assert result == (3, 4), f"Test 12 failed: got {result}, expected {(3, 4)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = twoSum([2147483647, -2147483648, 1, 0], -1)
        assert result == (0, 1), f"Test 13 failed: got {result}, expected {(0, 1)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = twoSum([-2147483648, 2147483647, -1, 2], 1)
        assert result == (2, 3), f"Test 14 failed: got {result}, expected {(2, 3)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = twoSum([5, 0, -4, 10], 5)
        assert result == (0, 1), f"Test 15 failed: got {result}, expected {(0, 1)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = twoSum([13, 26, 39, 52], 78)
        assert result == (1, 3), f"Test 16 failed: got {result}, expected {(1, 3)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = twoSum([1, 1, 2, 3], 5)
        assert result == (2, 3), f"Test 17 failed: got {result}, expected {(2, 3)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = twoSum([0, 4, 3, 0, 200], 0)
        assert result == (0, 3), f"Test 18 failed: got {result}, expected {(0, 3)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = twoSum([13, 0, 3, 4, 0], 0)
        assert result == (1, 4), f"Test 19 failed: got {result}, expected {(1, 4)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = twoSum([-7, 15, 11, 7, 2], 0)
        assert result == (0, 3), f"Test 20 failed: got {result}, expected {(0, 3)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = twoSum([1, 2, 3, 4], 6)
        assert result == (1, 3), f"Test 21 failed: got {result}, expected {(1, 3)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = twoSum([0, -2, -3, -4, -5], -8)
        assert result == (2, 4), f"Test 22 failed: got {result}, expected {(2, 4)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = twoSum([10, -2, 8, 1, 0], -1)
        assert result == (1, 3), f"Test 23 failed: got {result}, expected {(1, 3)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = twoSum([10, -2, 8, 1, 0], 9)
        assert result == (2, 3), f"Test 24 failed: got {result}, expected {(2, 3)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = twoSum([10, -2, 8, 1, 0, 32], 11)
        assert result == (0, 3), f"Test 25 failed: got {result}, expected {(0, 3)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = twoSum([1, 10, 1, 6, 6, 0], 10)
        assert result == (1, 5), f"Test 26 failed: got {result}, expected {(1, 5)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = twoSum([1, 5, 1, 5, -5, 0, 0], 10)
        assert result == (1, 3), f"Test 27 failed: got {result}, expected {(1, 3)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = twoSum([0, 5, 1, 5], 10)
        assert result == (1, 3), f"Test 28 failed: got {result}, expected {(1, 3)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = twoSum([1, 5, 1, 5, 1, 0], 10)
        assert result == (1, 3), f"Test 29 failed: got {result}, expected {(1, 3)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = twoSum([4, 3, 2, 2, 11], 4)
        assert result == (2, 3), f"Test 30 failed: got {result}, expected {(2, 3)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = twoSum([4, 3, 2, 2, 55], 4)
        assert result == (2, 3), f"Test 31 failed: got {result}, expected {(2, 3)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = twoSum([1000000, -1000000, 3, 7, 0, 0, 0], 10)
        assert result == (2, 3), f"Test 32 failed: got {result}, expected {(2, 3)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = twoSum([65, 5, -20, 30, 21, -10], 20)
        assert result == (3, 5), f"Test 33 failed: got {result}, expected {(3, 5)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = twoSum([-10, 30, -20, 5, 1000000], -15)
        assert result == (2, 3), f"Test 34 failed: got {result}, expected {(2, 3)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = twoSum([68, 5, -20, 30, 21, -10], 10)
        assert result == (2, 3), f"Test 35 failed: got {result}, expected {(2, 3)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = twoSum([6, 1, 16, 14], 15)
        assert result == (1, 3), f"Test 36 failed: got {result}, expected {(1, 3)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = twoSum([0, -1, 14, 1, 6], 15)
        assert result == (2, 3), f"Test 37 failed: got {result}, expected {(2, 3)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = twoSum([9, -6, 4, 12], 6)
        assert result == (1, 3), f"Test 38 failed: got {result}, expected {(1, 3)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = twoSum([11, 22, 33, 44, 55, 0, 52], 99)
        assert result == (3, 4), f"Test 39 failed: got {result}, expected {(3, 4)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = twoSum([2147483647, -2147483648, 1, 0, 128], 1)
        assert result == (2, 3), f"Test 40 failed: got {result}, expected {(2, 3)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = twoSum([-2147483648, 2147483647, -1, 2, 0], 1)
        assert result == (2, 3), f"Test 41 failed: got {result}, expected {(2, 3)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = twoSum([-2147483648, 2147483647, -2, 2, -99], 0)
        assert result == (2, 3), f"Test 42 failed: got {result}, expected {(2, 3)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = twoSum([-97, 0, -4, 10, -101, 0], 6)
        assert result == (2, 3), f"Test 43 failed: got {result}, expected {(2, 3)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = twoSum([0, 0, -7, -1, 9, 1], 2)
        assert result == (2, 4), f"Test 44 failed: got {result}, expected {(2, 4)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = twoSum([2, 9, -1, -7], 2)
        assert result == (1, 3), f"Test 45 failed: got {result}, expected {(1, 3)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = twoSum([2, 9, -1, -6, 0], 3)
        assert result == (1, 3), f"Test 46 failed: got {result}, expected {(1, 3)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = twoSum([-7, -1, 9, 2, 0], 1)
        assert result == (1, 3), f"Test 47 failed: got {result}, expected {(1, 3)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = twoSum([-7, -1, 9, 2, 200], 1)
        assert result == (1, 3), f"Test 48 failed: got {result}, expected {(1, 3)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = twoSum([13, 26, 39, 52, 110], 78)
        assert result == (1, 3), f"Test 49 failed: got {result}, expected {(1, 3)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = twoSum([0, -7, 20, 10, 3], 23)
        assert result == (2, 4), f"Test 50 failed: got {result}, expected {(2, 4)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = twoSum([1, 2, 0, 0, 55], 0)
        assert result == (2, 3), f"Test 51 failed: got {result}, expected {(2, 3)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
