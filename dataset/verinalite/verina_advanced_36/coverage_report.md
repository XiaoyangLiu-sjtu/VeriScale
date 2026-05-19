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
        result = majorityElement([2, 1, 2, 3, 2])
        assert result == 2, f"Test 6 failed: got {result}, expected {2}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = majorityElement([7, 8, 7, 7, 9, 7, 1])
        assert result == 7, f"Test 7 failed: got {result}, expected {7}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = majorityElement([5, 4, 5, 5, 4, 5, 6, 5])
        assert result == 5, f"Test 8 failed: got {result}, expected {5}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = majorityElement([20, 21, 20, 22, 20, 23, 20, 24, 20, 25, 20])
        assert result == 20, f"Test 9 failed: got {result}, expected {20}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = majorityElement([30, 30, 30, 30, 30, 31, 32, 33])
        assert result == 30, f"Test 10 failed: got {result}, expected {30}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = majorityElement([2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2])
        assert result == 2, f"Test 11 failed: got {result}, expected {2}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = majorityElement([14, 14, 14, 15, 16, 14, 17])
        assert result == 14, f"Test 12 failed: got {result}, expected {14}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = majorityElement([25, 26, 25, 27, 25, 28, 25, 29, 25])
        assert result == 25, f"Test 13 failed: got {result}, expected {25}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = majorityElement([4, 4, 4, 4, 4, 4, 2, 3, 5, 6, 7])
        assert result == 4, f"Test 14 failed: got {result}, expected {4}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = majorityElement([3, 4, 2, 3, 3, 3])
        assert result == 3, f"Test 15 failed: got {result}, expected {3}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = majorityElement([3, 3, 4, 3, 3, 3, 29])
        assert result == 3, f"Test 16 failed: got {result}, expected {3}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = majorityElement([3, 3, 4, 2, 3, 3, 3, 0, 0])
        assert result == 3, f"Test 17 failed: got {result}, expected {3}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = majorityElement([3, 3, 4, 2, 3, 3, 3, 0])
        assert result == 3, f"Test 18 failed: got {result}, expected {3}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = majorityElement([1, 1, 2, 1, 3, 1, 1, 61])
        assert result == 1, f"Test 19 failed: got {result}, expected {1}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = majorityElement([1, 1, 2, 1, 3, 1, 1, 30, 6])
        assert result == 1, f"Test 20 failed: got {result}, expected {1}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = majorityElement([1, 1, 3, 1, 2, 1, 1, 25])
        assert result == 1, f"Test 21 failed: got {result}, expected {1}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = majorityElement([9, 9, 9, 9, 1, 3, 96])
        assert result == 9, f"Test 22 failed: got {result}, expected {9}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = majorityElement([3, 2, 1, 9, 9, 9, 9])
        assert result == 9, f"Test 23 failed: got {result}, expected {9}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = majorityElement([5, 1, 5, 5, 5, 6, 7])
        assert result == 5, f"Test 24 failed: got {result}, expected {5}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = majorityElement([5, 5, 5, 5, 5, 6, 7, 0])
        assert result == 5, f"Test 25 failed: got {result}, expected {5}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = majorityElement([5, 5, 5, 5, 26, 6, 4])
        assert result == 5, f"Test 26 failed: got {result}, expected {5}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = majorityElement([7, 6, 5, 5, 5, 5, 5, 0])
        assert result == 5, f"Test 27 failed: got {result}, expected {5}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = majorityElement([7, 6, 5, 5, 5, 5, 0])
        assert result == 5, f"Test 28 failed: got {result}, expected {5}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = majorityElement([7, 6, 5, 5, 5, 5, 5])
        assert result == 5, f"Test 29 failed: got {result}, expected {5}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = majorityElement([5, 5, 5, 5, 6, 7, 0])
        assert result == 5, f"Test 30 failed: got {result}, expected {5}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = majorityElement([5, 5, 5, 5, 7, 31, 0])
        assert result == 5, f"Test 31 failed: got {result}, expected {5}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = majorityElement([5, 0, 5, 5, 5, 6, 7])
        assert result == 5, f"Test 32 failed: got {result}, expected {5}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = majorityElement([6, 5, 5, 5, 7])
        assert result == 5, f"Test 33 failed: got {result}, expected {5}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = majorityElement([5, 5, 5, 5, 5, 6, 7, 60])
        assert result == 5, f"Test 34 failed: got {result}, expected {5}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = majorityElement([4, 4, 4, 2, 3, 4, 28])
        assert result == 4, f"Test 35 failed: got {result}, expected {4}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = majorityElement([0, 4, 3, 50, 4, 4, 4])
        assert result == 4, f"Test 36 failed: got {result}, expected {4}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = majorityElement([7, 8, 7, 7, 7, 1])
        assert result == 7, f"Test 37 failed: got {result}, expected {7}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = majorityElement([15, 2, 15, 15, 0, 15, 99])
        assert result == 15, f"Test 38 failed: got {result}, expected {15}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = majorityElement([28, 12, 16, 12, 12, 14, 12, 13, 12, 12, 0])
        assert result == 12, f"Test 39 failed: got {result}, expected {12}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = majorityElement([5, 4, 5, 5, 4, 5, 6, 5, 0])
        assert result == 5, f"Test 40 failed: got {result}, expected {5}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = majorityElement([5, 4, 5, 5, 4, 5, 6])
        assert result == 5, f"Test 41 failed: got {result}, expected {5}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = majorityElement([3, 0, 3, 3, 1, 3, 70, 3, 3, 97])
        assert result == 3, f"Test 42 failed: got {result}, expected {3}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = majorityElement([0, 3, 3, 2, 3, 1, 3, 3, 26])
        assert result == 3, f"Test 43 failed: got {result}, expected {3}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = majorityElement([3, 0, 3, 3, 1, 3, 2, 3, 3, 100])
        assert result == 3, f"Test 44 failed: got {result}, expected {3}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = majorityElement([3, 1, 42, 42, 42, 42, 41])
        assert result == 42, f"Test 45 failed: got {result}, expected {42}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = majorityElement([7, 0, 7, 7, 32])
        assert result == 7, f"Test 46 failed: got {result}, expected {7}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = majorityElement([33, 32, 31, 30, 30, 30, 30, 30, 0])
        assert result == 30, f"Test 47 failed: got {result}, expected {30}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = majorityElement([0, 33, 32, 31, 30, 30, 30, 30, 30])
        assert result == 30, f"Test 48 failed: got {result}, expected {30}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = majorityElement([33, 32, 31, 30, 30, 30, 30, 30])
        assert result == 30, f"Test 49 failed: got {result}, expected {30}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = majorityElement([26, 33, 31, 30, 30, 30, 30, 30, 0])
        assert result == 30, f"Test 50 failed: got {result}, expected {30}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = majorityElement([2, 3, 2, 4, 2, 2, 6, 2, 7, 2, 8, 2, 0])
        assert result == 2, f"Test 51 failed: got {result}, expected {2}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = majorityElement([21, 19, 18, 18, 18, 18])
        assert result == 18, f"Test 52 failed: got {result}, expected {18}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = majorityElement([7, 6, 5, 3, 2, 4, 4, 4, 4, 4, 4])
        assert result == 4, f"Test 53 failed: got {result}, expected {4}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = majorityElement([6, 5, 3, 2, 4, 4, 4, 4, 4, 4, 0])
        assert result == 4, f"Test 54 failed: got {result}, expected {4}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
