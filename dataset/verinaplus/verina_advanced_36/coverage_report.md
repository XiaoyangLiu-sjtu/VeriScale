# Coverage Report

Total executable lines: 11
Covered lines: 11
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def majorityElement(xs):
2: ✓     count = 0
3: ✓     candidate = None
4: ✓     for num in xs:
5: ✓         if count == 0:
6: ✓             candidate = num
7: ✓             count = 1
8: ✓         elif candidate == num:
9: ✓             count += 1
10:           else:
11: ✓             count -= 1
12: ✓     return candidate
```

## Complete Test File

```python
def majorityElement(xs):
    count = 0
    candidate = None
    for num in xs:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    return candidate

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = majorityElement([3, 3, 4, 2, 3, 3, 3])
        assert result == 3, f"Test 1 failed: got {result}, expected {3}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = majorityElement([1, 1, 2, 1, 3, 1, 1])
        assert result == 1, f"Test 2 failed: got {result}, expected {1}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = majorityElement([2, 2, 2, 1, 1])
        assert result == 2, f"Test 3 failed: got {result}, expected {2}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = majorityElement([9, 9, 9, 9, 1, 2, 3])
        assert result == 9, f"Test 4 failed: got {result}, expected {9}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = majorityElement([5, 5, 5, 5, 5, 6, 7])
        assert result == 5, f"Test 5 failed: got {result}, expected {5}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = majorityElement([0])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = majorityElement([5, 5])
        assert result == 5, f"Test 7 failed: got {result}, expected {5}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = majorityElement([1, 2, 1])
        assert result == 1, f"Test 8 failed: got {result}, expected {1}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = majorityElement([2, 1, 2, 3, 2])
        assert result == 2, f"Test 9 failed: got {result}, expected {2}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = majorityElement([4, 4, 4, 2, 3, 4])
        assert result == 4, f"Test 10 failed: got {result}, expected {4}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = majorityElement([7, 8, 7, 7, 9, 7, 1])
        assert result == 7, f"Test 11 failed: got {result}, expected {7}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = majorityElement([10, 10, 11, 10, 12, 10, 13, 10])
        assert result == 10, f"Test 12 failed: got {result}, expected {10}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = majorityElement([3, 3, 3, 1, 2])
        assert result == 3, f"Test 13 failed: got {result}, expected {3}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = majorityElement([6, 6, 6, 6, 1, 2, 3])
        assert result == 6, f"Test 14 failed: got {result}, expected {6}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = majorityElement([9, 1, 9, 2, 9, 3, 9, 4, 9])
        assert result == 9, f"Test 15 failed: got {result}, expected {9}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = majorityElement([2, 2, 2, 2, 2, 3, 4, 5, 6])
        assert result == 2, f"Test 16 failed: got {result}, expected {2}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = majorityElement([8, 8, 8, 8, 1, 1, 2])
        assert result == 8, f"Test 17 failed: got {result}, expected {8}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = majorityElement([15, 0, 15, 15, 2, 15])
        assert result == 15, f"Test 18 failed: got {result}, expected {15}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = majorityElement([100, 100, 50, 100, 60, 100, 70, 100, 80, 100, 90])
        assert result == 100, f"Test 19 failed: got {result}, expected {100}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = majorityElement([1, 1, 1, 1, 2, 2, 3])
        assert result == 1, f"Test 20 failed: got {result}, expected {1}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = majorityElement([12, 12, 13, 12, 14, 12, 15, 12, 16, 12])
        assert result == 12, f"Test 21 failed: got {result}, expected {12}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = majorityElement([5, 4, 5, 5, 4, 5, 6, 5])
        assert result == 5, f"Test 22 failed: got {result}, expected {5}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = majorityElement([20, 21, 20, 22, 20, 23, 20, 24, 20, 25, 20])
        assert result == 20, f"Test 23 failed: got {result}, expected {20}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = majorityElement([3, 0, 3, 3, 1, 3, 2, 3, 3])
        assert result == 3, f"Test 24 failed: got {result}, expected {3}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = majorityElement([11, 11, 11, 2, 11, 3, 11, 4])
        assert result == 11, f"Test 25 failed: got {result}, expected {11}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = majorityElement([42, 42, 42, 42, 42, 1, 2, 3, 4])
        assert result == 42, f"Test 26 failed: got {result}, expected {42}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = majorityElement([7, 7, 8, 7, 9, 7])
        assert result == 7, f"Test 27 failed: got {result}, expected {7}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = majorityElement([30, 30, 30, 30, 30, 31, 32, 33])
        assert result == 30, f"Test 28 failed: got {result}, expected {30}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = majorityElement([2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2])
        assert result == 2, f"Test 29 failed: got {result}, expected {2}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = majorityElement([9, 9, 9, 9, 9, 9, 1, 2, 3, 4, 5])
        assert result == 9, f"Test 30 failed: got {result}, expected {9}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = majorityElement([14, 14, 14, 15, 16, 14, 17])
        assert result == 14, f"Test 31 failed: got {result}, expected {14}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = majorityElement([6, 1, 6, 2, 6, 3, 6, 4, 6, 5, 6, 6])
        assert result == 6, f"Test 32 failed: got {result}, expected {6}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = majorityElement([0, 1, 0, 2, 0, 3, 0])
        assert result == 0, f"Test 33 failed: got {result}, expected {0}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = majorityElement([99, 99, 98, 99, 97, 99, 96, 99, 95, 99])
        assert result == 99, f"Test 34 failed: got {result}, expected {99}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = majorityElement([18, 18, 18, 18, 19, 20, 21, 18])
        assert result == 18, f"Test 35 failed: got {result}, expected {18}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = majorityElement([25, 26, 25, 27, 25, 28, 25, 29, 25])
        assert result == 25, f"Test 36 failed: got {result}, expected {25}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = majorityElement([4, 4, 4, 4, 4, 4, 2, 3, 5, 6, 7])
        assert result == 4, f"Test 37 failed: got {result}, expected {4}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = majorityElement([3, 4, 2, 3, 3, 3])
        assert result == 3, f"Test 38 failed: got {result}, expected {3}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = majorityElement([3, 3, 5, 2, 3, 3, 3])
        assert result == 3, f"Test 39 failed: got {result}, expected {3}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = majorityElement([3, 3, 4, 3, 3, 3])
        assert result == 3, f"Test 40 failed: got {result}, expected {3}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = majorityElement([3, 3, 2, 3, 3, 0])
        assert result == 3, f"Test 41 failed: got {result}, expected {3}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = majorityElement([3, 3, 4, 3, 3, 3, 29])
        assert result == 3, f"Test 42 failed: got {result}, expected {3}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = majorityElement([3, 3, 4, 2, 3, 3, 3, 0, 0])
        assert result == 3, f"Test 43 failed: got {result}, expected {3}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = majorityElement([3, 3, 4, 2, 3, 3, 3, 0])
        assert result == 3, f"Test 44 failed: got {result}, expected {3}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = majorityElement([1, 1, 2, 1, 3, 1, 1, 61])
        assert result == 1, f"Test 45 failed: got {result}, expected {1}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = majorityElement([1, 1, 3, 1, 1, 1])
        assert result == 1, f"Test 46 failed: got {result}, expected {1}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = majorityElement([1, 1, 2, 1, 3, 1, 1, 30, 6])
        assert result == 1, f"Test 47 failed: got {result}, expected {1}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = majorityElement([1, 1, 2, 3, 1, 1])
        assert result == 1, f"Test 48 failed: got {result}, expected {1}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = majorityElement([1, 1, 3, 1, 2, 0, 1])
        assert result == 1, f"Test 49 failed: got {result}, expected {1}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = majorityElement([1, 1, 3, 1, 2, 1, 1, 25])
        assert result == 1, f"Test 50 failed: got {result}, expected {1}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = majorityElement([1, 1, 3, 1, 2, 1, 1])
        assert result == 1, f"Test 51 failed: got {result}, expected {1}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = majorityElement([1, 1, 2, 1, 3, 1])
        assert result == 1, f"Test 52 failed: got {result}, expected {1}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = majorityElement([1, 1, 2, 1, 3, 1, 1, 0])
        assert result == 1, f"Test 53 failed: got {result}, expected {1}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = majorityElement([0, 2, 1, 2, 2, 2])
        assert result == 2, f"Test 54 failed: got {result}, expected {2}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = majorityElement([9, 9, 9, 9, 2, 3])
        assert result == 9, f"Test 55 failed: got {result}, expected {9}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = majorityElement([9, 9, 9, 9, 1, 3, 96])
        assert result == 9, f"Test 56 failed: got {result}, expected {9}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = majorityElement([9, 3, 2, 1, 9, 9, 9, 9, 4])
        assert result == 9, f"Test 57 failed: got {result}, expected {9}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = majorityElement([3, 2, 1, 9, 9, 9, 9])
        assert result == 9, f"Test 58 failed: got {result}, expected {9}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = majorityElement([9, 9, 9, 9, 1, 2])
        assert result == 9, f"Test 59 failed: got {result}, expected {9}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = majorityElement([9, 9, 9, 0, 3])
        assert result == 9, f"Test 60 failed: got {result}, expected {9}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = majorityElement([5, 1, 5, 5, 5, 6, 7])
        assert result == 5, f"Test 61 failed: got {result}, expected {5}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = majorityElement([5, 5, 5, 5, 5, 6, 7, 0])
        assert result == 5, f"Test 62 failed: got {result}, expected {5}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = majorityElement([5, 5, 5, 5, 26, 6, 4])
        assert result == 5, f"Test 63 failed: got {result}, expected {5}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = majorityElement([7, 6, 5, 5, 5, 5, 5, 0])
        assert result == 5, f"Test 64 failed: got {result}, expected {5}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = majorityElement([7, 6, 5, 5, 5, 5, 0])
        assert result == 5, f"Test 65 failed: got {result}, expected {5}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = majorityElement([7, 6, 5, 5, 5, 5, 5])
        assert result == 5, f"Test 66 failed: got {result}, expected {5}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = majorityElement([5, 5, 5, 5, 6, 7, 0])
        assert result == 5, f"Test 67 failed: got {result}, expected {5}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = majorityElement([5, 5, 5, 5, 7, 31, 0])
        assert result == 5, f"Test 68 failed: got {result}, expected {5}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = majorityElement([5, 0, 5, 5, 5, 6, 7])
        assert result == 5, f"Test 69 failed: got {result}, expected {5}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = majorityElement([6, 5, 5, 5, 7])
        assert result == 5, f"Test 70 failed: got {result}, expected {5}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = majorityElement([5, 5, 5, 5, 5, 6, 7, 60])
        assert result == 5, f"Test 71 failed: got {result}, expected {5}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = majorityElement([2])
        assert result == 2, f"Test 72 failed: got {result}, expected {2}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = majorityElement([3, 3])
        assert result == 3, f"Test 73 failed: got {result}, expected {3}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = majorityElement([1, 0, 10, 0, 0])
        assert result == 0, f"Test 74 failed: got {result}, expected {0}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = majorityElement([0])
        assert result == 0, f"Test 75 failed: got {result}, expected {0}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = majorityElement([0, 0, 98, 0])
        assert result == 0, f"Test 76 failed: got {result}, expected {0}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = majorityElement([0, 0, 31])
        assert result == 0, f"Test 77 failed: got {result}, expected {0}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = majorityElement([0, 0, 90])
        assert result == 0, f"Test 78 failed: got {result}, expected {0}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = majorityElement([0, 0, 11, 0])
        assert result == 0, f"Test 79 failed: got {result}, expected {0}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = majorityElement([0, 0])
        assert result == 0, f"Test 80 failed: got {result}, expected {0}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = majorityElement([0, 0])
        assert result == 0, f"Test 81 failed: got {result}, expected {0}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = majorityElement([0, 0, 12])
        assert result == 0, f"Test 82 failed: got {result}, expected {0}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = majorityElement([0, 0, 16])
        assert result == 0, f"Test 83 failed: got {result}, expected {0}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = majorityElement([0, 0, 14, 0])
        assert result == 0, f"Test 84 failed: got {result}, expected {0}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = majorityElement([0, 0, 0])
        assert result == 0, f"Test 85 failed: got {result}, expected {0}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = majorityElement([1, 0, 0])
        assert result == 0, f"Test 86 failed: got {result}, expected {0}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = majorityElement([8])
        assert result == 8, f"Test 87 failed: got {result}, expected {8}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = majorityElement([1])
        assert result == 1, f"Test 88 failed: got {result}, expected {1}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = majorityElement([5, 5, 0])
        assert result == 5, f"Test 89 failed: got {result}, expected {5}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = majorityElement([5])
        assert result == 5, f"Test 90 failed: got {result}, expected {5}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = majorityElement([100])
        assert result == 100, f"Test 91 failed: got {result}, expected {100}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = majorityElement([1, 0, 1])
        assert result == 1, f"Test 92 failed: got {result}, expected {1}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = majorityElement([1, 2, 1, 1])
        assert result == 1, f"Test 93 failed: got {result}, expected {1}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = majorityElement([2, 2, 1, 2])
        assert result == 2, f"Test 94 failed: got {result}, expected {2}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = majorityElement([2, 2, 0])
        assert result == 2, f"Test 95 failed: got {result}, expected {2}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = majorityElement([4, 4, 4, 2, 3, 4, 0])
        assert result == 4, f"Test 96 failed: got {result}, expected {4}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = majorityElement([4, 3, 2, 4, 4, 4])
        assert result == 4, f"Test 97 failed: got {result}, expected {4}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = majorityElement([4, 4, 4, 2, 3, 4, 28])
        assert result == 4, f"Test 98 failed: got {result}, expected {4}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = majorityElement([4, 4, 3, 4])
        assert result == 4, f"Test 99 failed: got {result}, expected {4}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = majorityElement([4, 4, 4, 4, 6, 10])
        assert result == 4, f"Test 100 failed: got {result}, expected {4}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = majorityElement([0, 4, 3, 50, 4, 4, 4])
        assert result == 4, f"Test 101 failed: got {result}, expected {4}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = majorityElement([4, 4, 4, 4, 3, 4, 0])
        assert result == 4, f"Test 102 failed: got {result}, expected {4}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = majorityElement([0, 4, 2, 4, 4, 4])
        assert result == 4, f"Test 103 failed: got {result}, expected {4}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = majorityElement([7, 7, 7, 9, 7, 1, 0])
        assert result == 7, f"Test 104 failed: got {result}, expected {7}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = majorityElement([7, 8, 7, 7, 7, 1, 19])
        assert result == 7, f"Test 105 failed: got {result}, expected {7}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = majorityElement([7, 7, 7, 0, 7, 1, 18])
        assert result == 7, f"Test 106 failed: got {result}, expected {7}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = majorityElement([1, 7, 9, 7, 7, 8, 7])
        assert result == 7, f"Test 107 failed: got {result}, expected {7}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = majorityElement([7, 8, 7, 7, 7, 1])
        assert result == 7, f"Test 108 failed: got {result}, expected {7}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = majorityElement([10, 8, 11, 10, 10])
        assert result == 10, f"Test 109 failed: got {result}, expected {10}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = majorityElement([10, 10, 0, 10, 12, 10, 13, 10, 0])
        assert result == 10, f"Test 110 failed: got {result}, expected {10}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = majorityElement([10, 10, 11, 10, 12, 10, 12, 10])
        assert result == 10, f"Test 111 failed: got {result}, expected {10}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = majorityElement([10, 10, 12, 10, 0, 10, 10])
        assert result == 10, f"Test 112 failed: got {result}, expected {10}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = majorityElement([10, 13, 10, 12, 10, 11, 10, 10])
        assert result == 10, f"Test 113 failed: got {result}, expected {10}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = majorityElement([3, 3, 3, 2, 50])
        assert result == 3, f"Test 114 failed: got {result}, expected {3}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = majorityElement([3, 0, 6, 6, 6, 6])
        assert result == 6, f"Test 115 failed: got {result}, expected {6}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = majorityElement([3, 2, 6, 6, 6, 6])
        assert result == 6, f"Test 116 failed: got {result}, expected {6}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = majorityElement([9, 4, 9, 3, 9, 2, 9, 1, 9])
        assert result == 9, f"Test 117 failed: got {result}, expected {9}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = majorityElement([42, 9, 1, 9, 9, 3, 9, 4, 9])
        assert result == 9, f"Test 118 failed: got {result}, expected {9}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = majorityElement([9, 9, 2, 9, 3, 9, 4, 9])
        assert result == 9, f"Test 119 failed: got {result}, expected {9}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = majorityElement([2, 2, 2, 2, 2, 4, 5, 6])
        assert result == 2, f"Test 120 failed: got {result}, expected {2}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = majorityElement([8, 8, 8, 8, 1, 0, 2])
        assert result == 8, f"Test 121 failed: got {result}, expected {8}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = majorityElement([8, 8, 8, 8, 0, 1, 2])
        assert result == 8, f"Test 122 failed: got {result}, expected {8}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = majorityElement([15, 15, 15, 0, 32])
        assert result == 15, f"Test 123 failed: got {result}, expected {15}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = majorityElement([15, 23, 15, 15, 2, 15])
        assert result == 15, f"Test 124 failed: got {result}, expected {15}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = majorityElement([20, 15, 2, 15, 15, 0, 15])
        assert result == 15, f"Test 125 failed: got {result}, expected {15}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = majorityElement([0, 0, 15, 2, 15, 15, 15])
        assert result == 15, f"Test 126 failed: got {result}, expected {15}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = majorityElement([15, 0, 15, 15, 2, 15, 0])
        assert result == 15, f"Test 127 failed: got {result}, expected {15}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = majorityElement([15, 2, 15, 15, 0, 15, 99])
        assert result == 15, f"Test 128 failed: got {result}, expected {15}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = majorityElement([15, 2, 15, 15, 0, 15, 0])
        assert result == 15, f"Test 129 failed: got {result}, expected {15}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = majorityElement([15, 2, 15, 15, 0, 15])
        assert result == 15, f"Test 130 failed: got {result}, expected {15}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = majorityElement([15, 2, 15, 0, 15])
        assert result == 15, f"Test 131 failed: got {result}, expected {15}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = majorityElement([100, 100, 52, 100, 60, 100, 70, 100, 80, 100, 90])
        assert result == 100, f"Test 132 failed: got {result}, expected {100}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = majorityElement([100, 100, 100, 60, 100, 70, 100, 80, 100, 90])
        assert result == 100, f"Test 133 failed: got {result}, expected {100}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = majorityElement([90, 100, 80, 100, 70, 100, 60, 100, 50, 100, 100])
        assert result == 100, f"Test 134 failed: got {result}, expected {100}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = majorityElement([3, 2, 1, 1, 1, 1])
        assert result == 1, f"Test 135 failed: got {result}, expected {1}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = majorityElement([0, 2, 2, 1, 1, 1, 1])
        assert result == 1, f"Test 136 failed: got {result}, expected {1}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = majorityElement([1, 1, 1, 2, 3])
        assert result == 1, f"Test 137 failed: got {result}, expected {1}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = majorityElement([1, 1, 1, 1, 2, 2])
        assert result == 1, f"Test 138 failed: got {result}, expected {1}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = majorityElement([12, 12, 13, 12, 14, 12, 80, 12, 16, 12])
        assert result == 12, f"Test 139 failed: got {result}, expected {12}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = majorityElement([12, 16, 12, 15, 12, 14, 12, 13, 12])
        assert result == 12, f"Test 140 failed: got {result}, expected {12}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = majorityElement([12, 12, 13, 12, 14, 12, 15, 12, 12, 2, 52])
        assert result == 12, f"Test 141 failed: got {result}, expected {12}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = majorityElement([12, 12, 9, 12, 14, 12, 12, 16, 12, 0])
        assert result == 12, f"Test 142 failed: got {result}, expected {12}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = majorityElement([12, 12, 13, 12, 12, 0, 12, 16])
        assert result == 12, f"Test 143 failed: got {result}, expected {12}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = majorityElement([12, 12, 13, 12, 14, 12, 15, 12, 16, 12, 19])
        assert result == 12, f"Test 144 failed: got {result}, expected {12}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = majorityElement([28, 12, 16, 12, 12, 14, 12, 13, 12, 12, 0])
        assert result == 12, f"Test 145 failed: got {result}, expected {12}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = majorityElement([12, 12, 13, 12, 15, 12, 15, 12, 16, 12, 0, 12])
        assert result == 12, f"Test 146 failed: got {result}, expected {12}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = majorityElement([12, 12, 13, 12, 14, 12, 13, 12, 16])
        assert result == 12, f"Test 147 failed: got {result}, expected {12}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = majorityElement([5, 4, 5, 5, 4, 5, 6, 5, 0])
        assert result == 5, f"Test 148 failed: got {result}, expected {5}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = majorityElement([5, 5, 5, 4, 5, 5, 4, 5])
        assert result == 5, f"Test 149 failed: got {result}, expected {5}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = majorityElement([5, 6, 5, 4, 5, 5])
        assert result == 5, f"Test 150 failed: got {result}, expected {5}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = majorityElement([5, 6, 5, 80, 5, 4, 5])
        assert result == 5, f"Test 151 failed: got {result}, expected {5}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = majorityElement([5, 4, 5, 5, 4, 5, 6, 5, 12])
        assert result == 5, f"Test 152 failed: got {result}, expected {5}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = majorityElement([5, 6, 5, 4, 5, 5, 4, 5])
        assert result == 5, f"Test 153 failed: got {result}, expected {5}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = majorityElement([5, 4, 5, 5, 4, 5, 6])
        assert result == 5, f"Test 154 failed: got {result}, expected {5}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = majorityElement([20, 25, 20, 24, 20, 23, 20, 22, 20, 21, 20])
        assert result == 20, f"Test 155 failed: got {result}, expected {20}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = majorityElement([20, 21, 20, 22, 20, 25, 20, 24, 20, 25, 20])
        assert result == 20, f"Test 156 failed: got {result}, expected {20}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = majorityElement([3, 0, 3, 3, 1, 3, 2, 3, 3, 0])
        assert result == 3, f"Test 157 failed: got {result}, expected {3}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = majorityElement([3, 0, 3, 3, 1, 3, 70, 3, 3, 97])
        assert result == 3, f"Test 158 failed: got {result}, expected {3}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = majorityElement([0, 3, 3, 2, 3, 1, 3, 3, 26])
        assert result == 3, f"Test 159 failed: got {result}, expected {3}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = majorityElement([3, 0, 3, 1, 3, 2, 3, 3])
        assert result == 3, f"Test 160 failed: got {result}, expected {3}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = majorityElement([3, 0, 3, 3, 1, 3, 2, 3, 3, 100])
        assert result == 3, f"Test 161 failed: got {result}, expected {3}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = majorityElement([3, 0, 3, 3, 28, 3, 1, 3, 3, 0, 0])
        assert result == 3, f"Test 162 failed: got {result}, expected {3}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = majorityElement([3, 0, 3, 3, 1, 3, 2, 3, 3, 0, 18])
        assert result == 3, f"Test 163 failed: got {result}, expected {3}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = majorityElement([4, 11, 3, 11, 2, 11, 11, 11])
        assert result == 11, f"Test 164 failed: got {result}, expected {11}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = majorityElement([1, 4, 11, 11, 2, 11, 11, 11])
        assert result == 11, f"Test 165 failed: got {result}, expected {11}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = majorityElement([11, 11, 11, 2, 11, 3, 11])
        assert result == 11, f"Test 166 failed: got {result}, expected {11}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = majorityElement([11, 11, 11, 11, 3, 11, 4, 26, 11, 0])
        assert result == 11, f"Test 167 failed: got {result}, expected {11}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = majorityElement([11, 11, 11, 2, 11, 11, 4, 98, 6])
        assert result == 11, f"Test 168 failed: got {result}, expected {11}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = majorityElement([42, 42, 42, 42, 1, 2, 3])
        assert result == 42, f"Test 169 failed: got {result}, expected {42}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = majorityElement([3, 1, 42, 42, 42, 42, 41])
        assert result == 42, f"Test 170 failed: got {result}, expected {42}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = majorityElement([7, 7, 8, 7, 9, 7, 0])
        assert result == 7, f"Test 171 failed: got {result}, expected {7}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = majorityElement([7, 8, 7, 7])
        assert result == 7, f"Test 172 failed: got {result}, expected {7}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = majorityElement([7, 7, 8, 7, 9, 7, 23])
        assert result == 7, f"Test 173 failed: got {result}, expected {7}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = majorityElement([7, 0, 7, 7, 32])
        assert result == 7, f"Test 174 failed: got {result}, expected {7}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = majorityElement([8, 7, 7, 9, 7])
        assert result == 7, f"Test 175 failed: got {result}, expected {7}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = majorityElement([7, 9, 7, 8, 7, 7, 0])
        assert result == 7, f"Test 176 failed: got {result}, expected {7}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = majorityElement([7, 7, 8, 7, 9, 7, 26])
        assert result == 7, f"Test 177 failed: got {result}, expected {7}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = majorityElement([30, 30, 30, 30, 30, 31, 31, 33])
        assert result == 30, f"Test 178 failed: got {result}, expected {30}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = majorityElement([33, 32, 31, 30, 30, 30, 30, 30, 0])
        assert result == 30, f"Test 179 failed: got {result}, expected {30}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = majorityElement([30, 30, 30, 30, 30, 31, 32, 34])
        assert result == 30, f"Test 180 failed: got {result}, expected {30}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = majorityElement([30, 30, 30, 30, 30, 32, 33])
        assert result == 30, f"Test 181 failed: got {result}, expected {30}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = majorityElement([0, 33, 32, 31, 30, 30, 30, 30, 30])
        assert result == 30, f"Test 182 failed: got {result}, expected {30}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = majorityElement([33, 32, 31, 30, 30, 30, 30, 30])
        assert result == 30, f"Test 183 failed: got {result}, expected {30}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = majorityElement([26, 33, 31, 30, 30, 30, 30, 30, 0])
        assert result == 30, f"Test 184 failed: got {result}, expected {30}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = majorityElement([2, 15, 2, 7, 2, 6, 2, 5, 2, 4, 2, 3, 2])
        assert result == 2, f"Test 185 failed: got {result}, expected {2}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = majorityElement([2, 3, 2, 4, 2, 2, 6, 2, 7, 2, 8, 2, 0])
        assert result == 2, f"Test 186 failed: got {result}, expected {2}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = majorityElement([2, 3, 2, 3, 2, 5, 2, 6, 2, 7, 2, 8, 2])
        assert result == 2, f"Test 187 failed: got {result}, expected {2}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = majorityElement([0, 2, 8, 2, 7, 2, 6, 2, 2, 4, 2, 3, 2])
        assert result == 2, f"Test 188 failed: got {result}, expected {2}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = majorityElement([2, 3, 2, 4, 2, 5, 2, 2, 7, 2, 2, 0])
        assert result == 2, f"Test 189 failed: got {result}, expected {2}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = majorityElement([9, 9, 9, 9, 9, 2, 3, 4, 5])
        assert result == 9, f"Test 190 failed: got {result}, expected {9}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = majorityElement([9, 9, 9, 9, 9, 9, 2, 3, 4, 5, 0])
        assert result == 9, f"Test 191 failed: got {result}, expected {9}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = majorityElement([5, 4, 3, 2, 1, 9, 9, 9, 9, 9, 9])
        assert result == 9, f"Test 192 failed: got {result}, expected {9}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = majorityElement([4, 3, 2, 1, 9, 9, 9, 9, 9, 9])
        assert result == 9, f"Test 193 failed: got {result}, expected {9}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = majorityElement([17, 14, 16, 15, 14, 14, 14])
        assert result == 14, f"Test 194 failed: got {result}, expected {14}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = majorityElement([0, 14, 15, 14, 14])
        assert result == 14, f"Test 195 failed: got {result}, expected {14}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = majorityElement([32, 14, 14, 14])
        assert result == 14, f"Test 196 failed: got {result}, expected {14}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = majorityElement([1, 14, 16, 15, 14, 14, 14])
        assert result == 14, f"Test 197 failed: got {result}, expected {14}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = majorityElement([6, 1, 6, 2, 6, 3, 6, 4, 6, 5, 6, 6, 0])
        assert result == 6, f"Test 198 failed: got {result}, expected {6}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = majorityElement([6, 6, 2, 6, 3, 6, 4, 6, 5, 6, 6, 0])
        assert result == 6, f"Test 199 failed: got {result}, expected {6}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = majorityElement([6, 6, 2, 6, 3, 6, 4, 6, 5, 6, 6])
        assert result == 6, f"Test 200 failed: got {result}, expected {6}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = majorityElement([4, 6, 6, 5, 6, 4, 6, 3, 6, 2, 6, 1, 6])
        assert result == 6, f"Test 201 failed: got {result}, expected {6}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = majorityElement([50, 6, 2, 6, 13, 6, 4, 6, 5, 6, 6])
        assert result == 6, f"Test 202 failed: got {result}, expected {6}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = majorityElement([0, 0, 3, 0, 2, 0, 1, 0, 0])
        assert result == 0, f"Test 203 failed: got {result}, expected {0}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = majorityElement([19, 0, 60, 0, 3, 0, 2, 0, 1, 0, 0])
        assert result == 0, f"Test 204 failed: got {result}, expected {0}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = majorityElement([0, 3, 0, 2, 0, 1, 0])
        assert result == 0, f"Test 205 failed: got {result}, expected {0}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = majorityElement([0, 0, 0, 3, 0, 0, 70, 32])
        assert result == 0, f"Test 206 failed: got {result}, expected {0}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = majorityElement([0, 3, 0, 2, 0, 1, 0, 0, 0])
        assert result == 0, f"Test 207 failed: got {result}, expected {0}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = majorityElement([0, 1, 0, 2, 0, 3, 0, 0])
        assert result == 0, f"Test 208 failed: got {result}, expected {0}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = majorityElement([29, 0, 0, 0, 3, 0])
        assert result == 0, f"Test 209 failed: got {result}, expected {0}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = majorityElement([99, 99, 98, 99, 97, 99, 96, 99, 95, 99, 13])
        assert result == 99, f"Test 210 failed: got {result}, expected {99}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = majorityElement([99, 99, 98, 99, 97, 99, 96, 99, 95, 99, 0])
        assert result == 99, f"Test 211 failed: got {result}, expected {99}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = majorityElement([99, 99, 98, 99, 97, 99, 96, 99, 99, 50, 0])
        assert result == 99, f"Test 212 failed: got {result}, expected {99}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = majorityElement([0, 99, 95, 99, 96, 99, 97, 99, 98, 99, 99])
        assert result == 99, f"Test 213 failed: got {result}, expected {99}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = majorityElement([99, 95, 99, 96, 99, 97, 99, 1, 99, 99, 0])
        assert result == 99, f"Test 214 failed: got {result}, expected {99}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = majorityElement([18, 21, 20, 19, 18, 18, 18, 18])
        assert result == 18, f"Test 215 failed: got {result}, expected {18}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = majorityElement([18, 18, 18, 18, 22, 20, 21, 20, 18])
        assert result == 18, f"Test 216 failed: got {result}, expected {18}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = majorityElement([21, 19, 18, 18, 18, 18])
        assert result == 18, f"Test 217 failed: got {result}, expected {18}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = majorityElement([18, 18, 18, 18, 19, 20, 21, 18, 34])
        assert result == 18, f"Test 218 failed: got {result}, expected {18}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = majorityElement([18, 18, 18, 18, 19, 20, 21, 18, 0])
        assert result == 18, f"Test 219 failed: got {result}, expected {18}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = majorityElement([18, 21, 20, 19, 18, 18, 18])
        assert result == 18, f"Test 220 failed: got {result}, expected {18}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = majorityElement([25, 26, 25, 27, 25, 28, 25, 28, 25])
        assert result == 25, f"Test 221 failed: got {result}, expected {25}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = majorityElement([25, 26, 25, 27, 25, 28, 25, 25])
        assert result == 25, f"Test 222 failed: got {result}, expected {25}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = majorityElement([7, 6, 5, 3, 2, 4, 4, 4, 4, 4, 4])
        assert result == 4, f"Test 223 failed: got {result}, expected {4}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = majorityElement([4, 4, 4, 4, 4, 4, 2, 5, 6, 7, 33])
        assert result == 4, f"Test 224 failed: got {result}, expected {4}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = majorityElement([4, 4, 4, 4, 4, 2, 5, 0])
        assert result == 4, f"Test 225 failed: got {result}, expected {4}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = majorityElement([6, 5, 3, 2, 4, 4, 4, 4, 4, 4, 0])
        assert result == 4, f"Test 226 failed: got {result}, expected {4}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = majorityElement([61])
        assert result == 61, f"Test 227 failed: got {result}, expected {61}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = majorityElement([60])
        assert result == 60, f"Test 228 failed: got {result}, expected {60}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = majorityElement([2, 0, 99, 0, 0])
        assert result == 0, f"Test 229 failed: got {result}, expected {0}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = majorityElement([2, 0, 0])
        assert result == 0, f"Test 230 failed: got {result}, expected {0}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = majorityElement([0, 15, 0])
        assert result == 0, f"Test 231 failed: got {result}, expected {0}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = majorityElement([29])
        assert result == 29, f"Test 232 failed: got {result}, expected {29}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = majorityElement([2, 3, 0, 0, 0])
        assert result == 0, f"Test 233 failed: got {result}, expected {0}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = majorityElement([0, 0, 3, 0])
        assert result == 0, f"Test 234 failed: got {result}, expected {0}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = majorityElement([4])
        assert result == 4, f"Test 235 failed: got {result}, expected {4}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = majorityElement([4, 5, 5])
        assert result == 5, f"Test 236 failed: got {result}, expected {5}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = majorityElement([4, 4, 5])
        assert result == 4, f"Test 237 failed: got {result}, expected {4}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = majorityElement([9])
        assert result == 9, f"Test 238 failed: got {result}, expected {9}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = majorityElement([2, 1, 1, 0, 0, 0, 0])
        assert result == 0, f"Test 239 failed: got {result}, expected {0}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = majorityElement([4, 4, 4, 0, 4, 3])
        assert result == 4, f"Test 240 failed: got {result}, expected {4}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = majorityElement([3, 3, 3, 4])
        assert result == 3, f"Test 241 failed: got {result}, expected {3}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = majorityElement([4, 3, 3, 3])
        assert result == 3, f"Test 242 failed: got {result}, expected {3}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
