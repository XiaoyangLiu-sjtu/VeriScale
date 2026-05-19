# Coverage Report

Total executable lines: 12
Covered lines: 12
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def insertionSort(xs):
2: ✓     sorted_list = []
3: ✓     for x in xs:
4: ✓         inserted = False
5: ✓         for i in range(len(sorted_list)):
6: ✓             if x < sorted_list[i]:
7: ✓                 sorted_list.insert(i, x)
8: ✓                 inserted = True
9: ✓                 break
10: ✓         if not inserted:
11: ✓             sorted_list.append(x)
12: ✓     return sorted_list
```

## Complete Test File

```python
def insertionSort(xs):
    sorted_list = []
    for x in xs:
        inserted = False
        for i in range(len(sorted_list)):
            if x < sorted_list[i]:
                sorted_list.insert(i, x)
                inserted = True
                break
        if not inserted:
            sorted_list.append(x)
    return sorted_list

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = insertionSort([])
        assert result == [], f"Test 1 failed: got {result}, expected {[]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = insertionSort([42])
        assert result == [42], f"Test 2 failed: got {result}, expected {[42]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = insertionSort([3, 1, 4, 2])
        assert result == [1, 2, 3, 4], f"Test 3 failed: got {result}, expected {[1, 2, 3, 4]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = insertionSort([5, -1, 0, 10, -1])
        assert result == [-1, -1, 0, 5, 10], f"Test 4 failed: got {result}, expected {[-1, -1, 0, 5, 10]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = insertionSort([2, 2, 2, 2, 2])
        assert result == [2, 2, 2, 2, 2], f"Test 5 failed: got {result}, expected {[2, 2, 2, 2, 2]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = insertionSort([2147483647, -2147483648, 0, 2147483646, -2147483647])
        assert result == [-2147483648, -2147483647, 0, 2147483646, 2147483647], f"Test 6 failed: got {result}, expected {[-2147483648, -2147483647, 0, 2147483646, 2147483647]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = insertionSort([8, -8, 6, -6, 4, -4, 2, -2, 0])
        assert result == [-8, -6, -4, -2, 0, 2, 4, 6, 8], f"Test 7 failed: got {result}, expected {[-8, -6, -4, -2, 0, 2, 4, 6, 8]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = insertionSort([3, 3, 2, 1, 2, 3, 1, 0, 0])
        assert result == [0, 0, 1, 1, 2, 2, 3, 3, 3], f"Test 8 failed: got {result}, expected {[0, 0, 1, 1, 2, 2, 3, 3, 3]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = insertionSort([42, -2147483647, 0, 987654321])
        assert result == [-2147483647, 0, 42, 987654321], f"Test 9 failed: got {result}, expected {[-2147483647, 0, 42, 987654321]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = insertionSort([-2, 4, 1])
        assert result == [-2, 1, 4], f"Test 10 failed: got {result}, expected {[-2, 1, 4]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = insertionSort([3, 1, 4, 0, 17, -5])
        assert result == [-5, 0, 1, 3, 4, 17], f"Test 11 failed: got {result}, expected {[-5, 0, 1, 3, 4, 17]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = insertionSort([3, 1, 9223372036854775807, 4, 0])
        assert result == [0, 1, 3, 4, 9223372036854775807], f"Test 12 failed: got {result}, expected {[0, 1, 3, 4, 9223372036854775807]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = insertionSort([-4, 5, -1, 0, 10])
        assert result == [-4, -1, 0, 5, 10], f"Test 13 failed: got {result}, expected {[-4, -1, 0, 5, 10]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = insertionSort([-1, 10, 0, -2, 5])
        assert result == [-2, -1, 0, 5, 10], f"Test 14 failed: got {result}, expected {[-2, -1, 0, 5, 10]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = insertionSort([1, -17, -1, -3])
        assert result == [-17, -3, -1, 1], f"Test 15 failed: got {result}, expected {[-17, -3, -1, 1]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = insertionSort([1, 50, 77, 43])
        assert result == [1, 43, 50, 77], f"Test 16 failed: got {result}, expected {[1, 43, 50, 77]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = insertionSort([-1, 0, -2147483647])
        assert result == [-2147483647, -1, 0], f"Test 17 failed: got {result}, expected {[-2147483647, -1, 0]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = insertionSort([0, 5, 4, 3, 2, 1, 0, 0])
        assert result == [0, 0, 0, 1, 2, 3, 4, 5], f"Test 18 failed: got {result}, expected {[0, 0, 0, 1, 2, 3, 4, 5]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = insertionSort([1, 2, 3, 2, 5])
        assert result == [1, 2, 2, 3, 5], f"Test 19 failed: got {result}, expected {[1, 2, 2, 3, 5]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = insertionSort([5, 4, 2, 2, 6])
        assert result == [2, 2, 4, 5, 6], f"Test 20 failed: got {result}, expected {[2, 2, 4, 5, 6]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = insertionSort([0, -1, -2, -2, -4, 0])
        assert result == [-4, -2, -2, -1, 0, 0], f"Test 21 failed: got {result}, expected {[-4, -2, -2, -1, 0, 0]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = insertionSort([0, -1, -2, -3, -4, 2])
        assert result == [-4, -3, -2, -1, 0, 2], f"Test 22 failed: got {result}, expected {[-4, -3, -2, -1, 0, 2]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = insertionSort([22, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
        assert result == [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22], f"Test 23 failed: got {result}, expected {[0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = insertionSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 999999999999999999999999, 0])
        assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999999999999999999999999], f"Test 24 failed: got {result}, expected {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999999999999999999999999]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = insertionSort([0, -50, 50, -100, 100, -13])
        assert result == [-100, -50, -13, 0, 50, 100], f"Test 25 failed: got {result}, expected {[-100, -50, -13, 0, 50, 100]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = insertionSort([0, 0, -1, 1, -999999999999999999999999, 999999999999999999999999, 17])
        assert result == [-999999999999999999999999, -1, 0, 0, 1, 17, 999999999999999999999999], f"Test 26 failed: got {result}, expected {[-999999999999999999999999, -1, 0, 0, 1, 17, 999999999999999999999999]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = insertionSort([123456789, 999999999999999999999999, -999999999999999999999999, 1, -1, 0])
        assert result == [-999999999999999999999999, -1, 0, 1, 123456789, 999999999999999999999999], f"Test 27 failed: got {result}, expected {[-999999999999999999999999, -1, 0, 1, 123456789, 999999999999999999999999]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = insertionSort([-1, -999999999999999999999999, 999999999999999999999999])
        assert result == [-999999999999999999999999, -1, 999999999999999999999999], f"Test 28 failed: got {result}, expected {[-999999999999999999999999, -1, 999999999999999999999999]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = insertionSort([-100, 1, 1, 5, 5, 3, 3, 7, 7])
        assert result == [-100, 1, 1, 3, 3, 5, 5, 7, 7], f"Test 29 failed: got {result}, expected {[-100, 1, 1, 3, 3, 5, 5, 7, 7]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = insertionSort([7, 3, 3, 5, 5, 1, 1])
        assert result == [1, 1, 3, 3, 5, 5, 7], f"Test 30 failed: got {result}, expected {[1, 1, 3, 3, 5, 5, 7]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = insertionSort([7, 7, 3, 3, 5, 5, 1, 1, 77])
        assert result == [1, 1, 3, 3, 5, 5, 7, 7, 77], f"Test 31 failed: got {result}, expected {[1, 1, 3, 3, 5, 5, 7, 7, 77]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = insertionSort([1, 3, 3, 3, 2, 2, 1, -987654321])
        assert result == [-987654321, 1, 1, 2, 2, 3, 3, 3], f"Test 32 failed: got {result}, expected {[-987654321, 1, 1, 2, 2, 3, 3, 3]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = insertionSort([1, 2, 2, 3, 3, 3, 2, 2, 1, 12, 0])
        assert result == [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 12], f"Test 33 failed: got {result}, expected {[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 12]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = insertionSort([0, -17, -42, 42, 50, 42])
        assert result == [-42, -17, 0, 42, 42, 50], f"Test 34 failed: got {result}, expected {[-42, -17, 0, 42, 42, 50]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = insertionSort([42, 42, -42, 17])
        assert result == [-42, 17, 42, 42], f"Test 35 failed: got {result}, expected {[-42, 17, 42, 42]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = insertionSort([8, -8, 6, -6, 4, -4, 2, -2, 0, -1])
        assert result == [-8, -6, -4, -2, -1, 0, 2, 4, 6, 8], f"Test 36 failed: got {result}, expected {[-8, -6, -4, -2, -1, 0, 2, 4, 6, 8]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = insertionSort([-8, -8, 6, -6, 4, -4, 2, 17, 0, 998, -13])
        assert result == [-13, -8, -8, -6, -4, 0, 2, 4, 6, 17, 998], f"Test 37 failed: got {result}, expected {[-13, -8, -8, -6, -4, 0, 2, 4, 6, 17, 998]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = insertionSort([9, 1, 8, 2, 7, 3, 6, 4, 5, 0, 0])
        assert result == [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], f"Test 38 failed: got {result}, expected {[0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = insertionSort([1, 0, 1, 0, 50, 0, 1, 0])
        assert result == [0, 0, 0, 0, 1, 1, 1, 50], f"Test 39 failed: got {result}, expected {[0, 0, 0, 0, 1, 1, 1, 50]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = insertionSort([0, 1, 0, 1, 0, 1, 0, 1, -2147483647, 0])
        assert result == [-2147483647, 0, 0, 0, 0, 0, 1, 1, 1, 1], f"Test 40 failed: got {result}, expected {[-2147483647, 0, 0, 0, 0, 0, 1, 1, 1, 1]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = insertionSort([-7, -1, -3, 22, -5, 0])
        assert result == [-7, -5, -3, -1, 0, 22], f"Test 41 failed: got {result}, expected {[-7, -5, -3, -1, 0, 22]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = insertionSort([55, 2147483649, 2147483647, -7, -1, -3, 6, -5])
        assert result == [-7, -5, -3, -1, 6, 55, 2147483647, 2147483649], f"Test 42 failed: got {result}, expected {[-7, -5, -3, -1, 6, 55, 2147483647, 2147483649]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = insertionSort([-13, 13, -987654321])
        assert result == [-987654321, -13, 13], f"Test 43 failed: got {result}, expected {[-987654321, -13, 13]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = insertionSort([123456789, -13, 12])
        assert result == [-13, 12, 123456789], f"Test 44 failed: got {result}, expected {[-13, 12, 123456789]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = insertionSort([0, 1, 3, 2, 1, 2, 3, 0])
        assert result == [0, 0, 1, 1, 2, 2, 3, 3], f"Test 45 failed: got {result}, expected {[0, 0, 1, 1, 2, 2, 3, 3]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = insertionSort([3, 3, 2, 1, 2, 3, 1, 0, 0, 0, 0, 13, 0])
        assert result == [0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 13], f"Test 46 failed: got {result}, expected {[0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 13]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = insertionSort([3, 3, 1, 1, 2, 3, 1, 0, 0, 0])
        assert result == [0, 0, 0, 1, 1, 1, 2, 3, 3, 3], f"Test 47 failed: got {result}, expected {[0, 0, 0, 1, 1, 1, 2, 3, 3, 3]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = insertionSort([3, -9, 7, 1, -4, 12, -4, 12])
        assert result == [-9, -4, -4, 1, 3, 7, 12, 12], f"Test 48 failed: got {result}, expected {[-9, -4, -4, 1, 3, 7, 12, 12]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = insertionSort([4, -1, 2, -1, -1, 0, -1])
        assert result == [-1, -1, -1, -1, 0, 2, 4], f"Test 49 failed: got {result}, expected {[-1, -1, -1, -1, 0, 2, 4]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = insertionSort([-4, 4, 4, 5, 6, 5, 6, 5, 6])
        assert result == [-4, 4, 4, 5, 5, 5, 6, 6, 6], f"Test 50 failed: got {result}, expected {[-4, 4, 4, 5, 5, 5, 6, 6, 6]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = insertionSort([-3, -1, 1, -1, 1, -1, 1, -1, 1])
        assert result == [-3, -1, -1, -1, -1, 1, 1, 1, 1], f"Test 51 failed: got {result}, expected {[-3, -1, -1, -1, -1, 1, 1, 1, 1]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = insertionSort([123456789, 987654321, -123456789, -987654321, -1975308642, -2147483648, 0])
        assert result == [-2147483648, -1975308642, -987654321, -123456789, 0, 123456789, 987654321], f"Test 52 failed: got {result}, expected {[-2147483648, -1975308642, -987654321, -123456789, 0, 123456789, 987654321]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = insertionSort([1, 2, 2147483649, -1000, 0])
        assert result == [-1000, 0, 1, 2, 2147483649], f"Test 53 failed: got {result}, expected {[-1000, 0, 1, 2, 2147483649]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = insertionSort([1, 2, -1])
        assert result == [-1, 1, 2], f"Test 54 failed: got {result}, expected {[-1, 1, 2]}"
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
