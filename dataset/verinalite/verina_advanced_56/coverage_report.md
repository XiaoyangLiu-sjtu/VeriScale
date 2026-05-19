# Coverage Report

Total executable lines: 4
Covered lines: 4
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def moveZeroes(xs):
2: ✓     non_zeroes = [x for x in xs if x != 0]
3: ✓     zeroes = [0] * (len(xs) - len(non_zeroes))
4: ✓     return non_zeroes + zeroes
```

## Complete Test File

```python
def moveZeroes(xs):
    non_zeroes = [x for x in xs if x != 0]
    zeroes = [0] * (len(xs) - len(non_zeroes))
    return non_zeroes + zeroes

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = moveZeroes([0, 1, 0, 3, 12])
        assert result == [1, 3, 12, 0, 0], f"Test 1 failed: got {result}, expected {[1, 3, 12, 0, 0]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = moveZeroes([0, 0, 1])
        assert result == [1, 0, 0], f"Test 2 failed: got {result}, expected {[1, 0, 0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = moveZeroes([1, 2, 3])
        assert result == [1, 2, 3], f"Test 3 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = moveZeroes([0, 0, 0])
        assert result == [0, 0, 0], f"Test 4 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = moveZeroes([])
        assert result == [], f"Test 5 failed: got {result}, expected {[]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = moveZeroes([4, 0, 5, 0, 6])
        assert result == [4, 5, 6, 0, 0], f"Test 6 failed: got {result}, expected {[4, 5, 6, 0, 0]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = moveZeroes([0, 1])
        assert result == [1, 0], f"Test 7 failed: got {result}, expected {[1, 0]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = moveZeroes([1, 0])
        assert result == [1, 0], f"Test 8 failed: got {result}, expected {[1, 0]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = moveZeroes([2, 0, 0, 3])
        assert result == [2, 3, 0, 0], f"Test 9 failed: got {result}, expected {[2, 3, 0, 0]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = moveZeroes([2147483647, 0, -2147483648, 0])
        assert result == [2147483647, -2147483648, 0, 0], f"Test 10 failed: got {result}, expected {[2147483647, -2147483648, 0, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = moveZeroes([0, 0, 0, 0, 1, 1, 1, 1])
        assert result == [1, 1, 1, 1, 0, 0, 0, 0], f"Test 11 failed: got {result}, expected {[1, 1, 1, 1, 0, 0, 0, 0]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = moveZeroes([3, -3, 0, 3, -3, 0, 0, 3, -3])
        assert result == [3, -3, 3, -3, 3, -3, 0, 0, 0], f"Test 12 failed: got {result}, expected {[3, -3, 3, -3, 3, -3, 0, 0, 0]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = moveZeroes([10, 0, 20, 30, 0, 40, 0, 50, 60, 0, 70])
        assert result == [10, 20, 30, 40, 50, 60, 70, 0, 0, 0, 0], f"Test 13 failed: got {result}, expected {[10, 20, 30, 40, 50, 60, 70, 0, 0, 0, 0]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = moveZeroes([123456789, 0, -123456789, 0, 987654321, -987654321, 0])
        assert result == [123456789, -123456789, 987654321, -987654321, 0, 0, 0], f"Test 14 failed: got {result}, expected {[123456789, -123456789, 987654321, -987654321, 0, 0, 0]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = moveZeroes([0, 12, 3, 0, 1, 0])
        assert result == [12, 3, 1, 0, 0, 0], f"Test 15 failed: got {result}, expected {[12, 3, 1, 0, 0, 0]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = moveZeroes([0, 0, 1, -9223372036854775808])
        assert result == [1, -9223372036854775808, 0, 0], f"Test 16 failed: got {result}, expected {[1, -9223372036854775808, 0, 0]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = moveZeroes([987654321, 0, 12])
        assert result == [987654321, 12, 0], f"Test 17 failed: got {result}, expected {[987654321, 12, 0]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = moveZeroes([0, 0, 1, 0])
        assert result == [1, 0, 0, 0], f"Test 18 failed: got {result}, expected {[1, 0, 0, 0]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = moveZeroes([-1, 0, -1, 0])
        assert result == [-1, -1, 0, 0], f"Test 19 failed: got {result}, expected {[-1, -1, 0, 0]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = moveZeroes([0, 0, 0, 9223372036854775807])
        assert result == [9223372036854775807, 0, 0, 0], f"Test 20 failed: got {result}, expected {[9223372036854775807, 0, 0, 0]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = moveZeroes([0, 0, 987654321, 40, 40, 0])
        assert result == [987654321, 40, 40, 0, 0, 0], f"Test 21 failed: got {result}, expected {[987654321, 40, 40, 0, 0, 0]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = moveZeroes([0, 0, -5])
        assert result == [-5, 0, 0], f"Test 22 failed: got {result}, expected {[-5, 0, 0]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = moveZeroes([6, 0, 5, 4])
        assert result == [6, 5, 4, 0], f"Test 23 failed: got {result}, expected {[6, 5, 4, 0]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = moveZeroes([1, 0, 2147483647, 7, 0])
        assert result == [1, 2147483647, 7, 0, 0], f"Test 24 failed: got {result}, expected {[1, 2147483647, 7, 0, 0]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = moveZeroes([0, 0, 1, 0, 0])
        assert result == [1, 0, 0, 0, 0], f"Test 25 failed: got {result}, expected {[1, 0, 0, 0, 0]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = moveZeroes([0, 3, 0, 2, -9223372036854775808])
        assert result == [3, 2, -9223372036854775808, 0, 0], f"Test 26 failed: got {result}, expected {[3, 2, -9223372036854775808, 0, 0]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = moveZeroes([0, 0, 3])
        assert result == [3, 0, 0], f"Test 27 failed: got {result}, expected {[3, 0, 0]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = moveZeroes([0, -2147483648, 0, 0])
        assert result == [-2147483648, 0, 0, 0], f"Test 28 failed: got {result}, expected {[-2147483648, 0, 0, 0]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = moveZeroes([0, 0, 5, -1000000000])
        assert result == [5, -1000000000, 0, 0], f"Test 29 failed: got {result}, expected {[5, -1000000000, 0, 0]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = moveZeroes([-3, 0, 9223372036854775806, 0, 1])
        assert result == [-3, 9223372036854775806, 1, 0, 0], f"Test 30 failed: got {result}, expected {[-3, 9223372036854775806, 1, 0, 0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = moveZeroes([-3, 0, 9223372036854775806, 0])
        assert result == [-3, 9223372036854775806, 0, 0], f"Test 31 failed: got {result}, expected {[-3, 9223372036854775806, 0, 0]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = moveZeroes([0, 0, 0, 3, 3, 0])
        assert result == [3, 3, 0, 0, 0, 0], f"Test 32 failed: got {result}, expected {[3, 3, 0, 0, 0, 0]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = moveZeroes([0, 0, -987654321])
        assert result == [-987654321, 0, 0], f"Test 33 failed: got {result}, expected {[-987654321, 0, 0]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = moveZeroes([0, 0, 0, -987654321, -987654321])
        assert result == [-987654321, -987654321, 0, 0, 0], f"Test 34 failed: got {result}, expected {[-987654321, -987654321, 0, 0, 0]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = moveZeroes([0, 4, 3, 4, 1])
        assert result == [4, 3, 4, 1, 0], f"Test 35 failed: got {result}, expected {[4, 3, 4, 1, 0]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = moveZeroes([1, 0, 1, 12, 0])
        assert result == [1, 1, 12, 0, 0], f"Test 36 failed: got {result}, expected {[1, 1, 12, 0, 0]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = moveZeroes([0, 0, 1, 0, 0])
        assert result == [1, 0, 0, 0, 0], f"Test 37 failed: got {result}, expected {[1, 0, 0, 0, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = moveZeroes([0, 0, 1, -9223372036854775808])
        assert result == [1, -9223372036854775808, 0, 0], f"Test 38 failed: got {result}, expected {[1, -9223372036854775808, 0, 0]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = moveZeroes([0, 0, 1, 0])
        assert result == [1, 0, 0, 0], f"Test 39 failed: got {result}, expected {[1, 0, 0, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = moveZeroes([1, -1, 4, 0, 3, 0, 4])
        assert result == [1, -1, 4, 3, 4, 0, 0], f"Test 40 failed: got {result}, expected {[1, -1, 4, 3, 4, 0, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = moveZeroes([0, 0, 0, 0, 4, 9, 0, 5])
        assert result == [4, 9, 5, 0, 0, 0, 0, 0], f"Test 41 failed: got {result}, expected {[4, 9, 5, 0, 0, 0, 0, 0]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = moveZeroes([8, 9, 0, 3])
        assert result == [8, 9, 3, 0], f"Test 42 failed: got {result}, expected {[8, 9, 3, 0]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = moveZeroes([7, 8, 9, 0, 40])
        assert result == [7, 8, 9, 40, 0], f"Test 43 failed: got {result}, expected {[7, 8, 9, 40, 0]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = moveZeroes([0, 7, 8, 20])
        assert result == [7, 8, 20, 0], f"Test 44 failed: got {result}, expected {[7, 8, 20, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = moveZeroes([1, 0, -1, 0, 50, 0])
        assert result == [1, -1, 50, 0, 0, 0], f"Test 45 failed: got {result}, expected {[1, -1, 50, 0, 0, 0]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = moveZeroes([-5, 0, 5, 0, -5, 5, 987654321, 0, -123456788])
        assert result == [-5, 5, -5, 5, 987654321, -123456788, 0, 0, 0], f"Test 46 failed: got {result}, expected {[-5, 5, -5, 5, 987654321, -123456788, 0, 0, 0]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = moveZeroes([0, -5, 0, 5, 0, -5, 5, 0, 0])
        assert result == [-5, 5, -5, 5, 0, 0, 0, 0, 0], f"Test 47 failed: got {result}, expected {[-5, 5, -5, 5, 0, 0, 0, 0, 0]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = moveZeroes([-5, 0, 0, -5, 5, 0, 0, 10, 0])
        assert result == [-5, -5, 5, 10, 0, 0, 0, 0, 0], f"Test 48 failed: got {result}, expected {[-5, -5, 5, 10, 0, 0, 0, 0, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = moveZeroes([-5, 0, 5, 0, -5, 5, 123456789, 3])
        assert result == [-5, 5, -5, 5, 123456789, 3, 0, 0], f"Test 49 failed: got {result}, expected {[-5, 5, -5, 5, 123456789, 3, 0, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = moveZeroes([-9223372036854775808, 0, 9223372036854775807])
        assert result == [-9223372036854775808, 9223372036854775807, 0], f"Test 50 failed: got {result}, expected {[-9223372036854775808, 9223372036854775807, 0]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = moveZeroes([9223372036854775806, 0, 1, 0])
        assert result == [9223372036854775806, 1, 0, 0], f"Test 51 failed: got {result}, expected {[9223372036854775806, 1, 0, 0]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = moveZeroes([0, -9223372036854775808, 18446744073709551614])
        assert result == [-9223372036854775808, 18446744073709551614, 0], f"Test 52 failed: got {result}, expected {[-9223372036854775808, 18446744073709551614, 0]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = moveZeroes([0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0])
        assert result == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0], f"Test 53 failed: got {result}, expected {[9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = moveZeroes([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0], f"Test 54 failed: got {result}, expected {[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = moveZeroes([5, 0, 6, 6, 7, 0, 8, 1, 9, 0, 1, -6])
        assert result == [5, 6, 6, 7, 8, 1, 9, 1, -6, 0, 0, 0], f"Test 55 failed: got {result}, expected {[5, 6, 6, 7, 8, 1, 9, 1, -6, 0, 0, 0]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = moveZeroes([0, 0, 8, 0, 9, 0, 6, 0, 5])
        assert result == [8, 9, 6, 5, 0, 0, 0, 0, 0], f"Test 56 failed: got {result}, expected {[8, 9, 6, 5, 0, 0, 0, 0, 0]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = moveZeroes([0, 1, 1, 0, 0, 0, 0, 0, 70])
        assert result == [1, 1, 70, 0, 0, 0, 0, 0, 0], f"Test 57 failed: got {result}, expected {[1, 1, 70, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
