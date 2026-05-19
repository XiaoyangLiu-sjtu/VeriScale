# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def arraySum(a, b):
2: ✓     return [x + y for x, y in zip(a, b)]
```

## Complete Test File

```python
def arraySum(a, b):
    return [x + y for x, y in zip(a, b)]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = arraySum([1, 2, 3], [4, 5, 6])
        assert result == [5, 7, 9], f"Test 1 failed: got {result}, expected {[5, 7, 9]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = arraySum([0, 0, 0], [0, 0, 0])
        assert result == [0, 0, 0], f"Test 2 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = arraySum([-1, 2, 3], [1, -2, 4])
        assert result == [0, 0, 7], f"Test 3 failed: got {result}, expected {[0, 0, 7]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = arraySum([10], [-10])
        assert result == [0], f"Test 4 failed: got {result}, expected {[0]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = arraySum([100, 200, 300], [100, 200, 300])
        assert result == [200, 400, 600], f"Test 5 failed: got {result}, expected {[200, 400, 600]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = arraySum([1, 2], [3, 4])
        assert result == [4, 6], f"Test 6 failed: got {result}, expected {[4, 6]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = arraySum([1, 2, 3, 4], [10, 20, 30, 40])
        assert result == [11, 22, 33, 44], f"Test 7 failed: got {result}, expected {[11, 22, 33, 44]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = arraySum([1000000, 2000000, 3000000, 4000000, 5000000], [-5000000, -4000000, -3000000, -2000000, -1000000])
        assert result == [-4000000, -2000000, 0, 2000000, 4000000], f"Test 8 failed: got {result}, expected {[-4000000, -2000000, 0, 2000000, 4000000]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = arraySum([2, 3, 5, 7, 11, 13, 17], [19, 23, 29, 31, 37, 41, 43])
        assert result == [21, 26, 34, 38, 48, 54, 60], f"Test 9 failed: got {result}, expected {[21, 26, 34, 38, 48, 54, 60]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = arraySum([4, 4, 4, 4, 4, 4, 4, 4], [1, 2, 3, 4, 5, 6, 7, 8])
        assert result == [5, 6, 7, 8, 9, 10, 11, 12], f"Test 10 failed: got {result}, expected {[5, 6, 7, 8, 9, 10, 11, 12]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = arraySum([999999999999999999999, -999999999999999999999], [1, -1])
        assert result == [1000000000000000000000, -1000000000000000000000], f"Test 11 failed: got {result}, expected {[1000000000000000000000, -1000000000000000000000]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = arraySum([123456789012345678901234567890, -123456789012345678901234567890, 0], [-1, 1, 999999999999999999999999999999])
        assert result == [123456789012345678901234567889, -123456789012345678901234567889, 999999999999999999999999999999], f"Test 12 failed: got {result}, expected {[123456789012345678901234567889, -123456789012345678901234567889, 999999999999999999999999999999]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = arraySum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        assert result == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], f"Test 13 failed: got {result}, expected {[9, 9, 9, 9, 9, 9, 9, 9, 9, 9]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = arraySum([7, 7, 7], [7, 7, 7])
        assert result == [14, 14, 14], f"Test 14 failed: got {result}, expected {[14, 14, 14]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = arraySum([9223372036854775807, -9223372036854775808, 3141592653589793, -2718281828459045], [1, -1, -3141592653589793, 2718281828459045])
        assert result == [9223372036854775808, -9223372036854775809, 0, 0], f"Test 15 failed: got {result}, expected {[9223372036854775808, -9223372036854775809, 0, 0]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = arraySum([-100, 0, 100, 200], [300, -200, 0, -100])
        assert result == [200, -200, 100, 100], f"Test 16 failed: got {result}, expected {[200, -200, 100, 100]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = arraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13], f"Test 17 failed: got {result}, expected {[13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = arraySum([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], [377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0])
        assert result == [377, 234, 145, 91, 58, 39, 29, 26, 29, 39, 58, 91, 145, 234, 377], f"Test 18 failed: got {result}, expected {[377, 234, 145, 91, 58, 39, 29, 26, 29, 39, 58, 91, 145, 234, 377]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = arraySum([-2147483648, 2147483647], [2147483647, -2147483648])
        assert result == [-1, -1], f"Test 19 failed: got {result}, expected {[-1, -1]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = arraySum([5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5])
        assert result == [10, 10, 10, 10, 10, 10], f"Test 20 failed: got {result}, expected {[10, 10, 10, 10, 10, 10]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = arraySum([-3, -3, -3, -3, -3, -3], [9, 8, 7, 6, 5, 4])
        assert result == [6, 5, 4, 3, 2, 1], f"Test 21 failed: got {result}, expected {[6, 5, 4, 3, 2, 1]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = arraySum([100000000000000000000000000000000000000000000000000, -100000000000000000000000000000000000000000000000000, 42], [-99999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999, -42])
        assert result == [1, -1, 0], f"Test 22 failed: got {result}, expected {[1, -1, 0]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = arraySum([1, 2, 3, 0], [4, 5, 6, 0])
        assert result == [5, 7, 9, 0], f"Test 23 failed: got {result}, expected {[5, 7, 9, 0]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = arraySum([-1, 2, 0], [13, -2, 4])
        assert result == [12, 0, 4], f"Test 24 failed: got {result}, expected {[12, 0, 4]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = arraySum([-1, 2, 66], [-2, 5, 0])
        assert result == [-3, 7, 66], f"Test 25 failed: got {result}, expected {[-3, 7, 66]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = arraySum([-1, 41, 2], [4, -2, 1])
        assert result == [3, 39, 3], f"Test 26 failed: got {result}, expected {[3, 39, 3]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = arraySum([10, 0], [-10, 999999999999999999999999999999])
        assert result == [0, 999999999999999999999999999999], f"Test 27 failed: got {result}, expected {[0, 999999999999999999999999999999]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = arraySum([10, 0], [-10, -66])
        assert result == [0, -66], f"Test 28 failed: got {result}, expected {[0, -66]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = arraySum([10, 0], [0, -10])
        assert result == [10, -10], f"Test 29 failed: got {result}, expected {[10, -10]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = arraySum([300, 100, 0], [100, 200, 300])
        assert result == [400, 300, 300], f"Test 30 failed: got {result}, expected {[400, 300, 300]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = arraySum([2, 200, 300], [100, 200, 300])
        assert result == [102, 400, 600], f"Test 31 failed: got {result}, expected {[102, 400, 600]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = arraySum([0, 200, 300], [100, 200, 300])
        assert result == [100, 400, 600], f"Test 32 failed: got {result}, expected {[100, 400, 600]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = arraySum([200, 300], [300, -999999999999999999])
        assert result == [500, -999999999999999699], f"Test 33 failed: got {result}, expected {[500, -999999999999999699]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = arraySum([300, 31], [99999999999999999999999999999999999999999999999999, 200])
        assert result == [100000000000000000000000000000000000000000000000299, 231], f"Test 34 failed: got {result}, expected {[100000000000000000000000000000000000000000000000299, 231]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = arraySum([1, 2, 0, 5], [6, 7, 6, 5])
        assert result == [7, 9, 6, 10], f"Test 35 failed: got {result}, expected {[7, 9, 6, 10]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = arraySum([4, 3, 2], [-66, 6, 7])
        assert result == [-62, 9, 9], f"Test 36 failed: got {result}, expected {[-62, 9, 9]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = arraySum([4, 3, 1], [7, 8, 5])
        assert result == [11, 11, 6], f"Test 37 failed: got {result}, expected {[11, 11, 6]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = arraySum([42], [-43])
        assert result == [-1], f"Test 38 failed: got {result}, expected {[-1]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = arraySum([42, 0], [-42, 100])
        assert result == [0, 100], f"Test 39 failed: got {result}, expected {[0, 100]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = arraySum([42, 42], [-41, 0])
        assert result == [1, 42], f"Test 40 failed: got {result}, expected {[1, 42]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = arraySum([-1, 0], [4, 4])
        assert result == [3, 4], f"Test 41 failed: got {result}, expected {[3, 4]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = arraySum([2, 0], [4, 9])
        assert result == [6, 9], f"Test 42 failed: got {result}, expected {[6, 9]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = arraySum([9223372036854775807, 2], [3, 4])
        assert result == [9223372036854775810, 6], f"Test 43 failed: got {result}, expected {[9223372036854775810, 6]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = arraySum([2, 0], [3, -42])
        assert result == [5, -42], f"Test 44 failed: got {result}, expected {[5, -42]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = arraySum([1, 4], [-4, 3])
        assert result == [-3, 7], f"Test 45 failed: got {result}, expected {[-3, 7]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = arraySum([1, 2, 0], [3, 4, 20])
        assert result == [4, 6, 20], f"Test 46 failed: got {result}, expected {[4, 6, 20]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = arraySum([-10, -5], [5, 9])
        assert result == [-5, 4], f"Test 47 failed: got {result}, expected {[-5, 4]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = arraySum([-5], [10])
        assert result == [5], f"Test 48 failed: got {result}, expected {[5]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = arraySum([-5, -10], [233, 10])
        assert result == [228, 0], f"Test 49 failed: got {result}, expected {[228, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = arraySum([-10, -5], [10, 10])
        assert result == [0, 5], f"Test 50 failed: got {result}, expected {[0, 5]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = arraySum([-5, 0], [5, 10])
        assert result == [0, 10], f"Test 51 failed: got {result}, expected {[0, 10]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = arraySum([-5, -10], [10, 5])
        assert result == [5, -5], f"Test 52 failed: got {result}, expected {[5, -5]}"
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
