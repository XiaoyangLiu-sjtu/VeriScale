# Coverage Report

Total executable lines: 25
Covered lines: 25
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def mergeSorted(a1, a2):
2: ✓     i, j = 0, 0
3: ✓     merged = []
4: ✓     while i < len(a1) and j < len(a2):
5: ✓         if a1[i] < a2[j]:
6: ✓             if not merged or merged[-1] != a1[i]:
7: ✓                 merged.append(a1[i])
8: ✓             i += 1
9: ✓         elif a1[i] > a2[j]:
10: ✓             if not merged or merged[-1] != a2[j]:
11: ✓                 merged.append(a2[j])
12: ✓             j += 1
13:           else:
14: ✓             if not merged or merged[-1] != a1[i]:
15: ✓                 merged.append(a1[i])
16: ✓             i += 1
17: ✓             j += 1
18: ✓     while i < len(a1):
19: ✓         if not merged or merged[-1] != a1[i]:
20: ✓             merged.append(a1[i])
21: ✓         i += 1
22: ✓     while j < len(a2):
23: ✓         if not merged or merged[-1] != a2[j]:
24: ✓             merged.append(a2[j])
25: ✓         j += 1
26: ✓     return merged
```

## Complete Test File

```python
def mergeSorted(a1, a2):
    i, j = 0, 0
    merged = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            if not merged or merged[-1] != a1[i]:
                merged.append(a1[i])
            i += 1
        elif a1[i] > a2[j]:
            if not merged or merged[-1] != a2[j]:
                merged.append(a2[j])
            j += 1
        else:
            if not merged or merged[-1] != a1[i]:
                merged.append(a1[i])
            i += 1
            j += 1
    while i < len(a1):
        if not merged or merged[-1] != a1[i]:
            merged.append(a1[i])
        i += 1
    while j < len(a2):
        if not merged or merged[-1] != a2[j]:
            merged.append(a2[j])
        j += 1
    return merged

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = mergeSorted([1, 3, 5], [2, 4, 6])
        assert result == [1, 2, 3, 4, 5, 6], f"Test 1 failed: got {result}, expected {[1, 2, 3, 4, 5, 6]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = mergeSorted([], [1, 2, 3])
        assert result == [1, 2, 3], f"Test 2 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = mergeSorted([1, 2, 3], [])
        assert result == [1, 2, 3], f"Test 3 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = mergeSorted([], [])
        assert result == [], f"Test 4 failed: got {result}, expected {[]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = mergeSorted([1, 1, 2], [1, 2, 2])
        assert result == [1, 1, 1, 2, 2, 2], f"Test 5 failed: got {result}, expected {[1, 1, 1, 2, 2, 2]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = mergeSorted([10, 20, 30], [5, 15, 25])
        assert result == [5, 10, 15, 20, 25, 30], f"Test 6 failed: got {result}, expected {[5, 10, 15, 20, 25, 30]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = mergeSorted([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], f"Test 7 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = mergeSorted([5, 5, 5], [5, 5, 5])
        assert result == [5, 5, 5, 5, 5, 5], f"Test 8 failed: got {result}, expected {[5, 5, 5, 5, 5, 5]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = mergeSorted([5], [5])
        assert result == [5, 5], f"Test 9 failed: got {result}, expected {[5, 5]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = mergeSorted([0, 0, 0], [0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 10 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = mergeSorted([1, 2, 2, 2, 9], [2, 2, 3, 10])
        assert result == [1, 2, 2, 2, 2, 2, 3, 9, 10], f"Test 11 failed: got {result}, expected {[1, 2, 2, 2, 2, 2, 3, 9, 10]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = mergeSorted([10, 20, 30], [10, 20, 30])
        assert result == [10, 10, 20, 20, 30, 30], f"Test 12 failed: got {result}, expected {[10, 10, 20, 20, 30, 30]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = mergeSorted([0, 5, 10, 15], [1, 1, 1, 1])
        assert result == [0, 1, 1, 1, 1, 5, 10, 15], f"Test 13 failed: got {result}, expected {[0, 1, 1, 1, 1, 5, 10, 15]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = mergeSorted([42], [1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5, 42], f"Test 14 failed: got {result}, expected {[1, 2, 3, 4, 5, 42]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = mergeSorted([1, 2, 3, 4, 5], [42])
        assert result == [1, 2, 3, 4, 5, 42], f"Test 15 failed: got {result}, expected {[1, 2, 3, 4, 5, 42]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = mergeSorted([0, 1000000], [500000, 1000000, 2000000])
        assert result == [0, 500000, 1000000, 1000000, 2000000], f"Test 16 failed: got {result}, expected {[0, 500000, 1000000, 1000000, 2000000]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = mergeSorted([7, 7, 8, 9, 9, 9], [7, 8, 8, 10])
        assert result == [7, 7, 7, 8, 8, 8, 9, 9, 9, 10], f"Test 17 failed: got {result}, expected {[7, 7, 7, 8, 8, 8, 9, 9, 9, 10]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = mergeSorted([1], [1, 1, 1, 1, 1])
        assert result == [1, 1, 1, 1, 1, 1], f"Test 18 failed: got {result}, expected {[1, 1, 1, 1, 1, 1]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = mergeSorted([1, 1, 1, 1, 1], [1])
        assert result == [1, 1, 1, 1, 1, 1], f"Test 19 failed: got {result}, expected {[1, 1, 1, 1, 1, 1]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = mergeSorted([3, 3, 3, 4], [4, 4, 5, 5, 6])
        assert result == [3, 3, 3, 4, 4, 4, 5, 5, 6], f"Test 20 failed: got {result}, expected {[3, 3, 3, 4, 4, 4, 5, 5, 6]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = mergeSorted([0, 0, 1], [1, 1, 1, 2])
        assert result == [0, 0, 1, 1, 1, 1, 2], f"Test 21 failed: got {result}, expected {[0, 0, 1, 1, 1, 1, 2]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = mergeSorted([2, 4, 6], [2, 4, 6])
        assert result == [2, 2, 4, 4, 6, 6], f"Test 22 failed: got {result}, expected {[2, 2, 4, 4, 6, 6]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = mergeSorted([999999999], [0, 999999999, 1000000000])
        assert result == [0, 999999999, 999999999, 1000000000], f"Test 23 failed: got {result}, expected {[0, 999999999, 999999999, 1000000000]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = mergeSorted([0, 1], [0, 1])
        assert result == [0, 0, 1, 1], f"Test 24 failed: got {result}, expected {[0, 0, 1, 1]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = mergeSorted([8, 9, 10, 11, 12], [1, 2])
        assert result == [1, 2, 8, 9, 10, 11, 12], f"Test 25 failed: got {result}, expected {[1, 2, 8, 9, 10, 11, 12]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = mergeSorted([1, 2], [8, 9, 10, 11, 12])
        assert result == [1, 2, 8, 9, 10, 11, 12], f"Test 26 failed: got {result}, expected {[1, 2, 8, 9, 10, 11, 12]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = mergeSorted([0, 0, 0, 1, 1, 2, 2, 2], [2, 2, 3, 3, 3])
        assert result == [0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3], f"Test 27 failed: got {result}, expected {[0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = mergeSorted([5, 10, 10, 10, 15, 20], [0, 10, 10, 30])
        assert result == [0, 5, 10, 10, 10, 10, 10, 15, 20, 30], f"Test 28 failed: got {result}, expected {[0, 5, 10, 10, 10, 10, 10, 15, 20, 30]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = mergeSorted([4], [4])
        assert result == [4, 4], f"Test 29 failed: got {result}, expected {[4, 4]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = mergeSorted([0, 2, 2, 2, 3, 100], [2, 2, 50, 100, 100])
        assert result == [0, 2, 2, 2, 2, 2, 3, 50, 100, 100, 100], f"Test 30 failed: got {result}, expected {[0, 2, 2, 2, 2, 2, 3, 50, 100, 100, 100]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = mergeSorted([3, 5], [2, 4, 6])
        assert result == [2, 3, 4, 5, 6], f"Test 31 failed: got {result}, expected {[2, 3, 4, 5, 6]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = mergeSorted([1, 3, 5], [2, 5, 6])
        assert result == [1, 2, 3, 5, 5, 6], f"Test 32 failed: got {result}, expected {[1, 2, 3, 5, 5, 6]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = mergeSorted([1, 3, 5], [2, 6])
        assert result == [1, 2, 3, 5, 6], f"Test 33 failed: got {result}, expected {[1, 2, 3, 5, 6]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = mergeSorted([1, 3, 11], [2, 4, 6])
        assert result == [1, 2, 3, 4, 6, 11], f"Test 34 failed: got {result}, expected {[1, 2, 3, 4, 6, 11]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = mergeSorted([0, 1], [1, 2, 3])
        assert result == [0, 1, 1, 2, 3], f"Test 35 failed: got {result}, expected {[0, 1, 1, 2, 3]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = mergeSorted([0, 0], [1, 2, 3])
        assert result == [0, 0, 1, 2, 3], f"Test 36 failed: got {result}, expected {[0, 0, 1, 2, 3]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = mergeSorted([0, 0, 2, 12], [1, 2, 3])
        assert result == [0, 0, 1, 2, 2, 3, 12], f"Test 37 failed: got {result}, expected {[0, 0, 1, 2, 2, 3, 12]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = mergeSorted([0], [2, 3, 8, 1000000])
        assert result == [0, 2, 3, 8, 1000000], f"Test 38 failed: got {result}, expected {[0, 2, 3, 8, 1000000]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = mergeSorted([11], [2, 3])
        assert result == [2, 3, 11], f"Test 39 failed: got {result}, expected {[2, 3, 11]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = mergeSorted([1, 2, 3], [0, 0])
        assert result == [0, 0, 1, 2, 3], f"Test 40 failed: got {result}, expected {[0, 0, 1, 2, 3]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = mergeSorted([10], [0, 0])
        assert result == [0, 0, 10], f"Test 41 failed: got {result}, expected {[0, 0, 10]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = mergeSorted([1, 2, 3, 5], [0])
        assert result == [0, 1, 2, 3, 5], f"Test 42 failed: got {result}, expected {[0, 1, 2, 3, 5]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = mergeSorted([2, 3], [0])
        assert result == [0, 2, 3], f"Test 43 failed: got {result}, expected {[0, 2, 3]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = mergeSorted([1, 2, 3], [0, 0, 0])
        assert result == [0, 0, 0, 1, 2, 3], f"Test 44 failed: got {result}, expected {[0, 0, 0, 1, 2, 3]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = mergeSorted([0], [42])
        assert result == [0, 42], f"Test 45 failed: got {result}, expected {[0, 42]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = mergeSorted([0], [0, 15])
        assert result == [0, 0, 15], f"Test 46 failed: got {result}, expected {[0, 0, 15]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = mergeSorted([0], [1000000])
        assert result == [0, 1000000], f"Test 47 failed: got {result}, expected {[0, 1000000]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = mergeSorted([1, 4], [0, 0])
        assert result == [0, 0, 1, 4], f"Test 48 failed: got {result}, expected {[0, 0, 1, 4]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = mergeSorted([0], [0])
        assert result == [0, 0], f"Test 49 failed: got {result}, expected {[0, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = mergeSorted([0], [0, 10])
        assert result == [0, 0, 10], f"Test 50 failed: got {result}, expected {[0, 0, 10]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = mergeSorted([15], [0, 0])
        assert result == [0, 0, 15], f"Test 51 failed: got {result}, expected {[0, 0, 15]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = mergeSorted([0, 0], [0])
        assert result == [0, 0, 0], f"Test 52 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = mergeSorted([0, 1, 1, 20], [1, 2, 2])
        assert result == [0, 1, 1, 1, 2, 2, 20], f"Test 53 failed: got {result}, expected {[0, 1, 1, 1, 2, 2, 20]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
