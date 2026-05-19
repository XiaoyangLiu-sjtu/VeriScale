# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def reverse(a):
2: ✓     return a[::-1]
```

## Complete Test File

```python
def reverse(a):
    return a[::-1]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = reverse([1, 2, 3, 4, 5])
        assert result == [5, 4, 3, 2, 1], f"Test 1 failed: got {result}, expected {[5, 4, 3, 2, 1]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = reverse([10, 20, 30, 40])
        assert result == [40, 30, 20, 10], f"Test 2 failed: got {result}, expected {[40, 30, 20, 10]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = reverse([])
        assert result == [], f"Test 3 failed: got {result}, expected {[]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = reverse([7])
        assert result == [7], f"Test 4 failed: got {result}, expected {[7]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = reverse([-1, 0, 1])
        assert result == [1, 0, -1], f"Test 5 failed: got {result}, expected {[1, 0, -1]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = reverse([1, 2])
        assert result == [2, 1], f"Test 6 failed: got {result}, expected {[2, 1]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = reverse([2, 1])
        assert result == [1, 2], f"Test 7 failed: got {result}, expected {[1, 2]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = reverse([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5], f"Test 8 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = reverse([10, -10, 20, -20, 0])
        assert result == [0, -20, 20, -10, 10], f"Test 9 failed: got {result}, expected {[0, -20, 20, -10, 10]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = reverse([2147483647, -2147483648])
        assert result == [-2147483648, 2147483647], f"Test 10 failed: got {result}, expected {[-2147483648, 2147483647]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = reverse([9223372036854775807, -9223372036854775808])
        assert result == [-9223372036854775808, 9223372036854775807], f"Test 11 failed: got {result}, expected {[-9223372036854775808, 9223372036854775807]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = reverse([1000000000000, -1000000000000, 999999999999, -999999999999])
        assert result == [-999999999999, 999999999999, -1000000000000, 1000000000000], f"Test 12 failed: got {result}, expected {[-999999999999, 999999999999, -1000000000000, 1000000000000]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = reverse([3, 1, 4, 1, 5, 9, 2, 6])
        assert result == [6, 2, 9, 5, 1, 4, 1, 3], f"Test 13 failed: got {result}, expected {[6, 2, 9, 5, 1, 4, 1, 3]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = reverse([-5, -4, -3, -2, -1])
        assert result == [-1, -2, -3, -4, -5], f"Test 14 failed: got {result}, expected {[-1, -2, -3, -4, -5]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = reverse([11, 22, 33, 44, 55, 66, 77, 88, 99])
        assert result == [99, 88, 77, 66, 55, 44, 33, 22, 11], f"Test 15 failed: got {result}, expected {[99, 88, 77, 66, 55, 44, 33, 22, 11]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = reverse([-10, 10, -20, 20, -30, 30, -40, 40])
        assert result == [40, -40, 30, -30, 20, -20, 10, -10], f"Test 16 failed: got {result}, expected {[40, -40, 30, -30, 20, -20, 10, -10]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = reverse([-999999999, 0, 999999999])
        assert result == [999999999, 0, -999999999], f"Test 17 failed: got {result}, expected {[999999999, 0, -999999999]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = reverse([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        assert result == [20, 18, 16, 14, 12, 10, 8, 6, 4, 2], f"Test 18 failed: got {result}, expected {[20, 18, 16, 14, 12, 10, 8, 6, 4, 2]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = reverse([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])
        assert result == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], f"Test 19 failed: got {result}, expected {[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = reverse([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])
        assert result == [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1], f"Test 20 failed: got {result}, expected {[-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = reverse([8, 6, 7, 5, 3, 0, 9])
        assert result == [9, 0, 3, 5, 7, 6, 8], f"Test 21 failed: got {result}, expected {[9, 0, 3, 5, 7, 6, 8]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = reverse([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
        assert result == [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100], f"Test 22 failed: got {result}, expected {[1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = reverse([-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000])
        assert result == [-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100], f"Test 23 failed: got {result}, expected {[-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = reverse([31, 41, 59, 26, 53, 58, 97])
        assert result == [97, 58, 53, 26, 59, 41, 31], f"Test 24 failed: got {result}, expected {[97, 58, 53, 26, 59, 41, 31]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = reverse([4, 3, 2, 1, 0, -1, -2, -3, -4])
        assert result == [-4, -3, -2, -1, 0, 1, 2, 3, 4], f"Test 25 failed: got {result}, expected {[-4, -3, -2, -1, 0, 1, 2, 3, 4]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = reverse([18446744073709551616, -18446744073709551616])
        assert result == [-18446744073709551616, 18446744073709551616], f"Test 26 failed: got {result}, expected {[-18446744073709551616, 18446744073709551616]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = reverse([123456789012345678901234567890, -123456789012345678901234567890])
        assert result == [-123456789012345678901234567890, 123456789012345678901234567890], f"Test 27 failed: got {result}, expected {[-123456789012345678901234567890, 123456789012345678901234567890]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = reverse([1, -1, 9007199254740993, -9007199254740993])
        assert result == [-9007199254740993, 9007199254740993, -1, 1], f"Test 28 failed: got {result}, expected {[-9007199254740993, 9007199254740993, -1, 1]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = reverse([1, 3, 4, 5])
        assert result == [5, 4, 3, 1], f"Test 29 failed: got {result}, expected {[5, 4, 3, 1]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = reverse([-1000000000000, 2, 3, 4, 700])
        assert result == [700, 4, 3, 2, -1000000000000], f"Test 30 failed: got {result}, expected {[700, 4, 3, 2, -1000000000000]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = reverse([1, 2, 6, 4, 5, 0, 0, -800, 31])
        assert result == [31, -800, 0, 0, 5, 4, 6, 2, 1], f"Test 31 failed: got {result}, expected {[31, -800, 0, 0, 5, 4, 6, 2, 1]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = reverse([1, 2, 3, 0, 5, 0])
        assert result == [0, 5, 0, 3, 2, 1], f"Test 32 failed: got {result}, expected {[0, 5, 0, 3, 2, 1]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = reverse([2, 2, 3, 4, 5, 0, 6])
        assert result == [6, 0, 5, 4, 3, 2, 2], f"Test 33 failed: got {result}, expected {[6, 0, 5, 4, 3, 2, 2]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = reverse([5, 4, 3, 2, 2, 99, -3])
        assert result == [-3, 99, 2, 2, 3, 4, 5], f"Test 34 failed: got {result}, expected {[-3, 99, 2, 2, 3, 4, 5]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = reverse([5, 4, 3, 2])
        assert result == [2, 3, 4, 5], f"Test 35 failed: got {result}, expected {[2, 3, 4, 5]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = reverse([4, 3, 4, 5])
        assert result == [5, 4, 3, 4], f"Test 36 failed: got {result}, expected {[5, 4, 3, 4]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = reverse([-5, 5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5, -5], f"Test 37 failed: got {result}, expected {[1, 2, 3, 4, 5, -5]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = reverse([1, 3, 4, 5, 0, 0, 0])
        assert result == [0, 0, 0, 5, 4, 3, 1], f"Test 38 failed: got {result}, expected {[0, 0, 0, 5, 4, 3, 1]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = reverse([-1, 2, 3, 4, 5, 16])
        assert result == [16, 5, 4, 3, 2, -1], f"Test 39 failed: got {result}, expected {[16, 5, 4, 3, 2, -1]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = reverse([1, 2, 3, 4, 5, 0])
        assert result == [0, 5, 4, 3, 2, 1], f"Test 40 failed: got {result}, expected {[0, 5, 4, 3, 2, 1]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = reverse([7, 0])
        assert result == [0, 7], f"Test 41 failed: got {result}, expected {[0, 7]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = reverse([0, 7])
        assert result == [7, 0], f"Test 42 failed: got {result}, expected {[7, 0]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = reverse([-1, 1])
        assert result == [1, -1], f"Test 43 failed: got {result}, expected {[1, -1]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = reverse([1, 0, 0])
        assert result == [0, 0, 1], f"Test 44 failed: got {result}, expected {[0, 0, 1]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = reverse([7, 0])
        assert result == [0, 7], f"Test 45 failed: got {result}, expected {[0, 7]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = reverse([1, 0, 0])
        assert result == [0, 0, 1], f"Test 46 failed: got {result}, expected {[0, 0, 1]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = reverse([-1, 1])
        assert result == [1, -1], f"Test 47 failed: got {result}, expected {[1, -1]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = reverse([1, 2, 3, 4, 5, 0])
        assert result == [0, 5, 4, 3, 2, 1], f"Test 48 failed: got {result}, expected {[0, 5, 4, 3, 2, 1]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = reverse([5, 4, 3, 2])
        assert result == [2, 3, 4, 5], f"Test 49 failed: got {result}, expected {[2, 3, 4, 5]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = reverse([0, 7])
        assert result == [7, 0], f"Test 50 failed: got {result}, expected {[7, 0]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
