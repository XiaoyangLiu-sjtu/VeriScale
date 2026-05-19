# Coverage Report

Total executable lines: 6
Covered lines: 6
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def hasCommonElement(a, b):
2: ✓     set_b = set(b)
3: ✓     for x in a:
4: ✓         if x in set_b:
5: ✓             return True
6: ✓     return False
```

## Complete Test File

```python
def hasCommonElement(a, b):
    set_b = set(b)
    for x in a:
        if x in set_b:
            return True
    return False

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = hasCommonElement([1, 2, 3], [4, 5, 6])
        assert result == False, f"Test 1 failed: got {result}, expected {False}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = hasCommonElement([1, 2, 3], [3, 4, 5])
        assert result == True, f"Test 2 failed: got {result}, expected {True}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = hasCommonElement([7, 8, 9], [10, 11, 7])
        assert result == True, f"Test 3 failed: got {result}, expected {True}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = hasCommonElement([1, 2, 3, 4], [5, 6, 7, 8])
        assert result == False, f"Test 4 failed: got {result}, expected {False}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = hasCommonElement([1, 2, 3, 4], [4, 5, 6])
        assert result == True, f"Test 5 failed: got {result}, expected {True}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = hasCommonElement([1, 1, 1], [1, 2, 1])
        assert result == True, f"Test 6 failed: got {result}, expected {True}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = hasCommonElement([0], [0])
        assert result == True, f"Test 7 failed: got {result}, expected {True}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = hasCommonElement([0], [-1, 1])
        assert result == False, f"Test 8 failed: got {result}, expected {False}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = hasCommonElement([11, 12], [12, 13, 14, 15])
        assert result == True, f"Test 9 failed: got {result}, expected {True}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = hasCommonElement([-5, -4, -3, -2, -1], [-1])
        assert result == True, f"Test 10 failed: got {result}, expected {True}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = hasCommonElement([1, 2, 3], [3, 5, -2147483648, 3])
        assert result == True, f"Test 11 failed: got {result}, expected {True}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = hasCommonElement([0, 9, 8, 7], [11, 7, 14, -1])
        assert result == True, f"Test 12 failed: got {result}, expected {True}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = hasCommonElement([8, 0], [10, 11, 8])
        assert result == True, f"Test 13 failed: got {result}, expected {True}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = hasCommonElement([1, 1, 3, 4], [4, 5, 6])
        assert result == True, f"Test 14 failed: got {result}, expected {True}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = hasCommonElement([1, 2, 3, 4], [6, 4, 0])
        assert result == True, f"Test 15 failed: got {result}, expected {True}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = hasCommonElement([1, 2, 3, 4, -4], [6, 5, 4])
        assert result == True, f"Test 16 failed: got {result}, expected {True}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = hasCommonElement([4, 3, 1], [6, 5, 4, 0])
        assert result == True, f"Test 17 failed: got {result}, expected {True}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = hasCommonElement([1, 1, 1, 0], [1, 2, 1])
        assert result == True, f"Test 18 failed: got {result}, expected {True}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = hasCommonElement([0], [0, -39])
        assert result == True, f"Test 19 failed: got {result}, expected {True}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = hasCommonElement([0], [123456789, 0])
        assert result == True, f"Test 20 failed: got {result}, expected {True}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = hasCommonElement([1], [-100, 1])
        assert result == True, f"Test 21 failed: got {result}, expected {True}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = hasCommonElement([0, 0], [2, 0])
        assert result == True, f"Test 22 failed: got {result}, expected {True}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = hasCommonElement([2, 1], [2])
        assert result == True, f"Test 23 failed: got {result}, expected {True}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = hasCommonElement([1, 0], [0])
        assert result == True, f"Test 24 failed: got {result}, expected {True}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = hasCommonElement([0], [1, 0])
        assert result == True, f"Test 25 failed: got {result}, expected {True}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = hasCommonElement([-1, 0, 0, 0], [1, -1])
        assert result == True, f"Test 26 failed: got {result}, expected {True}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = hasCommonElement([-1, 0], [1, -1, 0])
        assert result == True, f"Test 27 failed: got {result}, expected {True}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = hasCommonElement([-1], [0, 0, 0, 32, -1, 1])
        assert result == True, f"Test 28 failed: got {result}, expected {True}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = hasCommonElement([1, 1, 2, 0], [2, 2, 3])
        assert result == True, f"Test 29 failed: got {result}, expected {True}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = hasCommonElement([1, 1, 2, 40], [2, 0, 3])
        assert result == True, f"Test 30 failed: got {result}, expected {True}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = hasCommonElement([2, 1, 1], [0, 3, 1, 2, 18])
        assert result == True, f"Test 31 failed: got {result}, expected {True}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = hasCommonElement([-1, -2, -3, 0, -999999999999999999], [0, 1])
        assert result == True, f"Test 32 failed: got {result}, expected {True}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = hasCommonElement([-3, -2, -1, 0], [-1, 0, 1])
        assert result == True, f"Test 33 failed: got {result}, expected {True}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = hasCommonElement([-3, -2, -1, 0, 0, 0], [-1, 0, 1])
        assert result == True, f"Test 34 failed: got {result}, expected {True}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = hasCommonElement([-3, -2, -1], [-1, 0, 1, 43])
        assert result == True, f"Test 35 failed: got {result}, expected {True}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = hasCommonElement([1000000000000], [3, 1000000000000, 0, 0, 0, 0])
        assert result == True, f"Test 36 failed: got {result}, expected {True}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = hasCommonElement([4294967294, -2147483648, -7], [-2147483648, 0])
        assert result == True, f"Test 37 failed: got {result}, expected {True}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = hasCommonElement([12, -2147483648, 2147483647, 0], [-2147483648, 44])
        assert result == True, f"Test 38 failed: got {result}, expected {True}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = hasCommonElement([-10, 0, 20], [10, 16, 30, 0])
        assert result == True, f"Test 39 failed: got {result}, expected {True}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = hasCommonElement([-10, -1, 10, 0, 44], [10])
        assert result == True, f"Test 40 failed: got {result}, expected {True}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = hasCommonElement([-10, 0, 10, 0], [10, 20, 30])
        assert result == True, f"Test 41 failed: got {result}, expected {True}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = hasCommonElement([-10, 0, 20], [10, 20, 18])
        assert result == True, f"Test 42 failed: got {result}, expected {True}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = hasCommonElement([-10], [0, 8, -40, -30, -20])
        assert result == False, f"Test 43 failed: got {result}, expected {False}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = hasCommonElement([2, 4, 6, 9, 10], [10, 9, 7, 6, 3, 1])
        assert result == True, f"Test 44 failed: got {result}, expected {True}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = hasCommonElement([2, 4, 6, 8, 9], [3, 5, 7, 9, 0])
        assert result == True, f"Test 45 failed: got {result}, expected {True}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = hasCommonElement([2, 4, 6, 8, 10], [0, 2, 987654321, 7])
        assert result == True, f"Test 46 failed: got {result}, expected {True}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = hasCommonElement([2, 5, 6, 10, 44], [0, 2])
        assert result == True, f"Test 47 failed: got {result}, expected {True}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = hasCommonElement([11, 12], [12, 13, 14, 15, 0])
        assert result == True, f"Test 48 failed: got {result}, expected {True}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = hasCommonElement([13, 14, 100], [10, 11, 12])
        assert result == False, f"Test 49 failed: got {result}, expected {False}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = hasCommonElement([-5, -4, -3, -2, -1, 2, 43], [-1])
        assert result == True, f"Test 50 failed: got {result}, expected {True}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = hasCommonElement([-5, -4, -3, -1, -1], [-1])
        assert result == True, f"Test 51 failed: got {result}, expected {True}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = hasCommonElement([-5, 12, -3, -2, -1], [0, -1])
        assert result == True, f"Test 52 failed: got {result}, expected {True}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = hasCommonElement([1, 2, 3, 4, 5], [5, 4, 3, 2])
        assert result == True, f"Test 53 failed: got {result}, expected {True}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = hasCommonElement([-100, 100, 0], [100, 0, 29])
        assert result == True, f"Test 54 failed: got {result}, expected {True}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = hasCommonElement([11, 32, 24, 16, 8], [32, 40, 0])
        assert result == True, f"Test 55 failed: got {result}, expected {True}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = hasCommonElement([8, 16, 24, 32, 100, 0, 4], [40, 0])
        assert result == True, f"Test 56 failed: got {result}, expected {True}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = hasCommonElement([8, 16, 24, 32, -10], [32, 40])
        assert result == True, f"Test 57 failed: got {result}, expected {True}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = hasCommonElement([-30, -7], [1, 0])
        assert result == False, f"Test 58 failed: got {result}, expected {False}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
