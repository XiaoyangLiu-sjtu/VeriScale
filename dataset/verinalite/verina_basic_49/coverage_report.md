# Coverage Report

Total executable lines: 5
Covered lines: 5
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def findFirstOdd(a):
2: ✓     for i, num in enumerate(a):
3: ✓         if num % 2 != 0:
4: ✓             return (True, i)
5: ✓     return (False, -1)
```

## Complete Test File

```python
def findFirstOdd(a):
    for i, num in enumerate(a):
        if num % 2 != 0:
            return (True, i)
    return (False, -1)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = findFirstOdd([2, 4, 6, 8])
        assert result == None, f"Test 1 failed: got {result}, expected {None}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = findFirstOdd([3, 4, 6, 8])
        assert result == 0, f"Test 2 failed: got {result}, expected {0}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = findFirstOdd([2, 4, 5, 8])
        assert result == 2, f"Test 3 failed: got {result}, expected {2}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = findFirstOdd([7])
        assert result == 0, f"Test 4 failed: got {result}, expected {0}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = findFirstOdd([2])
        assert result == None, f"Test 5 failed: got {result}, expected {None}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = findFirstOdd([1, 2, 3])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = findFirstOdd([2, 4, 6, 9])
        assert result == 3, f"Test 7 failed: got {result}, expected {3}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = findFirstOdd([8, 10, 12, 14, 16, 18, 20, 21])
        assert result == 7, f"Test 8 failed: got {result}, expected {7}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = findFirstOdd([-2147483648, -2147483647])
        assert result == 1, f"Test 9 failed: got {result}, expected {1}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = findFirstOdd([0, 4, 6, 8, 12])
        assert result == None, f"Test 10 failed: got {result}, expected {None}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = findFirstOdd([2, -2147483648, 14, 8, 0, 0])
        assert result == None, f"Test 11 failed: got {result}, expected {None}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = findFirstOdd([8, 6, 4, 3, 999999999999999999999999999998])
        assert result == 3, f"Test 12 failed: got {result}, expected {3}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = findFirstOdd([0, 5, 4, 2, 16, -1000000000000000001])
        assert result == 1, f"Test 13 failed: got {result}, expected {1}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = findFirstOdd([8, 5, 16])
        assert result == 1, f"Test 14 failed: got {result}, expected {1}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = findFirstOdd([7, 5, 4, 2, 0])
        assert result == 0, f"Test 15 failed: got {result}, expected {0}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = findFirstOdd([2, 5, 8, 2])
        assert result == 1, f"Test 16 failed: got {result}, expected {1}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = findFirstOdd([0, 2147483647, 0, 15])
        assert result == 1, f"Test 17 failed: got {result}, expected {1}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = findFirstOdd([0, 7, 999999999999999999999999999999, 0])
        assert result == 1, f"Test 18 failed: got {result}, expected {1}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = findFirstOdd([7, 0])
        assert result == 0, f"Test 19 failed: got {result}, expected {0}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = findFirstOdd([0, 8, 0, -5, 0])
        assert result == 3, f"Test 20 failed: got {result}, expected {3}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = findFirstOdd([2, 4, 6, -5, 0])
        assert result == 3, f"Test 21 failed: got {result}, expected {3}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = findFirstOdd([0, 4, 0, 9, 0])
        assert result == 3, f"Test 22 failed: got {result}, expected {3}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = findFirstOdd([0, 2, 4, 6, 9])
        assert result == 4, f"Test 23 failed: got {result}, expected {4}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = findFirstOdd([16, 11, 9, -8])
        assert result == 1, f"Test 24 failed: got {result}, expected {1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = findFirstOdd([2, 2, 2, 3, 6, 1000000000000000001])
        assert result == 3, f"Test 25 failed: got {result}, expected {3}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = findFirstOdd([2, 2, 2, 2, 3, 0])
        assert result == 4, f"Test 26 failed: got {result}, expected {4}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = findFirstOdd([2, 2, 2, 2, 3, 10])
        assert result == 4, f"Test 27 failed: got {result}, expected {4}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = findFirstOdd([2, 2, 2, 2, 3, 1000000000000000001, 0, 6])
        assert result == 4, f"Test 28 failed: got {result}, expected {4}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = findFirstOdd([6, -5, 4, 3, 2, 0])
        assert result == 1, f"Test 29 failed: got {result}, expected {1}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = findFirstOdd([2, 3, 20])
        assert result == 1, f"Test 30 failed: got {result}, expected {1}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = findFirstOdd([2, 3, 4, 5, 6, 0])
        assert result == 1, f"Test 31 failed: got {result}, expected {1}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = findFirstOdd([2, 3, 4, 5, 7, -6, 21, 0])
        assert result == 1, f"Test 32 failed: got {result}, expected {1}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = findFirstOdd([0, 6, 5, 4, 3, 2])
        assert result == 2, f"Test 33 failed: got {result}, expected {2}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = findFirstOdd([-4, -6, -8, -9])
        assert result == 3, f"Test 34 failed: got {result}, expected {3}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = findFirstOdd([-4, 0, -9, -10, 0])
        assert result == 2, f"Test 35 failed: got {result}, expected {2}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = findFirstOdd([-4, -6, -7, -8, 0])
        assert result == 2, f"Test 36 failed: got {result}, expected {2}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = findFirstOdd([-8, -6])
        assert result == None, f"Test 37 failed: got {result}, expected {None}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = findFirstOdd([1000000000000000000, 1000000000000000001, 2147483647])
        assert result == 1, f"Test 38 failed: got {result}, expected {1}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = findFirstOdd([1000000000000000000, 43])
        assert result == 1, f"Test 39 failed: got {result}, expected {1}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = findFirstOdd([42, 4, 2, -1000000000000000001])
        assert result == 3, f"Test 40 failed: got {result}, expected {3}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = findFirstOdd([0, 0, 0, 1, -999999999999999999999999999999])
        assert result == 3, f"Test 41 failed: got {result}, expected {3}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = findFirstOdd([4, 0, 0, 1, 999999999999999999999999999999, 0, 0])
        assert result == 3, f"Test 42 failed: got {result}, expected {3}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = findFirstOdd([0, 0, 0, 1, -5])
        assert result == 3, f"Test 43 failed: got {result}, expected {3}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = findFirstOdd([0, 1, 0, 5, 7, 14])
        assert result == 1, f"Test 44 failed: got {result}, expected {1}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = findFirstOdd([0, -1, 0, 0, -1000000000000000001, 0])
        assert result == 1, f"Test 45 failed: got {result}, expected {1}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = findFirstOdd([0, 0, 0, -1])
        assert result == 3, f"Test 46 failed: got {result}, expected {3}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = findFirstOdd([12, 4, 2, 0, 5, 2147483646, 0])
        assert result == 4, f"Test 47 failed: got {result}, expected {4}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = findFirstOdd([1000000000000000000, 4, 0, 5, -3])
        assert result == 3, f"Test 48 failed: got {result}, expected {3}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = findFirstOdd([-3, 9, -14, 0])
        assert result == 0, f"Test 49 failed: got {result}, expected {0}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = findFirstOdd([8, 10, 12, 14, 16, 18, 21, 8, 20])
        assert result == 6, f"Test 50 failed: got {result}, expected {6}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = findFirstOdd([8, 10, 12, 13, 16, 18, 20, 21, 6])
        assert result == 3, f"Test 51 failed: got {result}, expected {3}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = findFirstOdd([-2147483648, -2147483648, -5, 0])
        assert result == 2, f"Test 52 failed: got {result}, expected {2}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = findFirstOdd([42, 42, 42, 42, 2147483649, 11, 0, 7])
        assert result == 4, f"Test 53 failed: got {result}, expected {4}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = findFirstOdd([2, 6, 8, 10, 12, 14, 15, 16, 0, 0, 0])
        assert result == 6, f"Test 54 failed: got {result}, expected {6}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = findFirstOdd([-2, -4, -6, -8, -9, -10, 43, -2147483647])
        assert result == 4, f"Test 55 failed: got {result}, expected {4}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = findFirstOdd([6, 4, 4, 0, -4, 1, 6])
        assert result == 5, f"Test 56 failed: got {result}, expected {5}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
