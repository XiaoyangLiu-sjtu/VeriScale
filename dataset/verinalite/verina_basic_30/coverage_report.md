# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def elementWiseModulo(a, b):
2: ✓     return [x % y for x, y in zip(a, b)]
```

## Complete Test File

```python
def elementWiseModulo(a, b):
    return [x % y for x, y in zip(a, b)]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = elementWiseModulo([10, 20, 30], [3, 7, 5])
        assert result == [1, 6, 0], f"Test 1 failed: got {result}, expected {[1, 6, 0]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = elementWiseModulo([100, 200, 300, 400], [10, 20, 30, 50])
        assert result == [0, 0, 0, 0], f"Test 2 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = elementWiseModulo([-10, -20, 30], [3, -7, 5])
        assert result == [2, 1, 0], f"Test 3 failed: got {result}, expected {[2, 1, 0]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = elementWiseModulo([5], [2])
        assert result == [1], f"Test 4 failed: got {result}, expected {[1]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = elementWiseModulo([-5], [-2])
        assert result == [1], f"Test 5 failed: got {result}, expected {[1]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = elementWiseModulo([0, 14], [3, 5])
        assert result == [0, 4], f"Test 6 failed: got {result}, expected {[0, 4]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = elementWiseModulo([-13, 27], [5, -4])
        assert result == [2, 3], f"Test 7 failed: got {result}, expected {[2, 3]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = elementWiseModulo([10, -20, 30], [3, 7, -5])
        assert result == [1, 1, 0], f"Test 8 failed: got {result}, expected {[1, 1, 0]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = elementWiseModulo([1000000, -999999, 123456789], [97, -31, 1000])
        assert result == [27, 30, 789], f"Test 9 failed: got {result}, expected {[27, 30, 789]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = elementWiseModulo([9, -8, 7, -6], [-2, -3, -4, -5])
        assert result == [1, 1, 3, 4], f"Test 10 failed: got {result}, expected {[1, 1, 3, 4]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = elementWiseModulo([11, -22, 33, -44, 55], [6, 7, -8, 9, -10])
        assert result == [5, 6, 1, 1, 5], f"Test 11 failed: got {result}, expected {[5, 6, 1, 1, 5]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = elementWiseModulo([101, 103, 107, 109, 113], [2, 3, 5, 7, 11])
        assert result == [1, 1, 2, 4, 3], f"Test 12 failed: got {result}, expected {[1, 1, 2, 4, 3]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = elementWiseModulo([-9223372036854775808, 9223372036854775807, 0, 42, -42, 999999999999], [3, -7, 5, -9, 11, 13])
        assert result == [1, 0, 0, 6, 2, 0], f"Test 13 failed: got {result}, expected {[1, 0, 0, 6, 2, 0]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = elementWiseModulo([7, 14, 21, 28, 35, 42, 49], [5, 6, 7, 8, 9, 10, 11])
        assert result == [2, 2, 0, 4, 8, 2, 5], f"Test 14 failed: got {result}, expected {[2, 2, 0, 4, 8, 2, 5]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = elementWiseModulo([3, 6, 9, 12, 15, 18, 21, 24], [2, -5, 4, -7, 6, -9, 8, -11])
        assert result == [1, 1, 1, 5, 3, 0, 5, 2], f"Test 15 failed: got {result}, expected {[1, 1, 1, 5, 3, 0, 5, 2]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = elementWiseModulo([12345678901234567890, -12345678901234567890], [97, -97])
        assert result == [3, 94], f"Test 16 failed: got {result}, expected {[3, 94]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = elementWiseModulo([8, 16, 24, 32, 40, 48, 56, 64, 72], [3, 5, 7, 9, 11, 13, 15, 17, 19])
        assert result == [2, 1, 3, 5, 7, 9, 11, 13, 15], f"Test 17 failed: got {result}, expected {[2, 1, 3, 5, 7, 9, 11, 13, 15]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = elementWiseModulo([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], f"Test 18 failed: got {result}, expected {[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = elementWiseModulo([0, -1, 1], [-2, 3, -4])
        assert result == [0, 2, 1], f"Test 19 failed: got {result}, expected {[0, 2, 1]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = elementWiseModulo([-100, -50, 50, 100], [9, -8, 7, -6])
        assert result == [8, 6, 1, 4], f"Test 20 failed: got {result}, expected {[8, 6, 1, 4]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = elementWiseModulo([-9, -18, -27], [-4, -5, -6])
        assert result == [3, 2, 3], f"Test 21 failed: got {result}, expected {[3, 2, 3]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = elementWiseModulo([-1000, -2000], [256, 512])
        assert result == [24, 48], f"Test 22 failed: got {result}, expected {[24, 48]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = elementWiseModulo([17, 19, 23, 29], [4, 6, 8, 10])
        assert result == [1, 1, 7, 9], f"Test 23 failed: got {result}, expected {[1, 1, 7, 9]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = elementWiseModulo([5, 5, 5, 5, 5], [2, 3, 4, 5, 6])
        assert result == [1, 2, 1, 0, 5], f"Test 24 failed: got {result}, expected {[1, 2, 1, 0, 5]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = elementWiseModulo([2, 4, 8, 16, 32, 64, 128, 256], [3, 5, 7, 9, 11, 13, 15, 17])
        assert result == [2, 4, 1, 7, 10, 12, 8, 1], f"Test 25 failed: got {result}, expected {[2, 4, 1, 7, 10, 12, 8, 1]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = elementWiseModulo([12, -24, 36, -48, 60, -72, 84, -96, 108, -120, 132, -144], [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27])
        assert result == [2, 4, 0, 7, 8, 3, 16, 18, 3, 18, 7, 18], f"Test 26 failed: got {result}, expected {[2, 4, 0, 7, 8, 3, 16, 18, 3, 18, 7, 18]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = elementWiseModulo([100, 200, 300, 399], [10, 20, 30, 50])
        assert result == [0, 0, 0, 49], f"Test 27 failed: got {result}, expected {[0, 0, 0, 49]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = elementWiseModulo([100, 200, 300, 401], [50, 30, 20, 10])
        assert result == [0, 20, 0, 1], f"Test 28 failed: got {result}, expected {[0, 20, 0, 1]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = elementWiseModulo([0, 30, -20, -10], [-7, 5, 33, -72])
        assert result == [0, 0, 13, 62], f"Test 29 failed: got {result}, expected {[0, 0, 13, 62]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = elementWiseModulo([-10, -20, 0], [13, -7, 5])
        assert result == [3, 1, 0], f"Test 30 failed: got {result}, expected {[3, 1, 0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = elementWiseModulo([-10, 33, 29], [5, -7, 3])
        assert result == [0, 5, 2], f"Test 31 failed: got {result}, expected {[0, 5, 2]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = elementWiseModulo([5, 0], [2, 15])
        assert result == [1, 0], f"Test 32 failed: got {result}, expected {[1, 0]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = elementWiseModulo([-5], [-3])
        assert result == [1], f"Test 33 failed: got {result}, expected {[1]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = elementWiseModulo([0, 14], [5, 3])
        assert result == [0, 2], f"Test 34 failed: got {result}, expected {[0, 2]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = elementWiseModulo([14, 0], [3, 5])
        assert result == [2, 0], f"Test 35 failed: got {result}, expected {[2, 0]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = elementWiseModulo([0, 14, 0], [90, 3, -48])
        assert result == [0, 2, 0], f"Test 36 failed: got {result}, expected {[0, 2, 0]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = elementWiseModulo([-13, 27, 0], [5, -4, 399])
        assert result == [2, 3, 0], f"Test 37 failed: got {result}, expected {[2, 3, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = elementWiseModulo([0, 27, 0], [5, -4, 11])
        assert result == [0, 3, 0], f"Test 38 failed: got {result}, expected {[0, 3, 0]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = elementWiseModulo([27, -13], [5, 113])
        assert result == [2, 100], f"Test 39 failed: got {result}, expected {[2, 100]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = elementWiseModulo([13, 27], [-4, 4])
        assert result == [1, 3], f"Test 40 failed: got {result}, expected {[1, 3]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = elementWiseModulo([10, -20, 30], [3, 7, 401])
        assert result == [1, 1, 30], f"Test 41 failed: got {result}, expected {[1, 1, 30]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = elementWiseModulo([-20, 30], [8, -5])
        assert result == [4, 0], f"Test 42 failed: got {result}, expected {[4, 0]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = elementWiseModulo([-40, 10, 0], [3, 7, -5])
        assert result == [2, 3, 0], f"Test 43 failed: got {result}, expected {[2, 3, 0]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = elementWiseModulo([30, -20, 10], [1, 7, -5])
        assert result == [0, 1, 0], f"Test 44 failed: got {result}, expected {[0, 1, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = elementWiseModulo([0, 30, -20], [-5, 8, 3])
        assert result == [0, 6, 1], f"Test 45 failed: got {result}, expected {[0, 6, 1]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = elementWiseModulo([-999999, 1000000], [-31, 1000])
        assert result == [30, 0], f"Test 46 failed: got {result}, expected {[30, 0]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = elementWiseModulo([1000000, 123456790, 13], [97, -31, 1000])
        assert result == [27, 3, 13], f"Test 47 failed: got {result}, expected {[27, 3, 13]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = elementWiseModulo([1000000, 0, 0], [97, -31, 1000])
        assert result == [27, 0, 0], f"Test 48 failed: got {result}, expected {[27, 0, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = elementWiseModulo([1000000, 123456791, 16], [1000, 31, 97])
        assert result == [0, 4, 16], f"Test 49 failed: got {result}, expected {[0, 4, 16]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = elementWiseModulo([1, 2, 3, 4], [1, -7, 1, 1])
        assert result == [0, 2, 0, 0], f"Test 50 failed: got {result}, expected {[0, 2, 0, 0]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = elementWiseModulo([1, 2, 3, 4], [1, 1, 1, 256])
        assert result == [0, 0, 0, 4], f"Test 51 failed: got {result}, expected {[0, 0, 0, 4]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
