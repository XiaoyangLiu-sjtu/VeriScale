# Coverage Report

Total executable lines: 7
Covered lines: 7
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def task_code(sequence):
2: ✓     cur = sequence[0]
3: ✓     maxSoFar = sequence[0]
4: ✓     for num in sequence[1:]:
5: ✓         cur = max(num, cur + num)
6: ✓         maxSoFar = max(maxSoFar, cur)
7: ✓     return maxSoFar
```

## Complete Test File

```python
def task_code(sequence):
    cur = sequence[0]
    maxSoFar = sequence[0]
    for num in sequence[1:]:
        cur = max(num, cur + num)
        maxSoFar = max(maxSoFar, cur)
    return maxSoFar

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = task_code([10, -4, 3, 1, 5, 6, -35, 12, 21, -1])
        assert result == 33, f"Test 1 failed: got {result}, expected {33}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = task_code([2, 1, -4, 3, 4, -4, 6, 5, -5, 1])
        assert result == 14, f"Test 2 failed: got {result}, expected {14}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = task_code([-1, -2, -3, -4, -5])
        assert result == -1, f"Test 3 failed: got {result}, expected {-1}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = task_code([7])
        assert result == 7, f"Test 4 failed: got {result}, expected {7}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = task_code([1, 2, 3, 4, 5])
        assert result == 15, f"Test 5 failed: got {result}, expected {15}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = task_code([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        assert result == 6, f"Test 6 failed: got {result}, expected {6}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = task_code([1, -2, 3, 10, -4, 7, 2, -5])
        assert result == 18, f"Test 7 failed: got {result}, expected {18}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = task_code([0, -1, 2, -1, 2, -1, 0])
        assert result == 3, f"Test 8 failed: got {result}, expected {3}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = task_code([50, -100, 60, -10, 70, -5])
        assert result == 120, f"Test 9 failed: got {result}, expected {120}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = task_code([-5, -1, -8, -9])
        assert result == -1, f"Test 10 failed: got {result}, expected {-1}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = task_code([10, -4, 3, 5, 6, -35, 12, 21, -1])
        assert result == 33, f"Test 11 failed: got {result}, expected {33}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = task_code([10, -4, 3, 1, 6, -35, 12, 21, -1, 0, 0, -16])
        assert result == 33, f"Test 12 failed: got {result}, expected {33}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = task_code([-1, 21, 12, -35, 6, 5, 1, 3, 10])
        assert result == 33, f"Test 13 failed: got {result}, expected {33}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = task_code([10, -4, 3, 1, 5, 6, -35, 12, 21])
        assert result == 33, f"Test 14 failed: got {result}, expected {33}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = task_code([10, -4, 3, 1, 5, 6, -35, 12, 21, -1, 0])
        assert result == 33, f"Test 15 failed: got {result}, expected {33}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = task_code([20, -4, 3, 1, 5, 6, -35, 12, 21, -1, 0, 6])
        assert result == 38, f"Test 16 failed: got {result}, expected {38}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = task_code([-10, -1, 12, -36, 6, 5, 1, 3, -4])
        assert result == 15, f"Test 17 failed: got {result}, expected {15}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = task_code([-10, -4, 3, 1, 5, 6, -35, 12, 21, -1, 8])
        assert result == 40, f"Test 18 failed: got {result}, expected {40}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = task_code([10, -4, 3, 1, 5, 6, -35, 12, -1, -9])
        assert result == 21, f"Test 19 failed: got {result}, expected {21}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = task_code([0, -1, 21, 12, -35, 6, 5, 1, 3, -4, 10])
        assert result == 33, f"Test 20 failed: got {result}, expected {33}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = task_code([2, 1, -4, 3, -4, 6, 5, -5, 1])
        assert result == 11, f"Test 21 failed: got {result}, expected {11}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = task_code([1, -5, 5, 6, -4, 4, 3, -4, 2])
        assert result == 14, f"Test 22 failed: got {result}, expected {14}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = task_code([0, 1, -5, 5, 6, -100, 4, 3, -4, 0, 2, 0])
        assert result == 11, f"Test 23 failed: got {result}, expected {11}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = task_code([2, 70, -4, 3, 4, -4, 6, 5, -5, 1, 12, 0, -19])
        assert result == 90, f"Test 24 failed: got {result}, expected {90}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = task_code([2, 1, -4, 3, 4, -4, 6, 5, -5, 1, 0])
        assert result == 14, f"Test 25 failed: got {result}, expected {14}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = task_code([-36, 1, -5, 5, 6, -4, 4, 3, -4, 1, 2])
        assert result == 14, f"Test 26 failed: got {result}, expected {14}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = task_code([1, -4, 3, 4, -4, 6, 5, -5, -2147483648, 0, 0, 0])
        assert result == 14, f"Test 27 failed: got {result}, expected {14}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = task_code([1, -5, 5, 6, -4, 4, 3, -4, 1, 2])
        assert result == 14, f"Test 28 failed: got {result}, expected {14}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = task_code([0, -4, -3, -2, -1, 500000000, 600000000])
        assert result == 1100000000, f"Test 29 failed: got {result}, expected {1100000000}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = task_code([-5, -4, -3, -2, -1, 6, 0, 0])
        assert result == 6, f"Test 30 failed: got {result}, expected {6}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = task_code([2147483647, 100, -5, -4, -3, -2, -1])
        assert result == 2147483747, f"Test 31 failed: got {result}, expected {2147483747}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = task_code([1, 2, 3, 3, 6, -35, 0])
        assert result == 15, f"Test 32 failed: got {result}, expected {15}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = task_code([-5, 8, -4])
        assert result == 8, f"Test 33 failed: got {result}, expected {8}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = task_code([-1, 1, 0])
        assert result == 1, f"Test 34 failed: got {result}, expected {1}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = task_code([1, 1, -2])
        assert result == 2, f"Test 35 failed: got {result}, expected {2}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = task_code([0, 0, 1, -32])
        assert result == 1, f"Test 36 failed: got {result}, expected {1}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = task_code([-1, 1, 1000000000])
        assert result == 1000000001, f"Test 37 failed: got {result}, expected {1000000001}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = task_code([0, 7, -36])
        assert result == 7, f"Test 38 failed: got {result}, expected {7}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = task_code([0, 10, -4, -3, -2, -1])
        assert result == 10, f"Test 39 failed: got {result}, expected {10}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = task_code([-6, 1, 3, -1, 4])
        assert result == 7, f"Test 40 failed: got {result}, expected {7}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = task_code([4, -1, 2, 1, 0, -2, 0, 0])
        assert result == 6, f"Test 41 failed: got {result}, expected {6}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = task_code([0, -1, 2, 1, 2147483646, 14])
        assert result == 2147483663, f"Test 42 failed: got {result}, expected {2147483663}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = task_code([4, -5, 1, 2, -1, 4, 1, -2, 0])
        assert result == 7, f"Test 43 failed: got {result}, expected {7}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = task_code([0, -2, 1, -3, 4, -1, 2, 1, -5, 4, -1000000000])
        assert result == 6, f"Test 44 failed: got {result}, expected {6}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = task_code([4, -5, 1, 0, 5, -3, 1, 0])
        assert result == 6, f"Test 45 failed: got {result}, expected {6}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = task_code([12, -2, 1, -3, 4, 2, 1, -5, 4, 0])
        assert result == 15, f"Test 46 failed: got {result}, expected {15}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = task_code([-2, 1, -3, 4, 2, 1, -5, 4, 0])
        assert result == 7, f"Test 47 failed: got {result}, expected {7}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = task_code([1000000000, 4, -5, 1, 2, -1, 4, -3, 1, -2])
        assert result == 1000000005, f"Test 48 failed: got {result}, expected {1000000005}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = task_code([10, -4, 3, 1, 5, 6, -35, 12, 21, -1, 0])
        assert result == 33, f"Test 49 failed: got {result}, expected {33}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = task_code([10, -4, 3, 5, 6, -35, 12, 21, -1])
        assert result == 33, f"Test 50 failed: got {result}, expected {33}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = task_code([1, -5, 5, 6, -4, 4, 3, -4, 1, 2])
        assert result == 14, f"Test 51 failed: got {result}, expected {14}"
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
