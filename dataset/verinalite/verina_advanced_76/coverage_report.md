# Coverage Report

Total executable lines: 9
Covered lines: 9
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def topKFrequent(nums, k):
2: ✓     freq = {}
3: ✓     first_index = {}
4: ✓     for i, num in enumerate(nums):
5: ✓         freq[num] = freq.get(num, 0) + 1
6: ✓         if num not in first_index:
7: ✓             first_index[num] = i
8: ✓     sorted_nums = sorted(freq.keys(), key=lambda x: (-freq[x], first_index[x]))
9: ✓     return sorted_nums[:k]
```

## Complete Test File

```python
def topKFrequent(nums, k):
    freq = {}
    first_index = {}
    for i, num in enumerate(nums):
        freq[num] = freq.get(num, 0) + 1
        if num not in first_index:
            first_index[num] = i
    sorted_nums = sorted(freq.keys(), key=lambda x: (-freq[x], first_index[x]))
    return sorted_nums[:k]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = topKFrequent([1, 1, 1, 2, 2, 3], 2)
        assert result == [1, 2], f"Test 1 failed: got {result}, expected {[1, 2]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
        assert result == [-1, 2], f"Test 2 failed: got {result}, expected {[-1, 2]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = topKFrequent([5], 1)
        assert result == [5], f"Test 3 failed: got {result}, expected {[5]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = topKFrequent([7, 7, 7, 8, 8, 9], 1)
        assert result == [7], f"Test 4 failed: got {result}, expected {[7]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = topKFrequent([], 0)
        assert result == [], f"Test 5 failed: got {result}, expected {[]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = topKFrequent([1, 2, 2, 3, 3, 3], 2)
        assert result == [3, 2], f"Test 6 failed: got {result}, expected {[3, 2]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = topKFrequent([2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5], 4)
        assert result == [4, 2, 5, 3], f"Test 7 failed: got {result}, expected {[4, 2, 5, 3]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = topKFrequent([1, 1, 2, 2, 3], 2)
        assert result == [1, 2], f"Test 8 failed: got {result}, expected {[1, 2]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = topKFrequent([4, 1, -1, 2, -1, -2, 4], 2)
        assert result == [4, -1], f"Test 9 failed: got {result}, expected {[4, -1]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = topKFrequent([4, 1, -1, 2, -1, 2, 3, 11], 2)
        assert result == [-1, 2], f"Test 10 failed: got {result}, expected {[-1, 2]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = topKFrequent([1, 2, 3], 3)
        assert result == [1, 2, 3], f"Test 11 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = topKFrequent([1, 2, 0, 0], 2)
        assert result == [0, 1], f"Test 12 failed: got {result}, expected {[0, 1]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = topKFrequent([3, 3, 3, 2, 2, 1, 0], 3)
        assert result == [3, 2, 1], f"Test 13 failed: got {result}, expected {[3, 2, 1]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = topKFrequent([0, 0, 3, 3, 3, 2, 2, 1, 22], 2)
        assert result == [3, 0], f"Test 14 failed: got {result}, expected {[3, 0]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = topKFrequent([41, 1, 2, 2, 3, 3, 3], 3)
        assert result == [3, 2, 41], f"Test 15 failed: got {result}, expected {[3, 2, 41]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = topKFrequent([0, 0, 3, 3, 3, 2, 2, 1], 4)
        assert result == [3, 0, 2, 1], f"Test 16 failed: got {result}, expected {[3, 0, 2, 1]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = topKFrequent([1, 4, 2, 3, 3, 3, 0, 0], 2)
        assert result == [3, 0], f"Test 17 failed: got {result}, expected {[3, 0]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = topKFrequent([-1, -1, -2, -2, -3, 0, -2147483646], 3)
        assert result == [-1, -2, -3], f"Test 18 failed: got {result}, expected {[-1, -2, -3]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = topKFrequent([-3, -2, -2, -1, -1], 3)
        assert result == [-2, -1, -3], f"Test 19 failed: got {result}, expected {[-2, -1, -3]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = topKFrequent([-1, -1, -2, -3], 2)
        assert result == [-1, -2], f"Test 20 failed: got {result}, expected {[-1, -2]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = topKFrequent([-1, -1, -2, -2, -3], 2)
        assert result == [-1, -2], f"Test 21 failed: got {result}, expected {[-1, -2]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = topKFrequent([-1, -2, -2, 24, -4], 1)
        assert result == [-2], f"Test 22 failed: got {result}, expected {[-2]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = topKFrequent([5, 4, 3, 2, 1, 0], 5)
        assert result == [5, 4, 3, 2, 1], f"Test 23 failed: got {result}, expected {[5, 4, 3, 2, 1]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = topKFrequent([8, 5, 10, 3, 2, 1], 2)
        assert result == [8, 5], f"Test 24 failed: got {result}, expected {[8, 5]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = topKFrequent([5, 4, 3, 2, 1, 22], 4)
        assert result == [5, 4, 3, 2], f"Test 25 failed: got {result}, expected {[5, 4, 3, 2]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = topKFrequent([1, 2, 3, 4, 5, -4], 3)
        assert result == [1, 2, 3], f"Test 26 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = topKFrequent([12, 10, 9, 9, 0, 8, 7, 7], 5)
        assert result == [9, 7, 12, 10, 0], f"Test 27 failed: got {result}, expected {[9, 7, 12, 10, 0]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = topKFrequent([1000000000, -1000000000, 1000000000, 0, 0], 3)
        assert result == [1000000000, 0, -1000000000], f"Test 28 failed: got {result}, expected {[1000000000, 0, -1000000000]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = topKFrequent([42, 42, 42, 42, 42, 43, 0], 2)
        assert result == [42, 43], f"Test 29 failed: got {result}, expected {[42, 43]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = topKFrequent([0, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 88], 5)
        assert result == [4, 2, 5, 3, 0], f"Test 30 failed: got {result}, expected {[4, 2, 5, 3, 0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = topKFrequent([5, 5, 6, 4, 4, 4, 4, 3, 3, 2, 2, 2], 4)
        assert result == [4, 2, 5, 3], f"Test 31 failed: got {result}, expected {[4, 2, 5, 3]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = topKFrequent([5, 5, 5, 4, 4, 4, 4, 5, 3, 2, 2, 2, -1], 2)
        assert result == [5, 4], f"Test 32 failed: got {result}, expected {[5, 4]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = topKFrequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0], 5)
        assert result == [1, 2, 3, 4, 5], f"Test 33 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = topKFrequent([1, 3, 4, 5, 6, 7, 8, 9, 0], 9)
        assert result == [1, 3, 4, 5, 6, 7, 8, 9, 0], f"Test 34 failed: got {result}, expected {[1, 3, 4, 5, 6, 7, 8, 9, 0]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = topKFrequent([1, 2, 3, 4, 5, 5, 7, 8, 10, -1000000000], 9)
        assert result == [5, 1, 2, 3, 4, 7, 8, 10, -1000000000], f"Test 35 failed: got {result}, expected {[5, 1, 2, 3, 4, 7, 8, 10, -1000000000]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = topKFrequent([3, 3, 3, 3, 2, 2, 1, 0, 18], 3)
        assert result == [3, 2, 1], f"Test 36 failed: got {result}, expected {[3, 2, 1]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = topKFrequent([3, 3, 3, 3, 2, 2, 1, 999999998, 0, 0], 3)
        assert result == [3, 2, 0], f"Test 37 failed: got {result}, expected {[3, 2, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = topKFrequent([3, 3, 3, 2, 2, 1], 2)
        assert result == [3, 2], f"Test 38 failed: got {result}, expected {[3, 2]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = topKFrequent([3, 3, 3, -2, 2, 1, 21], 2)
        assert result == [3, -2], f"Test 39 failed: got {result}, expected {[3, -2]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = topKFrequent([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 0], 11)
        assert result == [0, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5], f"Test 40 failed: got {result}, expected {[0, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = topKFrequent([11, 10, 10, 9, 9, 0, 8, 7, 7, 0, 21], 5)
        assert result == [10, 9, 0, 7, 11], f"Test 41 failed: got {result}, expected {[10, 9, 0, 7, 11]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = topKFrequent([7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 0], 5)
        assert result == [7, 8, 9, 10, 11], f"Test 42 failed: got {result}, expected {[7, 8, 9, 10, 11]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = topKFrequent([0, 11, 11, 10, 10, 9, 9, 8, 8, 7, 7], 6)
        assert result == [11, 10, 9, 8, 7, 0], f"Test 43 failed: got {result}, expected {[11, 10, 9, 8, 7, 0]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = topKFrequent([2147483647, -2147483648, 2147483647, -2147483648, 0, 0], 3)
        assert result == [2147483647, -2147483648, 0], f"Test 44 failed: got {result}, expected {[2147483647, -2147483648, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = topKFrequent([2147483647, -2147483648, 2147483647, -2147483648, 0, 300], 3)
        assert result == [2147483647, -2147483648, 0], f"Test 45 failed: got {result}, expected {[2147483647, -2147483648, 0]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = topKFrequent([1, 1, 2, 2, 3, 3, 4, -4, 5, 5, 6, 6], 7)
        assert result == [1, 2, 3, 5, 6, 4, -4], f"Test 46 failed: got {result}, expected {[1, 2, 3, 5, 6, 4, -4]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = topKFrequent([6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1], 5)
        assert result == [6, 5, 4, 3, 2], f"Test 47 failed: got {result}, expected {[6, 5, 4, 3, 2]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = topKFrequent([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 0], 6)
        assert result == [1, 2, 3, 5, 6, 4], f"Test 48 failed: got {result}, expected {[1, 2, 3, 5, 6, 4]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = topKFrequent([-6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1], 6)
        assert result == [5, 4, 3, 2, 1, -6], f"Test 49 failed: got {result}, expected {[5, 4, 3, 2, 1, -6]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = topKFrequent([3, 2, 1, 7, 0], 4)
        assert result == [3, 2, 1, 7], f"Test 50 failed: got {result}, expected {[3, 2, 1, 7]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = topKFrequent([1, 2, 3], 3)
        assert result == [1, 2, 3], f"Test 51 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = topKFrequent([-1, -2, -3, -4, 0], 5)
        assert result == [-1, -2, -3, -4, 0], f"Test 52 failed: got {result}, expected {[-1, -2, -3, -4, 0]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = topKFrequent([-9, 9, 8, 8, 7, 7, 6, 6, 5, 5], 6)
        assert result == [8, 7, 6, 5, -9, 9], f"Test 53 failed: got {result}, expected {[8, 7, 6, 5, -9, 9]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = topKFrequent([9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 11, 0], 3)
        assert result == [9, 8, 7], f"Test 54 failed: got {result}, expected {[9, 8, 7]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
