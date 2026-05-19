# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def maxOfList(lst):
2: ✓     return max(lst)
```

## Complete Test File

```python
def maxOfList(lst):
    return max(lst)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = maxOfList([1, 2, 3])
        assert result == 3, f"Test 1 failed: got {result}, expected {3}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = maxOfList([5, 5, 5])
        assert result == 5, f"Test 2 failed: got {result}, expected {5}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = maxOfList([10, 1, 9])
        assert result == 10, f"Test 3 failed: got {result}, expected {10}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = maxOfList([7])
        assert result == 7, f"Test 4 failed: got {result}, expected {7}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = maxOfList([0, 0, 0, 0])
        assert result == 0, f"Test 5 failed: got {result}, expected {0}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = maxOfList([2, 9, 3, 9, 1])
        assert result == 9, f"Test 6 failed: got {result}, expected {9}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = maxOfList([0, 100, 0, 100, 0])
        assert result == 100, f"Test 7 failed: got {result}, expected {100}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = maxOfList([42, 17, 42, 3, 41])
        assert result == 42, f"Test 8 failed: got {result}, expected {42}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == 9, f"Test 9 failed: got {result}, expected {9}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = maxOfList([2, 2, 1, 0, 0, 0])
        assert result == 2, f"Test 10 failed: got {result}, expected {2}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = maxOfList([3, 0])
        assert result == 3, f"Test 11 failed: got {result}, expected {3}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = maxOfList([1, 2, 3, 0, 0])
        assert result == 3, f"Test 12 failed: got {result}, expected {3}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = maxOfList([11, 5])
        assert result == 11, f"Test 13 failed: got {result}, expected {11}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = maxOfList([10, 9])
        assert result == 10, f"Test 14 failed: got {result}, expected {10}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = maxOfList([1, 9, 7, 18446744073709551616])
        assert result == 18446744073709551616, f"Test 15 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = maxOfList([23, 7])
        assert result == 23, f"Test 16 failed: got {result}, expected {23}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = maxOfList([0, 0, 6])
        assert result == 6, f"Test 17 failed: got {result}, expected {6}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = maxOfList([0, 0, 0, 0, 0, 24])
        assert result == 24, f"Test 18 failed: got {result}, expected {24}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = maxOfList([0, 4, 1])
        assert result == 4, f"Test 19 failed: got {result}, expected {4}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = maxOfList([1, 456, 1])
        assert result == 456, f"Test 20 failed: got {result}, expected {456}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = maxOfList([41, 1])
        assert result == 41, f"Test 21 failed: got {result}, expected {41}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = maxOfList([0, 1, 3, 0, 2])
        assert result == 3, f"Test 22 failed: got {result}, expected {3}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = maxOfList([0, 5, 5, 0])
        assert result == 5, f"Test 23 failed: got {result}, expected {5}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = maxOfList([5, 5, 5, 5, 0, 6, 0, 0])
        assert result == 6, f"Test 24 failed: got {result}, expected {6}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = maxOfList([1, 2, 3, 4, 0])
        assert result == 4, f"Test 25 failed: got {result}, expected {4}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = maxOfList([1000000, 3, 2, 1, 0])
        assert result == 1000000, f"Test 26 failed: got {result}, expected {1000000}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = maxOfList([5, 6, 3, 2, 1])
        assert result == 6, f"Test 27 failed: got {result}, expected {6}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = maxOfList([0, 2, 9, 9, 1, 0])
        assert result == 9, f"Test 28 failed: got {result}, expected {9}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = maxOfList([2, 11, 3, 9, 1])
        assert result == 11, f"Test 29 failed: got {result}, expected {11}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = maxOfList([0, 42, 999999, 1, 9, 3, 7, 2])
        assert result == 999999, f"Test 30 failed: got {result}, expected {999999}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = maxOfList([7, 8, 8, 7, 0, 999999999, 2])
        assert result == 999999999, f"Test 31 failed: got {result}, expected {999999999}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = maxOfList([7, 7, 9, 7])
        assert result == 9, f"Test 32 failed: got {result}, expected {9}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = maxOfList([7, 8, 7, 0])
        assert result == 8, f"Test 33 failed: got {result}, expected {8}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = maxOfList([7, 7, 7, 0])
        assert result == 7, f"Test 34 failed: got {result}, expected {7}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = maxOfList([7, 8, 7, 7])
        assert result == 8, f"Test 35 failed: got {result}, expected {8}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = maxOfList([8, 20, 7, 7, 16])
        assert result == 20, f"Test 36 failed: got {result}, expected {20}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = maxOfList([7, 7, 7, 3999999996, 8])
        assert result == 3999999996, f"Test 37 failed: got {result}, expected {3999999996}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = maxOfList([7, 18446744073709551615, 7, 8])
        assert result == 18446744073709551615, f"Test 38 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = maxOfList([0, 100, 0, 100, 0, 0])
        assert result == 100, f"Test 39 failed: got {result}, expected {100}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = maxOfList([0, 200, 0])
        assert result == 200, f"Test 40 failed: got {result}, expected {200}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = maxOfList([16, 100, 1, 100, 0])
        assert result == 100, f"Test 41 failed: got {result}, expected {100}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = maxOfList([0, 100, 0, 100, 0, 0, 0])
        assert result == 100, f"Test 42 failed: got {result}, expected {100}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = maxOfList([42, 17, 42, 3, 41, 0, 0])
        assert result == 42, f"Test 43 failed: got {result}, expected {42}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = maxOfList([3, 1, 4, 1, 7, 9, 2, 6, 0, 9])
        assert result == 9, f"Test 44 failed: got {result}, expected {9}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2])
        assert result == 9, f"Test 45 failed: got {result}, expected {9}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = maxOfList([2, 9, 5, 1, 4, 1, 3, 0, 0])
        assert result == 9, f"Test 46 failed: got {result}, expected {9}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = maxOfList([9, 2, 6, 5, 101, 5, 0])
        assert result == 101, f"Test 47 failed: got {result}, expected {101}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = maxOfList([101, 5, 6, 2, 9, 0])
        assert result == 101, f"Test 48 failed: got {result}, expected {101}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = maxOfList([9, 2, 6, 18446744073709551615, 3, 5])
        assert result == 18446744073709551615, f"Test 49 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = maxOfList([999999, 1000001, 0, 7])
        assert result == 1000001, f"Test 50 failed: got {result}, expected {1000001}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = maxOfList([123, 456, 20, 10, 11])
        assert result == 456, f"Test 51 failed: got {result}, expected {456}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = maxOfList([5, 11, 10, 789, 100])
        assert result == 789, f"Test 52 failed: got {result}, expected {789}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = maxOfList([15, 23, 8, 23, 4, 23, 0])
        assert result == 23, f"Test 53 failed: got {result}, expected {23}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = maxOfList([15, 0, 8, 23, 4, 23, 0])
        assert result == 23, f"Test 54 failed: got {result}, expected {23}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = maxOfList([1, 2, 14, 6])
        assert result == 14, f"Test 55 failed: got {result}, expected {14}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
