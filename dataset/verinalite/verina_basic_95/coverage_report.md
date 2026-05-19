# Coverage Report

Total executable lines: 3
Covered lines: 3
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def swap(arr, i, j):
2: ✓     arr[i], arr[j] = arr[j], arr[i]
3: ✓     return arr
```

## Complete Test File

```python
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = swap([1, 2, 3, 4, 5], 1, 3)
        assert result == [1, 4, 3, 2, 5], f"Test 1 failed: got {result}, expected {[1, 4, 3, 2, 5]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = swap([10, 20, 30, 40], 0, 3)
        assert result == [40, 20, 30, 10], f"Test 2 failed: got {result}, expected {[40, 20, 30, 10]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = swap([7, 8, 9], 1, 2)
        assert result == [7, 9, 8], f"Test 3 failed: got {result}, expected {[7, 9, 8]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = swap([1, 2, 3, 4], 0, 0)
        assert result == [1, 2, 3, 4], f"Test 4 failed: got {result}, expected {[1, 2, 3, 4]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = swap([-1, -2, -3], 0, 2)
        assert result == [-3, -2, -1], f"Test 5 failed: got {result}, expected {[-3, -2, -1]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = swap([-5, 0, 5], 0, 2)
        assert result == [5, 0, -5], f"Test 6 failed: got {result}, expected {[5, 0, -5]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = swap([9, 8, 7, 6, 5], 2, 4)
        assert result == [9, 8, 5, 6, 7], f"Test 7 failed: got {result}, expected {[9, 8, 5, 6, 7]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = swap([9, 8, 7, 6, 5], 4, 2)
        assert result == [9, 8, 5, 6, 7], f"Test 8 failed: got {result}, expected {[9, 8, 5, 6, 7]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = swap([-1, -2, -3, -4], 0, 3)
        assert result == [-4, -2, -3, -1], f"Test 9 failed: got {result}, expected {[-4, -2, -3, -1]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = swap([11, 22, 33, 44, 55, 66, 77, 88], 1, 7)
        assert result == [11, 88, 33, 44, 55, 66, 77, 22], f"Test 10 failed: got {result}, expected {[11, 88, 33, 44, 55, 66, 77, 22]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = swap([11, 22, 33, 44, 55, 66, 77, 88], 7, 1)
        assert result == [11, 88, 33, 44, 55, 66, 77, 22], f"Test 11 failed: got {result}, expected {[11, 88, 33, 44, 55, 66, 77, 22]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = swap([1, 3, 5, 7, 9, 11, 13, 15, 17], 0, 8)
        assert result == [17, 3, 5, 7, 9, 11, 13, 15, 1], f"Test 12 failed: got {result}, expected {[17, 3, 5, 7, 9, 11, 13, 15, 1]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = swap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 0, 10)
        assert result == [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], f"Test 13 failed: got {result}, expected {[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = swap([5, -4, 3, -2, 1], 1, 3)
        assert result == [5, -2, 3, -4, 1], f"Test 14 failed: got {result}, expected {[5, -2, 3, -4, 1]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = swap([1, 3, 4, 5], 1, 3)
        assert result == [1, 5, 4, 3], f"Test 15 failed: got {result}, expected {[1, 5, 4, 3]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = swap([44, 2, 3, 4, 33], 1, 3)
        assert result == [44, 4, 3, 2, 33], f"Test 16 failed: got {result}, expected {[44, 4, 3, 2, 33]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = swap([5, 4, 3, 2], 1, 3)
        assert result == [5, 2, 3, 4], f"Test 17 failed: got {result}, expected {[5, 2, 3, 4]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = swap([1, 2, 3, 4, 5, 999999999998], 1, 4)
        assert result == [1, 5, 3, 4, 2, 999999999998], f"Test 18 failed: got {result}, expected {[1, 5, 3, 4, 2, 999999999998]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = swap([1, 2, 3, 4, 5], 0, 4)
        assert result == [5, 2, 3, 4, 1], f"Test 19 failed: got {result}, expected {[5, 2, 3, 4, 1]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = swap([20, 30, 40, 14], 0, 3)
        assert result == [14, 30, 40, 20], f"Test 20 failed: got {result}, expected {[14, 30, 40, 20]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = swap([10, 20, 30, 40, 12], 0, 3)
        assert result == [40, 20, 30, 10, 12], f"Test 21 failed: got {result}, expected {[40, 20, 30, 10, 12]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = swap([26, 40, 30, 20, 10], 0, 3)
        assert result == [20, 40, 30, 26, 10], f"Test 22 failed: got {result}, expected {[20, 40, 30, 26, 10]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = swap([10, 20, 30, 40, 0], 0, 2)
        assert result == [30, 20, 10, 40, 0], f"Test 23 failed: got {result}, expected {[30, 20, 10, 40, 0]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = swap([12, 20, 30, 41, -100], 0, 3)
        assert result == [41, 20, 30, 12, -100], f"Test 24 failed: got {result}, expected {[41, 20, 30, 12, -100]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = swap([7, 8, 9], 1, 0)
        assert result == [8, 7, 9], f"Test 25 failed: got {result}, expected {[8, 7, 9]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = swap([7, 8, 22], 0, 2)
        assert result == [22, 8, 7], f"Test 26 failed: got {result}, expected {[22, 8, 7]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = swap([-3, -1, 0], 0, 2)
        assert result == [0, -1, -3], f"Test 27 failed: got {result}, expected {[0, -1, -3]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = swap([-1, -2, -3, 0], 0, 2)
        assert result == [-3, -2, -1, 0], f"Test 28 failed: got {result}, expected {[-3, -2, -1, 0]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = swap([1, 2, 3, 4, 0], 0, 3)
        assert result == [4, 2, 3, 1, 0], f"Test 29 failed: got {result}, expected {[4, 2, 3, 1, 0]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = swap([4, 3, 2, 1], 2, 0)
        assert result == [2, 3, 4, 1], f"Test 30 failed: got {result}, expected {[2, 3, 4, 1]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = swap([1, 3, 3, 4], 1, 3)
        assert result == [1, 4, 3, 3], f"Test 31 failed: got {result}, expected {[1, 4, 3, 3]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = swap([0, 4, 3, 2, 1], 0, 4)
        assert result == [1, 4, 3, 2, 0], f"Test 32 failed: got {result}, expected {[1, 4, 3, 2, 0]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = swap([1, 2, -4, 0], 0, 2)
        assert result == [-4, 2, 1, 0], f"Test 33 failed: got {result}, expected {[-4, 2, 1, 0]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = swap([7, 6, 5], 2, 1)
        assert result == [7, 5, 6], f"Test 34 failed: got {result}, expected {[7, 5, 6]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = swap([5, 7, 13], 1, 0)
        assert result == [7, 5, 13], f"Test 35 failed: got {result}, expected {[7, 5, 13]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = swap([5, 6, 7], 0, 2)
        assert result == [7, 6, 5], f"Test 36 failed: got {result}, expected {[7, 6, 5]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = swap([5, 6, 7], 2, 1)
        assert result == [5, 7, 6], f"Test 37 failed: got {result}, expected {[5, 7, 6]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = swap([7, 6, 5], 1, 0)
        assert result == [6, 7, 5], f"Test 38 failed: got {result}, expected {[6, 7, 5]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = swap([5, 6, 7], 1, 0)
        assert result == [6, 5, 7], f"Test 39 failed: got {result}, expected {[6, 5, 7]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = swap([10, 20, 30, 40, 0], 3, 0)
        assert result == [40, 20, 30, 10, 0], f"Test 40 failed: got {result}, expected {[40, 20, 30, 10, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = swap([10, 20, 30, 40, -5], 2, 0)
        assert result == [30, 20, 10, 40, -5], f"Test 41 failed: got {result}, expected {[30, 20, 10, 40, -5]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = swap([10, 8, 7, 6, 5], 2, 4)
        assert result == [10, 8, 5, 6, 7], f"Test 42 failed: got {result}, expected {[10, 8, 5, 6, 7]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = swap([9, 8, 6, 5, 0], 0, 4)
        assert result == [0, 8, 6, 5, 9], f"Test 43 failed: got {result}, expected {[0, 8, 6, 5, 9]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = swap([9, 8, 7, 6, 5, 999999999998], 2, 4)
        assert result == [9, 8, 5, 6, 7, 999999999998], f"Test 44 failed: got {result}, expected {[9, 8, 5, 6, 7, 999999999998]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = swap([9, 8, 7, 6, 5], 4, 1)
        assert result == [9, 5, 7, 6, 8], f"Test 45 failed: got {result}, expected {[9, 5, 7, 6, 8]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = swap([9, 8, 7, 6, 5], 0, 2)
        assert result == [7, 8, 9, 6, 5], f"Test 46 failed: got {result}, expected {[7, 8, 9, 6, 5]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = swap([3, 1, 4, 1, 5, 9], 0, 2)
        assert result == [4, 1, 3, 1, 5, 9], f"Test 47 failed: got {result}, expected {[4, 1, 3, 1, 5, 9]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = swap([3, 1, 4, 1, 5, 9], 2, 1)
        assert result == [3, 4, 1, 1, 5, 9], f"Test 48 failed: got {result}, expected {[3, 4, 1, 1, 5, 9]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = swap([-1, -2, -3, -4, 0], 0, 3)
        assert result == [-4, -2, -3, -1, 0], f"Test 49 failed: got {result}, expected {[-4, -2, -3, -1, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = swap([-1, -2, -6, -4], 0, 3)
        assert result == [-4, -2, -6, -1], f"Test 50 failed: got {result}, expected {[-4, -2, -6, -1]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = swap([-1, -1, -3, -4], 0, 3)
        assert result == [-4, -1, -3, -1], f"Test 51 failed: got {result}, expected {[-4, -1, -3, -1]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = swap([48, -1, -2, -3, -4], 0, 3)
        assert result == [-3, -1, -2, 48, -4], f"Test 52 failed: got {result}, expected {[-3, -1, -2, 48, -4]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
