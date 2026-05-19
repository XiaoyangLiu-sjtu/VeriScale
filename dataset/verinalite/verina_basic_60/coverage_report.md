# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def FindEvenNumbers(arr):
2: ✓     return [x for x in arr if x % 2 == 0]
```

## Complete Test File

```python
def FindEvenNumbers(arr):
    return [x for x in arr if x % 2 == 0]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = FindEvenNumbers([1, 2, 3, 4, 5, 6])
        assert result == [2, 4, 6], f"Test 1 failed: got {result}, expected {[2, 4, 6]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = FindEvenNumbers([0, -2, 3, -4, 7])
        assert result == [0, -2, -4], f"Test 2 failed: got {result}, expected {[0, -2, -4]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = FindEvenNumbers([1, 3, 5, 7])
        assert result == [], f"Test 3 failed: got {result}, expected {[]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = FindEvenNumbers([2, 4, 8, 10])
        assert result == [2, 4, 8, 10], f"Test 4 failed: got {result}, expected {[2, 4, 8, 10]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = FindEvenNumbers([])
        assert result == [], f"Test 5 failed: got {result}, expected {[]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = FindEvenNumbers([2, 4, 2, 6])
        assert result == [2, 4, 2, 6], f"Test 6 failed: got {result}, expected {[2, 4, 2, 6]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = FindEvenNumbers([1, 2, 8, 2, 5])
        assert result == [2, 8, 2], f"Test 7 failed: got {result}, expected {[2, 8, 2]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = FindEvenNumbers([2, 1, 4, 3, 6, 5, 8, 7])
        assert result == [2, 4, 6, 8], f"Test 8 failed: got {result}, expected {[2, 4, 6, 8]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = FindEvenNumbers([-10, -9, -8, -7, -6, -5])
        assert result == [-10, -8, -6], f"Test 9 failed: got {result}, expected {[-10, -8, -6]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = FindEvenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        assert result == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], f"Test 10 failed: got {result}, expected {[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = FindEvenNumbers([-2, -4, -6, -8, -10, -12, -14, -16])
        assert result == [-2, -4, -6, -8, -10, -12, -14, -16], f"Test 11 failed: got {result}, expected {[-2, -4, -6, -8, -10, -12, -14, -16]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = FindEvenNumbers([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert result == [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10], f"Test 12 failed: got {result}, expected {[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = FindEvenNumbers([-2147483648, 2147483647, 2147483646, -2147483647])
        assert result == [-2147483648, 2147483646], f"Test 13 failed: got {result}, expected {[-2147483648, 2147483646]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = FindEvenNumbers([-1001, 1002, -1003, 1004, -1005, 1006])
        assert result == [1002, 1004, 1006], f"Test 14 failed: got {result}, expected {[1002, 1004, 1006]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = FindEvenNumbers([2, 4, 5, 6, 0])
        assert result == [2, 4, 6, 0], f"Test 15 failed: got {result}, expected {[2, 4, 6, 0]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = FindEvenNumbers([2147483647, 65, -2, 0])
        assert result == [-2, 0], f"Test 16 failed: got {result}, expected {[-2, 0]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = FindEvenNumbers([7, -4, 3, -2, -1])
        assert result == [-4, -2], f"Test 17 failed: got {result}, expected {[-4, -2]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = FindEvenNumbers([7, -4, 3, -2, 0])
        assert result == [-4, -2, 0], f"Test 18 failed: got {result}, expected {[-4, -2, 0]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = FindEvenNumbers([0, -2, 3, 7])
        assert result == [0, -2], f"Test 19 failed: got {result}, expected {[0, -2]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = FindEvenNumbers([0, -2, 3, -4, 7, 0, -1003, 7])
        assert result == [0, -2, -4, 0], f"Test 20 failed: got {result}, expected {[0, -2, -4, 0]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = FindEvenNumbers([2, 3, 5, 7, 0])
        assert result == [2, 0], f"Test 21 failed: got {result}, expected {[2, 0]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = FindEvenNumbers([2, 4, 8, 0, 123456789012345678901234567891])
        assert result == [2, 4, 8, 0], f"Test 22 failed: got {result}, expected {[2, 4, 8, 0]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = FindEvenNumbers([10, 8, 4, 2, 16])
        assert result == [10, 8, 4, 2, 16], f"Test 23 failed: got {result}, expected {[10, 8, 4, 2, 16]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = FindEvenNumbers([10, 8, 4, 2])
        assert result == [10, 8, 4, 2], f"Test 24 failed: got {result}, expected {[10, 8, 4, 2]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = FindEvenNumbers([6, 2, -19])
        assert result == [6, 2], f"Test 25 failed: got {result}, expected {[6, 2]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = FindEvenNumbers([1, 2, 9, 4, 0, 42])
        assert result == [2, 4, 0, 42], f"Test 26 failed: got {result}, expected {[2, 4, 0, 42]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = FindEvenNumbers([-2, 0, -9])
        assert result == [-2, 0], f"Test 27 failed: got {result}, expected {[-2, 0]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = FindEvenNumbers([2, 4, 5, 8, 0])
        assert result == [2, 4, 8, 0], f"Test 28 failed: got {result}, expected {[2, 4, 8, 0]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = FindEvenNumbers([123456789012345678901234567890, 3, 5, 7, 9, 18])
        assert result == [123456789012345678901234567890, 18], f"Test 29 failed: got {result}, expected {[123456789012345678901234567890, 18]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = FindEvenNumbers([0, -1, -2, -3, -5, -6, 52])
        assert result == [0, -2, -6, 52], f"Test 30 failed: got {result}, expected {[0, -2, -6, 52]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = FindEvenNumbers([2, 123456789012345678901234567891, 2, 2, 0, 0, -1000])
        assert result == [2, 2, 2, 0, 0, -1000], f"Test 31 failed: got {result}, expected {[2, 2, 2, 0, 0, -1000]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = FindEvenNumbers([-32, 1, 2, 3, 3, 1])
        assert result == [-32, 2], f"Test 32 failed: got {result}, expected {[-32, 2]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = FindEvenNumbers([0, 0, -5, -6, -7, 0, -9, -10])
        assert result == [0, 0, -6, 0, -10], f"Test 33 failed: got {result}, expected {[0, 0, -6, 0, -10]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = FindEvenNumbers([13, 26, 39, 52, 65, 78, 9223372036854775806, 0])
        assert result == [26, 52, 78, 9223372036854775806, 0], f"Test 34 failed: got {result}, expected {[26, 52, 78, 9223372036854775806, 0]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = FindEvenNumbers([13, 26, 39, 19, 65, 78, 14, -2])
        assert result == [26, 78, 14, -2], f"Test 35 failed: got {result}, expected {[26, 78, 14, -2]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = FindEvenNumbers([13, 16, 39, 52, 130, 78, 0])
        assert result == [16, 52, 130, 78, 0], f"Test 36 failed: got {result}, expected {[16, 52, 130, 78, 0]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = FindEvenNumbers([13, 26, 52, 65, 78, 0, -5])
        assert result == [26, 52, 78, 0], f"Test 37 failed: got {result}, expected {[26, 52, 78, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = FindEvenNumbers([1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 4294967294, 38])
        assert result == [2, 6, 8, 10, 12, 14, 16, 18, 20, 4294967294, 38], f"Test 38 failed: got {result}, expected {[2, 6, 8, 10, 12, 14, 16, 18, 20, 4294967294, 38]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = FindEvenNumbers([-1, -3, -10, -7, 0, -11, 9223372036854775807])
        assert result == [-10, 0], f"Test 39 failed: got {result}, expected {[-10, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = FindEvenNumbers([0, 0, -1000, 0, -1])
        assert result == [0, 0, -1000, 0], f"Test 40 failed: got {result}, expected {[0, 0, -1000, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = FindEvenNumbers([7, 8, 0, 0])
        assert result == [8, 0, 0], f"Test 41 failed: got {result}, expected {[8, 0, 0]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = FindEvenNumbers([8, 7, -2, 0])
        assert result == [8, -2, 0], f"Test 42 failed: got {result}, expected {[8, -2, 0]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = FindEvenNumbers([5, 4, 5, 4, 4, -8, -1000000000000000000000000000001])
        assert result == [4, 4, 4, -8], f"Test 43 failed: got {result}, expected {[4, 4, 4, -8]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = FindEvenNumbers([2, 3, 5, 7, 11, 17, 19, 0])
        assert result == [2, 0], f"Test 44 failed: got {result}, expected {[2, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = FindEvenNumbers([2, 3, 5, 7, 11, 13, 17, 19, 0, -16, 0, 0, 0])
        assert result == [2, 0, -16, 0, 0, 0], f"Test 45 failed: got {result}, expected {[2, 0, -16, 0, 0, 0]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = FindEvenNumbers([31, 16, 15, 8, 7, 4, 3, 2, 1, 0, -19])
        assert result == [16, 8, 4, 2, 0], f"Test 46 failed: got {result}, expected {[16, 8, 4, 2, 0]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = FindEvenNumbers([0, 15, -2147483647, 2147483646, 2147483647, -2147483648, 0])
        assert result == [0, 2147483646, -2147483648, 0], f"Test 47 failed: got {result}, expected {[0, 2147483646, -2147483648, 0]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = FindEvenNumbers([9, 0, 11, 0, 26, 0])
        assert result == [0, 0, 26, 0], f"Test 48 failed: got {result}, expected {[0, 0, 26, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = FindEvenNumbers([-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 15])
        assert result == [-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10], f"Test 49 failed: got {result}, expected {[-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = FindEvenNumbers([-19, -17, -13, -11, -9, -7, -5, -3, 8, 1, 3, 5, 9, -13, 0])
        assert result == [8, 0], f"Test 50 failed: got {result}, expected {[8, 0]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = FindEvenNumbers([0, 9223372036854775807, 9223372036854775807, -9223372036854775807, -9223372036854775808, -19, 1000000000000000000000000000000])
        assert result == [0, -9223372036854775808, 1000000000000000000000000000000], f"Test 51 failed: got {result}, expected {[0, -9223372036854775808, 1000000000000000000000000000000]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = FindEvenNumbers([0, 9223372036854775807, 9223372036854775807, -9223372036854775808, -9223372036854775808])
        assert result == [0, -9223372036854775808, -9223372036854775808], f"Test 52 failed: got {result}, expected {[0, -9223372036854775808, -9223372036854775808]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = FindEvenNumbers([-9223372036854775808, -9223372036854775808, 9223372036854775807, 0, 0, 0, 52, 0])
        assert result == [-9223372036854775808, -9223372036854775808, 0, 0, 0, 52, 0], f"Test 53 failed: got {result}, expected {[-9223372036854775808, -9223372036854775808, 0, 0, 0, 52, 0]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = FindEvenNumbers([0, -8, 7, -6, 5, -4, 3, 999, 0, -17, 0, 0])
        assert result == [0, -8, -6, -4, 0, 0, 0], f"Test 54 failed: got {result}, expected {[0, -8, -6, -4, 0, 0, 0]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = FindEvenNumbers([-11, 6, 1, 6, 1, 6, 1, 6, 1, 0])
        assert result == [6, 6, 6, 6, 0], f"Test 55 failed: got {result}, expected {[6, 6, 6, 6, 0]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = FindEvenNumbers([6, 1, 6, 1, 12, 1, 6, 1, 0])
        assert result == [6, 6, 12, 6, 0], f"Test 56 failed: got {result}, expected {[6, 6, 12, 6, 0]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
