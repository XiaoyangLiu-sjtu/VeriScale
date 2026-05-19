# Coverage Report

Total executable lines: 12
Covered lines: 12
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def SlopeSearch(a, key):
2: ✓     rows = len(a)
3: ✓     cols = len(a[0])
4: ✓     i = 0
5: ✓     j = cols - 1
6: ✓     while i < rows and j >= 0:
7: ✓         if a[i][j] == key:
8: ✓             return (i, j)
9: ✓         elif a[i][j] > key:
10: ✓             j -= 1
11:           else:
12: ✓             i += 1
13: ✓     return (-1, -1)
```

## Complete Test File

```python
def SlopeSearch(a, key):
    rows = len(a)
    cols = len(a[0])
    i = 0
    j = cols - 1
    while i < rows and j >= 0:
        if a[i][j] == key:
            return (i, j)
        elif a[i][j] > key:
            j -= 1
        else:
            i += 1
    return (-1, -1)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = SlopeSearch([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5)
        assert result == (1, 1), f"Test 1 failed: got {result}, expected {(1, 1)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = SlopeSearch([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)
        assert result == (0, 2), f"Test 2 failed: got {result}, expected {(0, 2)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = SlopeSearch([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10)
        assert result == (-1, -1), f"Test 3 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = SlopeSearch([[1, 2, 3, 4]], 4)
        assert result == (0, 3), f"Test 4 failed: got {result}, expected {(0, 3)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = SlopeSearch([[1], [2], [3], [4]], 3)
        assert result == (2, 0), f"Test 5 failed: got {result}, expected {(2, 0)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = SlopeSearch([[5]], 5)
        assert result == (0, 0), f"Test 6 failed: got {result}, expected {(0, 0)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = SlopeSearch([[1, 2, 3, 4, 5]], 1)
        assert result == (0, 0), f"Test 7 failed: got {result}, expected {(0, 0)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = SlopeSearch([[1, 2, 3, 4, 5]], 5)
        assert result == (0, 4), f"Test 8 failed: got {result}, expected {(0, 4)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = SlopeSearch([[1, 1, 1, 2, 2]], 2)
        assert result == (0, 4), f"Test 9 failed: got {result}, expected {(0, 4)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = SlopeSearch([[1], [3], [5], [7], [9]], 5)
        assert result == (2, 0), f"Test 10 failed: got {result}, expected {(2, 0)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = SlopeSearch([[1], [3], [5], [7], [9]], 6)
        assert result == (-1, -1), f"Test 11 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = SlopeSearch([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0)
        assert result == (-1, -1), f"Test 12 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = SlopeSearch([[1, 2, 2], [2, 2, 3], [2, 3, 4]], 2)
        assert result == (0, 2), f"Test 13 failed: got {result}, expected {(0, 2)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = SlopeSearch([[-5, -3, 0, 2], [-4, -1, 1, 3], [-2, 0, 2, 4]], -1)
        assert result == (1, 1), f"Test 14 failed: got {result}, expected {(1, 1)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = SlopeSearch([[-5, -3, 0, 2], [-4, -1, 1, 3], [-2, 0, 2, 4]], -6)
        assert result == (-1, -1), f"Test 15 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = SlopeSearch([[7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7]], 7)
        assert result == (0, 2), f"Test 16 failed: got {result}, expected {(0, 2)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = SlopeSearch([[7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7]], 8)
        assert result == (-1, -1), f"Test 17 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = SlopeSearch([[-1000000000000, 0], [1000000000000, 1000000000001]], 1000000000001)
        assert result == (1, 1), f"Test 18 failed: got {result}, expected {(1, 1)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = SlopeSearch([[-1000000000000, 0], [1000000000000, 1000000000001]], -1000000000001)
        assert result == (-1, -1), f"Test 19 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = SlopeSearch([[1, 2, 2, 3], [2, 3, 4, 5], [2, 4, 6, 7], [3, 5, 7, 8]], 6)
        assert result == (2, 2), f"Test 20 failed: got {result}, expected {(2, 2)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = SlopeSearch([[1, 2, 2, 3], [2, 3, 4, 5], [2, 4, 6, 7], [3, 5, 7, 8]], 9)
        assert result == (-1, -1), f"Test 21 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = SlopeSearch([[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]], 7)
        assert result == (1, 3), f"Test 22 failed: got {result}, expected {(1, 3)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = SlopeSearch([[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]], 10)
        assert result == (-1, -1), f"Test 23 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = SlopeSearch([[-3, 0], [-2, 1], [-1, 2], [0, 3], [1, 4]], 0)
        assert result == (0, 1), f"Test 24 failed: got {result}, expected {(0, 1)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = SlopeSearch([[-3, 0], [-2, 1], [-1, 2], [0, 3], [1, 4]], 5)
        assert result == (-1, -1), f"Test 25 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = SlopeSearch([[-10, -5, 0], [-8, -3, 2], [-6, -1, 4]], -1)
        assert result == (2, 1), f"Test 26 failed: got {result}, expected {(2, 1)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = SlopeSearch([[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]], 11)
        assert result == (5, 5), f"Test 27 failed: got {result}, expected {(5, 5)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = SlopeSearch([[1, 1, 2, 2, 3], [1, 2, 2, 3, 4], [2, 2, 3, 4, 4]], 3)
        assert result == (0, 4), f"Test 28 failed: got {result}, expected {(0, 4)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = SlopeSearch([[-1], [0]], 0)
        assert result == (1, 0), f"Test 29 failed: got {result}, expected {(1, 0)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = SlopeSearch([[-9007199254740990, -10, 0], [-9007199254740989, -9, 1], [-9007199254740988, -8, 2]], -9007199254740989)
        assert result == (1, 0), f"Test 30 failed: got {result}, expected {(1, 0)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = SlopeSearch([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 7)
        assert result == (2, 0), f"Test 31 failed: got {result}, expected {(2, 0)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = SlopeSearch([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9)
        assert result == (2, 2), f"Test 32 failed: got {result}, expected {(2, 2)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = SlopeSearch([[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]], 5)
        assert result == (1, 2), f"Test 33 failed: got {result}, expected {(1, 2)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = SlopeSearch([[1, 2, 3, 4, 5]], 2)
        assert result == (0, 1), f"Test 34 failed: got {result}, expected {(0, 1)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = SlopeSearch([[1, 2, 2], [2, 2, 3], [2, 3, 4]], 4)
        assert result == (2, 2), f"Test 35 failed: got {result}, expected {(2, 2)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = SlopeSearch([[1, 1, 2, 2, 3], [1, 2, 2, 3, 4], [2, 2, 3, 4, 4]], 1)
        assert result == (0, 1), f"Test 36 failed: got {result}, expected {(0, 1)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = SlopeSearch([[-5, -3, 0, 2], [-4, -1, 1, 3], [-2, 0, 2, 4]], 0)
        assert result == (0, 2), f"Test 37 failed: got {result}, expected {(0, 2)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = SlopeSearch([[-5, -3, 0, 2], [-4, -1, 1, 3], [-2, 0, 2, 4]], -4)
        assert result == (1, 0), f"Test 38 failed: got {result}, expected {(1, 0)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = SlopeSearch([[-1000000000000, 0], [1000000000000, 1000000000001]], 0)
        assert result == (0, 1), f"Test 39 failed: got {result}, expected {(0, 1)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = SlopeSearch([[1, 2, 2, 3], [2, 3, 4, 5], [2, 4, 6, 7], [3, 5, 7, 8]], 7)
        assert result == (2, 3), f"Test 40 failed: got {result}, expected {(2, 3)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = SlopeSearch([[1, 2, 2, 3], [2, 3, 4, 5], [2, 4, 6, 7], [3, 5, 7, 8]], 5)
        assert result == (1, 3), f"Test 41 failed: got {result}, expected {(1, 3)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = SlopeSearch([[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]], 8)
        assert result == (0, 4), f"Test 42 failed: got {result}, expected {(0, 4)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = SlopeSearch([[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]], 9)
        assert result == (1, 4), f"Test 43 failed: got {result}, expected {(1, 4)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = SlopeSearch([[-3, 0], [-2, 1], [-1, 2], [0, 3], [1, 4]], -2)
        assert result == (1, 0), f"Test 44 failed: got {result}, expected {(1, 0)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = SlopeSearch([[-3, 0], [-2, 1], [-1, 2], [0, 3], [1, 4]], 4)
        assert result == (4, 1), f"Test 45 failed: got {result}, expected {(4, 1)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = SlopeSearch([[-10, -5, 0], [-8, -3, 2], [-6, -1, 4]], 0)
        assert result == (0, 2), f"Test 46 failed: got {result}, expected {(0, 2)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = SlopeSearch([[-10, -5, 0], [-8, -3, 2], [-6, -1, 4]], -8)
        assert result == (1, 0), f"Test 47 failed: got {result}, expected {(1, 0)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = SlopeSearch([[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]], 2)
        assert result == (0, 1), f"Test 48 failed: got {result}, expected {(0, 1)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = SlopeSearch([[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]], 10)
        assert result == (4, 5), f"Test 49 failed: got {result}, expected {(4, 5)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = SlopeSearch([[-9007199254740990, -10, 0], [-9007199254740989, -9, 1], [-9007199254740988, -8, 2]], 0)
        assert result == (0, 2), f"Test 50 failed: got {result}, expected {(0, 2)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
