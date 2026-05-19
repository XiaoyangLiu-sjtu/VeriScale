# Coverage Report

Total executable lines: 10
Covered lines: 10
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def majorityElement(nums):
2: ✓     candidate, count = None, 0
3: ✓     for num in nums:
4: ✓         if count == 0:
5: ✓             candidate = num
6: ✓             count = 1
7: ✓         elif num == candidate:
8: ✓             count += 1
9:           else:
10: ✓             count -= 1
11: ✓     return candidate
```

## Complete Test File

```python
def majorityElement(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = majorityElement([3, 2, 3])
        assert result == 3, f"Test 1 failed: got {result}, expected {3}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = majorityElement([2, 2, 1, 1, 1, 2, 2])
        assert result == 2, f"Test 2 failed: got {result}, expected {2}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = majorityElement([1])
        assert result == 1, f"Test 3 failed: got {result}, expected {1}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = majorityElement([4, 4, 4, 4, 4, 2, 2, 3, 3])
        assert result == 4, f"Test 4 failed: got {result}, expected {4}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = majorityElement([9, 8, 9, 9, 7, 9, 6, 9, 9])
        assert result == 9, f"Test 5 failed: got {result}, expected {9}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = majorityElement([0, 0, 0, 0, 1])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = majorityElement([100000, 100000, 100000, 100000, -100000])
        assert result == 100000, f"Test 7 failed: got {result}, expected {100000}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = majorityElement([-1, -1, -1, -1, 0, 1, 2])
        assert result == -1, f"Test 8 failed: got {result}, expected {-1}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = majorityElement([5, 5, 5, 5, 5, 5, 5])
        assert result == 5, f"Test 9 failed: got {result}, expected {5}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = majorityElement([1, 2, 3, 3, 3, 3, 3])
        assert result == 3, f"Test 10 failed: got {result}, expected {3}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = majorityElement([5, 5, 3])
        assert result == 5, f"Test 11 failed: got {result}, expected {5}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = majorityElement([1, 1, 2])
        assert result == 1, f"Test 12 failed: got {result}, expected {1}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = majorityElement([-2, -2, -2, 1, 1])
        assert result == -2, f"Test 13 failed: got {result}, expected {-2}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = majorityElement([10, 10, 10, 10, 10, 3, 4, 5, 6])
        assert result == 10, f"Test 14 failed: got {result}, expected {10}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = majorityElement([-5, -5, -5, -5, -5, -1, -2, -3, -4])
        assert result == -5, f"Test 15 failed: got {result}, expected {-5}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = majorityElement([1, 1, 1, 1, 2, 2, 2])
        assert result == 1, f"Test 16 failed: got {result}, expected {1}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = majorityElement([2147483647, 2147483647, -2147483648, 2147483647, 5])
        assert result == 2147483647, f"Test 17 failed: got {result}, expected {2147483647}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = majorityElement([0, 3, 3, 4, 2, 4, 4, 4, 4, 4])
        assert result == 4, f"Test 18 failed: got {result}, expected {4}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = majorityElement([-4, 4, 4, 4, 4, 4, 2, 2, 3])
        assert result == 4, f"Test 19 failed: got {result}, expected {4}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = majorityElement([0, 9, 9, 6, 7, 9, 9, 8, 9])
        assert result == 9, f"Test 20 failed: got {result}, expected {9}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = majorityElement([9, 8, 9, 7, 9, 6, 9, 9, 0, 9, 0])
        assert result == 9, f"Test 21 failed: got {result}, expected {9}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = majorityElement([9, 8, 9, 9, 7, 9, 6, 9, 9, 0])
        assert result == 9, f"Test 22 failed: got {result}, expected {9}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = majorityElement([8, 9, 9, 7, 9, 6, 9, 9, 0])
        assert result == 9, f"Test 23 failed: got {result}, expected {9}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = majorityElement([-100000, 100000, 100000, 100000, 8])
        assert result == 100000, f"Test 24 failed: got {result}, expected {100000}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = majorityElement([2, 0, -1, -1, -1, -1, 0])
        assert result == -1, f"Test 25 failed: got {result}, expected {-1}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = majorityElement([0, 5, 5, 5, 5, 5, 8, 5, 0])
        assert result == 5, f"Test 26 failed: got {result}, expected {5}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = majorityElement([0, 5, 5, 5, 0, 4, 5, 5])
        assert result == 5, f"Test 27 failed: got {result}, expected {5}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = majorityElement([-100000, 5, 5, 5, 5, 5, 5, 4])
        assert result == 5, f"Test 28 failed: got {result}, expected {5}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = majorityElement([0, 5, 5, 5, 5, 5, 5, -2])
        assert result == 5, f"Test 29 failed: got {result}, expected {5}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = majorityElement([0, -6, 5, 5, 5, 5])
        assert result == 5, f"Test 30 failed: got {result}, expected {5}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = majorityElement([1, 2, 3, 3, 3, 3, 3, 0])
        assert result == 3, f"Test 31 failed: got {result}, expected {3}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = majorityElement([1, 0, 3, 3, 3, 3, 3])
        assert result == 3, f"Test 32 failed: got {result}, expected {3}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = majorityElement([0, 3, 3, 3, 3, 2, 1])
        assert result == 3, f"Test 33 failed: got {result}, expected {3}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = majorityElement([2, 2, 1, 1, 2, 2, 200000])
        assert result == 2, f"Test 34 failed: got {result}, expected {2}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = majorityElement([2, 2, 1, 1, 2, 2, 0])
        assert result == 2, f"Test 35 failed: got {result}, expected {2}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = majorityElement([2, 2, 1, 1, 2, 2, 2147483647])
        assert result == 2, f"Test 36 failed: got {result}, expected {2}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = majorityElement([9, 8, 9, 9, 9, 6, 9, 9, 0, -1])
        assert result == 9, f"Test 37 failed: got {result}, expected {9}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = majorityElement([13, 9, 9, 6, 9, 7, 9, 9, 8, 9])
        assert result == 9, f"Test 38 failed: got {result}, expected {9}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = majorityElement([9, 8, 9, 9, 7, 9, 6, 9, 9, 0])
        assert result == 9, f"Test 39 failed: got {result}, expected {9}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = majorityElement([9, 9, 9, 7, 9, 6, 9, 9, 0, 16])
        assert result == 9, f"Test 40 failed: got {result}, expected {9}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = majorityElement([1, -2, -2, -2, 0])
        assert result == -2, f"Test 41 failed: got {result}, expected {-2}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = majorityElement([0, 12, 5, 4, 10, 10, 10, 10, 10])
        assert result == 10, f"Test 42 failed: got {result}, expected {10}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = majorityElement([7, 7, 8, 7, 9, 7, 10, 7, 0])
        assert result == 7, f"Test 43 failed: got {result}, expected {7}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = majorityElement([2, 2, 2, 1, 1, 1, 1, 1, 16])
        assert result == 1, f"Test 44 failed: got {result}, expected {1}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = majorityElement([2, 3, 2, 4, 2, 5, 2, 2, 2, 42])
        assert result == 2, f"Test 45 failed: got {result}, expected {2}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = majorityElement([0, -10, -10, 0, -10])
        assert result == -10, f"Test 46 failed: got {result}, expected {-10}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = majorityElement([0, 42, 42, -42, 42, 42, 42, 12, 5])
        assert result == 42, f"Test 47 failed: got {result}, expected {42}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = majorityElement([0, 12, 42, 42, 84, 42, 42, 42, 1])
        assert result == 42, f"Test 48 failed: got {result}, expected {42}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = majorityElement([0, 5, 42, 42, 42, 42, 42, 42])
        assert result == 42, f"Test 49 failed: got {result}, expected {42}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = majorityElement([-2147483648, 42, 42, 42, 42, 42, 0, 100000])
        assert result == 42, f"Test 50 failed: got {result}, expected {42}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = majorityElement([3, 2, 1, 8, 8, 8, 8, 8, 0])
        assert result == 8, f"Test 51 failed: got {result}, expected {8}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = majorityElement([2, 1, 8, 8, 8, 8, 8, 0, 0])
        assert result == 8, f"Test 52 failed: got {result}, expected {8}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = majorityElement([84, 8, 8, 8, 8, 2, 3])
        assert result == 8, f"Test 53 failed: got {result}, expected {8}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = majorityElement([15, 11, 14, 11, 13, 11, 11, 12, 11])
        assert result == 11, f"Test 54 failed: got {result}, expected {11}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = majorityElement([5, 2147483647, -2147483648, 2147483647, 2147483647])
        assert result == 2147483647, f"Test 55 failed: got {result}, expected {2147483647}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = majorityElement([2147483647, 2147483647, 0, 2147483647, 0])
        assert result == 2147483647, f"Test 56 failed: got {result}, expected {2147483647}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = majorityElement([0, 2, 1, -2147483648, -2147483648, -2147483648, -2147483648])
        assert result == -2147483648, f"Test 57 failed: got {result}, expected {-2147483648}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = majorityElement([13, 13, 13, 15, 13, 17, 1000000001])
        assert result == 13, f"Test 58 failed: got {result}, expected {13}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
