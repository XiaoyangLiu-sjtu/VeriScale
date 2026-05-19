# Coverage Report

Total executable lines: 6
Covered lines: 6
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def modify_array_element(arr, index1, index2, val):
2: ✓     new_arr = arr.copy()
3: ✓     modified_inner = new_arr[index1][:]
4: ✓     modified_inner[index2] = val
5: ✓     new_arr[index1] = modified_inner
6: ✓     return new_arr
```

## Complete Test File

```python
def modify_array_element(arr, index1, index2, val):
    new_arr = arr.copy()
    modified_inner = new_arr[index1][:]
    modified_inner[index2] = val
    new_arr[index1] = modified_inner
    return new_arr

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 0, 1, 99)
        assert result == [[1, 99, 3], [4, 5, 6]], f"Test 1 failed: got {result}, expected {[[1, 99, 3], [4, 5, 6]]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = modify_array_element([[7, 8], [9, 10]], 1, 0, 0)
        assert result == [[7, 8], [0, 10]], f"Test 2 failed: got {result}, expected {[[7, 8], [0, 10]]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = modify_array_element([[0, 0, 0]], 0, 2, 5)
        assert result == [[0, 0, 5]], f"Test 3 failed: got {result}, expected {[[0, 0, 5]]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = modify_array_element([[3, 4, 5], [6, 7, 8], [9, 10, 11]], 2, 1, 100)
        assert result == [[3, 4, 5], [6, 7, 8], [9, 100, 11]], f"Test 4 failed: got {result}, expected {[[3, 4, 5], [6, 7, 8], [9, 100, 11]]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = modify_array_element([[1]], 0, 0, 42)
        assert result == [[42]], f"Test 5 failed: got {result}, expected {[[42]]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 0, 2, 99)
        assert result == [[1, 2, 99], [4, 5, 6]], f"Test 6 failed: got {result}, expected {[[1, 2, 99], [4, 5, 6]]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 1, 1, 0)
        assert result == [[1, 2, 3], [4, 0, 6]], f"Test 7 failed: got {result}, expected {[[1, 2, 3], [4, 0, 6]]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = modify_array_element([[0, 0, 0]], 0, 2, 5)
        assert result == [[0, 0, 5]], f"Test 8 failed: got {result}, expected {[[0, 0, 5]]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = modify_array_element([[3, 4, 5], [6, 7, 8], [9, 10, 11]], 2, 1, 100)
        assert result == [[3, 4, 5], [6, 7, 8], [9, 100, 11]], f"Test 9 failed: got {result}, expected {[[3, 4, 5], [6, 7, 8], [9, 100, 11]]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = modify_array_element([[5, 6, 7, 8]], 0, 3, 1)
        assert result == [[5, 6, 7, 1]], f"Test 10 failed: got {result}, expected {[[5, 6, 7, 1]]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = modify_array_element([[2], [], [3, 4]], 2, 1, 8)
        assert result == [[2], [], [3, 8]], f"Test 11 failed: got {result}, expected {[[2], [], [3, 8]]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = modify_array_element([[], [1, 2, 3]], 1, 2, 9)
        assert result == [[], [1, 2, 9]], f"Test 12 failed: got {result}, expected {[[], [1, 2, 9]]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = modify_array_element([[10, 20], [30], [40, 50, 60, 70]], 2, 3, 0)
        assert result == [[10, 20], [30], [40, 50, 60, 0]], f"Test 13 failed: got {result}, expected {[[10, 20], [30], [40, 50, 60, 0]]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = modify_array_element([[1, 1, 1], [2, 2], [3]], 0, 1, 2)
        assert result == [[1, 2, 1], [2, 2], [3]], f"Test 14 failed: got {result}, expected {[[1, 2, 1], [2, 2], [3]]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = modify_array_element([[100, 200, 300, 400], [500, 600]], 0, 3, 700)
        assert result == [[100, 200, 300, 700], [500, 600]], f"Test 15 failed: got {result}, expected {[[100, 200, 300, 700], [500, 600]]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = modify_array_element([[8, 6, 7, 5, 3, 0, 9]], 0, 6, 4)
        assert result == [[8, 6, 7, 5, 3, 0, 4]], f"Test 16 failed: got {result}, expected {[[8, 6, 7, 5, 3, 0, 4]]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = modify_array_element([[0, 1], [2, 3], [4, 5], [6, 7]], 3, 1, 8)
        assert result == [[0, 1], [2, 3], [4, 5], [6, 8]], f"Test 17 failed: got {result}, expected {[[0, 1], [2, 3], [4, 5], [6, 8]]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = modify_array_element([[11, 22, 33], [44, 55, 66], [77, 88, 99]], 1, 2, 123)
        assert result == [[11, 22, 33], [44, 55, 123], [77, 88, 99]], f"Test 18 failed: got {result}, expected {[[11, 22, 33], [44, 55, 123], [77, 88, 99]]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = modify_array_element([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 1, 4, 11)
        assert result == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 11]], f"Test 19 failed: got {result}, expected {[[1, 2, 3, 4, 5], [6, 7, 8, 9, 11]]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = modify_array_element([[1, 3, 5, 7], [], [2, 4, 6, 8], [9]], 2, 2, 10)
        assert result == [[1, 3, 5, 7], [], [2, 4, 10, 8], [9]], f"Test 20 failed: got {result}, expected {[[1, 3, 5, 7], [], [2, 4, 10, 8], [9]]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = modify_array_element([[12, 13], [14, 15, 16], [17, 18, 19, 20]], 1, 1, 21)
        assert result == [[12, 13], [14, 21, 16], [17, 18, 19, 20]], f"Test 21 failed: got {result}, expected {[[12, 13], [14, 21, 16], [17, 18, 19, 20]]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = modify_array_element([[5, 4, 3, 2, 1], [10, 20, 30], [40, 50]], 0, 4, 0)
        assert result == [[5, 4, 3, 2, 0], [10, 20, 30], [40, 50]], f"Test 22 failed: got {result}, expected {[[5, 4, 3, 2, 0], [10, 20, 30], [40, 50]]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = modify_array_element([[5, 4, 3, 2, 1], [10, 20, 30], [40, 50]], 2, 1, 60)
        assert result == [[5, 4, 3, 2, 1], [10, 20, 30], [40, 60]], f"Test 23 failed: got {result}, expected {[[5, 4, 3, 2, 1], [10, 20, 30], [40, 60]]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = modify_array_element([[1, 0, 1, 0, 1, 0], [2, 2, 2, 2], [3, 3]], 1, 3, 9)
        assert result == [[1, 0, 1, 0, 1, 0], [2, 2, 2, 9], [3, 3]], f"Test 24 failed: got {result}, expected {[[1, 0, 1, 0, 1, 0], [2, 2, 2, 9], [3, 3]]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = modify_array_element([[6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9]], 2, 2, 1)
        assert result == [[6, 6, 6], [7, 7, 7], [8, 8, 1], [9, 9, 9]], f"Test 25 failed: got {result}, expected {[[6, 6, 6], [7, 7, 7], [8, 8, 1], [9, 9, 9]]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = modify_array_element([[123], [], [], [456, 789]], 3, 1, 0)
        assert result == [[123], [], [], [456, 0]], f"Test 26 failed: got {result}, expected {[[123], [], [], [456, 0]]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = modify_array_element([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], 4, 1, 11)
        assert result == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 11]], f"Test 27 failed: got {result}, expected {[[1, 2], [3, 4], [5, 6], [7, 8], [9, 11]]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = modify_array_element([[1, 1, 1], [2, 2], [3]], 0, 1, 99)
        assert result == [[1, 99, 1], [2, 2], [3]], f"Test 28 failed: got {result}, expected {[[1, 99, 1], [2, 2], [3]]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = modify_array_element([[5, 6, 7, 8]], 0, 2, 2)
        assert result == [[5, 6, 2, 8]], f"Test 29 failed: got {result}, expected {[[5, 6, 2, 8]]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 0, 1, 0)
        assert result == [[1, 0, 3], [4, 5, 6]], f"Test 30 failed: got {result}, expected {[[1, 0, 3], [4, 5, 6]]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 0, 2, 99)
        assert result == [[1, 2, 99], [4, 5, 6]], f"Test 31 failed: got {result}, expected {[[1, 2, 99], [4, 5, 6]]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = modify_array_element([[0, 0, 0]], 0, 2, 21)
        assert result == [[0, 0, 21]], f"Test 32 failed: got {result}, expected {[[0, 0, 21]]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 0, 1, 9)
        assert result == [[1, 9, 3], [4, 5, 6]], f"Test 33 failed: got {result}, expected {[[1, 9, 3], [4, 5, 6]]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 0, 2, 1)
        assert result == [[1, 2, 1], [4, 5, 6]], f"Test 34 failed: got {result}, expected {[[1, 2, 1], [4, 5, 6]]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 1, 2, 99)
        assert result == [[1, 2, 3], [4, 5, 99]], f"Test 35 failed: got {result}, expected {[[1, 2, 3], [4, 5, 99]]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 0, 2, 102)
        assert result == [[1, 2, 102], [4, 5, 6]], f"Test 36 failed: got {result}, expected {[[1, 2, 102], [4, 5, 6]]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = modify_array_element([[1, 2, 3], [4, 5, 6]], 1, 2, 0)
        assert result == [[1, 2, 3], [4, 5, 0]], f"Test 37 failed: got {result}, expected {[[1, 2, 3], [4, 5, 0]]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = modify_array_element([[0, 0, 0]], 0, 2, 16)
        assert result == [[0, 0, 16]], f"Test 38 failed: got {result}, expected {[[0, 0, 16]]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = modify_array_element([[0, 0, 0]], 0, 2, 60)
        assert result == [[0, 0, 60]], f"Test 39 failed: got {result}, expected {[[0, 0, 60]]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = modify_array_element([[0, 0, 0]], 0, 2, 123)
        assert result == [[0, 0, 123]], f"Test 40 failed: got {result}, expected {[[0, 0, 123]]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = modify_array_element([[3, 4, 5], [6, 7, 8], [9, 10, 11]], 2, 1, 198)
        assert result == [[3, 4, 5], [6, 7, 8], [9, 198, 11]], f"Test 41 failed: got {result}, expected {[[3, 4, 5], [6, 7, 8], [9, 198, 11]]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = modify_array_element([[3, 4, 5], [6, 7, 8], [9, 10, 11]], 1, 1, 0)
        assert result == [[3, 4, 5], [6, 0, 8], [9, 10, 11]], f"Test 42 failed: got {result}, expected {[[3, 4, 5], [6, 0, 8], [9, 10, 11]]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = modify_array_element([[3, 4, 5], [6, 7, 8], [9, 10, 11]], 2, 1, 0)
        assert result == [[3, 4, 5], [6, 7, 8], [9, 0, 11]], f"Test 43 failed: got {result}, expected {[[3, 4, 5], [6, 7, 8], [9, 0, 11]]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = modify_array_element([[], [1, 2, 3]], 1, 2, 0)
        assert result == [[], [1, 2, 0]], f"Test 44 failed: got {result}, expected {[[], [1, 2, 0]]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = modify_array_element([[], [1, 2, 3]], 1, 2, 10)
        assert result == [[], [1, 2, 10]], f"Test 45 failed: got {result}, expected {[[], [1, 2, 10]]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = modify_array_element([[10, 20], [30], [40, 50, 60, 70]], 2, 3, 123)
        assert result == [[10, 20], [30], [40, 50, 60, 123]], f"Test 46 failed: got {result}, expected {[[10, 20], [30], [40, 50, 60, 123]]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = modify_array_element([[10, 20], [30], [40, 50, 60, 70]], 2, 3, 700)
        assert result == [[10, 20], [30], [40, 50, 60, 700]], f"Test 47 failed: got {result}, expected {[[10, 20], [30], [40, 50, 60, 700]]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = modify_array_element([[1, 1, 1], [2, 2], [3]], 0, 1, 50)
        assert result == [[1, 50, 1], [2, 2], [3]], f"Test 48 failed: got {result}, expected {[[1, 50, 1], [2, 2], [3]]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = modify_array_element([[1, 1, 1], [2, 2], [3]], 0, 1, 4)
        assert result == [[1, 4, 1], [2, 2], [3]], f"Test 49 failed: got {result}, expected {[[1, 4, 1], [2, 2], [3]]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = modify_array_element([[1, 1, 1], [2, 2], [3]], 0, 1, 42)
        assert result == [[1, 42, 1], [2, 2], [3]], f"Test 50 failed: got {result}, expected {[[1, 42, 1], [2, 2], [3]]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = modify_array_element([[1, 1, 1], [2, 2], [3]], 0, 1, 3)
        assert result == [[1, 3, 1], [2, 2], [3]], f"Test 51 failed: got {result}, expected {[[1, 3, 1], [2, 2], [3]]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = modify_array_element([[100, 200, 300, 400], [500, 600]], 0, 3, 12)
        assert result == [[100, 200, 300, 12], [500, 600]], f"Test 52 failed: got {result}, expected {[[100, 200, 300, 12], [500, 600]]}"
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
