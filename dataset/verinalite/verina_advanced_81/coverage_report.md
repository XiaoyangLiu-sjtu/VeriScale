# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def uniqueSorted(arr):
2: ✓     return sorted(set(arr))
```

## Complete Test File

```python
def uniqueSorted(arr):
    return sorted(set(arr))

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = uniqueSorted([1, 1, 2, 3])
        assert result == [1, 2, 3], f"Test 1 failed: got {result}, expected {[1, 2, 3]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = uniqueSorted([3, 3, 3])
        assert result == [3], f"Test 2 failed: got {result}, expected {[3]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = uniqueSorted([])
        assert result == [], f"Test 3 failed: got {result}, expected {[]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = uniqueSorted([5, 2, 2, 5])
        assert result == [2, 5], f"Test 4 failed: got {result}, expected {[2, 5]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = uniqueSorted([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5], f"Test 5 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = uniqueSorted([104, 91, 78, 65, 52, 39, 26, 13])
        assert result == [13, 26, 39, 52, 65, 78, 91, 104], f"Test 6 failed: got {result}, expected {[13, 26, 39, 52, 65, 78, 91, 104]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = uniqueSorted([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        assert result == [1, 2, 3, 4], f"Test 7 failed: got {result}, expected {[1, 2, 3, 4]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = uniqueSorted([314159265358979323846, 271828182845904523536, -161803398874989484820])
        assert result == [-161803398874989484820, 271828182845904523536, 314159265358979323846], f"Test 8 failed: got {result}, expected {[-161803398874989484820, 271828182845904523536, 314159265358979323846]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = uniqueSorted([92, 0])
        assert result == [0, 92], f"Test 9 failed: got {result}, expected {[0, 92]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = uniqueSorted([-60, 3, 5, 2, -2, 5, 0])
        assert result == [-60, -2, 0, 2, 3, 5], f"Test 10 failed: got {result}, expected {[-60, -2, 0, 2, 3, 5]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = uniqueSorted([5, 2, 2, 5, -1000000000000000000000])
        assert result == [-1000000000000000000000, 2, 5], f"Test 11 failed: got {result}, expected {[-1000000000000000000000, 2, 5]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = uniqueSorted([5, 4, 15, 65])
        assert result == [4, 5, 15, 65], f"Test 12 failed: got {result}, expected {[4, 5, 15, 65]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = uniqueSorted([1, -1, 1, 1])
        assert result == [-1, 1], f"Test 13 failed: got {result}, expected {[-1, 1]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = uniqueSorted([4, 1, -3])
        assert result == [-3, 1, 4], f"Test 14 failed: got {result}, expected {[-3, 1, 4]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = uniqueSorted([0, 0, -1, -1, 1, 1, 8, -94])
        assert result == [-94, -1, 0, 1, 8], f"Test 15 failed: got {result}, expected {[-94, -1, 0, 1, 8]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = uniqueSorted([0, 0, 1, 1, 2, 2, 3, 3])
        assert result == [0, 1, 2, 3], f"Test 16 failed: got {result}, expected {[0, 1, 2, 3]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = uniqueSorted([3, 0, 2, 1, 1, 100])
        assert result == [0, 1, 2, 3, 100], f"Test 17 failed: got {result}, expected {[0, 1, 2, 3, 100]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = uniqueSorted([0, 1, 1, -15, 2, 3, 3])
        assert result == [-15, 0, 1, 2, 3], f"Test 18 failed: got {result}, expected {[-15, 0, 1, 2, 3]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = uniqueSorted([-60, 95, 92, -1, -2, -3, -4, -5])
        assert result == [-60, -5, -4, -3, -2, -1, 92, 95], f"Test 19 failed: got {result}, expected {[-60, -5, -4, -3, -2, -1, 92, 95]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = uniqueSorted([-5, -4, -3, -2, -1, -2147483648, -2147483648, 0])
        assert result == [-2147483648, -5, -4, -3, -2, -1, 0], f"Test 20 failed: got {result}, expected {[-2147483648, -5, -4, -3, -2, -1, 0]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = uniqueSorted([-92, 18, -5, -4, -3, -2, -1])
        assert result == [-92, -5, -4, -3, -2, -1, 18], f"Test 21 failed: got {result}, expected {[-92, -5, -4, -3, -2, -1, 18]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = uniqueSorted([-1, -2, -3, -4, -4, -5, 98, 0])
        assert result == [-5, -4, -3, -2, -1, 0, 98], f"Test 22 failed: got {result}, expected {[-5, -4, -3, -2, -1, 0, 98]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = uniqueSorted([0, -10, 10, -10, 7, 0, 11])
        assert result == [-10, 0, 7, 10, 11], f"Test 23 failed: got {result}, expected {[-10, 0, 7, 10, 11]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = uniqueSorted([2147483647, 0, 2147483647])
        assert result == [0, 2147483647], f"Test 24 failed: got {result}, expected {[0, 2147483647]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = uniqueSorted([5, -1000000000000000000000, 1000000000000000000000, 0, 0])
        assert result == [-1000000000000000000000, 0, 5, 1000000000000000000000], f"Test 25 failed: got {result}, expected {[-1000000000000000000000, 0, 5, 1000000000000000000000]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = uniqueSorted([1000000000000000000000, -1000000000000000000000, 5, 94])
        assert result == [-1000000000000000000000, 5, 94, 1000000000000000000000], f"Test 26 failed: got {result}, expected {[-1000000000000000000000, 5, 94, 1000000000000000000000]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = uniqueSorted([-2, -1000000000000000000000, 5])
        assert result == [-1000000000000000000000, -2, 5], f"Test 27 failed: got {result}, expected {[-1000000000000000000000, -2, 5]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = uniqueSorted([7, 9, 9, 8, -6, 8, 7, 7, 7, 0, 0])
        assert result == [-6, 0, 7, 8, 9], f"Test 28 failed: got {result}, expected {[-6, 0, 7, 8, 9]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = uniqueSorted([7, 7, 8, 8, 9, 9, 9, 7])
        assert result == [7, 8, 9], f"Test 29 failed: got {result}, expected {[7, 8, 9]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = uniqueSorted([314159265358979323846, 42, -42, 42, 42, 42])
        assert result == [-42, 42, 314159265358979323846], f"Test 30 failed: got {result}, expected {[-42, 42, 314159265358979323846]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = uniqueSorted([11, 11, 10, 10, 9, 0, 8, 8, -1000000000000000000000, 2147483647, 0])
        assert result == [-1000000000000000000000, 0, 8, 9, 10, 11, 2147483647], f"Test 31 failed: got {result}, expected {[-1000000000000000000000, 0, 8, 9, 10, 11, 2147483647]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = uniqueSorted([11, 0, 10, 10, 9, 9, 8, 0])
        assert result == [0, 8, 9, 10, 11], f"Test 32 failed: got {result}, expected {[0, 8, 9, 10, 11]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = uniqueSorted([11, 11, -2147483648, 9, 9, 8, 8, 0, -5, 78])
        assert result == [-2147483648, -5, 0, 8, 9, 11, 78], f"Test 33 failed: got {result}, expected {[-2147483648, -5, 0, 8, 9, 11, 78]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = uniqueSorted([11, 11, 10, 10, 9, 9, 7, 0, 60])
        assert result == [0, 7, 9, 10, 11, 60], f"Test 34 failed: got {result}, expected {[0, 7, 9, 10, 11, 60]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = uniqueSorted([1, 1, -1, 2, -2, 2, -2, 65])
        assert result == [-2, -1, 1, 2, 65], f"Test 35 failed: got {result}, expected {[-2, -1, 1, 2, 65]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = uniqueSorted([0, -1, 1, -1, 2, -1, 2, -2])
        assert result == [-2, -1, 0, 1, 2], f"Test 36 failed: got {result}, expected {[-2, -1, 0, 1, 2]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = uniqueSorted([-2, 2, -2, 2, -1, 1, -1, 1, -1000])
        assert result == [-1000, -2, -1, 1, 2], f"Test 37 failed: got {result}, expected {[-1000, -2, -1, 1, 2]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = uniqueSorted([999, 999, 1001, 999, 1001, 5, -93, 0])
        assert result == [-93, 0, 5, 999, 1001], f"Test 38 failed: got {result}, expected {[-93, 0, 5, 999, 1001]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = uniqueSorted([1001, 999, -1001, 1000, 999])
        assert result == [-1001, 999, 1000, 1001], f"Test 39 failed: got {result}, expected {[-1001, 999, 1000, 1001]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = uniqueSorted([999, 1001, 1001, 999, 1001, 13, 0, -17])
        assert result == [-17, 0, 13, 999, 1001], f"Test 40 failed: got {result}, expected {[-17, 0, 13, 999, 1001]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = uniqueSorted([-999, -1000, -1001, -999, -1001, 9223372036854775807])
        assert result == [-1001, -1000, -999, 9223372036854775807], f"Test 41 failed: got {result}, expected {[-1001, -1000, -999, 9223372036854775807]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = uniqueSorted([0, -1001, -999, -1001, -1000, 999, 0, 0])
        assert result == [-1001, -1000, -999, 0, 999], f"Test 42 failed: got {result}, expected {[-1001, -1000, -999, 0, 999]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = uniqueSorted([0, 1, 5, 5, 3, 5, 4, -5, 91, 123456789])
        assert result == [-5, 0, 1, 3, 4, 5, 91, 123456789], f"Test 43 failed: got {result}, expected {[-5, 0, 1, 3, 4, 5, 91, 123456789]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = uniqueSorted([26, 52, 65, 78, 91, 104, -93])
        assert result == [-93, 26, 52, 65, 78, 91, 104], f"Test 44 failed: got {result}, expected {[-93, 26, 52, 65, 78, 91, 104]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = uniqueSorted([5, 5, 4, 4, 4, 3, 3, 2, 2, 2])
        assert result == [2, 3, 4, 5], f"Test 45 failed: got {result}, expected {[2, 3, 4, 5]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = uniqueSorted([5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 2, 0])
        assert result == [0, 2, 3, 4, 5], f"Test 46 failed: got {result}, expected {[0, 2, 3, 4, 5]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = uniqueSorted([-5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 2, 45, 43, 1003])
        assert result == [-5, 2, 3, 4, 5, 43, 45, 1003], f"Test 47 failed: got {result}, expected {[-5, 2, 3, 4, 5, 43, 45, 1003]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = uniqueSorted([123456789, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 0])
        assert result == [0, 2, 3, 4, 5, 123456789], f"Test 48 failed: got {result}, expected {[0, 2, 3, 4, 5, 123456789]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = uniqueSorted([-4, -2, -1, 0, 1, 2, 3, 3, 2, 1, 0, -1, -3, 0, -1001])
        assert result == [-1001, -4, -3, -2, -1, 0, 1, 2, 3], f"Test 49 failed: got {result}, expected {[-1001, -4, -3, -2, -1, 0, 1, 2, 3]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = uniqueSorted([-3, -2, -1, 0, 1, 2, 3, 3, 2, 1, 0, -1, -2, -3, 0, 0])
        assert result == [-3, -2, -1, 0, 1, 2, 3], f"Test 50 failed: got {result}, expected {[-3, -2, -1, 0, 1, 2, 3]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = uniqueSorted([123456789, 29, 123456789, 0, 0])
        assert result == [0, 29, 123456789], f"Test 51 failed: got {result}, expected {[0, 29, 123456789]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = uniqueSorted([0, -123456789, 0, 123456789, 987654321, 246913578])
        assert result == [-123456789, 0, 123456789, 246913578, 987654321], f"Test 52 failed: got {result}, expected {[-123456789, 0, 123456789, 246913578, 987654321]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = uniqueSorted([0, 0, 17, 0])
        assert result == [0, 17], f"Test 53 failed: got {result}, expected {[0, 17]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = uniqueSorted([0, 0, 1, 0, 1, 0, -9223372036854775808])
        assert result == [-9223372036854775808, 0, 1], f"Test 54 failed: got {result}, expected {[-9223372036854775808, 0, 1]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = uniqueSorted([314159265358979323846, -161803398874989484820, 0, 0, 91, 0])
        assert result == [-161803398874989484820, 0, 91, 314159265358979323846], f"Test 55 failed: got {result}, expected {[-161803398874989484820, 0, 91, 314159265358979323846]}"
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
