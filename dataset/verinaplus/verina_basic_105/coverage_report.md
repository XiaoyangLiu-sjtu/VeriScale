# Coverage Report

Total executable lines: 8
Covered lines: 8
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def arrayProduct(a, b):
2: ✓     n = max(len(a), len(b))
3: ✓     result = []
4: ✓     for i in range(n):
5: ✓         x = a[i] if i < len(a) else 0
6: ✓         y = b[i] if i < len(b) else 0
7: ✓         result.append(x * y)
8: ✓     return result
```

## Complete Test File

```python
def arrayProduct(a, b):
    n = max(len(a), len(b))
    result = []
    for i in range(n):
        x = a[i] if i < len(a) else 0
        y = b[i] if i < len(b) else 0
        result.append(x * y)
    return result

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = arrayProduct([1, 2, 3], [4, 5, 6])
        assert result == [4, 10, 18], f"Test 1 failed: got {result}, expected {[4, 10, 18]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = arrayProduct([0, 0, 0], [1, 2, 3])
        assert result == [0, 0, 0], f"Test 2 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = arrayProduct([-1, 2, -3], [3, -4, 5])
        assert result == [-3, -8, -15], f"Test 3 failed: got {result}, expected {[-3, -8, -15]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = arrayProduct([2], [10])
        assert result == [20], f"Test 4 failed: got {result}, expected {[20]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = arrayProduct([1, 2, 3, 4], [2, 2, 2, 2])
        assert result == [2, 4, 6, 8], f"Test 5 failed: got {result}, expected {[2, 4, 6, 8]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = arrayProduct([0], [0])
        assert result == [0], f"Test 6 failed: got {result}, expected {[0]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = arrayProduct([7], [-3])
        assert result == [-21], f"Test 7 failed: got {result}, expected {[-21]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = arrayProduct([1, 2], [3, 4])
        assert result == [3, 8], f"Test 8 failed: got {result}, expected {[3, 8]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = arrayProduct([-1, -2], [-3, 5])
        assert result == [3, -10], f"Test 9 failed: got {result}, expected {[3, -10]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = arrayProduct([-1, 0, 2], [3, -4, 5])
        assert result == [-3, 0, 10], f"Test 10 failed: got {result}, expected {[-3, 0, 10]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = arrayProduct([0, 0, 0], [9, -8, 7])
        assert result == [0, 0, 0], f"Test 11 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = arrayProduct([2, 2, 2, 2], [5, -5, 0, 3])
        assert result == [10, -10, 0, 6], f"Test 12 failed: got {result}, expected {[10, -10, 0, 6]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = arrayProduct([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        assert result == [5, 8, 9, 8, 5], f"Test 13 failed: got {result}, expected {[5, 8, 9, 8, 5]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = arrayProduct([1, -1, 1, -1, 1, -1], [-1, 1, -1, 1, -1, 1])
        assert result == [-1, -1, -1, -1, -1, -1], f"Test 14 failed: got {result}, expected {[-1, -1, -1, -1, -1, -1]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = arrayProduct([2, 3, 5, 7, 11, 13, 17], [19, 23, 29, 31, 37, 41, 43])
        assert result == [38, 69, 145, 217, 407, 533, 731], f"Test 15 failed: got {result}, expected {[38, 69, 145, 217, 407, 533, 731]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = arrayProduct([1000000, -1000000, 123456789, -987654321, 42, -42, 0, 7], [-1, 2, -3, 4, -5, 6, 7, -8])
        assert result == [-1000000, -2000000, -370370367, -3950617284, -210, -252, 0, -56], f"Test 16 failed: got {result}, expected {[-1000000, -2000000, -370370367, -3950617284, -210, -252, 0, -56]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = arrayProduct([999999999999999999, -999999999999999999, 1234567890123456789], [1, -1, 0])
        assert result == [999999999999999999, 999999999999999999, 0], f"Test 17 failed: got {result}, expected {[999999999999999999, 999999999999999999, 0]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = arrayProduct([-9223372036854775808], [9223372036854775807])
        assert result == [-85070591730234615856620279821087277056], f"Test 18 failed: got {result}, expected {[-85070591730234615856620279821087277056]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = arrayProduct([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], f"Test 19 failed: got {result}, expected {[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = arrayProduct([0, -1, 2, -3, 4, -5, 6, -7, 8, -9], [9, -8, 7, -6, 5, -4, 3, -2, 1, 0])
        assert result == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0], f"Test 20 failed: got {result}, expected {[0, 8, 14, 18, 20, 20, 18, 14, 8, 0]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = arrayProduct([2147483647, -2147483648], [-2147483648, 2147483647])
        assert result == [-4611686016279904256, -4611686016279904256], f"Test 21 failed: got {result}, expected {[-4611686016279904256, -4611686016279904256]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = arrayProduct([-5, -4, -3, -2], [-1, -2, -3, -4])
        assert result == [5, 8, 9, 8], f"Test 22 failed: got {result}, expected {[5, 8, 9, 8]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = arrayProduct([3, 3, 3, 3], [0, 1, -1, 2])
        assert result == [0, 3, -3, 6], f"Test 23 failed: got {result}, expected {[0, 3, -3, 6]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = arrayProduct([1000000000000, 1, -1, 2, -2], [0, -1000000000000, 1000000000000, -3, 3])
        assert result == [0, -1000000000000, -1000000000000, -6, -6], f"Test 24 failed: got {result}, expected {[0, -1000000000000, -1000000000000, -6, -6]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = arrayProduct([8, -8, 8], [-8, 8, -8])
        assert result == [-64, -64, -64], f"Test 25 failed: got {result}, expected {[-64, -64, -64]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = arrayProduct([4, 0, -4, 8, -8, 16, -16, 32, -32], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert result == [4, 0, -12, 32, -40, 96, -112, 256, -288], f"Test 26 failed: got {result}, expected {[4, 0, -12, 32, -40, 96, -112, 256, -288]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = arrayProduct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [12, 22, 30, 36, 40, 42, 42, 40, 36, 30, 22, 12], f"Test 27 failed: got {result}, expected {[12, 22, 30, 36, 40, 42, 42, 40, 36, 30, 22, 12]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = arrayProduct([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 28 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = arrayProduct([0, 0], [123, -456])
        assert result == [0, 0], f"Test 29 failed: got {result}, expected {[0, 0]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = arrayProduct([0], [999999999999999999999999])
        assert result == [0], f"Test 30 failed: got {result}, expected {[0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = arrayProduct([2147483646, 2147483647, -2147483648, -2147483647, 0, 1], [1, -1, 1, -1, 12345, -12345])
        assert result == [2147483646, -2147483647, -2147483648, 2147483647, 0, -12345], f"Test 31 failed: got {result}, expected {[2147483646, -2147483647, -2147483648, 2147483647, 0, -12345]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = arrayProduct([-2147483648, -1, 0, 1, 2147483647, 42], [2, 3, 4, 5, 6, 7])
        assert result == [-4294967296, -3, 0, 5, 12884901882, 294], f"Test 32 failed: got {result}, expected {[-4294967296, -3, 0, 5, 12884901882, 294]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = arrayProduct([0, 5, 0, -5, 0], [9, 0, -9, 0, 3])
        assert result == [0, 0, 0, 0, 0], f"Test 33 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = arrayProduct([6, 6, 6], [6, -6, 0])
        assert result == [36, -36, 0], f"Test 34 failed: got {result}, expected {[36, -36, 0]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = arrayProduct([1, 2, 3, 2, 1, 0, -1, -2], [-2, -1, 0, 1, 2, 3, 2, 1])
        assert result == [-2, -2, 0, 2, 2, 0, -2, -2], f"Test 35 failed: got {result}, expected {[-2, -2, 0, 2, 2, 0, -2, -2]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = arrayProduct([11, -22, 33, -44, 55, -66, 77, -88, 99, -110, 121], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        assert result == [11, -44, 99, -176, 275, -396, 539, -704, 891, -1100, 1331], f"Test 36 failed: got {result}, expected {[11, -44, 99, -176, 275, -396, 539, -704, 891, -1100, 1331]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = arrayProduct([1, 2, -44], [4, 5, 6])
        assert result == [4, 10, -264], f"Test 37 failed: got {result}, expected {[4, 10, -264]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = arrayProduct([0, 37, 0], [1, 2, 3])
        assert result == [0, 74, 0], f"Test 38 failed: got {result}, expected {[0, 74, 0]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = arrayProduct([0, 1, 0], [3, 2, 1])
        assert result == [0, 2, 0], f"Test 39 failed: got {result}, expected {[0, 2, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = arrayProduct([0, 0, 23, 0], [1, 2, 3, 0])
        assert result == [0, 0, 69, 0], f"Test 40 failed: got {result}, expected {[0, 0, 69, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = arrayProduct([-3, 2, -1], [3, -4, 5])
        assert result == [-9, -8, -5], f"Test 41 failed: got {result}, expected {[-9, -8, -5]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = arrayProduct([0, -3, 2, -1], [-4, 5, 42, -66])
        assert result == [0, -15, 84, 66], f"Test 42 failed: got {result}, expected {[0, -15, 84, 66]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = arrayProduct([-1, 2, -2], [3, -4, 5])
        assert result == [-3, -8, -10], f"Test 43 failed: got {result}, expected {[-3, -8, -10]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = arrayProduct([2, -3, -9], [3, -4, 5])
        assert result == [6, 12, -45], f"Test 44 failed: got {result}, expected {[6, 12, -45]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = arrayProduct([-1, 2, -3], [5, -4, 6])
        assert result == [-5, -8, -18], f"Test 45 failed: got {result}, expected {[-5, -8, -18]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = arrayProduct([-7], [10])
        assert result == [-70], f"Test 46 failed: got {result}, expected {[-70]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = arrayProduct([2, 19], [10, 0])
        assert result == [20, 0], f"Test 47 failed: got {result}, expected {[20, 0]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = arrayProduct([4, 3, 2, -8], [2, 2, 2, 2])
        assert result == [8, 6, 4, -16], f"Test 48 failed: got {result}, expected {[8, 6, 4, -16]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = arrayProduct([1, 2, 3, 4], [2, 2, 2, 6])
        assert result == [2, 4, 6, 24], f"Test 49 failed: got {result}, expected {[2, 4, 6, 24]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = arrayProduct([1, 2, 3, 4, 0], [2, 2, -22, 1, -9223372036854775808])
        assert result == [2, 4, -66, 4, 0], f"Test 50 failed: got {result}, expected {[2, 4, -66, 4, 0]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = arrayProduct([1, 2, 3, 4], [2, 2, 2, 0])
        assert result == [2, 4, 6, 0], f"Test 51 failed: got {result}, expected {[2, 4, 6, 0]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = arrayProduct([1, 0, 3, 4], [2, 2, 2, 2])
        assert result == [2, 0, 6, 8], f"Test 52 failed: got {result}, expected {[2, 0, 6, 8]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = arrayProduct([1, -5], [5, -5])
        assert result == [5, 25], f"Test 53 failed: got {result}, expected {[5, 25]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = arrayProduct([1, 3], [4, 5])
        assert result == [4, 15], f"Test 54 failed: got {result}, expected {[4, 15]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = arrayProduct([0, 0], [0, 0])
        assert result == [0, 0], f"Test 55 failed: got {result}, expected {[0, 0]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = arrayProduct([-66], [0])
        assert result == [0], f"Test 56 failed: got {result}, expected {[0]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = arrayProduct([0, -8], [0, 0])
        assert result == [0, 0], f"Test 57 failed: got {result}, expected {[0, 0]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = arrayProduct([0, 16], [0, 0])
        assert result == [0, 0], f"Test 58 failed: got {result}, expected {[0, 0]}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = arrayProduct([0, -2147483647], [0, 0])
        assert result == [0, 0], f"Test 59 failed: got {result}, expected {[0, 0]}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = arrayProduct([7, 0], [16, 0])
        assert result == [112, 0], f"Test 60 failed: got {result}, expected {[112, 0]}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = arrayProduct([6], [0])
        assert result == [0], f"Test 61 failed: got {result}, expected {[0]}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = arrayProduct([7], [-4])
        assert result == [-28], f"Test 62 failed: got {result}, expected {[-28]}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = arrayProduct([7, 0], [-3, 2147483647])
        assert result == [-21, 0], f"Test 63 failed: got {result}, expected {[-21, 0]}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = arrayProduct([7, 0], [-3, 0])
        assert result == [-21, 0], f"Test 64 failed: got {result}, expected {[-21, 0]}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = arrayProduct([2, 1], [4, 1])
        assert result == [8, 1], f"Test 65 failed: got {result}, expected {[8, 1]}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = arrayProduct([1, 2], [4, 3])
        assert result == [4, 6], f"Test 66 failed: got {result}, expected {[4, 6]}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = arrayProduct([2, 0], [4, 9])
        assert result == [8, 0], f"Test 67 failed: got {result}, expected {[8, 0]}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = arrayProduct([1234567890123456788, 2], [3, 4])
        assert result == [3703703670370370364, 8], f"Test 68 failed: got {result}, expected {[3703703670370370364, 8]}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = arrayProduct([-12345, 0], [4, 3])
        assert result == [-49380, 0], f"Test 69 failed: got {result}, expected {[-49380, 0]}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = arrayProduct([-1, -2, -9223372036854775808], [-3, 5, 0])
        assert result == [3, -10, 0], f"Test 70 failed: got {result}, expected {[3, -10, 0]}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = arrayProduct([-2, 0], [5, -3])
        assert result == [-10, 0], f"Test 71 failed: got {result}, expected {[-10, 0]}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = arrayProduct([-2, 19], [-3, 5])
        assert result == [6, 95], f"Test 72 failed: got {result}, expected {[6, 95]}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = arrayProduct([-2, -1], [5, -3])
        assert result == [-10, 3], f"Test 73 failed: got {result}, expected {[-10, 3]}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = arrayProduct([-2, -1], [-3, 5])
        assert result == [6, -5], f"Test 74 failed: got {result}, expected {[6, -5]}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = arrayProduct([-1, 0, 2], [3, 13, 5])
        assert result == [-3, 0, 10], f"Test 75 failed: got {result}, expected {[-3, 0, 10]}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = arrayProduct([-1, 0, 2], [3, -4, -5])
        assert result == [-3, 0, -10], f"Test 76 failed: got {result}, expected {[-3, 0, -10]}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = arrayProduct([-1, 0, 0], [5, -4, -9223372036854775808])
        assert result == [-5, 0, 0], f"Test 77 failed: got {result}, expected {[-5, 0, 0]}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = arrayProduct([0, -1, 0], [7, -8, 9])
        assert result == [0, 8, 0], f"Test 78 failed: got {result}, expected {[0, 8, 0]}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = arrayProduct([1000000, 0, 0, 0], [7, -8, 9, 0])
        assert result == [7000000, 0, 0, 0], f"Test 79 failed: got {result}, expected {[7000000, 0, 0, 0]}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = arrayProduct([0, 0, 0, 0], [9, -8, 7, 0])
        assert result == [0, 0, 0, 0], f"Test 80 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = arrayProduct([0, 0, 0], [7, 9, -12345])
        assert result == [0, 0, 0], f"Test 81 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = arrayProduct([-1000000000000, 2, 2, 2, 9223372036854775807], [5, -5, 3, 1234567890123456788, 0])
        assert result == [-5000000000000, -10, 6, 2469135780246913576, 0], f"Test 82 failed: got {result}, expected {[-5000000000000, -10, 6, 2469135780246913576, 0]}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = arrayProduct([2, 2, 2, 2], [3, 1, -5, 5])
        assert result == [6, 2, -10, 10], f"Test 83 failed: got {result}, expected {[6, 2, -10, 10]}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = arrayProduct([2, 2, 2, 2147483647], [-3, 0, -5, 5])
        assert result == [-6, 0, -10, 10737418235], f"Test 84 failed: got {result}, expected {[-6, 0, -10, 10737418235]}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = arrayProduct([1, 2, 3, 4, 5, 121], [5, 4, 3, 2, 1, 0])
        assert result == [5, 8, 9, 8, 5, 0], f"Test 85 failed: got {result}, expected {[5, 8, 9, 8, 5, 0]}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = arrayProduct([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        assert result == [1, 4, 9, 16, 25], f"Test 86 failed: got {result}, expected {[1, 4, 9, 16, 25]}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = arrayProduct([1, 2, 3, 4, 5], [5, 4, 2, 1, 0])
        assert result == [5, 8, 6, 4, 0], f"Test 87 failed: got {result}, expected {[5, 8, 6, 4, 0]}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = arrayProduct([1, 2, 3, 4, 5], [5, 4, 3, 2147483647, 1])
        assert result == [5, 8, 9, 8589934588, 5], f"Test 88 failed: got {result}, expected {[5, 8, 9, 8589934588, 5]}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = arrayProduct([5, 4, 3, 2, 1], [5, 4, 3, 2, 1])
        assert result == [25, 16, 9, 4, 1], f"Test 89 failed: got {result}, expected {[25, 16, 9, 4, 1]}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = arrayProduct([1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1])
        assert result == [1, 1, 1, 1, 1, 1], f"Test 90 failed: got {result}, expected {[1, 1, 1, 1, 1, 1]}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = arrayProduct([0, -1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, -1, 1, 12345])
        assert result == [0, -1, -1, -1, -1, -1, 12345], f"Test 91 failed: got {result}, expected {[0, -1, -1, -1, -1, -1, 12345]}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = arrayProduct([-1, 1, -1, 1, -1, 1], [-1, 1, -2, 1, -2, 1])
        assert result == [1, 1, 2, 1, 2, 1], f"Test 92 failed: got {result}, expected {[1, 1, 2, 1, 2, 1]}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = arrayProduct([-1, 1, -1, 1, -1, 1], [-1, 1, -1, 1, 0, 1])
        assert result == [1, 1, 1, 1, 0, 1], f"Test 93 failed: got {result}, expected {[1, 1, 1, 1, 0, 1]}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = arrayProduct([-1, 1, -1, 1, -1, 1], [0, 1, -1, 1, 1, -1])
        assert result == [0, 1, 1, 1, -1, -1], f"Test 94 failed: got {result}, expected {[0, 1, 1, 1, -1, -1]}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = arrayProduct([17, 13, 11, 7, 5, 2], [19, 29, 31, 37, 41, 43])
        assert result == [323, 377, 341, 259, 205, 86], f"Test 95 failed: got {result}, expected {[323, 377, 341, 259, 205, 86]}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = arrayProduct([2, 3, 5, 7, 11, 13, 17], [43, 41, 37, 31, 29, 23, 19])
        assert result == [86, 123, 185, 217, 319, 299, 323], f"Test 96 failed: got {result}, expected {[86, 123, 185, 217, 319, 299, 323]}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = arrayProduct([2, 3, 5, 7, 11, 13, 0], [43, 41, 37, 31, 29, 23, -2])
        assert result == [86, 123, 185, 217, 319, 299, 0], f"Test 97 failed: got {result}, expected {[86, 123, 185, 217, 319, 299, 0]}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = arrayProduct([1000000, -1000000, 0, -987654321, 42, -42, 0, 7], [-1, 2, -3, 4, -5, 6, 7, -8])
        assert result == [-1000000, -2000000, 0, -3950617284, -210, -252, 0, -56], f"Test 98 failed: got {result}, expected {[-1000000, -2000000, 0, -3950617284, -210, -252, 0, -56]}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = arrayProduct([43, 1000000, -1000000, 123456789, -987654321, 42, -42, 0, 7], [-1, 2, -3, 4, -5, 6, 7, -8, 0])
        assert result == [-43, 2000000, 3000000, 493827156, 4938271605, 252, -294, 0, 0], f"Test 99 failed: got {result}, expected {[-43, 2000000, 3000000, 493827156, 4938271605, 252, -294, 0, 0]}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = arrayProduct([7, 0, -42, 42, -987654321, 123456789, 1000000], [-1, 2, -3, 4, -5, 6, 7])
        assert result == [-7, 0, 126, 168, 4938271605, 740740734, 7000000], f"Test 100 failed: got {result}, expected {[-7, 0, 126, 168, 4938271605, 740740734, 7000000]}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = arrayProduct([1234567890123456789, -999999999999999999, 999999999999999999], [1, -1, 0])
        assert result == [1234567890123456789, 999999999999999999, 0], f"Test 101 failed: got {result}, expected {[1234567890123456789, 999999999999999999, 0]}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = arrayProduct([18, -999999999999999999, 999999999999999999], [0, -1, -4])
        assert result == [0, 999999999999999999, -3999999999999999996], f"Test 102 failed: got {result}, expected {[0, 999999999999999999, -3999999999999999996]}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = arrayProduct([999999999999999999, -999999999999999999, 1234567890123456789], [0, -1, 1])
        assert result == [0, 999999999999999999, 1234567890123456789], f"Test 103 failed: got {result}, expected {[0, 999999999999999999, 1234567890123456789]}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = arrayProduct([999999999999999999, -999999999999999999, 1234567890123456789, -456], [1, -1, 0, 0])
        assert result == [999999999999999999, 999999999999999999, 0, 0], f"Test 104 failed: got {result}, expected {[999999999999999999, 999999999999999999, 0, 0]}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = arrayProduct([1234567890123456789, -999999999999999999, 999999999999999999, 0], [1, -1, 0, 0])
        assert result == [1234567890123456789, 999999999999999999, 0, 0], f"Test 105 failed: got {result}, expected {[1234567890123456789, 999999999999999999, 0, 0]}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = arrayProduct([-9223372036854775808, 18], [9223372036854775807, 0])
        assert result == [-85070591730234615856620279821087277056, 0], f"Test 106 failed: got {result}, expected {[-85070591730234615856620279821087277056, 0]}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = arrayProduct([0, -9223372036854775808], [9223372036854775807, -32])
        assert result == [0, 295147905179352825856], f"Test 107 failed: got {result}, expected {[0, 295147905179352825856]}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = arrayProduct([43], [-9223372036854775809])
        assert result == [-396604997584755359787], f"Test 108 failed: got {result}, expected {[-396604997584755359787]}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = arrayProduct([-9223372036854775809], [9223372036854775806])
        assert result == [-85070591730234615856620279821087277054], f"Test 109 failed: got {result}, expected {[-85070591730234615856620279821087277054]}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = arrayProduct([9223372036854775808], [9223372036854775807])
        assert result == [85070591730234615856620279821087277056], f"Test 110 failed: got {result}, expected {[85070591730234615856620279821087277056]}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = arrayProduct([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 12])
        assert result == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0], f"Test 111 failed: got {result}, expected {[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = arrayProduct([1, 1, 1, 1, 1, 1, 1, 1, 1, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        assert result == [2, 2, 2, 2, 2, 2, 2, 2, 2, 4], f"Test 112 failed: got {result}, expected {[2, 2, 2, 2, 2, 2, 2, 2, 2, 4]}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = arrayProduct([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, -1000000000000])
        assert result == [2, 2, 2, 2, 2, 2, 2, 2, 2, -1000000000000], f"Test 113 failed: got {result}, expected {[2, 2, 2, 2, 2, 2, 2, 2, 2, -1000000000000]}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = arrayProduct([0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 0], [9, -8, 7, -6, 5, -3, 3, -2, 1, 0, 0])
        assert result == [0, 8, 14, 18, 20, 15, 18, 14, 8, 0, 0], f"Test 114 failed: got {result}, expected {[0, 8, 14, 18, 20, 15, 18, 14, 8, 0, 0]}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = arrayProduct([0, -1, 2, -3, 4, -5, 6, -7, 8, -9], [9, -8, 7, -6, 5, -4, 3, -2, 1, -6])
        assert result == [0, 8, 14, 18, 20, 20, 18, 14, 8, 54], f"Test 115 failed: got {result}, expected {[0, 8, 14, 18, 20, 20, 18, 14, 8, 54]}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = arrayProduct([0, -1, 2, -3, 4, -5, -6, -7, 8, -9], [9, -8, 7, -6, 5, -12345, 3, -2, 1, 0])
        assert result == [0, 8, 14, 18, 20, 61725, -18, 14, 8, 0], f"Test 116 failed: got {result}, expected {[0, 8, 14, 18, 20, 61725, -18, 14, 8, 0]}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = arrayProduct([-9, 8, -7, 6, -5, 4, -3, 2, -1, 0], [9, -8, 7, -6, 5, -4, 3, -2, 1, 0])
        assert result == [-81, -64, -49, -36, -25, -16, -9, -4, -1, 0], f"Test 117 failed: got {result}, expected {[-81, -64, -49, -36, -25, -16, -9, -4, -1, 0]}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = arrayProduct([0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 999999999999999999], [0, 1, -2, 3, -4, 5, -6, 7, -8, 9, 9])
        assert result == [0, -1, -4, -9, -16, -25, -36, -49, -64, -81, 8999999999999999991], f"Test 118 failed: got {result}, expected {[0, -1, -4, -9, -16, -25, -36, -49, -64, -81, 8999999999999999991]}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = arrayProduct([0, -1, 4, -3, 4, -5, 6, -7, 8, -9], [9, -8, 7, -6, 5, -4, 3, -2, 1, 0])
        assert result == [0, 8, 28, 18, 20, 20, 18, 14, 8, 0], f"Test 119 failed: got {result}, expected {[0, 8, 28, 18, 20, 20, 18, 14, 8, 0]}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = arrayProduct([0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 0], [121, 42, 1, -2, 3, -4, 5, -6, 7, -8, 9])
        assert result == [0, -42, 2, 6, 12, 20, 30, 42, 56, 72, 0], f"Test 120 failed: got {result}, expected {[0, -42, 2, 6, 12, 20, 30, 42, 56, 72, 0]}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = arrayProduct([-2147483648, 2147483647, 55], [2147483647, -2147483648, 123])
        assert result == [-4611686016279904256, -4611686016279904256, 6765], f"Test 121 failed: got {result}, expected {[-4611686016279904256, -4611686016279904256, 6765]}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = arrayProduct([2147483647, -2147483648], [2147483647, -2147483648])
        assert result == [4611686014132420609, 4611686018427387904], f"Test 122 failed: got {result}, expected {[4611686014132420609, 4611686018427387904]}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = arrayProduct([0, 2147483645], [-2147483648, 2147483647])
        assert result == [0, 4611686009837453315], f"Test 123 failed: got {result}, expected {[0, 4611686009837453315]}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = arrayProduct([-2, -3, -4, -5], [-1, -2, -3, -4])
        assert result == [2, 6, 12, 20], f"Test 124 failed: got {result}, expected {[2, 6, 12, 20]}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = arrayProduct([-5, -4, -3], [-1, -3, -4])
        assert result == [5, 12, 12], f"Test 125 failed: got {result}, expected {[5, 12, 12]}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = arrayProduct([-2, -3, 41, -5], [-1, -2, -3, -4])
        assert result == [2, 6, -123, 20], f"Test 126 failed: got {result}, expected {[2, 6, -123, 20]}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = arrayProduct([-5, -4, -3, -2], [-1, -2, -4, 0])
        assert result == [5, 8, 12, 0], f"Test 127 failed: got {result}, expected {[5, 8, 12, 0]}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = arrayProduct([-5, -4, 11, 0], [-1, -2, -3, -4])
        assert result == [5, 8, -33, 0], f"Test 128 failed: got {result}, expected {[5, 8, -33, 0]}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = arrayProduct([-5, -4, -3, -2, 18], [-1, -2, -3, -8, 9223372036854775807])
        assert result == [5, 8, 9, 16, 166020696663385964526], f"Test 129 failed: got {result}, expected {[5, 8, 9, 16, 166020696663385964526]}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = arrayProduct([3, 3, 6], [0, 12, -1])
        assert result == [0, 36, -6], f"Test 130 failed: got {result}, expected {[0, 36, -6]}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = arrayProduct([3, 6, 3, 3, 29], [-42, 2, -1, 1, 0])
        assert result == [-126, 12, -3, 3, 0], f"Test 131 failed: got {result}, expected {[-126, 12, -3, 3, 0]}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = arrayProduct([3, 3, 3, 2], [2, -1, 1, 0])
        assert result == [6, -3, 3, 0], f"Test 132 failed: got {result}, expected {[6, -3, 3, 0]}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = arrayProduct([1000000000000, 1, -1, 2, -2], [0, -1000000000000, -3, 3, 9223372036854775806])
        assert result == [0, -1000000000000, 3, 6, -18446744073709551612], f"Test 133 failed: got {result}, expected {[0, -1000000000000, 3, 6, -18446744073709551612]}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = arrayProduct([-2, 2, -1, 1, 1000000000000], [0, -1000000000000, 1000000000000, -3, 3])
        assert result == [0, -2000000000000, -1000000000000, -3, 3000000000000], f"Test 134 failed: got {result}, expected {[0, -2000000000000, -1000000000000, -3, 3000000000000]}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = arrayProduct([1000000000000, 1, -1, 2, -2], [-1, -1000000000000, 1000000000001, -3, 3])
        assert result == [-1000000000000, -1000000000000, -1000000000001, -6, -6], f"Test 135 failed: got {result}, expected {[-1000000000000, -1000000000000, -1000000000001, -6, -6]}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = arrayProduct([-8, 8, 0], [-8, 8, -8])
        assert result == [64, 64, 0], f"Test 136 failed: got {result}, expected {[64, 64, 0]}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = arrayProduct([16, -8, 9223372036854775807], [-8, 8, -8])
        assert result == [-128, -64, -73786976294838206456], f"Test 137 failed: got {result}, expected {[-128, -64, -73786976294838206456]}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = arrayProduct([8, -8, 8], [-8, -8, -8])
        assert result == [-64, 64, -64], f"Test 138 failed: got {result}, expected {[-64, 64, -64]}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = arrayProduct([8, -8, 8, 4294967294], [-8, 7, -8, 0])
        assert result == [-64, -56, -64, 0], f"Test 139 failed: got {result}, expected {[-64, -56, -64, 0]}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = arrayProduct([8, -8, 9], [-8, 8, -8])
        assert result == [-64, -64, -72], f"Test 140 failed: got {result}, expected {[-64, -64, -72]}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = arrayProduct([4, 0, -4, 121, -8, 16, -16, 32, -32], [1, 2, 3, 4, 5, 6, 7, 9, 0])
        assert result == [4, 0, -12, 484, -40, 96, -112, 288, 0], f"Test 141 failed: got {result}, expected {[4, 0, -12, 484, -40, 96, -112, 288, 0]}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = arrayProduct([4, 0, -4, 8, -8, 16, -16, 32, -32], [9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [36, 0, -28, 48, -40, 64, -48, 64, -32], f"Test 142 failed: got {result}, expected {[36, 0, -28, 48, -40, 64, -48, 64, -32]}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = arrayProduct([-32, 32, -16, 16, -8, 8, -4, 0, 4, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0])
        assert result == [-32, 64, -48, 64, -40, 48, -28, 0, 36, 0, 0], f"Test 143 failed: got {result}, expected {[-32, 64, -48, 64, -40, 48, -28, 0, 36, 0, 0]}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = arrayProduct([4, 0, -4, 8, -8, 16, -16, 32, -32, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        assert result == [4, 0, -12, 32, -40, 96, -112, 256, -288, 0], f"Test 144 failed: got {result}, expected {[4, 0, -12, 32, -40, 96, -112, 256, -288, 0]}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = arrayProduct([4, 0, -4, 8, -8, 16, 32, -32, 1234567890123456789], [0, 9, 8, 7, 6, 5, 4, 2, 1])
        assert result == [0, 0, -32, 56, -48, 80, 128, -64, 1234567890123456789], f"Test 145 failed: got {result}, expected {[0, 0, -32, 56, -48, 80, 128, -64, 1234567890123456789]}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = arrayProduct([4, 0, -4, 8, -8, 16, 7, 32, -32, 0], [0, 9, 8, 7, 7, 5, 4, 3, 2, 1])
        assert result == [0, 0, -32, 56, -56, 80, 28, 96, -64, 0], f"Test 146 failed: got {result}, expected {[0, 0, -32, 56, -56, 80, 28, 96, -64, 0]}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = arrayProduct([4, 0, -4, 8, -8, 16, -16, 32, -32, -456], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        assert result == [4, 0, -12, 32, -40, 96, -112, 256, -288, 0], f"Test 147 failed: got {result}, expected {[4, 0, -12, 32, -40, 96, -112, 256, -288, 0]}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = arrayProduct([12, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [144, 0, 100, 81, 64, 49, 36, 25, 16, 9, 4, 1], f"Test 148 failed: got {result}, expected {[144, 0, 100, 81, 64, 49, 36, 25, 16, 9, 4, 1]}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = arrayProduct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        assert result == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144], f"Test 149 failed: got {result}, expected {[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = arrayProduct([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 12], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [12, 22, 30, 36, 40, 42, 42, 40, 36, 33, 22, 12], f"Test 150 failed: got {result}, expected {[12, 22, 30, 36, 40, 42, 42, 40, 36, 33, 22, 12]}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = arrayProduct([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 151 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = arrayProduct([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, -7, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 152 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = arrayProduct([-1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, -9223372036854775808, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        assert result == [-1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], f"Test 153 failed: got {result}, expected {[-1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = arrayProduct([0, 0, 1000000000001, -22], [123, -456, 13, -9223372036854775808])
        assert result == [0, 0, 13000000000013, 202914184810805067776], f"Test 154 failed: got {result}, expected {[0, 0, 13000000000013, 202914184810805067776]}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = arrayProduct([0, 0], [-455, 123])
        assert result == [0, 0], f"Test 155 failed: got {result}, expected {[0, 0]}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = arrayProduct([0, 0], [999999999999999999999999, 0])
        assert result == [0, 0], f"Test 156 failed: got {result}, expected {[0, 0]}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = arrayProduct([0], [-999999999999999999999999])
        assert result == [0], f"Test 157 failed: got {result}, expected {[0]}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = arrayProduct([0, -9223372036854775808], [999999999999999999999999, 2147483648])
        assert result == [0, -19807040628566084398385987584], f"Test 158 failed: got {result}, expected {[0, -19807040628566084398385987584]}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = arrayProduct([-1, 0], [999999999999999999999999, 0])
        assert result == [-999999999999999999999999, 0], f"Test 159 failed: got {result}, expected {[-999999999999999999999999, 0]}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = arrayProduct([2147483646, 2147483647, -2147483648, -2147483647, 0, 36], [-12345, 12345, -1, 1, -1, 1])
        assert result == [-26510685609870, 26510685622215, 2147483648, -2147483647, 0, 36], f"Test 160 failed: got {result}, expected {[-26510685609870, 26510685622215, 2147483648, -2147483647, 0, 36]}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = arrayProduct([2147483646, 0, -2147483648, -2147483647, 0, 1], [1, -1, 1, -1, 12345, -12345])
        assert result == [2147483646, 0, -2147483648, 2147483647, 0, -12345], f"Test 161 failed: got {result}, expected {[2147483646, 0, -2147483648, 2147483647, 0, -12345]}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = arrayProduct([2147483646, 2147483647, -2147483648, -2147483647, 0, 1], [-1, 1, 0, 12345, -12345, 0])
        assert result == [-2147483646, 2147483647, 0, -26510685622215, 0, 0], f"Test 162 failed: got {result}, expected {[-2147483646, 2147483647, 0, -26510685622215, 0, 0]}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = arrayProduct([-2147483648, -1, 0, 2, 2147483647, 42], [2, 3, 4, 5, 6, 7])
        assert result == [-4294967296, -3, 0, 10, 12884901882, 294], f"Test 163 failed: got {result}, expected {[-4294967296, -3, 0, 10, 12884901882, 294]}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = arrayProduct([-4294967296, -1, 1, 1, 2147483647, 42, -22], [37, 7, 6, 5, 4, 3, 2])
        assert result == [-158913789952, -7, 6, 5, 8589934588, 126, -44], f"Test 164 failed: got {result}, expected {[-158913789952, -7, 6, 5, 8589934588, 126, -44]}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = arrayProduct([-2147483648, -1, 0, 1, 13, 42], [2, 3, 4, 5, 6, 7])
        assert result == [-4294967296, -3, 0, 5, 78, 294], f"Test 165 failed: got {result}, expected {[-4294967296, -3, 0, 5, 78, 294]}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = arrayProduct([-2147483648, -1, 0, 123456789, 2147483647, 42, 11], [2, 3, 4, 5, 6, 7, -1000000000000])
        assert result == [-4294967296, -3, 0, 617283945, 12884901882, 294, -11000000000000], f"Test 166 failed: got {result}, expected {[-4294967296, -3, 0, 617283945, 12884901882, 294, -11000000000000]}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = arrayProduct([-1, 0, 3, 2147483647, 42], [2, 3, 4, 6, 7])
        assert result == [-2, 0, 12, 12884901882, 294], f"Test 167 failed: got {result}, expected {[-2, 0, 12, 12884901882, 294]}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = arrayProduct([38, 42, 2147483647, 1, 0, -1, -2147483648], [1, 3, 4, 5, 6, 7, 4])
        assert result == [38, 126, 8589934588, 5, 0, -7, -8589934592], f"Test 168 failed: got {result}, expected {[38, 126, 8589934588, 5, 0, -7, -8589934592]}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = arrayProduct([-2147483648, -1, 0, 1, 2147483647, 42], [7, -6, 5, 4, 3, 2])
        assert result == [-15032385536, 6, 0, 4, 6442450941, 84], f"Test 169 failed: got {result}, expected {[-15032385536, 6, 0, 4, 6442450941, 84]}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = arrayProduct([5, 0, -5, 0, 42], [9, 0, -9, 0, 3])
        assert result == [45, 0, 45, 0, 126], f"Test 170 failed: got {result}, expected {[45, 0, 45, 0, 126]}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = arrayProduct([0, 5, 0, -5, 0], [-9, 0, -9, 0, 3])
        assert result == [0, 0, 0, 0, 0], f"Test 171 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = arrayProduct([0, 5, 0, 5, -2], [3, 0, -9, 1, 9])
        assert result == [0, 0, 0, 5, -18], f"Test 172 failed: got {result}, expected {[0, 0, 0, 5, -18]}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = arrayProduct([0, -5, 0, 5, 0], [9, 0, -9, 0, 3])
        assert result == [0, 0, 0, 0, 0], f"Test 173 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = arrayProduct([0, 5, 0, -5, 0], [9, 1, -9, 0, 0])
        assert result == [0, 5, 0, 0, 0], f"Test 174 failed: got {result}, expected {[0, 5, 0, 0, 0]}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = arrayProduct([-5, 1, 5, 0], [3, -9, 0, 9])
        assert result == [-15, -9, 0, 0], f"Test 175 failed: got {result}, expected {[-15, -9, 0, 0]}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = arrayProduct([6, -6, 9223372036854775806], [6, -6, 0])
        assert result == [36, 36, 0], f"Test 176 failed: got {result}, expected {[36, 36, 0]}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = arrayProduct([6, 6, 6, 38], [6, -6, 0, 0])
        assert result == [36, -36, 0, 0], f"Test 177 failed: got {result}, expected {[36, -36, 0, 0]}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = arrayProduct([6, 6, 6], [0, -6, 6])
        assert result == [0, -36, 36], f"Test 178 failed: got {result}, expected {[0, -36, 36]}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = arrayProduct([6, 6, 6, 0], [6, -6, 0, 0])
        assert result == [36, -36, 0, 0], f"Test 179 failed: got {result}, expected {[36, -36, 0, 0]}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = arrayProduct([1, 2, 3, 2, 1, 0, -1, -2, 0], [-2, -1, 0, 1, 2, 3, 2, 1, 0])
        assert result == [-2, -2, 0, 2, 2, 0, -2, -2, 0], f"Test 180 failed: got {result}, expected {[-2, -2, 0, 2, 2, 0, -2, -2, 0]}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = arrayProduct([1, 2, 3, 2, 1, 0, -2], [-2, -1, 0, 1, 2, 3, 2])
        assert result == [-2, -2, 0, 2, 2, 0, -4], f"Test 181 failed: got {result}, expected {[-2, -2, 0, 2, 2, 0, -4]}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = arrayProduct([1, 2, 0, 2, 1, 0, -1, -2, 29], [-2, -1, 0, 1, 2, 3, 2, 1, 31])
        assert result == [-2, -2, 0, 2, 2, 0, -2, -2, 899], f"Test 182 failed: got {result}, expected {[-2, -2, 0, 2, 2, 0, -2, -2, 899]}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = arrayProduct([11, -22, 33, -44, 55, -66, 77, -88, 99, -110, 121], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == [121, -220, 297, -352, 385, -396, 385, -352, 297, -220, 121], f"Test 183 failed: got {result}, expected {[121, -220, 297, -352, 385, -396, 385, -352, 297, -220, 121]}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = arrayProduct([11, -23, 33, -44, 55, -66, 77, -88, 99, -110, 121], [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11])
        assert result == [11, -46, 99, -176, 275, -396, 539, -704, 792, -1100, 1331], f"Test 184 failed: got {result}, expected {[11, -46, 99, -176, 275, -396, 539, -704, 792, -1100, 1331]}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = arrayProduct([121, -110, 99, -88, 77, -66, 55, -44, 33, -22, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        assert result == [121, -220, 297, -352, 385, -396, 385, -352, 297, -220, 121], f"Test 185 failed: got {result}, expected {[121, -220, 297, -352, 385, -396, 385, -352, 297, -220, 121]}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = arrayProduct([0], [1])
        assert result == [0], f"Test 186 failed: got {result}, expected {[0]}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = arrayProduct([-66, 29], [0, 1])
        assert result == [0, 29], f"Test 187 failed: got {result}, expected {[0, 29]}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = arrayProduct([-16], [0])
        assert result == [0], f"Test 188 failed: got {result}, expected {[0]}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = arrayProduct([1000001, 42], [1, 0])
        assert result == [1000001, 0], f"Test 189 failed: got {result}, expected {[1000001, 0]}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = arrayProduct([-456, 12], [0, 0])
        assert result == [0, 0], f"Test 190 failed: got {result}, expected {[0, 0]}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = arrayProduct([1], [0])
        assert result == [0], f"Test 191 failed: got {result}, expected {[0]}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = arrayProduct([1, 0], [0, -8])
        assert result == [0, 0], f"Test 192 failed: got {result}, expected {[0, 0]}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = arrayProduct([1, 0], [0, 0])
        assert result == [0, 0], f"Test 193 failed: got {result}, expected {[0, 0]}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = arrayProduct([-12], [0])
        assert result == [0], f"Test 194 failed: got {result}, expected {[0]}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = arrayProduct([1, 2, -88, -22], [5, 4, 3, 0])
        assert result == [5, 8, -264, 0], f"Test 195 failed: got {result}, expected {[5, 8, -264, 0]}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = arrayProduct([1, 2, -9223372036854775809], [5, 4, 3])
        assert result == [5, 8, -27670116110564327427], f"Test 196 failed: got {result}, expected {[5, 8, -27670116110564327427]}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = arrayProduct([1, 2, 0], [5, 4, 4])
        assert result == [5, 8, 0], f"Test 197 failed: got {result}, expected {[5, 8, 0]}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = arrayProduct([1, 2, 0, -88], [3, 4, 5, 0])
        assert result == [3, 8, 0, 0], f"Test 198 failed: got {result}, expected {[3, 8, 0, 0]}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = arrayProduct([-3, -2, -1], [0, 5, 4])
        assert result == [0, -10, -4], f"Test 199 failed: got {result}, expected {[0, -10, -4]}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = arrayProduct([-3, -2, 9223372036854775807, 0], [4, 5, 43, 4])
        assert result == [-12, -10, 396604997584755359701, 0], f"Test 200 failed: got {result}, expected {[-12, -10, 396604997584755359701, 0]}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = arrayProduct([1, -2, -3], [4, 5, 0])
        assert result == [4, -10, 0], f"Test 201 failed: got {result}, expected {[4, -10, 0]}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = arrayProduct([-1, -2, -3], [4, 5, -9])
        assert result == [-4, -10, 27], f"Test 202 failed: got {result}, expected {[-4, -10, 27]}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = arrayProduct([0, 0, 0, 0], [1, 2, 3, 4])
        assert result == [0, 0, 0, 0], f"Test 203 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = arrayProduct([0, 0, 0, 0, 0], [1, 2, 3, 4, 17])
        assert result == [0, 0, 0, 0, 0], f"Test 204 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = arrayProduct([0, 0, 0, 0, -1], [32, 1, 2, 3, 4])
        assert result == [0, 0, 0, 0, -4], f"Test 205 failed: got {result}, expected {[0, 0, 0, 0, -4]}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = arrayProduct([0, 0, 0, 0, 0], [1, -44, 3, 4, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 206 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = arrayProduct([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 1000000000001])
        assert result == [2, 2, 2, 2, 2, 2, 2, 2, 2, 1000000000001], f"Test 207 failed: got {result}, expected {[2, 2, 2, 2, 2, 2, 2, 2, 2, 1000000000001]}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = arrayProduct([1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 0])
        assert result == [2, 2, 2, 2, 2, 2, 2, 2, 0], f"Test 208 failed: got {result}, expected {[2, 2, 2, 2, 2, 2, 2, 2, 0]}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = arrayProduct([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 2, 2, 0, 2, 2, 2, 2, 2, 2])
        assert result == [0, 2, 2, 0, 2, 2, 2, 2, 2, 2], f"Test 209 failed: got {result}, expected {[0, 2, 2, 0, 2, 2, 2, 2, 2, 2]}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = arrayProduct([999999999999999999], [-1])
        assert result == [-999999999999999999], f"Test 210 failed: got {result}, expected {[-999999999999999999]}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = arrayProduct([999999999999999999, 0], [-1, 0])
        assert result == [-999999999999999999, 0], f"Test 211 failed: got {result}, expected {[-999999999999999999, 0]}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = arrayProduct([999999999999999999, 0], [-1, 1])
        assert result == [-999999999999999999, 0], f"Test 212 failed: got {result}, expected {[-999999999999999999, 0]}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = arrayProduct([0, 0], [-1, 0])
        assert result == [0, 0], f"Test 213 failed: got {result}, expected {[0, 0]}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
