# Coverage Report

Total executable lines: 25
Covered lines: 25
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def maxCoverageAfterRemovingOne(intervals):
2: ✓     n = len(intervals)
3: ✓     events = []
4: ✓     for i, (start, end) in enumerate(intervals):
5: ✓         events.append((start, 1, i))
6: ✓         events.append((end, -1, i))
7: ✓     events.sort(key=lambda x: (x[0], -x[1]))
8: ✓     total = 0
9: ✓     unique = [0] * n
10: ✓     active = set()
11: ✓     last_time = events[0][0]
12: ✓     for time, typ, idx in events:
13: ✓         if time > last_time:
14: ✓             duration = time - last_time
15: ✓             if active:
16: ✓                 total += duration
17: ✓             if len(active) == 1:
18:                   # Only one interval active, add to its unique coverage.
19: ✓                 guard = next(iter(active))
20: ✓                 unique[guard] += duration
21: ✓             last_time = time
22: ✓         if typ == 1:
23: ✓             active.add(idx)
24:           else:
25: ✓             active.remove(idx)
26: ✓     best = total - min(unique)
27: ✓     return best
```

## Complete Test File

```python
def maxCoverageAfterRemovingOne(intervals):
    n = len(intervals)
    events = []
    for i, (start, end) in enumerate(intervals):
        events.append((start, 1, i))
        events.append((end, -1, i))
    events.sort(key=lambda x: (x[0], -x[1]))
    total = 0
    unique = [0] * n
    active = set()
    last_time = events[0][0]
    for time, typ, idx in events:
        if time > last_time:
            duration = time - last_time
            if active:
                total += duration
            if len(active) == 1:
                # Only one interval active, add to its unique coverage.
                guard = next(iter(active))
                unique[guard] += duration
            last_time = time
        if typ == 1:
            active.add(idx)
        else:
            active.remove(idx)
    best = total - min(unique)
    return best

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = maxCoverageAfterRemovingOne([(1, 3), (2, 5), (6, 8)])
        assert result == 5, f"Test 1 failed: got {result}, expected {5}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = maxCoverageAfterRemovingOne([(1, 4), (2, 6), (8, 10), (9, 12)])
        assert result == 8, f"Test 2 failed: got {result}, expected {8}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = maxCoverageAfterRemovingOne([(1, 2), (2, 3), (3, 4)])
        assert result == 2, f"Test 3 failed: got {result}, expected {2}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = maxCoverageAfterRemovingOne([(1, 10), (2, 3), (4, 5)])
        assert result == 9, f"Test 4 failed: got {result}, expected {9}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = maxCoverageAfterRemovingOne([(5, 6), (1, 2), (3, 4)])
        assert result == 2, f"Test 5 failed: got {result}, expected {2}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = maxCoverageAfterRemovingOne([(2, 5), (3, 4)])
        assert result == 3, f"Test 6 failed: got {result}, expected {3}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = maxCoverageAfterRemovingOne([(1, 10), (2, 3), (4, 5), (6, 7)])
        assert result == 9, f"Test 7 failed: got {result}, expected {9}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = maxCoverageAfterRemovingOne([(10, 20), (1, 2), (3, 15)])
        assert result == 17, f"Test 8 failed: got {result}, expected {17}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = maxCoverageAfterRemovingOne([(100, 200), (150, 250), (300, 400)])
        assert result == 200, f"Test 9 failed: got {result}, expected {200}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = maxCoverageAfterRemovingOne([(0, 2), (1, 3), (2, 4), (3, 5)])
        assert result == 5, f"Test 10 failed: got {result}, expected {5}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = maxCoverageAfterRemovingOne([(5, 5), (0, 10)])
        assert result == 10, f"Test 11 failed: got {result}, expected {10}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = maxCoverageAfterRemovingOne([(0, 10), (5, 5)])
        assert result == 10, f"Test 12 failed: got {result}, expected {10}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = maxCoverageAfterRemovingOne([(1, 1000000), (2, 999999), (500000, 500000)])
        assert result == 999999, f"Test 13 failed: got {result}, expected {999999}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = maxCoverageAfterRemovingOne([(8, 12), (1, 3), (4, 6), (7, 10)])
        assert result == 8, f"Test 14 failed: got {result}, expected {8}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = maxCoverageAfterRemovingOne([(3, 8), (1, 2), (9, 10), (2, 9)])
        assert result == 9, f"Test 15 failed: got {result}, expected {9}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = maxCoverageAfterRemovingOne([(0, 0), (0, 1), (1, 1)])
        assert result == 1, f"Test 16 failed: got {result}, expected {1}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = maxCoverageAfterRemovingOne([(6, 9), (2, 4), (4, 6), (9, 12)])
        assert result == 8, f"Test 17 failed: got {result}, expected {8}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = maxCoverageAfterRemovingOne([(1, 5), (1, 5), (2, 6), (0, 7)])
        assert result == 7, f"Test 18 failed: got {result}, expected {7}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = maxCoverageAfterRemovingOne([(0, 3), (3, 3), (3, 6)])
        assert result == 6, f"Test 19 failed: got {result}, expected {6}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = maxCoverageAfterRemovingOne([(2, 2), (2, 8), (8, 8), (1, 9)])
        assert result == 8, f"Test 20 failed: got {result}, expected {8}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = maxCoverageAfterRemovingOne([(4, 10), (10, 15), (15, 20), (0, 25)])
        assert result == 25, f"Test 21 failed: got {result}, expected {25}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = maxCoverageAfterRemovingOne([(0, 100), (20, 30), (30, 40), (40, 90), (90, 100)])
        assert result == 100, f"Test 22 failed: got {result}, expected {100}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
