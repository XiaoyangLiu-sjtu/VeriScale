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
        result = maxOfList([1, 0])
        assert result == 1, f"Test 6 failed: got {result}, expected {1}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = maxOfList([0, 1])
        assert result == 1, f"Test 7 failed: got {result}, expected {1}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = maxOfList([5, 5, 5, 5])
        assert result == 5, f"Test 8 failed: got {result}, expected {5}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = maxOfList([1, 2, 3, 4, 5])
        assert result == 5, f"Test 9 failed: got {result}, expected {5}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = maxOfList([5, 4, 3, 2, 1])
        assert result == 5, f"Test 10 failed: got {result}, expected {5}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = maxOfList([2, 9, 3, 9, 1])
        assert result == 9, f"Test 11 failed: got {result}, expected {9}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = maxOfList([7, 7, 8, 7])
        assert result == 8, f"Test 12 failed: got {result}, expected {8}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = maxOfList([8, 7, 7, 7])
        assert result == 8, f"Test 13 failed: got {result}, expected {8}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = maxOfList([7, 7, 7, 8])
        assert result == 8, f"Test 14 failed: got {result}, expected {8}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = maxOfList([0, 100, 0, 100, 0])
        assert result == 100, f"Test 15 failed: got {result}, expected {100}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = maxOfList([42, 17, 42, 3, 41])
        assert result == 42, f"Test 16 failed: got {result}, expected {42}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == 9, f"Test 17 failed: got {result}, expected {9}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = maxOfList([9, 2, 6, 5, 3, 5])
        assert result == 9, f"Test 18 failed: got {result}, expected {9}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = maxOfList([1000000, 999999, 1000001])
        assert result == 1000001, f"Test 19 failed: got {result}, expected {1000001}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = maxOfList([123, 456, 789, 10, 11])
        assert result == 789, f"Test 20 failed: got {result}, expected {789}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = maxOfList([1, 1, 1, 1, 2])
        assert result == 2, f"Test 21 failed: got {result}, expected {2}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = maxOfList([2, 1, 1, 1, 1])
        assert result == 2, f"Test 22 failed: got {result}, expected {2}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = maxOfList([1, 2, 1, 2, 1, 2])
        assert result == 2, f"Test 23 failed: got {result}, expected {2}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = maxOfList([0, 0, 0, 0, 0, 0, 1])
        assert result == 1, f"Test 24 failed: got {result}, expected {1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = maxOfList([1, 0, 0, 0, 0, 0, 0])
        assert result == 1, f"Test 25 failed: got {result}, expected {1}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = maxOfList([15, 23, 8, 23, 4, 23])
        assert result == 23, f"Test 26 failed: got {result}, expected {23}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = maxOfList([6, 10, 14, 3, 2, 1])
        assert result == 14, f"Test 27 failed: got {result}, expected {14}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = maxOfList('[2] ++ [1, 3]')
        assert result == 3, f"Test 28 failed: got {result}, expected {3}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = maxOfList([2, 3])
        assert result == 3, f"Test 29 failed: got {result}, expected {3}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = maxOfList([7, 2, 4])
        assert result == 7, f"Test 30 failed: got {result}, expected {7}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = maxOfList([0, 3, 0, 0, 14])
        assert result == 14, f"Test 31 failed: got {result}, expected {14}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = maxOfList([1, 3, 3])
        assert result == 3, f"Test 32 failed: got {result}, expected {3}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = maxOfList([2, 2, 1, 0, 0, 0])
        assert result == 2, f"Test 33 failed: got {result}, expected {2}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = maxOfList([1, 3])
        assert result == 3, f"Test 34 failed: got {result}, expected {3}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = maxOfList([3, 0])
        assert result == 3, f"Test 35 failed: got {result}, expected {3}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = maxOfList([3, 2])
        assert result == 3, f"Test 36 failed: got {result}, expected {3}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = maxOfList([42, 23, 2, 8])
        assert result == 42, f"Test 37 failed: got {result}, expected {42}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = maxOfList([1, 2, 3, 0, 0])
        assert result == 3, f"Test 38 failed: got {result}, expected {3}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = maxOfList([5, 3, 0, 0])
        assert result == 5, f"Test 39 failed: got {result}, expected {5}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = maxOfList([3, 2, 1])
        assert result == 3, f"Test 40 failed: got {result}, expected {3}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = maxOfList([0, 3, 2, 1])
        assert result == 3, f"Test 41 failed: got {result}, expected {3}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = maxOfList([1, 2, 3, 0])
        assert result == 3, f"Test 42 failed: got {result}, expected {3}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = maxOfList([1, 2, 11])
        assert result == 11, f"Test 43 failed: got {result}, expected {11}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = maxOfList([0, 5, 5, 5])
        assert result == 5, f"Test 44 failed: got {result}, expected {5}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = maxOfList([5, 5])
        assert result == 5, f"Test 45 failed: got {result}, expected {5}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = maxOfList([5, 5, 5, 24])
        assert result == 24, f"Test 46 failed: got {result}, expected {24}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = maxOfList([10, 5, 5, 0])
        assert result == 10, f"Test 47 failed: got {result}, expected {10}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = maxOfList([5, 5, 789])
        assert result == 789, f"Test 48 failed: got {result}, expected {789}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = maxOfList([456, 5, 5, 5])
        assert result == 456, f"Test 49 failed: got {result}, expected {456}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = maxOfList([4, 5, 0])
        assert result == 5, f"Test 50 failed: got {result}, expected {5}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = maxOfList([5, 5, 5, 0, 18446744073709551615])
        assert result == 18446744073709551615, f"Test 51 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = maxOfList([5, 3, 5])
        assert result == 5, f"Test 52 failed: got {result}, expected {5}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = maxOfList([15, 10, 5, 6])
        assert result == 15, f"Test 53 failed: got {result}, expected {15}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = maxOfList([5, 5, 5, 18446744073709551616])
        assert result == 18446744073709551616, f"Test 54 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = maxOfList([5, 5, 5, 0])
        assert result == 5, f"Test 55 failed: got {result}, expected {5}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = maxOfList([0, 5, 5, 8, 42])
        assert result == 42, f"Test 56 failed: got {result}, expected {42}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = maxOfList([11, 5])
        assert result == 11, f"Test 57 failed: got {result}, expected {11}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = maxOfList([10, 9])
        assert result == 10, f"Test 58 failed: got {result}, expected {10}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = maxOfList([10, 1, 9, 0, 0])
        assert result == 10, f"Test 59 failed: got {result}, expected {10}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = maxOfList([10, 0, 0])
        assert result == 10, f"Test 60 failed: got {result}, expected {10}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = maxOfList([8, 1])
        assert result == 8, f"Test 61 failed: got {result}, expected {8}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = maxOfList([10, 1, 18])
        assert result == 18, f"Test 62 failed: got {result}, expected {18}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = maxOfList([9, 1, 10, 100])
        assert result == 100, f"Test 63 failed: got {result}, expected {100}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = maxOfList([9, 1, 10, 999999])
        assert result == 999999, f"Test 64 failed: got {result}, expected {999999}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = maxOfList([0, 9, 1, 10])
        assert result == 10, f"Test 65 failed: got {result}, expected {10}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = maxOfList([1, 9, 7, 18446744073709551616])
        assert result == 18446744073709551616, f"Test 66 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = maxOfList([789, 1, 9, 0, 0])
        assert result == 789, f"Test 67 failed: got {result}, expected {789}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = maxOfList([0, 18, 1, 10])
        assert result == 18, f"Test 68 failed: got {result}, expected {18}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = maxOfList([41, 0])
        assert result == 41, f"Test 69 failed: got {result}, expected {41}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = maxOfList([23, 18446744073709551615, 9, 1, 10])
        assert result == 18446744073709551615, f"Test 70 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = maxOfList([9, 10, 0])
        assert result == 10, f"Test 71 failed: got {result}, expected {10}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = maxOfList([14, 41, 1000001, 0])
        assert result == 1000001, f"Test 72 failed: got {result}, expected {1000001}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = maxOfList([7, 0, 24])
        assert result == 24, f"Test 73 failed: got {result}, expected {24}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = maxOfList([4, 0])
        assert result == 4, f"Test 74 failed: got {result}, expected {4}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = maxOfList([999999, 0, 7])
        assert result == 999999, f"Test 75 failed: got {result}, expected {999999}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = maxOfList([7, 0, 8])
        assert result == 8, f"Test 76 failed: got {result}, expected {8}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = maxOfList([4, 0, 7])
        assert result == 7, f"Test 77 failed: got {result}, expected {7}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = maxOfList([0, 456])
        assert result == 456, f"Test 78 failed: got {result}, expected {456}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = maxOfList([0, 7])
        assert result == 7, f"Test 79 failed: got {result}, expected {7}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = maxOfList([23, 7])
        assert result == 23, f"Test 80 failed: got {result}, expected {23}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = maxOfList([18])
        assert result == 18, f"Test 81 failed: got {result}, expected {18}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = maxOfList([7, 24])
        assert result == 24, f"Test 82 failed: got {result}, expected {24}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = maxOfList([11, 4, 0, 9, 0])
        assert result == 11, f"Test 83 failed: got {result}, expected {11}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = maxOfList([7, 0])
        assert result == 7, f"Test 84 failed: got {result}, expected {7}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = maxOfList([0, 2, 0])
        assert result == 2, f"Test 85 failed: got {result}, expected {2}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = maxOfList([0, 0, 18446744073709551615, 11, 0, 0, 0])
        assert result == 18446744073709551615, f"Test 86 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = maxOfList([0, 0, 15, 0])
        assert result == 15, f"Test 87 failed: got {result}, expected {15}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = maxOfList([999999, 0, 0, 0, 0])
        assert result == 999999, f"Test 88 failed: got {result}, expected {999999}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = maxOfList([0, 0, 6])
        assert result == 6, f"Test 89 failed: got {result}, expected {6}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = maxOfList([0, 0, 0, 0, 24])
        assert result == 24, f"Test 90 failed: got {result}, expected {24}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = maxOfList([0, 0, 0, 4])
        assert result == 4, f"Test 91 failed: got {result}, expected {4}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = maxOfList([0, 0, 0, 0, 0])
        assert result == 0, f"Test 92 failed: got {result}, expected {0}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = maxOfList([0, 0, 0, 0, 0, 24])
        assert result == 24, f"Test 93 failed: got {result}, expected {24}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = maxOfList([0, 0, 8])
        assert result == 8, f"Test 94 failed: got {result}, expected {8}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = maxOfList([0, 0, 0, 0, 0, 999999999, 2, 1000001])
        assert result == 999999999, f"Test 95 failed: got {result}, expected {999999999}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = maxOfList([0, 15])
        assert result == 15, f"Test 96 failed: got {result}, expected {15}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = maxOfList([0, 1, 14])
        assert result == 14, f"Test 97 failed: got {result}, expected {14}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = maxOfList([0, 0, 42, 0])
        assert result == 42, f"Test 98 failed: got {result}, expected {42}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = maxOfList([0, 0, 15])
        assert result == 15, f"Test 99 failed: got {result}, expected {15}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = maxOfList([1000000, 4, 100, 0])
        assert result == 1000000, f"Test 100 failed: got {result}, expected {1000000}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = maxOfList([2, 18446744073709551615])
        assert result == 18446744073709551615, f"Test 101 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = maxOfList([0, 0, 999999999])
        assert result == 999999999, f"Test 102 failed: got {result}, expected {999999999}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = maxOfList([0, 2, 1000000])
        assert result == 1000000, f"Test 103 failed: got {result}, expected {1000000}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = maxOfList([0, 8, 23])
        assert result == 23, f"Test 104 failed: got {result}, expected {23}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = maxOfList([15])
        assert result == 15, f"Test 105 failed: got {result}, expected {15}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = maxOfList([1, 6])
        assert result == 6, f"Test 106 failed: got {result}, expected {6}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = maxOfList([10, 0])
        assert result == 10, f"Test 107 failed: got {result}, expected {10}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = maxOfList([0, 41])
        assert result == 41, f"Test 108 failed: got {result}, expected {41}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = maxOfList([11, 11])
        assert result == 11, f"Test 109 failed: got {result}, expected {11}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = maxOfList([2, 0])
        assert result == 2, f"Test 110 failed: got {result}, expected {2}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = maxOfList([15, 5])
        assert result == 15, f"Test 111 failed: got {result}, expected {15}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = maxOfList([1, 5, 0, 10])
        assert result == 10, f"Test 112 failed: got {result}, expected {10}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = maxOfList([1, 41])
        assert result == 41, f"Test 113 failed: got {result}, expected {41}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = maxOfList([1, 1000001])
        assert result == 1000001, f"Test 114 failed: got {result}, expected {1000001}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = maxOfList([1, 6, 0])
        assert result == 6, f"Test 115 failed: got {result}, expected {6}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = maxOfList([1, 0, 999999])
        assert result == 999999, f"Test 116 failed: got {result}, expected {999999}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = maxOfList([0, 0, 17])
        assert result == 17, f"Test 117 failed: got {result}, expected {17}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = maxOfList([1, 42])
        assert result == 42, f"Test 118 failed: got {result}, expected {42}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = maxOfList([1, 2, 1000000])
        assert result == 1000000, f"Test 119 failed: got {result}, expected {1000000}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = maxOfList([3, 0, 14])
        assert result == 14, f"Test 120 failed: got {result}, expected {14}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = maxOfList([0, 0, 456])
        assert result == 456, f"Test 121 failed: got {result}, expected {456}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = maxOfList([999999999, 6])
        assert result == 999999999, f"Test 122 failed: got {result}, expected {999999999}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = maxOfList([999999999, 0, 1])
        assert result == 999999999, f"Test 123 failed: got {result}, expected {999999999}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = maxOfList([4, 999999999, 24, 0])
        assert result == 999999999, f"Test 124 failed: got {result}, expected {999999999}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = maxOfList([999999999, 0])
        assert result == 999999999, f"Test 125 failed: got {result}, expected {999999999}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = maxOfList([0, 999999999, 0, 0])
        assert result == 999999999, f"Test 126 failed: got {result}, expected {999999999}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = maxOfList([0, 999999999])
        assert result == 999999999, f"Test 127 failed: got {result}, expected {999999999}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = maxOfList([999999999, 3, 8, 789])
        assert result == 999999999, f"Test 128 failed: got {result}, expected {999999999}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = maxOfList([0, 999999999, 15])
        assert result == 999999999, f"Test 129 failed: got {result}, expected {999999999}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = maxOfList([999999999, 1])
        assert result == 999999999, f"Test 130 failed: got {result}, expected {999999999}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = maxOfList([999999, 0, 0, 42])
        assert result == 999999, f"Test 131 failed: got {result}, expected {999999}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = maxOfList([0, 1, 23])
        assert result == 23, f"Test 132 failed: got {result}, expected {23}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = maxOfList([0, 0, 0, 14])
        assert result == 14, f"Test 133 failed: got {result}, expected {14}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = maxOfList([0, 0, 11])
        assert result == 11, f"Test 134 failed: got {result}, expected {11}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = maxOfList([0, 5, 0])
        assert result == 5, f"Test 135 failed: got {result}, expected {5}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = maxOfList([0, 4, 1])
        assert result == 4, f"Test 136 failed: got {result}, expected {4}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = maxOfList([1, 0, 9])
        assert result == 9, f"Test 137 failed: got {result}, expected {9}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = maxOfList([14, 1, 0])
        assert result == 14, f"Test 138 failed: got {result}, expected {14}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = maxOfList([1, 1, 0, 6])
        assert result == 6, f"Test 139 failed: got {result}, expected {6}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = maxOfList([1, 456, 1])
        assert result == 456, f"Test 140 failed: got {result}, expected {456}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = maxOfList([15, 100, 0])
        assert result == 100, f"Test 141 failed: got {result}, expected {100}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = maxOfList([0, 2])
        assert result == 2, f"Test 142 failed: got {result}, expected {2}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = maxOfList([1, 0, 14])
        assert result == 14, f"Test 143 failed: got {result}, expected {14}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = maxOfList([0, 0, 1])
        assert result == 1, f"Test 144 failed: got {result}, expected {1}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = maxOfList([1, 0, 0])
        assert result == 1, f"Test 145 failed: got {result}, expected {1}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = maxOfList([0, 456, 999999])
        assert result == 999999, f"Test 146 failed: got {result}, expected {999999}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = maxOfList([0, 1, 6])
        assert result == 6, f"Test 147 failed: got {result}, expected {6}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = maxOfList([0, 1, 0, 20])
        assert result == 20, f"Test 148 failed: got {result}, expected {20}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = maxOfList([20, 1, 0, 789])
        assert result == 789, f"Test 149 failed: got {result}, expected {789}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = maxOfList([41, 1])
        assert result == 41, f"Test 150 failed: got {result}, expected {41}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = maxOfList([0, 1, 3, 0, 2])
        assert result == 3, f"Test 151 failed: got {result}, expected {3}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = maxOfList([41, 5])
        assert result == 41, f"Test 152 failed: got {result}, expected {41}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = maxOfList([0, 1, 789])
        assert result == 789, f"Test 153 failed: got {result}, expected {789}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = maxOfList([0, 1, 3])
        assert result == 3, f"Test 154 failed: got {result}, expected {3}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = maxOfList([0, 3999999996, 1, 0])
        assert result == 3999999996, f"Test 155 failed: got {result}, expected {3999999996}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = maxOfList([4, 5, 5, 0])
        assert result == 5, f"Test 156 failed: got {result}, expected {5}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = maxOfList([5, 0, 5])
        assert result == 5, f"Test 157 failed: got {result}, expected {5}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = maxOfList([5, 5, 5, 6, 3])
        assert result == 6, f"Test 158 failed: got {result}, expected {6}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = maxOfList([5, 5, 5, 23, 3999999996])
        assert result == 3999999996, f"Test 159 failed: got {result}, expected {3999999996}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = maxOfList([5, 0, 5, 5, 0])
        assert result == 5, f"Test 160 failed: got {result}, expected {5}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = maxOfList([5, 5, 5, 5, 24])
        assert result == 24, f"Test 161 failed: got {result}, expected {24}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = maxOfList([0, 0, 5, 5, 5, 5])
        assert result == 5, f"Test 162 failed: got {result}, expected {5}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = maxOfList([5, 5, 5, 5, 0])
        assert result == 5, f"Test 163 failed: got {result}, expected {5}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = maxOfList([0, 5, 5, 0])
        assert result == 5, f"Test 164 failed: got {result}, expected {5}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = maxOfList([4, 1000000])
        assert result == 1000000, f"Test 165 failed: got {result}, expected {1000000}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = maxOfList([24, 5, 5, 5, 5])
        assert result == 24, f"Test 166 failed: got {result}, expected {24}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = maxOfList([5, 5, 5, 5, 0, 0, 0])
        assert result == 5, f"Test 167 failed: got {result}, expected {5}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = maxOfList([5, 5, 5, 5, 0, 6, 0, 0])
        assert result == 6, f"Test 168 failed: got {result}, expected {6}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = maxOfList([1, 2, 3, 0, 1000001])
        assert result == 1000001, f"Test 169 failed: got {result}, expected {1000001}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = maxOfList([1, 2, 4, 5, 0, 0, 18446744073709551615, 0])
        assert result == 18446744073709551615, f"Test 170 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = maxOfList([0, 5, 4, 3, 2, 1, 0])
        assert result == 5, f"Test 171 failed: got {result}, expected {5}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = maxOfList([1, 2, 3, 4, 5, 20, 3])
        assert result == 20, f"Test 172 failed: got {result}, expected {20}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = maxOfList([1, 2, 3, 5, 0, 0])
        assert result == 5, f"Test 173 failed: got {result}, expected {5}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = maxOfList([1, 2, 3, 4, 5, 0, 20, 0])
        assert result == 20, f"Test 174 failed: got {result}, expected {20}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = maxOfList([1, 3, 4, 5])
        assert result == 5, f"Test 175 failed: got {result}, expected {5}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = maxOfList([1, 2, 3, 4, 5, 42, 17, 4, 7])
        assert result == 42, f"Test 176 failed: got {result}, expected {42}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = maxOfList([1, 2, 2, 4, 5, 0])
        assert result == 5, f"Test 177 failed: got {result}, expected {5}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = maxOfList([0, 5, 4, 3, 2, 11])
        assert result == 11, f"Test 178 failed: got {result}, expected {11}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = maxOfList([0, 5, 3, 2, 1, 3999999996])
        assert result == 3999999996, f"Test 179 failed: got {result}, expected {3999999996}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = maxOfList([0, 6, 4, 5, 2, 1])
        assert result == 6, f"Test 180 failed: got {result}, expected {6}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = maxOfList([1, 2, 3, 4, 5, 23])
        assert result == 23, f"Test 181 failed: got {result}, expected {23}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = maxOfList([17, 24, 3, 4, 5])
        assert result == 24, f"Test 182 failed: got {result}, expected {24}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = maxOfList([1, 2, 3, 4, 0])
        assert result == 4, f"Test 183 failed: got {result}, expected {4}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = maxOfList([5, 4, 789, 1, 0])
        assert result == 789, f"Test 184 failed: got {result}, expected {789}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = maxOfList([5, 4, 3, 2, 1, 1000000, 789])
        assert result == 1000000, f"Test 185 failed: got {result}, expected {1000000}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = maxOfList([1000000, 3, 2, 1, 0])
        assert result == 1000000, f"Test 186 failed: got {result}, expected {1000000}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = maxOfList([1, 2, 3, 4, 5, 11, 0])
        assert result == 11, f"Test 187 failed: got {result}, expected {11}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = maxOfList([5, 6, 3, 2, 1])
        assert result == 6, f"Test 188 failed: got {result}, expected {6}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = maxOfList([5, 8, 3, 2, 1])
        assert result == 8, f"Test 189 failed: got {result}, expected {8}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = maxOfList([5, 4, 3, 2, 1, 6, 0, 23])
        assert result == 23, f"Test 190 failed: got {result}, expected {23}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = maxOfList([5, 4, 3, 0, 0])
        assert result == 5, f"Test 191 failed: got {result}, expected {5}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = maxOfList([1, 2, 3, 5])
        assert result == 5, f"Test 192 failed: got {result}, expected {5}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = maxOfList([24, 1, 3, 4, 5])
        assert result == 24, f"Test 193 failed: got {result}, expected {24}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = maxOfList([5, 4, 3, 2, 1, 1, 18446744073709551616, 0])
        assert result == 18446744073709551616, f"Test 194 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = maxOfList([5, 4, 3, 3999999996, 0, 0, 123])
        assert result == 3999999996, f"Test 195 failed: got {result}, expected {3999999996}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = maxOfList([10, 0, 5, 4, 3, 2, 1, 9])
        assert result == 10, f"Test 196 failed: got {result}, expected {10}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = maxOfList([0, 2, 1, 2, 3, 17, 5])
        assert result == 17, f"Test 197 failed: got {result}, expected {17}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = maxOfList([3, 4, 4])
        assert result == 4, f"Test 198 failed: got {result}, expected {4}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = maxOfList([0, 2, 9, 9, 1, 0])
        assert result == 9, f"Test 199 failed: got {result}, expected {9}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = maxOfList([2, 9, 3, 9, 1, 14, 0])
        assert result == 14, f"Test 200 failed: got {result}, expected {14}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = maxOfList([2, 9, 3, 9, 11, 1000001])
        assert result == 1000001, f"Test 201 failed: got {result}, expected {1000001}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = maxOfList([2, 9, 3, 9, 1, 0])
        assert result == 9, f"Test 202 failed: got {result}, expected {9}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = maxOfList([2, 10, 3, 9, 1, 0])
        assert result == 10, f"Test 203 failed: got {result}, expected {10}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = maxOfList([2, 11, 3, 9, 1])
        assert result == 11, f"Test 204 failed: got {result}, expected {11}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = maxOfList([9, 3, 9, 1, 0, 1000001])
        assert result == 1000001, f"Test 205 failed: got {result}, expected {1000001}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = maxOfList([2, 9, 3, 9, 1, 0, 0, 24, 0, 999999])
        assert result == 999999, f"Test 206 failed: got {result}, expected {999999}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = maxOfList([1000001, 9, 3, 9, 1, 0, 3999999996, 0])
        assert result == 3999999996, f"Test 207 failed: got {result}, expected {3999999996}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = maxOfList([10, 3, 9, 2])
        assert result == 10, f"Test 208 failed: got {result}, expected {10}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = maxOfList([0, 9, 6, 2, 23])
        assert result == 23, f"Test 209 failed: got {result}, expected {23}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = maxOfList([0, 0, 1, 9, 3, 18, 2])
        assert result == 18, f"Test 210 failed: got {result}, expected {18}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = maxOfList([2, 9, 3, 9, 1, 0, 42])
        assert result == 42, f"Test 211 failed: got {result}, expected {42}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = maxOfList([1, 0, 9, 2, 1000000, 0])
        assert result == 1000000, f"Test 212 failed: got {result}, expected {1000000}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = maxOfList([0, 42, 999999, 1, 9, 3, 7, 2])
        assert result == 999999, f"Test 213 failed: got {result}, expected {999999}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = maxOfList([7, 8, 8, 7, 0, 999999999, 2])
        assert result == 999999999, f"Test 214 failed: got {result}, expected {999999999}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = maxOfList([7, 7, 0, 7, 0, 0, 0])
        assert result == 7, f"Test 215 failed: got {result}, expected {7}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = maxOfList([7, 7, 9, 7])
        assert result == 9, f"Test 216 failed: got {result}, expected {9}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = maxOfList([7, 8, 7, 0])
        assert result == 8, f"Test 217 failed: got {result}, expected {8}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = maxOfList([7, 7, 8, 7, 1000001])
        assert result == 1000001, f"Test 218 failed: got {result}, expected {1000001}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = maxOfList([0, 0, 0, 7, 8, 7])
        assert result == 8, f"Test 219 failed: got {result}, expected {8}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = maxOfList([7, 8, 7, 24])
        assert result == 24, f"Test 220 failed: got {result}, expected {24}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = maxOfList([7, 10, 7])
        assert result == 10, f"Test 221 failed: got {result}, expected {10}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = maxOfList([7, 7, 7, 0])
        assert result == 7, f"Test 222 failed: got {result}, expected {7}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = maxOfList([7, 7, 8, 7, 999999999, 15, 14])
        assert result == 999999999, f"Test 223 failed: got {result}, expected {999999999}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = maxOfList([7, 7, 8, 7, 0, 6])
        assert result == 8, f"Test 224 failed: got {result}, expected {8}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = maxOfList([7, 8, 7, 7])
        assert result == 8, f"Test 225 failed: got {result}, expected {8}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = maxOfList([0, 7, 8, 7, 7, 0])
        assert result == 8, f"Test 226 failed: got {result}, expected {8}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = maxOfList([7, 8, 7, 7, 0])
        assert result == 8, f"Test 227 failed: got {result}, expected {8}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = maxOfList([0, 7, 8, 7, 7])
        assert result == 8, f"Test 228 failed: got {result}, expected {8}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = maxOfList([8, 7, 7, 7, 0])
        assert result == 8, f"Test 229 failed: got {result}, expected {8}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = maxOfList([8, 7, 7, 7, 999999])
        assert result == 999999, f"Test 230 failed: got {result}, expected {999999}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = maxOfList([7, 7])
        assert result == 7, f"Test 231 failed: got {result}, expected {7}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = maxOfList([8, 7])
        assert result == 8, f"Test 232 failed: got {result}, expected {8}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = maxOfList([8, 7, 0, 7, 0])
        assert result == 8, f"Test 233 failed: got {result}, expected {8}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = maxOfList([8, 7, 7, 7, 3999999996, 1000001])
        assert result == 3999999996, f"Test 234 failed: got {result}, expected {3999999996}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = maxOfList([8, 6, 7, 7])
        assert result == 8, f"Test 235 failed: got {result}, expected {8}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = maxOfList([8, 7, 7])
        assert result == 8, f"Test 236 failed: got {result}, expected {8}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = maxOfList([7, 7, 0, 0])
        assert result == 7, f"Test 237 failed: got {result}, expected {7}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = maxOfList([0, 7, 7, 8])
        assert result == 8, f"Test 238 failed: got {result}, expected {8}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = maxOfList([14, 7, 7])
        assert result == 14, f"Test 239 failed: got {result}, expected {14}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = maxOfList([8, 7, 0])
        assert result == 8, f"Test 240 failed: got {result}, expected {8}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = maxOfList([3999999996, 7, 7, 8, 1, 17, 10])
        assert result == 3999999996, f"Test 241 failed: got {result}, expected {3999999996}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = maxOfList([8, 20, 7, 7, 16])
        assert result == 20, f"Test 242 failed: got {result}, expected {20}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = maxOfList([7, 7, 7, 8, 0, 11, 0])
        assert result == 11, f"Test 243 failed: got {result}, expected {11}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = maxOfList([1, 8, 7, 7, 7, 42])
        assert result == 42, f"Test 244 failed: got {result}, expected {42}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = maxOfList([0, 17, 8, 7, 7])
        assert result == 17, f"Test 245 failed: got {result}, expected {17}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = maxOfList([7, 7, 7, 3999999996, 8])
        assert result == 3999999996, f"Test 246 failed: got {result}, expected {3999999996}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = maxOfList([7, 1, 456, 8])
        assert result == 456, f"Test 247 failed: got {result}, expected {456}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = maxOfList([7, 18446744073709551615, 7, 8])
        assert result == 18446744073709551615, f"Test 248 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = maxOfList([2, 16, 8, 7, 7, 0])
        assert result == 16, f"Test 249 failed: got {result}, expected {16}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = maxOfList([7, 7, 8, 41])
        assert result == 41, f"Test 250 failed: got {result}, expected {41}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = maxOfList([7, 0, 7, 8])
        assert result == 8, f"Test 251 failed: got {result}, expected {8}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = maxOfList([7, 7, 7])
        assert result == 7, f"Test 252 failed: got {result}, expected {7}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = maxOfList([789, 0, 100, 0, 100, 0])
        assert result == 789, f"Test 253 failed: got {result}, expected {789}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = maxOfList([0, 100, 0, 100, 0, 16])
        assert result == 100, f"Test 254 failed: got {result}, expected {100}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = maxOfList([0, 100, 0, 100, 18])
        assert result == 100, f"Test 255 failed: got {result}, expected {100}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = maxOfList([0, 100, 0, 100, 0, 0, 1])
        assert result == 100, f"Test 256 failed: got {result}, expected {100}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = maxOfList([0, 100, 0, 100, 0, 0, 3999999996, 0])
        assert result == 3999999996, f"Test 257 failed: got {result}, expected {3999999996}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = maxOfList([8, 18446744073709551616, 0, 100, 0])
        assert result == 18446744073709551616, f"Test 258 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = maxOfList([0, 100, 0, 100, 0, 0])
        assert result == 100, f"Test 259 failed: got {result}, expected {100}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = maxOfList([3999999996, 0, 0, 100, 4, 100, 0])
        assert result == 3999999996, f"Test 260 failed: got {result}, expected {3999999996}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = maxOfList([100, 15, 100, 2, 0])
        assert result == 100, f"Test 261 failed: got {result}, expected {100}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = maxOfList([0, 101, 0, 100, 0, 456])
        assert result == 456, f"Test 262 failed: got {result}, expected {456}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = maxOfList([0, 200, 0])
        assert result == 200, f"Test 263 failed: got {result}, expected {200}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = maxOfList([16, 100, 1, 100, 0])
        assert result == 100, f"Test 264 failed: got {result}, expected {100}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = maxOfList([0, 100, 0, 0, 16])
        assert result == 100, f"Test 265 failed: got {result}, expected {100}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = maxOfList([0, 100, 0, 100, 0, 0, 0])
        assert result == 100, f"Test 266 failed: got {result}, expected {100}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = maxOfList([0, 18, 42, 3, 41, 0])
        assert result == 42, f"Test 267 failed: got {result}, expected {42}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = maxOfList([42, 17, 42, 3, 41, 0])
        assert result == 42, f"Test 268 failed: got {result}, expected {42}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = maxOfList([1000001, 42, 17, 42, 3, 3])
        assert result == 1000001, f"Test 269 failed: got {result}, expected {1000001}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = maxOfList([17, 42, 3, 41, 0])
        assert result == 42, f"Test 270 failed: got {result}, expected {42}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = maxOfList([17, 42, 3, 41])
        assert result == 42, f"Test 271 failed: got {result}, expected {42}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = maxOfList([0, 8, 41, 3, 42, 17, 42, 0])
        assert result == 42, f"Test 272 failed: got {result}, expected {42}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = maxOfList([4, 41, 3, 42, 17, 42])
        assert result == 42, f"Test 273 failed: got {result}, expected {42}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = maxOfList([42, 42, 6, 41, 0])
        assert result == 42, f"Test 274 failed: got {result}, expected {42}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = maxOfList([0, 41, 3, 42, 17, 42, 18446744073709551616])
        assert result == 18446744073709551616, f"Test 275 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = maxOfList([9, 17, 999999999, 3, 41])
        assert result == 999999999, f"Test 276 failed: got {result}, expected {999999999}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = maxOfList([42, 17, 42, 3, 41, 0, 0])
        assert result == 42, f"Test 277 failed: got {result}, expected {42}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = maxOfList([41, 3, 17, 16, 42])
        assert result == 42, f"Test 278 failed: got {result}, expected {42}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = maxOfList([42, 17, 0, 41, 0])
        assert result == 42, f"Test 279 failed: got {result}, expected {42}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = maxOfList([42, 0, 42, 3, 41, 0, 1])
        assert result == 42, f"Test 280 failed: got {result}, expected {42}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = maxOfList([3, 1, 4, 1, 7, 9, 2, 6, 0, 9])
        assert result == 9, f"Test 281 failed: got {result}, expected {9}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = maxOfList([0, 5, 6, 2, 9, 5, 1, 4, 1, 3])
        assert result == 9, f"Test 282 failed: got {result}, expected {9}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = maxOfList([6, 2, 9, 5, 1, 4, 1, 3, 0])
        assert result == 9, f"Test 283 failed: got {result}, expected {9}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2, 6, 0, 8, 20])
        assert result == 20, f"Test 284 failed: got {result}, expected {20}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = maxOfList([6, 9, 5, 1, 4, 0, 3, 0, 789])
        assert result == 789, f"Test 285 failed: got {result}, expected {789}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = maxOfList([3, 17, 1, 5, 9, 2, 6, 0])
        assert result == 17, f"Test 286 failed: got {result}, expected {17}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = maxOfList([3, 1, 4, 1, 5, 100, 2, 6, 0])
        assert result == 100, f"Test 287 failed: got {result}, expected {100}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = maxOfList([6, 2, 9, 5, 18446744073709551616, 1, 3, 10, 2])
        assert result == 18446744073709551616, f"Test 288 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2, 456])
        assert result == 456, f"Test 289 failed: got {result}, expected {456}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = maxOfList([0, 3, 1, 3, 1, 5, 9, 2, 6])
        assert result == 9, f"Test 290 failed: got {result}, expected {9}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2, 6, 0])
        assert result == 9, f"Test 291 failed: got {result}, expected {9}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2])
        assert result == 9, f"Test 292 failed: got {result}, expected {9}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = maxOfList([2, 9, 5, 1, 4, 1, 3, 0, 0])
        assert result == 9, f"Test 293 failed: got {result}, expected {9}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = maxOfList([9, 2, 6, 5, 3, 5, 0])
        assert result == 9, f"Test 294 failed: got {result}, expected {9}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = maxOfList([200, 9, 5, 3, 5])
        assert result == 200, f"Test 295 failed: got {result}, expected {200}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = maxOfList([11, 2, 6, 5, 3, 5, 0])
        assert result == 11, f"Test 296 failed: got {result}, expected {11}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = maxOfList([5, 2, 5, 0, 2, 9, 9, 7])
        assert result == 9, f"Test 297 failed: got {result}, expected {9}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = maxOfList([9, 2, 6, 5, 101, 5, 0])
        assert result == 101, f"Test 298 failed: got {result}, expected {101}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = maxOfList([9, 2, 6, 5, 3, 5, 18446744073709551615])
        assert result == 18446744073709551615, f"Test 299 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = maxOfList([9, 2, 24, 5, 3, 5, 0, 17])
        assert result == 24, f"Test 300 failed: got {result}, expected {24}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = maxOfList([9, 2, 6, 5, 3, 10])
        assert result == 10, f"Test 301 failed: got {result}, expected {10}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = maxOfList([9, 2, 6, 18, 3, 5])
        assert result == 18, f"Test 302 failed: got {result}, expected {18}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = maxOfList([9, 2, 0, 3, 0])
        assert result == 9, f"Test 303 failed: got {result}, expected {9}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = maxOfList([5, 4, 5, 6, 2, 9])
        assert result == 9, f"Test 304 failed: got {result}, expected {9}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = maxOfList([101, 5, 6, 2, 9, 0])
        assert result == 101, f"Test 305 failed: got {result}, expected {101}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = maxOfList([9, 2, 6, 18446744073709551615, 3, 5])
        assert result == 18446744073709551615, f"Test 306 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = maxOfList([4, 4, 6, 2])
        assert result == 6, f"Test 307 failed: got {result}, expected {6}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = maxOfList([100, 9, 2, 6, 5, 3, 18446744073709551616])
        assert result == 18446744073709551616, f"Test 308 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = maxOfList([23, 789, 1, 1000001])
        assert result == 1000001, f"Test 309 failed: got {result}, expected {1000001}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = maxOfList([999999, 1000001, 0, 7])
        assert result == 1000001, f"Test 310 failed: got {result}, expected {1000001}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = maxOfList([1000001, 999999, 1000000, 3999999996])
        assert result == 3999999996, f"Test 311 failed: got {result}, expected {3999999996}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = maxOfList([1000001, 1000000, 1000000, 23])
        assert result == 1000001, f"Test 312 failed: got {result}, expected {1000001}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = maxOfList([2, 0, 1000001, 999999])
        assert result == 1000001, f"Test 313 failed: got {result}, expected {1000001}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = maxOfList([20, 0])
        assert result == 20, f"Test 314 failed: got {result}, expected {20}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = maxOfList([1000000])
        assert result == 1000000, f"Test 315 failed: got {result}, expected {1000000}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = maxOfList([1000000, 999999, 1000001, 999999999])
        assert result == 999999999, f"Test 316 failed: got {result}, expected {999999999}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = maxOfList([999999, 1000001, 0, 4])
        assert result == 1000001, f"Test 317 failed: got {result}, expected {1000001}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = maxOfList([0, 1000001, 3, 1000000])
        assert result == 1000001, f"Test 318 failed: got {result}, expected {1000001}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = maxOfList([1000001, 999999, 1000000])
        assert result == 1000001, f"Test 319 failed: got {result}, expected {1000001}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = maxOfList([1000000, 999999, 0, 0, 0])
        assert result == 1000000, f"Test 320 failed: got {result}, expected {1000000}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = maxOfList([1000000, 999999, 1000001, 0])
        assert result == 1000001, f"Test 321 failed: got {result}, expected {1000001}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = maxOfList([0, 1000001])
        assert result == 1000001, f"Test 322 failed: got {result}, expected {1000001}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = maxOfList([123, 456, 789, 10, 0])
        assert result == 789, f"Test 323 failed: got {result}, expected {789}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = maxOfList([123, 456, 20, 10, 11])
        assert result == 456, f"Test 324 failed: got {result}, expected {456}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = maxOfList([15, 123, 1000001, 789, 10, 11, 0])
        assert result == 1000001, f"Test 325 failed: got {result}, expected {1000001}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = maxOfList([123, 456, 789, 12, 4])
        assert result == 789, f"Test 326 failed: got {result}, expected {789}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = maxOfList([123, 456, 789, 10, 11, 0])
        assert result == 789, f"Test 327 failed: got {result}, expected {789}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = maxOfList([11, 9, 789, 456, 123, 9, 0])
        assert result == 789, f"Test 328 failed: got {result}, expected {789}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = maxOfList([123, 456, 789, 10, 0, 18446744073709551615])
        assert result == 18446744073709551615, f"Test 329 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = maxOfList([456, 789, 10, 11, 0, 18])
        assert result == 789, f"Test 330 failed: got {result}, expected {789}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = maxOfList([11, 10, 789])
        assert result == 789, f"Test 331 failed: got {result}, expected {789}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = maxOfList([11, 10, 789, 456, 123, 200])
        assert result == 789, f"Test 332 failed: got {result}, expected {789}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = maxOfList([5, 11, 10, 789, 100])
        assert result == 789, f"Test 333 failed: got {result}, expected {789}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = maxOfList([0, 123, 456, 789, 10, 11, 0])
        assert result == 789, f"Test 334 failed: got {result}, expected {789}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = maxOfList([123, 456, 789, 10, 11, 1000000, 0, 101])
        assert result == 1000000, f"Test 335 failed: got {result}, expected {1000000}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = maxOfList([3, 2, 1, 1, 2, 0])
        assert result == 3, f"Test 336 failed: got {result}, expected {3}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = maxOfList([1, 1, 1, 1, 2, 0, 200, 0, 0])
        assert result == 200, f"Test 337 failed: got {result}, expected {200}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = maxOfList([1, 1, 1, 1, 2, 0])
        assert result == 2, f"Test 338 failed: got {result}, expected {2}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = maxOfList([0, 2, 1, 0, 2])
        assert result == 2, f"Test 339 failed: got {result}, expected {2}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = maxOfList([1, 1, 2, 101])
        assert result == 101, f"Test 340 failed: got {result}, expected {101}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = maxOfList([1, 0, 1, 2])
        assert result == 2, f"Test 341 failed: got {result}, expected {2}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = maxOfList([2, 1, 1, 1, 1, 0])
        assert result == 2, f"Test 342 failed: got {result}, expected {2}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = maxOfList([1, 1, 1, 1, 2, 7])
        assert result == 7, f"Test 343 failed: got {result}, expected {7}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = maxOfList([1, 1, 1, 2, 123])
        assert result == 123, f"Test 344 failed: got {result}, expected {123}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = maxOfList([0, 2, 1, 1])
        assert result == 2, f"Test 345 failed: got {result}, expected {2}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = maxOfList([1, 1, 0, 2, 0, 0, 20])
        assert result == 20, f"Test 346 failed: got {result}, expected {20}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    # Test case 347
    try:
        result = maxOfList([2, 1, 1, 1, 6, 18, 2, 0])
        assert result == 18, f"Test 347 failed: got {result}, expected {18}"
        print(f"Test 347 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 347 failed: {e}")
        test_results.append(False)

    # Test case 348
    try:
        result = maxOfList([11, 1, 1, 1, 1, 16])
        assert result == 16, f"Test 348 failed: got {result}, expected {16}"
        print(f"Test 348 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 348 failed: {e}")
        test_results.append(False)

    # Test case 349
    try:
        result = maxOfList([1, 1000000, 1])
        assert result == 1000000, f"Test 349 failed: got {result}, expected {1000000}"
        print(f"Test 349 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 349 failed: {e}")
        test_results.append(False)

    # Test case 350
    try:
        result = maxOfList([1, 42, 1])
        assert result == 42, f"Test 350 failed: got {result}, expected {42}"
        print(f"Test 350 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 350 failed: {e}")
        test_results.append(False)

    # Test case 351
    try:
        result = maxOfList([16, 1, 1, 0, 1, 2])
        assert result == 16, f"Test 351 failed: got {result}, expected {16}"
        print(f"Test 351 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 351 failed: {e}")
        test_results.append(False)

    # Test case 352
    try:
        result = maxOfList([2, 1, 1, 1])
        assert result == 2, f"Test 352 failed: got {result}, expected {2}"
        print(f"Test 352 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 352 failed: {e}")
        test_results.append(False)

    # Test case 353
    try:
        result = maxOfList([0, 0, 1, 1, 1, 1, 2])
        assert result == 2, f"Test 353 failed: got {result}, expected {2}"
        print(f"Test 353 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 353 failed: {e}")
        test_results.append(False)

    # Test case 354
    try:
        result = maxOfList([82, 1, 2, 1, 2])
        assert result == 82, f"Test 354 failed: got {result}, expected {82}"
        print(f"Test 354 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 354 failed: {e}")
        test_results.append(False)

    # Test case 355
    try:
        result = maxOfList([3999999996, 1, 1, 1, 1])
        assert result == 3999999996, f"Test 355 failed: got {result}, expected {3999999996}"
        print(f"Test 355 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 355 failed: {e}")
        test_results.append(False)

    # Test case 356
    try:
        result = maxOfList([1, 1, 1, 2, 41])
        assert result == 41, f"Test 356 failed: got {result}, expected {41}"
        print(f"Test 356 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 356 failed: {e}")
        test_results.append(False)

    # Test case 357
    try:
        result = maxOfList([1, 1, 1, 1, 1, 101, 0, 0])
        assert result == 101, f"Test 357 failed: got {result}, expected {101}"
        print(f"Test 357 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 357 failed: {e}")
        test_results.append(False)

    # Test case 358
    try:
        result = maxOfList([2, 2, 1, 1, 1, 0])
        assert result == 2, f"Test 358 failed: got {result}, expected {2}"
        print(f"Test 358 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 358 failed: {e}")
        test_results.append(False)

    # Test case 359
    try:
        result = maxOfList([1, 1, 1, 1, 0])
        assert result == 1, f"Test 359 failed: got {result}, expected {1}"
        print(f"Test 359 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 359 failed: {e}")
        test_results.append(False)

    # Test case 360
    try:
        result = maxOfList([0, 1, 1, 1, 1, 1000000])
        assert result == 1000000, f"Test 360 failed: got {result}, expected {1000000}"
        print(f"Test 360 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 360 failed: {e}")
        test_results.append(False)

    # Test case 361
    try:
        result = maxOfList([2, 2, 1, 2, 0])
        assert result == 2, f"Test 361 failed: got {result}, expected {2}"
        print(f"Test 361 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 361 failed: {e}")
        test_results.append(False)

    # Test case 362
    try:
        result = maxOfList([999999, 2, 1, 2, 2])
        assert result == 999999, f"Test 362 failed: got {result}, expected {999999}"
        print(f"Test 362 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 362 failed: {e}")
        test_results.append(False)

    # Test case 363
    try:
        result = maxOfList([1, 2, 1, 2, 1, 2, 0])
        assert result == 2, f"Test 363 failed: got {result}, expected {2}"
        print(f"Test 363 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 363 failed: {e}")
        test_results.append(False)

    # Test case 364
    try:
        result = maxOfList([5, 2, 1, 2, 1, 2])
        assert result == 5, f"Test 364 failed: got {result}, expected {5}"
        print(f"Test 364 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 364 failed: {e}")
        test_results.append(False)

    # Test case 365
    try:
        result = maxOfList([18446744073709551615, 1, 1, 2, 1, 2, 2])
        assert result == 18446744073709551615, f"Test 365 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 365 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 365 failed: {e}")
        test_results.append(False)

    # Test case 366
    try:
        result = maxOfList([2, 1, 1, 2, 7, 0, 0])
        assert result == 7, f"Test 366 failed: got {result}, expected {7}"
        print(f"Test 366 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 366 failed: {e}")
        test_results.append(False)

    # Test case 367
    try:
        result = maxOfList([1, 0, 1, 2, 1, 16])
        assert result == 16, f"Test 367 failed: got {result}, expected {16}"
        print(f"Test 367 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 367 failed: {e}")
        test_results.append(False)

    # Test case 368
    try:
        result = maxOfList([0, 2, 1, 15, 1, 2, 0])
        assert result == 15, f"Test 368 failed: got {result}, expected {15}"
        print(f"Test 368 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 368 failed: {e}")
        test_results.append(False)

    # Test case 369
    try:
        result = maxOfList([999999, 1, 2, 1, 2])
        assert result == 999999, f"Test 369 failed: got {result}, expected {999999}"
        print(f"Test 369 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 369 failed: {e}")
        test_results.append(False)

    # Test case 370
    try:
        result = maxOfList([2, 1, 2, 456, 2, 1])
        assert result == 456, f"Test 370 failed: got {result}, expected {456}"
        print(f"Test 370 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 370 failed: {e}")
        test_results.append(False)

    # Test case 371
    try:
        result = maxOfList([1, 1, 2, 1, 2, 23])
        assert result == 23, f"Test 371 failed: got {result}, expected {23}"
        print(f"Test 371 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 371 failed: {e}")
        test_results.append(False)

    # Test case 372
    try:
        result = maxOfList([1, 2, 1, 2, 0])
        assert result == 2, f"Test 372 failed: got {result}, expected {2}"
        print(f"Test 372 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 372 failed: {e}")
        test_results.append(False)

    # Test case 373
    try:
        result = maxOfList([2, 1, 2, 1, 2, 1])
        assert result == 2, f"Test 373 failed: got {result}, expected {2}"
        print(f"Test 373 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 373 failed: {e}")
        test_results.append(False)

    # Test case 374
    try:
        result = maxOfList([1, 1, 2, 1, 2, 0, 0, 0])
        assert result == 2, f"Test 374 failed: got {result}, expected {2}"
        print(f"Test 374 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 374 failed: {e}")
        test_results.append(False)

    # Test case 375
    try:
        result = maxOfList([0, 2, 1, 0, 1, 2, 0])
        assert result == 2, f"Test 375 failed: got {result}, expected {2}"
        print(f"Test 375 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 375 failed: {e}")
        test_results.append(False)

    # Test case 376
    try:
        result = maxOfList([5, 1, 0, 0, 0, 0, 0, 0, 23])
        assert result == 23, f"Test 376 failed: got {result}, expected {23}"
        print(f"Test 376 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 376 failed: {e}")
        test_results.append(False)

    # Test case 377
    try:
        result = maxOfList([0, 1, 0, 0, 0, 0, 0, 0])
        assert result == 1, f"Test 377 failed: got {result}, expected {1}"
        print(f"Test 377 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 377 failed: {e}")
        test_results.append(False)

    # Test case 378
    try:
        result = maxOfList([1, 0, 0, 0, 789])
        assert result == 789, f"Test 378 failed: got {result}, expected {789}"
        print(f"Test 378 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 378 failed: {e}")
        test_results.append(False)

    # Test case 379
    try:
        result = maxOfList([0, 0, 0, 0, 2, 0, 1, 3999999996])
        assert result == 3999999996, f"Test 379 failed: got {result}, expected {3999999996}"
        print(f"Test 379 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 379 failed: {e}")
        test_results.append(False)

    # Test case 380
    try:
        result = maxOfList([0, 0, 0, 0, 0, 0, 1, 789])
        assert result == 789, f"Test 380 failed: got {result}, expected {789}"
        print(f"Test 380 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 380 failed: {e}")
        test_results.append(False)

    # Test case 381
    try:
        result = maxOfList([1, 0, 0, 0, 0, 0, 0, 20])
        assert result == 20, f"Test 381 failed: got {result}, expected {20}"
        print(f"Test 381 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 381 failed: {e}")
        test_results.append(False)

    # Test case 382
    try:
        result = maxOfList([0, 0, 0, 0, 1, 0])
        assert result == 1, f"Test 382 failed: got {result}, expected {1}"
        print(f"Test 382 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 382 failed: {e}")
        test_results.append(False)

    # Test case 383
    try:
        result = maxOfList([0, 0, 0, 1, 0, 0, 1, 0])
        assert result == 1, f"Test 383 failed: got {result}, expected {1}"
        print(f"Test 383 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 383 failed: {e}")
        test_results.append(False)

    # Test case 384
    try:
        result = maxOfList([1, 0, 0, 0, 0, 0, 7])
        assert result == 7, f"Test 384 failed: got {result}, expected {7}"
        print(f"Test 384 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 384 failed: {e}")
        test_results.append(False)

    # Test case 385
    try:
        result = maxOfList([0, 0, 0, 0, 0, 0, 0])
        assert result == 0, f"Test 385 failed: got {result}, expected {0}"
        print(f"Test 385 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 385 failed: {e}")
        test_results.append(False)

    # Test case 386
    try:
        result = maxOfList([0, 1, 0, 0, 0, 1, 0, 0])
        assert result == 1, f"Test 386 failed: got {result}, expected {1}"
        print(f"Test 386 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 386 failed: {e}")
        test_results.append(False)

    # Test case 387
    try:
        result = maxOfList([1, 0, 0, 0, 0, 0, 200])
        assert result == 200, f"Test 387 failed: got {result}, expected {200}"
        print(f"Test 387 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 387 failed: {e}")
        test_results.append(False)

    # Test case 388
    try:
        result = maxOfList([0, 0, 0, 0, 0, 0, 1, 0, 11])
        assert result == 11, f"Test 388 failed: got {result}, expected {11}"
        print(f"Test 388 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 388 failed: {e}")
        test_results.append(False)

    # Test case 389
    try:
        result = maxOfList([0, 0, 0, 0, 0, 1, 7])
        assert result == 7, f"Test 389 failed: got {result}, expected {7}"
        print(f"Test 389 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 389 failed: {e}")
        test_results.append(False)

    # Test case 390
    try:
        result = maxOfList([1, 0, 0, 0, 0])
        assert result == 1, f"Test 390 failed: got {result}, expected {1}"
        print(f"Test 390 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 390 failed: {e}")
        test_results.append(False)

    # Test case 391
    try:
        result = maxOfList([1, 1, 0, 0, 0, 0, 0])
        assert result == 1, f"Test 391 failed: got {result}, expected {1}"
        print(f"Test 391 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 391 failed: {e}")
        test_results.append(False)

    # Test case 392
    try:
        result = maxOfList([0, 18446744073709551616, 0, 0, 2, 1])
        assert result == 18446744073709551616, f"Test 392 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 392 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 392 failed: {e}")
        test_results.append(False)

    # Test case 393
    try:
        result = maxOfList([1000001, 0, 0, 0, 0, 0, 0, 1, 1000000, 5, 12])
        assert result == 1000001, f"Test 393 failed: got {result}, expected {1000001}"
        print(f"Test 393 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 393 failed: {e}")
        test_results.append(False)

    # Test case 394
    try:
        result = maxOfList([0, 0, 999999, 0, 0, 0, 1, 0, 0])
        assert result == 999999, f"Test 394 failed: got {result}, expected {999999}"
        print(f"Test 394 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 394 failed: {e}")
        test_results.append(False)

    # Test case 395
    try:
        result = maxOfList([1, 0, 0, 0, 0, 0, 0, 41, 0])
        assert result == 41, f"Test 395 failed: got {result}, expected {41}"
        print(f"Test 395 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 395 failed: {e}")
        test_results.append(False)

    # Test case 396
    try:
        result = maxOfList([0, 0, 0, 0, 0, 1, 1, 16])
        assert result == 16, f"Test 396 failed: got {result}, expected {16}"
        print(f"Test 396 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 396 failed: {e}")
        test_results.append(False)

    # Test case 397
    try:
        result = maxOfList([1, 0, 0, 0, 0, 11, 0])
        assert result == 11, f"Test 397 failed: got {result}, expected {11}"
        print(f"Test 397 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 397 failed: {e}")
        test_results.append(False)

    # Test case 398
    try:
        result = maxOfList([1, 0, 0, 0, 0, 0, 0, 0])
        assert result == 1, f"Test 398 failed: got {result}, expected {1}"
        print(f"Test 398 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 398 failed: {e}")
        test_results.append(False)

    # Test case 399
    try:
        result = maxOfList([1, 0, 0, 0, 0, 6, 0, 0])
        assert result == 6, f"Test 399 failed: got {result}, expected {6}"
        print(f"Test 399 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 399 failed: {e}")
        test_results.append(False)

    # Test case 400
    try:
        result = maxOfList([15, 8, 4, 23])
        assert result == 23, f"Test 400 failed: got {result}, expected {23}"
        print(f"Test 400 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 400 failed: {e}")
        test_results.append(False)

    # Test case 401
    try:
        result = maxOfList([15, 23, 8, 23, 4, 23, 100])
        assert result == 100, f"Test 401 failed: got {result}, expected {100}"
        print(f"Test 401 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 401 failed: {e}")
        test_results.append(False)

    # Test case 402
    try:
        result = maxOfList([0, 23, 4, 23, 8, 23, 15])
        assert result == 23, f"Test 402 failed: got {result}, expected {23}"
        print(f"Test 402 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 402 failed: {e}")
        test_results.append(False)

    # Test case 403
    try:
        result = maxOfList([15, 46, 8, 9, 4, 23, 1000001, 12])
        assert result == 1000001, f"Test 403 failed: got {result}, expected {1000001}"
        print(f"Test 403 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 403 failed: {e}")
        test_results.append(False)

    # Test case 404
    try:
        result = maxOfList([15, 23, 8, 21, 4, 23, 18446744073709551615])
        assert result == 18446744073709551615, f"Test 404 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 404 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 404 failed: {e}")
        test_results.append(False)

    # Test case 405
    try:
        result = maxOfList([23, 8, 200, 15])
        assert result == 200, f"Test 405 failed: got {result}, expected {200}"
        print(f"Test 405 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 405 failed: {e}")
        test_results.append(False)

    # Test case 406
    try:
        result = maxOfList([15, 23, 8, 23, 4, 23, 0])
        assert result == 23, f"Test 406 failed: got {result}, expected {23}"
        print(f"Test 406 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 406 failed: {e}")
        test_results.append(False)

    # Test case 407
    try:
        result = maxOfList([15, 24, 8, 23, 4, 23, 21])
        assert result == 24, f"Test 407 failed: got {result}, expected {24}"
        print(f"Test 407 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 407 failed: {e}")
        test_results.append(False)

    # Test case 408
    try:
        result = maxOfList([30, 23, 8, 23, 4, 23, 200, 0])
        assert result == 200, f"Test 408 failed: got {result}, expected {200}"
        print(f"Test 408 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 408 failed: {e}")
        test_results.append(False)

    # Test case 409
    try:
        result = maxOfList([15, 0, 8, 23, 4, 23, 0])
        assert result == 23, f"Test 409 failed: got {result}, expected {23}"
        print(f"Test 409 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 409 failed: {e}")
        test_results.append(False)

    # Test case 410
    try:
        result = maxOfList([23, 4, 23, 7, 23, 15])
        assert result == 23, f"Test 410 failed: got {result}, expected {23}"
        print(f"Test 410 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 410 failed: {e}")
        test_results.append(False)

    # Test case 411
    try:
        result = maxOfList([0, 23, 4, 23, 0, 23, 15])
        assert result == 23, f"Test 411 failed: got {result}, expected {23}"
        print(f"Test 411 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 411 failed: {e}")
        test_results.append(False)

    # Test case 412
    try:
        result = maxOfList([15, 23, 8, 5, 23])
        assert result == 23, f"Test 412 failed: got {result}, expected {23}"
        print(f"Test 412 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 412 failed: {e}")
        test_results.append(False)

    # Test case 413
    try:
        result = maxOfList([23, 4, 23, 8, 23, 15])
        assert result == 23, f"Test 413 failed: got {result}, expected {23}"
        print(f"Test 413 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 413 failed: {e}")
        test_results.append(False)

    # Test case 414
    try:
        result = maxOfList([3999999996, 1, 2, 3, 28, 6])
        assert result == 3999999996, f"Test 414 failed: got {result}, expected {3999999996}"
        print(f"Test 414 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 414 failed: {e}")
        test_results.append(False)

    # Test case 415
    try:
        result = maxOfList([0, 1, 2, 3, 14, 10, 6, 46])
        assert result == 46, f"Test 415 failed: got {result}, expected {46}"
        print(f"Test 415 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 415 failed: {e}")
        test_results.append(False)

    # Test case 416
    try:
        result = maxOfList([6, 10, 14, 2, 1])
        assert result == 14, f"Test 416 failed: got {result}, expected {14}"
        print(f"Test 416 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 416 failed: {e}")
        test_results.append(False)

    # Test case 417
    try:
        result = maxOfList([1, 1, 2, 3, 14, 10, 6, 12])
        assert result == 14, f"Test 417 failed: got {result}, expected {14}"
        print(f"Test 417 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 417 failed: {e}")
        test_results.append(False)

    # Test case 418
    try:
        result = maxOfList([2, 3, 14, 10, 6, 0, 0])
        assert result == 14, f"Test 418 failed: got {result}, expected {14}"
        print(f"Test 418 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 418 failed: {e}")
        test_results.append(False)

    # Test case 419
    try:
        result = maxOfList([1, 2, 42, 14, 20, 6])
        assert result == 42, f"Test 419 failed: got {result}, expected {42}"
        print(f"Test 419 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 419 failed: {e}")
        test_results.append(False)

    # Test case 420
    try:
        result = maxOfList([1, 2, 3, 14, 10, 6, 0, 0])
        assert result == 14, f"Test 420 failed: got {result}, expected {14}"
        print(f"Test 420 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 420 failed: {e}")
        test_results.append(False)

    # Test case 421
    try:
        result = maxOfList([10, 14, 3, 2, 1, 0, 23])
        assert result == 23, f"Test 421 failed: got {result}, expected {23}"
        print(f"Test 421 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 421 failed: {e}")
        test_results.append(False)

    # Test case 422
    try:
        result = maxOfList([1, 2, 14, 6])
        assert result == 14, f"Test 422 failed: got {result}, expected {14}"
        print(f"Test 422 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 422 failed: {e}")
        test_results.append(False)

    # Test case 423
    try:
        result = maxOfList([6, 10, 10, 3, 1, 15])
        assert result == 15, f"Test 423 failed: got {result}, expected {15}"
        print(f"Test 423 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 423 failed: {e}")
        test_results.append(False)

    # Test case 424
    try:
        result = maxOfList([6, 10, 14, 4, 2, 1])
        assert result == 14, f"Test 424 failed: got {result}, expected {14}"
        print(f"Test 424 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 424 failed: {e}")
        test_results.append(False)

    # Test case 425
    try:
        result = maxOfList([0, 20, 3, 14, 10, 6])
        assert result == 20, f"Test 425 failed: got {result}, expected {20}"
        print(f"Test 425 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 425 failed: {e}")
        test_results.append(False)

    # Test case 426
    try:
        result = maxOfList([3999999996, 1, 14, 10, 6, 0])
        assert result == 3999999996, f"Test 426 failed: got {result}, expected {3999999996}"
        print(f"Test 426 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 426 failed: {e}")
        test_results.append(False)

    # Test case 427
    try:
        result = maxOfList([18446744073709551616, 0, 18446744073709551615, 0])
        assert result == 18446744073709551616, f"Test 427 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 427 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 427 failed: {e}")
        test_results.append(False)

    # Test case 428
    try:
        result = maxOfList([0, 18446744073709551615, 0, 0, 0])
        assert result == 18446744073709551615, f"Test 428 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 428 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 428 failed: {e}")
        test_results.append(False)

    # Test case 429
    try:
        result = maxOfList([0, 18446744073709551616, 0, 30])
        assert result == 18446744073709551616, f"Test 429 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 429 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 429 failed: {e}")
        test_results.append(False)

    # Test case 430
    try:
        result = maxOfList([9, 0, 18446744073709551615, 0, 18446744073709551616])
        assert result == 18446744073709551616, f"Test 430 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 430 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 430 failed: {e}")
        test_results.append(False)

    # Test case 431
    try:
        result = maxOfList([18446744073709551615, 0, 0])
        assert result == 18446744073709551615, f"Test 431 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 431 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 431 failed: {e}")
        test_results.append(False)

    # Test case 432
    try:
        result = maxOfList([18446744073709551616, 0, 18446744073709551615, 17])
        assert result == 18446744073709551616, f"Test 432 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 432 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 432 failed: {e}")
        test_results.append(False)

    # Test case 433
    try:
        result = maxOfList([18446744073709551616, 5])
        assert result == 18446744073709551616, f"Test 433 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 433 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 433 failed: {e}")
        test_results.append(False)

    # Test case 434
    try:
        result = maxOfList([18446744073709551616, 1, 18446744073709551615, 7, 0])
        assert result == 18446744073709551616, f"Test 434 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 434 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 434 failed: {e}")
        test_results.append(False)

    # Test case 435
    try:
        result = maxOfList([18446744073709551615, 0, 123, 41, 6])
        assert result == 18446744073709551615, f"Test 435 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 435 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 435 failed: {e}")
        test_results.append(False)

    # Test case 436
    try:
        result = maxOfList([18446744073709551615])
        assert result == 18446744073709551615, f"Test 436 failed: got {result}, expected {18446744073709551615}"
        print(f"Test 436 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 436 failed: {e}")
        test_results.append(False)

    # Test case 437
    try:
        result = maxOfList([18446744073709551616, 0, 23, 0])
        assert result == 18446744073709551616, f"Test 437 failed: got {result}, expected {18446744073709551616}"
        print(f"Test 437 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 437 failed: {e}")
        test_results.append(False)

    # Test case 438
    try:
        result = maxOfList([0, 0, 42])
        assert result == 42, f"Test 438 failed: got {result}, expected {42}"
        print(f"Test 438 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 438 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
