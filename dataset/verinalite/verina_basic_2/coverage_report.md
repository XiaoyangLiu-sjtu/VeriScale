# Coverage Report

Total executable lines: 8
Covered lines: 8
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def findSmallest(s):
2: ✓     if not s:
3: ✓         return None
4: ✓     smallest = s[0]
5: ✓     for num in s[1:]:
6: ✓         if num < smallest:
7: ✓             smallest = num
8: ✓     return smallest
```

## Complete Test File

```python
def findSmallest(s):
    if not s:
        return None
    smallest = s[0]
    for num in s[1:]:
        if num < smallest:
            smallest = num
    return smallest

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = findSmallest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        assert result == 1, f"Test 1 failed: got {result}, expected {1}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = findSmallest([0, 1, 2, 3, 4, 5])
        assert result == 0, f"Test 2 failed: got {result}, expected {0}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = findSmallest([1])
        assert result == 1, f"Test 3 failed: got {result}, expected {1}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = findSmallest([10, 10, 10])
        assert result == 10, f"Test 4 failed: got {result}, expected {10}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = findSmallest([3, 2, 2, 2, 2, 2, 2, 1])
        assert result == 1, f"Test 5 failed: got {result}, expected {1}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = findSmallest([0])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = findSmallest([100, 99, 98])
        assert result == 98, f"Test 7 failed: got {result}, expected {98}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = findSmallest([])
        assert result == None, f"Test 8 failed: got {result}, expected {None}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = findSmallest([10, 2, 8, 6, 4])
        assert result == 2, f"Test 9 failed: got {result}, expected {2}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = findSmallest([123456789, 987654321, 111111111, 222222222, 333333333])
        assert result == 111111111, f"Test 10 failed: got {result}, expected {111111111}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = findSmallest([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        assert result == 0, f"Test 11 failed: got {result}, expected {0}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = findSmallest([1000, 900, 800, 1, 700, 600, 500])
        assert result == 1, f"Test 12 failed: got {result}, expected {1}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = findSmallest([31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33, 83, 27, 95, 2, 88, 41, 97])
        assert result == 2, f"Test 13 failed: got {result}, expected {2}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = findSmallest([15, 22, 13, 27, 19, 31, 0, 44, 8])
        assert result == 0, f"Test 14 failed: got {result}, expected {0}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = findSmallest([3, 1, 4, 5, 9, 2, 6, 5, 3, 5])
        assert result == 1, f"Test 15 failed: got {result}, expected {1}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = findSmallest([0, 5, 3, 5, 6, 42, 9, 5, 1, 4, 1])
        assert result == 0, f"Test 16 failed: got {result}, expected {0}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = findSmallest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 0, 58])
        assert result == 0, f"Test 17 failed: got {result}, expected {0}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = findSmallest([10, 83])
        assert result == 10, f"Test 18 failed: got {result}, expected {10}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = findSmallest([3, 2, 2, 2, 2, 2, 2, 1, 88])
        assert result == 1, f"Test 19 failed: got {result}, expected {1}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = findSmallest([2, 0, 333333333])
        assert result == 0, f"Test 20 failed: got {result}, expected {0}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = findSmallest([100, 99, 98, 0, 84])
        assert result == 0, f"Test 21 failed: got {result}, expected {0}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = findSmallest([100, 99, 98, 12, 0, 11])
        assert result == 0, f"Test 22 failed: got {result}, expected {0}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = findSmallest([99, 256, 1])
        assert result == 1, f"Test 23 failed: got {result}, expected {1}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = findSmallest([12, 0, 83, 101])
        assert result == 0, f"Test 24 failed: got {result}, expected {0}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = findSmallest([1024, 26, 1, 15])
        assert result == 1, f"Test 25 failed: got {result}, expected {1}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = findSmallest([5, 5, 5, 222222222])
        assert result == 5, f"Test 26 failed: got {result}, expected {5}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = findSmallest([5, 5, 5, 0])
        assert result == 0, f"Test 27 failed: got {result}, expected {0}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = findSmallest([5, 5, 5, 18446744073709551615, 0, 0])
        assert result == 0, f"Test 28 failed: got {result}, expected {0}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = findSmallest([1, 2, 4, 4, 5, 40, 97])
        assert result == 1, f"Test 29 failed: got {result}, expected {1}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = findSmallest([4, 3, 2, 0, 26])
        assert result == 0, f"Test 30 failed: got {result}, expected {0}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = findSmallest([2, 4, 4, 6])
        assert result == 2, f"Test 31 failed: got {result}, expected {2}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = findSmallest([4, 0, 10, 800])
        assert result == 0, f"Test 32 failed: got {result}, expected {0}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = findSmallest([10, 8, 6, 4, 0, 0, 0, 50])
        assert result == 0, f"Test 33 failed: got {result}, expected {0}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = findSmallest([10, 2, 93, 6, 4])
        assert result == 2, f"Test 34 failed: got {result}, expected {2}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = findSmallest([88, 2, 4, 6, 8, 10])
        assert result == 2, f"Test 35 failed: got {result}, expected {2}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = findSmallest([10, 8, 6, 2])
        assert result == 2, f"Test 36 failed: got {result}, expected {2}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = findSmallest([3, 3, 800, 3, 51])
        assert result == 3, f"Test 37 failed: got {result}, expected {3}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = findSmallest([7, 512, 5, 0, 11, 12])
        assert result == 0, f"Test 38 failed: got {result}, expected {0}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = findSmallest([2, 999999999999999999999999, 5, 7, 11, 13, 17, 19])
        assert result == 2, f"Test 39 failed: got {result}, expected {2}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = findSmallest([987654321, 3, 5, 14, 11, 13, 17, 19])
        assert result == 3, f"Test 40 failed: got {result}, expected {3}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = findSmallest([19, 34, 13, 11, 7, 5, 17])
        assert result == 5, f"Test 41 failed: got {result}, expected {5}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = findSmallest([128, 27, 888888888888888888888888, 999999999999999999999999])
        assert result == 27, f"Test 42 failed: got {result}, expected {27}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = findSmallest([999999999999999999999999, 888888888888888888888888, 777777777777777777777777, 14, 13, 987654321, 111111111])
        assert result == 13, f"Test 43 failed: got {result}, expected {13}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = findSmallest([18446744073709551614, 0, 18446744073709551615])
        assert result == 0, f"Test 44 failed: got {result}, expected {0}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = findSmallest([2, 1, 340282366920938463463374607431768211455])
        assert result == 1, f"Test 45 failed: got {result}, expected {1}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = findSmallest([340282366920938463463374607431768211455, 1, 2, 99, 84])
        assert result == 1, f"Test 46 failed: got {result}, expected {1}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = findSmallest([50, 32, 30, 20, 10, 0, 20, 30, 40, 50])
        assert result == 0, f"Test 47 failed: got {result}, expected {0}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = findSmallest([50, 40, 30, 20, 10, 0, 10, 20, 13, 40, 50])
        assert result == 0, f"Test 48 failed: got {result}, expected {0}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = findSmallest([50, 40, 30, 20, 10, 0, 10, 84, 30, 40, 50, 93, 11])
        assert result == 0, f"Test 49 failed: got {result}, expected {0}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = findSmallest([9, 9, 0, 3, 5, 7, 6, 8])
        assert result == 0, f"Test 50 failed: got {result}, expected {0}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = findSmallest([1023, 2, 2, 2, 2, 2, 1, 2, 2, 2])
        assert result == 1, f"Test 51 failed: got {result}, expected {1}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = findSmallest([0, 11, 333333333, 222222222, 111111111, 987654321, 123456789])
        assert result == 0, f"Test 52 failed: got {result}, expected {0}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = findSmallest([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 17])
        assert result == 1, f"Test 53 failed: got {result}, expected {1}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = findSmallest([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 500, 27])
        assert result == 1, f"Test 54 failed: got {result}, expected {1}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = findSmallest([18446744073709551615, 1000, 900, 800, 1, 700, 18])
        assert result == 1, f"Test 55 failed: got {result}, expected {1}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = findSmallest([1000, 900, 801, 1, 700, 600, 500, 900])
        assert result == 1, f"Test 56 failed: got {result}, expected {1}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = findSmallest([1000000000000000000000000000000, 0, 1])
        assert result == 0, f"Test 57 failed: got {result}, expected {0}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = findSmallest([59, 15, 22, 13, 27, 19, 31, 0, 44, 8])
        assert result == 0, f"Test 58 failed: got {result}, expected {0}"
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
