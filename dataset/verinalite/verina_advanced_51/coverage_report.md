# Coverage Report

Total executable lines: 12
Covered lines: 12
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def mergeSorted(a, b):
2: ✓     i, j = 0, 0
3: ✓     merged = []
4: ✓     while i < len(a) and j < len(b):
5: ✓         if a[i] <= b[j]:
6: ✓             merged.append(a[i])
7: ✓             i += 1
8:           else:
9: ✓             merged.append(b[j])
10: ✓             j += 1
11: ✓     merged.extend(a[i:])
12: ✓     merged.extend(b[j:])
13: ✓     return merged
```

## Complete Test File

```python
def mergeSorted(a, b):
    i, j = 0, 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
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
        result = mergeSorted([1, 2], [1, 2, 3])
        assert result == [1, 1, 2, 2, 3], f"Test 2 failed: got {result}, expected {[1, 1, 2, 2, 3]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = mergeSorted([], [4, 5])
        assert result == [4, 5], f"Test 3 failed: got {result}, expected {[4, 5]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = mergeSorted([0, 3, 4], [])
        assert result == [0, 3, 4], f"Test 4 failed: got {result}, expected {[0, 3, 4]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = mergeSorted([1, 4, 6], [2, 3, 5])
        assert result == [1, 2, 3, 4, 5, 6], f"Test 5 failed: got {result}, expected {[1, 2, 3, 4, 5, 6]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = mergeSorted([-3, -1, 0], [-2, -2, 7])
        assert result == [-3, -2, -2, -1, 0, 7], f"Test 6 failed: got {result}, expected {[-3, -2, -2, -1, 0, 7]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = mergeSorted([-5, -4, -4, -1], [-3, 2, 2, 9])
        assert result == [-5, -4, -4, -3, -1, 2, 2, 9], f"Test 7 failed: got {result}, expected {[-5, -4, -4, -3, -1, 2, 2, 9]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = mergeSorted([1000000000000, 1000000000001], [-1000000000000, 0, 1000000000002])
        assert result == [-1000000000000, 0, 1000000000000, 1000000000001, 1000000000002], f"Test 8 failed: got {result}, expected {[-1000000000000, 0, 1000000000000, 1000000000001, 1000000000002]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = mergeSorted([10, 11, 12], [1, 2, 3])
        assert result == [1, 2, 3, 10, 11, 12], f"Test 9 failed: got {result}, expected {[1, 2, 3, 10, 11, 12]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = mergeSorted([1, 4, 7, 10], [2, 3, 8, 9, 11])
        assert result == [1, 2, 3, 4, 7, 8, 9, 10, 11], f"Test 10 failed: got {result}, expected {[1, 2, 3, 4, 7, 8, 9, 10, 11]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = mergeSorted([-100, -50, -50, 0, 50], [-99, -50, 50, 51])
        assert result == [-100, -99, -50, -50, -50, 0, 50, 50, 51], f"Test 11 failed: got {result}, expected {[-100, -99, -50, -50, -50, 0, 50, 50, 51]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = mergeSorted([42], [-100, -50, 0, 50, 100])
        assert result == [-100, -50, 0, 42, 50, 100], f"Test 12 failed: got {result}, expected {[-100, -50, 0, 42, 50, 100]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = mergeSorted([-100, -50, 0, 50, 100], [42])
        assert result == [-100, -50, 0, 42, 50, 100], f"Test 13 failed: got {result}, expected {[-100, -50, 0, 42, 50, 100]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = mergeSorted([3, 3, 4, 4, 4, 9], [1, 2, 2, 10])
        assert result == [1, 2, 2, 3, 3, 4, 4, 4, 9, 10], f"Test 14 failed: got {result}, expected {[1, 2, 2, 3, 3, 4, 4, 4, 9, 10]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = mergeSorted([7, 8, 9], [7, 8, 9])
        assert result == [7, 7, 8, 8, 9, 9], f"Test 15 failed: got {result}, expected {[7, 7, 8, 8, 9, 9]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = mergeSorted([-3, -3, -1, 2, 2], [-3, 0, 0, 3])
        assert result == [-3, -3, -3, -1, 0, 0, 2, 2, 3], f"Test 16 failed: got {result}, expected {[-3, -3, -3, -1, 0, 0, 2, 2, 3]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = mergeSorted([2147483647], [-2147483648])
        assert result == [-2147483648, 2147483647], f"Test 17 failed: got {result}, expected {[-2147483648, 2147483647]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = mergeSorted([-10, -5, 0, 5, 10], [-9, -4, 1, 6, 11])
        assert result == [-10, -9, -5, -4, 0, 1, 5, 6, 10, 11], f"Test 18 failed: got {result}, expected {[-10, -9, -5, -4, 0, 1, 5, 6, 10, 11]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = mergeSorted([2, 2, 2, 2, 2, 2], [1])
        assert result == [1, 2, 2, 2, 2, 2, 2], f"Test 19 failed: got {result}, expected {[1, 2, 2, 2, 2, 2, 2]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = mergeSorted([-1000000000000000000, 0, 1000000000000000000], [-999999999999999999, 1, 999999999999999999])
        assert result == [-1000000000000000000, -999999999999999999, 0, 1, 999999999999999999, 1000000000000000000], f"Test 20 failed: got {result}, expected {[-1000000000000000000, -999999999999999999, 0, 1, 999999999999999999, 1000000000000000000]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = mergeSorted([3, 5], [2, 4, 6])
        assert result == [2, 3, 4, 5, 6], f"Test 21 failed: got {result}, expected {[2, 3, 4, 5, 6]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = mergeSorted([2, 3, 5, 6], [2, 6])
        assert result == [2, 2, 3, 5, 6, 6], f"Test 22 failed: got {result}, expected {[2, 2, 3, 5, 6, 6]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = mergeSorted([1, 5], [2, 4, 6])
        assert result == [1, 2, 4, 5, 6], f"Test 23 failed: got {result}, expected {[1, 2, 4, 5, 6]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = mergeSorted([2], [1, 2, 3])
        assert result == [1, 2, 2, 3], f"Test 24 failed: got {result}, expected {[1, 2, 2, 3]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = mergeSorted([1, 2, 1000000000001], [1, 2, 3])
        assert result == [1, 1, 2, 2, 3, 1000000000001], f"Test 25 failed: got {result}, expected {[1, 1, 2, 2, 3, 1000000000001]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = mergeSorted([0], [-5])
        assert result == [-5, 0], f"Test 26 failed: got {result}, expected {[-5, 0]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = mergeSorted([9007199254740990], [5])
        assert result == [5, 9007199254740990], f"Test 27 failed: got {result}, expected {[5, 9007199254740990]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = mergeSorted([0, 3, 4], [0])
        assert result == [0, 0, 3, 4], f"Test 28 failed: got {result}, expected {[0, 0, 3, 4]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = mergeSorted([0, 3], [0])
        assert result == [0, 0, 3], f"Test 29 failed: got {result}, expected {[0, 0, 3]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = mergeSorted([0, 3, 4, 4], [0, 0])
        assert result == [0, 0, 0, 3, 4, 4], f"Test 30 failed: got {result}, expected {[0, 0, 0, 3, 4, 4]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = mergeSorted([0, 4, 6], [2, 3, 5])
        assert result == [0, 2, 3, 4, 5, 6], f"Test 31 failed: got {result}, expected {[0, 2, 3, 4, 5, 6]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = mergeSorted([4, 6], [5, 7])
        assert result == [4, 5, 6, 7], f"Test 32 failed: got {result}, expected {[4, 5, 6, 7]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = mergeSorted([6, 10], [-1000000000000, 3])
        assert result == [-1000000000000, 3, 6, 10], f"Test 33 failed: got {result}, expected {[-1000000000000, 3, 6, 10]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = mergeSorted([1, 2], [0, 4, 5])
        assert result == [0, 1, 2, 4, 5], f"Test 34 failed: got {result}, expected {[0, 1, 2, 4, 5]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = mergeSorted([100], [0])
        assert result == [0, 100], f"Test 35 failed: got {result}, expected {[0, 100]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = mergeSorted([0], [-4])
        assert result == [-4, 0], f"Test 36 failed: got {result}, expected {[-4, 0]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = mergeSorted([0], [-100, -1])
        assert result == [-100, -1, 0], f"Test 37 failed: got {result}, expected {[-100, -1, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = mergeSorted([-100, 18014398509481980], [0])
        assert result == [-100, 0, 18014398509481980], f"Test 38 failed: got {result}, expected {[-100, 0, 18014398509481980]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = mergeSorted([0, 0], [-1])
        assert result == [-1, 0, 0], f"Test 39 failed: got {result}, expected {[-1, 0, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = mergeSorted([0], [-1])
        assert result == [-1, 0], f"Test 40 failed: got {result}, expected {[-1, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = mergeSorted([5], [0])
        assert result == [0, 5], f"Test 41 failed: got {result}, expected {[0, 5]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = mergeSorted([5], [0, 1000000000000])
        assert result == [0, 5, 1000000000000], f"Test 42 failed: got {result}, expected {[0, 5, 1000000000000]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = mergeSorted([5], [0, 0])
        assert result == [0, 0, 5], f"Test 43 failed: got {result}, expected {[0, 0, 5]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = mergeSorted([1000000000001], [2])
        assert result == [2, 1000000000001], f"Test 44 failed: got {result}, expected {[2, 1000000000001]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = mergeSorted([2], [0, 0])
        assert result == [0, 0, 2], f"Test 45 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = mergeSorted([9], [2])
        assert result == [2, 9], f"Test 46 failed: got {result}, expected {[2, 9]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = mergeSorted([2], [0, 2])
        assert result == [0, 2, 2], f"Test 47 failed: got {result}, expected {[0, 2, 2]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = mergeSorted([1, 3, 5], [2, 4])
        assert result == [1, 2, 3, 4, 5], f"Test 48 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = mergeSorted([1, 1, 2, 2, 3, 1000000000000000000], [4, 4, 7])
        assert result == [1, 1, 2, 2, 3, 4, 4, 7, 1000000000000000000], f"Test 49 failed: got {result}, expected {[1, 1, 2, 2, 3, 4, 4, 7, 1000000000000000000]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = mergeSorted([-3, 6], [-2, -2, 7, 1000000000001])
        assert result == [-3, -2, -2, 6, 7, 1000000000001], f"Test 50 failed: got {result}, expected {[-3, -2, -2, 6, 7, 1000000000001]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = mergeSorted([-3, -1, 0], [-8, -2, 7, 10])
        assert result == [-8, -3, -2, -1, 0, 7, 10], f"Test 51 failed: got {result}, expected {[-8, -3, -2, -1, 0, 7, 10]}"
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
