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
        result = double_array_elements([-1, -2, -3, -4, -5, -6])
        assert result == [-2, -4, -6, -8, -10, -12], f"Test 6 failed: got {result}, expected {[-2, -4, -6, -8, -10, -12]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = double_array_elements([11, 13, 17, 19, 23])
        assert result == [22, 26, 34, 38, 46], f"Test 7 failed: got {result}, expected {[22, 26, 34, 38, 46]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = double_array_elements([123456789])
        assert result == [246913578], f"Test 8 failed: got {result}, expected {[246913578]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = double_array_elements([-123456789])
        assert result == [-246913578], f"Test 9 failed: got {result}, expected {[-246913578]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = double_array_elements([999999999, -999999999, 0])
        assert result == [1999999998, -1999999998, 0], f"Test 10 failed: got {result}, expected {[1999999998, -1999999998, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = double_array_elements([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == [6, 2, 8, 2, 10, 18, 4, 12], f"Test 11 failed: got {result}, expected {[6, 2, 8, 2, 10, 18, 4, 12]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = double_array_elements([50, 40, 30, 20, 10])
        assert result == [100, 80, 60, 40, 20], f"Test 12 failed: got {result}, expected {[100, 80, 60, 40, 20]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = double_array_elements([9223372036854775807, -9223372036854775808, 0])
        assert result == [18446744073709551614, -18446744073709551616, 0], f"Test 13 failed: got {result}, expected {[18446744073709551614, -18446744073709551616, 0]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = double_array_elements([-170141183460469231731687303715884105728])
        assert result == [-340282366920938463463374607431768211456], f"Test 14 failed: got {result}, expected {[-340282366920938463463374607431768211456]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = double_array_elements([5, 0, -16])
        assert result == [10, 0, -32], f"Test 15 failed: got {result}, expected {[10, 0, -32]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = double_array_elements([1, 2, -3, 4])
        assert result == [2, 4, -6, 8], f"Test 16 failed: got {result}, expected {[2, 4, -6, 8]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = double_array_elements([-1, 5, 0, 5])
        assert result == [-2, 10, 0, 10], f"Test 17 failed: got {result}, expected {[-2, 10, 0, 10]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = double_array_elements([0, 100])
        assert result == [0, 200], f"Test 18 failed: got {result}, expected {[0, 200]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = double_array_elements([-100, 0])
        assert result == [-200, 0], f"Test 19 failed: got {result}, expected {[-200, 0]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = double_array_elements([-2, 0, 19])
        assert result == [-4, 0, 38], f"Test 20 failed: got {result}, expected {[-4, 0, 38]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = double_array_elements([-1, 0, 0])
        assert result == [-2, 0, 0], f"Test 21 failed: got {result}, expected {[-2, 0, 0]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = double_array_elements([9223372036854775808, 62])
        assert result == [18446744073709551616, 124], f"Test 22 failed: got {result}, expected {[18446744073709551616, 124]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = double_array_elements([1, 123456789, -999999999, -999999999999999999999999999999999999999999])
        assert result == [2, 246913578, -1999999998, -1999999999999999999999999999999999999999998], f"Test 23 failed: got {result}, expected {[2, 246913578, -1999999998, -1999999999999999999999999999999999999999998]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = double_array_elements([2, 0, 0, 0, 2147483647])
        assert result == [4, 0, 0, 0, 4294967294], f"Test 24 failed: got {result}, expected {[4, 0, 0, 0, 4294967294]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = double_array_elements([0, 1, 2, 3, 4, 5, 0, 0])
        assert result == [0, 2, 4, 6, 8, 10, 0, 0], f"Test 25 failed: got {result}, expected {[0, 2, 4, 6, 8, 10, 0, 0]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = double_array_elements([0, 0, 0, 20, 0])
        assert result == [0, 0, 0, 40, 0], f"Test 26 failed: got {result}, expected {[0, 0, 0, 40, 0]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = double_array_elements([-10, 10, 20])
        assert result == [-20, 20, 40], f"Test 27 failed: got {result}, expected {[-20, 20, 40]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = double_array_elements([42, 0, -42, -60])
        assert result == [84, 0, -84, -120], f"Test 28 failed: got {result}, expected {[84, 0, -84, -120]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = double_array_elements([11, 13, 17, 0, 23])
        assert result == [22, 26, 34, 0, 46], f"Test 29 failed: got {result}, expected {[22, 26, 34, 0, 46]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = double_array_elements([16384, 1, -1, -1, 1, -1, 2, -1])
        assert result == [32768, 2, -2, -2, 2, -2, 4, -2], f"Test 30 failed: got {result}, expected {[32768, 2, -2, -2, 2, -2, 4, -2]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = double_array_elements([-123456789, -170141183460469231731687303715884105728])
        assert result == [-246913578, -340282366920938463463374607431768211456], f"Test 31 failed: got {result}, expected {[-246913578, -340282366920938463463374607431768211456]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = double_array_elements([-123456789, -99])
        assert result == [-246913578, -198], f"Test 32 failed: got {result}, expected {[-246913578, -198]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = double_array_elements([-123456789, -7])
        assert result == [-246913578, -14], f"Test 33 failed: got {result}, expected {[-246913578, -14]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = double_array_elements([-512, 512])
        assert result == [-1024, 1024], f"Test 34 failed: got {result}, expected {[-1024, 1024]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = double_array_elements([20, 0, 999999999, -1024])
        assert result == [40, 0, 1999999998, -2048], f"Test 35 failed: got {result}, expected {[40, 0, 1999999998, -2048]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = double_array_elements([-4, -6, -2, -10, -12])
        assert result == [-8, -12, -4, -20, -24], f"Test 36 failed: got {result}, expected {[-8, -12, -4, -20, -24]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = double_array_elements([-2, -4, -6, -8, -10, -12, 0, 0, 13, 0])
        assert result == [-4, -8, -12, -16, -20, -24, 0, 0, 26, 0], f"Test 37 failed: got {result}, expected {[-4, -8, -12, -16, -20, -24, 0, 0, 26, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = double_array_elements([0, -12, -10, -4, -2, 124])
        assert result == [0, -24, -20, -8, -4, 248], f"Test 38 failed: got {result}, expected {[0, -24, -20, -8, -4, 248]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = double_array_elements([-2, -6, -8, -12, -7])
        assert result == [-4, -12, -16, -24, -14], f"Test 39 failed: got {result}, expected {[-4, -12, -16, -24, -14]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = double_array_elements([-2, -4, -6, -9, -3, -12, 0, 0])
        assert result == [-4, -8, -12, -18, -6, -24, 0, 0], f"Test 40 failed: got {result}, expected {[-4, -8, -12, -18, -6, -24, 0, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = double_array_elements([28, 496, 8130, 0, 64])
        assert result == [56, 992, 16260, 0, 128], f"Test 41 failed: got {result}, expected {[56, 992, 16260, 0, 128]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = double_array_elements([-123456788, 0, 8128, 496, 28, 6, 0])
        assert result == [-246913576, 0, 16256, 992, 56, 12, 0], f"Test 42 failed: got {result}, expected {[-246913576, 0, 16256, 992, 56, 12, 0]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = double_array_elements([28, 23, 8128])
        assert result == [56, 46, 16256], f"Test 43 failed: got {result}, expected {[56, 46, 16256]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = double_array_elements([8128, 496, 28])
        assert result == [16256, 992, 56], f"Test 44 failed: got {result}, expected {[16256, 992, 56]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = double_array_elements([0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0])
        assert result == [0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0], f"Test 45 failed: got {result}, expected {[0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = double_array_elements([1000, -1000, 2000, 3000, 0])
        assert result == [2000, -2000, 4000, 6000, 0], f"Test 46 failed: got {result}, expected {[2000, -2000, 4000, 6000, 0]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = double_array_elements([-3000, 3000, -2000, 2000, -1000, 1000, -12, -44])
        assert result == [-6000, 6000, -4000, 4000, -2000, 2000, -24, -88], f"Test 47 failed: got {result}, expected {[-6000, 6000, -4000, 4000, -2000, 2000, -24, -88]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = double_array_elements([0, 4611686018427387904, -4611686018427387904])
        assert result == [0, 9223372036854775808, -9223372036854775808], f"Test 48 failed: got {result}, expected {[0, 9223372036854775808, -9223372036854775808]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = double_array_elements([170141183460469231731687303715884105727, -8])
        assert result == [340282366920938463463374607431768211454, -16], f"Test 49 failed: got {result}, expected {[340282366920938463463374607431768211454, -16]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = double_array_elements([-2147483649])
        assert result == [-4294967298], f"Test 50 failed: got {result}, expected {[-4294967298]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = double_array_elements([-999999999999999999999999999999999999999999, 0])
        assert result == [-1999999999999999999999999999999999999999998, 0], f"Test 51 failed: got {result}, expected {[-1999999999999999999999999999999999999999998, 0]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = double_array_elements([-999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999])
        assert result == [-1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999998], f"Test 52 failed: got {result}, expected {[-1999999999999999999999999999999999999999998, 1999999999999999999999999999999999999999998]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = double_array_elements([1, -1, 2, -2, 4, -4, 8, -8, 16, -16, 32, -32, 64, -64, 128, 256, -256, 512, -512, 1024, -1024, 2048, -2048, 4096, -4096, 8192, -8192, 16384, -16384, 999999999])
        assert result == '8192, -8192, 16384, -16384, 32768, -32768, 1999999998]', f"Test 53 failed: got {result}, expected {'8192, -8192, 16384, -16384, 32768, -32768, 1999999998]'}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
