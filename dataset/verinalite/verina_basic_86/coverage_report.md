# Coverage Report

Total executable lines: 6
Covered lines: 6
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def rotate(a, offset):
2: ✓     n = len(a)
3: ✓     if n == 0:
4: ✓         return a
5: ✓     offset %= n
6: ✓     return a[offset:] + a[:offset]
```

## Complete Test File

```python
def rotate(a, offset):
    n = len(a)
    if n == 0:
        return a
    offset %= n
    return a[offset:] + a[:offset]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = rotate([1, 2, 3, 4, 5], 2)
        assert result == [3, 4, 5, 1, 2], f"Test 1 failed: got {result}, expected {[3, 4, 5, 1, 2]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = rotate([10, 20, 30, 40], 1)
        assert result == [20, 30, 40, 10], f"Test 2 failed: got {result}, expected {[20, 30, 40, 10]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = rotate([], 5)
        assert result == [], f"Test 3 failed: got {result}, expected {[]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = rotate([7], 0)
        assert result == [7], f"Test 4 failed: got {result}, expected {[7]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = rotate([-1, -2, -3, -4], 3)
        assert result == [-4, -1, -2, -3], f"Test 5 failed: got {result}, expected {[-4, -1, -2, -3]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = rotate([5, 10, 15], 5)
        assert result == [15, 5, 10], f"Test 6 failed: got {result}, expected {[15, 5, 10]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = rotate([1, 2], 1)
        assert result == [2, 1], f"Test 7 failed: got {result}, expected {[2, 1]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = rotate([1, 2], 3)
        assert result == [2, 1], f"Test 8 failed: got {result}, expected {[2, 1]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = rotate([1, 2, 3], 1)
        assert result == [2, 3, 1], f"Test 9 failed: got {result}, expected {[2, 3, 1]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = rotate([1, 2, 3], 2)
        assert result == [3, 1, 2], f"Test 10 failed: got {result}, expected {[3, 1, 2]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = rotate([1, 2, 3], 4)
        assert result == [2, 3, 1], f"Test 11 failed: got {result}, expected {[2, 3, 1]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = rotate([-1, -2, -3, -4], 2)
        assert result == [-3, -4, -1, -2], f"Test 12 failed: got {result}, expected {[-3, -4, -1, -2]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = rotate([100, -50, 0, 25, -75, 200], 5)
        assert result == [200, 100, -50, 0, 25, -75], f"Test 13 failed: got {result}, expected {[200, 100, -50, 0, 25, -75]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = rotate([4, 4, 4, 2, 2, 9, 9], 3)
        assert result == [2, 2, 9, 9, 4, 4, 4], f"Test 14 failed: got {result}, expected {[2, 2, 9, 9, 4, 4, 4]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = rotate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
        assert result == [9, 0, 1, 2, 3, 4, 5, 6, 7, 8], f"Test 15 failed: got {result}, expected {[9, 0, 1, 2, 3, 4, 5, 6, 7, 8]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = rotate([2, 3, 5, 7, 11, 13, 17], 100)
        assert result == [5, 7, 11, 13, 17, 2, 3], f"Test 16 failed: got {result}, expected {[5, 7, 11, 13, 17, 2, 3]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = rotate([0, 0, 0, 5, 0, 0], 4)
        assert result == [0, 0, 0, 0, 0, 5], f"Test 17 failed: got {result}, expected {[0, 0, 0, 0, 0, 5]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = rotate([9007199254740991, -9007199254740991, 42, -42], 2)
        assert result == [42, -42, 9007199254740991, -9007199254740991], f"Test 18 failed: got {result}, expected {[42, -42, 9007199254740991, -9007199254740991]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = rotate([-1000000000, -2000000000, -3000000000], 1)
        assert result == [-2000000000, -3000000000, -1000000000], f"Test 19 failed: got {result}, expected {[-2000000000, -3000000000, -1000000000]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = rotate([5, 10, 15, 20, 25], 2147483647)
        assert result == [15, 20, 25, 5, 10], f"Test 20 failed: got {result}, expected {[15, 20, 25, 5, 10]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = rotate([5, 10, 15, 20, 25], 2147483648)
        assert result == [20, 25, 5, 10, 15], f"Test 21 failed: got {result}, expected {[20, 25, 5, 10, 15]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = rotate([1, 3, 4, 5], 2)
        assert result == [4, 5, 1, 3], f"Test 22 failed: got {result}, expected {[4, 5, 1, 3]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = rotate([-1000000000, 2, 3, 4, -2147483648], 2)
        assert result == [3, 4, -2147483648, -1000000000, 2], f"Test 23 failed: got {result}, expected {[3, 4, -2147483648, -1000000000, 2]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = rotate([1, 2, 3, 4, 5, 99], 2)
        assert result == [3, 4, 5, 99, 1, 2], f"Test 24 failed: got {result}, expected {[3, 4, 5, 99, 1, 2]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = rotate([-15, 5, 4, 3, 2, 1], 4)
        assert result == [2, 1, -15, 5, 4, 3], f"Test 25 failed: got {result}, expected {[2, 1, -15, 5, 4, 3]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = rotate([1, 2, 3, 4, 5, 0], 2)
        assert result == [3, 4, 5, 0, 1, 2], f"Test 26 failed: got {result}, expected {[3, 4, 5, 0, 1, 2]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = rotate([1, 2, 3, 4, 28, 0, 0], 2)
        assert result == [3, 4, 28, 0, 0, 1, 2], f"Test 27 failed: got {result}, expected {[3, 4, 28, 0, 0, 1, 2]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = rotate([10, 18, 30, 40, 1000000000], 2)
        assert result == [30, 40, 1000000000, 10, 18], f"Test 28 failed: got {result}, expected {[30, 40, 1000000000, 10, 18]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = rotate([10, 20, 30], 2)
        assert result == [30, 10, 20], f"Test 29 failed: got {result}, expected {[30, 10, 20]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = rotate([19, 30, 40, -2147483648, 0], 1)
        assert result == [30, 40, -2147483648, 0, 19], f"Test 30 failed: got {result}, expected {[30, 40, -2147483648, 0, 19]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = rotate([20, 30, 40], 1)
        assert result == [30, 40, 20], f"Test 31 failed: got {result}, expected {[30, 40, 20]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = rotate([40, 31, 18], 1)
        assert result == [31, 18, 40], f"Test 32 failed: got {result}, expected {[31, 18, 40]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = rotate([40, 30, 20, 10], 1)
        assert result == [30, 20, 10, 40], f"Test 33 failed: got {result}, expected {[30, 20, 10, 40]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = rotate([12, 20, 30, 40, -30, 0, 0], 2)
        assert result == [30, 40, -30, 0, 0, 12, 20], f"Test 34 failed: got {result}, expected {[30, 40, -30, 0, 0, 12, 20]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = rotate([7, -20], 1)
        assert result == [-20, 7], f"Test 35 failed: got {result}, expected {[-20, 7]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = rotate([-1, -2, -3, -4, 0], 6)
        assert result == [-2, -3, -4, 0, -1], f"Test 36 failed: got {result}, expected {[-2, -3, -4, 0, -1]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = rotate([-1, -2, -3, -4, -1], 2)
        assert result == [-3, -4, -1, -1, -2], f"Test 37 failed: got {result}, expected {[-3, -4, -1, -1, -2]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = rotate([-2, -3], 3)
        assert result == [-3, -2], f"Test 38 failed: got {result}, expected {[-3, -2]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = rotate([-1, 0, -3, -4], 5)
        assert result == [0, -3, -4, -1], f"Test 39 failed: got {result}, expected {[0, -3, -4, -1]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = rotate([-1, -2, -3, -4, -20], 4)
        assert result == [-20, -1, -2, -3, -4], f"Test 40 failed: got {result}, expected {[-20, -1, -2, -3, -4]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = rotate([-4, -3, 0, -1], 6)
        assert result == [0, -1, -4, -3], f"Test 41 failed: got {result}, expected {[0, -1, -4, -3]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = rotate([-1, -2, -3, -4, 18], 9)
        assert result == [18, -1, -2, -3, -4], f"Test 42 failed: got {result}, expected {[18, -1, -2, -3, -4]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = rotate([-1, -2, -3, -4, 0, 30], 4)
        assert result == [0, 30, -1, -2, -3, -4], f"Test 43 failed: got {result}, expected {[0, 30, -1, -2, -3, -4]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = rotate([-1, -2, -3, -4, 33, 0, 0], 3)
        assert result == [-4, 33, 0, 0, -1, -2, -3], f"Test 44 failed: got {result}, expected {[-4, 33, 0, 0, -1, -2, -3]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = rotate([15, 10, 5], 7)
        assert result == [10, 5, 15], f"Test 45 failed: got {result}, expected {[10, 5, 15]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = rotate([5, 10, 15], 2)
        assert result == [15, 5, 10], f"Test 46 failed: got {result}, expected {[15, 5, 10]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = rotate([5, 10, 15], 4)
        assert result == [10, 15, 5], f"Test 47 failed: got {result}, expected {[10, 15, 5]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = rotate([1, 2, 3, 4, 5, 10], 4)
        assert result == [5, 10, 1, 2, 3, 4], f"Test 48 failed: got {result}, expected {[5, 10, 1, 2, 3, 4]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = rotate([1, 2, 3, 4, 5], 12)
        assert result == [3, 4, 5, 1, 2], f"Test 49 failed: got {result}, expected {[3, 4, 5, 1, 2]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = rotate([1, 2, 3, 4, 5], 24)
        assert result == [5, 1, 2, 3, 4], f"Test 50 failed: got {result}, expected {[5, 1, 2, 3, 4]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = rotate([1, 2, 3, 4, 5, 2147483648], 1)
        assert result == [2, 3, 4, 5, 2147483648, 1], f"Test 51 failed: got {result}, expected {[2, 3, 4, 5, 2147483648, 1]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = rotate([1, 2, 3, 4, 5], 56)
        assert result == [2, 3, 4, 5, 1], f"Test 52 failed: got {result}, expected {[2, 3, 4, 5, 1]}"
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
