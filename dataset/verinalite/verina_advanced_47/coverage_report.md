# Coverage Report

Total executable lines: 8
Covered lines: 8
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def mergeIntervals(intervals):
2: ✓     intervals.sort(key=lambda x: x[0])
3: ✓     merged = []
4: ✓     for interval in intervals:
5: ✓         if not merged or merged[-1][1] < interval[0]:
6: ✓             merged.append(interval)
7:           else:
8: ✓             merged[-1][1] = max(merged[-1][1], interval[1])
9: ✓     return merged
```

## Complete Test File

```python
def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = mergeIntervals([(1, 3), (2, 6), (8, 10), (15, 18)])
        assert result == [(1, 6), (8, 10), (15, 18)], f"Test 1 failed: got {result}, expected {[(1, 6), (8, 10), (15, 18)]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = mergeIntervals([(1, 4), (4, 5)])
        assert result == [(1, 5)], f"Test 2 failed: got {result}, expected {[(1, 5)]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = mergeIntervals([(1, 10), (2, 3), (4, 5)])
        assert result == [(1, 10)], f"Test 3 failed: got {result}, expected {[(1, 10)]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = mergeIntervals([(1, 2), (3, 4), (5, 6)])
        assert result == [(1, 2), (3, 4), (5, 6)], f"Test 4 failed: got {result}, expected {[(1, 2), (3, 4), (5, 6)]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = mergeIntervals([(5, 6), (1, 3), (2, 4)])
        assert result == [(1, 4), (5, 6)], f"Test 5 failed: got {result}, expected {[(1, 4), (5, 6)]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = mergeIntervals([(1, 3)])
        assert result == [(1, 3)], f"Test 6 failed: got {result}, expected {[(1, 3)]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = mergeIntervals([(1, 3), (10, 12)])
        assert result == [(1, 3), (10, 12)], f"Test 7 failed: got {result}, expected {[(1, 3), (10, 12)]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = mergeIntervals([])
        assert result == [], f"Test 8 failed: got {result}, expected {[]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = mergeIntervals([(0, 0)])
        assert result == [(0, 0)], f"Test 9 failed: got {result}, expected {[(0, 0)]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = mergeIntervals([(5, 5)])
        assert result == [(5, 5)], f"Test 10 failed: got {result}, expected {[(5, 5)]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = mergeIntervals([(1, 3), (2, 6), (5, 8)])
        assert result == [(1, 8)], f"Test 11 failed: got {result}, expected {[(1, 8)]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = mergeIntervals([(-10, -5), (-7, -3), (-2, 1)])
        assert result == [(-10, -3), (-2, 1)], f"Test 12 failed: got {result}, expected {[(-10, -3), (-2, 1)]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = mergeIntervals([(-3, 0), (0, 2), (3, 5)])
        assert result == [(-3, 2), (3, 5)], f"Test 13 failed: got {result}, expected {[(-3, 2), (3, 5)]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = mergeIntervals([(2, 2), (2, 2), (2, 2)])
        assert result == [(2, 2)], f"Test 14 failed: got {result}, expected {[(2, 2)]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = mergeIntervals([(1, 2), (1, 5), (1, 3)])
        assert result == [(1, 5)], f"Test 15 failed: got {result}, expected {[(1, 5)]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = mergeIntervals([(0, 4), (2, 4), (4, 4)])
        assert result == [(0, 4)], f"Test 16 failed: got {result}, expected {[(0, 4)]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = mergeIntervals([(-1000000000, 1000000000)])
        assert result == [(-1000000000, 1000000000)], f"Test 17 failed: got {result}, expected {[(-1000000000, 1000000000)]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = mergeIntervals([(-1000000000, -999999999), (999999999, 1000000000)])
        assert result == [(-1000000000, -999999999), (999999999, 1000000000)], f"Test 18 failed: got {result}, expected {[(-1000000000, -999999999), (999999999, 1000000000)]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = mergeIntervals([(8, 10), (1, 3), (15, 18), (2, 6)])
        assert result == [(1, 6), (8, 10), (15, 18)], f"Test 19 failed: got {result}, expected {[(1, 6), (8, 10), (15, 18)]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = mergeIntervals([(1, 2), (2, 3), (3, 4), (4, 5)])
        assert result == [(1, 5)], f"Test 20 failed: got {result}, expected {[(1, 5)]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = mergeIntervals([(1, 5), (6, 8), (7, 9), (10, 12)])
        assert result == [(1, 5), (6, 9), (10, 12)], f"Test 21 failed: got {result}, expected {[(1, 5), (6, 9), (10, 12)]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = mergeIntervals([(-5, 5), (-4, -1), (0, 3)])
        assert result == [(-5, 5)], f"Test 22 failed: got {result}, expected {[(-5, 5)]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = mergeIntervals([(-1, -1), (0, 0), (1, 1)])
        assert result == [(-1, -1), (0, 0), (1, 1)], f"Test 23 failed: got {result}, expected {[(-1, -1), (0, 0), (1, 1)]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = mergeIntervals([(10, 12), (7, 9), (4, 6), (1, 3)])
        assert result == [(1, 3), (4, 6), (7, 9), (10, 12)], f"Test 24 failed: got {result}, expected {[(1, 3), (4, 6), (7, 9), (10, 12)]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = mergeIntervals([(0, 1), (1, 2), (4, 5), (5, 5), (6, 10)])
        assert result == [(0, 2), (4, 5), (6, 10)], f"Test 25 failed: got {result}, expected {[(0, 2), (4, 5), (6, 10)]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = mergeIntervals([(3, 7), (3, 7), (1, 2), (2, 3)])
        assert result == [(1, 7)], f"Test 26 failed: got {result}, expected {[(1, 7)]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = mergeIntervals([(12, 15), (-4, -4), (0, 3), (3, 3), (2, 8), (-10, -2)])
        assert result == [(-10, -2), (0, 8), (12, 15)], f"Test 27 failed: got {result}, expected {[(-10, -2), (0, 8), (12, 15)]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = mergeIntervals([(-2147483648, -2147483648), (2147483647, 2147483647)])
        assert result == [(-2147483648, -2147483648), (2147483647, 2147483647)], f"Test 28 failed: got {result}, expected {[(-2147483648, -2147483648), (2147483647, 2147483647)]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = mergeIntervals([(-2147483648, 0), (0, 2147483647)])
        assert result == [(-2147483648, 2147483647)], f"Test 29 failed: got {result}, expected {[(-2147483648, 2147483647)]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = mergeIntervals([(-9, -8), (-7, -6), (-5, -4), (-3, -2), (-1, 0)])
        assert result == [(-9, -8), (-7, -6), (-5, -4), (-3, -2), (-1, 0)], f"Test 30 failed: got {result}, expected {[(-9, -8), (-7, -6), (-5, -4), (-3, -2), (-1, 0)]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = mergeIntervals([(1, 100), (2, 90), (3, 80), (4, 70)])
        assert result == [(1, 100)], f"Test 31 failed: got {result}, expected {[(1, 100)]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = mergeIntervals([(5, 10), (10, 10), (10, 15)])
        assert result == [(5, 15)], f"Test 32 failed: got {result}, expected {[(5, 15)]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = mergeIntervals([(4, 4), (-2, 1), (2, 2), (-5, -3), (1, 3)])
        assert result == [(-5, -3), (-2, 3), (4, 4)], f"Test 33 failed: got {result}, expected {[(-5, -3), (-2, 3), (4, 4)]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = mergeIntervals([(20, 25), (5, 10), (10, 15), (15, 20)])
        assert result == [(5, 25)], f"Test 34 failed: got {result}, expected {[(5, 25)]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = mergeIntervals([(1, 2), (100, 200), (2, 3), (150, 250), (-10, -5)])
        assert result == [(-10, -5), (1, 3), (100, 250)], f"Test 35 failed: got {result}, expected {[(-10, -5), (1, 3), (100, 250)]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = mergeIntervals('')
        assert result == [], f"Test 36 failed: got {result}, expected {[]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
