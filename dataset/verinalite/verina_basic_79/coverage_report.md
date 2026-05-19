# Coverage Report

Total executable lines: 10
Covered lines: 10
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def onlineMax(a, x):
2: ✓     m = max(a[:x])
3: ✓     p = None
4: ✓     for i in range(x, len(a)):
5: ✓         if a[i] > m:
6: ✓             p = i
7: ✓             break
8: ✓     if p is None:
9: ✓         p = len(a) - 1
10: ✓     return (m, p)
```

## Complete Test File

```python
def onlineMax(a, x):
    m = max(a[:x])
    p = None
    for i in range(x, len(a)):
        if a[i] > m:
            p = i
            break
    if p is None:
        p = len(a) - 1
    return (m, p)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = onlineMax([3, 7, 5, 2, 9], 3)
        assert result == (7, 4), f"Test 1 failed: got {result}, expected {(7, 4)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = onlineMax([10, 10, 5, 1], 2)
        assert result == (10, 3), f"Test 2 failed: got {result}, expected {(10, 3)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = onlineMax([1, 3, 3, 3, 1], 2)
        assert result == (3, 4), f"Test 3 failed: got {result}, expected {(3, 4)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = onlineMax([5, 4, 4, 6, 2], 2)
        assert result == (5, 3), f"Test 4 failed: got {result}, expected {(5, 3)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = onlineMax([2, 8, 7, 7, 7], 3)
        assert result == (8, 4), f"Test 5 failed: got {result}, expected {(8, 4)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = onlineMax([100, 50, 1, 2, 3], 2)
        assert result == (100, 4), f"Test 6 failed: got {result}, expected {(100, 4)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = onlineMax([1, 10, 5, 15, 20], 1)
        assert result == (1, 1), f"Test 7 failed: got {result}, expected {(1, 1)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = onlineMax([8, 6, 7, 5, 3, 0, 9], 5)
        assert result == (8, 6), f"Test 8 failed: got {result}, expected {(8, 6)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = onlineMax([100, -100, 50, -50, 200], 2)
        assert result == (100, 4), f"Test 9 failed: got {result}, expected {(100, 4)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = onlineMax([-1, 0, -1, 0, -1, 0], 3)
        assert result == (0, 5), f"Test 10 failed: got {result}, expected {(0, 5)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = onlineMax([29, 23, 19, 17, 13, 11], 2)
        assert result == (29, 5), f"Test 11 failed: got {result}, expected {(29, 5)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = onlineMax([3, 7, 5, 2, 9], 4)
        assert result == (7, 4), f"Test 12 failed: got {result}, expected {(7, 4)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = onlineMax([3, 7, 5, 2, 9, 10], 2)
        assert result == (7, 4), f"Test 13 failed: got {result}, expected {(7, 4)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = onlineMax([10, 5, 1, 0], 2)
        assert result == (10, 3), f"Test 14 failed: got {result}, expected {(10, 3)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = onlineMax([0, 0, 0, 200, 1, 5, 10, 10], 2)
        assert result == (0, 3), f"Test 15 failed: got {result}, expected {(0, 3)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = onlineMax([1, 3, 3, 3, 2147483646], 2)
        assert result == (3, 4), f"Test 16 failed: got {result}, expected {(3, 4)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = onlineMax([0, 5, 4, 4, 6, 0], 2)
        assert result == (5, 4), f"Test 17 failed: got {result}, expected {(5, 4)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = onlineMax([5, 4, 4, 6, 2, 11], 2)
        assert result == (5, 3), f"Test 18 failed: got {result}, expected {(5, 3)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = onlineMax([5, 4, 4, 6, 2, 8], 2)
        assert result == (5, 3), f"Test 19 failed: got {result}, expected {(5, 3)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = onlineMax([0, 2, 6, 4, 0, 5], 2)
        assert result == (2, 2), f"Test 20 failed: got {result}, expected {(2, 2)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = onlineMax([2, 8, 7, 7, 7, 17, 0, 0], 3)
        assert result == (8, 5), f"Test 21 failed: got {result}, expected {(8, 5)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = onlineMax([1, 10, 5, 15, 20], 2)
        assert result == (10, 3), f"Test 22 failed: got {result}, expected {(10, 3)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = onlineMax([-3, -2, -1, -100, 23, 34], 2)
        assert result == (-2, 2), f"Test 23 failed: got {result}, expected {(-2, 2)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = onlineMax([3, 2, 1, 9, 4, 19, 99], 4)
        assert result == (9, 5), f"Test 24 failed: got {result}, expected {(9, 5)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = onlineMax([4, 9, 1, 2, 3, 29], 2)
        assert result == (9, 5), f"Test 25 failed: got {result}, expected {(9, 5)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = onlineMax([3, 2, 1, 9, 4], 2)
        assert result == (3, 3), f"Test 26 failed: got {result}, expected {(3, 3)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = onlineMax([4, 11, 1, 2, 3], 2)
        assert result == (11, 4), f"Test 27 failed: got {result}, expected {(11, 4)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = onlineMax([8, 10, 10, 10, 10], 2)
        assert result == (10, 4), f"Test 28 failed: got {result}, expected {(10, 4)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = onlineMax([1, 3, 2, 4, 0, 118], 2)
        assert result == (3, 3), f"Test 29 failed: got {result}, expected {(3, 3)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = onlineMax([0, 4, 2, 3, 1, 100], 2)
        assert result == (4, 5), f"Test 30 failed: got {result}, expected {(4, 5)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = onlineMax([8, 6, 8, 5, 3, 0, 9], 5)
        assert result == (8, 6), f"Test 31 failed: got {result}, expected {(8, 6)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = onlineMax([-4, -5, -5, -5, 0, 0], 4)
        assert result == (-4, 4), f"Test 32 failed: got {result}, expected {(-4, 4)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = onlineMax([100, -100, 50, -50, 200], 3)
        assert result == (100, 4), f"Test 33 failed: got {result}, expected {(100, 4)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = onlineMax([200, -50, 50, -100, 100], 2)
        assert result == (200, 4), f"Test 34 failed: got {result}, expected {(200, 4)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = onlineMax([0, 6, 2, 9, 5, 1, 4, 1, 3], 7)
        assert result == (9, 8), f"Test 35 failed: got {result}, expected {(9, 8)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = onlineMax([6, 2, 9, 5, 1, 4, 1, 3], 6)
        assert result == (9, 7), f"Test 36 failed: got {result}, expected {(9, 7)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = onlineMax([9, 8, 7, 6, 5, 17, 0], 4)
        assert result == (9, 5), f"Test 37 failed: got {result}, expected {(9, 5)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = onlineMax([-1, 0, -1, 0, -1, 0], 4)
        assert result == (0, 5), f"Test 38 failed: got {result}, expected {(0, 5)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = onlineMax([2147483646, 0, -2147483648, 2147483647], 2)
        assert result == (2147483646, 3), f"Test 39 failed: got {result}, expected {(2147483646, 3)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = onlineMax([3, -2147483648, 0, 2147483646], 2)
        assert result == (3, 3), f"Test 40 failed: got {result}, expected {(3, 3)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = onlineMax([0, 60, -50, 40, -30, 20, -10], 4)
        assert result == (60, 6), f"Test 41 failed: got {result}, expected {(60, 6)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = onlineMax([-10, 20, -30, 40, -50, 60], 2)
        assert result == (20, 3), f"Test 42 failed: got {result}, expected {(20, 3)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = onlineMax([6, 1, 2, 3, 4, 5, 0], 3)
        assert result == (6, 6), f"Test 43 failed: got {result}, expected {(6, 6)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = onlineMax([6, 1, 2, 3, 4, 5, 0], 2)
        assert result == (6, 6), f"Test 44 failed: got {result}, expected {(6, 6)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = onlineMax([0, 5, 4, 3, 2, 1, 6, 0], 4)
        assert result == (5, 6), f"Test 45 failed: got {result}, expected {(5, 6)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = onlineMax([0, 0, 0, 0, 1, 0, 60], 1)
        assert result == (0, 4), f"Test 46 failed: got {result}, expected {(0, 4)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = onlineMax([13, 19, 23, 29, 0], 2)
        assert result == (19, 2), f"Test 47 failed: got {result}, expected {(19, 2)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = onlineMax([11, 13, 17, 19, 23, 29], 3)
        assert result == (17, 3), f"Test 48 failed: got {result}, expected {(17, 3)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = onlineMax([11, 13, 17, 19, 23, 29], 4)
        assert result == (19, 4), f"Test 49 failed: got {result}, expected {(19, 4)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = onlineMax([29, 23, 19, 17, 13, 11, 11], 2)
        assert result == (29, 6), f"Test 50 failed: got {result}, expected {(29, 6)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = onlineMax([29, 23, 19, 17, 13, 11, 12], 2)
        assert result == (29, 6), f"Test 51 failed: got {result}, expected {(29, 6)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = onlineMax([0, 13, 11, 13, 17, 19, 23, 0], 2)
        assert result == (13, 4), f"Test 52 failed: got {result}, expected {(13, 4)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = onlineMax([29, 23, 19, 16, 13, 11, 2, 51, 0], 2)
        assert result == (29, 7), f"Test 53 failed: got {result}, expected {(29, 7)}"
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
