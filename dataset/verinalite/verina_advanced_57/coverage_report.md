# Coverage Report

Total executable lines: 11
Covered lines: 11
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def nextGreaterElement(nums1, nums2):
2: ✓     next_greater = {}
3: ✓     stack = []
4: ✓     for num in nums2:
5: ✓         while stack and num > stack[-1]:
6: ✓             prev = stack.pop()
7: ✓             next_greater[prev] = num
8: ✓         stack.append(num)
9: ✓     for num in stack:
10: ✓         next_greater[num] = -1
11: ✓     return [next_greater[num] for num in nums1]
```

## Complete Test File

```python
def nextGreaterElement(nums1, nums2):
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and num > stack[-1]:
            prev = stack.pop()
            next_greater[prev] = num
        stack.append(num)
    for num in stack:
        next_greater[num] = -1
    return [next_greater[num] for num in nums1]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
        assert result == [-1, 3, -1], f"Test 1 failed: got {result}, expected {[-1, 3, -1]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = nextGreaterElement([2, 4], [1, 2, 3, 4])
        assert result == [3, -1], f"Test 2 failed: got {result}, expected {[3, -1]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = nextGreaterElement([1], [1, 2])
        assert result == [2], f"Test 3 failed: got {result}, expected {[2]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = nextGreaterElement([5], [5, 4, 3, 2, 1])
        assert result == [-1], f"Test 4 failed: got {result}, expected {[-1]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1])
        assert result == [-1, -1, -1, -1, -1], f"Test 5 failed: got {result}, expected {[-1, -1, -1, -1, -1]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = nextGreaterElement([1, 2, 3], [3, 2, 1, 4])
        assert result == [4, 4, 4], f"Test 6 failed: got {result}, expected {[4, 4, 4]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = nextGreaterElement([4, 3, 2, 1], [4, 3, 2, 1])
        assert result == [-1, -1, -1, -1], f"Test 7 failed: got {result}, expected {[-1, -1, -1, -1]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = nextGreaterElement([5], [2, 5, 7])
        assert result == [7], f"Test 8 failed: got {result}, expected {[7]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = nextGreaterElement([1, 2, 3], [1, 2, 3])
        assert result == [2, 3, -1], f"Test 9 failed: got {result}, expected {[2, 3, -1]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = nextGreaterElement([-3, -1], [-3, -2, -1, 0])
        assert result == [-2, 0], f"Test 10 failed: got {result}, expected {[-2, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = nextGreaterElement([0, -2], [-2, 0, 2])
        assert result == [2, 0], f"Test 11 failed: got {result}, expected {[2, 0]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = nextGreaterElement([1000000, -1000000], [-1000000, 0, 999999, 1000000])
        assert result == [-1, 0], f"Test 12 failed: got {result}, expected {[-1, 0]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = nextGreaterElement([2, 7], [2, 1, 7, 8, 3])
        assert result == [7, 8], f"Test 13 failed: got {result}, expected {[7, 8]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = nextGreaterElement([-5, 3, 9], [9, -5, 0, 3, 4, 8])
        assert result == [0, 4, -1], f"Test 14 failed: got {result}, expected {[0, 4, -1]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = nextGreaterElement([11, 14], [10, 11, 12, 13, 14, 15])
        assert result == [12, 15], f"Test 15 failed: got {result}, expected {[12, 15]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = nextGreaterElement([1, 3, 5, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8])
        assert result == [2, 4, 6, 8], f"Test 16 failed: got {result}, expected {[2, 4, 6, 8]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = nextGreaterElement([0, 2, 4, 6], [0, 1, 2, 3, 4, 5, 6, 7])
        assert result == [1, 3, 5, 7], f"Test 17 failed: got {result}, expected {[1, 3, 5, 7]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = nextGreaterElement([13, 1, 8, 21, 3], [13, 1, 34, 8, 2, 21, 5, 3])
        assert result == [34, 34, 21, -1, -1], f"Test 18 failed: got {result}, expected {[34, 34, 21, -1, -1]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = nextGreaterElement([13, 1, 34, 8, 2, 21, 5], [13, 1, 34, 8, 2, 21, 5, 3])
        assert result == [34, 34, -1, 21, 21, -1, -1], f"Test 19 failed: got {result}, expected {[34, 34, -1, 21, 21, -1, -1]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = nextGreaterElement([2147483647, -2147483648], [-2147483648, 2147483647])
        assert result == [-1, 2147483647], f"Test 20 failed: got {result}, expected {[-1, 2147483647]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = nextGreaterElement([31, 17], [5, 31, 12, 17, 29])
        assert result == [-1, 29], f"Test 21 failed: got {result}, expected {[-1, 29]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = nextGreaterElement([-999999999999, 999999999999], [7, -999999999999, 0, 999999999999, 8])
        assert result == [0, -1], f"Test 22 failed: got {result}, expected {[0, -1]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = nextGreaterElement([6, 1, 4], [6, 2, 1, 3, 4, 5])
        assert result == [-1, 3, 5], f"Test 23 failed: got {result}, expected {[-1, 3, 5]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = nextGreaterElement([15, 5, 25], [5, 10, 15, 20, 25, 30])
        assert result == [20, 10, 30], f"Test 24 failed: got {result}, expected {[20, 10, 30]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = nextGreaterElement([1, 2], [1, 3, 4, 2])
        assert result == [3, -1], f"Test 25 failed: got {result}, expected {[3, -1]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = nextGreaterElement([4, 1, 2], [1, 3, 4, 2, 0])
        assert result == [-1, 3, -1], f"Test 26 failed: got {result}, expected {[-1, 3, -1]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = nextGreaterElement([2, 1, 4], [1, 4, 2])
        assert result == [-1, 4, -1], f"Test 27 failed: got {result}, expected {[-1, 4, -1]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = nextGreaterElement([2], [1, 2, 3, 4])
        assert result == [3], f"Test 28 failed: got {result}, expected {[3]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = nextGreaterElement([2], [1, 2, 3, 4, 42])
        assert result == [3], f"Test 29 failed: got {result}, expected {[3]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = nextGreaterElement([2, 4], [4, 3, 2, 1, 34])
        assert result == [34, 34], f"Test 30 failed: got {result}, expected {[34, 34]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = nextGreaterElement([4, 2], [1, 2, 3, 4])
        assert result == [-1, 3], f"Test 31 failed: got {result}, expected {[-1, 3]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = nextGreaterElement([1, 0], [1, 15, 0])
        assert result == [15, -1], f"Test 32 failed: got {result}, expected {[15, -1]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = nextGreaterElement([1], [1, 2, 0])
        assert result == [2], f"Test 33 failed: got {result}, expected {[2]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = nextGreaterElement([5], [1, 2, 3, 4, 5, 0, 60])
        assert result == [60], f"Test 34 failed: got {result}, expected {[60]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = nextGreaterElement([5], [5, 4, 3, 2, 29, -5, 0, 17])
        assert result == [29], f"Test 35 failed: got {result}, expected {[29]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = nextGreaterElement([1, 3, 5, 2, 4], [1, 2, 3, 4, 5, 6])
        assert result == [2, 4, 6, 3, 5], f"Test 36 failed: got {result}, expected {[2, 4, 6, 3, 5]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = nextGreaterElement([1, 3], [3, 2, 1, 4])
        assert result == [4, 4], f"Test 37 failed: got {result}, expected {[4, 4]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = nextGreaterElement([3, 2, 1], [1, 2, 3, 4])
        assert result == [4, 3, 2], f"Test 38 failed: got {result}, expected {[4, 3, 2]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = nextGreaterElement([0], [0, 12])
        assert result == [12], f"Test 39 failed: got {result}, expected {[12]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = nextGreaterElement([0], [0, 3])
        assert result == [3], f"Test 40 failed: got {result}, expected {[3]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = nextGreaterElement([5], [5, 70])
        assert result == [70], f"Test 41 failed: got {result}, expected {[70]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = nextGreaterElement([5], [2, 5, 7, 0])
        assert result == [7], f"Test 42 failed: got {result}, expected {[7]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = nextGreaterElement([5, 0], [2, 5, 7, 0])
        assert result == [7, -1], f"Test 43 failed: got {result}, expected {[7, -1]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = nextGreaterElement([5], [90, 5, 7, 13])
        assert result == [7], f"Test 44 failed: got {result}, expected {[7]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = nextGreaterElement([5], [2, 5, 7, 1])
        assert result == [7], f"Test 45 failed: got {result}, expected {[7]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = nextGreaterElement([1, 2, 3], [1, 2, 3, 12, 0, 6])
        assert result == [2, 3, 12], f"Test 46 failed: got {result}, expected {[2, 3, 12]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = nextGreaterElement([3, 2, 1], [1, 2, 3, 20])
        assert result == [20, 3, 2], f"Test 47 failed: got {result}, expected {[20, 3, 2]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = nextGreaterElement([1, 2], [1, 2, 3])
        assert result == [2, 3], f"Test 48 failed: got {result}, expected {[2, 3]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = nextGreaterElement([3], [1, 3, 0, 999999])
        assert result == [999999], f"Test 49 failed: got {result}, expected {[999999]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = nextGreaterElement([3, 2, 1], [3, 2, 1, 0, 15])
        assert result == [15, 15, 15], f"Test 50 failed: got {result}, expected {[15, 15, 15]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = nextGreaterElement([2, 1, 4], [1, 3, 4, 2, 31])
        assert result == [31, 3, 31], f"Test 51 failed: got {result}, expected {[31, 3, 31]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = nextGreaterElement([-3, -1], [-3, -2, -1, 0, -50])
        assert result == [-2, 0], f"Test 52 failed: got {result}, expected {[-2, 0]}"
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
