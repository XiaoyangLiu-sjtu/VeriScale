# Coverage Report

Total executable lines: 11
Covered lines: 11
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def findProduct(lst):
2: ✓     even = None
3: ✓     odd = None
4: ✓     for num in lst:
5: ✓         if even is None and num % 2 == 0:
6: ✓             even = num
7: ✓         if odd is None and num % 2 != 0:
8: ✓             odd = num
9: ✓         if even is not None and odd is not None:
10: ✓             break
11: ✓     return even * odd
```

## Complete Test File

```python
def findProduct(lst):
    even = None
    odd = None
    for num in lst:
        if even is None and num % 2 == 0:
            even = num
        if odd is None and num % 2 != 0:
            odd = num
        if even is not None and odd is not None:
            break
    return even * odd

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = findProduct([2, 3, 4, 5])
        assert result == 6, f"Test 1 failed: got {result}, expected {6}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = findProduct([2, 4, 3, 6])
        assert result == 6, f"Test 2 failed: got {result}, expected {6}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = findProduct([1, 2, 5, 4])
        assert result == 2, f"Test 3 failed: got {result}, expected {2}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = findProduct([2, 3])
        assert result == 6, f"Test 4 failed: got {result}, expected {6}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = findProduct([3, 2])
        assert result == 6, f"Test 5 failed: got {result}, expected {6}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = findProduct([-2, 5])
        assert result == -10, f"Test 6 failed: got {result}, expected {-10}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = findProduct([7, -4])
        assert result == -28, f"Test 7 failed: got {result}, expected {-28}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = findProduct([-3, -2])
        assert result == 6, f"Test 8 failed: got {result}, expected {6}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = findProduct([-2, -3])
        assert result == 6, f"Test 9 failed: got {result}, expected {6}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = findProduct([2, 4, 6, 7])
        assert result == 14, f"Test 10 failed: got {result}, expected {14}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = findProduct([1, 3, 5, 8])
        assert result == 8, f"Test 11 failed: got {result}, expected {8}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = findProduct([10, 11, 12, 13])
        assert result == 110, f"Test 12 failed: got {result}, expected {110}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = findProduct([11, 10, 9, 8])
        assert result == 110, f"Test 13 failed: got {result}, expected {110}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = findProduct([2, 2, 2, 3])
        assert result == 6, f"Test 14 failed: got {result}, expected {6}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = findProduct([3, 3, 2, 5])
        assert result == 6, f"Test 15 failed: got {result}, expected {6}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = findProduct([100, -101, 4])
        assert result == -10100, f"Test 16 failed: got {result}, expected {-10100}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = findProduct([-100, 101, -4])
        assert result == -10100, f"Test 17 failed: got {result}, expected {-10100}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = findProduct([6, -1, -3, -5])
        assert result == -6, f"Test 18 failed: got {result}, expected {-6}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = findProduct([-7, 8, 10])
        assert result == -56, f"Test 19 failed: got {result}, expected {-56}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = findProduct([5, 7, 9, 2, 4])
        assert result == 10, f"Test 20 failed: got {result}, expected {10}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = findProduct([14, 15])
        assert result == 210, f"Test 21 failed: got {result}, expected {210}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = findProduct([15, 14])
        assert result == 210, f"Test 22 failed: got {result}, expected {210}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = findProduct([2, -1, 4, -3, 6, -5])
        assert result == -2, f"Test 23 failed: got {result}, expected {-2}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = findProduct([-1, 2, -3, 4, -5, 6])
        assert result == -2, f"Test 24 failed: got {result}, expected {-2}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = findProduct([8, 8, 8, 8, 9])
        assert result == 72, f"Test 25 failed: got {result}, expected {72}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = findProduct([9, 9, 9, 2])
        assert result == 18, f"Test 26 failed: got {result}, expected {18}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = findProduct([42, -17, 0, 5])
        assert result == -714, f"Test 27 failed: got {result}, expected {-714}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = findProduct([-17, 42, 5, 0])
        assert result == -714, f"Test 28 failed: got {result}, expected {-714}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = findProduct([2147483646, 2147483647])
        assert result == 4611686011984936962, f"Test 29 failed: got {result}, expected {4611686011984936962}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = findProduct([-2147483648, -2147483647])
        assert result == 4611686016279904256, f"Test 30 failed: got {result}, expected {4611686016279904256}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = findProduct([2, 4, 5])
        assert result == 10, f"Test 31 failed: got {result}, expected {10}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = findProduct([5, 4, 3])
        assert result == 20, f"Test 32 failed: got {result}, expected {20}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = findProduct([2, 3, 5])
        assert result == 6, f"Test 33 failed: got {result}, expected {6}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = findProduct([2, 3, 4, 5, 0])
        assert result == 6, f"Test 34 failed: got {result}, expected {6}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = findProduct([2, 3, 5, 5])
        assert result == 6, f"Test 35 failed: got {result}, expected {6}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = findProduct([4, 3, 4, 6])
        assert result == 12, f"Test 36 failed: got {result}, expected {12}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = findProduct([2, 3, 0])
        assert result == 6, f"Test 37 failed: got {result}, expected {6}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = findProduct([6, 4, 5])
        assert result == 30, f"Test 38 failed: got {result}, expected {30}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = findProduct([2147483647, 5, 4, 3, 2])
        assert result == 8589934588, f"Test 39 failed: got {result}, expected {8589934588}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = findProduct([5, 4, 3, 2, 0, 0, 0])
        assert result == 20, f"Test 40 failed: got {result}, expected {20}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = findProduct([4, 3])
        assert result == 12, f"Test 41 failed: got {result}, expected {12}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = findProduct([3, 6])
        assert result == 18, f"Test 42 failed: got {result}, expected {18}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = findProduct([3, 4, 2])
        assert result == 12, f"Test 43 failed: got {result}, expected {12}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = findProduct([1, 100, 15, 6, 0, 0])
        assert result == 100, f"Test 44 failed: got {result}, expected {100}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = findProduct([2, 4, 3, 6, 8, -2, 6])
        assert result == 6, f"Test 45 failed: got {result}, expected {6}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = findProduct([2, 4, 3])
        assert result == 6, f"Test 46 failed: got {result}, expected {6}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = findProduct([100, 4, 3, 6, 12, 0, -5])
        assert result == 300, f"Test 47 failed: got {result}, expected {300}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = findProduct([6, 3, 4, 3])
        assert result == 18, f"Test 48 failed: got {result}, expected {18}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = findProduct([2, 4, 3, 6, 0])
        assert result == 6, f"Test 49 failed: got {result}, expected {6}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = findProduct([2, 4, 3, 6, 10])
        assert result == 6, f"Test 50 failed: got {result}, expected {6}"
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
