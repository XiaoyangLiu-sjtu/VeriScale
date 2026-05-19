# Coverage Report

Total executable lines: 16
Covered lines: 16
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def hasChordIntersection(N, chords):
2: ✓     import heapq
3: ✓     new_chords = []
4: ✓     for a, b in chords:
5: ✓         if a > b:
6: ✓             a, b = b, a
7: ✓         new_chords.append((a, b))
8: ✓     new_chords.sort(key=lambda x: x[0])
9: ✓     open_heap = []
10: ✓     for c, d in new_chords:
11: ✓         while open_heap and open_heap[0] < c:
12: ✓             heapq.heappop(open_heap)
13: ✓         if open_heap and open_heap[0] < d:
14: ✓             return True
15: ✓         heapq.heappush(open_heap, d)
16: ✓     return False
```

## Complete Test File

```python
def hasChordIntersection(N, chords):
    import heapq
    new_chords = []
    for a, b in chords:
        if a > b:
            a, b = b, a
        new_chords.append((a, b))
    new_chords.sort(key=lambda x: x[0])
    open_heap = []
    for c, d in new_chords:
        while open_heap and open_heap[0] < c:
            heapq.heappop(open_heap)
        if open_heap and open_heap[0] < d:
            return True
        heapq.heappush(open_heap, d)
    return False

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = hasChordIntersection(3, [[1, 3], [4, 2], [5, 6]])
        assert result == True, f"Test 1 failed: got {result}, expected {True}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = hasChordIntersection(3, [[6, 1], [4, 3], [2, 5]])
        assert result == False, f"Test 2 failed: got {result}, expected {False}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = hasChordIntersection(4, [[2, 4], [3, 7], [8, 6], [5, 1]])
        assert result == True, f"Test 3 failed: got {result}, expected {True}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = hasChordIntersection(2, [[1, 2], [3, 4]])
        assert result == False, f"Test 4 failed: got {result}, expected {False}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = hasChordIntersection(2, [[3, 1], [4, 2]])
        assert result == True, f"Test 5 failed: got {result}, expected {True}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = hasChordIntersection(2, [[1, 3], [2, 4]])
        assert result == True, f"Test 6 failed: got {result}, expected {True}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = hasChordIntersection(2, [[4, 1], [2, 3]])
        assert result == False, f"Test 7 failed: got {result}, expected {False}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = hasChordIntersection(2, [[2, 4], [1, 3]])
        assert result == True, f"Test 8 failed: got {result}, expected {True}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = hasChordIntersection(3, [[1, 4], [2, 5], [3, 6]])
        assert result == True, f"Test 9 failed: got {result}, expected {True}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = hasChordIntersection(3, [[1, 2], [3, 4], [5, 6]])
        assert result == False, f"Test 10 failed: got {result}, expected {False}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = hasChordIntersection(3, [[1, 6], [2, 3], [4, 5]])
        assert result == False, f"Test 11 failed: got {result}, expected {False}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = hasChordIntersection(3, [[1, 3], [2, 6], [4, 5]])
        assert result == True, f"Test 12 failed: got {result}, expected {True}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = hasChordIntersection(3, [[6, 2], [1, 4], [3, 5]])
        assert result == True, f"Test 13 failed: got {result}, expected {True}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = hasChordIntersection(3, [[5, 1], [2, 4], [3, 6]])
        assert result == True, f"Test 14 failed: got {result}, expected {True}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = hasChordIntersection(4, [[1, 5], [2, 6], [3, 7], [4, 8]])
        assert result == True, f"Test 15 failed: got {result}, expected {True}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = hasChordIntersection(4, [[1, 2], [3, 4], [5, 6], [7, 8]])
        assert result == False, f"Test 16 failed: got {result}, expected {False}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = hasChordIntersection(4, [[1, 8], [2, 3], [4, 5], [6, 7]])
        assert result == False, f"Test 17 failed: got {result}, expected {False}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = hasChordIntersection(4, [[1, 4], [2, 3], [5, 8], [6, 7]])
        assert result == False, f"Test 18 failed: got {result}, expected {False}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = hasChordIntersection(4, [[1, 3], [2, 4], [5, 7], [6, 8]])
        assert result == True, f"Test 19 failed: got {result}, expected {True}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = hasChordIntersection(4, [[2, 5], [1, 4], [3, 8], [6, 7]])
        assert result == True, f"Test 20 failed: got {result}, expected {True}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = hasChordIntersection(5, [[1, 6], [2, 7], [3, 8], [4, 9], [5, 10]])
        assert result == True, f"Test 21 failed: got {result}, expected {True}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = hasChordIntersection(5, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
        assert result == False, f"Test 22 failed: got {result}, expected {False}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = hasChordIntersection(5, [[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]])
        assert result == False, f"Test 23 failed: got {result}, expected {False}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = hasChordIntersection(5, [[1, 4], [2, 9], [3, 6], [5, 8], [7, 10]])
        assert result == True, f"Test 24 failed: got {result}, expected {True}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = hasChordIntersection(5, [[10, 2], [1, 5], [3, 7], [4, 9], [6, 8]])
        assert result == True, f"Test 25 failed: got {result}, expected {True}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = hasChordIntersection(6, [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]])
        assert result == True, f"Test 26 failed: got {result}, expected {True}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = hasChordIntersection(6, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
        assert result == False, f"Test 27 failed: got {result}, expected {False}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = hasChordIntersection(6, [[1, 12], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]])
        assert result == False, f"Test 28 failed: got {result}, expected {False}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = hasChordIntersection(6, [[1, 4], [2, 11], [3, 6], [5, 8], [7, 10], [9, 12]])
        assert result == True, f"Test 29 failed: got {result}, expected {True}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = hasChordIntersection(7, [[1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14]])
        assert result == True, f"Test 30 failed: got {result}, expected {True}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = hasChordIntersection(7, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]])
        assert result == False, f"Test 31 failed: got {result}, expected {False}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = hasChordIntersection(7, [[14, 1], [2, 5], [3, 8], [4, 11], [6, 9], [7, 12], [10, 13]])
        assert result == True, f"Test 32 failed: got {result}, expected {True}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = hasChordIntersection(8, [[1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [8, 16]])
        assert result == True, f"Test 33 failed: got {result}, expected {True}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = hasChordIntersection(8, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]])
        assert result == False, f"Test 34 failed: got {result}, expected {False}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = hasChordIntersection(8, [[1, 16], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15]])
        assert result == False, f"Test 35 failed: got {result}, expected {False}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = hasChordIntersection(9, [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18]])
        assert result == True, f"Test 36 failed: got {result}, expected {True}"
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
