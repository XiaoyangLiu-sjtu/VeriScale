# Coverage Report

Total executable lines: 4
Covered lines: 4
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def partitionEvensOdds(nums):
2: ✓     evens = [x for x in nums if x % 2 == 0]
3: ✓     odds = [x for x in nums if x % 2 == 1]
4: ✓     return (evens, odds)
```

## Complete Test File

```python
def partitionEvensOdds(nums):
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 == 1]
    return (evens, odds)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = partitionEvensOdds([1, 2, 3, 4, 5, 6])
        assert result == ([2, 4, 6], [1, 3, 5]), f"Test 1 failed: got {result}, expected {([2, 4, 6], [1, 3, 5])}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = partitionEvensOdds([0, 7, 8, 9, 10])
        assert result == ([0, 8, 10], [7, 9]), f"Test 2 failed: got {result}, expected {([0, 8, 10], [7, 9])}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = partitionEvensOdds([])
        assert result == ([], []), f"Test 3 failed: got {result}, expected {([], [])}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = partitionEvensOdds([2, 4, 6, 8])
        assert result == ([2, 4, 6, 8], []), f"Test 4 failed: got {result}, expected {([2, 4, 6, 8], [])}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = partitionEvensOdds([1, 3, 5, 7])
        assert result == ([], [1, 3, 5, 7]), f"Test 5 failed: got {result}, expected {([], [1, 3, 5, 7])}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = partitionEvensOdds([0])
        assert result == ([0], []), f"Test 6 failed: got {result}, expected {([0], [])}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = partitionEvensOdds([1])
        assert result == ([], [1]), f"Test 7 failed: got {result}, expected {([], [1])}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = partitionEvensOdds([2])
        assert result == ([2], []), f"Test 8 failed: got {result}, expected {([2], [])}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = partitionEvensOdds([999999937])
        assert result == ([], [999999937]), f"Test 9 failed: got {result}, expected {([], [999999937])}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = partitionEvensOdds([0, 1])
        assert result == ([0], [1]), f"Test 10 failed: got {result}, expected {([0], [1])}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = partitionEvensOdds([1, 0])
        assert result == ([0], [1]), f"Test 11 failed: got {result}, expected {([0], [1])}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = partitionEvensOdds([2, 4, 6, 8, 10])
        assert result == ([2, 4, 6, 8, 10], []), f"Test 12 failed: got {result}, expected {([2, 4, 6, 8, 10], [])}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 9])
        assert result == ([], [1, 3, 5, 7, 9]), f"Test 13 failed: got {result}, expected {([], [1, 3, 5, 7, 9])}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = partitionEvensOdds([0, 2, 4, 1, 3, 5])
        assert result == ([0, 2, 4], [1, 3, 5]), f"Test 14 failed: got {result}, expected {([0, 2, 4], [1, 3, 5])}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = partitionEvensOdds([6, 5, 4, 3, 2, 1, 0])
        assert result == ([6, 4, 2, 0], [5, 3, 1]), f"Test 15 failed: got {result}, expected {([6, 4, 2, 0], [5, 3, 1])}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = partitionEvensOdds([11, 14, 17, 20, 23, 26])
        assert result == ([14, 20, 26], [11, 17, 23]), f"Test 16 failed: got {result}, expected {([14, 20, 26], [11, 17, 23])}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = partitionEvensOdds([42, 17, 8, 3, 0, 19])
        assert result == ([42, 8, 0], [17, 3, 19]), f"Test 17 failed: got {result}, expected {([42, 8, 0], [17, 3, 19])}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = partitionEvensOdds([100, 101, 102, 103, 104, 105])
        assert result == ([100, 102, 104], [101, 103, 105]), f"Test 18 failed: got {result}, expected {([100, 102, 104], [101, 103, 105])}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = partitionEvensOdds([15, 14, 13, 12, 11, 10])
        assert result == ([14, 12, 10], [15, 13, 11]), f"Test 19 failed: got {result}, expected {([14, 12, 10], [15, 13, 11])}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = partitionEvensOdds([2, 1, 4, 3, 6, 5, 8, 7])
        assert result == ([2, 4, 6, 8], [1, 3, 5, 7]), f"Test 20 failed: got {result}, expected {([2, 4, 6, 8], [1, 3, 5, 7])}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = partitionEvensOdds([31, 0, 29, 2, 27, 4, 25, 6])
        assert result == ([0, 2, 4, 6], [31, 29, 27, 25]), f"Test 21 failed: got {result}, expected {([0, 2, 4, 6], [31, 29, 27, 25])}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = partitionEvensOdds([1000, 999, 998, 997, 996])
        assert result == ([1000, 998, 996], [999, 997]), f"Test 22 failed: got {result}, expected {([1000, 998, 996], [999, 997])}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = partitionEvensOdds([18446744073709551616, 3, 5, 8])
        assert result == ([18446744073709551616, 8], [3, 5]), f"Test 23 failed: got {result}, expected {([18446744073709551616, 8], [3, 5])}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = partitionEvensOdds([999999999999999999, 1000000000000000000])
        assert result == ([1000000000000000000], [999999999999999999]), f"Test 24 failed: got {result}, expected {([1000000000000000000], [999999999999999999])}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = partitionEvensOdds([13, 21, 34, 55, 89, 144])
        assert result == ([34, 144], [13, 21, 55, 89]), f"Test 25 failed: got {result}, expected {([34, 144], [13, 21, 55, 89])}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = partitionEvensOdds([97, 98, 99, 100, 101])
        assert result == ([98, 100], [97, 99, 101]), f"Test 26 failed: got {result}, expected {([98, 100], [97, 99, 101])}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = partitionEvensOdds([50, 40, 30, 20, 10, 1, 3, 5])
        assert result == ([50, 40, 30, 20, 10], [1, 3, 5]), f"Test 27 failed: got {result}, expected {([50, 40, 30, 20, 10], [1, 3, 5])}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = partitionEvensOdds([7, 14, 28, 56, 112, 224])
        assert result == ([14, 28, 56, 112, 224], [7]), f"Test 28 failed: got {result}, expected {([14, 28, 56, 112, 224], [7])}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = partitionEvensOdds([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        assert result == ([8, 6, 4, 2, 0], [9, 7, 5, 3, 1]), f"Test 29 failed: got {result}, expected {([8, 6, 4, 2, 0], [9, 7, 5, 3, 1])}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = partitionEvensOdds([0, 100, 200, 300, 401, 501, 601])
        assert result == ([0, 100, 200, 300], [401, 501, 601]), f"Test 30 failed: got {result}, expected {([0, 100, 200, 300], [401, 501, 601])}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = partitionEvensOdds([16, 1, 18, 3, 20, 5, 22, 7, 24, 9])
        assert result == ([16, 18, 20, 22, 24], [1, 3, 5, 7, 9]), f"Test 31 failed: got {result}, expected {([16, 18, 20, 22, 24], [1, 3, 5, 7, 9])}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = partitionEvensOdds([123456789, 987654321, 222222222, 333333333])
        assert result == ([222222222], [123456789, 987654321, 333333333]), f"Test 32 failed: got {result}, expected {([222222222], [123456789, 987654321, 333333333])}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = partitionEvensOdds([4294967295, 4294967296, 4294967297])
        assert result == ([4294967296], [4294967295, 4294967297]), f"Test 33 failed: got {result}, expected {([4294967296], [4294967295, 4294967297])}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = partitionEvensOdds([73, 64, 55, 46, 37, 28, 19, 10, 1])
        assert result == ([64, 46, 28, 10], [73, 55, 37, 19, 1]), f"Test 34 failed: got {result}, expected {([64, 46, 28, 10], [73, 55, 37, 19, 1])}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = partitionEvensOdds([1, 1])
        assert result == ([], [1, 1]), f"Test 35 failed: got {result}, expected {([], [1, 1])}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = partitionEvensOdds([0, 0, 2, 4])
        assert result == ([0, 0, 2, 4], []), f"Test 36 failed: got {result}, expected {([0, 0, 2, 4], [])}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = partitionEvensOdds([3, 5, 3, 7])
        assert result == ([], [3, 5, 3, 7]), f"Test 37 failed: got {result}, expected {([], [3, 5, 3, 7])}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = partitionEvensOdds([2, 4, 6, 6, 8])
        assert result == ([2, 4, 6, 6, 8], []), f"Test 38 failed: got {result}, expected {([2, 4, 6, 6, 8], [])}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = partitionEvensOdds([9, 8, 7, 8, 9])
        assert result == ([8, 8], [9, 7, 9]), f"Test 39 failed: got {result}, expected {([8, 8], [9, 7, 9])}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = partitionEvensOdds([10, 11, 12, 13, 10])
        assert result == ([10, 12, 10], [11, 13]), f"Test 40 failed: got {result}, expected {([10, 12, 10], [11, 13])}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = partitionEvensOdds([42, 42, 42])
        assert result == ([42, 42, 42], []), f"Test 41 failed: got {result}, expected {([42, 42, 42], [])}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = partitionEvensOdds([0, 1, 2, 3, 2, 1, 0])
        assert result == ([0, 2, 2, 0], [1, 3, 1]), f"Test 42 failed: got {result}, expected {([0, 2, 2, 0], [1, 3, 1])}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = partitionEvensOdds([1, 3, 4, 5, 6])
        assert result == ([4, 6], [1, 3, 5]), f"Test 43 failed: got {result}, expected {([4, 6], [1, 3, 5])}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = partitionEvensOdds([29, 2, 3, 4, 5, 7])
        assert result == ([2, 4], [29, 3, 5, 7]), f"Test 44 failed: got {result}, expected {([2, 4], [29, 3, 5, 7])}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = partitionEvensOdds([1, 0, 4, 5, 6, 0, 0, 97])
        assert result == ([0, 4, 6, 0, 0], [1, 5, 97]), f"Test 45 failed: got {result}, expected {([0, 4, 6, 0, 0], [1, 5, 97])}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = partitionEvensOdds([1, 2, 4, 4, 5, 6])
        assert result == ([2, 4, 4, 6], [1, 5]), f"Test 46 failed: got {result}, expected {([2, 4, 4, 6], [1, 5])}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = partitionEvensOdds([5, 5, 4, 3, 2, 1, 0, 0, 0])
        assert result == ([4, 2, 0, 0, 0], [5, 5, 3, 1]), f"Test 47 failed: got {result}, expected {([4, 2, 0, 0, 0], [5, 5, 3, 1])}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = partitionEvensOdds([1, 2, 3, 5, 6])
        assert result == ([2, 6], [1, 3, 5]), f"Test 48 failed: got {result}, expected {([2, 6], [1, 3, 5])}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = partitionEvensOdds([2, 4, 5, 6, 0])
        assert result == ([2, 4, 6, 0], [5]), f"Test 49 failed: got {result}, expected {([2, 4, 6, 0], [5])}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = partitionEvensOdds([6, 5, 4, 3, 2])
        assert result == ([6, 4, 2], [5, 3]), f"Test 50 failed: got {result}, expected {([6, 4, 2], [5, 3])}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = partitionEvensOdds([103, 5, 112, 3, 2])
        assert result == ([112, 2], [103, 5, 3]), f"Test 51 failed: got {result}, expected {([112, 2], [103, 5, 3])}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = partitionEvensOdds([1, 2, 3, 4, 5, 6, 0, 0])
        assert result == ([2, 4, 6, 0, 0], [1, 3, 5]), f"Test 52 failed: got {result}, expected {([2, 4, 6, 0, 0], [1, 3, 5])}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = partitionEvensOdds([601, 14, 6, 5, 4, 3, 2, 1])
        assert result == ([14, 6, 4, 2], [601, 5, 3, 1]), f"Test 53 failed: got {result}, expected {([14, 6, 4, 2], [601, 5, 3, 1])}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = partitionEvensOdds([1, 2, 3, 4, 10, 6, 0, 0, 98])
        assert result == ([2, 4, 10, 6, 0, 0, 98], [1, 3]), f"Test 54 failed: got {result}, expected {([2, 4, 10, 6, 0, 0, 98], [1, 3])}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = partitionEvensOdds([1, 2, 3, 4, 5, 6, 0])
        assert result == ([2, 4, 6, 0], [1, 3, 5]), f"Test 55 failed: got {result}, expected {([2, 4, 6, 0], [1, 3, 5])}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = partitionEvensOdds([1, 2, 3, 4, 5, 222222222])
        assert result == ([2, 4, 222222222], [1, 3, 5]), f"Test 56 failed: got {result}, expected {([2, 4, 222222222], [1, 3, 5])}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = partitionEvensOdds([0, 6, 5, 4, 3, 2, 1])
        assert result == ([0, 6, 4, 2], [5, 3, 1]), f"Test 57 failed: got {result}, expected {([0, 6, 4, 2], [5, 3, 1])}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = partitionEvensOdds([0, 7, 9, 10])
        assert result == ([0, 10], [7, 9]), f"Test 58 failed: got {result}, expected {([0, 10], [7, 9])}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = partitionEvensOdds([0, 7, 8, 9, 10, 998])
        assert result == ([0, 8, 10, 998], [7, 9]), f"Test 59 failed: got {result}, expected {([0, 8, 10, 998], [7, 9])}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = partitionEvensOdds([10, 9, 8, 7])
        assert result == ([10, 8], [9, 7]), f"Test 60 failed: got {result}, expected {([10, 8], [9, 7])}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = partitionEvensOdds([997, 55, 8, 7, 0, 0])
        assert result == ([8, 0, 0], [997, 55, 7]), f"Test 61 failed: got {result}, expected {([8, 0, 0], [997, 55, 7])}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = partitionEvensOdds([7, 8, 9, 0, 0])
        assert result == ([8, 0, 0], [7, 9]), f"Test 62 failed: got {result}, expected {([8, 0, 0], [7, 9])}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = partitionEvensOdds([0, 7, 8, 9, 10, 100, 12])
        assert result == ([0, 8, 10, 100, 12], [7, 9]), f"Test 63 failed: got {result}, expected {([0, 8, 10, 100, 12], [7, 9])}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = partitionEvensOdds([0, 7, 8, 10])
        assert result == ([0, 8, 10], [7]), f"Test 64 failed: got {result}, expected {([0, 8, 10], [7])}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = partitionEvensOdds([55, 7, 8, 9, 10, 401, 0, 601])
        assert result == ([8, 10, 0], [55, 7, 9, 401, 601]), f"Test 65 failed: got {result}, expected {([8, 10, 0], [55, 7, 9, 401, 601])}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = partitionEvensOdds([10, 9, 8, 5, 0])
        assert result == ([10, 8, 0], [9, 5]), f"Test 66 failed: got {result}, expected {([10, 8, 0], [9, 5])}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = partitionEvensOdds([0, 102, 8, 9, 10, 123456789, 200])
        assert result == ([0, 102, 8, 10, 200], [9, 123456789]), f"Test 67 failed: got {result}, expected {([0, 102, 8, 10, 200], [9, 123456789])}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = partitionEvensOdds([0, 7, 8, 9, 10, 0, 401, 7])
        assert result == ([0, 8, 10, 0], [7, 9, 401, 7]), f"Test 68 failed: got {result}, expected {([0, 8, 10, 0], [7, 9, 401, 7])}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = partitionEvensOdds([7, 8, 9, 10, 23, 0, 0])
        assert result == ([8, 10, 0, 0], [7, 9, 23]), f"Test 69 failed: got {result}, expected {([8, 10, 0, 0], [7, 9, 23])}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = partitionEvensOdds([10, 9, 8, 7, 0])
        assert result == ([10, 8, 0], [9, 7]), f"Test 70 failed: got {result}, expected {([10, 8, 0], [9, 7])}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = partitionEvensOdds([0, 7, 8, 9, 10, 0])
        assert result == ([0, 8, 10, 0], [7, 9]), f"Test 71 failed: got {result}, expected {([0, 8, 10, 0], [7, 9])}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = partitionEvensOdds([0, 9, 8, 7, 0, 4294967296, 42])
        assert result == ([0, 8, 0, 4294967296, 42], [9, 7]), f"Test 72 failed: got {result}, expected {([0, 8, 0, 4294967296, 42], [9, 7])}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = partitionEvensOdds([56, 222222222])
        assert result == ([56, 222222222], []), f"Test 73 failed: got {result}, expected {([56, 222222222], [])}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = partitionEvensOdds([0, 0, 0])
        assert result == ([0, 0, 0], []), f"Test 74 failed: got {result}, expected {([0, 0, 0], [])}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = partitionEvensOdds([26, 4294967296])
        assert result == ([26, 4294967296], []), f"Test 75 failed: got {result}, expected {([26, 4294967296], [])}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = partitionEvensOdds([0, 50, 0])
        assert result == ([0, 50, 0], []), f"Test 76 failed: got {result}, expected {([0, 50, 0], [])}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = partitionEvensOdds([31])
        assert result == ([], [31]), f"Test 77 failed: got {result}, expected {([], [31])}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = partitionEvensOdds([20, 50, 34])
        assert result == ([20, 50, 34], []), f"Test 78 failed: got {result}, expected {([20, 50, 34], [])}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = partitionEvensOdds([0, 0])
        assert result == ([0, 0], []), f"Test 79 failed: got {result}, expected {([0, 0], [])}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = partitionEvensOdds([0, 4294967295])
        assert result == ([0], [4294967295]), f"Test 80 failed: got {result}, expected {([0], [4294967295])}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = partitionEvensOdds([8])
        assert result == ([8], []), f"Test 81 failed: got {result}, expected {([8], [])}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = partitionEvensOdds([2, 4, 8, 0])
        assert result == ([2, 4, 8, 0], []), f"Test 82 failed: got {result}, expected {([2, 4, 8, 0], [])}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = partitionEvensOdds([2, 4, 6, 8, 0, 10, 0])
        assert result == ([2, 4, 6, 8, 0, 10, 0], []), f"Test 83 failed: got {result}, expected {([2, 4, 6, 8, 0, 10, 0], [])}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = partitionEvensOdds([0, 100, 25, 6, 8])
        assert result == ([0, 100, 6, 8], [25]), f"Test 84 failed: got {result}, expected {([0, 100, 6, 8], [25])}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = partitionEvensOdds([2, 4, 6, 1000, 15, 99])
        assert result == ([2, 4, 6, 1000], [15, 99]), f"Test 85 failed: got {result}, expected {([2, 4, 6, 1000], [15, 99])}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = partitionEvensOdds([8, 4, 2, 0, 100, 0])
        assert result == ([8, 4, 2, 0, 100, 0], []), f"Test 86 failed: got {result}, expected {([8, 4, 2, 0, 100, 0], [])}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = partitionEvensOdds([4, 19])
        assert result == ([4], [19]), f"Test 87 failed: got {result}, expected {([4], [19])}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = partitionEvensOdds([27, 8, 6, 4, 2])
        assert result == ([8, 6, 4, 2], [27]), f"Test 88 failed: got {result}, expected {([8, 6, 4, 2], [27])}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = partitionEvensOdds([0, 8, 6, 4, 2, 89, 0])
        assert result == ([0, 8, 6, 4, 2, 0], [89]), f"Test 89 failed: got {result}, expected {([0, 8, 6, 4, 2, 0], [89])}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = partitionEvensOdds([8, 6, 4, 2])
        assert result == ([8, 6, 4, 2], []), f"Test 90 failed: got {result}, expected {([8, 6, 4, 2], [])}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = partitionEvensOdds([2, 4, 6])
        assert result == ([2, 4, 6], []), f"Test 91 failed: got {result}, expected {([2, 4, 6], [])}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = partitionEvensOdds([4, 0, 8])
        assert result == ([4, 0, 8], []), f"Test 92 failed: got {result}, expected {([4, 0, 8], [])}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = partitionEvensOdds([8, 6, 4, 99])
        assert result == ([8, 6, 4], [99]), f"Test 93 failed: got {result}, expected {([8, 6, 4], [99])}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = partitionEvensOdds([2, 4, 6, 98])
        assert result == ([2, 4, 6, 98], []), f"Test 94 failed: got {result}, expected {([2, 4, 6, 98], [])}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = partitionEvensOdds([2, 4, 6, 997])
        assert result == ([2, 4, 6], [997]), f"Test 95 failed: got {result}, expected {([2, 4, 6], [997])}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 8])
        assert result == ([8], [1, 3, 5, 7]), f"Test 96 failed: got {result}, expected {([8], [1, 3, 5, 7])}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 25])
        assert result == ([], [1, 3, 5, 7, 25]), f"Test 97 failed: got {result}, expected {([], [1, 3, 5, 7, 25])}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 18446744073709551616])
        assert result == ([18446744073709551616], [1, 3, 5, 7]), f"Test 98 failed: got {result}, expected {([18446744073709551616], [1, 3, 5, 7])}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = partitionEvensOdds([0, 5, 3, 1, 300])
        assert result == ([0, 300], [5, 3, 1]), f"Test 99 failed: got {result}, expected {([0, 300], [5, 3, 1])}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = partitionEvensOdds([1, 3, 5])
        assert result == ([], [1, 3, 5]), f"Test 100 failed: got {result}, expected {([], [1, 3, 5])}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = partitionEvensOdds([42, 5, 7])
        assert result == ([42], [5, 7]), f"Test 101 failed: got {result}, expected {([42], [5, 7])}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = partitionEvensOdds([0, 0, 18, 999999937, 5, 3, 1])
        assert result == ([0, 0, 18], [999999937, 5, 3, 1]), f"Test 102 failed: got {result}, expected {([0, 0, 18], [999999937, 5, 3, 1])}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = partitionEvensOdds([1, 3, 102, 0])
        assert result == ([102, 0], [1, 3]), f"Test 103 failed: got {result}, expected {([102, 0], [1, 3])}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 333333333, 0])
        assert result == ([0], [1, 3, 5, 7, 333333333]), f"Test 104 failed: got {result}, expected {([0], [1, 3, 5, 7, 333333333])}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = partitionEvensOdds([123456789, 5, 3, 1])
        assert result == ([], [123456789, 5, 3, 1]), f"Test 105 failed: got {result}, expected {([], [123456789, 5, 3, 1])}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = partitionEvensOdds([0, 7, 5, 3, 1])
        assert result == ([0], [7, 5, 3, 1]), f"Test 106 failed: got {result}, expected {([0], [7, 5, 3, 1])}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = partitionEvensOdds([6, 3, 27])
        assert result == ([6], [3, 27]), f"Test 107 failed: got {result}, expected {([6], [3, 27])}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = partitionEvensOdds([5, 7, 0])
        assert result == ([0], [5, 7]), f"Test 108 failed: got {result}, expected {([0], [5, 7])}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 102])
        assert result == ([102], [1, 3, 5, 7]), f"Test 109 failed: got {result}, expected {([102], [1, 3, 5, 7])}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = partitionEvensOdds([89, 0, 19, 0])
        assert result == ([0, 0], [89, 19]), f"Test 110 failed: got {result}, expected {([0, 0], [89, 19])}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = partitionEvensOdds([0, 27])
        assert result == ([0], [27]), f"Test 111 failed: got {result}, expected {([0], [27])}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = partitionEvensOdds([0, 30, 0, 0])
        assert result == ([0, 30, 0, 0], []), f"Test 112 failed: got {result}, expected {([0, 30, 0, 0], [])}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = partitionEvensOdds([34, 0, 300])
        assert result == ([34, 0, 300], []), f"Test 113 failed: got {result}, expected {([34, 0, 300], [])}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = partitionEvensOdds([501, 0, 100])
        assert result == ([0, 100], [501]), f"Test 114 failed: got {result}, expected {([0, 100], [501])}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = partitionEvensOdds([0, 103, 0])
        assert result == ([0, 0], [103]), f"Test 115 failed: got {result}, expected {([0, 0], [103])}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = partitionEvensOdds([98, 1])
        assert result == ([98], [1]), f"Test 116 failed: got {result}, expected {([98], [1])}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = partitionEvensOdds([3])
        assert result == ([], [3]), f"Test 117 failed: got {result}, expected {([], [3])}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = partitionEvensOdds([0, 0, 1])
        assert result == ([0, 0], [1]), f"Test 118 failed: got {result}, expected {([0, 0], [1])}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = partitionEvensOdds([1, 501])
        assert result == ([], [1, 501]), f"Test 119 failed: got {result}, expected {([], [1, 501])}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = partitionEvensOdds([1, 98])
        assert result == ([98], [1]), f"Test 120 failed: got {result}, expected {([98], [1])}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = partitionEvensOdds([0, 0, 37])
        assert result == ([0, 0], [37]), f"Test 121 failed: got {result}, expected {([0, 0], [37])}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = partitionEvensOdds([1, 42])
        assert result == ([42], [1]), f"Test 122 failed: got {result}, expected {([42], [1])}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = partitionEvensOdds([1, 31, 0, 21])
        assert result == ([0], [1, 31, 21]), f"Test 123 failed: got {result}, expected {([0], [1, 31, 21])}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = partitionEvensOdds([1, 0, 99])
        assert result == ([0], [1, 99]), f"Test 124 failed: got {result}, expected {([0], [1, 99])}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = partitionEvensOdds([0, 2, 0])
        assert result == ([0, 2, 0], []), f"Test 125 failed: got {result}, expected {([0, 2, 0], [])}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = partitionEvensOdds([2, 0])
        assert result == ([2, 0], []), f"Test 126 failed: got {result}, expected {([2, 0], [])}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = partitionEvensOdds([0, 0, 0, 0])
        assert result == ([0, 0, 0, 0], []), f"Test 127 failed: got {result}, expected {([0, 0, 0, 0], [])}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = partitionEvensOdds([2, 64, 0, 0])
        assert result == ([2, 64, 0, 0], []), f"Test 128 failed: got {result}, expected {([2, 64, 0, 0], [])}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = partitionEvensOdds([2, 28, 0])
        assert result == ([2, 28, 0], []), f"Test 129 failed: got {result}, expected {([2, 28, 0], [])}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = partitionEvensOdds([0, 2])
        assert result == ([0, 2], []), f"Test 130 failed: got {result}, expected {([0, 2], [])}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = partitionEvensOdds([2, 0, 0])
        assert result == ([2, 0, 0], []), f"Test 131 failed: got {result}, expected {([2, 0, 0], [])}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = partitionEvensOdds([2, 2])
        assert result == ([2, 2], []), f"Test 132 failed: got {result}, expected {([2, 2], [])}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = partitionEvensOdds([999999937, 18446744073709551616])
        assert result == ([18446744073709551616], [999999937]), f"Test 133 failed: got {result}, expected {([18446744073709551616], [999999937])}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = partitionEvensOdds([0, 0, 18446744073709551616, 14, 1])
        assert result == ([0, 0, 18446744073709551616, 14], [1]), f"Test 134 failed: got {result}, expected {([0, 0, 18446744073709551616, 14], [1])}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = partitionEvensOdds([18446744073709551616, 0, 0])
        assert result == ([18446744073709551616, 0, 0], []), f"Test 135 failed: got {result}, expected {([18446744073709551616, 0, 0], [])}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = partitionEvensOdds([0, 999999937, 0, 0])
        assert result == ([0, 0, 0], [999999937]), f"Test 136 failed: got {result}, expected {([0, 0, 0], [999999937])}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = partitionEvensOdds([18446744073709551616])
        assert result == ([18446744073709551616], []), f"Test 137 failed: got {result}, expected {([18446744073709551616], [])}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = partitionEvensOdds([999999938])
        assert result == ([999999938], []), f"Test 138 failed: got {result}, expected {([999999938], [])}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = partitionEvensOdds([1999999874])
        assert result == ([1999999874], []), f"Test 139 failed: got {result}, expected {([1999999874], [])}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = partitionEvensOdds([999999937, 0])
        assert result == ([0], [999999937]), f"Test 140 failed: got {result}, expected {([0], [999999937])}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = partitionEvensOdds([2000000000000000000])
        assert result == ([2000000000000000000], []), f"Test 141 failed: got {result}, expected {([2000000000000000000], [])}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = partitionEvensOdds([2, 997])
        assert result == ([2], [997]), f"Test 142 failed: got {result}, expected {([2], [997])}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = partitionEvensOdds([999999937, 0, 0])
        assert result == ([0, 0], [999999937]), f"Test 143 failed: got {result}, expected {([0, 0], [999999937])}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = partitionEvensOdds([0, 6, 0])
        assert result == ([0, 6, 0], []), f"Test 144 failed: got {result}, expected {([0, 6, 0], [])}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = partitionEvensOdds([0, 99, 0])
        assert result == ([0, 0], [99]), f"Test 145 failed: got {result}, expected {([0, 0], [99])}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = partitionEvensOdds([1000])
        assert result == ([1000], []), f"Test 146 failed: got {result}, expected {([1000], [])}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = partitionEvensOdds([0, 9, 0])
        assert result == ([0, 0], [9]), f"Test 147 failed: got {result}, expected {([0, 0], [9])}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = partitionEvensOdds([999999999999999999])
        assert result == ([], [999999999999999999]), f"Test 148 failed: got {result}, expected {([], [999999999999999999])}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = partitionEvensOdds([401, 0])
        assert result == ([0], [401]), f"Test 149 failed: got {result}, expected {([0], [401])}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = partitionEvensOdds([1, 2, 28, 9, 0])
        assert result == ([2, 28, 0], [1, 9]), f"Test 150 failed: got {result}, expected {([2, 28, 0], [1, 9])}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = partitionEvensOdds([0, 1, 23, 112])
        assert result == ([0, 112], [1, 23]), f"Test 151 failed: got {result}, expected {([0, 112], [1, 23])}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = partitionEvensOdds([25, 0])
        assert result == ([0], [25]), f"Test 152 failed: got {result}, expected {([0], [25])}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = partitionEvensOdds([1, 144, 100])
        assert result == ([144, 100], [1]), f"Test 153 failed: got {result}, expected {([144, 100], [1])}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = partitionEvensOdds([1, 40])
        assert result == ([40], [1]), f"Test 154 failed: got {result}, expected {([40], [1])}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = partitionEvensOdds([19, 15, 0])
        assert result == ([0], [19, 15]), f"Test 155 failed: got {result}, expected {([0], [19, 15])}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = partitionEvensOdds([2, 0, 401, 42])
        assert result == ([2, 0, 42], [401]), f"Test 156 failed: got {result}, expected {([2, 0, 42], [401])}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = partitionEvensOdds([0, 13, 5, 0])
        assert result == ([0, 0], [13, 5]), f"Test 157 failed: got {result}, expected {([0, 0], [13, 5])}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = partitionEvensOdds([17, 1, 0])
        assert result == ([0], [17, 1]), f"Test 158 failed: got {result}, expected {([0], [17, 1])}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = partitionEvensOdds([1, 0, 5])
        assert result == ([0], [1, 5]), f"Test 159 failed: got {result}, expected {([0], [1, 5])}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = partitionEvensOdds([1, 999999999999999999, 0])
        assert result == ([0], [1, 999999999999999999]), f"Test 160 failed: got {result}, expected {([0], [1, 999999999999999999])}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = partitionEvensOdds([112, 0, 144])
        assert result == ([112, 0, 144], []), f"Test 161 failed: got {result}, expected {([112, 0, 144], [])}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = partitionEvensOdds([1, 0, 0])
        assert result == ([0, 0], [1]), f"Test 162 failed: got {result}, expected {([0, 0], [1])}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = partitionEvensOdds([0, 8])
        assert result == ([0, 8], []), f"Test 163 failed: got {result}, expected {([0, 8], [])}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = partitionEvensOdds([0, 1, 0])
        assert result == ([0, 0], [1]), f"Test 164 failed: got {result}, expected {([0, 0], [1])}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = partitionEvensOdds([1, 0, 300])
        assert result == ([0, 300], [1]), f"Test 165 failed: got {result}, expected {([0, 300], [1])}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = partitionEvensOdds([4294967295, 0, 10, 8, 4, 2])
        assert result == ([0, 10, 8, 4, 2], [4294967295]), f"Test 166 failed: got {result}, expected {([0, 10, 8, 4, 2], [4294967295])}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = partitionEvensOdds([2, 10, 0])
        assert result == ([2, 10, 0], []), f"Test 167 failed: got {result}, expected {([2, 10, 0], [])}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = partitionEvensOdds([2, 4, 6, 8, 10, 30])
        assert result == ([2, 4, 6, 8, 10, 30], []), f"Test 168 failed: got {result}, expected {([2, 4, 6, 8, 10, 30], [])}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = partitionEvensOdds([8, 6, 0, 2, 0])
        assert result == ([8, 6, 0, 2, 0], []), f"Test 169 failed: got {result}, expected {([8, 6, 0, 2, 0], [])}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = partitionEvensOdds([55, 2, 4, 6, 8, 10, 0, 999999938])
        assert result == ([2, 4, 6, 8, 10, 0, 999999938], [55]), f"Test 170 failed: got {result}, expected {([2, 4, 6, 8, 10, 0, 999999938], [55])}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = partitionEvensOdds([2, 4, 999999938, 8])
        assert result == ([2, 4, 999999938, 8], []), f"Test 171 failed: got {result}, expected {([2, 4, 999999938, 8], [])}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = partitionEvensOdds([2, 4, 6, 8, 0, 0])
        assert result == ([2, 4, 6, 8, 0, 0], []), f"Test 172 failed: got {result}, expected {([2, 4, 6, 8, 0, 0], [])}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = partitionEvensOdds([998, 4, 6, 8, 10, 999999999999999999, 0, 998, 0])
        assert result == ([998, 4, 6, 8, 10, 0, 998, 0], [999999999999999999]), f"Test 173 failed: got {result}, expected {([998, 4, 6, 8, 10, 0, 998, 0], [999999999999999999])}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = partitionEvensOdds([2, 4, 6, 8, 10, 0])
        assert result == ([2, 4, 6, 8, 10, 0], []), f"Test 174 failed: got {result}, expected {([2, 4, 6, 8, 10, 0], [])}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = partitionEvensOdds([10, 8, 6, 4, 2])
        assert result == ([10, 8, 6, 4, 2], []), f"Test 175 failed: got {result}, expected {([10, 8, 6, 4, 2], [])}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = partitionEvensOdds([2, 4, 6, 8, 10, 112])
        assert result == ([2, 4, 6, 8, 10, 112], []), f"Test 176 failed: got {result}, expected {([2, 4, 6, 8, 10, 112], [])}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = partitionEvensOdds([4, 8, 10])
        assert result == ([4, 8, 10], []), f"Test 177 failed: got {result}, expected {([4, 8, 10], [])}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = partitionEvensOdds([2, 6, 8, 10, 0])
        assert result == ([2, 6, 8, 10, 0], []), f"Test 178 failed: got {result}, expected {([2, 6, 8, 10, 0], [])}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = partitionEvensOdds([2, 4, 6, 12, 20])
        assert result == ([2, 4, 6, 12, 20], []), f"Test 179 failed: got {result}, expected {([2, 4, 6, 12, 20], [])}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = partitionEvensOdds([0, 20, 10, 8, 6, 4, 2])
        assert result == ([0, 20, 10, 8, 6, 4, 2], []), f"Test 180 failed: got {result}, expected {([0, 20, 10, 8, 6, 4, 2], [])}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = partitionEvensOdds([501, 3, 5, 7, 9, 0])
        assert result == ([0], [501, 3, 5, 7, 9]), f"Test 181 failed: got {result}, expected {([0], [501, 3, 5, 7, 9])}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = partitionEvensOdds([0, 9, 4294967297, 996, 3, 1])
        assert result == ([0, 996], [9, 4294967297, 3, 1]), f"Test 182 failed: got {result}, expected {([0, 996], [9, 4294967297, 3, 1])}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = partitionEvensOdds([1, 3, 5, 14, 9, 0])
        assert result == ([14, 0], [1, 3, 5, 9]), f"Test 183 failed: got {result}, expected {([14, 0], [1, 3, 5, 9])}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = partitionEvensOdds([64, 3, 7, 9, 12, 25, 0])
        assert result == ([64, 12, 0], [3, 7, 9, 25]), f"Test 184 failed: got {result}, expected {([64, 12, 0], [3, 7, 9, 25])}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 999999999999999999, 101, 0])
        assert result == ([0], [1, 3, 5, 7, 999999999999999999, 101]), f"Test 185 failed: got {result}, expected {([0], [1, 3, 5, 7, 999999999999999999, 101])}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = partitionEvensOdds([0, 9, 5, 3, 1])
        assert result == ([0], [9, 5, 3, 1]), f"Test 186 failed: got {result}, expected {([0], [9, 5, 3, 1])}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 9, 0])
        assert result == ([0], [1, 3, 5, 7, 9]), f"Test 187 failed: got {result}, expected {([0], [1, 3, 5, 7, 9])}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = partitionEvensOdds([2, 31, 9, 7, 5, 3, 1])
        assert result == ([2], [31, 9, 7, 5, 3, 1]), f"Test 188 failed: got {result}, expected {([2], [31, 9, 7, 5, 3, 1])}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 9, 26])
        assert result == ([26], [1, 3, 5, 7, 9]), f"Test 189 failed: got {result}, expected {([26], [1, 3, 5, 7, 9])}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = partitionEvensOdds([9, 5, 3, 1, 0])
        assert result == ([0], [9, 5, 3, 1]), f"Test 190 failed: got {result}, expected {([0], [9, 5, 3, 1])}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = partitionEvensOdds([123456789, 46, 37, 9, 7, 5, 3, 1])
        assert result == ([46], [123456789, 37, 9, 7, 5, 3, 1]), f"Test 191 failed: got {result}, expected {([46], [123456789, 37, 9, 7, 5, 3, 1])}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = partitionEvensOdds([9, 7, 5, 3, 42])
        assert result == ([42], [9, 7, 5, 3]), f"Test 192 failed: got {result}, expected {([42], [9, 7, 5, 3])}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = partitionEvensOdds([1, 3, 4, 7, 9])
        assert result == ([4], [1, 3, 7, 9]), f"Test 193 failed: got {result}, expected {([4], [1, 3, 7, 9])}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = partitionEvensOdds([1, 3, 5, 7, 9, 2000000000000000000, 0, 13, 6])
        assert result == ([2000000000000000000, 0, 6], [1, 3, 5, 7, 9, 13]), f"Test 194 failed: got {result}, expected {([2000000000000000000, 0, 6], [1, 3, 5, 7, 9, 13])}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = partitionEvensOdds([0, 6, 5, 3, 1, 4, 2, 0])
        assert result == ([0, 6, 4, 2, 0], [5, 3, 1]), f"Test 195 failed: got {result}, expected {([0, 6, 4, 2, 0], [5, 3, 1])}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = partitionEvensOdds([0, 2, 4, 1, 3, 39, 104])
        assert result == ([0, 2, 4, 104], [1, 3, 39]), f"Test 196 failed: got {result}, expected {([0, 2, 4, 104], [1, 3, 39])}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = partitionEvensOdds([5, 3, 1, 4, 2, 0, 40])
        assert result == ([4, 2, 0, 40], [5, 3, 1]), f"Test 197 failed: got {result}, expected {([4, 2, 0, 40], [5, 3, 1])}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = partitionEvensOdds([0, 2, 4, 1, 5])
        assert result == ([0, 2, 4], [1, 5]), f"Test 198 failed: got {result}, expected {([0, 2, 4], [1, 5])}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = partitionEvensOdds([0, 3, 5, 0, 300])
        assert result == ([0, 0, 300], [3, 5]), f"Test 199 failed: got {result}, expected {([0, 0, 300], [3, 5])}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = partitionEvensOdds([999999999999999999, 1, 5, 1, 4, 2, 0])
        assert result == ([4, 2, 0], [999999999999999999, 1, 5, 1]), f"Test 200 failed: got {result}, expected {([4, 2, 0], [999999999999999999, 1, 5, 1])}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = partitionEvensOdds([5, 17, 0])
        assert result == ([0], [5, 17]), f"Test 201 failed: got {result}, expected {([0], [5, 17])}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = partitionEvensOdds([7, 3, 1, 4, 2, 999999999999999999, 101])
        assert result == ([4, 2], [7, 3, 1, 999999999999999999, 101]), f"Test 202 failed: got {result}, expected {([4, 2], [7, 3, 1, 999999999999999999, 101])}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = partitionEvensOdds([224, 5, 3, 1, 4, 2, 0])
        assert result == ([224, 4, 2, 0], [5, 3, 1]), f"Test 203 failed: got {result}, expected {([224, 4, 2, 0], [5, 3, 1])}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = partitionEvensOdds([5, 3, 1, 4, 2, 0, 0, 1000, 0, 0])
        assert result == ([4, 2, 0, 0, 1000, 0, 0], [5, 3, 1]), f"Test 204 failed: got {result}, expected {([4, 2, 0, 0, 1000, 0, 0], [5, 3, 1])}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = partitionEvensOdds([0, 2, 4, 1, 3, 5, 1, 55])
        assert result == ([0, 2, 4], [1, 3, 5, 1, 55]), f"Test 205 failed: got {result}, expected {([0, 2, 4], [1, 3, 5, 1, 55])}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = partitionEvensOdds([998, 18446744073709551616, 1, 4, 2, 0])
        assert result == ([998, 18446744073709551616, 4, 2, 0], [1]), f"Test 206 failed: got {result}, expected {([998, 18446744073709551616, 4, 2, 0], [1])}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = partitionEvensOdds([2, 4, 1, 3, 5])
        assert result == ([2, 4], [1, 3, 5]), f"Test 207 failed: got {result}, expected {([2, 4], [1, 3, 5])}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = partitionEvensOdds([5, 3, 7, 4, 2, 0])
        assert result == ([4, 2, 0], [5, 3, 7]), f"Test 208 failed: got {result}, expected {([4, 2, 0], [5, 3, 7])}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = partitionEvensOdds([5, 3, 1, 4, 2, 0])
        assert result == ([4, 2, 0], [5, 3, 1]), f"Test 209 failed: got {result}, expected {([4, 2, 0], [5, 3, 1])}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = partitionEvensOdds([0, 2, 3, 4, 5, 6, 0, 0])
        assert result == ([0, 2, 4, 6, 0, 0], [3, 5]), f"Test 210 failed: got {result}, expected {([0, 2, 4, 6, 0, 0], [3, 5])}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = partitionEvensOdds([6, 5, 4, 3, 2, 1, 0, 0, 31])
        assert result == ([6, 4, 2, 0, 0], [5, 3, 1, 31]), f"Test 211 failed: got {result}, expected {([6, 4, 2, 0, 0], [5, 3, 1, 31])}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = partitionEvensOdds([5, 4, 4, 3, 2, 1, 0, 37, 5])
        assert result == ([4, 4, 2, 0], [5, 3, 1, 37, 5]), f"Test 212 failed: got {result}, expected {([4, 4, 2, 0], [5, 3, 1, 37, 5])}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = partitionEvensOdds([6, 5, 997, 3, 2, 1, 0, 2000000000000000000, 0, 42])
        assert result == ([6, 2, 0, 2000000000000000000, 0, 42], [5, 997, 3, 1]), f"Test 213 failed: got {result}, expected {([6, 2, 0, 2000000000000000000, 0, 42], [5, 997, 3, 1])}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = partitionEvensOdds([6, 5, 4, 3, 3, 1, 0, 42, 401])
        assert result == ([6, 4, 0, 42], [5, 3, 3, 1, 401]), f"Test 214 failed: got {result}, expected {([6, 4, 0, 42], [5, 3, 3, 1, 401])}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = partitionEvensOdds([0, 6, 5, 4, 3, 2, 1, 0, 42])
        assert result == ([0, 6, 4, 2, 0, 42], [5, 3, 1]), f"Test 215 failed: got {result}, expected {([0, 6, 4, 2, 0, 42], [5, 3, 1])}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = partitionEvensOdds([0, 1, 3, 5, 6])
        assert result == ([0, 6], [1, 3, 5]), f"Test 216 failed: got {result}, expected {([0, 6], [1, 3, 5])}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = partitionEvensOdds([24, 6, 5, 4, 3, 1, 0, 0])
        assert result == ([24, 6, 4, 0, 0], [5, 3, 1]), f"Test 217 failed: got {result}, expected {([24, 6, 4, 0, 0], [5, 3, 1])}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = partitionEvensOdds([6, 5, 4, 3, 2, 1, 999999937])
        assert result == ([6, 4, 2], [5, 3, 1, 999999937]), f"Test 218 failed: got {result}, expected {([6, 4, 2], [5, 3, 1, 999999937])}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = partitionEvensOdds([6, 5, 3, 2, 1, 0, 0])
        assert result == ([6, 2, 0, 0], [5, 3, 1]), f"Test 219 failed: got {result}, expected {([6, 2, 0, 0], [5, 3, 1])}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = partitionEvensOdds([6, 3, 2, 1, 0])
        assert result == ([6, 2, 0], [3, 1]), f"Test 220 failed: got {result}, expected {([6, 2, 0], [3, 1])}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = partitionEvensOdds([98, 0, 1, 2, 3, 4, 5, 6])
        assert result == ([98, 0, 2, 4, 6], [1, 3, 5]), f"Test 221 failed: got {result}, expected {([98, 0, 2, 4, 6], [1, 3, 5])}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = partitionEvensOdds([1, 2, 3, 4, 5, 6, 89, 2000000000000000000, 2000000000000000000])
        assert result == ([2, 4, 6, 2000000000000000000, 2000000000000000000], [1, 3, 5, 89]), f"Test 222 failed: got {result}, expected {([2, 4, 6, 2000000000000000000, 2000000000000000000], [1, 3, 5, 89])}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = partitionEvensOdds([5, 4, 3, 2, 27, 0])
        assert result == ([4, 2, 0], [5, 3, 27]), f"Test 223 failed: got {result}, expected {([4, 2, 0], [5, 3, 27])}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = partitionEvensOdds([26, 23, 20, 17, 24, 11, 0])
        assert result == ([26, 20, 24, 0], [23, 17, 11]), f"Test 224 failed: got {result}, expected {([26, 20, 24, 0], [23, 17, 11])}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = partitionEvensOdds([14, 0, 23, 48])
        assert result == ([14, 0, 48], [23]), f"Test 225 failed: got {result}, expected {([14, 0, 48], [23])}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = partitionEvensOdds([14, 17, 20, 23, 0, 27, 48])
        assert result == ([14, 20, 0, 48], [17, 23, 27]), f"Test 226 failed: got {result}, expected {([14, 20, 0, 48], [17, 23, 27])}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = partitionEvensOdds([11, 14, 17, 20, 23, 26, 0])
        assert result == ([14, 20, 26, 0], [11, 17, 23]), f"Test 227 failed: got {result}, expected {([14, 20, 26, 0], [11, 17, 23])}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = partitionEvensOdds([11, 14, 30, 20, 23, 26, 0])
        assert result == ([14, 30, 20, 26, 0], [11, 23]), f"Test 228 failed: got {result}, expected {([14, 30, 20, 26, 0], [11, 23])}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = partitionEvensOdds([14, 17, 20, 23, 26, 10])
        assert result == ([14, 20, 26, 10], [17, 23]), f"Test 229 failed: got {result}, expected {([14, 20, 26, 10], [17, 23])}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = partitionEvensOdds([11, 17, 20, 23, 26])
        assert result == ([20, 26], [11, 17, 23]), f"Test 230 failed: got {result}, expected {([20, 26], [11, 17, 23])}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = partitionEvensOdds([11, 14, 19, 20, 31, 26])
        assert result == ([14, 20, 26], [11, 19, 31]), f"Test 231 failed: got {result}, expected {([14, 20, 26], [11, 19, 31])}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = partitionEvensOdds([14, 17, 19, 23, 26, 104, 0])
        assert result == ([14, 26, 104, 0], [17, 19, 23]), f"Test 232 failed: got {result}, expected {([14, 26, 104, 0], [17, 19, 23])}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = partitionEvensOdds([0, 26, 23, 17, 14, 0])
        assert result == ([0, 26, 14, 0], [23, 17]), f"Test 233 failed: got {result}, expected {([0, 26, 14, 0], [23, 17])}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = partitionEvensOdds([26, 0, 14, 11, 34])
        assert result == ([26, 0, 14, 34], [11]), f"Test 234 failed: got {result}, expected {([26, 0, 14, 34], [11])}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = partitionEvensOdds([0, 26, 23, 20, 17, 14, 11])
        assert result == ([0, 26, 20, 14], [23, 17, 11]), f"Test 235 failed: got {result}, expected {([0, 26, 20, 14], [23, 17, 11])}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = partitionEvensOdds([14, 17, 20, 23, 26])
        assert result == ([14, 20, 26], [17, 23]), f"Test 236 failed: got {result}, expected {([14, 20, 26], [17, 23])}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = partitionEvensOdds([0, 26, 17, 14, 11])
        assert result == ([0, 26, 14], [17, 11]), f"Test 237 failed: got {result}, expected {([0, 26, 14], [17, 11])}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = partitionEvensOdds([26, 23, 20, 14, 99, 0])
        assert result == ([26, 20, 14, 0], [23, 99]), f"Test 238 failed: got {result}, expected {([26, 20, 14, 0], [23, 99])}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = partitionEvensOdds([17, 8, 3, 0, 19, 0, 0])
        assert result == ([8, 0, 0, 0], [17, 3, 19]), f"Test 239 failed: got {result}, expected {([8, 0, 0, 0], [17, 3, 19])}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = partitionEvensOdds([42, 17, 8, 3, 0, 19, 105])
        assert result == ([42, 8, 0], [17, 3, 19, 105]), f"Test 240 failed: got {result}, expected {([42, 8, 0], [17, 3, 19, 105])}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = partitionEvensOdds([19, 0, 3, 8, 17, 42])
        assert result == ([0, 8, 42], [19, 3, 17]), f"Test 241 failed: got {result}, expected {([0, 8, 42], [19, 3, 17])}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = partitionEvensOdds([42, 17, 8, 2, 0, 19, 0, 0])
        assert result == ([42, 8, 2, 0, 0, 0], [17, 19]), f"Test 242 failed: got {result}, expected {([42, 8, 2, 0, 0, 0], [17, 19])}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = partitionEvensOdds([28, 17, 8, 3, 0, 19])
        assert result == ([28, 8, 0], [17, 3, 19]), f"Test 243 failed: got {result}, expected {([28, 8, 0], [17, 3, 19])}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = partitionEvensOdds([17, 8, 0, 19, 333333333])
        assert result == ([8, 0], [17, 19, 333333333]), f"Test 244 failed: got {result}, expected {([8, 0], [17, 19, 333333333])}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = partitionEvensOdds([56, 8, 3, 0, 19])
        assert result == ([56, 8, 0], [3, 19]), f"Test 245 failed: got {result}, expected {([56, 8, 0], [3, 19])}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = partitionEvensOdds([42, 17, 8, 3, 0, 19, 333333333])
        assert result == ([42, 8, 0], [17, 3, 19, 333333333]), f"Test 246 failed: got {result}, expected {([42, 8, 0], [17, 3, 19, 333333333])}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = partitionEvensOdds([19, 3, 8, 17, 42])
        assert result == ([8, 42], [19, 3, 17]), f"Test 247 failed: got {result}, expected {([8, 42], [19, 3, 17])}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = partitionEvensOdds([23, 19, 0, 3, 8, 17, 42])
        assert result == ([0, 8, 42], [23, 19, 3, 17]), f"Test 248 failed: got {result}, expected {([0, 8, 42], [23, 19, 3, 17])}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = partitionEvensOdds([26, 42, 222222222, 8, 0, 19])
        assert result == ([26, 42, 222222222, 8, 0], [19]), f"Test 249 failed: got {result}, expected {([26, 42, 222222222, 8, 0], [19])}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = partitionEvensOdds([42, 17, 8, 3, 0, 0, 0, 0, 0])
        assert result == ([42, 8, 0, 0, 0, 0, 0], [17, 3]), f"Test 250 failed: got {result}, expected {([42, 8, 0, 0, 0, 0, 0], [17, 3])}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = partitionEvensOdds([42, 17, 8, 3, 0, 19, 0, 48])
        assert result == ([42, 8, 0, 0, 48], [17, 3, 19]), f"Test 251 failed: got {result}, expected {([42, 8, 0, 0, 48], [17, 3, 19])}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = partitionEvensOdds([101, 102, 103, 104, 105])
        assert result == ([102, 104], [101, 103, 105]), f"Test 252 failed: got {result}, expected {([102, 104], [101, 103, 105])}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = partitionEvensOdds([300, 105, 104, 103, 102, 101, 100])
        assert result == ([300, 104, 102, 100], [105, 103, 101]), f"Test 253 failed: got {result}, expected {([300, 104, 102, 100], [105, 103, 101])}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = partitionEvensOdds([0, 0, 105, 104, 103, 102, 101, 100])
        assert result == ([0, 0, 104, 102, 100], [105, 103, 101]), f"Test 254 failed: got {result}, expected {([0, 0, 104, 102, 100], [105, 103, 101])}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = partitionEvensOdds([101, 102, 103, 104, 105, 48, 0])
        assert result == ([102, 104, 48, 0], [101, 103, 105]), f"Test 255 failed: got {result}, expected {([102, 104, 48, 0], [101, 103, 105])}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = partitionEvensOdds([98, 105, 104, 103, 102, 101, 100])
        assert result == ([98, 104, 102, 100], [105, 103, 101]), f"Test 256 failed: got {result}, expected {([98, 104, 102, 100], [105, 103, 101])}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = partitionEvensOdds([100, 101, 102, 103, 104, 105, 0, 40])
        assert result == ([100, 102, 104, 0, 40], [101, 103, 105]), f"Test 257 failed: got {result}, expected {([100, 102, 104, 0, 40], [101, 103, 105])}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = partitionEvensOdds([100, 101, 102, 103, 104, 105, 222222222])
        assert result == ([100, 102, 104, 222222222], [101, 103, 105]), f"Test 258 failed: got {result}, expected {([100, 102, 104, 222222222], [101, 103, 105])}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = partitionEvensOdds([105, 104, 103, 102, 101, 100, 0, 0])
        assert result == ([104, 102, 100, 0, 0], [105, 103, 101]), f"Test 259 failed: got {result}, expected {([104, 102, 100, 0, 0], [105, 103, 101])}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = partitionEvensOdds([100, 101, 102, 103, 104, 105, 0])
        assert result == ([100, 102, 104, 0], [101, 103, 105]), f"Test 260 failed: got {result}, expected {([100, 102, 104, 0], [101, 103, 105])}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = partitionEvensOdds([100, 101, 102, 103, 104, 105, 42])
        assert result == ([100, 102, 104, 42], [101, 103, 105]), f"Test 261 failed: got {result}, expected {([100, 102, 104, 42], [101, 103, 105])}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = partitionEvensOdds([100, 101, 103, 104, 105])
        assert result == ([100, 104], [101, 103, 105]), f"Test 262 failed: got {result}, expected {([100, 104], [101, 103, 105])}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = partitionEvensOdds([100, 998, 102, 103, 104, 105])
        assert result == ([100, 998, 102, 104], [103, 105]), f"Test 263 failed: got {result}, expected {([100, 998, 102, 104], [103, 105])}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = partitionEvensOdds([100, 101, 102, 103, 104, 105, 501, 26, 0])
        assert result == ([100, 102, 104, 26, 0], [101, 103, 105, 501]), f"Test 264 failed: got {result}, expected {([100, 102, 104, 26, 0], [101, 103, 105, 501])}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = partitionEvensOdds([100, 101, 102, 103, 0])
        assert result == ([100, 102, 0], [101, 103]), f"Test 265 failed: got {result}, expected {([100, 102, 0], [101, 103])}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = partitionEvensOdds([100, 101, 102, 103, 104, 105, 31])
        assert result == ([100, 102, 104], [101, 103, 105, 31]), f"Test 266 failed: got {result}, expected {([100, 102, 104], [101, 103, 105, 31])}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = partitionEvensOdds([15, 14, 13, 12, 11, 10, 99, 996])
        assert result == ([14, 12, 10, 996], [15, 13, 11, 99]), f"Test 267 failed: got {result}, expected {([14, 12, 10, 996], [15, 13, 11, 99])}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = partitionEvensOdds([10, 11, 12, 14, 0])
        assert result == ([10, 12, 14, 0], [11]), f"Test 268 failed: got {result}, expected {([10, 12, 14, 0], [11])}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = partitionEvensOdds([103, 9, 11, 12, 13, 14, 15])
        assert result == ([12, 14], [103, 9, 11, 13, 15]), f"Test 269 failed: got {result}, expected {([12, 14], [103, 9, 11, 13, 15])}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = partitionEvensOdds([15, 14, 12, 11, 10])
        assert result == ([14, 12, 10], [15, 11]), f"Test 270 failed: got {result}, expected {([14, 12, 10], [15, 11])}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = partitionEvensOdds([15, 14, 13, 12, 11, 9])
        assert result == ([14, 12], [15, 13, 11, 9]), f"Test 271 failed: got {result}, expected {([14, 12], [15, 13, 11, 9])}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = partitionEvensOdds([15, 14, 18446744073709551616, 11, 10])
        assert result == ([14, 18446744073709551616, 10], [15, 11]), f"Test 272 failed: got {result}, expected {([14, 18446744073709551616, 10], [15, 11])}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = partitionEvensOdds([10, 11, 12, 13, 14, 15, 103])
        assert result == ([10, 12, 14], [11, 13, 15, 103]), f"Test 273 failed: got {result}, expected {([10, 12, 14], [11, 13, 15, 103])}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = partitionEvensOdds([15, 28, 13, 12, 11, 10])
        assert result == ([28, 12, 10], [15, 13, 11]), f"Test 274 failed: got {result}, expected {([28, 12, 10], [15, 13, 11])}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = partitionEvensOdds([0, 11, 12, 13, 14, 0, 98, 16])
        assert result == ([0, 12, 14, 0, 98, 16], [11, 13]), f"Test 275 failed: got {result}, expected {([0, 12, 14, 0, 98, 16], [11, 13])}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = partitionEvensOdds([15, 14, 13, 12, 11, 10, 0])
        assert result == ([14, 12, 10, 0], [15, 13, 11]), f"Test 276 failed: got {result}, expected {([14, 12, 10, 0], [15, 13, 11])}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = partitionEvensOdds([15, 14, 13, 12, 11, 101])
        assert result == ([14, 12], [15, 13, 11, 101]), f"Test 277 failed: got {result}, expected {([14, 12], [15, 13, 11, 101])}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = partitionEvensOdds([15, 14, 13, 13, 11, 10, 15, 31])
        assert result == ([14, 10], [15, 13, 13, 11, 15, 31]), f"Test 278 failed: got {result}, expected {([14, 10], [15, 13, 13, 11, 15, 31])}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = partitionEvensOdds([10, 1000000000000000000, 12, 13, 15])
        assert result == ([10, 1000000000000000000, 12], [13, 15]), f"Test 279 failed: got {result}, expected {([10, 1000000000000000000, 12], [13, 15])}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = partitionEvensOdds([15, 12, 11, 10, 0])
        assert result == ([12, 10, 0], [15, 11]), f"Test 280 failed: got {result}, expected {([12, 10, 0], [15, 11])}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = partitionEvensOdds([2, 1, 4, 6, 5, 8, 7])
        assert result == ([2, 4, 6, 8], [1, 5, 7]), f"Test 281 failed: got {result}, expected {([2, 4, 6, 8], [1, 5, 7])}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = partitionEvensOdds([7, 8, 5, 6, 3, 4, 1, 2])
        assert result == ([8, 6, 4, 2], [7, 5, 3, 1]), f"Test 282 failed: got {result}, expected {([8, 6, 4, 2], [7, 5, 3, 1])}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = partitionEvensOdds([0, 1, 4, 3, 6, 5, 8, 7, 0])
        assert result == ([0, 4, 6, 8, 0], [1, 3, 5, 7]), f"Test 283 failed: got {result}, expected {([0, 4, 6, 8, 0], [1, 3, 5, 7])}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = partitionEvensOdds([0, 5, 6, 3, 4, 2])
        assert result == ([0, 6, 4, 2], [5, 3]), f"Test 284 failed: got {result}, expected {([0, 6, 4, 2], [5, 3])}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = partitionEvensOdds([2, 4, 3, 6, 5, 8, 0, 601])
        assert result == ([2, 4, 6, 8, 0], [3, 5, 601]), f"Test 285 failed: got {result}, expected {([2, 4, 6, 8, 0], [3, 5, 601])}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = partitionEvensOdds([7, 8, 5, 20, 3, 4, 2])
        assert result == ([8, 20, 4, 2], [7, 5, 3]), f"Test 286 failed: got {result}, expected {([8, 20, 4, 2], [7, 5, 3])}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = partitionEvensOdds([987654321, 1, 4, 3, 6, 5, 8, 7, 0, 300])
        assert result == ([4, 6, 8, 0, 300], [987654321, 1, 3, 5, 7]), f"Test 287 failed: got {result}, expected {([4, 6, 8, 0, 300], [987654321, 1, 3, 5, 7])}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = partitionEvensOdds([2, 1, 4, 3, 6, 5, 8, 7, 18, 0, 50])
        assert result == ([2, 4, 6, 8, 18, 0, 50], [1, 3, 5, 7]), f"Test 288 failed: got {result}, expected {([2, 4, 6, 8, 18, 0, 50], [1, 3, 5, 7])}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = partitionEvensOdds([2, 1, 4, 3, 5, 8, 7, 0])
        assert result == ([2, 4, 8, 0], [1, 3, 5, 7]), f"Test 289 failed: got {result}, expected {([2, 4, 8, 0], [1, 3, 5, 7])}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = partitionEvensOdds([28, 0, 7, 8, 5, 6, 3, 4, 1, 2])
        assert result == ([28, 0, 8, 6, 4, 2], [7, 5, 3, 1]), f"Test 290 failed: got {result}, expected {([28, 0, 8, 6, 4, 2], [7, 5, 3, 1])}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = partitionEvensOdds([2, 1, 4, 3, 5, 8, 7])
        assert result == ([2, 4, 8], [1, 3, 5, 7]), f"Test 291 failed: got {result}, expected {([2, 4, 8], [1, 3, 5, 7])}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = partitionEvensOdds([2, 1, 4, 3, 6, 999999938, 8, 7, 0, 0])
        assert result == ([2, 4, 6, 999999938, 8, 0, 0], [1, 3, 7]), f"Test 292 failed: got {result}, expected {([2, 4, 6, 999999938, 8, 0, 0], [1, 3, 7])}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = partitionEvensOdds([2, 1, 4, 3, 6, 5, 8, 0])
        assert result == ([2, 4, 6, 8, 0], [1, 3, 5]), f"Test 293 failed: got {result}, expected {([2, 4, 6, 8, 0], [1, 3, 5])}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = partitionEvensOdds([2, 1, 4, 3, 6, 97, 401, 7])
        assert result == ([2, 4, 6], [1, 3, 97, 401, 7]), f"Test 294 failed: got {result}, expected {([2, 4, 6], [1, 3, 97, 401, 7])}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = partitionEvensOdds([1999999874, 7, 29, 5, 6, 3, 4, 1, 2])
        assert result == ([1999999874, 6, 4, 2], [7, 29, 5, 3, 1]), f"Test 295 failed: got {result}, expected {([1999999874, 6, 4, 2], [7, 29, 5, 3, 1])}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = partitionEvensOdds([0, 0, 25, 4, 27, 2, 29, 0, 31, 0])
        assert result == ([0, 0, 4, 2, 0, 0], [25, 27, 29, 31]), f"Test 296 failed: got {result}, expected {([0, 0, 4, 2, 0, 0], [25, 27, 29, 31])}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = partitionEvensOdds([6, 25, 4, 27, 2, 29, 31, 9])
        assert result == ([6, 4, 2], [25, 27, 29, 31, 9]), f"Test 297 failed: got {result}, expected {([6, 4, 2], [25, 27, 29, 31, 9])}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = partitionEvensOdds([31, 0, 29, 2, 27, 4, 25, 6, 0, 13])
        assert result == ([0, 2, 4, 6, 0], [31, 29, 27, 25, 13]), f"Test 298 failed: got {result}, expected {([0, 2, 4, 6, 0], [31, 29, 27, 25, 13])}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = partitionEvensOdds([31, 0, 29, 2, 27, 4, 25, 6, 22])
        assert result == ([0, 2, 4, 6, 22], [31, 29, 27, 25]), f"Test 299 failed: got {result}, expected {([0, 2, 4, 6, 22], [31, 29, 27, 25])}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = partitionEvensOdds([31, 29, 2, 27, 4, 25, 6, 42, 50])
        assert result == ([2, 4, 6, 42, 50], [31, 29, 27, 25]), f"Test 300 failed: got {result}, expected {([2, 4, 6, 42, 50], [31, 29, 27, 25])}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = partitionEvensOdds([31, 0, 29, 2, 27, 4, 25, 6, 73, 0])
        assert result == ([0, 2, 4, 6, 0], [31, 29, 27, 25, 73]), f"Test 301 failed: got {result}, expected {([0, 2, 4, 6, 0], [31, 29, 27, 25, 73])}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = partitionEvensOdds([31, 0, 2, 27, 4, 25, 6])
        assert result == ([0, 2, 4, 6], [31, 27, 25]), f"Test 302 failed: got {result}, expected {([0, 2, 4, 6], [31, 27, 25])}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = partitionEvensOdds([6, 25, 4, 27, 2, 29, 0, 31])
        assert result == ([6, 4, 2, 0], [25, 27, 29, 31]), f"Test 303 failed: got {result}, expected {([6, 4, 2, 0], [25, 27, 29, 31])}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = partitionEvensOdds([0, 0, 29, 8, 27, 4, 25, 17])
        assert result == ([0, 0, 8, 4], [29, 27, 25, 17]), f"Test 304 failed: got {result}, expected {([0, 0, 8, 4], [29, 27, 25, 17])}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = partitionEvensOdds([6, 25, 4, 27, 2, 29, 31])
        assert result == ([6, 4, 2], [25, 27, 29, 31]), f"Test 305 failed: got {result}, expected {([6, 4, 2], [25, 27, 29, 31])}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = partitionEvensOdds([31, 0, 29, 2, 27, 4, 25, 6, 0])
        assert result == ([0, 2, 4, 6, 0], [31, 29, 27, 25]), f"Test 306 failed: got {result}, expected {([0, 2, 4, 6, 0], [31, 29, 27, 25])}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = partitionEvensOdds([31, 0, 29, 2, 27, 4, 25, 6, 73, 37])
        assert result == ([0, 2, 4, 6], [31, 29, 27, 25, 73, 37]), f"Test 307 failed: got {result}, expected {([0, 2, 4, 6], [31, 29, 27, 25, 73, 37])}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = partitionEvensOdds([31, 0, 29, 2, 27, 4, 25, 4, 0])
        assert result == ([0, 2, 4, 4, 0], [31, 29, 27, 25]), f"Test 308 failed: got {result}, expected {([0, 2, 4, 4, 0], [31, 29, 27, 25])}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = partitionEvensOdds([31, 0, 29, 2, 26, 4, 25, 6, 0])
        assert result == ([0, 2, 26, 4, 6, 0], [31, 29, 25]), f"Test 309 failed: got {result}, expected {([0, 2, 26, 4, 6, 0], [31, 29, 25])}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = partitionEvensOdds([31, 29, 987654321, 27, 6, 0])
        assert result == ([6, 0], [31, 29, 987654321, 27]), f"Test 310 failed: got {result}, expected {([6, 0], [31, 29, 987654321, 27])}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = partitionEvensOdds([1000, 7, 998, 997, 996, 0])
        assert result == ([1000, 998, 996, 0], [7, 997]), f"Test 311 failed: got {result}, expected {([1000, 998, 996, 0], [7, 997])}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = partitionEvensOdds([1000, 999, 998, 997, 0])
        assert result == ([1000, 998, 0], [999, 997]), f"Test 312 failed: got {result}, expected {([1000, 998, 0], [999, 997])}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = partitionEvensOdds([28, 996, 997, 998, 999, 1000, 224, 0])
        assert result == ([28, 996, 998, 1000, 224, 0], [997, 999]), f"Test 313 failed: got {result}, expected {([28, 996, 998, 1000, 224, 0], [997, 999])}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = partitionEvensOdds([999, 998, 997, 56, 998])
        assert result == ([998, 56, 998], [999, 997]), f"Test 314 failed: got {result}, expected {([998, 56, 998], [999, 997])}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = partitionEvensOdds([1000, 999, 999, 997, 996, 0])
        assert result == ([1000, 996, 0], [999, 999, 997]), f"Test 315 failed: got {result}, expected {([1000, 996, 0], [999, 999, 997])}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = partitionEvensOdds([1000, 999, 997, 996])
        assert result == ([1000, 996], [999, 997]), f"Test 316 failed: got {result}, expected {([1000, 996], [999, 997])}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = partitionEvensOdds([996, 998, 999, 1000])
        assert result == ([996, 998, 1000], [999]), f"Test 317 failed: got {result}, expected {([996, 998, 1000], [999])}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = partitionEvensOdds([998, 997, 998, 999, 1001, 1000])
        assert result == ([998, 998, 1000], [997, 999, 1001]), f"Test 318 failed: got {result}, expected {([998, 998, 1000], [997, 999, 1001])}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = partitionEvensOdds([0, 996, 997, 998, 999])
        assert result == ([0, 996, 998], [997, 999]), f"Test 319 failed: got {result}, expected {([0, 996, 998], [997, 999])}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = partitionEvensOdds([1000, 998, 996])
        assert result == ([1000, 998, 996], []), f"Test 320 failed: got {result}, expected {([1000, 998, 996], [])}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = partitionEvensOdds([0, 999, 997, 996])
        assert result == ([0, 996], [999, 997]), f"Test 321 failed: got {result}, expected {([0, 996], [999, 997])}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = partitionEvensOdds([996, 997, 998, 998, 1000, 0, 22])
        assert result == ([996, 998, 998, 1000, 0, 22], [997]), f"Test 322 failed: got {result}, expected {([996, 998, 998, 1000, 0, 22], [997])}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = partitionEvensOdds([999, 998, 997, 996])
        assert result == ([998, 996], [999, 997]), f"Test 323 failed: got {result}, expected {([998, 996], [999, 997])}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = partitionEvensOdds([0, 999, 998, 997, 0])
        assert result == ([0, 998, 0], [999, 997]), f"Test 324 failed: got {result}, expected {([0, 998, 0], [999, 997])}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = partitionEvensOdds([0, 11, 104])
        assert result == ([0, 104], [11]), f"Test 325 failed: got {result}, expected {([0, 104], [11])}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = partitionEvensOdds([18446744073709551616, 3, 5, 0, 12, 21])
        assert result == ([18446744073709551616, 0, 12], [3, 5, 21]), f"Test 326 failed: got {result}, expected {([18446744073709551616, 0, 12], [3, 5, 21])}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = partitionEvensOdds([3, 34, 601])
        assert result == ([34], [3, 601]), f"Test 327 failed: got {result}, expected {([34], [3, 601])}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = partitionEvensOdds([0, 0, 8, 5, 3, 18446744073709551616])
        assert result == ([0, 0, 8, 18446744073709551616], [5, 3]), f"Test 328 failed: got {result}, expected {([0, 0, 8, 18446744073709551616], [5, 3])}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = partitionEvensOdds([0, 0, 8, 21, 3, 18446744073709551616])
        assert result == ([0, 0, 8, 18446744073709551616], [21, 3]), f"Test 329 failed: got {result}, expected {([0, 0, 8, 18446744073709551616], [21, 3])}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = partitionEvensOdds([18446744073709551616, 3, 5, 999999999999999999, 5])
        assert result == ([18446744073709551616], [3, 5, 999999999999999999, 5]), f"Test 330 failed: got {result}, expected {([18446744073709551616], [3, 5, 999999999999999999, 5])}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = partitionEvensOdds([8, 5, 3])
        assert result == ([8], [5, 3]), f"Test 331 failed: got {result}, expected {([8], [5, 3])}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = partitionEvensOdds([18446744073709551616, 3, 5, 19, 1])
        assert result == ([18446744073709551616], [3, 5, 19, 1]), f"Test 332 failed: got {result}, expected {([18446744073709551616], [3, 5, 19, 1])}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = partitionEvensOdds([18446744073709551616, 16, 5, 0])
        assert result == ([18446744073709551616, 16, 0], [5]), f"Test 333 failed: got {result}, expected {([18446744073709551616, 16, 0], [5])}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = partitionEvensOdds([18446744073709551616, 5])
        assert result == ([18446744073709551616], [5]), f"Test 334 failed: got {result}, expected {([18446744073709551616], [5])}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = partitionEvensOdds([18446744073709551616, 3, 5, 8, 42])
        assert result == ([18446744073709551616, 8, 42], [3, 5]), f"Test 335 failed: got {result}, expected {([18446744073709551616, 8, 42], [3, 5])}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = partitionEvensOdds([105, 5, 3, 18446744073709551616, 0])
        assert result == ([18446744073709551616, 0], [105, 5, 3]), f"Test 336 failed: got {result}, expected {([18446744073709551616, 0], [105, 5, 3])}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = partitionEvensOdds([18446744073709551616, 3, 6, 8, 0, 24])
        assert result == ([18446744073709551616, 6, 8, 0, 24], [3]), f"Test 337 failed: got {result}, expected {([18446744073709551616, 6, 8, 0, 24], [3])}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = partitionEvensOdds([18446744073709551616, 3, 144, 8, 4])
        assert result == ([18446744073709551616, 144, 8, 4], [3]), f"Test 338 failed: got {result}, expected {([18446744073709551616, 144, 8, 4], [3])}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = partitionEvensOdds([224, 5, 6, 987654321, 0])
        assert result == ([224, 6, 0], [5, 987654321]), f"Test 339 failed: got {result}, expected {([224, 6, 0], [5, 987654321])}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = partitionEvensOdds([26, 1000000000000000000, 999999999999999999])
        assert result == ([26, 1000000000000000000], [999999999999999999]), f"Test 340 failed: got {result}, expected {([26, 1000000000000000000], [999999999999999999])}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = partitionEvensOdds([999999999999999999, 144])
        assert result == ([144], [999999999999999999]), f"Test 341 failed: got {result}, expected {([144], [999999999999999999])}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = partitionEvensOdds([999999999999999999, 2000000000000000000])
        assert result == ([2000000000000000000], [999999999999999999]), f"Test 342 failed: got {result}, expected {([2000000000000000000], [999999999999999999])}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = partitionEvensOdds([0, 1000000000000000000, 999999999999999999])
        assert result == ([0, 1000000000000000000], [999999999999999999]), f"Test 343 failed: got {result}, expected {([0, 1000000000000000000], [999999999999999999])}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = partitionEvensOdds([999999999999999999, 1000000000000000000, 0])
        assert result == ([1000000000000000000, 0], [999999999999999999]), f"Test 344 failed: got {result}, expected {([1000000000000000000, 0], [999999999999999999])}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = partitionEvensOdds([0, 999999937, 4294967297])
        assert result == ([0], [999999937, 4294967297]), f"Test 345 failed: got {result}, expected {([0], [999999937, 4294967297])}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = partitionEvensOdds([1000000000000000000, 0, 0])
        assert result == ([1000000000000000000, 0, 0], []), f"Test 346 failed: got {result}, expected {([1000000000000000000, 0, 0], [])}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    # Test case 347
    try:
        result = partitionEvensOdds([4294967295, 999999999999999999, 0])
        assert result == ([0], [4294967295, 999999999999999999]), f"Test 347 failed: got {result}, expected {([0], [4294967295, 999999999999999999])}"
        print(f"Test 347 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 347 failed: {e}")
        test_results.append(False)

    # Test case 348
    try:
        result = partitionEvensOdds([1000000000000000000, 25, 48])
        assert result == ([1000000000000000000, 48], [25]), f"Test 348 failed: got {result}, expected {([1000000000000000000, 48], [25])}"
        print(f"Test 348 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 348 failed: {e}")
        test_results.append(False)

    # Test case 349
    try:
        result = partitionEvensOdds([1000000000000000000, 999999999999999999, 48])
        assert result == ([1000000000000000000, 48], [999999999999999999]), f"Test 349 failed: got {result}, expected {([1000000000000000000, 48], [999999999999999999])}"
        print(f"Test 349 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 349 failed: {e}")
        test_results.append(False)

    # Test case 350
    try:
        result = partitionEvensOdds([1000000000000000000, 999999999999999999])
        assert result == ([1000000000000000000], [999999999999999999]), f"Test 350 failed: got {result}, expected {([1000000000000000000], [999999999999999999])}"
        print(f"Test 350 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 350 failed: {e}")
        test_results.append(False)

    # Test case 351
    try:
        result = partitionEvensOdds([996, 1000000000000000000, 999999999999999999, 1001])
        assert result == ([996, 1000000000000000000], [999999999999999999, 1001]), f"Test 351 failed: got {result}, expected {([996, 1000000000000000000], [999999999999999999, 1001])}"
        print(f"Test 351 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 351 failed: {e}")
        test_results.append(False)

    # Test case 352
    try:
        result = partitionEvensOdds([64, 1000000000000000000])
        assert result == ([64, 1000000000000000000], []), f"Test 352 failed: got {result}, expected {([64, 1000000000000000000], [])}"
        print(f"Test 352 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 352 failed: {e}")
        test_results.append(False)

    # Test case 353
    try:
        result = partitionEvensOdds([144, 89, 55, 34, 21, 13, 21])
        assert result == ([144, 34], [89, 55, 21, 13, 21]), f"Test 353 failed: got {result}, expected {([144, 34], [89, 55, 21, 13, 21])}"
        print(f"Test 353 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 353 failed: {e}")
        test_results.append(False)

    # Test case 354
    try:
        result = partitionEvensOdds([13, 21, 34, 55, 89, 0, 28, 2, 0])
        assert result == ([34, 0, 28, 2, 0], [13, 21, 55, 89]), f"Test 354 failed: got {result}, expected {([34, 0, 28, 2, 0], [13, 21, 55, 89])}"
        print(f"Test 354 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 354 failed: {e}")
        test_results.append(False)

    # Test case 355
    try:
        result = partitionEvensOdds([0, 14, 333333333, 55, 19, 21, 13])
        assert result == ([0, 14], [333333333, 55, 19, 21, 13]), f"Test 355 failed: got {result}, expected {([0, 14], [333333333, 55, 19, 21, 13])}"
        print(f"Test 355 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 355 failed: {e}")
        test_results.append(False)

    # Test case 356
    try:
        result = partitionEvensOdds([89, 55, 34, 21, 13, 0])
        assert result == ([34, 0], [89, 55, 21, 13]), f"Test 356 failed: got {result}, expected {([34, 0], [89, 55, 21, 13])}"
        print(f"Test 356 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 356 failed: {e}")
        test_results.append(False)

    # Test case 357
    try:
        result = partitionEvensOdds([13, 21, 34, 55, 89, 144, 1000])
        assert result == ([34, 144, 1000], [13, 21, 55, 89]), f"Test 357 failed: got {result}, expected {([34, 144, 1000], [13, 21, 55, 89])}"
        print(f"Test 357 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 357 failed: {e}")
        test_results.append(False)

    # Test case 358
    try:
        result = partitionEvensOdds([13, 21, 34, 55, 89, 0])
        assert result == ([34, 0], [13, 21, 55, 89]), f"Test 358 failed: got {result}, expected {([34, 0], [13, 21, 55, 89])}"
        print(f"Test 358 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 358 failed: {e}")
        test_results.append(False)

    # Test case 359
    try:
        result = partitionEvensOdds([13, 0, 34, 55, 89, 144, 5, 200, 0])
        assert result == ([0, 34, 144, 200, 0], [13, 55, 89, 5]), f"Test 359 failed: got {result}, expected {([0, 34, 144, 200, 0], [13, 55, 89, 5])}"
        print(f"Test 359 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 359 failed: {e}")
        test_results.append(False)

    # Test case 360
    try:
        result = partitionEvensOdds([13, 21, 68, 55, 89, 144])
        assert result == ([68, 144], [13, 21, 55, 89]), f"Test 360 failed: got {result}, expected {([68, 144], [13, 21, 55, 89])}"
        print(f"Test 360 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 360 failed: {e}")
        test_results.append(False)

    # Test case 361
    try:
        result = partitionEvensOdds([17, 21, 34, 89, 144])
        assert result == ([34, 144], [17, 21, 89]), f"Test 361 failed: got {result}, expected {([34, 144], [17, 21, 89])}"
        print(f"Test 361 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 361 failed: {e}")
        test_results.append(False)

    # Test case 362
    try:
        result = partitionEvensOdds([13, 21, 99, 89, 144])
        assert result == ([144], [13, 21, 99, 89]), f"Test 362 failed: got {result}, expected {([144], [13, 21, 99, 89])}"
        print(f"Test 362 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 362 failed: {e}")
        test_results.append(False)

    # Test case 363
    try:
        result = partitionEvensOdds([13, 21, 34, 20, 144])
        assert result == ([34, 20, 144], [13, 21]), f"Test 363 failed: got {result}, expected {([34, 20, 144], [13, 21])}"
        print(f"Test 363 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 363 failed: {e}")
        test_results.append(False)

    # Test case 364
    try:
        result = partitionEvensOdds([1000, 0, 144, 48, 55, 34, 21])
        assert result == ([1000, 0, 144, 48, 34], [55, 21]), f"Test 364 failed: got {result}, expected {([1000, 0, 144, 48, 34], [55, 21])}"
        print(f"Test 364 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 364 failed: {e}")
        test_results.append(False)

    # Test case 365
    try:
        result = partitionEvensOdds([13, 21, 34, 55, 144])
        assert result == ([34, 144], [13, 21, 55]), f"Test 365 failed: got {result}, expected {([34, 144], [13, 21, 55])}"
        print(f"Test 365 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 365 failed: {e}")
        test_results.append(False)

    # Test case 366
    try:
        result = partitionEvensOdds([144, 89, 55, 34, 21, 0, 0])
        assert result == ([144, 34, 0, 0], [89, 55, 21]), f"Test 366 failed: got {result}, expected {([144, 34, 0, 0], [89, 55, 21])}"
        print(f"Test 366 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 366 failed: {e}")
        test_results.append(False)

    # Test case 367
    try:
        result = partitionEvensOdds([0, 0, 144, 89, 110, 34, 21, 13])
        assert result == ([0, 0, 144, 110, 34], [89, 21, 13]), f"Test 367 failed: got {result}, expected {([0, 0, 144, 110, 34], [89, 21, 13])}"
        print(f"Test 367 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 367 failed: {e}")
        test_results.append(False)

    # Test case 368
    try:
        result = partitionEvensOdds([101, 100, 99, 98, 97, 0])
        assert result == ([100, 98, 0], [101, 99, 97]), f"Test 368 failed: got {result}, expected {([100, 98, 0], [101, 99, 97])}"
        print(f"Test 368 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 368 failed: {e}")
        test_results.append(False)

    # Test case 369
    try:
        result = partitionEvensOdds([222222222, 99, 97, 97])
        assert result == ([222222222], [99, 97, 97]), f"Test 369 failed: got {result}, expected {([222222222], [99, 97, 97])}"
        print(f"Test 369 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 369 failed: {e}")
        test_results.append(False)

    # Test case 370
    try:
        result = partitionEvensOdds([101, 100, 99, 0])
        assert result == ([100, 0], [101, 99]), f"Test 370 failed: got {result}, expected {([100, 0], [101, 99])}"
        print(f"Test 370 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 370 failed: {e}")
        test_results.append(False)

    # Test case 371
    try:
        result = partitionEvensOdds([97, 98, 99, 100, 101, 0])
        assert result == ([98, 100, 0], [97, 99, 101]), f"Test 371 failed: got {result}, expected {([98, 100, 0], [97, 99, 101])}"
        print(f"Test 371 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 371 failed: {e}")
        test_results.append(False)

    # Test case 372
    try:
        result = partitionEvensOdds([96, 98, 98, 100])
        assert result == ([96, 98, 98, 100], []), f"Test 372 failed: got {result}, expected {([96, 98, 98, 100], [])}"
        print(f"Test 372 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 372 failed: {e}")
        test_results.append(False)

    # Test case 373
    try:
        result = partitionEvensOdds([56, 101, 100, 99, 98, 97])
        assert result == ([56, 100, 98], [101, 99, 97]), f"Test 373 failed: got {result}, expected {([56, 100, 98], [101, 99, 97])}"
        print(f"Test 373 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 373 failed: {e}")
        test_results.append(False)

    # Test case 374
    try:
        result = partitionEvensOdds([101, 100, 99, 98, 97])
        assert result == ([100, 98], [101, 99, 97]), f"Test 374 failed: got {result}, expected {([100, 98], [101, 99, 97])}"
        print(f"Test 374 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 374 failed: {e}")
        test_results.append(False)

    # Test case 375
    try:
        result = partitionEvensOdds([101, 100, 99, 98, 97, 0, 0, 0])
        assert result == ([100, 98, 0, 0, 0], [101, 99, 97]), f"Test 375 failed: got {result}, expected {([100, 98, 0, 0, 0], [101, 99, 97])}"
        print(f"Test 375 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 375 failed: {e}")
        test_results.append(False)

    # Test case 376
    try:
        result = partitionEvensOdds([97, 98, 99, 100, 101, 0, 13, 0, 0])
        assert result == ([98, 100, 0, 0, 0], [97, 99, 101, 13]), f"Test 376 failed: got {result}, expected {([98, 100, 0, 0, 0], [97, 99, 101, 13])}"
        print(f"Test 376 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 376 failed: {e}")
        test_results.append(False)

    # Test case 377
    try:
        result = partitionEvensOdds([97, 98, 99, 0, 99])
        assert result == ([98, 0], [97, 99, 99]), f"Test 377 failed: got {result}, expected {([98, 0], [97, 99, 99])}"
        print(f"Test 377 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 377 failed: {e}")
        test_results.append(False)

    # Test case 378
    try:
        result = partitionEvensOdds([97, 98, 100, 101, 0, 0, 26, 0])
        assert result == ([98, 100, 0, 0, 26, 0], [97, 101]), f"Test 378 failed: got {result}, expected {([98, 100, 0, 0, 26, 0], [97, 101])}"
        print(f"Test 378 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 378 failed: {e}")
        test_results.append(False)

    # Test case 379
    try:
        result = partitionEvensOdds([0, 101, 100, 7, 98, 97, 0])
        assert result == ([0, 100, 98, 0], [101, 7, 97]), f"Test 379 failed: got {result}, expected {([0, 100, 98, 0], [101, 7, 97])}"
        print(f"Test 379 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 379 failed: {e}")
        test_results.append(False)

    # Test case 380
    try:
        result = partitionEvensOdds([97, 98, 99, 100, 101, 39, 7])
        assert result == ([98, 100], [97, 99, 101, 39, 7]), f"Test 380 failed: got {result}, expected {([98, 100], [97, 99, 101, 39, 7])}"
        print(f"Test 380 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 380 failed: {e}")
        test_results.append(False)

    # Test case 381
    try:
        result = partitionEvensOdds([97, 98, 99, 101, 0, 0])
        assert result == ([98, 0, 0], [97, 99, 101]), f"Test 381 failed: got {result}, expected {([98, 0, 0], [97, 99, 101])}"
        print(f"Test 381 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 381 failed: {e}")
        test_results.append(False)

    # Test case 382
    try:
        result = partitionEvensOdds([97, 98, 99, 99, 103, 0, 224, 0])
        assert result == ([98, 0, 224, 0], [97, 99, 99, 103]), f"Test 382 failed: got {result}, expected {([98, 0, 224, 0], [97, 99, 99, 103])}"
        print(f"Test 382 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 382 failed: {e}")
        test_results.append(False)

    # Test case 383
    try:
        result = partitionEvensOdds([50, 40, 30, 20, 10, 1, 3, 5, 0, 40])
        assert result == ([50, 40, 30, 20, 10, 0, 40], [1, 3, 5]), f"Test 383 failed: got {result}, expected {([50, 40, 30, 20, 10, 0, 40], [1, 3, 5])}"
        print(f"Test 383 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 383 failed: {e}")
        test_results.append(False)

    # Test case 384
    try:
        result = partitionEvensOdds([5, 3, 1, 10, 20, 31, 40, 50, 0, 20])
        assert result == ([10, 20, 40, 50, 0, 20], [5, 3, 1, 31]), f"Test 384 failed: got {result}, expected {([10, 20, 40, 50, 0, 20], [5, 3, 1, 31])}"
        print(f"Test 384 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 384 failed: {e}")
        test_results.append(False)

    # Test case 385
    try:
        result = partitionEvensOdds([0, 0, 5, 3, 0, 11, 20, 30, 40, 50])
        assert result == ([0, 0, 0, 20, 30, 40, 50], [5, 3, 11]), f"Test 385 failed: got {result}, expected {([0, 0, 0, 20, 30, 40, 50], [5, 3, 11])}"
        print(f"Test 385 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 385 failed: {e}")
        test_results.append(False)

    # Test case 386
    try:
        result = partitionEvensOdds([5, 3, 1, 10, 20, 30, 40, 50])
        assert result == ([10, 20, 30, 40, 50], [5, 3, 1]), f"Test 386 failed: got {result}, expected {([10, 20, 30, 40, 50], [5, 3, 1])}"
        print(f"Test 386 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 386 failed: {e}")
        test_results.append(False)

    # Test case 387
    try:
        result = partitionEvensOdds([50, 40, 30, 20, 10, 4, 5, 999, 0])
        assert result == ([50, 40, 30, 20, 10, 4, 0], [5, 999]), f"Test 387 failed: got {result}, expected {([50, 40, 30, 20, 10, 4, 0], [5, 999])}"
        print(f"Test 387 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 387 failed: {e}")
        test_results.append(False)

    # Test case 388
    try:
        result = partitionEvensOdds([1, 5, 3, 10, 20, 30, 40, 50])
        assert result == ([10, 20, 30, 40, 50], [1, 5, 3]), f"Test 388 failed: got {result}, expected {([10, 20, 30, 40, 50], [1, 5, 3])}"
        print(f"Test 388 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 388 failed: {e}")
        test_results.append(False)

    # Test case 389
    try:
        result = partitionEvensOdds([50, 40, 31, 18, 10, 1, 3, 5])
        assert result == ([50, 40, 18, 10], [31, 1, 3, 5]), f"Test 389 failed: got {result}, expected {([50, 40, 18, 10], [31, 1, 3, 5])}"
        print(f"Test 389 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 389 failed: {e}")
        test_results.append(False)

    # Test case 390
    try:
        result = partitionEvensOdds([4294967296, 30, 20, 10, 1, 3, 5, 3, 0])
        assert result == ([4294967296, 30, 20, 10, 0], [1, 3, 5, 3]), f"Test 390 failed: got {result}, expected {([4294967296, 30, 20, 10, 0], [1, 3, 5, 3])}"
        print(f"Test 390 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 390 failed: {e}")
        test_results.append(False)

    # Test case 391
    try:
        result = partitionEvensOdds([40, 30, 20, 10, 999, 42, 5, 0])
        assert result == ([40, 30, 20, 10, 42, 0], [999, 5]), f"Test 391 failed: got {result}, expected {([40, 30, 20, 10, 42, 0], [999, 5])}"
        print(f"Test 391 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 391 failed: {e}")
        test_results.append(False)

    # Test case 392
    try:
        result = partitionEvensOdds([50, 40, 30, 20, 10, 1, 3, 0, 97])
        assert result == ([50, 40, 30, 20, 10, 0], [1, 3, 97]), f"Test 392 failed: got {result}, expected {([50, 40, 30, 20, 10, 0], [1, 3, 97])}"
        print(f"Test 392 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 392 failed: {e}")
        test_results.append(False)

    # Test case 393
    try:
        result = partitionEvensOdds([50, 40, 30, 10, 1, 3, 5, 5, 0, 0])
        assert result == ([50, 40, 30, 10, 0, 0], [1, 3, 5, 5]), f"Test 393 failed: got {result}, expected {([50, 40, 30, 10, 0, 0], [1, 3, 5, 5])}"
        print(f"Test 393 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 393 failed: {e}")
        test_results.append(False)

    # Test case 394
    try:
        result = partitionEvensOdds([5, 3, 1, 10, 20, 30, 40, 50, 23, 0])
        assert result == ([10, 20, 30, 40, 50, 0], [5, 3, 1, 23]), f"Test 394 failed: got {result}, expected {([10, 20, 30, 40, 50, 0], [5, 3, 1, 23])}"
        print(f"Test 394 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 394 failed: {e}")
        test_results.append(False)

    # Test case 395
    try:
        result = partitionEvensOdds([50, 32, 20, 10, 1, 3, 5, 0])
        assert result == ([50, 32, 20, 10, 0], [1, 3, 5]), f"Test 395 failed: got {result}, expected {([50, 32, 20, 10, 0], [1, 3, 5])}"
        print(f"Test 395 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 395 failed: {e}")
        test_results.append(False)

    # Test case 396
    try:
        result = partitionEvensOdds([50, 40, 30, 20, 10, 3, 5, 2000000000000000000, 12])
        assert result == ([50, 40, 30, 20, 10, 2000000000000000000, 12], [3, 5]), f"Test 396 failed: got {result}, expected {([50, 40, 30, 20, 10, 2000000000000000000, 12], [3, 5])}"
        print(f"Test 396 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 396 failed: {e}")
        test_results.append(False)

    # Test case 397
    try:
        result = partitionEvensOdds([46, 5, 3, 1, 10, 20, 30, 40, 50, 0])
        assert result == ([46, 10, 20, 30, 40, 50, 0], [5, 3, 1]), f"Test 397 failed: got {result}, expected {([46, 10, 20, 30, 40, 50, 0], [5, 3, 1])}"
        print(f"Test 397 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 397 failed: {e}")
        test_results.append(False)

    # Test case 398
    try:
        result = partitionEvensOdds([7, 14, 28, 112, 224, 0])
        assert result == ([14, 28, 112, 224, 0], [7]), f"Test 398 failed: got {result}, expected {([14, 28, 112, 224, 0], [7])}"
        print(f"Test 398 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 398 failed: {e}")
        test_results.append(False)

    # Test case 399
    try:
        result = partitionEvensOdds([7, 28, 56, 224])
        assert result == ([28, 56, 224], [7]), f"Test 399 failed: got {result}, expected {([28, 56, 224], [7])}"
        print(f"Test 399 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 399 failed: {e}")
        test_results.append(False)

    # Test case 400
    try:
        result = partitionEvensOdds([8, 14, 28, 56, 112, 0])
        assert result == ([8, 14, 28, 56, 112, 0], []), f"Test 400 failed: got {result}, expected {([8, 14, 28, 56, 112, 0], [])}"
        print(f"Test 400 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 400 failed: {e}")
        test_results.append(False)

    # Test case 401
    try:
        result = partitionEvensOdds([7, 14, 28, 56, 300, 224, 0, 68, 999999937, 105])
        assert result == ([14, 28, 56, 300, 224, 0, 68], [7, 999999937, 105]), f"Test 401 failed: got {result}, expected {([14, 28, 56, 300, 224, 0, 68], [7, 999999937, 105])}"
        print(f"Test 401 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 401 failed: {e}")
        test_results.append(False)

    # Test case 402
    try:
        result = partitionEvensOdds([0, 997, 0, 7, 14, 28, 56, 112, 224])
        assert result == ([0, 0, 14, 28, 56, 112, 224], [997, 7]), f"Test 402 failed: got {result}, expected {([0, 0, 14, 28, 56, 112, 224], [997, 7])}"
        print(f"Test 402 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 402 failed: {e}")
        test_results.append(False)

    # Test case 403
    try:
        result = partitionEvensOdds([0, 224, 112, 56, 28, 14, 7])
        assert result == ([0, 224, 112, 56, 28, 14], [7]), f"Test 403 failed: got {result}, expected {([0, 224, 112, 56, 28, 14], [7])}"
        print(f"Test 403 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 403 failed: {e}")
        test_results.append(False)

    # Test case 404
    try:
        result = partitionEvensOdds([112, 224, 112, 56, 26, 14, 7])
        assert result == ([112, 224, 112, 56, 26, 14], [7]), f"Test 404 failed: got {result}, expected {([112, 224, 112, 56, 26, 14], [7])}"
        print(f"Test 404 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 404 failed: {e}")
        test_results.append(False)

    # Test case 405
    try:
        result = partitionEvensOdds([224, 56, 28, 14])
        assert result == ([224, 56, 28, 14], []), f"Test 405 failed: got {result}, expected {([224, 56, 28, 14], [])}"
        print(f"Test 405 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 405 failed: {e}")
        test_results.append(False)

    # Test case 406
    try:
        result = partitionEvensOdds([224, 112, 56, 28, 14, 7])
        assert result == ([224, 112, 56, 28, 14], [7]), f"Test 406 failed: got {result}, expected {([224, 112, 56, 28, 14], [7])}"
        print(f"Test 406 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 406 failed: {e}")
        test_results.append(False)

    # Test case 407
    try:
        result = partitionEvensOdds([224, 112, 56, 14, 7])
        assert result == ([224, 112, 56, 14], [7]), f"Test 407 failed: got {result}, expected {([224, 112, 56, 14], [7])}"
        print(f"Test 407 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 407 failed: {e}")
        test_results.append(False)

    # Test case 408
    try:
        result = partitionEvensOdds([0, 224, 112, 56, 28, 14, 7, 9, 19, 68])
        assert result == ([0, 224, 112, 56, 28, 14, 68], [7, 9, 19]), f"Test 408 failed: got {result}, expected {([0, 224, 112, 56, 28, 14, 68], [7, 9, 19])}"
        print(f"Test 408 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 408 failed: {e}")
        test_results.append(False)

    # Test case 409
    try:
        result = partitionEvensOdds([99, 224, 112, 57, 28, 14, 7, 5, 0])
        assert result == ([224, 112, 28, 14, 0], [99, 57, 7, 5]), f"Test 409 failed: got {result}, expected {([224, 112, 28, 14, 0], [99, 57, 7, 5])}"
        print(f"Test 409 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 409 failed: {e}")
        test_results.append(False)

    # Test case 410
    try:
        result = partitionEvensOdds([7, 23, 56, 112, 224, 998, 0, 0])
        assert result == ([56, 112, 224, 998, 0, 0], [7, 23]), f"Test 410 failed: got {result}, expected {([56, 112, 224, 998, 0, 0], [7, 23])}"
        print(f"Test 410 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 410 failed: {e}")
        test_results.append(False)

    # Test case 411
    try:
        result = partitionEvensOdds([224, 112, 56, 28, 14, 7, 0])
        assert result == ([224, 112, 56, 28, 14, 0], [7]), f"Test 411 failed: got {result}, expected {([224, 112, 56, 28, 14, 0], [7])}"
        print(f"Test 411 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 411 failed: {e}")
        test_results.append(False)

    # Test case 412
    try:
        result = partitionEvensOdds([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 55, 0])
        assert result == ([8, 6, 4, 2, 0, 0], [9, 7, 5, 3, 1, 55]), f"Test 412 failed: got {result}, expected {([8, 6, 4, 2, 0, 0], [9, 7, 5, 3, 1, 55])}"
        print(f"Test 412 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 412 failed: {e}")
        test_results.append(False)

    # Test case 413
    try:
        result = partitionEvensOdds([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 73, 13, 200, 999999938, 105])
        assert result == ([8, 6, 4, 2, 0, 200, 999999938], [9, 7, 5, 3, 1, 73, 13, 105]), f"Test 413 failed: got {result}, expected {([8, 6, 4, 2, 0, 200, 999999938], [9, 7, 5, 3, 1, 73, 13, 105])}"
        print(f"Test 413 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 413 failed: {e}")
        test_results.append(False)

    # Test case 414
    try:
        result = partitionEvensOdds([0, 1, 3, 3, 4, 5, 6, 7, 8, 9, 110])
        assert result == ([0, 4, 6, 8, 110], [1, 3, 3, 5, 7, 9]), f"Test 414 failed: got {result}, expected {([0, 4, 6, 8, 110], [1, 3, 3, 5, 7, 9])}"
        print(f"Test 414 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 414 failed: {e}")
        test_results.append(False)

    # Test case 415
    try:
        result = partitionEvensOdds([0, 0, 1, 2, 6, 4, 5, 7, 8, 9])
        assert result == ([0, 0, 2, 6, 4, 8], [1, 5, 7, 9]), f"Test 415 failed: got {result}, expected {([0, 0, 2, 6, 4, 8], [1, 5, 7, 9])}"
        print(f"Test 415 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 415 failed: {e}")
        test_results.append(False)

    # Test case 416
    try:
        result = partitionEvensOdds([9, 8, 7, 6, 5, 4, 2, 1, 0])
        assert result == ([8, 6, 4, 2, 0], [9, 7, 5, 1]), f"Test 416 failed: got {result}, expected {([8, 6, 4, 2, 0], [9, 7, 5, 1])}"
        print(f"Test 416 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 416 failed: {e}")
        test_results.append(False)

    # Test case 417
    try:
        result = partitionEvensOdds([9, 8, 7, 6, 5, 4, 3, 2, 0, 99, 0])
        assert result == ([8, 6, 4, 2, 0, 0], [9, 7, 5, 3, 99]), f"Test 417 failed: got {result}, expected {([8, 6, 4, 2, 0, 0], [9, 7, 5, 3, 99])}"
        print(f"Test 417 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 417 failed: {e}")
        test_results.append(False)

    # Test case 418
    try:
        result = partitionEvensOdds([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 68])
        assert result == ([8, 6, 4, 2, 0, 68], [9, 7, 5, 3, 1]), f"Test 418 failed: got {result}, expected {([8, 6, 4, 2, 0, 68], [9, 7, 5, 3, 1])}"
        print(f"Test 418 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 418 failed: {e}")
        test_results.append(False)

    # Test case 419
    try:
        result = partitionEvensOdds([0, 1, 2, 0, 4, 6, 7, 8, 987654321])
        assert result == ([0, 2, 0, 4, 6, 8], [1, 7, 987654321]), f"Test 419 failed: got {result}, expected {([0, 2, 0, 4, 6, 8], [1, 7, 987654321])}"
        print(f"Test 419 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 419 failed: {e}")
        test_results.append(False)

    # Test case 420
    try:
        result = partitionEvensOdds([0, 68, 89, 0, 1, 2, 3, 4, 5, 6, 5, 8, 9])
        assert result == ([0, 68, 0, 2, 4, 6, 8], [89, 1, 3, 5, 5, 9]), f"Test 420 failed: got {result}, expected {([0, 68, 0, 2, 4, 6, 8], [89, 1, 3, 5, 5, 9])}"
        print(f"Test 420 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 420 failed: {e}")
        test_results.append(False)

    # Test case 421
    try:
        result = partitionEvensOdds([999, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 501])
        assert result == ([0, 0, 2, 4, 6, 8], [999, 1, 3, 5, 7, 9, 501]), f"Test 421 failed: got {result}, expected {([0, 0, 2, 4, 6, 8], [999, 1, 3, 5, 7, 9, 501])}"
        print(f"Test 421 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 421 failed: {e}")
        test_results.append(False)

    # Test case 422
    try:
        result = partitionEvensOdds([9, 8, 7, 6, 0, 0, 3, 2, 1, 0, 4, 0, 0])
        assert result == ([8, 6, 0, 0, 2, 0, 4, 0, 0], [9, 7, 3, 1]), f"Test 422 failed: got {result}, expected {([8, 6, 0, 0, 2, 0, 4, 0, 0], [9, 7, 3, 1])}"
        print(f"Test 422 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 422 failed: {e}")
        test_results.append(False)

    # Test case 423
    try:
        result = partitionEvensOdds([9, 9, 7, 6, 4, 3, 2, 1, 0])
        assert result == ([6, 4, 2, 0], [9, 9, 7, 3, 1]), f"Test 423 failed: got {result}, expected {([6, 4, 2, 0], [9, 9, 7, 3, 1])}"
        print(f"Test 423 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 423 failed: {e}")
        test_results.append(False)

    # Test case 424
    try:
        result = partitionEvensOdds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        assert result == ([0, 2, 4, 6, 8, 0], [1, 3, 5, 7, 9]), f"Test 424 failed: got {result}, expected {([0, 2, 4, 6, 8, 0], [1, 3, 5, 7, 9])}"
        print(f"Test 424 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 424 failed: {e}")
        test_results.append(False)

    # Test case 425
    try:
        result = partitionEvensOdds([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 97])
        assert result == ([8, 6, 4, 2, 0], [9, 7, 5, 3, 1, 97]), f"Test 425 failed: got {result}, expected {([8, 6, 4, 2, 0], [9, 7, 5, 3, 1, 97])}"
        print(f"Test 425 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 425 failed: {e}")
        test_results.append(False)

    # Test case 426
    try:
        result = partitionEvensOdds([0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 9])
        assert result == ([0, 0, 0, 0, 2, 4, 6], [1, 3, 5, 7, 9]), f"Test 426 failed: got {result}, expected {([0, 0, 0, 0, 2, 4, 6], [1, 3, 5, 7, 9])}"
        print(f"Test 426 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 426 failed: {e}")
        test_results.append(False)

    # Test case 427
    try:
        result = partitionEvensOdds([0, 200, 300, 401, 501, 601, 55])
        assert result == ([0, 200, 300], [401, 501, 601, 55]), f"Test 427 failed: got {result}, expected {([0, 200, 300], [401, 501, 601, 55])}"
        print(f"Test 427 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 427 failed: {e}")
        test_results.append(False)

    # Test case 428
    try:
        result = partitionEvensOdds([37, 46, 601, 501, 401, 300, 200, 100])
        assert result == ([46, 300, 200, 100], [37, 601, 501, 401]), f"Test 428 failed: got {result}, expected {([46, 300, 200, 100], [37, 601, 501, 401])}"
        print(f"Test 428 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 428 failed: {e}")
        test_results.append(False)

    # Test case 429
    try:
        result = partitionEvensOdds([0, 601, 501, 300, 200, 100, 0])
        assert result == ([0, 300, 200, 100, 0], [601, 501]), f"Test 429 failed: got {result}, expected {([0, 300, 200, 100, 0], [601, 501])}"
        print(f"Test 429 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 429 failed: {e}")
        test_results.append(False)

    # Test case 430
    try:
        result = partitionEvensOdds([0, 100, 200, 401, 501, 601, 24, 30, 31, 13])
        assert result == ([0, 100, 200, 24, 30], [401, 501, 601, 31, 13]), f"Test 430 failed: got {result}, expected {([0, 100, 200, 24, 30], [401, 501, 601, 31, 13])}"
        print(f"Test 430 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 430 failed: {e}")
        test_results.append(False)

    # Test case 431
    try:
        result = partitionEvensOdds([601, 501, 401, 300, 200, 100, 0])
        assert result == ([300, 200, 100, 0], [601, 501, 401]), f"Test 431 failed: got {result}, expected {([300, 200, 100, 0], [601, 501, 401])}"
        print(f"Test 431 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 431 failed: {e}")
        test_results.append(False)

    # Test case 432
    try:
        result = partitionEvensOdds([0, 601, 501, 401, 300, 200, 100, 0, 0])
        assert result == ([0, 300, 200, 100, 0, 0], [601, 501, 401]), f"Test 432 failed: got {result}, expected {([0, 300, 200, 100, 0, 0], [601, 501, 401])}"
        print(f"Test 432 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 432 failed: {e}")
        test_results.append(False)

    # Test case 433
    try:
        result = partitionEvensOdds([601, 501, 401, 300, 200, 100, 0, 0])
        assert result == ([300, 200, 100, 0, 0], [601, 501, 401]), f"Test 433 failed: got {result}, expected {([300, 200, 100, 0, 0], [601, 501, 401])}"
        print(f"Test 433 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 433 failed: {e}")
        test_results.append(False)

    # Test case 434
    try:
        result = partitionEvensOdds([0, 601, 501, 401, 300, 200, 100, 0])
        assert result == ([0, 300, 200, 100, 0], [601, 501, 401]), f"Test 434 failed: got {result}, expected {([0, 300, 200, 100, 0], [601, 501, 401])}"
        print(f"Test 434 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 434 failed: {e}")
        test_results.append(False)

    # Test case 435
    try:
        result = partitionEvensOdds([100, 200, 300, 401, 501, 601, 0, 0])
        assert result == ([100, 200, 300, 0, 0], [401, 501, 601]), f"Test 435 failed: got {result}, expected {([100, 200, 300, 0, 0], [401, 501, 601])}"
        print(f"Test 435 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 435 failed: {e}")
        test_results.append(False)

    # Test case 436
    try:
        result = partitionEvensOdds([0, 100, 401, 501, 601, 300, 34, 0])
        assert result == ([0, 100, 300, 34, 0], [401, 501, 601]), f"Test 436 failed: got {result}, expected {([0, 100, 300, 34, 0], [401, 501, 601])}"
        print(f"Test 436 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 436 failed: {e}")
        test_results.append(False)

    # Test case 437
    try:
        result = partitionEvensOdds([98, 501, 401, 300, 200, 100, 0, 0])
        assert result == ([98, 300, 200, 100, 0, 0], [501, 401]), f"Test 437 failed: got {result}, expected {([98, 300, 200, 100, 0, 0], [501, 401])}"
        print(f"Test 437 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 437 failed: {e}")
        test_results.append(False)

    # Test case 438
    try:
        result = partitionEvensOdds([601, 30, 401, 300, 200, 100, 0])
        assert result == ([30, 300, 200, 100, 0], [601, 401]), f"Test 438 failed: got {result}, expected {([30, 300, 200, 100, 0], [601, 401])}"
        print(f"Test 438 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 438 failed: {e}")
        test_results.append(False)

    # Test case 439
    try:
        result = partitionEvensOdds([0, 100, 200, 300, 401, 501, 601, 105, 98])
        assert result == ([0, 100, 200, 300, 98], [401, 501, 601, 105]), f"Test 439 failed: got {result}, expected {([0, 100, 200, 300, 98], [401, 501, 601, 105])}"
        print(f"Test 439 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 439 failed: {e}")
        test_results.append(False)

    # Test case 440
    try:
        result = partitionEvensOdds([601, 501, 401, 300, 200, 27, 0])
        assert result == ([300, 200, 0], [601, 501, 401, 27]), f"Test 440 failed: got {result}, expected {([300, 200, 0], [601, 501, 401, 27])}"
        print(f"Test 440 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 440 failed: {e}")
        test_results.append(False)

    # Test case 441
    try:
        result = partitionEvensOdds([1, 18, 3, 20, 5, 0, 64, 24, 9])
        assert result == ([18, 20, 0, 64, 24], [1, 3, 5, 9]), f"Test 441 failed: got {result}, expected {([18, 20, 0, 64, 24], [1, 3, 5, 9])}"
        print(f"Test 441 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 441 failed: {e}")
        test_results.append(False)

    # Test case 442
    try:
        result = partitionEvensOdds([0, 9, 24, 7, 22, 20, 3, 18, 1, 16])
        assert result == ([0, 24, 22, 20, 18, 16], [9, 7, 3, 1]), f"Test 442 failed: got {result}, expected {([0, 24, 22, 20, 18, 16], [9, 7, 3, 1])}"
        print(f"Test 442 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 442 failed: {e}")
        test_results.append(False)

    # Test case 443
    try:
        result = partitionEvensOdds([16, 29, 18, 3, 20, 5, 7, 24, 9])
        assert result == ([16, 18, 20, 24], [29, 3, 5, 7, 9]), f"Test 443 failed: got {result}, expected {([16, 18, 20, 24], [29, 3, 5, 7, 9])}"
        print(f"Test 443 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 443 failed: {e}")
        test_results.append(False)

    # Test case 444
    try:
        result = partitionEvensOdds([16, 1, 18, 3, 5, 22, 7, 9, 0])
        assert result == ([16, 18, 22, 0], [1, 3, 5, 7, 9]), f"Test 444 failed: got {result}, expected {([16, 18, 22, 0], [1, 3, 5, 7, 9])}"
        print(f"Test 444 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 444 failed: {e}")
        test_results.append(False)

    # Test case 445
    try:
        result = partitionEvensOdds([9, 24, 7, 13, 5, 20, 3, 601, 1, 16, 2, 501])
        assert result == ([24, 20, 16, 2], [9, 7, 13, 5, 3, 601, 1, 501]), f"Test 445 failed: got {result}, expected {([24, 20, 16, 2], [9, 7, 13, 5, 3, 601, 1, 501])}"
        print(f"Test 445 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 445 failed: {e}")
        test_results.append(False)

    # Test case 446
    try:
        result = partitionEvensOdds([62, 9, 24, 7, 22, 5, 89, 3, 18, 1, 16, 224])
        assert result == ([62, 24, 22, 18, 16, 224], [9, 7, 5, 89, 3, 1]), f"Test 446 failed: got {result}, expected {([62, 24, 22, 18, 16, 224], [9, 7, 5, 89, 3, 1])}"
        print(f"Test 446 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 446 failed: {e}")
        test_results.append(False)

    # Test case 447
    try:
        result = partitionEvensOdds([16, 1, 18, 3, 20, 5, 22, 7, 24, 9, 0, 0, 1000000000000000000, 0])
        assert result == ([16, 18, 20, 22, 24, 0, 0, 1000000000000000000, 0], [1, 3, 5, 7, 9]), f"Test 447 failed: got {result}, expected {([16, 18, 20, 22, 24, 0, 0, 1000000000000000000, 0], [1, 3, 5, 7, 9])}"
        print(f"Test 447 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 447 failed: {e}")
        test_results.append(False)

    # Test case 448
    try:
        result = partitionEvensOdds([0, 1, 18, 3, 20, 5, 22, 0, 9, 0, 0])
        assert result == ([0, 18, 20, 22, 0, 0, 0], [1, 3, 5, 9]), f"Test 448 failed: got {result}, expected {([0, 18, 20, 22, 0, 0, 0], [1, 3, 5, 9])}"
        print(f"Test 448 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 448 failed: {e}")
        test_results.append(False)

    # Test case 449
    try:
        result = partitionEvensOdds([1, 18, 3, 20, 5, 22, 7, 24, 9])
        assert result == ([18, 20, 22, 24], [1, 3, 5, 7, 9]), f"Test 449 failed: got {result}, expected {([18, 20, 22, 24], [1, 3, 5, 7, 9])}"
        print(f"Test 449 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 449 failed: {e}")
        test_results.append(False)

    # Test case 450
    try:
        result = partitionEvensOdds([0, 9, 25, 7, 22, 5, 20, 3, 18, 1, 16, 999])
        assert result == ([0, 22, 20, 18, 16], [9, 25, 7, 5, 3, 1, 999]), f"Test 450 failed: got {result}, expected {([0, 22, 20, 18, 16], [9, 25, 7, 5, 3, 1, 999])}"
        print(f"Test 450 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 450 failed: {e}")
        test_results.append(False)

    # Test case 451
    try:
        result = partitionEvensOdds([4294967297, 9, 24, 7, 22, 5, 20, 3, 18, 1, 0])
        assert result == ([24, 22, 20, 18, 0], [4294967297, 9, 7, 5, 3, 1]), f"Test 451 failed: got {result}, expected {([24, 22, 20, 18, 0], [4294967297, 9, 7, 5, 3, 1])}"
        print(f"Test 451 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 451 failed: {e}")
        test_results.append(False)

    # Test case 452
    try:
        result = partitionEvensOdds([9, 24, 14, 22, 5, 20, 3, 18, 1, 0, 48])
        assert result == ([24, 14, 22, 20, 18, 0, 48], [9, 5, 3, 1]), f"Test 452 failed: got {result}, expected {([24, 14, 22, 20, 18, 0, 48], [9, 5, 3, 1])}"
        print(f"Test 452 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 452 failed: {e}")
        test_results.append(False)

    # Test case 453
    try:
        result = partitionEvensOdds([16, 1, 18, 3, 20, 5, 22, 7, 13, 9])
        assert result == ([16, 18, 20, 22], [1, 3, 5, 7, 13, 9]), f"Test 453 failed: got {result}, expected {([16, 18, 20, 22], [1, 3, 5, 7, 13, 9])}"
        print(f"Test 453 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 453 failed: {e}")
        test_results.append(False)

    # Test case 454
    try:
        result = partitionEvensOdds([16, 1, 18, 3, 20, 5, 22, 97, 24, 9, 100, 11])
        assert result == ([16, 18, 20, 22, 24, 100], [1, 3, 5, 97, 9, 11]), f"Test 454 failed: got {result}, expected {([16, 18, 20, 22, 24, 100], [1, 3, 5, 97, 9, 11])}"
        print(f"Test 454 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 454 failed: {e}")
        test_results.append(False)

    # Test case 455
    try:
        result = partitionEvensOdds([16, 18, 3, 20, 104, 22, 24, 9])
        assert result == ([16, 18, 20, 104, 22, 24], [3, 9]), f"Test 455 failed: got {result}, expected {([16, 18, 20, 104, 22, 24], [3, 9])}"
        print(f"Test 455 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 455 failed: {e}")
        test_results.append(False)

    # Test case 456
    try:
        result = partitionEvensOdds([123456789, 987654321, 100])
        assert result == ([100], [123456789, 987654321]), f"Test 456 failed: got {result}, expected {([100], [123456789, 987654321])}"
        print(f"Test 456 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 456 failed: {e}")
        test_results.append(False)

    # Test case 457
    try:
        result = partitionEvensOdds([123456789, 987654321, 222222222, 333333333, 102, 0])
        assert result == ([222222222, 102, 0], [123456789, 987654321, 333333333]), f"Test 457 failed: got {result}, expected {([222222222, 102, 0], [123456789, 987654321, 333333333])}"
        print(f"Test 457 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 457 failed: {e}")
        test_results.append(False)

    # Test case 458
    try:
        result = partitionEvensOdds([333333333, 987654321, 123456789])
        assert result == ([], [333333333, 987654321, 123456789]), f"Test 458 failed: got {result}, expected {([], [333333333, 987654321, 123456789])}"
        print(f"Test 458 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 458 failed: {e}")
        test_results.append(False)

    # Test case 459
    try:
        result = partitionEvensOdds([123456789, 987654321, 222222222])
        assert result == ([222222222], [123456789, 987654321]), f"Test 459 failed: got {result}, expected {([222222222], [123456789, 987654321])}"
        print(f"Test 459 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 459 failed: {e}")
        test_results.append(False)

    # Test case 460
    try:
        result = partitionEvensOdds([0, 222222222, 333333333, 0])
        assert result == ([0, 222222222, 0], [333333333]), f"Test 460 failed: got {result}, expected {([0, 222222222, 0], [333333333])}"
        print(f"Test 460 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 460 failed: {e}")
        test_results.append(False)

    # Test case 461
    try:
        result = partitionEvensOdds([123456789, 987654321, 222222222, 333333333, 1])
        assert result == ([222222222], [123456789, 987654321, 333333333, 1]), f"Test 461 failed: got {result}, expected {([222222222], [123456789, 987654321, 333333333, 1])}"
        print(f"Test 461 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 461 failed: {e}")
        test_results.append(False)

    # Test case 462
    try:
        result = partitionEvensOdds([123456789, 987654321, 222222222, 333333333, 0])
        assert result == ([222222222, 0], [123456789, 987654321, 333333333]), f"Test 462 failed: got {result}, expected {([222222222, 0], [123456789, 987654321, 333333333])}"
        print(f"Test 462 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 462 failed: {e}")
        test_results.append(False)

    # Test case 463
    try:
        result = partitionEvensOdds([224, 11, 222222222, 333333333])
        assert result == ([224, 222222222], [11, 333333333]), f"Test 463 failed: got {result}, expected {([224, 222222222], [11, 333333333])}"
        print(f"Test 463 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 463 failed: {e}")
        test_results.append(False)

    # Test case 464
    try:
        result = partitionEvensOdds([333333333, 222222222, 987654321, 123456789])
        assert result == ([222222222], [333333333, 987654321, 123456789]), f"Test 464 failed: got {result}, expected {([222222222], [333333333, 987654321, 123456789])}"
        print(f"Test 464 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 464 failed: {e}")
        test_results.append(False)

    # Test case 465
    try:
        result = partitionEvensOdds([0, 333333333, 222222222, 987654321, 123456789])
        assert result == ([0, 222222222], [333333333, 987654321, 123456789]), f"Test 465 failed: got {result}, expected {([0, 222222222], [333333333, 987654321, 123456789])}"
        print(f"Test 465 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 465 failed: {e}")
        test_results.append(False)

    # Test case 466
    try:
        result = partitionEvensOdds([333333333, 222222222, 987654321, 123456789, 4294967296])
        assert result == ([222222222, 4294967296], [333333333, 987654321, 123456789]), f"Test 466 failed: got {result}, expected {([222222222, 4294967296], [333333333, 987654321, 123456789])}"
        print(f"Test 466 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 466 failed: {e}")
        test_results.append(False)

    # Test case 467
    try:
        result = partitionEvensOdds([333333333, 222222222, 987654322, 123456789, 0, 2, 0])
        assert result == ([222222222, 987654322, 0, 2, 0], [333333333, 123456789]), f"Test 467 failed: got {result}, expected {([222222222, 987654322, 0, 2, 0], [333333333, 123456789])}"
        print(f"Test 467 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 467 failed: {e}")
        test_results.append(False)

    # Test case 468
    try:
        result = partitionEvensOdds([123456789, 987654321, 222222222, 999999999999999999, 0])
        assert result == ([222222222, 0], [123456789, 987654321, 999999999999999999]), f"Test 468 failed: got {result}, expected {([222222222, 0], [123456789, 987654321, 999999999999999999])}"
        print(f"Test 468 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 468 failed: {e}")
        test_results.append(False)

    # Test case 469
    try:
        result = partitionEvensOdds([18446744073709551616, 4294967297])
        assert result == ([18446744073709551616], [4294967297]), f"Test 469 failed: got {result}, expected {([18446744073709551616], [4294967297])}"
        print(f"Test 469 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 469 failed: {e}")
        test_results.append(False)

    # Test case 470
    try:
        result = partitionEvensOdds([4294967295, 4294967296, 4294967297, 13, 12])
        assert result == ([4294967296, 12], [4294967295, 4294967297, 13]), f"Test 470 failed: got {result}, expected {([4294967296, 12], [4294967295, 4294967297, 13])}"
        print(f"Test 470 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 470 failed: {e}")
        test_results.append(False)

    # Test case 471
    try:
        result = partitionEvensOdds([4294967297, 4294967296, 4294967295])
        assert result == ([4294967296], [4294967297, 4294967295]), f"Test 471 failed: got {result}, expected {([4294967296], [4294967297, 4294967295])}"
        print(f"Test 471 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 471 failed: {e}")
        test_results.append(False)

    # Test case 472
    try:
        result = partitionEvensOdds([9, 4294967297, 123456789, 0])
        assert result == ([0], [9, 4294967297, 123456789]), f"Test 472 failed: got {result}, expected {([0], [9, 4294967297, 123456789])}"
        print(f"Test 472 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 472 failed: {e}")
        test_results.append(False)

    # Test case 473
    try:
        result = partitionEvensOdds([4294967296, 4294967297])
        assert result == ([4294967296], [4294967297]), f"Test 473 failed: got {result}, expected {([4294967296], [4294967297])}"
        print(f"Test 473 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 473 failed: {e}")
        test_results.append(False)

    # Test case 474
    try:
        result = partitionEvensOdds([4294967295, 4294967296, 73, 987654322])
        assert result == ([4294967296, 987654322], [4294967295, 73]), f"Test 474 failed: got {result}, expected {([4294967296, 987654322], [4294967295, 73])}"
        print(f"Test 474 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 474 failed: {e}")
        test_results.append(False)

    # Test case 475
    try:
        result = partitionEvensOdds([4294967295, 4294967296, 0, 0])
        assert result == ([4294967296, 0, 0], [4294967295]), f"Test 475 failed: got {result}, expected {([4294967296, 0, 0], [4294967295])}"
        print(f"Test 475 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 475 failed: {e}")
        test_results.append(False)

    # Test case 476
    try:
        result = partitionEvensOdds([4294967295, 4294967296, 4294967297, 1000000000000000000])
        assert result == ([4294967296, 1000000000000000000], [4294967295, 4294967297]), f"Test 476 failed: got {result}, expected {([4294967296, 1000000000000000000], [4294967295, 4294967297])}"
        print(f"Test 476 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 476 failed: {e}")
        test_results.append(False)

    # Test case 477
    try:
        result = partitionEvensOdds([200])
        assert result == ([200], []), f"Test 477 failed: got {result}, expected {([200], [])}"
        print(f"Test 477 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 477 failed: {e}")
        test_results.append(False)

    # Test case 478
    try:
        result = partitionEvensOdds([8589934594])
        assert result == ([8589934594], []), f"Test 478 failed: got {result}, expected {([8589934594], [])}"
        print(f"Test 478 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 478 failed: {e}")
        test_results.append(False)

    # Test case 479
    try:
        result = partitionEvensOdds([4294967297, 4294967296, 4294967298])
        assert result == ([4294967296, 4294967298], [4294967297]), f"Test 479 failed: got {result}, expected {([4294967296, 4294967298], [4294967297])}"
        print(f"Test 479 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 479 failed: {e}")
        test_results.append(False)

    # Test case 480
    try:
        result = partitionEvensOdds([9, 4294967297, 4294967296, 4294967295])
        assert result == ([4294967296], [9, 4294967297, 4294967295]), f"Test 480 failed: got {result}, expected {([4294967296], [9, 4294967297, 4294967295])}"
        print(f"Test 480 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 480 failed: {e}")
        test_results.append(False)

    # Test case 481
    try:
        result = partitionEvensOdds([4294967295, 4294967296, 4294967297, 0, 0])
        assert result == ([4294967296, 0, 0], [4294967295, 4294967297]), f"Test 481 failed: got {result}, expected {([4294967296, 0, 0], [4294967295, 4294967297])}"
        print(f"Test 481 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 481 failed: {e}")
        test_results.append(False)

    # Test case 482
    try:
        result = partitionEvensOdds([0, 4294967297, 4294967297, 0])
        assert result == ([0, 0], [4294967297, 4294967297]), f"Test 482 failed: got {result}, expected {([0, 0], [4294967297, 4294967297])}"
        print(f"Test 482 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 482 failed: {e}")
        test_results.append(False)

    # Test case 483
    try:
        result = partitionEvensOdds([4294967295, 4294967296, 4294967297, 0])
        assert result == ([4294967296, 0], [4294967295, 4294967297]), f"Test 483 failed: got {result}, expected {([4294967296, 0], [4294967295, 4294967297])}"
        print(f"Test 483 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 483 failed: {e}")
        test_results.append(False)

    # Test case 484
    try:
        result = partitionEvensOdds([73, 64, 55, 46, 37, 28, 19, 10, 1, 0])
        assert result == ([64, 46, 28, 10, 0], [73, 55, 37, 19, 1]), f"Test 484 failed: got {result}, expected {([64, 46, 28, 10, 0], [73, 55, 37, 19, 1])}"
        print(f"Test 484 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 484 failed: {e}")
        test_results.append(False)

    # Test case 485
    try:
        result = partitionEvensOdds([97, 73, 64, 55, 46, 37, 28, 19, 10, 6])
        assert result == ([64, 46, 28, 10, 6], [97, 73, 55, 37, 19]), f"Test 485 failed: got {result}, expected {([64, 46, 28, 10, 6], [97, 73, 55, 37, 19])}"
        print(f"Test 485 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 485 failed: {e}")
        test_results.append(False)

    # Test case 486
    try:
        result = partitionEvensOdds([73, 55, 46, 37, 28, 19, 10, 1, 0])
        assert result == ([46, 28, 10, 0], [73, 55, 37, 19, 1]), f"Test 486 failed: got {result}, expected {([46, 28, 10, 0], [73, 55, 37, 19, 1])}"
        print(f"Test 486 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 486 failed: {e}")
        test_results.append(False)

    # Test case 487
    try:
        result = partitionEvensOdds([73, 55, 46, 37, 28, 19, 10, 1])
        assert result == ([46, 28, 10], [73, 55, 37, 19, 1]), f"Test 487 failed: got {result}, expected {([46, 28, 10], [73, 55, 37, 19, 1])}"
        print(f"Test 487 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 487 failed: {e}")
        test_results.append(False)

    # Test case 488
    try:
        result = partitionEvensOdds([0, 17, 1, 10, 19, 28, 37, 46, 55, 64, 73, 0])
        assert result == ([0, 10, 28, 46, 64, 0], [17, 1, 19, 37, 55, 73]), f"Test 488 failed: got {result}, expected {([0, 10, 28, 46, 64, 0], [17, 1, 19, 37, 55, 73])}"
        print(f"Test 488 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 488 failed: {e}")
        test_results.append(False)

    # Test case 489
    try:
        result = partitionEvensOdds([9, 1, 10, 19, 28, 37, 46, 55, 64, 73])
        assert result == ([10, 28, 46, 64], [9, 1, 19, 37, 55, 73]), f"Test 489 failed: got {result}, expected {([10, 28, 46, 64], [9, 1, 19, 37, 55, 73])}"
        print(f"Test 489 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 489 failed: {e}")
        test_results.append(False)

    # Test case 490
    try:
        result = partitionEvensOdds([73, 64, 46, 37, 28, 38, 10, 1, 0])
        assert result == ([64, 46, 28, 38, 10, 0], [73, 37, 1]), f"Test 490 failed: got {result}, expected {([64, 46, 28, 38, 10, 0], [73, 37, 1])}"
        print(f"Test 490 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 490 failed: {e}")
        test_results.append(False)

    # Test case 491
    try:
        result = partitionEvensOdds([0, 1, 10, 19, 28, 37, 46, 55, 64, 73, 25])
        assert result == ([0, 10, 28, 46, 64], [1, 19, 37, 55, 73, 25]), f"Test 491 failed: got {result}, expected {([0, 10, 28, 46, 64], [1, 19, 37, 55, 73, 25])}"
        print(f"Test 491 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 491 failed: {e}")
        test_results.append(False)

    # Test case 492
    try:
        result = partitionEvensOdds([401, 55, 46, 37, 26, 19, 10, 1])
        assert result == ([46, 26, 10], [401, 55, 37, 19, 1]), f"Test 492 failed: got {result}, expected {([46, 26, 10], [401, 55, 37, 19, 1])}"
        print(f"Test 492 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 492 failed: {e}")
        test_results.append(False)

    # Test case 493
    try:
        result = partitionEvensOdds([73, 64, 55, 46, 501, 28, 19, 10, 1, 987654321, 0, 0])
        assert result == ([64, 46, 28, 10, 0, 0], [73, 55, 501, 19, 1, 987654321]), f"Test 493 failed: got {result}, expected {([64, 46, 28, 10, 0, 0], [73, 55, 501, 19, 1, 987654321])}"
        print(f"Test 493 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 493 failed: {e}")
        test_results.append(False)

    # Test case 494
    try:
        result = partitionEvensOdds([1, 19, 28, 46, 55, 73])
        assert result == ([28, 46], [1, 19, 55, 73]), f"Test 494 failed: got {result}, expected {([28, 46], [1, 19, 55, 73])}"
        print(f"Test 494 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 494 failed: {e}")
        test_results.append(False)

    # Test case 495
    try:
        result = partitionEvensOdds([73, 64, 55, 0, 37, 19, 10, 1, 25, 0, 2])
        assert result == ([64, 0, 10, 0, 2], [73, 55, 37, 19, 1, 25]), f"Test 495 failed: got {result}, expected {([64, 0, 10, 0, 2], [73, 55, 37, 19, 1, 25])}"
        print(f"Test 495 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 495 failed: {e}")
        test_results.append(False)

    # Test case 496
    try:
        result = partitionEvensOdds([73, 64, 55, 46, 39, 28, 19, 10, 1, 0, 19])
        assert result == ([64, 46, 28, 10, 0], [73, 55, 39, 19, 1, 19]), f"Test 496 failed: got {result}, expected {([64, 46, 28, 10, 0], [73, 55, 39, 19, 1, 19])}"
        print(f"Test 496 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 496 failed: {e}")
        test_results.append(False)

    # Test case 497
    try:
        result = partitionEvensOdds([0, 11, 1, 10, 19, 28, 37, 46, 55, 64, 73])
        assert result == ([0, 10, 28, 46, 64], [11, 1, 19, 37, 55, 73]), f"Test 497 failed: got {result}, expected {([0, 10, 28, 46, 64], [11, 1, 19, 37, 55, 73])}"
        print(f"Test 497 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 497 failed: {e}")
        test_results.append(False)

    # Test case 498
    try:
        result = partitionEvensOdds([1, 10, 19, 28, 37, 46, 55, 64, 73, 0])
        assert result == ([10, 28, 46, 64, 0], [1, 19, 37, 55, 73]), f"Test 498 failed: got {result}, expected {([10, 28, 46, 64, 0], [1, 19, 37, 55, 73])}"
        print(f"Test 498 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 498 failed: {e}")
        test_results.append(False)

    # Test case 499
    try:
        result = partitionEvensOdds([1, 1, 0, 996, 0])
        assert result == ([0, 996, 0], [1, 1]), f"Test 499 failed: got {result}, expected {([0, 996, 0], [1, 1])}"
        print(f"Test 499 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 499 failed: {e}")
        test_results.append(False)

    # Test case 500
    try:
        result = partitionEvensOdds([1, 1, 0, 42])
        assert result == ([0, 42], [1, 1]), f"Test 500 failed: got {result}, expected {([0, 42], [1, 1])}"
        print(f"Test 500 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 500 failed: {e}")
        test_results.append(False)

    # Test case 501
    try:
        result = partitionEvensOdds([1, 1, 24, 23, 0, 0])
        assert result == ([24, 0, 0], [1, 1, 23]), f"Test 501 failed: got {result}, expected {([24, 0, 0], [1, 1, 23])}"
        print(f"Test 501 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 501 failed: {e}")
        test_results.append(False)

    # Test case 502
    try:
        result = partitionEvensOdds([1, 1000, 105])
        assert result == ([1000], [1, 105]), f"Test 502 failed: got {result}, expected {([1000], [1, 105])}"
        print(f"Test 502 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 502 failed: {e}")
        test_results.append(False)

    # Test case 503
    try:
        result = partitionEvensOdds([1, 34, 24, 998])
        assert result == ([34, 24, 998], [1]), f"Test 503 failed: got {result}, expected {([34, 24, 998], [1])}"
        print(f"Test 503 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 503 failed: {e}")
        test_results.append(False)

    # Test case 504
    try:
        result = partitionEvensOdds([1, 1, 0])
        assert result == ([0], [1, 1]), f"Test 504 failed: got {result}, expected {([0], [1, 1])}"
        print(f"Test 504 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 504 failed: {e}")
        test_results.append(False)

    # Test case 505
    try:
        result = partitionEvensOdds([0, 1, 1])
        assert result == ([0], [1, 1]), f"Test 505 failed: got {result}, expected {([0], [1, 1])}"
        print(f"Test 505 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 505 failed: {e}")
        test_results.append(False)

    # Test case 506
    try:
        result = partitionEvensOdds([99])
        assert result == ([], [99]), f"Test 506 failed: got {result}, expected {([], [99])}"
        print(f"Test 506 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 506 failed: {e}")
        test_results.append(False)

    # Test case 507
    try:
        result = partitionEvensOdds([2, 0, 2, 4, 0])
        assert result == ([2, 0, 2, 4, 0], []), f"Test 507 failed: got {result}, expected {([2, 0, 2, 4, 0], [])}"
        print(f"Test 507 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 507 failed: {e}")
        test_results.append(False)

    # Test case 508
    try:
        result = partitionEvensOdds([4, 1, 0, 0, 16, 15])
        assert result == ([4, 0, 0, 16], [1, 15]), f"Test 508 failed: got {result}, expected {([4, 0, 0, 16], [1, 15])}"
        print(f"Test 508 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 508 failed: {e}")
        test_results.append(False)

    # Test case 509
    try:
        result = partitionEvensOdds([0, 0, 104, 4, 0])
        assert result == ([0, 0, 104, 4, 0], []), f"Test 509 failed: got {result}, expected {([0, 0, 104, 4, 0], [])}"
        print(f"Test 509 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 509 failed: {e}")
        test_results.append(False)

    # Test case 510
    try:
        result = partitionEvensOdds([0, 0, 2, 4, 27])
        assert result == ([0, 0, 2, 4], [27]), f"Test 510 failed: got {result}, expected {([0, 0, 2, 4], [27])}"
        print(f"Test 510 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 510 failed: {e}")
        test_results.append(False)

    # Test case 511
    try:
        result = partitionEvensOdds([0, 0, 2, 4, 0, 987654322, 0])
        assert result == ([0, 0, 2, 4, 0, 987654322, 0], []), f"Test 511 failed: got {result}, expected {([0, 0, 2, 4, 0, 987654322, 0], [])}"
        print(f"Test 511 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 511 failed: {e}")
        test_results.append(False)

    # Test case 512
    try:
        result = partitionEvensOdds([4, 37, 997])
        assert result == ([4], [37, 997]), f"Test 512 failed: got {result}, expected {([4], [37, 997])}"
        print(f"Test 512 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 512 failed: {e}")
        test_results.append(False)

    # Test case 513
    try:
        result = partitionEvensOdds([4, 2, 0, 222222222])
        assert result == ([4, 2, 0, 222222222], []), f"Test 513 failed: got {result}, expected {([4, 2, 0, 222222222], [])}"
        print(f"Test 513 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 513 failed: {e}")
        test_results.append(False)

    # Test case 514
    try:
        result = partitionEvensOdds([0, 0, 2, 4, 0])
        assert result == ([0, 0, 2, 4, 0], []), f"Test 514 failed: got {result}, expected {([0, 0, 2, 4, 0], [])}"
        print(f"Test 514 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 514 failed: {e}")
        test_results.append(False)

    # Test case 515
    try:
        result = partitionEvensOdds([0, 0, 4, 0, 0])
        assert result == ([0, 0, 4, 0, 0], []), f"Test 515 failed: got {result}, expected {([0, 0, 4, 0, 0], [])}"
        print(f"Test 515 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 515 failed: {e}")
        test_results.append(False)

    # Test case 516
    try:
        result = partitionEvensOdds([0, 2, 4, 222222222, 0])
        assert result == ([0, 2, 4, 222222222, 0], []), f"Test 516 failed: got {result}, expected {([0, 2, 4, 222222222, 0], [])}"
        print(f"Test 516 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 516 failed: {e}")
        test_results.append(False)

    # Test case 517
    try:
        result = partitionEvensOdds([0, 0, 1001])
        assert result == ([0, 0], [1001]), f"Test 517 failed: got {result}, expected {([0, 0], [1001])}"
        print(f"Test 517 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 517 failed: {e}")
        test_results.append(False)

    # Test case 518
    try:
        result = partitionEvensOdds([0, 0, 4])
        assert result == ([0, 0, 4], []), f"Test 518 failed: got {result}, expected {([0, 0, 4], [])}"
        print(f"Test 518 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 518 failed: {e}")
        test_results.append(False)

    # Test case 519
    try:
        result = partitionEvensOdds([24, 2, 1, 0])
        assert result == ([24, 2, 0], [1]), f"Test 519 failed: got {result}, expected {([24, 2, 0], [1])}"
        print(f"Test 519 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 519 failed: {e}")
        test_results.append(False)

    # Test case 520
    try:
        result = partitionEvensOdds([0, 0, 2, 4, 0, 0, 0, 1000000000000000000])
        assert result == ([0, 0, 2, 4, 0, 0, 0, 1000000000000000000], []), f"Test 520 failed: got {result}, expected {([0, 0, 2, 4, 0, 0, 0, 1000000000000000000], [])}"
        print(f"Test 520 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 520 failed: {e}")
        test_results.append(False)

    # Test case 521
    try:
        result = partitionEvensOdds([4, 2, 3, 0, 0])
        assert result == ([4, 2, 0, 0], [3]), f"Test 521 failed: got {result}, expected {([4, 2, 0, 0], [3])}"
        print(f"Test 521 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 521 failed: {e}")
        test_results.append(False)

    # Test case 522
    try:
        result = partitionEvensOdds([7, 3])
        assert result == ([], [7, 3]), f"Test 522 failed: got {result}, expected {([], [7, 3])}"
        print(f"Test 522 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 522 failed: {e}")
        test_results.append(False)

    # Test case 523
    try:
        result = partitionEvensOdds([3, 6, 3, 7, 0, 14])
        assert result == ([6, 0, 14], [3, 3, 7]), f"Test 523 failed: got {result}, expected {([6, 0, 14], [3, 3, 7])}"
        print(f"Test 523 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 523 failed: {e}")
        test_results.append(False)

    # Test case 524
    try:
        result = partitionEvensOdds([3, 3, 7, 50, 0, 0, 4])
        assert result == ([50, 0, 0, 4], [3, 3, 7]), f"Test 524 failed: got {result}, expected {([50, 0, 0, 4], [3, 3, 7])}"
        print(f"Test 524 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 524 failed: {e}")
        test_results.append(False)

    # Test case 525
    try:
        result = partitionEvensOdds([3, 5, 40, 0])
        assert result == ([40, 0], [3, 5]), f"Test 525 failed: got {result}, expected {([40, 0], [3, 5])}"
        print(f"Test 525 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 525 failed: {e}")
        test_results.append(False)

    # Test case 526
    try:
        result = partitionEvensOdds([55, 32, 7])
        assert result == ([32], [55, 7]), f"Test 526 failed: got {result}, expected {([32], [55, 7])}"
        print(f"Test 526 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 526 failed: {e}")
        test_results.append(False)

    # Test case 527
    try:
        result = partitionEvensOdds([3, 5, 3, 7, 9, 0, 0])
        assert result == ([0, 0], [3, 5, 3, 7, 9]), f"Test 527 failed: got {result}, expected {([0, 0], [3, 5, 3, 7, 9])}"
        print(f"Test 527 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 527 failed: {e}")
        test_results.append(False)

    # Test case 528
    try:
        result = partitionEvensOdds([64, 5, 3, 7, 3, 0, 0])
        assert result == ([64, 0, 0], [5, 3, 7, 3]), f"Test 528 failed: got {result}, expected {([64, 0, 0], [5, 3, 7, 3])}"
        print(f"Test 528 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 528 failed: {e}")
        test_results.append(False)

    # Test case 529
    try:
        result = partitionEvensOdds([7, 3, 2])
        assert result == ([2], [7, 3]), f"Test 529 failed: got {result}, expected {([2], [7, 3])}"
        print(f"Test 529 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 529 failed: {e}")
        test_results.append(False)

    # Test case 530
    try:
        result = partitionEvensOdds([3, 5, 28, 0])
        assert result == ([28, 0], [3, 5]), f"Test 530 failed: got {result}, expected {([28, 0], [3, 5])}"
        print(f"Test 530 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 530 failed: {e}")
        test_results.append(False)

    # Test case 531
    try:
        result = partitionEvensOdds([0, 7, 5, 0])
        assert result == ([0, 0], [7, 5]), f"Test 531 failed: got {result}, expected {([0, 0], [7, 5])}"
        print(f"Test 531 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 531 failed: {e}")
        test_results.append(False)

    # Test case 532
    try:
        result = partitionEvensOdds([3, 5, 3, 7, 0])
        assert result == ([0], [3, 5, 3, 7]), f"Test 532 failed: got {result}, expected {([0], [3, 5, 3, 7])}"
        print(f"Test 532 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 532 failed: {e}")
        test_results.append(False)

    # Test case 533
    try:
        result = partitionEvensOdds([0, 401, 0, 7, 3, 5, 3])
        assert result == ([0, 0], [401, 7, 3, 5, 3]), f"Test 533 failed: got {result}, expected {([0, 0], [401, 7, 3, 5, 3])}"
        print(f"Test 533 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 533 failed: {e}")
        test_results.append(False)

    # Test case 534
    try:
        result = partitionEvensOdds([7, 3, 3, 0, 997])
        assert result == ([0], [7, 3, 3, 997]), f"Test 534 failed: got {result}, expected {([0], [7, 3, 3, 997])}"
        print(f"Test 534 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 534 failed: {e}")
        test_results.append(False)

    # Test case 535
    try:
        result = partitionEvensOdds([3, 5, 3, 97])
        assert result == ([], [3, 5, 3, 97]), f"Test 535 failed: got {result}, expected {([], [3, 5, 3, 97])}"
        print(f"Test 535 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 535 failed: {e}")
        test_results.append(False)

    # Test case 536
    try:
        result = partitionEvensOdds([8, 6, 6, 4, 2, 0])
        assert result == ([8, 6, 6, 4, 2, 0], []), f"Test 536 failed: got {result}, expected {([8, 6, 6, 4, 2, 0], [])}"
        print(f"Test 536 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 536 failed: {e}")
        test_results.append(False)

    # Test case 537
    try:
        result = partitionEvensOdds([2, 4, 6, 6, 8, 17])
        assert result == ([2, 4, 6, 6, 8], [17]), f"Test 537 failed: got {result}, expected {([2, 4, 6, 6, 8], [17])}"
        print(f"Test 537 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 537 failed: {e}")
        test_results.append(False)

    # Test case 538
    try:
        result = partitionEvensOdds([2, 4, 6, 6, 997, 26])
        assert result == ([2, 4, 6, 6, 26], [997]), f"Test 538 failed: got {result}, expected {([2, 4, 6, 6, 26], [997])}"
        print(f"Test 538 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 538 failed: {e}")
        test_results.append(False)

    # Test case 539
    try:
        result = partitionEvensOdds([4, 6, 6, 8, 0, 38])
        assert result == ([4, 6, 6, 8, 0, 38], []), f"Test 539 failed: got {result}, expected {([4, 6, 6, 8, 0, 38], [])}"
        print(f"Test 539 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 539 failed: {e}")
        test_results.append(False)

    # Test case 540
    try:
        result = partitionEvensOdds([2, 4, 6, 6, 8, 0])
        assert result == ([2, 4, 6, 6, 8, 0], []), f"Test 540 failed: got {result}, expected {([2, 4, 6, 6, 8, 0], [])}"
        print(f"Test 540 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 540 failed: {e}")
        test_results.append(False)

    # Test case 541
    try:
        result = partitionEvensOdds([8, 6, 6])
        assert result == ([8, 6, 6], []), f"Test 541 failed: got {result}, expected {([8, 6, 6], [])}"
        print(f"Test 541 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 541 failed: {e}")
        test_results.append(False)

    # Test case 542
    try:
        result = partitionEvensOdds([8, 6, 6, 4, 2, 101])
        assert result == ([8, 6, 6, 4, 2], [101]), f"Test 542 failed: got {result}, expected {([8, 6, 6, 4, 2], [101])}"
        print(f"Test 542 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 542 failed: {e}")
        test_results.append(False)

    # Test case 543
    try:
        result = partitionEvensOdds([10, 8, 6, 6, 103])
        assert result == ([10, 8, 6, 6], [103]), f"Test 543 failed: got {result}, expected {([10, 8, 6, 6], [103])}"
        print(f"Test 543 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 543 failed: {e}")
        test_results.append(False)

    # Test case 544
    try:
        result = partitionEvensOdds([0, 2, 4, 6, 6, 8, 0])
        assert result == ([0, 2, 4, 6, 6, 8, 0], []), f"Test 544 failed: got {result}, expected {([0, 2, 4, 6, 6, 8, 0], [])}"
        print(f"Test 544 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 544 failed: {e}")
        test_results.append(False)

    # Test case 545
    try:
        result = partitionEvensOdds([2, 4, 6, 6, 8, 601, 0, 4294967295])
        assert result == ([2, 4, 6, 6, 8, 0], [601, 4294967295]), f"Test 545 failed: got {result}, expected {([2, 4, 6, 6, 8, 0], [601, 4294967295])}"
        print(f"Test 545 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 545 failed: {e}")
        test_results.append(False)

    # Test case 546
    try:
        result = partitionEvensOdds([10, 12, 6, 4, 2, 0, 0])
        assert result == ([10, 12, 6, 4, 2, 0, 0], []), f"Test 546 failed: got {result}, expected {([10, 12, 6, 4, 2, 0, 0], [])}"
        print(f"Test 546 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 546 failed: {e}")
        test_results.append(False)

    # Test case 547
    try:
        result = partitionEvensOdds([0, 0, 101, 8, 6, 6, 4])
        assert result == ([0, 0, 8, 6, 6, 4], [101]), f"Test 547 failed: got {result}, expected {([0, 0, 8, 6, 6, 4], [101])}"
        print(f"Test 547 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 547 failed: {e}")
        test_results.append(False)

    # Test case 548
    try:
        result = partitionEvensOdds([0, 8, 6, 3, 3])
        assert result == ([0, 8, 6], [3, 3]), f"Test 548 failed: got {result}, expected {([0, 8, 6], [3, 3])}"
        print(f"Test 548 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 548 failed: {e}")
        test_results.append(False)

    # Test case 549
    try:
        result = partitionEvensOdds([9, 8, 9, 105])
        assert result == ([8], [9, 9, 105]), f"Test 549 failed: got {result}, expected {([8], [9, 9, 105])}"
        print(f"Test 549 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 549 failed: {e}")
        test_results.append(False)

    # Test case 550
    try:
        result = partitionEvensOdds([9, 7, 8, 9])
        assert result == ([8], [9, 7, 9]), f"Test 550 failed: got {result}, expected {([8], [9, 7, 9])}"
        print(f"Test 550 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 550 failed: {e}")
        test_results.append(False)

    # Test case 551
    try:
        result = partitionEvensOdds([9, 8, 7, 8, 9, 0])
        assert result == ([8, 8, 0], [9, 7, 9]), f"Test 551 failed: got {result}, expected {([8, 8, 0], [9, 7, 9])}"
        print(f"Test 551 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 551 failed: {e}")
        test_results.append(False)

    # Test case 552
    try:
        result = partitionEvensOdds([9, 8, 7, 8, 9, 14])
        assert result == ([8, 8, 14], [9, 7, 9]), f"Test 552 failed: got {result}, expected {([8, 8, 14], [9, 7, 9])}"
        print(f"Test 552 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 552 failed: {e}")
        test_results.append(False)

    # Test case 553
    try:
        result = partitionEvensOdds([9, 8, 7, 9, 112])
        assert result == ([8, 112], [9, 7, 9]), f"Test 553 failed: got {result}, expected {([8, 112], [9, 7, 9])}"
        print(f"Test 553 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 553 failed: {e}")
        test_results.append(False)

    # Test case 554
    try:
        result = partitionEvensOdds([0, 9, 7, 8])
        assert result == ([0, 8], [9, 7]), f"Test 554 failed: got {result}, expected {([0, 8], [9, 7])}"
        print(f"Test 554 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 554 failed: {e}")
        test_results.append(False)

    # Test case 555
    try:
        result = partitionEvensOdds([9, 8, 7, 9, 0, 0, 42])
        assert result == ([8, 0, 0, 42], [9, 7, 9]), f"Test 555 failed: got {result}, expected {([8, 0, 0, 42], [9, 7, 9])}"
        print(f"Test 555 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 555 failed: {e}")
        test_results.append(False)

    # Test case 556
    try:
        result = partitionEvensOdds([9, 8, 7, 8, 12, 37, 4, 0])
        assert result == ([8, 8, 12, 4, 0], [9, 7, 37]), f"Test 556 failed: got {result}, expected {([8, 8, 12, 4, 0], [9, 7, 37])}"
        print(f"Test 556 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 556 failed: {e}")
        test_results.append(False)

    # Test case 557
    try:
        result = partitionEvensOdds([997, 100, 7, 8, 9])
        assert result == ([100, 8], [997, 7, 9]), f"Test 557 failed: got {result}, expected {([100, 8], [997, 7, 9])}"
        print(f"Test 557 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 557 failed: {e}")
        test_results.append(False)

    # Test case 558
    try:
        result = partitionEvensOdds([9, 8, 7, 9])
        assert result == ([8], [9, 7, 9]), f"Test 558 failed: got {result}, expected {([8], [9, 7, 9])}"
        print(f"Test 558 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 558 failed: {e}")
        test_results.append(False)

    # Test case 559
    try:
        result = partitionEvensOdds([9, 8, 7, 16, 9, 9, 97])
        assert result == ([8, 16], [9, 7, 9, 9, 97]), f"Test 559 failed: got {result}, expected {([8, 16], [9, 7, 9, 9, 97])}"
        print(f"Test 559 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 559 failed: {e}")
        test_results.append(False)

    # Test case 560
    try:
        result = partitionEvensOdds([9, 8, 7, 8, 9, 222222222])
        assert result == ([8, 8, 222222222], [9, 7, 9]), f"Test 560 failed: got {result}, expected {([8, 8, 222222222], [9, 7, 9])}"
        print(f"Test 560 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 560 failed: {e}")
        test_results.append(False)

    # Test case 561
    try:
        result = partitionEvensOdds([222222222, 987654321, 9, 8, 7, 8, 9])
        assert result == ([222222222, 8, 8], [987654321, 9, 7, 9]), f"Test 561 failed: got {result}, expected {([222222222, 8, 8], [987654321, 9, 7, 9])}"
        print(f"Test 561 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 561 failed: {e}")
        test_results.append(False)

    # Test case 562
    try:
        result = partitionEvensOdds([4294967296, 8, 7, 501, 9])
        assert result == ([4294967296, 8], [7, 501, 9]), f"Test 562 failed: got {result}, expected {([4294967296, 8], [7, 501, 9])}"
        print(f"Test 562 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 562 failed: {e}")
        test_results.append(False)

    # Test case 563
    try:
        result = partitionEvensOdds([0, 0, 10, 13, 12, 11, 10])
        assert result == ([0, 0, 10, 12, 10], [13, 11]), f"Test 563 failed: got {result}, expected {([0, 0, 10, 12, 10], [13, 11])}"
        print(f"Test 563 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 563 failed: {e}")
        test_results.append(False)

    # Test case 564
    try:
        result = partitionEvensOdds([124, 13, 13, 11, 10])
        assert result == ([124, 10], [13, 13, 11]), f"Test 564 failed: got {result}, expected {([124, 10], [13, 13, 11])}"
        print(f"Test 564 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 564 failed: {e}")
        test_results.append(False)

    # Test case 565
    try:
        result = partitionEvensOdds([987654321, 10, 13, 12, 11])
        assert result == ([10, 12], [987654321, 13, 11]), f"Test 565 failed: got {result}, expected {([10, 12], [987654321, 13, 11])}"
        print(f"Test 565 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 565 failed: {e}")
        test_results.append(False)

    # Test case 566
    try:
        result = partitionEvensOdds([10, 12, 11, 10, 62])
        assert result == ([10, 12, 10, 62], [11]), f"Test 566 failed: got {result}, expected {([10, 12, 10, 62], [11])}"
        print(f"Test 566 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 566 failed: {e}")
        test_results.append(False)

    # Test case 567
    try:
        result = partitionEvensOdds([10, 13, 12, 11, 10])
        assert result == ([10, 12, 10], [13, 11]), f"Test 567 failed: got {result}, expected {([10, 12, 10], [13, 11])}"
        print(f"Test 567 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 567 failed: {e}")
        test_results.append(False)

    # Test case 568
    try:
        result = partitionEvensOdds([10, 13, 12, 11, 9, 999999938, 0, 0])
        assert result == ([10, 12, 999999938, 0, 0], [13, 11, 9]), f"Test 568 failed: got {result}, expected {([10, 12, 999999938, 0, 0], [13, 11, 9])}"
        print(f"Test 568 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 568 failed: {e}")
        test_results.append(False)

    # Test case 569
    try:
        result = partitionEvensOdds([10, 222222222, 12, 13, 10, 1001])
        assert result == ([10, 222222222, 12, 10], [13, 1001]), f"Test 569 failed: got {result}, expected {([10, 222222222, 12, 10], [13, 1001])}"
        print(f"Test 569 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 569 failed: {e}")
        test_results.append(False)

    # Test case 570
    try:
        result = partitionEvensOdds([11, 12, 13, 10, 401])
        assert result == ([12, 10], [11, 13, 401]), f"Test 570 failed: got {result}, expected {([12, 10], [11, 13, 401])}"
        print(f"Test 570 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 570 failed: {e}")
        test_results.append(False)

    # Test case 571
    try:
        result = partitionEvensOdds([601, 0, 10, 13, 12, 11, 0])
        assert result == ([0, 10, 12, 0], [601, 13, 11]), f"Test 571 failed: got {result}, expected {([0, 10, 12, 0], [601, 13, 11])}"
        print(f"Test 571 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 571 failed: {e}")
        test_results.append(False)

    # Test case 572
    try:
        result = partitionEvensOdds([10, 12, 13, 10, 0, 0])
        assert result == ([10, 12, 10, 0, 0], [13]), f"Test 572 failed: got {result}, expected {([10, 12, 10, 0, 0], [13])}"
        print(f"Test 572 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 572 failed: {e}")
        test_results.append(False)

    # Test case 573
    try:
        result = partitionEvensOdds([89, 11, 12, 13])
        assert result == ([12], [89, 11, 13]), f"Test 573 failed: got {result}, expected {([12], [89, 11, 13])}"
        print(f"Test 573 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 573 failed: {e}")
        test_results.append(False)

    # Test case 574
    try:
        result = partitionEvensOdds([10, 11, 12, 13, 10, 1000000000000000000, 12])
        assert result == ([10, 12, 10, 1000000000000000000, 12], [11, 13]), f"Test 574 failed: got {result}, expected {([10, 12, 10, 1000000000000000000, 12], [11, 13])}"
        print(f"Test 574 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 574 failed: {e}")
        test_results.append(False)

    # Test case 575
    try:
        result = partitionEvensOdds([2, 10, 13, 12, 11, 26])
        assert result == ([2, 10, 12, 26], [13, 11]), f"Test 575 failed: got {result}, expected {([2, 10, 12, 26], [13, 11])}"
        print(f"Test 575 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 575 failed: {e}")
        test_results.append(False)

    # Test case 576
    try:
        result = partitionEvensOdds([0, 18, 13, 12, 11, 10])
        assert result == ([0, 18, 12, 10], [13, 11]), f"Test 576 failed: got {result}, expected {([0, 18, 12, 10], [13, 11])}"
        print(f"Test 576 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 576 failed: {e}")
        test_results.append(False)

    # Test case 577
    try:
        result = partitionEvensOdds([10, 11, 12, 13, 10, 0, 15, 0, 0])
        assert result == ([10, 12, 10, 0, 0, 0], [11, 13, 15]), f"Test 577 failed: got {result}, expected {([10, 12, 10, 0, 0, 0], [11, 13, 15])}"
        print(f"Test 577 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 577 failed: {e}")
        test_results.append(False)

    # Test case 578
    try:
        result = partitionEvensOdds([0, 42, 4294967296])
        assert result == ([0, 42, 4294967296], []), f"Test 578 failed: got {result}, expected {([0, 42, 4294967296], [])}"
        print(f"Test 578 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 578 failed: {e}")
        test_results.append(False)

    # Test case 579
    try:
        result = partitionEvensOdds([0, 30, 42, 0])
        assert result == ([0, 30, 42, 0], []), f"Test 579 failed: got {result}, expected {([0, 30, 42, 0], [])}"
        print(f"Test 579 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 579 failed: {e}")
        test_results.append(False)

    # Test case 580
    try:
        result = partitionEvensOdds([73, 42])
        assert result == ([42], [73]), f"Test 580 failed: got {result}, expected {([42], [73])}"
        print(f"Test 580 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 580 failed: {e}")
        test_results.append(False)

    # Test case 581
    try:
        result = partitionEvensOdds([42, 1999999874, 42])
        assert result == ([42, 1999999874, 42], []), f"Test 581 failed: got {result}, expected {([42, 1999999874, 42], [])}"
        print(f"Test 581 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 581 failed: {e}")
        test_results.append(False)

    # Test case 582
    try:
        result = partitionEvensOdds([42, 99])
        assert result == ([42], [99]), f"Test 582 failed: got {result}, expected {([42], [99])}"
        print(f"Test 582 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 582 failed: {e}")
        test_results.append(False)

    # Test case 583
    try:
        result = partitionEvensOdds([42, 42])
        assert result == ([42, 42], []), f"Test 583 failed: got {result}, expected {([42, 42], [])}"
        print(f"Test 583 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 583 failed: {e}")
        test_results.append(False)

    # Test case 584
    try:
        result = partitionEvensOdds([42, 42, 0, 0, 0])
        assert result == ([42, 42, 0, 0, 0], []), f"Test 584 failed: got {result}, expected {([42, 42, 0, 0, 0], [])}"
        print(f"Test 584 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 584 failed: {e}")
        test_results.append(False)

    # Test case 585
    try:
        result = partitionEvensOdds([0, 0, 42, 0])
        assert result == ([0, 0, 42, 0], []), f"Test 585 failed: got {result}, expected {([0, 0, 42, 0], [])}"
        print(f"Test 585 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 585 failed: {e}")
        test_results.append(False)

    # Test case 586
    try:
        result = partitionEvensOdds([42, 0, 42])
        assert result == ([42, 0, 42], []), f"Test 586 failed: got {result}, expected {([42, 0, 42], [])}"
        print(f"Test 586 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 586 failed: {e}")
        test_results.append(False)

    # Test case 587
    try:
        result = partitionEvensOdds([10, 42, 42, 42, 56])
        assert result == ([10, 42, 42, 42, 56], []), f"Test 587 failed: got {result}, expected {([10, 42, 42, 42, 56], [])}"
        print(f"Test 587 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 587 failed: {e}")
        test_results.append(False)

    # Test case 588
    try:
        result = partitionEvensOdds([0, 42, 42, 41])
        assert result == ([0, 42, 42], [41]), f"Test 588 failed: got {result}, expected {([0, 42, 42], [41])}"
        print(f"Test 588 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 588 failed: {e}")
        test_results.append(False)

    # Test case 589
    try:
        result = partitionEvensOdds([43])
        assert result == ([], [43]), f"Test 589 failed: got {result}, expected {([], [43])}"
        print(f"Test 589 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 589 failed: {e}")
        test_results.append(False)

    # Test case 590
    try:
        result = partitionEvensOdds([42, 42, 44, 401])
        assert result == ([42, 42, 44], [401]), f"Test 590 failed: got {result}, expected {([42, 42, 44], [401])}"
        print(f"Test 590 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 590 failed: {e}")
        test_results.append(False)

    # Test case 591
    try:
        result = partitionEvensOdds([0, 43, 0, 42, 42, 42, 42])
        assert result == ([0, 0, 42, 42, 42, 42], [43]), f"Test 591 failed: got {result}, expected {([0, 0, 42, 42, 42, 42], [43])}"
        print(f"Test 591 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 591 failed: {e}")
        test_results.append(False)

    # Test case 592
    try:
        result = partitionEvensOdds([42, 0])
        assert result == ([42, 0], []), f"Test 592 failed: got {result}, expected {([42, 0], [])}"
        print(f"Test 592 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 592 failed: {e}")
        test_results.append(False)

    # Test case 593
    try:
        result = partitionEvensOdds([0, 1, 2, 4, 2, 1, 0, 0])
        assert result == ([0, 2, 4, 2, 0, 0], [1, 1]), f"Test 593 failed: got {result}, expected {([0, 2, 4, 2, 0, 0], [1, 1])}"
        print(f"Test 593 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 593 failed: {e}")
        test_results.append(False)

    # Test case 594
    try:
        result = partitionEvensOdds([0, 1, 2, 3, 2, 1, 14])
        assert result == ([0, 2, 2, 14], [1, 3, 1]), f"Test 594 failed: got {result}, expected {([0, 2, 2, 14], [1, 3, 1])}"
        print(f"Test 594 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 594 failed: {e}")
        test_results.append(False)

    # Test case 595
    try:
        result = partitionEvensOdds([0, 0, 1, 2, 3, 2, 1, 0])
        assert result == ([0, 0, 2, 2, 0], [1, 3, 1]), f"Test 595 failed: got {result}, expected {([0, 0, 2, 2, 0], [1, 3, 1])}"
        print(f"Test 595 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 595 failed: {e}")
        test_results.append(False)

    # Test case 596
    try:
        result = partitionEvensOdds([0, 2, 2, 1, 0, 0, 99])
        assert result == ([0, 2, 2, 0, 0], [1, 99]), f"Test 596 failed: got {result}, expected {([0, 2, 2, 0, 0], [1, 99])}"
        print(f"Test 596 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 596 failed: {e}")
        test_results.append(False)

    # Test case 597
    try:
        result = partitionEvensOdds([0, 0, 2, 3, 2, 1, 0, 0, 18])
        assert result == ([0, 0, 2, 2, 0, 0, 18], [3, 1]), f"Test 597 failed: got {result}, expected {([0, 0, 2, 2, 0, 0, 18], [3, 1])}"
        print(f"Test 597 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 597 failed: {e}")
        test_results.append(False)

    # Test case 598
    try:
        result = partitionEvensOdds([0, 1, 3, 2, 1, 0, 14])
        assert result == ([0, 2, 0, 14], [1, 3, 1]), f"Test 598 failed: got {result}, expected {([0, 2, 0, 14], [1, 3, 1])}"
        print(f"Test 598 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 598 failed: {e}")
        test_results.append(False)

    # Test case 599
    try:
        result = partitionEvensOdds([0, 2, 2, 0, 0])
        assert result == ([0, 2, 2, 0, 0], []), f"Test 599 failed: got {result}, expected {([0, 2, 2, 0, 0], [])}"
        print(f"Test 599 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 599 failed: {e}")
        test_results.append(False)

    # Test case 600
    try:
        result = partitionEvensOdds([0, 1, 3, 2, 1, 0, 0])
        assert result == ([0, 2, 0, 0], [1, 3, 1]), f"Test 600 failed: got {result}, expected {([0, 2, 0, 0], [1, 3, 1])}"
        print(f"Test 600 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 600 failed: {e}")
        test_results.append(False)

    # Test case 601
    try:
        result = partitionEvensOdds([0, 3, 3, 2, 1, 0, 0])
        assert result == ([0, 2, 0, 0], [3, 3, 1]), f"Test 601 failed: got {result}, expected {([0, 2, 0, 0], [3, 3, 1])}"
        print(f"Test 601 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 601 failed: {e}")
        test_results.append(False)

    # Test case 602
    try:
        result = partitionEvensOdds([0, 1, 222222222, 2, 1, 0, 0])
        assert result == ([0, 222222222, 2, 0, 0], [1, 1]), f"Test 602 failed: got {result}, expected {([0, 222222222, 2, 0, 0], [1, 1])}"
        print(f"Test 602 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 602 failed: {e}")
        test_results.append(False)

    # Test case 603
    try:
        result = partitionEvensOdds([0, 1, 2, 3, 2, 1, 0, 0])
        assert result == ([0, 2, 2, 0, 0], [1, 3, 1]), f"Test 603 failed: got {result}, expected {([0, 2, 2, 0, 0], [1, 3, 1])}"
        print(f"Test 603 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 603 failed: {e}")
        test_results.append(False)

    # Test case 604
    try:
        result = partitionEvensOdds([0, 1, 2, 3, 2, 1, 0, 100, 0])
        assert result == ([0, 2, 2, 0, 100, 0], [1, 3, 1]), f"Test 604 failed: got {result}, expected {([0, 2, 2, 0, 100, 0], [1, 3, 1])}"
        print(f"Test 604 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 604 failed: {e}")
        test_results.append(False)

    # Test case 605
    try:
        result = partitionEvensOdds([0, 1, 0, 2, 1, 0])
        assert result == ([0, 0, 2, 0], [1, 1]), f"Test 605 failed: got {result}, expected {([0, 0, 2, 0], [1, 1])}"
        print(f"Test 605 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 605 failed: {e}")
        test_results.append(False)

    # Test case 606
    try:
        result = partitionEvensOdds([0, 1, 2, 3, 2, 0, 501, 0])
        assert result == ([0, 2, 2, 0, 0], [1, 3, 501]), f"Test 606 failed: got {result}, expected {([0, 2, 2, 0, 0], [1, 3, 501])}"
        print(f"Test 606 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 606 failed: {e}")
        test_results.append(False)

    # Test case 607
    try:
        result = partitionEvensOdds([0, 62, 2, 3, 2, 1, 0, 26, 0])
        assert result == ([0, 62, 2, 2, 0, 26, 0], [3, 1]), f"Test 607 failed: got {result}, expected {([0, 62, 2, 2, 0, 26, 0], [3, 1])}"
        print(f"Test 607 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 607 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
