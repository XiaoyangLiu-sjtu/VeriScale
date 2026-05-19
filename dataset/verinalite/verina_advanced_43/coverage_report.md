# Coverage Report

Total executable lines: 16
Covered lines: 16
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def maxStrength(nums):
2: ✓     from math import prod
3: ✓     if len(nums) == 1:
4: ✓         return nums[0]
5: ✓     pos = [x for x in nums if x > 0]
6: ✓     neg = [x for x in nums if x < 0]
7:       # Build candidate subset if possible.
8: ✓     candidate_product = None
9: ✓     if pos or len(neg) >= 2:
10: ✓         neg_sorted = sorted(neg, key=abs)
11: ✓         if len(neg_sorted) % 2 == 1:
12: ✓             neg_sorted = neg_sorted[:-1]
13: ✓         subset = pos + neg_sorted
14: ✓         if subset:
15: ✓             candidate_product = prod(subset)
16: ✓     candidate_product = candidate_product if candidate_product is not None else float('-inf')
17: ✓     return max(candidate_product, max(nums))
```

## Complete Test File

```python
def maxStrength(nums):
    from math import prod
    if len(nums) == 1:
        return nums[0]
    pos = [x for x in nums if x > 0]
    neg = [x for x in nums if x < 0]
    # Build candidate subset if possible.
    candidate_product = None
    if pos or len(neg) >= 2:
        neg_sorted = sorted(neg, key=abs)
        if len(neg_sorted) % 2 == 1:
            neg_sorted = neg_sorted[:-1]
        subset = pos + neg_sorted
        if subset:
            candidate_product = prod(subset)
    candidate_product = candidate_product if candidate_product is not None else float('-inf')
    return max(candidate_product, max(nums))

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = maxStrength([-2])
        assert result == -2, f"Test 1 failed: got {result}, expected {-2}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = maxStrength([3, -1, -5, 2, 5, -9])
        assert result == 1350, f"Test 2 failed: got {result}, expected {1350}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = maxStrength([-4, -5, -4])
        assert result == 20, f"Test 3 failed: got {result}, expected {20}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = maxStrength([0, -3, 4])
        assert result == 4, f"Test 4 failed: got {result}, expected {4}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = maxStrength([1, -1, -1])
        assert result == 1, f"Test 5 failed: got {result}, expected {1}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = maxStrength([-2, -1, 0])
        assert result == 2, f"Test 6 failed: got {result}, expected {2}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = maxStrength([-2, 0, 0, -6, 6])
        assert result == 72, f"Test 7 failed: got {result}, expected {72}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = maxStrength([-9, 0, 2])
        assert result == 2, f"Test 8 failed: got {result}, expected {2}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = maxStrength([0, 0, -4294967296, -2])
        assert result == 8589934592, f"Test 9 failed: got {result}, expected {8589934592}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = maxStrength([0, 5, 2, -5, -1, 3])
        assert result == 150, f"Test 10 failed: got {result}, expected {150}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = maxStrength([-1, -5, 2, 5, 5, 0, 0, 0])
        assert result == 250, f"Test 11 failed: got {result}, expected {250}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = maxStrength([-4, -5, -4, -2147483648, -100000, 0])
        assert result == 4294967296000000, f"Test 12 failed: got {result}, expected {4294967296000000}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = maxStrength([-8, -6, -4, -3, 0])
        assert result == 576, f"Test 13 failed: got {result}, expected {576}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = maxStrength([2147483647, -4, -5, -4])
        assert result == 42949672940, f"Test 14 failed: got {result}, expected {42949672940}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = maxStrength([4, -3, 0, 0, -2])
        assert result == 24, f"Test 15 failed: got {result}, expected {24}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = maxStrength([0, 4, 0])
        assert result == 4, f"Test 16 failed: got {result}, expected {4}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = maxStrength([4, -1, -100000, 0])
        assert result == 400000, f"Test 17 failed: got {result}, expected {400000}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = maxStrength([0, -1, -1])
        assert result == 1, f"Test 18 failed: got {result}, expected {1}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = maxStrength([1, -1, -1, 0])
        assert result == 1, f"Test 19 failed: got {result}, expected {1}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = maxStrength([-1, 1, 0])
        assert result == 1, f"Test 20 failed: got {result}, expected {1}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = maxStrength([-1, -1, 0])
        assert result == 1, f"Test 21 failed: got {result}, expected {1}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = maxStrength([8, 0, 9])
        assert result == 72, f"Test 22 failed: got {result}, expected {72}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = maxStrength([5, -10])
        assert result == 5, f"Test 23 failed: got {result}, expected {5}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = maxStrength([0, -1, -1])
        assert result == 1, f"Test 24 failed: got {result}, expected {1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = maxStrength([-2, -4])
        assert result == 8, f"Test 25 failed: got {result}, expected {8}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = maxStrength([-2, -3, 1, 1, 0])
        assert result == 6, f"Test 26 failed: got {result}, expected {6}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = maxStrength([-2, -3, 0, -7, -1, 0])
        assert result == 42, f"Test 27 failed: got {result}, expected {42}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = maxStrength([0, 4, 0])
        assert result == 4, f"Test 28 failed: got {result}, expected {4}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = maxStrength([0, -3, -2, 0, -4294967296])
        assert result == 12884901888, f"Test 29 failed: got {result}, expected {12884901888}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = maxStrength([0, -3, -1, 0, -2147483648])
        assert result == 6442450944, f"Test 30 failed: got {result}, expected {6442450944}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = maxStrength([0, -2, -3, -4, 0])
        assert result == 12, f"Test 31 failed: got {result}, expected {12}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = maxStrength([-1, -2, -18, 0])
        assert result == 36, f"Test 32 failed: got {result}, expected {36}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = maxStrength([7, -9, 5, 2, -5, -1, 3, 2147483646, 0])
        assert result == 20293720454700, f"Test 33 failed: got {result}, expected {20293720454700}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = maxStrength([0, -9, 5, 2, -5, 3])
        assert result == 1350, f"Test 34 failed: got {result}, expected {1350}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = maxStrength([0, -2147483648, 0, -1, 0])
        assert result == 2147483648, f"Test 35 failed: got {result}, expected {2147483648}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = maxStrength([1, -1, -1, 0])
        assert result == 1, f"Test 36 failed: got {result}, expected {1}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = maxStrength([-1, 1, 0])
        assert result == 1, f"Test 37 failed: got {result}, expected {1}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = maxStrength([10, 0, 10, 0, 10])
        assert result == 1000, f"Test 38 failed: got {result}, expected {1000}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = maxStrength([10, -18, -10, 0, 10, 3, 0, -10])
        assert result == 54000, f"Test 39 failed: got {result}, expected {54000}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = maxStrength([-10, 0, 10, 2, 0])
        assert result == 20, f"Test 40 failed: got {result}, expected {20}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = maxStrength([10, -9, -10, 0, 10])
        assert result == 9000, f"Test 41 failed: got {result}, expected {9000}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = maxStrength([2, -2147483648, 2, 2, 2])
        assert result == 16, f"Test 42 failed: got {result}, expected {16}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = maxStrength([2, 2, 2, 2, 0, -7])
        assert result == 16, f"Test 43 failed: got {result}, expected {16}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = maxStrength([-2, -2, -2, -2, 0, -99999])
        assert result == 799992, f"Test 44 failed: got {result}, expected {799992}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = maxStrength([-2, -1, 0])
        assert result == 2, f"Test 45 failed: got {result}, expected {2}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = maxStrength([0, 0, -1, -99999])
        assert result == 99999, f"Test 46 failed: got {result}, expected {99999}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = maxStrength([9, -8, 7, -6, -4, 3, -2, 1, 0])
        assert result == 72576, f"Test 47 failed: got {result}, expected {72576}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = maxStrength([-9, 8, -7, 6, 6, -3, 2, -1, 0])
        assert result == 108864, f"Test 48 failed: got {result}, expected {108864}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = maxStrength([-100000, 1, 0, -1, 2, 0])
        assert result == 200000, f"Test 49 failed: got {result}, expected {200000}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = maxStrength([-1, -1, 0])
        assert result == 1, f"Test 50 failed: got {result}, expected {1}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = maxStrength([-1, 0, -1, 0, -1, 0, -100002, 200002])
        assert result == 20000600004, f"Test 51 failed: got {result}, expected {20000600004}"
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
