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
        result = maxOfList([9, 1, 8, 2, 7, 3, 6, 4, 5, 0])
        assert result == 9, f"Test 6 failed: got {result}, expected {9}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = maxOfList([6, 1, 6, 1, 6, 1, 6, 1])
        assert result == 6, f"Test 7 failed: got {result}, expected {6}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
        assert result == 9, f"Test 8 failed: got {result}, expected {9}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = maxOfList([2, 2, 1, 0, 0, 0])
        assert result == 2, f"Test 9 failed: got {result}, expected {2}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = maxOfList([1, 2, 3, 0, 0])
        assert result == 3, f"Test 10 failed: got {result}, expected {3}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = maxOfList([1, 2, 3, 0])
        assert result == 3, f"Test 11 failed: got {result}, expected {3}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = maxOfList([0, 0, 58, 3, 2, 1])
        assert result == 58, f"Test 12 failed: got {result}, expected {58}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = maxOfList([5, 5, 4])
        assert result == 5, f"Test 13 failed: got {result}, expected {5}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = maxOfList([5, 5, 5, 0, 12, 3])
        assert result == 12, f"Test 14 failed: got {result}, expected {12}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = maxOfList([9, 1, 10, 0, 0])
        assert result == 10, f"Test 15 failed: got {result}, expected {10}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = maxOfList([10, 0, 9, 11])
        assert result == 11, f"Test 16 failed: got {result}, expected {11}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = maxOfList([0, 18, 1, 10])
        assert result == 18, f"Test 17 failed: got {result}, expected {18}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = maxOfList([10, 9, 0])
        assert result == 10, f"Test 18 failed: got {result}, expected {10}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = maxOfList([10, 1, 9, 0, 5, 0])
        assert result == 10, f"Test 19 failed: got {result}, expected {10}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = maxOfList([0, 58, 1, 9])
        assert result == 58, f"Test 20 failed: got {result}, expected {58}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = maxOfList([0, 58, 0])
        assert result == 58, f"Test 21 failed: got {result}, expected {58}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = maxOfList([7, 123456789, 0, 9])
        assert result == 123456789, f"Test 22 failed: got {result}, expected {123456789}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = maxOfList([9007199254740990, 7])
        assert result == 9007199254740990, f"Test 23 failed: got {result}, expected {9007199254740990}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = maxOfList([0, 0, 999999, 0])
        assert result == 999999, f"Test 24 failed: got {result}, expected {999999}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = maxOfList([0, 0, 0, 0, 35, 0])
        assert result == 35, f"Test 25 failed: got {result}, expected {35}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = maxOfList([0, 0, 1, 0])
        assert result == 1, f"Test 26 failed: got {result}, expected {1}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = maxOfList([999999, 987654321, 35])
        assert result == 987654321, f"Test 27 failed: got {result}, expected {987654321}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = maxOfList([2, 0, 42])
        assert result == 42, f"Test 28 failed: got {result}, expected {42}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = maxOfList([42, 0, 100, 9007199254740991, 0])
        assert result == 9007199254740991, f"Test 29 failed: got {result}, expected {9007199254740991}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = maxOfList([123456789, 6, 12, 0])
        assert result == 123456789, f"Test 30 failed: got {result}, expected {123456789}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = maxOfList([0, 2, 0, 35, 0])
        assert result == 35, f"Test 31 failed: got {result}, expected {35}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = maxOfList([0, 5, 5, 5, 19])
        assert result == 19, f"Test 32 failed: got {result}, expected {19}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = maxOfList([2, 7, 1, 7, 3, 0])
        assert result == 7, f"Test 33 failed: got {result}, expected {7}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = maxOfList([9, 1, 8, 2, 7, 3, 6, 4, 5, 0, 13])
        assert result == 13, f"Test 34 failed: got {result}, expected {13}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = maxOfList([3, 0, 4, 1, 9, 42, 6, 10])
        assert result == 42, f"Test 35 failed: got {result}, expected {42}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = maxOfList([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == 9, f"Test 36 failed: got {result}, expected {9}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = maxOfList([999999, 10, 9, 10, 0, 58])
        assert result == 999999, f"Test 37 failed: got {result}, expected {999999}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = maxOfList([999999, 1, 4, 3])
        assert result == 999999, f"Test 38 failed: got {result}, expected {999999}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = maxOfList([1, 2, 3, 0])
        assert result == 3, f"Test 39 failed: got {result}, expected {3}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = maxOfList([1, 2, 3, 999999, 0, 0, 6, 0])
        assert result == 999999, f"Test 40 failed: got {result}, expected {999999}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = maxOfList([9, 0, 3, 5, 7, 6, 8])
        assert result == 9, f"Test 41 failed: got {result}, expected {9}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = maxOfList([8, 6, 5, 3, 0, 10, 555555556, 0])
        assert result == 555555556, f"Test 42 failed: got {result}, expected {555555556}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = maxOfList([11, 11, 11, 11, 11, 1024, 11, 0, 7])
        assert result == 1024, f"Test 43 failed: got {result}, expected {1024}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = maxOfList([0, 2, 0, 2, 0, 2, 0, 0])
        assert result == 2, f"Test 44 failed: got {result}, expected {2}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = maxOfList([0, 12, 1, 12, 1, 12, 0])
        assert result == 12, f"Test 45 failed: got {result}, expected {12}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = maxOfList([7, 14, 21, 29, 35, 116, 0])
        assert result == 116, f"Test 46 failed: got {result}, expected {116}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = maxOfList([2, 3, 5, 7, 0, 13, 17, 0, 29, 0])
        assert result == 29, f"Test 47 failed: got {result}, expected {29}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = maxOfList([28, 23, 19, 13, 11, 7, 5, 3, 2, 98, 0])
        assert result == 98, f"Test 48 failed: got {result}, expected {98}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = maxOfList([6, 1, 6, 1, 6, 1, 6, 1, 987654321])
        assert result == 987654321, f"Test 49 failed: got {result}, expected {987654321}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = maxOfList([6, 1, 555555556, 1, 6, 1, 26, 1, 0])
        assert result == 555555556, f"Test 50 failed: got {result}, expected {555555556}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = maxOfList([0, 98, 101, 987654321, 555555555])
        assert result == 987654321, f"Test 51 failed: got {result}, expected {987654321}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = maxOfList([123456789, 987654321, 555555555, 555555555])
        assert result == 987654321, f"Test 52 failed: got {result}, expected {987654321}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = maxOfList([9007199254740990, 1, 0, 115])
        assert result == 9007199254740990, f"Test 53 failed: got {result}, expected {9007199254740990}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = maxOfList([9007199254740990, 1, 9007199254740991, 0])
        assert result == 9007199254740991, f"Test 54 failed: got {result}, expected {9007199254740991}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = maxOfList([3, 9, 64, 9, 8, 5, 5, 6, 2, 9, 5, 1, 6, 1, 3, 115])
        assert result == 115, f"Test 55 failed: got {result}, expected {115}"
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
