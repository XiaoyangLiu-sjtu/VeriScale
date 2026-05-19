# Coverage Report

Total executable lines: 9
Covered lines: 9
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def SelectionSort(a):
2: ✓     n = len(a)
3: ✓     for i in range(n):
4: ✓         min_index = i
5: ✓         for j in range(i + 1, n):
6: ✓             if a[j] < a[min_index]:
7: ✓                 min_index = j
8: ✓         a[i], a[min_index] = a[min_index], a[i]
9: ✓     return a
```

## Complete Test File

```python
def SelectionSort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = SelectionSort([3, 1, 2])
        assert result == [1, 2, 3], f"Test 1 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = SelectionSort([0])
        assert result == [0], f"Test 2 failed: got {result}, expected {[0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = SelectionSort([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5], f"Test 3 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = SelectionSort([2, 2, 1, 4])
        assert result == [1, 2, 2, 4], f"Test 4 failed: got {result}, expected {[1, 2, 2, 4]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = SelectionSort([10, -5, 0, 3])
        assert result == [-5, 0, 3, 10], f"Test 5 failed: got {result}, expected {[-5, 0, 3, 10]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = SelectionSort([1, 3, 2, 3, 1])
        assert result == [1, 1, 2, 3, 3], f"Test 6 failed: got {result}, expected {[1, 1, 2, 3, 3]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = SelectionSort([0, 0, 0, -1, -1, 2, 2])
        assert result == [-1, -1, 0, 0, 0, 2, 2], f"Test 7 failed: got {result}, expected {[-1, -1, 0, 0, 0, 2, 2]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = SelectionSort([9223372036854775807, -9223372036854775808, 0])
        assert result == [-9223372036854775808, 0, 9223372036854775807], f"Test 8 failed: got {result}, expected {[-9223372036854775808, 0, 9223372036854775807]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = SelectionSort([2147483647, -2147483648, 2147483646, -2147483647])
        assert result == [-2147483648, -2147483647, 2147483646, 2147483647], f"Test 9 failed: got {result}, expected {[-2147483648, -2147483647, 2147483646, 2147483647]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = SelectionSort([1000000, -1000000, 999999, -999999, 0])
        assert result == [-1000000, -999999, 0, 999999, 1000000], f"Test 10 failed: got {result}, expected {[-1000000, -999999, 0, 999999, 1000000]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = SelectionSort([7, -3, 7, -3, 7, -3])
        assert result == [-3, -3, -3, 7, 7, 7], f"Test 11 failed: got {result}, expected {[-3, -3, -3, 7, 7, 7]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = SelectionSort([0, 1, 0, 1, 0, 1, 0, 1])
        assert result == [0, 0, 0, 0, 1, 1, 1, 1], f"Test 12 failed: got {result}, expected {[0, 0, 0, 0, 1, 1, 1, 1]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = SelectionSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        assert result == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], f"Test 13 failed: got {result}, expected {[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = SelectionSort([8, 6, 7, 5, 3, 0, 9])
        assert result == [0, 3, 5, 6, 7, 8, 9], f"Test 14 failed: got {result}, expected {[0, 3, 5, 6, 7, 8, 9]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = SelectionSort([1, -1, 1, -1, 1, -1, 1, -1, 0])
        assert result == [-1, -1, -1, -1, 0, 1, 1, 1, 1], f"Test 15 failed: got {result}, expected {[-1, -1, -1, -1, 0, 1, 1, 1, 1]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = SelectionSort([2, 3, 2, 3, 2, 3, 1, 1, 1])
        assert result == [1, 1, 1, 2, 2, 2, 3, 3, 3], f"Test 16 failed: got {result}, expected {[1, 1, 1, 2, 2, 2, 3, 3, 3]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = SelectionSort([4, 2, 4, 2, 4, 2, 4, 2])
        assert result == [2, 2, 2, 2, 4, 4, 4, 4], f"Test 17 failed: got {result}, expected {[2, 2, 2, 2, 4, 4, 4, 4]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = SelectionSort([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1, 0])
        assert result == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], f"Test 18 failed: got {result}, expected {[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = SelectionSort([31, -1, 0, 31, -1, 0, 31, -1, 0])
        assert result == [-1, -1, -1, 0, 0, 0, 31, 31, 31], f"Test 19 failed: got {result}, expected {[-1, -1, -1, 0, 0, 0, 31, 31, 31]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = SelectionSort([1, 1000, 2, 999, 3, 998, 4, 997, 5, 996])
        assert result == [1, 2, 3, 4, 5, 996, 997, 998, 999, 1000], f"Test 20 failed: got {result}, expected {[1, 2, 3, 4, 5, 996, 997, 998, 999, 1000]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = SelectionSort([12, -7, 12, -7, 0, 0, 5, -3, 8, -1])
        assert result == [-7, -7, -3, -1, 0, 0, 5, 8, 12, 12], f"Test 21 failed: got {result}, expected {[-7, -7, -3, -1, 0, 0, 5, 8, 12, 12]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = SelectionSort([3, 1, 3, 0])
        assert result == [0, 1, 3, 3], f"Test 22 failed: got {result}, expected {[0, 1, 3, 3]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = SelectionSort([-40, 1, 2, 0, 0, -1000000])
        assert result == [-1000000, -40, 0, 0, 1, 2], f"Test 23 failed: got {result}, expected {[-1000000, -40, 0, 0, 1, 2]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = SelectionSort([12, 1, 2, 0, 0])
        assert result == [0, 0, 1, 2, 12], f"Test 24 failed: got {result}, expected {[0, 0, 1, 2, 12]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = SelectionSort([6, 1, 2])
        assert result == [1, 2, 6], f"Test 25 failed: got {result}, expected {[1, 2, 6]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = SelectionSort([3, 1, 2, 0, 0])
        assert result == [0, 0, 1, 2, 3], f"Test 26 failed: got {result}, expected {[0, 0, 1, 2, 3]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = SelectionSort([0, 2, -1])
        assert result == [-1, 0, 2], f"Test 27 failed: got {result}, expected {[-1, 0, 2]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = SelectionSort([2, 1, 3, 0, 0, 0])
        assert result == [0, 0, 0, 1, 2, 3], f"Test 28 failed: got {result}, expected {[0, 0, 0, 1, 2, 3]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = SelectionSort([0, 0, 42, 1, 3])
        assert result == [0, 0, 1, 3, 42], f"Test 29 failed: got {result}, expected {[0, 0, 1, 3, 42]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = SelectionSort([11, -1, 0])
        assert result == [-1, 0, 11], f"Test 30 failed: got {result}, expected {[-1, 0, 11]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = SelectionSort([0, 8, 0, 1000000])
        assert result == [0, 0, 8, 1000000], f"Test 31 failed: got {result}, expected {[0, 0, 8, 1000000]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = SelectionSort([0, 12, -4])
        assert result == [-4, 0, 12], f"Test 32 failed: got {result}, expected {[-4, 0, 12]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = SelectionSort([1, -2, 3, 4])
        assert result == [-2, 1, 3, 4], f"Test 33 failed: got {result}, expected {[-2, 1, 3, 4]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = SelectionSort([5, 4, 3, 2, 1, 42, -1000000, 0])
        assert result == [-1000000, 0, 1, 2, 3, 4, 5, 42], f"Test 34 failed: got {result}, expected {[-1000000, 0, 1, 2, 3, 4, 5, 42]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = SelectionSort([10, 4, 2, 2, 1, -7, 0])
        assert result == [-7, 0, 1, 2, 2, 4, 10], f"Test 35 failed: got {result}, expected {[-7, 0, 1, 2, 2, 4, 10]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = SelectionSort([5, 4, 3, 2, 1, 8])
        assert result == [1, 2, 3, 4, 5, 8], f"Test 36 failed: got {result}, expected {[1, 2, 3, 4, 5, 8]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = SelectionSort([5, 6, 1, 0])
        assert result == [0, 1, 5, 6], f"Test 37 failed: got {result}, expected {[0, 1, 5, 6]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = SelectionSort([0, 2, 12, 4, 5])
        assert result == [0, 2, 4, 5, 12], f"Test 38 failed: got {result}, expected {[0, 2, 4, 5, 12]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = SelectionSort([1000, 999999, 1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5, 1000, 999999], f"Test 39 failed: got {result}, expected {[1, 2, 3, 4, 5, 1000, 999999]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = SelectionSort([2, -2, 0, 4, 1, 70])
        assert result == [-2, 0, 1, 2, 4, 70], f"Test 40 failed: got {result}, expected {[-2, 0, 1, 2, 4, 70]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = SelectionSort([4, 1, 2, 2, 0, -20])
        assert result == [-20, 0, 1, 2, 2, 4], f"Test 41 failed: got {result}, expected {[-20, 0, 1, 2, 2, 4]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = SelectionSort([4, 1, 2, 2])
        assert result == [1, 2, 2, 4], f"Test 42 failed: got {result}, expected {[1, 2, 2, 4]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = SelectionSort([2, 2, 1, 4, -2147483648])
        assert result == [-2147483648, 1, 2, 2, 4], f"Test 43 failed: got {result}, expected {[-2147483648, 1, 2, 2, 4]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = SelectionSort([2, 2, 1, 4, 0, -7])
        assert result == [-7, 0, 1, 2, 2, 4], f"Test 44 failed: got {result}, expected {[-7, 0, 1, 2, 2, 4]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = SelectionSort([2, 1, 40, 0, 20])
        assert result == [0, 1, 2, 20, 40], f"Test 45 failed: got {result}, expected {[0, 1, 2, 20, 40]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = SelectionSort([7, 4, 1, 2, 2, 4])
        assert result == [1, 2, 2, 4, 4, 7], f"Test 46 failed: got {result}, expected {[1, 2, 2, 4, 4, 7]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = SelectionSort([0, 1, 2, 0])
        assert result == [0, 0, 1, 2], f"Test 47 failed: got {result}, expected {[0, 0, 1, 2]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = SelectionSort([4, 0, 2, 2147483647])
        assert result == [0, 2, 4, 2147483647], f"Test 48 failed: got {result}, expected {[0, 2, 4, 2147483647]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = SelectionSort([0, 4, -1, -999999, 2])
        assert result == [-999999, -1, 0, 2, 4], f"Test 49 failed: got {result}, expected {[-999999, -1, 0, 2, 4]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = SelectionSort([3, 0, -5, 10])
        assert result == [-5, 0, 3, 10], f"Test 50 failed: got {result}, expected {[-5, 0, 3, 10]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = SelectionSort([3, 0, -5, 10])
        assert result == [-5, 0, 3, 10], f"Test 51 failed: got {result}, expected {[-5, 0, 3, 10]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
