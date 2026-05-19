# Coverage Report

Total executable lines: 7
Covered lines: 7
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def double_array_elements(s):
2: ✓     def helper(index):
3: ✓         if index < len(s):
4: ✓             s[index] *= 2
5: ✓             helper(index + 1)
6: ✓     helper(0)
7: ✓     return s
```

## Complete Test File

```python
def double_array_elements(s):
    def helper(index):
        if index < len(s):
            s[index] *= 2
            helper(index + 1)
    helper(0)
    return s

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = double_array_elements([])
        assert result == [], f"Test 1 failed: got {result}, expected {[]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = double_array_elements([1, 2, 3, 4, 5])
        assert result == [2, 4, 6, 8, 10], f"Test 2 failed: got {result}, expected {[2, 4, 6, 8, 10]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = double_array_elements([0, -1, 5])
        assert result == [0, -2, 10], f"Test 3 failed: got {result}, expected {[0, -2, 10]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = double_array_elements([100])
        assert result == [200], f"Test 4 failed: got {result}, expected {[200]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = double_array_elements([-3, -4])
        assert result == [-6, -8], f"Test 5 failed: got {result}, expected {[-6, -8]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = double_array_elements([0])
        assert result == [0], f"Test 6 failed: got {result}, expected {[0]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = double_array_elements([1])
        assert result == [2], f"Test 7 failed: got {result}, expected {[2]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = double_array_elements([-1])
        assert result == [-2], f"Test 8 failed: got {result}, expected {[-2]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = double_array_elements([5, 4, 3, 2, 1])
        assert result == [10, 8, 6, 4, 2], f"Test 9 failed: got {result}, expected {[10, 8, 6, 4, 2]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = double_array_elements([0, 0, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 10 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = double_array_elements([-10, 10, -20, 20])
        assert result == [-20, 20, -40, 40], f"Test 11 failed: got {result}, expected {[-20, 20, -40, 40]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = double_array_elements([2, 2, 2, 2, 2])
        assert result == [4, 4, 4, 4, 4], f"Test 12 failed: got {result}, expected {[4, 4, 4, 4, 4]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = double_array_elements([7, -7, 14, -14, 21, -21])
        assert result == [14, -14, 28, -28, 42, -42], f"Test 13 failed: got {result}, expected {[14, -14, 28, -28, 42, -42]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = double_array_elements([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        assert result == [18, 16, 14, 12, 10, 8, 6, 4, 2, 0], f"Test 14 failed: got {result}, expected {[18, 16, 14, 12, 10, 8, 6, 4, 2, 0]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = double_array_elements([-1, -2, -3, -4, -5, -6])
        assert result == [-2, -4, -6, -8, -10, -12], f"Test 15 failed: got {result}, expected {[-2, -4, -6, -8, -10, -12]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = double_array_elements([42, 0, -42])
        assert result == [84, 0, -84], f"Test 16 failed: got {result}, expected {[84, 0, -84]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = double_array_elements([11, 13, 17, 19, 23])
        assert result == [22, 26, 34, 38, 46], f"Test 17 failed: got {result}, expected {[22, 26, 34, 38, 46]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = double_array_elements([1, -1, 1, -1, 1, -1, 1, -1])
        assert result == [2, -2, 2, -2, 2, -2, 2, -2], f"Test 18 failed: got {result}, expected {[2, -2, 2, -2, 2, -2, 2, -2]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = double_array_elements([123456789])
        assert result == [246913578], f"Test 19 failed: got {result}, expected {[246913578]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = double_array_elements([-123456789])
        assert result == [-246913578], f"Test 20 failed: got {result}, expected {[-246913578]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = double_array_elements([2147483647, -2147483648])
        assert result == [4294967294, -4294967296], f"Test 21 failed: got {result}, expected {[4294967294, -4294967296]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = double_array_elements([999999999, -999999999, 0])
        assert result == [1999999998, -1999999998, 0], f"Test 22 failed: got {result}, expected {[1999999998, -1999999998, 0]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = double_array_elements([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == [6, 2, 8, 2, 10, 18, 4, 12], f"Test 23 failed: got {result}, expected {[6, 2, 8, 2, 10, 18, 4, 12]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = double_array_elements([8, 6, 7, 5, 3, 0, 9])
        assert result == [16, 12, 14, 10, 6, 0, 18], f"Test 24 failed: got {result}, expected {[16, 12, 14, 10, 6, 0, 18]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = double_array_elements([15, -15, 30, -30, 45, -45, 60, -60])
        assert result == [30, -30, 60, -60, 90, -90, 120, -120], f"Test 25 failed: got {result}, expected {[30, -30, 60, -60, 90, -90, 120, -120]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = double_array_elements([1, 3, 5, 7, 9, 11, 13, 15])
        assert result == [2, 6, 10, 14, 18, 22, 26, 30], f"Test 26 failed: got {result}, expected {[2, 6, 10, 14, 18, 22, 26, 30]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = double_array_elements([-2, -4, -6, -8, -10, -12])
        assert result == [-4, -8, -12, -16, -20, -24], f"Test 27 failed: got {result}, expected {[-4, -8, -12, -16, -20, -24]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = double_array_elements([50, 40, 30, 20, 10])
        assert result == [100, 80, 60, 40, 20], f"Test 28 failed: got {result}, expected {[100, 80, 60, 40, 20]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = double_array_elements([6, 28, 496, 8128])
        assert result == [12, 56, 992, 16256], f"Test 29 failed: got {result}, expected {[12, 56, 992, 16256]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = double_array_elements([31, 62, 93, 124, 155])
        assert result == [62, 124, 186, 248, 310], f"Test 30 failed: got {result}, expected {[62, 124, 186, 248, 310]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = double_array_elements([0, 1, 0, 1, 0, 1, 0, 1, 0])
        assert result == [0, 2, 0, 2, 0, 2, 0, 2, 0], f"Test 31 failed: got {result}, expected {[0, 2, 0, 2, 0, 2, 0, 2, 0]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = double_array_elements([1000, -1000, 2000, -2000, 3000, -3000])
        assert result == [2000, -2000, 4000, -4000, 6000, -6000], f"Test 32 failed: got {result}, expected {[2000, -2000, 4000, -4000, 6000, -6000]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = double_array_elements([9223372036854775807])
        assert result == [18446744073709551614], f"Test 33 failed: got {result}, expected {[18446744073709551614]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = double_array_elements([-9223372036854775808])
        assert result == [-18446744073709551616], f"Test 34 failed: got {result}, expected {[-18446744073709551616]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = double_array_elements([9223372036854775807, -9223372036854775808, 0])
        assert result == [18446744073709551614, -18446744073709551616, 0], f"Test 35 failed: got {result}, expected {[18446744073709551614, -18446744073709551616, 0]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = double_array_elements([4611686018427387904, -4611686018427387904])
        assert result == [9223372036854775808, -9223372036854775808], f"Test 36 failed: got {result}, expected {[9223372036854775808, -9223372036854775808]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = double_array_elements([170141183460469231731687303715884105727])
        assert result == [340282366920938463463374607431768211454], f"Test 37 failed: got {result}, expected {[340282366920938463463374607431768211454]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = double_array_elements([-170141183460469231731687303715884105728])
        assert result == [-340282366920938463463374607431768211456], f"Test 38 failed: got {result}, expected {[-340282366920938463463374607431768211456]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = double_array_elements([999999999999999999999999999999999999999999, -999999999999999999999999999999999999999999])
        assert result == [1999999999999999999999999999999999999999998, -1999999999999999999999999999999999999999998], f"Test 39 failed: got {result}, expected {[1999999999999999999999999999999999999999998, -1999999999999999999999999999999999999999998]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = double_array_elements([1, -1, 2, -2, 4, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, -128, 256, -256, 512, -512, 1024, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384])
        assert result == '-4096, 8192, -8192, 16384, -16384, 32768, -32768]', f"Test 40 failed: got {result}, expected {'-4096, 8192, -8192, 16384, -16384, 32768, -32768]'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = double_array_elements([999999999, 0])
        assert result == [1999999998, 0], f"Test 41 failed: got {result}, expected {[1999999998, 0]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = double_array_elements([31])
        assert result == [62], f"Test 42 failed: got {result}, expected {[62]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = double_array_elements([0, 0, -128, 28])
        assert result == [0, 0, -256, 56], f"Test 43 failed: got {result}, expected {[0, 0, -256, 56]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = double_array_elements([0, 50, -2147483648])
        assert result == [0, 100, -4294967296], f"Test 44 failed: got {result}, expected {[0, 100, -4294967296]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = double_array_elements([0, 4096, -9])
        assert result == [0, 8192, -18], f"Test 45 failed: got {result}, expected {[0, 8192, -18]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = double_array_elements([0, 0])
        assert result == [0, 0], f"Test 46 failed: got {result}, expected {[0, 0]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = double_array_elements([5, 0, -16])
        assert result == [10, 0, -32], f"Test 47 failed: got {result}, expected {[10, 0, -32]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = double_array_elements([0, 0, 999999999, 0])
        assert result == [0, 0, 1999999998, 0], f"Test 48 failed: got {result}, expected {[0, 0, 1999999998, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = double_array_elements([-1, 0])
        assert result == [-2, 0], f"Test 49 failed: got {result}, expected {[-2, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = double_array_elements([1, 2, -3, 4])
        assert result == [2, 4, -6, 8], f"Test 50 failed: got {result}, expected {[2, 4, -6, 8]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = double_array_elements([0, 0, 4096, 5, 4, 6, 2, 1])
        assert result == [0, 0, 8192, 10, 8, 12, 4, 2], f"Test 51 failed: got {result}, expected {[0, 0, 8192, 10, 8, 12, 4, 2]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = double_array_elements([1, 2, 3, 4, 5, -30])
        assert result == [2, 4, 6, 8, 10, -60], f"Test 52 failed: got {result}, expected {[2, 4, 6, 8, 10, -60]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = double_array_elements([5, 4, 3, 2])
        assert result == [10, 8, 6, 4], f"Test 53 failed: got {result}, expected {[10, 8, 6, 4]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = double_array_elements([-9, 93, 3, 2, 1, 0])
        assert result == [-18, 186, 6, 4, 2, 0], f"Test 54 failed: got {result}, expected {[-18, 186, 6, 4, 2, 0]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = double_array_elements([0, 5, 4, 170141183460469231731687303715884105727, 2, 0, 0])
        assert result == [0, 10, 8, 340282366920938463463374607431768211454, 4, 0, 0], f"Test 55 failed: got {result}, expected {[0, 10, 8, 340282366920938463463374607431768211454, 4, 0, 0]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = double_array_elements([1, 2, 3, 4, 5, 3000, -2147483648])
        assert result == [2, 4, 6, 8, 10, 6000, -4294967296], f"Test 56 failed: got {result}, expected {[2, 4, 6, 8, 10, 6000, -4294967296]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = double_array_elements([1, 2, 3, 5])
        assert result == [2, 4, 6, 10], f"Test 57 failed: got {result}, expected {[2, 4, 6, 10]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = double_array_elements([-3, -45, 3, 5, -8192])
        assert result == [-6, -90, 6, 10, -16384], f"Test 58 failed: got {result}, expected {[-6, -90, 6, 10, -16384]}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = double_array_elements([5, 4, 3, 2, 0])
        assert result == [10, 8, 6, 4, 0], f"Test 59 failed: got {result}, expected {[10, 8, 6, 4, 0]}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = double_array_elements([5, 4, 3, 2, 1, 256])
        assert result == [10, 8, 6, 4, 2, 512], f"Test 60 failed: got {result}, expected {[10, 8, 6, 4, 2, 512]}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = double_array_elements([1, 2, 3, 4, 5, 0, -1000, 7])
        assert result == [2, 4, 6, 8, 10, 0, -2000, 14], f"Test 61 failed: got {result}, expected {[2, 4, 6, 8, 10, 0, -2000, 14]}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = double_array_elements([2, 3, 4, 5, 23, 0, 0])
        assert result == [4, 6, 8, 10, 46, 0, 0], f"Test 62 failed: got {result}, expected {[4, 6, 8, 10, 46, 0, 0]}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = double_array_elements([5, -1, 0])
        assert result == [10, -2, 0], f"Test 63 failed: got {result}, expected {[10, -2, 0]}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = double_array_elements([0, -1, 5, 0])
        assert result == [0, -2, 10, 0], f"Test 64 failed: got {result}, expected {[0, -2, 10, 0]}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = double_array_elements([0, -1, 0, 40, -512])
        assert result == [0, -2, 0, 80, -1024], f"Test 65 failed: got {result}, expected {[0, -2, 0, 80, -1024]}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = double_array_elements([-5, -1])
        assert result == [-10, -2], f"Test 66 failed: got {result}, expected {[-10, -2]}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = double_array_elements([0, -1, 5, 4096, 999999999999999999999999999999999999999999, 0])
        assert result == [0, -2, 10, 8192, 1999999999999999999999999999999999999999998, 0], f"Test 67 failed: got {result}, expected {[0, -2, 10, 8192, 1999999999999999999999999999999999999999998, 0]}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = double_array_elements([13, 0, 0])
        assert result == [26, 0, 0], f"Test 68 failed: got {result}, expected {[26, 0, 0]}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = double_array_elements([0, -2, 5, -4611686018427387904, 0])
        assert result == [0, -4, 10, -9223372036854775808, 0], f"Test 69 failed: got {result}, expected {[0, -4, 10, -9223372036854775808, 0]}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = double_array_elements([-1, 5, 0, 5])
        assert result == [-2, 10, 0, 10], f"Test 70 failed: got {result}, expected {[-2, 10, 0, 10]}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = double_array_elements([0, 32, 0])
        assert result == [0, 64, 0], f"Test 71 failed: got {result}, expected {[0, 64, 0]}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = double_array_elements([0, -2, 5, 16])
        assert result == [0, -4, 10, 32], f"Test 72 failed: got {result}, expected {[0, -4, 10, 32]}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = double_array_elements([-1, 5, -4096])
        assert result == [-2, 10, -8192], f"Test 73 failed: got {result}, expected {[-2, 10, -8192]}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = double_array_elements([-1, 5, 30, 256])
        assert result == [-2, 10, 60, 512], f"Test 74 failed: got {result}, expected {[-2, 10, 60, 512]}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = double_array_elements([0, -1, 5, 0, 0])
        assert result == [0, -2, 10, 0, 0], f"Test 75 failed: got {result}, expected {[0, -2, 10, 0, 0]}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = double_array_elements([-20, 8192, 100])
        assert result == [-40, 16384, 200], f"Test 76 failed: got {result}, expected {[-40, 16384, 200]}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = double_array_elements([100, 0, 123456789, 0])
        assert result == [200, 0, 246913578, 0], f"Test 77 failed: got {result}, expected {[200, 0, 246913578, 0]}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = double_array_elements([-99, 3, 3000])
        assert result == [-198, 6, 6000], f"Test 78 failed: got {result}, expected {[-198, 6, 6000]}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = double_array_elements([100, 0, -14])
        assert result == [200, 0, -28], f"Test 79 failed: got {result}, expected {[200, 0, -28]}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = double_array_elements([101, 0])
        assert result == [202, 0], f"Test 80 failed: got {result}, expected {[202, 0]}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = double_array_elements([0, 100])
        assert result == [0, 200], f"Test 81 failed: got {result}, expected {[0, 200]}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = double_array_elements([-3, 0, 100, -4, 0])
        assert result == [-6, 0, 200, -8, 0], f"Test 82 failed: got {result}, expected {[-6, 0, 200, -8, 0]}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = double_array_elements([100, -3000, 0, 19])
        assert result == [200, -6000, 0, 38], f"Test 83 failed: got {result}, expected {[200, -6000, 0, 38]}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = double_array_elements([100, -7])
        assert result == [200, -14], f"Test 84 failed: got {result}, expected {[200, -14]}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = double_array_elements([0, -4096])
        assert result == [0, -8192], f"Test 85 failed: got {result}, expected {[0, -8192]}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = double_array_elements([2000, 0])
        assert result == [4000, 0], f"Test 86 failed: got {result}, expected {[4000, 0]}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = double_array_elements([-100, 0])
        assert result == [-200, 0], f"Test 87 failed: got {result}, expected {[-200, 0]}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = double_array_elements([-3, -4, -100, 0])
        assert result == [-6, -8, -200, 0], f"Test 88 failed: got {result}, expected {[-6, -8, -200, 0]}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = double_array_elements([-3, 0])
        assert result == [-6, 0], f"Test 89 failed: got {result}, expected {[-6, 0]}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = double_array_elements([-3, -4, 63, 9])
        assert result == [-6, -8, 126, 18], f"Test 90 failed: got {result}, expected {[-6, -8, 126, 18]}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = double_array_elements([-3])
        assert result == [-6], f"Test 91 failed: got {result}, expected {[-6]}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = double_array_elements([0, -3, -3])
        assert result == [0, -6, -6], f"Test 92 failed: got {result}, expected {[0, -6, -6]}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = double_array_elements([-3, -4, -7, 0])
        assert result == [-6, -8, -14, 0], f"Test 93 failed: got {result}, expected {[-6, -8, -14, 0]}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = double_array_elements([-3, 0, 0, 0])
        assert result == [-6, 0, 0, 0], f"Test 94 failed: got {result}, expected {[-6, 0, 0, 0]}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = double_array_elements([-4])
        assert result == [-8], f"Test 95 failed: got {result}, expected {[-8]}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = double_array_elements([-4, 63, 0])
        assert result == [-8, 126, 0], f"Test 96 failed: got {result}, expected {[-8, 126, 0]}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = double_array_elements([-2, 0, 19])
        assert result == [-4, 0, 38], f"Test 97 failed: got {result}, expected {[-4, 0, 38]}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = double_array_elements([0, 0, -4])
        assert result == [0, 0, -8], f"Test 98 failed: got {result}, expected {[0, 0, -8]}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = double_array_elements([0, 16])
        assert result == [0, 32], f"Test 99 failed: got {result}, expected {[0, 32]}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = double_array_elements([42, 0, 62])
        assert result == [84, 0, 124], f"Test 100 failed: got {result}, expected {[84, 0, 124]}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = double_array_elements([0, 0, 0])
        assert result == [0, 0, 0], f"Test 101 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = double_array_elements([-14, 0, -4096])
        assert result == [-28, 0, -8192], f"Test 102 failed: got {result}, expected {[-28, 0, -8192]}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = double_array_elements([-1, 0, 0])
        assert result == [-2, 0, 0], f"Test 103 failed: got {result}, expected {[-2, 0, 0]}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = double_array_elements([14])
        assert result == [28], f"Test 104 failed: got {result}, expected {[28]}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = double_array_elements([0, 0, -64, 0])
        assert result == [0, 0, -128, 0], f"Test 105 failed: got {result}, expected {[0, 0, -128, 0]}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = double_array_elements([9223372036854775808, 62])
        assert result == [18446744073709551616, 124], f"Test 106 failed: got {result}, expected {[18446744073709551616, 124]}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = double_array_elements([0, -99, 0, 1])
        assert result == [0, -198, 0, 2], f"Test 107 failed: got {result}, expected {[0, -198, 0, 2]}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = double_array_elements([123456789, 0, 0])
        assert result == [246913578, 0, 0], f"Test 108 failed: got {result}, expected {[246913578, 0, 0]}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = double_array_elements([2])
        assert result == [4], f"Test 109 failed: got {result}, expected {[4]}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = double_array_elements([1, -12, -1, -4611686018427387904])
        assert result == [2, -24, -2, -9223372036854775808], f"Test 110 failed: got {result}, expected {[2, -24, -2, -9223372036854775808]}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = double_array_elements([1, 123456789, -999999999, -999999999999999999999999999999999999999999])
        assert result == [2, 246913578, -1999999998, -1999999999999999999999999999999999999999998], f"Test 111 failed: got {result}, expected {[2, 246913578, -1999999998, -1999999999999999999999999999999999999999998]}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = double_array_elements([1, 0])
        assert result == [2, 0], f"Test 112 failed: got {result}, expected {[2, 0]}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = double_array_elements([2, 0, 0, 0, 2147483647])
        assert result == [4, 0, 0, 0, 4294967294], f"Test 113 failed: got {result}, expected {[4, 0, 0, 0, 4294967294]}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = double_array_elements([1, 170141183460469231731687303715884105727, 0, 16])
        assert result == [2, 340282366920938463463374607431768211454, 0, 32], f"Test 114 failed: got {result}, expected {[2, 340282366920938463463374607431768211454, 0, 32]}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = double_array_elements([1, 0, 999999999999999999999999999999999999999999])
        assert result == [2, 0, 1999999999999999999999999999999999999999998], f"Test 115 failed: got {result}, expected {[2, 0, 1999999999999999999999999999999999999999998]}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = double_array_elements([0, 1, 0])
        assert result == [0, 2, 0], f"Test 116 failed: got {result}, expected {[0, 2, 0]}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = double_array_elements([-1, -32, 1000, 0, 2147483647])
        assert result == [-2, -64, 2000, 0, 4294967294], f"Test 117 failed: got {result}, expected {[-2, -64, 2000, 0, 4294967294]}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = double_array_elements([-1, 0, 512])
        assert result == [-2, 0, 1024], f"Test 118 failed: got {result}, expected {[-2, 0, 1024]}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = double_array_elements([-1, 0, 32])
        assert result == [-2, 0, 64], f"Test 119 failed: got {result}, expected {[-2, 0, 64]}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = double_array_elements([-5, -1, 0])
        assert result == [-10, -2, 0], f"Test 120 failed: got {result}, expected {[-10, -2, 0]}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = double_array_elements([-1, -2048])
        assert result == [-2, -4096], f"Test 121 failed: got {result}, expected {[-2, -4096]}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = double_array_elements([-1, 15])
        assert result == [-2, 30], f"Test 122 failed: got {result}, expected {[-2, 30]}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = double_array_elements([1, 9223372036854775807, 999999999])
        assert result == [2, 18446744073709551614, 1999999998], f"Test 123 failed: got {result}, expected {[2, 18446744073709551614, 1999999998]}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = double_array_elements([-1, 0, -60, 14, 1, -42])
        assert result == [-2, 0, -120, 28, 2, -84], f"Test 124 failed: got {result}, expected {[-2, 0, -120, 28, 2, -84]}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = double_array_elements([-1, 1024, -7, 0])
        assert result == [-2, 2048, -14, 0], f"Test 125 failed: got {result}, expected {[-2, 2048, -14, 0]}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = double_array_elements([0, 1, 2, 3, 4, 5, 0, 0])
        assert result == [0, 2, 4, 6, 8, 10, 0, 0], f"Test 126 failed: got {result}, expected {[0, 2, 4, 6, 8, 10, 0, 0]}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = double_array_elements([0, 4, 2, 0, 1])
        assert result == [0, 8, 4, 0, 2], f"Test 127 failed: got {result}, expected {[0, 8, 4, 0, 2]}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = double_array_elements([4, 4, 3, 2, 1])
        assert result == [8, 8, 6, 4, 2], f"Test 128 failed: got {result}, expected {[8, 8, 6, 4, 2]}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = double_array_elements([1, 2, 3, 5, -999999999999999999999999999999999999999999])
        assert result == [2, 4, 6, 10, -1999999999999999999999999999999999999999998], f"Test 129 failed: got {result}, expected {[2, 4, 6, 10, -1999999999999999999999999999999999999999998]}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = double_array_elements([6, 2, 1])
        assert result == [12, 4, 2], f"Test 130 failed: got {result}, expected {[12, 4, 2]}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = double_array_elements([5, 4, 6, 1, 1, 0, 0, -4])
        assert result == [10, 8, 12, 2, 2, 0, 0, -8], f"Test 131 failed: got {result}, expected {[10, 8, 12, 2, 2, 0, 0, -8]}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = double_array_elements([2, 6, 4, 5, 0])
        assert result == [4, 12, 8, 10, 0], f"Test 132 failed: got {result}, expected {[4, 12, 8, 10, 0]}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = double_array_elements([5, 4, 2, 1, 40, 4611686018427387904])
        assert result == [10, 8, 4, 2, 80, 9223372036854775808], f"Test 133 failed: got {result}, expected {[10, 8, 4, 2, 80, 9223372036854775808]}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = double_array_elements([5, 2, 3, 2, 101])
        assert result == [10, 4, 6, 4, 202], f"Test 134 failed: got {result}, expected {[10, 4, 6, 4, 202]}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = double_array_elements([0, 1, 2, 0, -1024, 5, -5])
        assert result == [0, 2, 4, 0, -2048, 10, -10], f"Test 135 failed: got {result}, expected {[0, 2, 4, 0, -2048, 10, -10]}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = double_array_elements([-6, 3])
        assert result == [-12, 6], f"Test 136 failed: got {result}, expected {[-12, 6]}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = double_array_elements([1, -2, 3, 4, 5, 0])
        assert result == [2, -4, 6, 8, 10, 0], f"Test 137 failed: got {result}, expected {[2, -4, 6, 8, 10, 0]}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = double_array_elements([0, 4, 3, 3, 1])
        assert result == [0, 8, 6, 6, 2], f"Test 138 failed: got {result}, expected {[0, 8, 6, 6, 2]}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = double_array_elements([3, 4, 5])
        assert result == [6, 8, 10], f"Test 139 failed: got {result}, expected {[6, 8, 10]}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = double_array_elements([0, 0, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 140 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = double_array_elements([16, 0, 0])
        assert result == [32, 0, 0], f"Test 141 failed: got {result}, expected {[32, 0, 0]}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = double_array_elements([0, -1, 0, 0])
        assert result == [0, -2, 0, 0], f"Test 142 failed: got {result}, expected {[0, -2, 0, 0]}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = double_array_elements([0, 2048, 0, 0])
        assert result == [0, 4096, 0, 0], f"Test 143 failed: got {result}, expected {[0, 4096, 0, 0]}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = double_array_elements([-512, 0, 0, 0, 0])
        assert result == [-1024, 0, 0, 0, 0], f"Test 144 failed: got {result}, expected {[-1024, 0, 0, 0, 0]}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = double_array_elements([-2])
        assert result == [-4], f"Test 145 failed: got {result}, expected {[-4]}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = double_array_elements([0, 0, 2, 0, 17])
        assert result == [0, 0, 4, 0, 34], f"Test 146 failed: got {result}, expected {[0, 0, 4, 0, 34]}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = double_array_elements([0, 0, 0, 20, 0])
        assert result == [0, 0, 0, 40, 0], f"Test 147 failed: got {result}, expected {[0, 0, 0, 40, 0]}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = double_array_elements([0, 0, 512])
        assert result == [0, 0, 1024], f"Test 148 failed: got {result}, expected {[0, 0, 1024]}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = double_array_elements([0, -999999999, -8192])
        assert result == [0, -1999999998, -16384], f"Test 149 failed: got {result}, expected {[0, -1999999998, -16384]}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = double_array_elements([10, -10])
        assert result == [20, -20], f"Test 150 failed: got {result}, expected {[20, -20]}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = double_array_elements([-10, 10, -20, 20, 4])
        assert result == [-20, 20, -40, 40, 8], f"Test 151 failed: got {result}, expected {[-20, 20, -40, 40, 8]}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = double_array_elements([0, 10, 15, 20, -123456789])
        assert result == [0, 20, 30, 40, -246913578], f"Test 152 failed: got {result}, expected {[0, 20, 30, 40, -246913578]}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = double_array_elements([-10, 10, -20, 20, 1, -2000, 496, 0])
        assert result == [-20, 20, -40, 40, 2, -4000, 992, 0], f"Test 153 failed: got {result}, expected {[-20, 20, -40, 40, 2, -4000, 992, 0]}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = double_array_elements([0, 20, -20, 20, -10])
        assert result == [0, 40, -40, 40, -20], f"Test 154 failed: got {result}, expected {[0, 40, -40, 40, -20]}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = double_array_elements([-10, 10, -4, 20])
        assert result == [-20, 20, -8, 40], f"Test 155 failed: got {result}, expected {[-20, 20, -8, 40]}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = double_array_elements([-10, 10, -20, 20, 5])
        assert result == [-20, 20, -40, 40, 10], f"Test 156 failed: got {result}, expected {[-20, 20, -40, 40, 10]}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = double_array_elements([-4611686018427387904, 20, -20, 10, -10, 8])
        assert result == [-9223372036854775808, 40, -40, 20, -20, 16], f"Test 157 failed: got {result}, expected {[-9223372036854775808, 40, -40, 20, -20, 16]}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = double_array_elements([-20, 20])
        assert result == [-40, 40], f"Test 158 failed: got {result}, expected {[-40, 40]}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = double_array_elements([-10, 10, -20, 20, -99])
        assert result == [-20, 20, -40, 40, -198], f"Test 159 failed: got {result}, expected {[-20, 20, -40, 40, -198]}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = double_array_elements([10, -20, -32, 0, 0])
        assert result == [20, -40, -64, 0, 0], f"Test 160 failed: got {result}, expected {[20, -40, -64, 0, 0]}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = double_array_elements([-10, 10, 20])
        assert result == [-20, 20, 40], f"Test 161 failed: got {result}, expected {[-20, 20, 40]}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = double_array_elements([0, 10, -20])
        assert result == [0, 20, -40], f"Test 162 failed: got {result}, expected {[0, 20, -40]}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = double_array_elements([-10, -4611686018427387904, -20])
        assert result == [-20, -9223372036854775808, -40], f"Test 163 failed: got {result}, expected {[-20, -9223372036854775808, -40]}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = double_array_elements([0, 2, 2, 2, 2, 0, 0])
        assert result == [0, 4, 4, 4, 4, 0, 0], f"Test 164 failed: got {result}, expected {[0, 4, 4, 4, 4, 0, 0]}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = double_array_elements([0, 2, 2, 2, 0])
        assert result == [0, 4, 4, 4, 0], f"Test 165 failed: got {result}, expected {[0, 4, 4, 4, 0]}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = double_array_elements([2, 2, 2, 2])
        assert result == [4, 4, 4, 4], f"Test 166 failed: got {result}, expected {[4, 4, 4, 4]}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = double_array_elements([2, 0, 2, 2, 2])
        assert result == [4, 0, 4, 4, 4], f"Test 167 failed: got {result}, expected {[4, 0, 4, 4, 4]}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = double_array_elements([2, 2, 1, 2, 2, 0])
        assert result == [4, 4, 2, 4, 4, 0], f"Test 168 failed: got {result}, expected {[4, 4, 2, 4, 4, 0]}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = double_array_elements([17, 2, 2])
        assert result == [34, 4, 4], f"Test 169 failed: got {result}, expected {[34, 4, 4]}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = double_array_elements([0, 0, 2, 2, 1, 2, 2])
        assert result == [0, 0, 4, 4, 2, 4, 4], f"Test 170 failed: got {result}, expected {[0, 0, 4, 4, 2, 4, 4]}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = double_array_elements([62, 2, 2, 2, 2, 2, 0, -4611686018427387904, -256])
        assert result == [124, 4, 4, 4, 4, 4, 0, -9223372036854775808, -512], f"Test 171 failed: got {result}, expected {[124, 4, 4, 4, 4, 4, 0, -9223372036854775808, -512]}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = double_array_elements([2, 2, -1, 21, 0, 2147483647])
        assert result == [4, 4, -2, 42, 0, 4294967294], f"Test 172 failed: got {result}, expected {[4, 4, -2, 42, 0, 4294967294]}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = double_array_elements([2, 2, 2, 2, 2, 0, 0, -4])
        assert result == [4, 4, 4, 4, 4, 0, 0, -8], f"Test 173 failed: got {result}, expected {[4, 4, 4, 4, 4, 0, 0, -8]}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = double_array_elements([0, -3, 0, 2, 2, 2, 2, -21])
        assert result == [0, -6, 0, 4, 4, 4, 4, -42], f"Test 174 failed: got {result}, expected {[0, -6, 0, 4, 4, 4, 4, -42]}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = double_array_elements([2, 0, 2, 2, 2048])
        assert result == [4, 0, 4, 4, 4096], f"Test 175 failed: got {result}, expected {[4, 0, 4, 4, 4096]}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = double_array_elements([2, 2, 2])
        assert result == [4, 4, 4], f"Test 176 failed: got {result}, expected {[4, 4, 4]}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = double_array_elements([128, 2, 2, 2, 2, 20])
        assert result == [256, 4, 4, 4, 4, 40], f"Test 177 failed: got {result}, expected {[256, 4, 4, 4, 4, 40]}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = double_array_elements([2, 2, 2, 2, 2, -9223372036854775808])
        assert result == [4, 4, 4, 4, 4, -18446744073709551616], f"Test 178 failed: got {result}, expected {[4, 4, 4, 4, 4, -18446744073709551616]}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, -7, 14, -14, 21, -21, 9223372036854775808])
        assert result == [-340282366920938463463374607431768211456, -14, 28, -28, 42, -42, 18446744073709551616], f"Test 179 failed: got {result}, expected {[-340282366920938463463374607431768211456, -14, 28, -28, 42, -42, 18446744073709551616]}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = double_array_elements([0, -21, 21, -16384, 14, -7, 7])
        assert result == [0, -42, 42, -32768, 28, -14, 14], f"Test 180 failed: got {result}, expected {[0, -42, 42, -32768, 28, -14, 14]}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = double_array_elements([7, -7, 14, -13, 21, -21, 0])
        assert result == [14, -14, 28, -26, 42, -42, 0], f"Test 181 failed: got {result}, expected {[14, -14, 28, -26, 42, -42, 0]}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = double_array_elements([7, -7, 14, -14, 21, -21, 0])
        assert result == [14, -14, 28, -28, 42, -42, 0], f"Test 182 failed: got {result}, expected {[14, -14, 28, -28, 42, -42, 0]}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = double_array_elements([64, -7, 14, -14, 21, -21, -170141183460469231731687303715884105728, 0])
        assert result == [128, -14, 28, -28, 42, -42, -340282366920938463463374607431768211456, 0], f"Test 183 failed: got {result}, expected {[128, -14, 28, -28, 42, -42, -340282366920938463463374607431768211456, 0]}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = double_array_elements([7, -7, 14, -14, -21, -170141183460469231731687303715884105728, 4096, 0])
        assert result == [14, -14, 28, -28, -42, -340282366920938463463374607431768211456, 8192, 0], f"Test 184 failed: got {result}, expected {[14, -14, 28, -28, -42, -340282366920938463463374607431768211456, 8192, 0]}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = double_array_elements([0, -21, -14, 14, -7, 7])
        assert result == [0, -42, -28, 28, -14, 14], f"Test 185 failed: got {result}, expected {[0, -42, -28, 28, -14, 14]}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = double_array_elements([7, -7, 14, -14, 22, 0])
        assert result == [14, -14, 28, -28, 44, 0], f"Test 186 failed: got {result}, expected {[14, -14, 28, -28, 44, 0]}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = double_array_elements([496, -21, 20, -14, 14, -7, 7])
        assert result == [992, -42, 40, -28, 28, -14, 14], f"Test 187 failed: got {result}, expected {[992, -42, 40, -28, 28, -14, 14]}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = double_array_elements([7, -7, 14, -14, 21, 16384, 0])
        assert result == [14, -14, 28, -28, 42, 32768, 0], f"Test 188 failed: got {result}, expected {[14, -14, 28, -28, 42, 32768, 0]}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = double_array_elements([-21, -14, 14, -7, 0, 0])
        assert result == [-42, -28, 28, -14, 0, 0], f"Test 189 failed: got {result}, expected {[-42, -28, 28, -14, 0, 0]}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = double_array_elements([7, -7, 14, -14, 21, -21, 40, -15])
        assert result == [14, -14, 28, -28, 42, -42, 80, -30], f"Test 190 failed: got {result}, expected {[14, -14, 28, -28, 42, -42, 80, -30]}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = double_array_elements([-21, 21, -14, 14, -7, 45])
        assert result == [-42, 42, -28, 28, -14, 90], f"Test 191 failed: got {result}, expected {[-42, 42, -28, 28, -14, 90]}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = double_array_elements([7, -7, 13, -14, 21, -21])
        assert result == [14, -14, 26, -28, 42, -42], f"Test 192 failed: got {result}, expected {[14, -14, 26, -28, 42, -42]}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = double_array_elements([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 512, 0, 13])
        assert result == [18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 1024, 0, 26], f"Test 193 failed: got {result}, expected {[18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 1024, 0, 26]}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = double_array_elements([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 6, 6, 0])
        assert result == [18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 12, 12, 0], f"Test 194 failed: got {result}, expected {[18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 12, 12, 0]}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = double_array_elements([9, -8, 7, 6, 5, 3, 2, 1, 0, -999999999999999999999999999999999999999999])
        assert result == [18, -16, 14, 12, 10, 6, 4, 2, 0, -1999999999999999999999999999999999999999998], f"Test 195 failed: got {result}, expected {[18, -16, 14, 12, 10, 6, 4, 2, 0, -1999999999999999999999999999999999999999998]}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = double_array_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -8])
        assert result == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, -16], f"Test 196 failed: got {result}, expected {[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, -16]}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = double_array_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -99])
        assert result == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, -198], f"Test 197 failed: got {result}, expected {[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, -198]}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = double_array_elements([9, 8, 7, 6, 5, 5, 3, 2, 1, 0, 14])
        assert result == [18, 16, 14, 12, 10, 10, 6, 4, 2, 0, 28], f"Test 198 failed: got {result}, expected {[18, 16, 14, 12, 10, 10, 6, 4, 2, 0, 28]}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = double_array_elements([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert result == [0, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18], f"Test 199 failed: got {result}, expected {[0, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = double_array_elements([0, 1, 2, -3, 4, 5, 6, 7, 8, 9, 0])
        assert result == [0, 2, 4, -6, 8, 10, 12, 14, 16, 18, 0], f"Test 200 failed: got {result}, expected {[0, 2, 4, -6, 8, 10, 12, 14, 16, 18, 0]}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = double_array_elements([9, -8, 7, 6, 5, 3, 2, 1])
        assert result == [18, -16, 14, 12, 10, 6, 4, 2], f"Test 201 failed: got {result}, expected {[18, -16, 14, 12, 10, 6, 4, 2]}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = double_array_elements([9, 8, 7, 6, -5, 4, 3, 2, 1, 0, -128])
        assert result == [18, 16, 14, 12, -10, 8, 6, 4, 2, 0, -256], f"Test 202 failed: got {result}, expected {[18, 16, 14, 12, -10, 8, 6, 4, 2, 0, -256]}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = double_array_elements([9, 8, 7, 6, 5, 4, 3, 2, 1, -2048, 0, 496, 0, 0])
        assert result == [18, 16, 14, 12, 10, 8, 6, 4, 2, -4096, 0, 992, 0, 0], f"Test 203 failed: got {result}, expected {[18, 16, 14, 12, 10, 8, 6, 4, 2, -4096, 0, 992, 0, 0]}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = double_array_elements([9, 8, 7, 6, 5, 4, 3, 2, 2, 0, 2000, 62, 0])
        assert result == [18, 16, 14, 12, 10, 8, 6, 4, 4, 0, 4000, 124, 0], f"Test 204 failed: got {result}, expected {[18, 16, 14, 12, 10, 8, 6, 4, 4, 0, 4000, 124, 0]}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = double_array_elements([9, 8, 7, 6, 5, 4, 5, 155, 1, 0, 2000])
        assert result == [18, 16, 14, 12, 10, 8, 10, 310, 2, 0, 4000], f"Test 205 failed: got {result}, expected {[18, 16, 14, 12, 10, 8, 10, 310, 2, 0, 4000]}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = double_array_elements([0, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0])
        assert result == [0, 4, 6, 8, 10, 12, 14, 16, 18, 0, 0], f"Test 206 failed: got {result}, expected {[0, 4, 6, 8, 10, 12, 14, 16, 18, 0, 0]}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = double_array_elements([-1, -2, -3, -5, -6, 0, 0, 31])
        assert result == [-2, -4, -6, -10, -12, 0, 0, 62], f"Test 207 failed: got {result}, expected {[-2, -4, -6, -10, -12, 0, 0, 62]}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = double_array_elements([-1, -2, -3, -4, -5, -6, 40, 16384])
        assert result == [-2, -4, -6, -8, -10, -12, 80, 32768], f"Test 208 failed: got {result}, expected {[-2, -4, -6, -8, -10, -12, 80, 32768]}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = double_array_elements([-1, -2, -3, -3, -5, -6])
        assert result == [-2, -4, -6, -6, -10, -12], f"Test 209 failed: got {result}, expected {[-2, -4, -6, -6, -10, -12]}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = double_array_elements([-1, -2, -3, -4, -5, -6, -99, -10])
        assert result == [-2, -4, -6, -8, -10, -12, -198, -20], f"Test 210 failed: got {result}, expected {[-2, -4, -6, -8, -10, -12, -198, -20]}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = double_array_elements([-2000, 0, -6, -5, -4, -3, -2, -1])
        assert result == [-4000, 0, -12, -10, -8, -6, -4, -2], f"Test 211 failed: got {result}, expected {[-4000, 0, -12, -10, -8, -6, -4, -2]}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = double_array_elements([0, -1, -2, -3, -5, -5, -6, -2000])
        assert result == [0, -2, -4, -6, -10, -10, -12, -4000], f"Test 212 failed: got {result}, expected {[0, -2, -4, -6, -10, -10, -12, -4000]}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = double_array_elements([-1, -2, -3, -4, -5, -6, 0, 28, 123456789, 0])
        assert result == [-2, -4, -6, -8, -10, -12, 0, 56, 246913578, 0], f"Test 213 failed: got {result}, expected {[-2, -4, -6, -8, -10, -12, 0, 56, 246913578, 0]}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = double_array_elements([0, -5, -4, -1, -2, -1])
        assert result == [0, -10, -8, -2, -4, -2], f"Test 214 failed: got {result}, expected {[0, -10, -8, -2, -4, -2]}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = double_array_elements([-1, -1, -3, -5, -6])
        assert result == [-2, -2, -6, -10, -12], f"Test 215 failed: got {result}, expected {[-2, -2, -6, -10, -12]}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = double_array_elements([-1000, -1, -2, -3, -5, -6, 0])
        assert result == [-2000, -2, -4, -6, -10, -12, 0], f"Test 216 failed: got {result}, expected {[-2000, -2, -4, -6, -10, -12, 0]}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = double_array_elements([-1, -2, -3, -5, -6, -2048])
        assert result == [-2, -4, -6, -10, -12, -4096], f"Test 217 failed: got {result}, expected {[-2, -4, -6, -10, -12, -4096]}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = double_array_elements([-1, -2, -4, -5, -6, 0])
        assert result == [-2, -4, -8, -10, -12, 0], f"Test 218 failed: got {result}, expected {[-2, -4, -8, -10, -12, 0]}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = double_array_elements([-1, -2, -3, -5, -7])
        assert result == [-2, -4, -6, -10, -14], f"Test 219 failed: got {result}, expected {[-2, -4, -6, -10, -14]}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = double_array_elements([0, -6, -5, -1])
        assert result == [0, -12, -10, -2], f"Test 220 failed: got {result}, expected {[0, -12, -10, -2]}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = double_array_elements([-1, -2, -3, -4, -5, -6, -10, 17, -64, 0])
        assert result == [-2, -4, -6, -8, -10, -12, -20, 34, -128, 0], f"Test 221 failed: got {result}, expected {[-2, -4, -6, -8, -10, -12, -20, 34, -128, 0]}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = double_array_elements([41, 0, -42])
        assert result == [82, 0, -84], f"Test 222 failed: got {result}, expected {[82, 0, -84]}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = double_array_elements([42, 0, -42, 1, 0])
        assert result == [84, 0, -84, 2, 0], f"Test 223 failed: got {result}, expected {[84, 0, -84, 2, 0]}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = double_array_elements([-41, 0, 40, 0])
        assert result == [-82, 0, 80, 0], f"Test 224 failed: got {result}, expected {[-82, 0, 80, 0]}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = double_array_elements([42, 0, -42, 0, 13, 0])
        assert result == [84, 0, -84, 0, 26, 0], f"Test 225 failed: got {result}, expected {[84, 0, -84, 0, 26, 0]}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = double_array_elements([42, 0, -41])
        assert result == [84, 0, -82], f"Test 226 failed: got {result}, expected {[84, 0, -82]}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = double_array_elements([0, -42, 0, 45])
        assert result == [0, -84, 0, 90], f"Test 227 failed: got {result}, expected {[0, -84, 0, 90]}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = double_array_elements([21, 0, 0, 9223372036854775808])
        assert result == [42, 0, 0, 18446744073709551616], f"Test 228 failed: got {result}, expected {[42, 0, 0, 18446744073709551616]}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = double_array_elements([2000, 0, -42])
        assert result == [4000, 0, -84], f"Test 229 failed: got {result}, expected {[4000, 0, -84]}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = double_array_elements([42, 0, -42, -60])
        assert result == [84, 0, -84, -120], f"Test 230 failed: got {result}, expected {[84, 0, -84, -120]}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = double_array_elements([0, -42, 0, 42])
        assert result == [0, -84, 0, 84], f"Test 231 failed: got {result}, expected {[0, -84, 0, 84]}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = double_array_elements([42, 0, -42, 0])
        assert result == [84, 0, -84, 0], f"Test 232 failed: got {result}, expected {[84, 0, -84, 0]}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = double_array_elements([2048, 0, -42, 0])
        assert result == [4096, 0, -84, 0], f"Test 233 failed: got {result}, expected {[4096, 0, -84, 0]}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = double_array_elements([-14, 0, -14, 0, 42])
        assert result == [-28, 0, -28, 0, 84], f"Test 234 failed: got {result}, expected {[-28, 0, -28, 0, 84]}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = double_array_elements([-2000, -42, 11])
        assert result == [-4000, -84, 22], f"Test 235 failed: got {result}, expected {[-4000, -84, 22]}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = double_array_elements([-64, 0, 42])
        assert result == [-128, 0, 84], f"Test 236 failed: got {result}, expected {[-128, 0, 84]}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = double_array_elements([23, 19, 17, 13, 11])
        assert result == [46, 38, 34, 26, 22], f"Test 237 failed: got {result}, expected {[46, 38, 34, 26, 22]}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = double_array_elements([0, 0, 23, 19, 17, 13, 11, 1024])
        assert result == [0, 0, 46, 38, 34, 26, 22, 2048], f"Test 238 failed: got {result}, expected {[0, 0, 46, 38, 34, 26, 22, 2048]}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = double_array_elements([11, 13, 17, 0, 23])
        assert result == [22, 26, 34, 0, 46], f"Test 239 failed: got {result}, expected {[22, 26, 34, 0, 46]}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = double_array_elements([11, 17, 19, 23])
        assert result == [22, 34, 38, 46], f"Test 240 failed: got {result}, expected {[22, 34, 38, 46]}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = double_array_elements([45, 11, 13, 17, 19, 23, 0])
        assert result == [90, 22, 26, 34, 38, 46, 0], f"Test 241 failed: got {result}, expected {[90, 22, 26, 34, 38, 46, 0]}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = double_array_elements([23, 19, 13, 11])
        assert result == [46, 38, 26, 22], f"Test 242 failed: got {result}, expected {[46, 38, 26, 22]}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = double_array_elements([23, 19, 17])
        assert result == [46, 38, 34], f"Test 243 failed: got {result}, expected {[46, 38, 34]}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = double_array_elements([13, 17, 19, 23, 0, 0])
        assert result == [26, 34, 38, 46, 0, 0], f"Test 244 failed: got {result}, expected {[26, 34, 38, 46, 0, 0]}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = double_array_elements([11, 13, 17, 19, 23, 256])
        assert result == [22, 26, 34, 38, 46, 512], f"Test 245 failed: got {result}, expected {[22, 26, 34, 38, 46, 512]}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = double_array_elements([23, 19, 17, 13, 11, -32, 170141183460469231731687303715884105727])
        assert result == [46, 38, 34, 26, 22, -64, 340282366920938463463374607431768211454], f"Test 246 failed: got {result}, expected {[46, 38, 34, 26, 22, -64, 340282366920938463463374607431768211454]}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = double_array_elements([11, 17, 19, 23, 0, 0, 0, 2147483647])
        assert result == [22, 34, 38, 46, 0, 0, 0, 4294967294], f"Test 247 failed: got {result}, expected {[22, 34, 38, 46, 0, 0, 0, 4294967294]}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = double_array_elements([11, 13, 17, 19, 23, 0])
        assert result == [22, 26, 34, 38, 46, 0], f"Test 248 failed: got {result}, expected {[22, 26, 34, 38, 46, 0]}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = double_array_elements([-99, 13, 17, 19, 23, 0])
        assert result == [-198, 26, 34, 38, 46, 0], f"Test 249 failed: got {result}, expected {[-198, 26, 34, 38, 46, 0]}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = double_array_elements([23, 17, 13, 0])
        assert result == [46, 34, 26, 0], f"Test 250 failed: got {result}, expected {[46, 34, 26, 0]}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = double_array_elements([1, 1, -1, 1, -1, 1, -1])
        assert result == [2, 2, -2, 2, -2, 2, -2], f"Test 251 failed: got {result}, expected {[2, 2, -2, 2, -2, 2, -2]}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = double_array_elements([1, -1, 1, -1, 1, -1, 1, -1, -999999999])
        assert result == [2, -2, 2, -2, 2, -2, 2, -2, -1999999998], f"Test 252 failed: got {result}, expected {[2, -2, 2, -2, 2, -2, 2, -2, -1999999998]}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = double_array_elements([1, -1, 1, -1, 1, -1, -1, -3])
        assert result == [2, -2, 2, -2, 2, -2, -2, -6], f"Test 253 failed: got {result}, expected {[2, -2, 2, -2, 2, -2, -2, -6]}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = double_array_elements([0, 1, -1, 1, -1, 1, -1, 1, -1, -32])
        assert result == [0, 2, -2, 2, -2, 2, -2, 2, -2, -64], f"Test 254 failed: got {result}, expected {[0, 2, -2, 2, -2, 2, -2, 2, -2, -64]}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = double_array_elements([16384, 1, -1, -1, 1, -1, 2, -1])
        assert result == [32768, 2, -2, -2, 2, -2, 4, -2], f"Test 255 failed: got {result}, expected {[32768, 2, -2, -2, 2, -2, 4, -2]}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = double_array_elements([-1, 1, -1, 1, -1, 1, -1, 1])
        assert result == [-2, 2, -2, 2, -2, 2, -2, 2], f"Test 256 failed: got {result}, expected {[-2, 2, -2, 2, -2, 2, -2, 2]}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = double_array_elements([1, -1, 1, -1, 1, 1, -1, 0, 0, 0, 0])
        assert result == [2, -2, 2, -2, 2, 2, -2, 0, 0, 0, 0], f"Test 257 failed: got {result}, expected {[2, -2, 2, -2, 2, 2, -2, 0, 0, 0, 0]}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = double_array_elements([1, -1, 1, -1, 1, -1, 1, -1, 0, 50])
        assert result == [2, -2, 2, -2, 2, -2, 2, -2, 0, 100], f"Test 258 failed: got {result}, expected {[2, -2, 2, -2, 2, -2, 2, -2, 0, 100]}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = double_array_elements([-99, -1, 1, -1, 1, -1, 1, -1, 1])
        assert result == [-198, -2, 2, -2, 2, -2, 2, -2, 2], f"Test 259 failed: got {result}, expected {[-198, -2, 2, -2, 2, -2, 2, -2, 2]}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = double_array_elements([0, 0, -1, 1, -1, 1, -1, 1, -1, 1])
        assert result == [0, 0, -2, 2, -2, 2, -2, 2, -2, 2], f"Test 260 failed: got {result}, expected {[0, 0, -2, 2, -2, 2, -2, 2, -2, 2]}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = double_array_elements([-1, 1, -1, 1, -1, 1, -1, 50, 0])
        assert result == [-2, 2, -2, 2, -2, 2, -2, 100, 0], f"Test 261 failed: got {result}, expected {[-2, 2, -2, 2, -2, 2, -2, 100, 0]}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = double_array_elements([1, -1, 1, -1, 1, -1, 1, -1, 999999999, 0])
        assert result == [2, -2, 2, -2, 2, -2, 2, -2, 1999999998, 0], f"Test 262 failed: got {result}, expected {[2, -2, 2, -2, 2, -2, 2, -2, 1999999998, 0]}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = double_array_elements([1, -1, 1, 1, -1, 1, -1, 10, 42, -6])
        assert result == [2, -2, 2, 2, -2, 2, -2, 20, 84, -12], f"Test 263 failed: got {result}, expected {[2, -2, 2, 2, -2, 2, -2, 20, 84, -12]}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = double_array_elements([1, -1, 1, -1, 1, -1, 1, -1, 0, 0])
        assert result == [2, -2, 2, -2, 2, -2, 2, -2, 0, 0], f"Test 264 failed: got {result}, expected {[2, -2, 2, -2, 2, -2, 2, -2, 0, 0]}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = double_array_elements([123456789, 0])
        assert result == [246913578, 0], f"Test 265 failed: got {result}, expected {[246913578, 0]}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = double_array_elements([4, 0])
        assert result == [8, 0], f"Test 266 failed: got {result}, expected {[8, 0]}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = double_array_elements([123456789, 16384, 0])
        assert result == [246913578, 32768, 0], f"Test 267 failed: got {result}, expected {[246913578, 32768, 0]}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = double_array_elements([123456789, 0, 0, -2])
        assert result == [246913578, 0, 0, -4], f"Test 268 failed: got {result}, expected {[246913578, 0, 0, -4]}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = double_array_elements([31, 0])
        assert result == [62, 0], f"Test 269 failed: got {result}, expected {[62, 0]}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = double_array_elements([0, 123456789, 0])
        assert result == [0, 246913578, 0], f"Test 270 failed: got {result}, expected {[0, 246913578, 0]}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = double_array_elements([20])
        assert result == [40], f"Test 271 failed: got {result}, expected {[40]}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = double_array_elements([123456787])
        assert result == [246913574], f"Test 272 failed: got {result}, expected {[246913574]}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = double_array_elements([0, 123456790, 101])
        assert result == [0, 246913580, 202], f"Test 273 failed: got {result}, expected {[0, 246913580, 202]}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = double_array_elements([-123456789, -170141183460469231731687303715884105728])
        assert result == [-246913578, -340282366920938463463374607431768211456], f"Test 274 failed: got {result}, expected {[-246913578, -340282366920938463463374607431768211456]}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = double_array_elements([-42, 123456789, 11, -512])
        assert result == [-84, 246913578, 22, -1024], f"Test 275 failed: got {result}, expected {[-84, 246913578, 22, -1024]}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = double_array_elements([2000, -123456788])
        assert result == [4000, -246913576], f"Test 276 failed: got {result}, expected {[4000, -246913576]}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = double_array_elements([-123456788, 123456790, 0])
        assert result == [-246913576, 246913580, 0], f"Test 277 failed: got {result}, expected {[-246913576, 246913580, 0]}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = double_array_elements([-123456789, 0])
        assert result == [-246913578, 0], f"Test 278 failed: got {result}, expected {[-246913578, 0]}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = double_array_elements([-2000])
        assert result == [-4000], f"Test 279 failed: got {result}, expected {[-4000]}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = double_array_elements([-123456789, -99])
        assert result == [-246913578, -198], f"Test 280 failed: got {result}, expected {[-246913578, -198]}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = double_array_elements([-123456790, 0, 123456790, 0, 93])
        assert result == [-246913580, 0, 246913580, 0, 186], f"Test 281 failed: got {result}, expected {[-246913580, 0, 246913580, 0, 186]}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = double_array_elements([8192, 170141183460469231731687303715884105727, 0, -15])
        assert result == [16384, 340282366920938463463374607431768211454, 0, -30], f"Test 282 failed: got {result}, expected {[16384, 340282366920938463463374607431768211454, 0, -30]}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = double_array_elements([-123456789, 16, 0, 60])
        assert result == [-246913578, 32, 0, 120], f"Test 283 failed: got {result}, expected {[-246913578, 32, 0, 120]}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = double_array_elements([-123456789, -30])
        assert result == [-246913578, -60], f"Test 284 failed: got {result}, expected {[-246913578, -60]}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = double_array_elements([-123456789, -7])
        assert result == [-246913578, -14], f"Test 285 failed: got {result}, expected {[-246913578, -14]}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = double_array_elements([-123456789, 512, 0])
        assert result == [-246913578, 1024, 0], f"Test 286 failed: got {result}, expected {[-246913578, 1024, 0]}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = double_array_elements([-2147483648, 2147483647, 0, 496])
        assert result == [-4294967296, 4294967294, 0, 992], f"Test 287 failed: got {result}, expected {[-4294967296, 4294967294, 0, 992]}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = double_array_elements([-2147483648, 2147483647, -20])
        assert result == [-4294967296, 4294967294, -40], f"Test 288 failed: got {result}, expected {[-4294967296, 4294967294, -40]}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = double_array_elements([2147483648, 0])
        assert result == [4294967296, 0], f"Test 289 failed: got {result}, expected {[4294967296, 0]}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = double_array_elements([-2147483648, 2147483647])
        assert result == [-4294967296, 4294967294], f"Test 290 failed: got {result}, expected {[-4294967296, 4294967294]}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = double_array_elements([2147483647])
        assert result == [4294967294], f"Test 291 failed: got {result}, expected {[4294967294]}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = double_array_elements([-2147483648, 2147483647, 9, -512])
        assert result == [-4294967296, 4294967294, 18, -1024], f"Test 292 failed: got {result}, expected {[-4294967296, 4294967294, 18, -1024]}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = double_array_elements([13, 2147483647, 0, -123456789])
        assert result == [26, 4294967294, 0, -246913578], f"Test 293 failed: got {result}, expected {[26, 4294967294, 0, -246913578]}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = double_array_elements([-2147483648, -7, 0])
        assert result == [-4294967296, -14, 0], f"Test 294 failed: got {result}, expected {[-4294967296, -14, 0]}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = double_array_elements([-2147483648])
        assert result == [-4294967296], f"Test 295 failed: got {result}, expected {[-4294967296]}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = double_array_elements([-512, 512])
        assert result == [-1024, 1024], f"Test 296 failed: got {result}, expected {[-1024, 1024]}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = double_array_elements([2147483646, -2147483650, -9, 11])
        assert result == [4294967292, -4294967300, -18, 22], f"Test 297 failed: got {result}, expected {[4294967292, -4294967300, -18, 22]}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = double_array_elements([0, 23])
        assert result == [0, 46], f"Test 298 failed: got {result}, expected {[0, 46]}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = double_array_elements([0, -2147483650, 0, -999999999, 17])
        assert result == [0, -4294967300, 0, -1999999998, 34], f"Test 299 failed: got {result}, expected {[0, -4294967300, 0, -1999999998, 34]}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = double_array_elements([-999999999, 0])
        assert result == [-1999999998, 0], f"Test 300 failed: got {result}, expected {[-1999999998, 0]}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = double_array_elements([999999999, -999999999, 0, 0])
        assert result == [1999999998, -1999999998, 0, 0], f"Test 301 failed: got {result}, expected {[1999999998, -1999999998, 0, 0]}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = double_array_elements([-999999999, 0, 0])
        assert result == [-1999999998, 0, 0], f"Test 302 failed: got {result}, expected {[-1999999998, 0, 0]}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = double_array_elements([999999999, -999999999, 0, -2147483648, 1024, -13])
        assert result == [1999999998, -1999999998, 0, -4294967296, 2048, -26], f"Test 303 failed: got {result}, expected {[1999999998, -1999999998, 0, -4294967296, 2048, -26]}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = double_array_elements([999999999, 0, 16])
        assert result == [1999999998, 0, 32], f"Test 304 failed: got {result}, expected {[1999999998, 0, 32]}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = double_array_elements([28, -999999999, -999999999, -8192, 0])
        assert result == [56, -1999999998, -1999999998, -16384, 0], f"Test 305 failed: got {result}, expected {[56, -1999999998, -1999999998, -16384, 0]}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = double_array_elements([-1024, -999999999, 0, -10])
        assert result == [-2048, -1999999998, 0, -20], f"Test 306 failed: got {result}, expected {[-2048, -1999999998, 0, -20]}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = double_array_elements([999999999, -999999999, -1, 0])
        assert result == [1999999998, -1999999998, -2, 0], f"Test 307 failed: got {result}, expected {[1999999998, -1999999998, -2, 0]}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = double_array_elements([20, 0, 999999999, -1024])
        assert result == [40, 0, 1999999998, -2048], f"Test 308 failed: got {result}, expected {[40, 0, 1999999998, -2048]}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = double_array_elements([-42, -999999999, 0, -60])
        assert result == [-84, -1999999998, 0, -120], f"Test 309 failed: got {result}, expected {[-84, -1999999998, 0, -120]}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = double_array_elements([0, -999999999, 999999999])
        assert result == [0, -1999999998, 1999999998], f"Test 310 failed: got {result}, expected {[0, -1999999998, 1999999998]}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = double_array_elements([-999999999])
        assert result == [-1999999998], f"Test 311 failed: got {result}, expected {[-1999999998]}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = double_array_elements([999999999, -999999999, 0, 31])
        assert result == [1999999998, -1999999998, 0, 62], f"Test 312 failed: got {result}, expected {[1999999998, -1999999998, 0, 62]}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = double_array_elements([6, 2, 9, 5, 1, 4, 1, 3])
        assert result == [12, 4, 18, 10, 2, 8, 2, 6], f"Test 313 failed: got {result}, expected {[12, 4, 18, 10, 2, 8, 2, 6]}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = double_array_elements([128, 6, 2, 9, 5, 1, 4, 2, 3, 0])
        assert result == [256, 12, 4, 18, 10, 2, 8, 4, 6, 0], f"Test 314 failed: got {result}, expected {[256, 12, 4, 18, 10, 2, 8, 4, 6, 0]}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = double_array_elements([6, 2, 9, 5, 32, 4, 1, 3])
        assert result == [12, 4, 18, 10, 64, 8, 2, 6], f"Test 315 failed: got {result}, expected {[12, 4, 18, 10, 64, 8, 2, 6]}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = double_array_elements([3, 1, 1, 5, 9, 2, 6])
        assert result == [6, 2, 2, 10, 18, 4, 12], f"Test 316 failed: got {result}, expected {[6, 2, 2, 10, 18, 4, 12]}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = double_array_elements([3, 2, 4, 5, 9, -2, 6, 6])
        assert result == [6, 4, 8, 10, 18, -4, 12, 12], f"Test 317 failed: got {result}, expected {[6, 4, 8, 10, 18, -4, 12, 12]}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = double_array_elements([3, 1, 4, 1, 9, 2, 6, 0])
        assert result == [6, 2, 8, 2, 18, 4, 12, 0], f"Test 318 failed: got {result}, expected {[6, 2, 8, 2, 18, 4, 12, 0]}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = double_array_elements([3, 1, 4, 1, 5, 11, 0, 6])
        assert result == [6, 2, 8, 2, 10, 22, 0, 12], f"Test 319 failed: got {result}, expected {[6, 2, 8, 2, 10, 22, 0, 12]}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = double_array_elements([3, 1, 4, 1, 5, 9, 2, 12, -2147483648, 21])
        assert result == [6, 2, 8, 2, 10, 18, 4, 24, -4294967296, 42], f"Test 320 failed: got {result}, expected {[6, 2, 8, 2, 10, 18, 4, 24, -4294967296, 42]}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = double_array_elements([6, 2, 9, 5, 1, 4, -3000, -123456790])
        assert result == [12, 4, 18, 10, 2, 8, -6000, -246913580], f"Test 321 failed: got {result}, expected {[12, 4, 18, 10, 2, 8, -6000, -246913580]}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = double_array_elements([3, 1, 4, 1, 5, 9, 2, 6, -6, 0, -3])
        assert result == [6, 2, 8, 2, 10, 18, 4, 12, -12, 0, -6], f"Test 322 failed: got {result}, expected {[6, 2, 8, 2, 10, 18, 4, 12, -12, 0, -6]}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = double_array_elements([0, 6, 2, 9, 5, 1, 4, 1, 3, 0, 0])
        assert result == [0, 12, 4, 18, 10, 2, 8, 2, 6, 0, 0], f"Test 323 failed: got {result}, expected {[0, 12, 4, 18, 10, 2, 8, 2, 6, 0, 0]}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = double_array_elements([3, 4, 1, 5, 10, 2, 6])
        assert result == [6, 8, 2, 10, 20, 4, 12], f"Test 324 failed: got {result}, expected {[6, 8, 2, 10, 20, 4, 12]}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = double_array_elements([3, 1, 4, 1, 5, 9, 2, 21, 9223372036854775807, -7])
        assert result == [6, 2, 8, 2, 10, 18, 4, 42, 18446744073709551614, -14], f"Test 325 failed: got {result}, expected {[6, 2, 8, 2, 10, 18, 4, 42, 18446744073709551614, -14]}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = double_array_elements([6, 2, 9, 5, 1, 4, 3, 0])
        assert result == [12, 4, 18, 10, 2, 8, 6, 0], f"Test 326 failed: got {result}, expected {[12, 4, 18, 10, 2, 8, 6, 0]}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = double_array_elements([3, 2, 4, 1, 5, 9, -999999999, 6, 0])
        assert result == [6, 4, 8, 2, 10, 18, -1999999998, 12, 0], f"Test 327 failed: got {result}, expected {[6, 4, 8, 2, 10, 18, -1999999998, 12, 0]}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = double_array_elements([8, 4611686018427387904, 14, 10, 3, 0])
        assert result == [16, 9223372036854775808, 28, 20, 6, 0], f"Test 328 failed: got {result}, expected {[16, 9223372036854775808, 28, 20, 6, 0]}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = double_array_elements([17, 9, 0, 3, 5, 7, 8, -999999999999999999999999999999999999999999])
        assert result == [34, 18, 0, 6, 10, 14, 16, -1999999999999999999999999999999999999999998], f"Test 329 failed: got {result}, expected {[34, 18, 0, 6, 10, 14, 16, -1999999999999999999999999999999999999999998]}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = double_array_elements([9, 0, 3, 5, 7, 6, 8])
        assert result == [18, 0, 6, 10, 14, 12, 16], f"Test 330 failed: got {result}, expected {[18, 0, 6, 10, 14, 12, 16]}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = double_array_elements([2147483648, -1000, -14, 9, 0, 3, 6, 7, 6, 8])
        assert result == [4294967296, -2000, -28, 18, 0, 6, 12, 14, 12, 16], f"Test 331 failed: got {result}, expected {[4294967296, -2000, -28, 18, 0, 6, 12, 14, 12, 16]}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = double_array_elements([8, 6, 5, 3, 2048, 9, 0, -4611686018427387904, 0])
        assert result == [16, 12, 10, 6, 4096, 18, 0, -9223372036854775808, 0], f"Test 332 failed: got {result}, expected {[16, 12, 10, 6, 4096, 18, 0, -9223372036854775808, 0]}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = double_array_elements([6, -7, 5, 3, 0, 9, -42])
        assert result == [12, -14, 10, 6, 0, 18, -84], f"Test 333 failed: got {result}, expected {[12, -14, 10, 6, 0, 18, -84]}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = double_array_elements([9, 0, 3, 4, 7, 6, 8])
        assert result == [18, 0, 6, 8, 14, 12, 16], f"Test 334 failed: got {result}, expected {[18, 0, 6, 8, 14, 12, 16]}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = double_array_elements([8, 6, 7, 5, 3, 0, 170141183460469231731687303715884105727])
        assert result == [16, 12, 14, 10, 6, 0, 340282366920938463463374607431768211454], f"Test 335 failed: got {result}, expected {[16, 12, 14, 10, 6, 0, 340282366920938463463374607431768211454]}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = double_array_elements([9, 0, 3, 5, 7, 6, 8, -123456788, 0, 0])
        assert result == [18, 0, 6, 10, 14, 12, 16, -246913576, 0, 0], f"Test 336 failed: got {result}, expected {[18, 0, 6, 10, 14, 12, 16, -246913576, 0, 0]}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = double_array_elements([8, 6, 7, 5, 3, 0, 9, 0])
        assert result == [16, 12, 14, 10, 6, 0, 18, 0], f"Test 337 failed: got {result}, expected {[16, 12, 14, 10, 6, 0, 18, 0]}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = double_array_elements([9, 3, 7, 6, 8])
        assert result == [18, 6, 14, 12, 16], f"Test 338 failed: got {result}, expected {[18, 6, 14, 12, 16]}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = double_array_elements([8, 6, 7, 5, 3, 9, 20])
        assert result == [16, 12, 14, 10, 6, 18, 40], f"Test 339 failed: got {result}, expected {[16, 12, 14, 10, 6, 18, 40]}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = double_array_elements([8, 7, 5, 3, 0, 9, 2147483647])
        assert result == [16, 14, 10, 6, 0, 18, 4294967294], f"Test 340 failed: got {result}, expected {[16, 14, 10, 6, 0, 18, 4294967294]}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = double_array_elements([8, 6, 7, 5, 3, 9])
        assert result == [16, 12, 14, 10, 6, 18], f"Test 341 failed: got {result}, expected {[16, 12, 14, 10, 6, 18]}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = double_array_elements([8, 6, 7, 5, 0, 9, -6])
        assert result == [16, 12, 14, 10, 0, 18, -12], f"Test 342 failed: got {result}, expected {[16, 12, 14, 10, 0, 18, -12]}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = double_array_elements([15, -30, 45, 60, -60, -21, 0])
        assert result == [30, -60, 90, 120, -120, -42, 0], f"Test 343 failed: got {result}, expected {[30, -60, 90, 120, -120, -42, 0]}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = double_array_elements([0, -60, 60, 45, -30, 30, -15, 15])
        assert result == [0, -120, 120, 90, -60, 60, -30, 30], f"Test 344 failed: got {result}, expected {[0, -120, 120, 90, -60, 60, -30, 30]}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = double_array_elements([15, 15, 30, -30, 45, -45, 60, -60])
        assert result == [30, 30, 60, -60, 90, -90, 120, -120], f"Test 345 failed: got {result}, expected {[30, 30, 60, -60, 90, -90, 120, -120]}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = double_array_elements([15, -15, 30, -30, 45, -45, -60, 17, -2000])
        assert result == [30, -30, 60, -60, 90, -90, -120, 34, -4000], f"Test 346 failed: got {result}, expected {[30, -30, 60, -60, 90, -90, -120, 34, -4000]}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    # Test case 347
    try:
        result = double_array_elements([-60, 60, -45, 45, -30, 30, -15, 15, -2000])
        assert result == [-120, 120, -90, 90, -60, 60, -30, 30, -4000], f"Test 347 failed: got {result}, expected {[-120, 120, -90, 90, -60, 60, -30, 30, -4000]}"
        print(f"Test 347 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 347 failed: {e}")
        test_results.append(False)

    # Test case 348
    try:
        result = double_array_elements([-60, 60, -45, 45, -30, 30, -15, 15])
        assert result == [-120, 120, -90, 90, -60, 60, -30, 30], f"Test 348 failed: got {result}, expected {[-120, 120, -90, 90, -60, 60, -30, 30]}"
        print(f"Test 348 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 348 failed: {e}")
        test_results.append(False)

    # Test case 349
    try:
        result = double_array_elements([3000, -60, 60, -45, 45, -30, 30, -15, 15, -60])
        assert result == [6000, -120, 120, -90, 90, -60, 60, -30, 30, -120], f"Test 349 failed: got {result}, expected {[6000, -120, 120, -90, 90, -60, 60, -30, 30, -120]}"
        print(f"Test 349 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 349 failed: {e}")
        test_results.append(False)

    # Test case 350
    try:
        result = double_array_elements([14, -15, 30, -30, 45, -44, 60, -60])
        assert result == [28, -30, 60, -60, 90, -88, 120, -120], f"Test 350 failed: got {result}, expected {[28, -30, 60, -60, 90, -88, 120, -120]}"
        print(f"Test 350 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 350 failed: {e}")
        test_results.append(False)

    # Test case 351
    try:
        result = double_array_elements([15, -15, -4611686018427387904, 45, -45, 60, -60])
        assert result == [30, -30, -9223372036854775808, 90, -90, 120, -120], f"Test 351 failed: got {result}, expected {[30, -30, -9223372036854775808, 90, -90, 120, -120]}"
        print(f"Test 351 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 351 failed: {e}")
        test_results.append(False)

    # Test case 352
    try:
        result = double_array_elements([15, -15, 30, -30, 45, -45, 60, -60, 0])
        assert result == [30, -30, 60, -60, 90, -90, 120, -120, 0], f"Test 352 failed: got {result}, expected {[30, -30, 60, -60, 90, -90, 120, -120, 0]}"
        print(f"Test 352 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 352 failed: {e}")
        test_results.append(False)

    # Test case 353
    try:
        result = double_array_elements([0, 8, -60, 60, -45, -30, 30, 15])
        assert result == [0, 16, -120, 120, -90, -60, 60, 30], f"Test 353 failed: got {result}, expected {[0, 16, -120, 120, -90, -60, 60, 30]}"
        print(f"Test 353 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 353 failed: {e}")
        test_results.append(False)

    # Test case 354
    try:
        result = double_array_elements([15, -15, 30, 9223372036854775807, 45, -45, 60, -60, 64])
        assert result == [30, -30, 60, 18446744073709551614, 90, -90, 120, -120, 128], f"Test 354 failed: got {result}, expected {[30, -30, 60, 18446744073709551614, 90, -90, 120, -120, 128]}"
        print(f"Test 354 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 354 failed: {e}")
        test_results.append(False)

    # Test case 355
    try:
        result = double_array_elements([-15, 30, -30, 45, -45, 60, -60])
        assert result == [-30, 60, -60, 90, -90, 120, -120], f"Test 355 failed: got {result}, expected {[-30, 60, -60, 90, -90, 120, -120]}"
        print(f"Test 355 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 355 failed: {e}")
        test_results.append(False)

    # Test case 356
    try:
        result = double_array_elements([-60, 60, -45, 45, 32, 30, -15, 14, 0])
        assert result == [-120, 120, -90, 90, 64, 60, -30, 28, 0], f"Test 356 failed: got {result}, expected {[-120, 120, -90, 90, 64, 60, -30, 28, 0]}"
        print(f"Test 356 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 356 failed: {e}")
        test_results.append(False)

    # Test case 357
    try:
        result = double_array_elements([0, 15, -15, 30, -30, 45, -45, -60, 0])
        assert result == [0, 30, -30, 60, -60, 90, -90, -120, 0], f"Test 357 failed: got {result}, expected {[0, 30, -30, 60, -60, 90, -90, -120, 0]}"
        print(f"Test 357 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 357 failed: {e}")
        test_results.append(False)

    # Test case 358
    try:
        result = double_array_elements([1, 3, 5, 7, 9, 11, 15, 0])
        assert result == [2, 6, 10, 14, 18, 22, 30, 0], f"Test 358 failed: got {result}, expected {[2, 6, 10, 14, 18, 22, 30, 0]}"
        print(f"Test 358 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 358 failed: {e}")
        test_results.append(False)

    # Test case 359
    try:
        result = double_array_elements([1, 3, 5, 9, 11, 14, 14])
        assert result == [2, 6, 10, 18, 22, 28, 28], f"Test 359 failed: got {result}, expected {[2, 6, 10, 18, 22, 28, 28]}"
        print(f"Test 359 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 359 failed: {e}")
        test_results.append(False)

    # Test case 360
    try:
        result = double_array_elements([1, 3, 10, 7, 0, 11, 11])
        assert result == [2, 6, 20, 14, 0, 22, 22], f"Test 360 failed: got {result}, expected {[2, 6, 20, 14, 0, 22, 22]}"
        print(f"Test 360 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 360 failed: {e}")
        test_results.append(False)

    # Test case 361
    try:
        result = double_array_elements([0, 3, 5, 7, 9, 11, 13, 15])
        assert result == [0, 6, 10, 14, 18, 22, 26, 30], f"Test 361 failed: got {result}, expected {[0, 6, 10, 14, 18, 22, 26, 30]}"
        print(f"Test 361 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 361 failed: {e}")
        test_results.append(False)

    # Test case 362
    try:
        result = double_array_elements([1, 3, -5, 7, 9, 11, 13])
        assert result == [2, 6, -10, 14, 18, 22, 26], f"Test 362 failed: got {result}, expected {[2, 6, -10, 14, 18, 22, 26]}"
        print(f"Test 362 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 362 failed: {e}")
        test_results.append(False)

    # Test case 363
    try:
        result = double_array_elements([15, 13, 11, 9, 7, 5, 3, 1])
        assert result == [30, 26, 22, 18, 14, 10, 6, 2], f"Test 363 failed: got {result}, expected {[30, 26, 22, 18, 14, 10, 6, 2]}"
        print(f"Test 363 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 363 failed: {e}")
        test_results.append(False)

    # Test case 364
    try:
        result = double_array_elements([15, 13, 11, 9, 7, 4, 3, 1])
        assert result == [30, 26, 22, 18, 14, 8, 6, 2], f"Test 364 failed: got {result}, expected {[30, 26, 22, 18, 14, 8, 6, 2]}"
        print(f"Test 364 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 364 failed: {e}")
        test_results.append(False)

    # Test case 365
    try:
        result = double_array_elements([1, 3, 5, 7, 9, 11, 13, 15, 0, -256])
        assert result == [2, 6, 10, 14, 18, 22, 26, 30, 0, -512], f"Test 365 failed: got {result}, expected {[2, 6, 10, 14, 18, 22, 26, 30, 0, -512]}"
        print(f"Test 365 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 365 failed: {e}")
        test_results.append(False)

    # Test case 366
    try:
        result = double_array_elements([3, 0, 9, 11, 13, 15, 9, 0])
        assert result == [6, 0, 18, 22, 26, 30, 18, 0], f"Test 366 failed: got {result}, expected {[6, 0, 18, 22, 26, 30, 18, 0]}"
        print(f"Test 366 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 366 failed: {e}")
        test_results.append(False)

    # Test case 367
    try:
        result = double_array_elements([10, 15, 13, 11, 9, 7, 6, 4, 1])
        assert result == [20, 30, 26, 22, 18, 14, 12, 8, 2], f"Test 367 failed: got {result}, expected {[20, 30, 26, 22, 18, 14, 12, 8, 2]}"
        print(f"Test 367 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 367 failed: {e}")
        test_results.append(False)

    # Test case 368
    try:
        result = double_array_elements([1, 3, 5, 7, 10, 11, 13, 0])
        assert result == [2, 6, 10, 14, 20, 22, 26, 0], f"Test 368 failed: got {result}, expected {[2, 6, 10, 14, 20, 22, 26, 0]}"
        print(f"Test 368 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 368 failed: {e}")
        test_results.append(False)

    # Test case 369
    try:
        result = double_array_elements([13, 11, 7, 5, 3, 0])
        assert result == [26, 22, 14, 10, 6, 0], f"Test 369 failed: got {result}, expected {[26, 22, 14, 10, 6, 0]}"
        print(f"Test 369 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 369 failed: {e}")
        test_results.append(False)

    # Test case 370
    try:
        result = double_array_elements([1, 3, 5, 7, 9, 11, 13, 15, 0])
        assert result == [2, 6, 10, 14, 18, 22, 26, 30, 0], f"Test 370 failed: got {result}, expected {[2, 6, 10, 14, 18, 22, 26, 30, 0]}"
        print(f"Test 370 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 370 failed: {e}")
        test_results.append(False)

    # Test case 371
    try:
        result = double_array_elements([-4, -6, -2, -10, -12])
        assert result == [-8, -12, -4, -20, -24], f"Test 371 failed: got {result}, expected {[-8, -12, -4, -20, -24]}"
        print(f"Test 371 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 371 failed: {e}")
        test_results.append(False)

    # Test case 372
    try:
        result = double_array_elements([0, -2, -4, -6, -8, -10, -12, 0])
        assert result == [0, -4, -8, -12, -16, -20, -24, 0], f"Test 372 failed: got {result}, expected {[0, -4, -8, -12, -16, -20, -24, 0]}"
        print(f"Test 372 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 372 failed: {e}")
        test_results.append(False)

    # Test case 373
    try:
        result = double_array_elements([-2, -4, -6, -8, -10, -12, 0])
        assert result == [-4, -8, -12, -16, -20, -24, 0], f"Test 373 failed: got {result}, expected {[-4, -8, -12, -16, -20, -24, 0]}"
        print(f"Test 373 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 373 failed: {e}")
        test_results.append(False)

    # Test case 374
    try:
        result = double_array_elements([-2, -4, -6, -8, -10, -12, 0, 0, 13, 0])
        assert result == [-4, -8, -12, -16, -20, -24, 0, 0, 26, 0], f"Test 374 failed: got {result}, expected {[-4, -8, -12, -16, -20, -24, 0, 0, 26, 0]}"
        print(f"Test 374 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 374 failed: {e}")
        test_results.append(False)

    # Test case 375
    try:
        result = double_array_elements([0, -12, -10, -4, -2, 124])
        assert result == [0, -24, -20, -8, -4, 248], f"Test 375 failed: got {result}, expected {[0, -24, -20, -8, -4, 248]}"
        print(f"Test 375 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 375 failed: {e}")
        test_results.append(False)

    # Test case 376
    try:
        result = double_array_elements([-2, -4, -8, -10, -12, 0, 0, 16384, 0])
        assert result == [-4, -8, -16, -20, -24, 0, 0, 32768, 0], f"Test 376 failed: got {result}, expected {[-4, -8, -16, -20, -24, 0, 0, 32768, 0]}"
        print(f"Test 376 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 376 failed: {e}")
        test_results.append(False)

    # Test case 377
    try:
        result = double_array_elements([0, -12, -10, -8, -5, -4, -9, 0])
        assert result == [0, -24, -20, -16, -10, -8, -18, 0], f"Test 377 failed: got {result}, expected {[0, -24, -20, -16, -10, -8, -18, 0]}"
        print(f"Test 377 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 377 failed: {e}")
        test_results.append(False)

    # Test case 378
    try:
        result = double_array_elements([-2, -6, -8, -10, -12])
        assert result == [-4, -12, -16, -20, -24], f"Test 378 failed: got {result}, expected {[-4, -12, -16, -20, -24]}"
        print(f"Test 378 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 378 failed: {e}")
        test_results.append(False)

    # Test case 379
    try:
        result = double_array_elements([-2, -6, -8, -12, -7])
        assert result == [-4, -12, -16, -24, -14], f"Test 379 failed: got {result}, expected {[-4, -12, -16, -24, -14]}"
        print(f"Test 379 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 379 failed: {e}")
        test_results.append(False)

    # Test case 380
    try:
        result = double_array_elements([-2, -4, -6, -9, -3, -12, 0, 0])
        assert result == [-4, -8, -12, -18, -6, -24, 0, 0], f"Test 380 failed: got {result}, expected {[-4, -8, -12, -18, -6, -24, 0, 0]}"
        print(f"Test 380 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 380 failed: {e}")
        test_results.append(False)

    # Test case 381
    try:
        result = double_array_elements([-2, -4, -6, -8, -12, 41, -42, 16])
        assert result == [-4, -8, -12, -16, -24, 82, -84, 32], f"Test 381 failed: got {result}, expected {[-4, -8, -12, -16, -24, 82, -84, 32]}"
        print(f"Test 381 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 381 failed: {e}")
        test_results.append(False)

    # Test case 382
    try:
        result = double_array_elements([-2, -4, -6, -8, -10, 12, 0, 20])
        assert result == [-4, -8, -12, -16, -20, 24, 0, 40], f"Test 382 failed: got {result}, expected {[-4, -8, -12, -16, -20, 24, 0, 40]}"
        print(f"Test 382 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 382 failed: {e}")
        test_results.append(False)

    # Test case 383
    try:
        result = double_array_elements([-2, -4, -6, -8, -12])
        assert result == [-4, -8, -12, -16, -24], f"Test 383 failed: got {result}, expected {[-4, -8, -12, -16, -24]}"
        print(f"Test 383 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 383 failed: {e}")
        test_results.append(False)

    # Test case 384
    try:
        result = double_array_elements([-12, -10, -8, -6, -4, -2])
        assert result == [-24, -20, -16, -12, -8, -4], f"Test 384 failed: got {result}, expected {[-24, -20, -16, -12, -8, -4]}"
        print(f"Test 384 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 384 failed: {e}")
        test_results.append(False)

    # Test case 385
    try:
        result = double_array_elements([0, 10, -30, 40, 50])
        assert result == [0, 20, -60, 80, 100], f"Test 385 failed: got {result}, expected {[0, 20, -60, 80, 100]}"
        print(f"Test 385 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 385 failed: {e}")
        test_results.append(False)

    # Test case 386
    try:
        result = double_array_elements([50, 40, 30, 20, 10, 0, 0])
        assert result == [100, 80, 60, 40, 20, 0, 0], f"Test 386 failed: got {result}, expected {[100, 80, 60, 40, 20, 0, 0]}"
        print(f"Test 386 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 386 failed: {e}")
        test_results.append(False)

    # Test case 387
    try:
        result = double_array_elements([0, 20, 20, 31, 40])
        assert result == [0, 40, 40, 62, 80], f"Test 387 failed: got {result}, expected {[0, 40, 40, 62, 80]}"
        print(f"Test 387 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 387 failed: {e}")
        test_results.append(False)

    # Test case 388
    try:
        result = double_array_elements([50, 41, 30, 20, 10, 0])
        assert result == [100, 82, 60, 40, 20, 0], f"Test 388 failed: got {result}, expected {[100, 82, 60, 40, 20, 0]}"
        print(f"Test 388 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 388 failed: {e}")
        test_results.append(False)

    # Test case 389
    try:
        result = double_array_elements([16, -30, 30, 20, 10, 0])
        assert result == [32, -60, 60, 40, 20, 0], f"Test 389 failed: got {result}, expected {[32, -60, 60, 40, 20, 0]}"
        print(f"Test 389 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 389 failed: {e}")
        test_results.append(False)

    # Test case 390
    try:
        result = double_array_elements([50, 40, 30, 10])
        assert result == [100, 80, 60, 20], f"Test 390 failed: got {result}, expected {[100, 80, 60, 20]}"
        print(f"Test 390 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 390 failed: {e}")
        test_results.append(False)

    # Test case 391
    try:
        result = double_array_elements([21, 30, 40, 50, 0])
        assert result == [42, 60, 80, 100, 0], f"Test 391 failed: got {result}, expected {[42, 60, 80, 100, 0]}"
        print(f"Test 391 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 391 failed: {e}")
        test_results.append(False)

    # Test case 392
    try:
        result = double_array_elements([50, 40, 30, 20])
        assert result == [100, 80, 60, 40], f"Test 392 failed: got {result}, expected {[100, 80, 60, 40]}"
        print(f"Test 392 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 392 failed: {e}")
        test_results.append(False)

    # Test case 393
    try:
        result = double_array_elements([10, 20, 30, 40, 50])
        assert result == [20, 40, 60, 80, 100], f"Test 393 failed: got {result}, expected {[20, 40, 60, 80, 100]}"
        print(f"Test 393 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 393 failed: {e}")
        test_results.append(False)

    # Test case 394
    try:
        result = double_array_elements([10, 28, 30, 40, -50, 42])
        assert result == [20, 56, 60, 80, -100, 84], f"Test 394 failed: got {result}, expected {[20, 56, 60, 80, -100, 84]}"
        print(f"Test 394 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 394 failed: {e}")
        test_results.append(False)

    # Test case 395
    try:
        result = double_array_elements([50, 40, 30, 20, 11])
        assert result == [100, 80, 60, 40, 22], f"Test 395 failed: got {result}, expected {[100, 80, 60, 40, 22]}"
        print(f"Test 395 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 395 failed: {e}")
        test_results.append(False)

    # Test case 396
    try:
        result = double_array_elements([50, 30, 20, 10, 124, 23, 0, 14])
        assert result == [100, 60, 40, 20, 248, 46, 0, 28], f"Test 396 failed: got {result}, expected {[100, 60, 40, 20, 248, 46, 0, 28]}"
        print(f"Test 396 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 396 failed: {e}")
        test_results.append(False)

    # Test case 397
    try:
        result = double_array_elements([50, 40, -30, 20, 10])
        assert result == [100, 80, -60, 40, 20], f"Test 397 failed: got {result}, expected {[100, 80, -60, 40, 20]}"
        print(f"Test 397 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 397 failed: {e}")
        test_results.append(False)

    # Test case 398
    try:
        result = double_array_elements([-2000, 0, -2147483648, 8128, 28, 6])
        assert result == [-4000, 0, -4294967296, 16256, 56, 12], f"Test 398 failed: got {result}, expected {[-4000, 0, -4294967296, 16256, 56, 12]}"
        print(f"Test 398 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 398 failed: {e}")
        test_results.append(False)

    # Test case 399
    try:
        result = double_array_elements([6, 28, 496, 0, 0])
        assert result == [12, 56, 992, 0, 0], f"Test 399 failed: got {result}, expected {[12, 56, 992, 0, 0]}"
        print(f"Test 399 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 399 failed: {e}")
        test_results.append(False)

    # Test case 400
    try:
        result = double_array_elements([8128, 496, 6])
        assert result == [16256, 992, 12], f"Test 400 failed: got {result}, expected {[16256, 992, 12]}"
        print(f"Test 400 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 400 failed: {e}")
        test_results.append(False)

    # Test case 401
    try:
        result = double_array_elements([6, 28, 496, 8128, -9])
        assert result == [12, 56, 992, 16256, -18], f"Test 401 failed: got {result}, expected {[12, 56, 992, 16256, -18]}"
        print(f"Test 401 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 401 failed: {e}")
        test_results.append(False)

    # Test case 402
    try:
        result = double_array_elements([8128, 28, 6, 2000])
        assert result == [16256, 56, 12, 4000], f"Test 402 failed: got {result}, expected {[16256, 56, 12, 4000]}"
        print(f"Test 402 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 402 failed: {e}")
        test_results.append(False)

    # Test case 403
    try:
        result = double_array_elements([28, 496, 8130, 0, 64])
        assert result == [56, 992, 16260, 0, 128], f"Test 403 failed: got {result}, expected {[56, 992, 16260, 0, 128]}"
        print(f"Test 403 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 403 failed: {e}")
        test_results.append(False)

    # Test case 404
    try:
        result = double_array_elements([-123456788, 0, 8128, 496, 28, 6, 0])
        assert result == [-246913576, 0, 16256, 992, 56, 12, 0], f"Test 404 failed: got {result}, expected {[-246913576, 0, 16256, 992, 56, 12, 0]}"
        print(f"Test 404 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 404 failed: {e}")
        test_results.append(False)

    # Test case 405
    try:
        result = double_array_elements([6, 28, 496, 8128, 0])
        assert result == [12, 56, 992, 16256, 0], f"Test 405 failed: got {result}, expected {[12, 56, 992, 16256, 0]}"
        print(f"Test 405 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 405 failed: {e}")
        test_results.append(False)

    # Test case 406
    try:
        result = double_array_elements([8128, 496, 28, 6, -99])
        assert result == [16256, 992, 56, 12, -198], f"Test 406 failed: got {result}, expected {[16256, 992, 56, 12, -198]}"
        print(f"Test 406 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 406 failed: {e}")
        test_results.append(False)

    # Test case 407
    try:
        result = double_array_elements([-15, -496, 8128])
        assert result == [-30, -992, 16256], f"Test 407 failed: got {result}, expected {[-30, -992, 16256]}"
        print(f"Test 407 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 407 failed: {e}")
        test_results.append(False)

    # Test case 408
    try:
        result = double_array_elements([8128, 496, 28, 12])
        assert result == [16256, 992, 56, 24], f"Test 408 failed: got {result}, expected {[16256, 992, 56, 24]}"
        print(f"Test 408 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 408 failed: {e}")
        test_results.append(False)

    # Test case 409
    try:
        result = double_array_elements([0, 0, 8128, 496, 28, 6, 0])
        assert result == [0, 0, 16256, 992, 56, 12, 0], f"Test 409 failed: got {result}, expected {[0, 0, 16256, 992, 56, 12, 0]}"
        print(f"Test 409 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 409 failed: {e}")
        test_results.append(False)

    # Test case 410
    try:
        result = double_array_elements([0, 0, 496, 28, 6])
        assert result == [0, 0, 992, 56, 12], f"Test 410 failed: got {result}, expected {[0, 0, 992, 56, 12]}"
        print(f"Test 410 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 410 failed: {e}")
        test_results.append(False)

    # Test case 411
    try:
        result = double_array_elements([28, 23, 8128])
        assert result == [56, 46, 16256], f"Test 411 failed: got {result}, expected {[56, 46, 16256]}"
        print(f"Test 411 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 411 failed: {e}")
        test_results.append(False)

    # Test case 412
    try:
        result = double_array_elements([8128, 496, 28])
        assert result == [16256, 992, 56], f"Test 412 failed: got {result}, expected {[16256, 992, 56]}"
        print(f"Test 412 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 412 failed: {e}")
        test_results.append(False)

    # Test case 413
    try:
        result = double_array_elements([0, 155, 124, 93, 62, 31, 5, 0])
        assert result == [0, 310, 248, 186, 124, 62, 10, 0], f"Test 413 failed: got {result}, expected {[0, 310, 248, 186, 124, 62, 10, 0]}"
        print(f"Test 413 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 413 failed: {e}")
        test_results.append(False)

    # Test case 414
    try:
        result = double_array_elements([31, 93, 124, 155, 8130, 0, 0])
        assert result == [62, 186, 248, 310, 16260, 0, 0], f"Test 414 failed: got {result}, expected {[62, 186, 248, 310, 16260, 0, 0]}"
        print(f"Test 414 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 414 failed: {e}")
        test_results.append(False)

    # Test case 415
    try:
        result = double_array_elements([0, 155, 124, 93, 62, 31])
        assert result == [0, 310, 248, 186, 124, 62], f"Test 415 failed: got {result}, expected {[0, 310, 248, 186, 124, 62]}"
        print(f"Test 415 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 415 failed: {e}")
        test_results.append(False)

    # Test case 416
    try:
        result = double_array_elements([155, 124, 93, 62, 31, 0])
        assert result == [310, 248, 186, 124, 62, 0], f"Test 416 failed: got {result}, expected {[310, 248, 186, 124, 62, 0]}"
        print(f"Test 416 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 416 failed: {e}")
        test_results.append(False)

    # Test case 417
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, 155, 124, 93, 62, 31])
        assert result == [-340282366920938463463374607431768211456, 310, 248, 186, 124, 62], f"Test 417 failed: got {result}, expected {[-340282366920938463463374607431768211456, 310, 248, 186, 124, 62]}"
        print(f"Test 417 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 417 failed: {e}")
        test_results.append(False)

    # Test case 418
    try:
        result = double_array_elements([31, 62, 93, 124, 155, -496, 13, 123456787, 8128, -123456788])
        assert result == [62, 124, 186, 248, 310, -992, 26, 246913574, 16256, -246913576], f"Test 418 failed: got {result}, expected {[62, 124, 186, 248, 310, -992, 26, 246913574, 16256, -246913576]}"
        print(f"Test 418 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 418 failed: {e}")
        test_results.append(False)

    # Test case 419
    try:
        result = double_array_elements([155, 125, 93, 62, 31, -15])
        assert result == [310, 250, 186, 124, 62, -30], f"Test 419 failed: got {result}, expected {[310, 250, 186, 124, 62, -30]}"
        print(f"Test 419 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 419 failed: {e}")
        test_results.append(False)

    # Test case 420
    try:
        result = double_array_elements([124, 94, 62])
        assert result == [248, 188, 124], f"Test 420 failed: got {result}, expected {[248, 188, 124]}"
        print(f"Test 420 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 420 failed: {e}")
        test_results.append(False)

    # Test case 421
    try:
        result = double_array_elements([0, 0, 0, 155, 124, 93, 62, 31])
        assert result == [0, 0, 0, 310, 248, 186, 124, 62], f"Test 421 failed: got {result}, expected {[0, 0, 0, 310, 248, 186, 124, 62]}"
        print(f"Test 421 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 421 failed: {e}")
        test_results.append(False)

    # Test case 422
    try:
        result = double_array_elements([155, 125, 93, 62, 31])
        assert result == [310, 250, 186, 124, 62], f"Test 422 failed: got {result}, expected {[310, 250, 186, 124, 62]}"
        print(f"Test 422 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 422 failed: {e}")
        test_results.append(False)

    # Test case 423
    try:
        result = double_array_elements([31, 62, 93, 124, 155, 0, 0, 0])
        assert result == [62, 124, 186, 248, 310, 0, 0, 0], f"Test 423 failed: got {result}, expected {[62, 124, 186, 248, 310, 0, 0, 0]}"
        print(f"Test 423 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 423 failed: {e}")
        test_results.append(False)

    # Test case 424
    try:
        result = double_array_elements([31, 62, 124, 155, 100, 2048])
        assert result == [62, 124, 248, 310, 200, 4096], f"Test 424 failed: got {result}, expected {[62, 124, 248, 310, 200, 4096]}"
        print(f"Test 424 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 424 failed: {e}")
        test_results.append(False)

    # Test case 425
    try:
        result = double_array_elements([155, 247, 93, 62, 31, -3000])
        assert result == [310, 494, 186, 124, 62, -6000], f"Test 425 failed: got {result}, expected {[310, 494, 186, 124, 62, -6000]}"
        print(f"Test 425 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 425 failed: {e}")
        test_results.append(False)

    # Test case 426
    try:
        result = double_array_elements([155, 124, 10, 62, 31, 0, 0])
        assert result == [310, 248, 20, 124, 62, 0, 0], f"Test 426 failed: got {result}, expected {[310, 248, 20, 124, 62, 0, 0]}"
        print(f"Test 426 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 426 failed: {e}")
        test_results.append(False)

    # Test case 427
    try:
        result = double_array_elements([155, 124, 93, 62, 31])
        assert result == [310, 248, 186, 124, 62], f"Test 427 failed: got {result}, expected {[310, 248, 186, 124, 62]}"
        print(f"Test 427 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 427 failed: {e}")
        test_results.append(False)

    # Test case 428
    try:
        result = double_array_elements([0, 1, 0, 1, 0, 0, 0, 1, 0, -12, 4, 0])
        assert result == [0, 2, 0, 2, 0, 0, 0, 2, 0, -24, 8, 0], f"Test 428 failed: got {result}, expected {[0, 2, 0, 2, 0, 0, 0, 2, 0, -24, 8, 0]}"
        print(f"Test 428 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 428 failed: {e}")
        test_results.append(False)

    # Test case 429
    try:
        result = double_array_elements([0, 1, 1, 0, 1, 0, 1, 0])
        assert result == [0, 2, 2, 0, 2, 0, 2, 0], f"Test 429 failed: got {result}, expected {[0, 2, 2, 0, 2, 0, 2, 0]}"
        print(f"Test 429 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 429 failed: {e}")
        test_results.append(False)

    # Test case 430
    try:
        result = double_array_elements([0, 0, 0, 1, 1, 0, 1, 0, 0, 0])
        assert result == [0, 0, 0, 2, 2, 0, 2, 0, 0, 0], f"Test 430 failed: got {result}, expected {[0, 0, 0, 2, 2, 0, 2, 0, 0, 0]}"
        print(f"Test 430 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 430 failed: {e}")
        test_results.append(False)

    # Test case 431
    try:
        result = double_array_elements([0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0])
        assert result == [0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0], f"Test 431 failed: got {result}, expected {[0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0]}"
        print(f"Test 431 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 431 failed: {e}")
        test_results.append(False)

    # Test case 432
    try:
        result = double_array_elements([-32, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])
        assert result == [-64, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0], f"Test 432 failed: got {result}, expected {[-64, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0]}"
        print(f"Test 432 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 432 failed: {e}")
        test_results.append(False)

    # Test case 433
    try:
        result = double_array_elements([0, 1, 0, 1, -64, 1, 0, 1, 0])
        assert result == [0, 2, 0, 2, -128, 2, 0, 2, 0], f"Test 433 failed: got {result}, expected {[0, 2, 0, 2, -128, 2, 0, 2, 0]}"
        print(f"Test 433 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 433 failed: {e}")
        test_results.append(False)

    # Test case 434
    try:
        result = double_array_elements([0, 1, 0, 1, 0, 1, 1, 0, 0])
        assert result == [0, 2, 0, 2, 0, 2, 2, 0, 0], f"Test 434 failed: got {result}, expected {[0, 2, 0, 2, 0, 2, 2, 0, 0]}"
        print(f"Test 434 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 434 failed: {e}")
        test_results.append(False)

    # Test case 435
    try:
        result = double_array_elements([0, 0, 2, 1, 0, 0, 1, 0])
        assert result == [0, 0, 4, 2, 0, 0, 2, 0], f"Test 435 failed: got {result}, expected {[0, 0, 4, 2, 0, 0, 2, 0]}"
        print(f"Test 435 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 435 failed: {e}")
        test_results.append(False)

    # Test case 436
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, 0, 1, 1, 0, 1, 0, 1, 0, -41, -14])
        assert result == [-340282366920938463463374607431768211456, 0, 2, 2, 0, 2, 0, 2, 0, -82, -28], f"Test 436 failed: got {result}, expected {[-340282366920938463463374607431768211456, 0, 2, 2, 0, 2, 0, 2, 0, -82, -28]}"
        print(f"Test 436 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 436 failed: {e}")
        test_results.append(False)

    # Test case 437
    try:
        result = double_array_elements([0, 0, 0, 1, 0, 1, 0, 1, 0, 2147483647])
        assert result == [0, 0, 0, 2, 0, 2, 0, 2, 0, 4294967294], f"Test 437 failed: got {result}, expected {[0, 0, 0, 2, 0, 2, 0, 2, 0, 4294967294]}"
        print(f"Test 437 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 437 failed: {e}")
        test_results.append(False)

    # Test case 438
    try:
        result = double_array_elements([0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])
        assert result == [0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0], f"Test 438 failed: got {result}, expected {[0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0]}"
        print(f"Test 438 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 438 failed: {e}")
        test_results.append(False)

    # Test case 439
    try:
        result = double_array_elements([1, 0, 1, 0, 1, 0, 1, 0, 0, 0])
        assert result == [2, 0, 2, 0, 2, 0, 2, 0, 0, 0], f"Test 439 failed: got {result}, expected {[2, 0, 2, 0, 2, 0, 2, 0, 0, 0]}"
        print(f"Test 439 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 439 failed: {e}")
        test_results.append(False)

    # Test case 440
    try:
        result = double_array_elements([0, 1, 1, 0, 0, 1, 0, 123456789, 1024, 0])
        assert result == [0, 2, 2, 0, 0, 2, 0, 246913578, 2048, 0], f"Test 440 failed: got {result}, expected {[0, 2, 2, 0, 0, 2, 0, 246913578, 2048, 0]}"
        print(f"Test 440 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 440 failed: {e}")
        test_results.append(False)

    # Test case 441
    try:
        result = double_array_elements([1000, -1000, 2000, 3000, -3000, 0])
        assert result == [2000, -2000, 4000, 6000, -6000, 0], f"Test 441 failed: got {result}, expected {[2000, -2000, 4000, 6000, -6000, 0]}"
        print(f"Test 441 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 441 failed: {e}")
        test_results.append(False)

    # Test case 442
    try:
        result = double_array_elements([30, 3000, -2000, 2000, -1000, 1000])
        assert result == [60, 6000, -4000, 4000, -2000, 2000], f"Test 442 failed: got {result}, expected {[60, 6000, -4000, 4000, -2000, 2000]}"
        print(f"Test 442 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 442 failed: {e}")
        test_results.append(False)

    # Test case 443
    try:
        result = double_array_elements([1000, -1000, 2000, -2000, 3000, -3000, -123456790, 101])
        assert result == [2000, -2000, 4000, -4000, 6000, -6000, -246913580, 202], f"Test 443 failed: got {result}, expected {[2000, -2000, 4000, -4000, 6000, -6000, -246913580, 202]}"
        print(f"Test 443 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 443 failed: {e}")
        test_results.append(False)

    # Test case 444
    try:
        result = double_array_elements([1000, -1000, -2000, 3000, -3000, 0])
        assert result == [2000, -2000, -4000, 6000, -6000, 0], f"Test 444 failed: got {result}, expected {[2000, -2000, -4000, 6000, -6000, 0]}"
        print(f"Test 444 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 444 failed: {e}")
        test_results.append(False)

    # Test case 445
    try:
        result = double_array_elements([1000, 0, 2000, -2000, 3000, -3000])
        assert result == [2000, 0, 4000, -4000, 6000, -6000], f"Test 445 failed: got {result}, expected {[2000, 0, 4000, -4000, 6000, -6000]}"
        print(f"Test 445 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 445 failed: {e}")
        test_results.append(False)

    # Test case 446
    try:
        result = double_array_elements([1000, -1000, -2000, 3000, -3000])
        assert result == [2000, -2000, -4000, 6000, -6000], f"Test 446 failed: got {result}, expected {[2000, -2000, -4000, 6000, -6000]}"
        print(f"Test 446 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 446 failed: {e}")
        test_results.append(False)

    # Test case 447
    try:
        result = double_array_elements([-1000, 2000, -1999, 3000, -3000, 0])
        assert result == [-2000, 4000, -3998, 6000, -6000, 0], f"Test 447 failed: got {result}, expected {[-2000, 4000, -3998, 6000, -6000, 0]}"
        print(f"Test 447 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 447 failed: {e}")
        test_results.append(False)

    # Test case 448
    try:
        result = double_array_elements([22, -3000, 3000, 0, 2000, -1000, 1000])
        assert result == [44, -6000, 6000, 0, 4000, -2000, 2000], f"Test 448 failed: got {result}, expected {[44, -6000, 6000, 0, 4000, -2000, 2000]}"
        print(f"Test 448 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 448 failed: {e}")
        test_results.append(False)

    # Test case 449
    try:
        result = double_array_elements([1000, -1000, 2000, 3000, 0])
        assert result == [2000, -2000, 4000, 6000, 0], f"Test 449 failed: got {result}, expected {[2000, -2000, 4000, 6000, 0]}"
        print(f"Test 449 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 449 failed: {e}")
        test_results.append(False)

    # Test case 450
    try:
        result = double_array_elements([-3000, 3000, -2000, 2000, -1000, 1000, -12, -44])
        assert result == [-6000, 6000, -4000, 4000, -2000, 2000, -24, -88], f"Test 450 failed: got {result}, expected {[-6000, 6000, -4000, 4000, -2000, 2000, -24, -88]}"
        print(f"Test 450 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 450 failed: {e}")
        test_results.append(False)

    # Test case 451
    try:
        result = double_array_elements([1000, 13, 2000, -1999, 3000, -3000])
        assert result == [2000, 26, 4000, -3998, 6000, -6000], f"Test 451 failed: got {result}, expected {[2000, 26, 4000, -3998, 6000, -6000]}"
        print(f"Test 451 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 451 failed: {e}")
        test_results.append(False)

    # Test case 452
    try:
        result = double_array_elements([62, -3000, 3000, -2000, 2001, -1000, 1000, 8192])
        assert result == [124, -6000, 6000, -4000, 4002, -2000, 2000, 16384], f"Test 452 failed: got {result}, expected {[124, -6000, 6000, -4000, 4002, -2000, 2000, 16384]}"
        print(f"Test 452 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 452 failed: {e}")
        test_results.append(False)

    # Test case 453
    try:
        result = double_array_elements([1000, -1000, 2000, -2000, 3000, -3000, 0, 0, 999999999, 0])
        assert result == [2000, -2000, 4000, -4000, 6000, -6000, 0, 0, 1999999998, 0], f"Test 453 failed: got {result}, expected {[2000, -2000, 4000, -4000, 6000, -6000, 0, 0, 1999999998, 0]}"
        print(f"Test 453 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 453 failed: {e}")
        test_results.append(False)

    # Test case 454
    try:
        result = double_array_elements([1000, -1000, 2000, 0, 3000, -3000, 0, 42])
        assert result == [2000, -2000, 4000, 0, 6000, -6000, 0, 84], f"Test 454 failed: got {result}, expected {[2000, -2000, 4000, 0, 6000, -6000, 0, 84]}"
        print(f"Test 454 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 454 failed: {e}")
        test_results.append(False)

    # Test case 455
    try:
        result = double_array_elements([9223372036854775807, 0])
        assert result == [18446744073709551614, 0], f"Test 455 failed: got {result}, expected {[18446744073709551614, 0]}"
        print(f"Test 455 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 455 failed: {e}")
        test_results.append(False)

    # Test case 456
    try:
        result = double_array_elements([9223372036854775807, 0, 0])
        assert result == [18446744073709551614, 0, 0], f"Test 456 failed: got {result}, expected {[18446744073709551614, 0, 0]}"
        print(f"Test 456 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 456 failed: {e}")
        test_results.append(False)

    # Test case 457
    try:
        result = double_array_elements([9223372036854775807, -10])
        assert result == [18446744073709551614, -20], f"Test 457 failed: got {result}, expected {[18446744073709551614, -20]}"
        print(f"Test 457 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 457 failed: {e}")
        test_results.append(False)

    # Test case 458
    try:
        result = double_array_elements([9223372036854775807, -256])
        assert result == [18446744073709551614, -512], f"Test 458 failed: got {result}, expected {[18446744073709551614, -512]}"
        print(f"Test 458 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 458 failed: {e}")
        test_results.append(False)

    # Test case 459
    try:
        result = double_array_elements([14, 9223372036854775807])
        assert result == [28, 18446744073709551614], f"Test 459 failed: got {result}, expected {[28, 18446744073709551614]}"
        print(f"Test 459 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 459 failed: {e}")
        test_results.append(False)

    # Test case 460
    try:
        result = double_array_elements([1, 6, 13])
        assert result == [2, 12, 26], f"Test 460 failed: got {result}, expected {[2, 12, 26]}"
        print(f"Test 460 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 460 failed: {e}")
        test_results.append(False)

    # Test case 461
    try:
        result = double_array_elements([9223372036854775809])
        assert result == [18446744073709551618], f"Test 461 failed: got {result}, expected {[18446744073709551618]}"
        print(f"Test 461 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 461 failed: {e}")
        test_results.append(False)

    # Test case 462
    try:
        result = double_array_elements([2, 9223372036854775807])
        assert result == [4, 18446744073709551614], f"Test 462 failed: got {result}, expected {[4, 18446744073709551614]}"
        print(f"Test 462 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 462 failed: {e}")
        test_results.append(False)

    # Test case 463
    try:
        result = double_array_elements([14, 0, 9223372036854775807])
        assert result == [28, 0, 18446744073709551614], f"Test 463 failed: got {result}, expected {[28, 0, 18446744073709551614]}"
        print(f"Test 463 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 463 failed: {e}")
        test_results.append(False)

    # Test case 464
    try:
        result = double_array_elements([0, -1024, 9223372036854775807])
        assert result == [0, -2048, 18446744073709551614], f"Test 464 failed: got {result}, expected {[0, -2048, 18446744073709551614]}"
        print(f"Test 464 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 464 failed: {e}")
        test_results.append(False)

    # Test case 465
    try:
        result = double_array_elements([11])
        assert result == [22], f"Test 465 failed: got {result}, expected {[22]}"
        print(f"Test 465 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 465 failed: {e}")
        test_results.append(False)

    # Test case 466
    try:
        result = double_array_elements([0, -9223372036854775808, 0])
        assert result == [0, -18446744073709551616, 0], f"Test 466 failed: got {result}, expected {[0, -18446744073709551616, 0]}"
        print(f"Test 466 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 466 failed: {e}")
        test_results.append(False)

    # Test case 467
    try:
        result = double_array_elements([-9223372036854775810, -12])
        assert result == [-18446744073709551620, -24], f"Test 467 failed: got {result}, expected {[-18446744073709551620, -24]}"
        print(f"Test 467 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 467 failed: {e}")
        test_results.append(False)

    # Test case 468
    try:
        result = double_array_elements([4])
        assert result == [8], f"Test 468 failed: got {result}, expected {[8]}"
        print(f"Test 468 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 468 failed: {e}")
        test_results.append(False)

    # Test case 469
    try:
        result = double_array_elements([9223372036854775808, 9223372036854775808, 0, 0])
        assert result == [18446744073709551616, 18446744073709551616, 0, 0], f"Test 469 failed: got {result}, expected {[18446744073709551616, 18446744073709551616, 0, 0]}"
        print(f"Test 469 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 469 failed: {e}")
        test_results.append(False)

    # Test case 470
    try:
        result = double_array_elements([0, -9223372036854775808])
        assert result == [0, -18446744073709551616], f"Test 470 failed: got {result}, expected {[0, -18446744073709551616]}"
        print(f"Test 470 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 470 failed: {e}")
        test_results.append(False)

    # Test case 471
    try:
        result = double_array_elements([0, 9223372036854775808])
        assert result == [0, 18446744073709551616], f"Test 471 failed: got {result}, expected {[0, 18446744073709551616]}"
        print(f"Test 471 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 471 failed: {e}")
        test_results.append(False)

    # Test case 472
    try:
        result = double_array_elements([9223372036854775808])
        assert result == [18446744073709551616], f"Test 472 failed: got {result}, expected {[18446744073709551616]}"
        print(f"Test 472 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 472 failed: {e}")
        test_results.append(False)

    # Test case 473
    try:
        result = double_array_elements([-9223372036854775808, 0])
        assert result == [-18446744073709551616, 0], f"Test 473 failed: got {result}, expected {[-18446744073709551616, 0]}"
        print(f"Test 473 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 473 failed: {e}")
        test_results.append(False)

    # Test case 474
    try:
        result = double_array_elements([0, -18446744073709551616])
        assert result == [0, -36893488147419103232], f"Test 474 failed: got {result}, expected {[0, -36893488147419103232]}"
        print(f"Test 474 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 474 failed: {e}")
        test_results.append(False)

    # Test case 475
    try:
        result = double_array_elements([124, -9223372036854775808, 0, 6])
        assert result == [248, -18446744073709551616, 0, 12], f"Test 475 failed: got {result}, expected {[248, -18446744073709551616, 0, 12]}"
        print(f"Test 475 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 475 failed: {e}")
        test_results.append(False)

    # Test case 476
    try:
        result = double_array_elements([-9223372036854775808, 0, 0])
        assert result == [-18446744073709551616, 0, 0], f"Test 476 failed: got {result}, expected {[-18446744073709551616, 0, 0]}"
        print(f"Test 476 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 476 failed: {e}")
        test_results.append(False)

    # Test case 477
    try:
        result = double_array_elements([9223372036854775807, -9223372036854775808, 0, 2001, 0])
        assert result == [18446744073709551614, -18446744073709551616, 0, 4002, 0], f"Test 477 failed: got {result}, expected {[18446744073709551614, -18446744073709551616, 0, 4002, 0]}"
        print(f"Test 477 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 477 failed: {e}")
        test_results.append(False)

    # Test case 478
    try:
        result = double_array_elements([9, 0, -9223372036854775808, 9223372036854775807])
        assert result == [18, 0, -18446744073709551616, 18446744073709551614], f"Test 478 failed: got {result}, expected {[18, 0, -18446744073709551616, 18446744073709551614]}"
        print(f"Test 478 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 478 failed: {e}")
        test_results.append(False)

    # Test case 479
    try:
        result = double_array_elements([9223372036854775807, -9223372036854775808, 0, -1999, 0])
        assert result == [18446744073709551614, -18446744073709551616, 0, -3998, 0], f"Test 479 failed: got {result}, expected {[18446744073709551614, -18446744073709551616, 0, -3998, 0]}"
        print(f"Test 479 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 479 failed: {e}")
        test_results.append(False)

    # Test case 480
    try:
        result = double_array_elements([9223372036854775807, -9223372036854775808, 0, 12])
        assert result == [18446744073709551614, -18446744073709551616, 0, 24], f"Test 480 failed: got {result}, expected {[18446744073709551614, -18446744073709551616, 0, 24]}"
        print(f"Test 480 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 480 failed: {e}")
        test_results.append(False)

    # Test case 481
    try:
        result = double_array_elements([0, 0, -9223372036854775808, 9223372036854775807, 512, -9223372036854775808])
        assert result == [0, 0, -18446744073709551616, 18446744073709551614, 1024, -18446744073709551616], f"Test 481 failed: got {result}, expected {[0, 0, -18446744073709551616, 18446744073709551614, 1024, -18446744073709551616]}"
        print(f"Test 481 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 481 failed: {e}")
        test_results.append(False)

    # Test case 482
    try:
        result = double_array_elements([-9223372036854775808, 0, 0, -8192, 0])
        assert result == [-18446744073709551616, 0, 0, -16384, 0], f"Test 482 failed: got {result}, expected {[-18446744073709551616, 0, 0, -16384, 0]}"
        print(f"Test 482 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 482 failed: {e}")
        test_results.append(False)

    # Test case 483
    try:
        result = double_array_elements([0, 512, 0, -18446744073709551616, 9223372036854775807])
        assert result == [0, 1024, 0, -36893488147419103232, 18446744073709551614], f"Test 483 failed: got {result}, expected {[0, 1024, 0, -36893488147419103232, 18446744073709551614]}"
        print(f"Test 483 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 483 failed: {e}")
        test_results.append(False)

    # Test case 484
    try:
        result = double_array_elements([9223372036854775807, -18446744073709551616, 2, -123456788, 19])
        assert result == [18446744073709551614, -36893488147419103232, 4, -246913576, 38], f"Test 484 failed: got {result}, expected {[18446744073709551614, -36893488147419103232, 4, -246913576, 38]}"
        print(f"Test 484 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 484 failed: {e}")
        test_results.append(False)

    # Test case 485
    try:
        result = double_array_elements([0, 11, 0, -9223372036854775808, 9223372036854775807])
        assert result == [0, 22, 0, -18446744073709551616, 18446744073709551614], f"Test 485 failed: got {result}, expected {[0, 22, 0, -18446744073709551616, 18446744073709551614]}"
        print(f"Test 485 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 485 failed: {e}")
        test_results.append(False)

    # Test case 486
    try:
        result = double_array_elements([0, -9223372036854775808, 9223372036854775807, 0])
        assert result == [0, -18446744073709551616, 18446744073709551614, 0], f"Test 486 failed: got {result}, expected {[0, -18446744073709551616, 18446744073709551614, 0]}"
        print(f"Test 486 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 486 failed: {e}")
        test_results.append(False)

    # Test case 487
    try:
        result = double_array_elements([9223372036854775807, -9223372036854775808, 0, 0, -64, 0])
        assert result == [18446744073709551614, -18446744073709551616, 0, 0, -128, 0], f"Test 487 failed: got {result}, expected {[18446744073709551614, -18446744073709551616, 0, 0, -128, 0]}"
        print(f"Test 487 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 487 failed: {e}")
        test_results.append(False)

    # Test case 488
    try:
        result = double_array_elements([-4611686018427387904, 4611686018427387904, 0, -2000])
        assert result == [-9223372036854775808, 9223372036854775808, 0, -4000], f"Test 488 failed: got {result}, expected {[-9223372036854775808, 9223372036854775808, 0, -4000]}"
        print(f"Test 488 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 488 failed: {e}")
        test_results.append(False)

    # Test case 489
    try:
        result = double_array_elements([4611686018427387904, 0])
        assert result == [9223372036854775808, 0], f"Test 489 failed: got {result}, expected {[9223372036854775808, 0]}"
        print(f"Test 489 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 489 failed: {e}")
        test_results.append(False)

    # Test case 490
    try:
        result = double_array_elements([2001, -4611686018427387904, -170141183460469231731687303715884105728, 0, 0])
        assert result == [4002, -9223372036854775808, -340282366920938463463374607431768211456, 0, 0], f"Test 490 failed: got {result}, expected {[4002, -9223372036854775808, -340282366920938463463374607431768211456, 0, 0]}"
        print(f"Test 490 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 490 failed: {e}")
        test_results.append(False)

    # Test case 491
    try:
        result = double_array_elements([4611686018427387904, -170141183460469231731687303715884105728, -123456788])
        assert result == [9223372036854775808, -340282366920938463463374607431768211456, -246913576], f"Test 491 failed: got {result}, expected {[9223372036854775808, -340282366920938463463374607431768211456, -246913576]}"
        print(f"Test 491 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 491 failed: {e}")
        test_results.append(False)

    # Test case 492
    try:
        result = double_array_elements([-4611686018427387904, -20, 4])
        assert result == [-9223372036854775808, -40, 8], f"Test 492 failed: got {result}, expected {[-9223372036854775808, -40, 8]}"
        print(f"Test 492 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 492 failed: {e}")
        test_results.append(False)

    # Test case 493
    try:
        result = double_array_elements([-4611686018427387904, 4611686018427387904, 0])
        assert result == [-9223372036854775808, 9223372036854775808, 0], f"Test 493 failed: got {result}, expected {[-9223372036854775808, 9223372036854775808, 0]}"
        print(f"Test 493 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 493 failed: {e}")
        test_results.append(False)

    # Test case 494
    try:
        result = double_array_elements([0, 4611686018427387904, -4611686018427387904])
        assert result == [0, 9223372036854775808, -9223372036854775808], f"Test 494 failed: got {result}, expected {[0, 9223372036854775808, -9223372036854775808]}"
        print(f"Test 494 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 494 failed: {e}")
        test_results.append(False)

    # Test case 495
    try:
        result = double_array_elements([4611686018427387904, -4611686018427387904, 0])
        assert result == [9223372036854775808, -9223372036854775808, 0], f"Test 495 failed: got {result}, expected {[9223372036854775808, -9223372036854775808, 0]}"
        print(f"Test 495 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 495 failed: {e}")
        test_results.append(False)

    # Test case 496
    try:
        result = double_array_elements([4611686018427387904])
        assert result == [9223372036854775808], f"Test 496 failed: got {result}, expected {[9223372036854775808]}"
        print(f"Test 496 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 496 failed: {e}")
        test_results.append(False)

    # Test case 497
    try:
        result = double_array_elements([4611686018427387904, 0, 0])
        assert result == [9223372036854775808, 0, 0], f"Test 497 failed: got {result}, expected {[9223372036854775808, 0, 0]}"
        print(f"Test 497 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 497 failed: {e}")
        test_results.append(False)

    # Test case 498
    try:
        result = double_array_elements([4096])
        assert result == [8192], f"Test 498 failed: got {result}, expected {[8192]}"
        print(f"Test 498 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 498 failed: {e}")
        test_results.append(False)

    # Test case 499
    try:
        result = double_array_elements([4611686018427387903, -4611686018427387903])
        assert result == [9223372036854775806, -9223372036854775806], f"Test 499 failed: got {result}, expected {[9223372036854775806, -9223372036854775806]}"
        print(f"Test 499 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 499 failed: {e}")
        test_results.append(False)

    # Test case 500
    try:
        result = double_array_elements([-41, 496, 170141183460469231731687303715884105728])
        assert result == [-82, 992, 340282366920938463463374607431768211456], f"Test 500 failed: got {result}, expected {[-82, 992, 340282366920938463463374607431768211456]}"
        print(f"Test 500 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 500 failed: {e}")
        test_results.append(False)

    # Test case 501
    try:
        result = double_array_elements([170141183460469231731687303715884105727, 30, 0])
        assert result == [340282366920938463463374607431768211454, 60, 0], f"Test 501 failed: got {result}, expected {[340282366920938463463374607431768211454, 60, 0]}"
        print(f"Test 501 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 501 failed: {e}")
        test_results.append(False)

    # Test case 502
    try:
        result = double_array_elements([0, 0, 100])
        assert result == [0, 0, 200], f"Test 502 failed: got {result}, expected {[0, 0, 200]}"
        print(f"Test 502 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 502 failed: {e}")
        test_results.append(False)

    # Test case 503
    try:
        result = double_array_elements([170141183460469231731687303715884105727, -8192])
        assert result == [340282366920938463463374607431768211454, -16384], f"Test 503 failed: got {result}, expected {[340282366920938463463374607431768211454, -16384]}"
        print(f"Test 503 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 503 failed: {e}")
        test_results.append(False)

    # Test case 504
    try:
        result = double_array_elements([-8, 0])
        assert result == [-16, 0], f"Test 504 failed: got {result}, expected {[-16, 0]}"
        print(f"Test 504 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 504 failed: {e}")
        test_results.append(False)

    # Test case 505
    try:
        result = double_array_elements([340282366920938463463374607431768211454, 0])
        assert result == [680564733841876926926749214863536422908, 0], f"Test 505 failed: got {result}, expected {[680564733841876926926749214863536422908, 0]}"
        print(f"Test 505 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 505 failed: {e}")
        test_results.append(False)

    # Test case 506
    try:
        result = double_array_elements([0, 14, 0])
        assert result == [0, 28, 0], f"Test 506 failed: got {result}, expected {[0, 28, 0]}"
        print(f"Test 506 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 506 failed: {e}")
        test_results.append(False)

    # Test case 507
    try:
        result = double_array_elements([-4611686018427387904, 0, 170141183460469231731687303715884105727, 0])
        assert result == [-9223372036854775808, 0, 340282366920938463463374607431768211454, 0], f"Test 507 failed: got {result}, expected {[-9223372036854775808, 0, 340282366920938463463374607431768211454, 0]}"
        print(f"Test 507 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 507 failed: {e}")
        test_results.append(False)

    # Test case 508
    try:
        result = double_array_elements([170141183460469231731687303715884105727, -1])
        assert result == [340282366920938463463374607431768211454, -2], f"Test 508 failed: got {result}, expected {[340282366920938463463374607431768211454, -2]}"
        print(f"Test 508 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 508 failed: {e}")
        test_results.append(False)

    # Test case 509
    try:
        result = double_array_elements([170141183460469231731687303715884105727, 1, -8192])
        assert result == [340282366920938463463374607431768211454, 2, -16384], f"Test 509 failed: got {result}, expected {[340282366920938463463374607431768211454, 2, -16384]}"
        print(f"Test 509 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 509 failed: {e}")
        test_results.append(False)

    # Test case 510
    try:
        result = double_array_elements([170141183460469231731687303715884105726])
        assert result == [340282366920938463463374607431768211452], f"Test 510 failed: got {result}, expected {[340282366920938463463374607431768211452]}"
        print(f"Test 510 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 510 failed: {e}")
        test_results.append(False)

    # Test case 511
    try:
        result = double_array_elements([170141183460469231731687303715884105727, -8])
        assert result == [340282366920938463463374607431768211454, -16], f"Test 511 failed: got {result}, expected {[340282366920938463463374607431768211454, -16]}"
        print(f"Test 511 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 511 failed: {e}")
        test_results.append(False)

    # Test case 512
    try:
        result = double_array_elements([-999999999, 7])
        assert result == [-1999999998, 14], f"Test 512 failed: got {result}, expected {[-1999999998, 14]}"
        print(f"Test 512 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 512 failed: {e}")
        test_results.append(False)

    # Test case 513
    try:
        result = double_array_elements([170141183460469231731687303715884105727, 123456789])
        assert result == [340282366920938463463374607431768211454, 246913578], f"Test 513 failed: got {result}, expected {[340282366920938463463374607431768211454, 246913578]}"
        print(f"Test 513 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 513 failed: {e}")
        test_results.append(False)

    # Test case 514
    try:
        result = double_array_elements([170141183460469231731687303715884105727, 0, 23])
        assert result == [340282366920938463463374607431768211454, 0, 46], f"Test 514 failed: got {result}, expected {[340282366920938463463374607431768211454, 0, 46]}"
        print(f"Test 514 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 514 failed: {e}")
        test_results.append(False)

    # Test case 515
    try:
        result = double_array_elements([8128, 0])
        assert result == [16256, 0], f"Test 515 failed: got {result}, expected {[16256, 0]}"
        print(f"Test 515 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 515 failed: {e}")
        test_results.append(False)

    # Test case 516
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, 9])
        assert result == [-340282366920938463463374607431768211456, 18], f"Test 516 failed: got {result}, expected {[-340282366920938463463374607431768211456, 18]}"
        print(f"Test 516 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 516 failed: {e}")
        test_results.append(False)

    # Test case 517
    try:
        result = double_array_elements([999999999999999999999999999999999999999999])
        assert result == [1999999999999999999999999999999999999999998], f"Test 517 failed: got {result}, expected {[1999999999999999999999999999999999999999998]}"
        print(f"Test 517 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 517 failed: {e}")
        test_results.append(False)

    # Test case 518
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, 0, 255, 0])
        assert result == [-340282366920938463463374607431768211456, 0, 510, 0], f"Test 518 failed: got {result}, expected {[-340282366920938463463374607431768211456, 0, 510, 0]}"
        print(f"Test 518 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 518 failed: {e}")
        test_results.append(False)

    # Test case 519
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, -256, 4611686018427387904, 0])
        assert result == [-340282366920938463463374607431768211456, -512, 9223372036854775808, 0], f"Test 519 failed: got {result}, expected {[-340282366920938463463374607431768211456, -512, 9223372036854775808, 0]}"
        print(f"Test 519 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 519 failed: {e}")
        test_results.append(False)

    # Test case 520
    try:
        result = double_array_elements([-2147483649])
        assert result == [-4294967298], f"Test 520 failed: got {result}, expected {[-4294967298]}"
        print(f"Test 520 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 520 failed: {e}")
        test_results.append(False)

    # Test case 521
    try:
        result = double_array_elements([0, 123456790])
        assert result == [0, 246913580], f"Test 521 failed: got {result}, expected {[0, 246913580]}"
        print(f"Test 521 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 521 failed: {e}")
        test_results.append(False)

    # Test case 522
    try:
        result = double_array_elements([-340282366920938463463374607431768211456, 0, 0])
        assert result == [-680564733841876926926749214863536422912, 0, 0], f"Test 522 failed: got {result}, expected {[-680564733841876926926749214863536422912, 0, 0]}"
        print(f"Test 522 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 522 failed: {e}")
        test_results.append(False)

    # Test case 523
    try:
        result = double_array_elements([0, -170141183460469231731687303715884105728])
        assert result == [0, -340282366920938463463374607431768211456], f"Test 523 failed: got {result}, expected {[0, -340282366920938463463374607431768211456]}"
        print(f"Test 523 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 523 failed: {e}")
        test_results.append(False)

    # Test case 524
    try:
        result = double_array_elements([4096, -9223372036854775810, 0, 0])
        assert result == [8192, -18446744073709551620, 0, 0], f"Test 524 failed: got {result}, expected {[8192, -18446744073709551620, 0, 0]}"
        print(f"Test 524 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 524 failed: {e}")
        test_results.append(False)

    # Test case 525
    try:
        result = double_array_elements([-15, 0])
        assert result == [-30, 0], f"Test 525 failed: got {result}, expected {[-30, 0]}"
        print(f"Test 525 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 525 failed: {e}")
        test_results.append(False)

    # Test case 526
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, 123456789])
        assert result == [-340282366920938463463374607431768211456, 246913578], f"Test 526 failed: got {result}, expected {[-340282366920938463463374607431768211456, 246913578]}"
        print(f"Test 526 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 526 failed: {e}")
        test_results.append(False)

    # Test case 527
    try:
        result = double_array_elements([-170141183460469231731687303715884105727, 0])
        assert result == [-340282366920938463463374607431768211454, 0], f"Test 527 failed: got {result}, expected {[-340282366920938463463374607431768211454, 0]}"
        print(f"Test 527 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 527 failed: {e}")
        test_results.append(False)

    # Test case 528
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, -21])
        assert result == [-340282366920938463463374607431768211456, -42], f"Test 528 failed: got {result}, expected {[-340282366920938463463374607431768211456, -42]}"
        print(f"Test 528 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 528 failed: {e}")
        test_results.append(False)

    # Test case 529
    try:
        result = double_array_elements([-170141183460469231731687303715884105728, 0, 0])
        assert result == [-340282366920938463463374607431768211456, 0, 0], f"Test 529 failed: got {result}, expected {[-340282366920938463463374607431768211456, 0, 0]}"
        print(f"Test 529 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 529 failed: {e}")
        test_results.append(False)

    # Test case 530
    try:
        result = double_array_elements([999999999999999999999999999999999999999999, -999999999999999999999999999999999999999999, -50])
        assert result == [1999999999999999999999999999999999999999998, -1999999999999999999999999999999999999999998, -100], f"Test 530 failed: got {result}, expected {[1999999999999999999999999999999999999999998, -1999999999999999999999999999999999999999998, -100]}"
        print(f"Test 530 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 530 failed: {e}")
        test_results.append(False)

    # Test case 531
    try:
        result = double_array_elements([999999999999999999999999999999999999999999, -999999999999999999999999999999999999999999, 0])
        assert result == [1999999999999999999999999999999999999999998, -1999999999999999999999999999999999999999998, 0], f"Test 531 failed: got {result}, expected {[1999999999999999999999999999999999999999998, -1999999999999999999999999999999999999999998, 0]}"
        print(f"Test 531 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 531 failed: {e}")
        test_results.append(False)

    # Test case 532
    try:
        result = double_array_elements([-999999999999999999999999999999999999999999, 0])
        assert result == [-1999999999999999999999999999999999999999998, 0], f"Test 532 failed: got {result}, expected {[-1999999999999999999999999999999999999999998, 0]}"
        print(f"Test 532 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 532 failed: {e}")
        test_results.append(False)

    # Test case 533
    try:
        result = double_array_elements([-999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999, 0, -16, -2147483650])
        assert result == [-1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999998, 0, -32, -4294967300], f"Test 533 failed: got {result}, expected {[-1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999998, 0, -32, -4294967300]}"
        print(f"Test 533 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 533 failed: {e}")
        test_results.append(False)

    # Test case 534
    try:
        result = double_array_elements([999999999999999999999999999999999999999999, 0, 8192, 2])
        assert result == [1999999999999999999999999999999999999999998, 0, 16384, 4], f"Test 534 failed: got {result}, expected {[1999999999999999999999999999999999999999998, 0, 16384, 4]}"
        print(f"Test 534 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 534 failed: {e}")
        test_results.append(False)

    # Test case 535
    try:
        result = double_array_elements([0, 0, -999999999999999999999999999999999999999999, 0])
        assert result == [0, 0, -1999999999999999999999999999999999999999998, 0], f"Test 535 failed: got {result}, expected {[0, 0, -1999999999999999999999999999999999999999998, 0]}"
        print(f"Test 535 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 535 failed: {e}")
        test_results.append(False)

    # Test case 536
    try:
        result = double_array_elements([0, -999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999, 12, 0, 0])
        assert result == [0, -1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999998, 24, 0, 0], f"Test 536 failed: got {result}, expected {[0, -1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999998, 24, 0, 0]}"
        print(f"Test 536 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 536 failed: {e}")
        test_results.append(False)

    # Test case 537
    try:
        result = double_array_elements([-1, -999999999999999999999999999999999999999999, 999999999999999999999999999999999999999998])
        assert result == [-2, -1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999996], f"Test 537 failed: got {result}, expected {[-2, -1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999996]}"
        print(f"Test 537 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 537 failed: {e}")
        test_results.append(False)

    # Test case 538
    try:
        result = double_array_elements([999999999999999999999999999999999999999999, -999999999999999999999999999999999999999999, 0, 0, -15])
        assert result == [1999999999999999999999999999999999999999998, -1999999999999999999999999999999999999999998, 0, 0, -30], f"Test 538 failed: got {result}, expected {[1999999999999999999999999999999999999999998, -1999999999999999999999999999999999999999998, 0, 0, -30]}"
        print(f"Test 538 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 538 failed: {e}")
        test_results.append(False)

    # Test case 539
    try:
        result = double_array_elements([-999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999])
        assert result == [-1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999998], f"Test 539 failed: got {result}, expected {[-1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999998]}"
        print(f"Test 539 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 539 failed: {e}")
        test_results.append(False)

    # Test case 540
    try:
        result = double_array_elements([0, 1000000000000000000000000000000000000000001])
        assert result == [0, 2000000000000000000000000000000000000000002], f"Test 540 failed: got {result}, expected {[0, 2000000000000000000000000000000000000000002]}"
        print(f"Test 540 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 540 failed: {e}")
        test_results.append(False)

    # Test case 541
    try:
        result = double_array_elements([1, -1, 2, -2, 4, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, -128, 256, -256, 512, -512, 1024, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384, 0])
        assert result == '-4096, 8192, -8192, 16384, -16384, 32768, -32768, 0]', f"Test 541 failed: got {result}, expected {'-4096, 8192, -8192, 16384, -16384, 32768, -32768, 0]'}"
        print(f"Test 541 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 541 failed: {e}")
        test_results.append(False)

    # Test case 542
    try:
        result = double_array_elements([-16384, 16384, -8192, 8192, -4096, 4096, -2048, 2048, -1024, 1024, -512, 512, -256, 256, -128, 128, -64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2, -1, 1])
        assert result == '-64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2]', f"Test 542 failed: got {result}, expected {'-64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2]'}"
        print(f"Test 542 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 542 failed: {e}")
        test_results.append(False)

    # Test case 543
    try:
        result = double_array_elements([1, -1, 2, -2, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, -128, 256, -256, 512, -512, 1024, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384])
        assert result == '8192, -8192, 16384, -16384, 32768, -32768]', f"Test 543 failed: got {result}, expected {'8192, -8192, 16384, -16384, 32768, -32768]'}"
        print(f"Test 543 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 543 failed: {e}")
        test_results.append(False)

    # Test case 544
    try:
        result = double_array_elements([-123456790, 1, -1, 2, -2, 4, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, -128, 256, -256, 512, -512, 1024, -1024, 2048, -1999, 4096, -4096, 8192, 16384, -16384])
        assert result == '4096, -3998, 8192, -8192, 16384, 32768, -32768]', f"Test 544 failed: got {result}, expected {'4096, -3998, 8192, -8192, 16384, 32768, -32768]'}"
        print(f"Test 544 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 544 failed: {e}")
        test_results.append(False)

    # Test case 545
    try:
        result = double_array_elements([1, -1, -2, 4, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, -128, 256, -256, 512, -512, 1024, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384, 0])
        assert result == '8192, -8192, 16384, -16384, 32768, -32768, 0]', f"Test 545 failed: got {result}, expected {'8192, -8192, 16384, -16384, 32768, -32768, 0]'}"
        print(f"Test 545 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 545 failed: {e}")
        test_results.append(False)

    # Test case 546
    try:
        result = double_array_elements([-16384, 16384, -8192, 8192, -4096, 4096, -2048, 2048, -1024, 1024, -512, 512, -256, 256, -128, 128, -64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2, -1, 1, -9223372036854775810])
        assert result == '-64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2, -18446744073709551620]', f"Test 546 failed: got {result}, expected {'-64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2, -18446744073709551620]'}"
        print(f"Test 546 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 546 failed: {e}")
        test_results.append(False)

    # Test case 547
    try:
        result = double_array_elements([1, -1, 2, -2, 4, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, -128, 256, -256, 512, -512, 22, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384, 0])
        assert result == '8192, -8192, 16384, -16384, 32768, -32768, 0]', f"Test 547 failed: got {result}, expected {'8192, -8192, 16384, -16384, 32768, -32768, 0]'}"
        print(f"Test 547 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 547 failed: {e}")
        test_results.append(False)

    # Test case 548
    try:
        result = double_array_elements([1, -1, 2, -2, 4, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, 256, -256, 512, -512, 1024, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384, 999999999])
        assert result == '8192, -8192, 16384, -16384, 32768, -32768, 1999999998]', f"Test 548 failed: got {result}, expected {'8192, -8192, 16384, -16384, 32768, -32768, 1999999998]'}"
        print(f"Test 548 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 548 failed: {e}")
        test_results.append(False)

    # Test case 549
    try:
        result = double_array_elements([16384, -8192, 8192, -4096, 4096, -2048, 2048, -1024, 1024, -512, 512, -256, 256, -128, 128, -64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2, -1, 1, 0])
        assert result == '-32, 32, -16, 16, -8, 8, -4, 4, -2, 2, 0]', f"Test 549 failed: got {result}, expected {'-32, 32, -16, 16, -8, 8, -4, 4, -2, 2, 0]'}"
        print(f"Test 549 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 549 failed: {e}")
        test_results.append(False)

    # Test case 550
    try:
        result = double_array_elements([1, -1, 2, -2, 4, -4, 8, -8, 0, 32, -32, 64, -64, 128, -128, 256, -256, 512, -512, 1024, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384, 63, 999999999999999999999999999999999999999998])
        assert result == '8192, -8192, 16384, -16384, 32768, -32768, 126, 1999999999999999999999999999999999999999996]', f"Test 550 failed: got {result}, expected {'8192, -8192, 16384, -16384, 32768, -32768, 126, 1999999999999999999999999999999999999999996]'}"
        print(f"Test 550 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 550 failed: {e}")
        test_results.append(False)

    # Test case 551
    try:
        result = double_array_elements([0, -16384, 16384, -8192, -41, -4096, 4096, -2048, 2048, -1024, 1024, -512, 512, -256, 256, -128, 128, -64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2, -1, 1, -256, 8])
        assert result == '-64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2, -512, 16]', f"Test 551 failed: got {result}, expected {'-64, 64, -32, 32, -16, 16, -8, 8, -4, 4, -2, 2, -512, 16]'}"
        print(f"Test 551 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 551 failed: {e}")
        test_results.append(False)

    # Test case 552
    try:
        result = double_array_elements([1, -1, 2, -2, 4, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, -128, 256, -256, 512, 512, 1024, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384])
        assert result == '8192, -8192, 16384, -16384, 32768, -32768]', f"Test 552 failed: got {result}, expected {'8192, -8192, 16384, -16384, 32768, -32768]'}"
        print(f"Test 552 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 552 failed: {e}")
        test_results.append(False)

    # Test case 553
    try:
        result = double_array_elements([1, -1, -2, -2, 4, -4, 8, -8, -16, 32, -32, 64, -64, 128, -128, 256, -256, 512, -512, 2048, -1024, -50, -2048, 4096, -4096, 8192, -8192, 16384, -16384, 0])
        assert result == '8192, -8192, 16384, -16384, 32768, -32768, 0]', f"Test 553 failed: got {result}, expected {'8192, -8192, 16384, -16384, 32768, -32768, 0]'}"
        print(f"Test 553 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 553 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
