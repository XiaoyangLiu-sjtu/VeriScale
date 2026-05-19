# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def findEvenNumbers(arr):
2: ✓     return [x for x in arr if x % 2 == 0]
```

## Complete Test File

```python
def findEvenNumbers(arr):
    return [x for x in arr if x % 2 == 0]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = findEvenNumbers([1, 2, 3, 4, 5, 6])
        assert result == [2, 4, 6], f"Test 1 failed: got {result}, expected {[2, 4, 6]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = findEvenNumbers([7, 8, 10, 13, 14])
        assert result == [8, 10, 14], f"Test 2 failed: got {result}, expected {[8, 10, 14]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = findEvenNumbers([1, 3, 5, 7])
        assert result == [], f"Test 3 failed: got {result}, expected {[]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = findEvenNumbers([])
        assert result == [], f"Test 4 failed: got {result}, expected {[]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = findEvenNumbers([0, -2, -3, -4, 5])
        assert result == [0, -2, -4], f"Test 5 failed: got {result}, expected {[0, -2, -4]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = findEvenNumbers([2, 2, 3])
        assert result == [2, 2], f"Test 6 failed: got {result}, expected {[2, 2]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = findEvenNumbers([1])
        assert result == [], f"Test 7 failed: got {result}, expected {[]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = findEvenNumbers([-3])
        assert result == [], f"Test 8 failed: got {result}, expected {[]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = findEvenNumbers([1, 3, 5, 7, 9])
        assert result == [], f"Test 9 failed: got {result}, expected {[]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = findEvenNumbers([2, 1, 4, 3, 6, 5])
        assert result == [2, 4, 6], f"Test 10 failed: got {result}, expected {[2, 4, 6]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = findEvenNumbers([-1, -2, -3, -4, -5, -6])
        assert result == [-2, -4, -6], f"Test 11 failed: got {result}, expected {[-2, -4, -6]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = findEvenNumbers([0, 0, 1, 2, 2, 3, 4, 4])
        assert result == [0, 0, 2, 2, 4, 4], f"Test 12 failed: got {result}, expected {[0, 0, 2, 2, 4, 4]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = findEvenNumbers([9007199254740990, 9007199254740991, -9007199254740990, -9007199254740991])
        assert result == [9007199254740990, -9007199254740990], f"Test 13 failed: got {result}, expected {[9007199254740990, -9007199254740990]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = findEvenNumbers([11, 13, 17, 19])
        assert result == [], f"Test 14 failed: got {result}, expected {[]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = findEvenNumbers([9, 7, 5, 3, 1, -1, -3])
        assert result == [], f"Test 15 failed: got {result}, expected {[]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = findEvenNumbers([5, -8, 13, 0, -21, 34, 55, -144])
        assert result == [-8, 0, 34, -144], f"Test 16 failed: got {result}, expected {[-8, 0, 34, -144]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = findEvenNumbers([2, 3, 2, 3, 2, 3, 2, 3])
        assert result == [2, 2, 2, 2], f"Test 17 failed: got {result}, expected {[2, 2, 2, 2]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = findEvenNumbers([-101, 101])
        assert result == [], f"Test 18 failed: got {result}, expected {[]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = findEvenNumbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
        assert result == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], f"Test 19 failed: got {result}, expected {[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = findEvenNumbers([2147483647, 2147483646, -2147483648, -2147483647])
        assert result == [2147483646, -2147483648], f"Test 20 failed: got {result}, expected {[2147483646, -2147483648]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = findEvenNumbers([1000000000000000, 1000000000000001, -1000000000000000, -1000000000000001])
        assert result == [1000000000000000, -1000000000000000], f"Test 21 failed: got {result}, expected {[1000000000000000, -1000000000000000]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = findEvenNumbers([1, 2, 3, 2, 1])
        assert result == [2, 2], f"Test 22 failed: got {result}, expected {[2, 2]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = findEvenNumbers([1, 3, 5, 7, 8, 10, 12])
        assert result == [8, 10, 12], f"Test 23 failed: got {result}, expected {[8, 10, 12]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = findEvenNumbers([8, 10, 12, 1, 3, 5, 7])
        assert result == [8, 10, 12], f"Test 24 failed: got {result}, expected {[8, 10, 12]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = findEvenNumbers([9, 7, 4, 5, 3])
        assert result == [4], f"Test 25 failed: got {result}, expected {[4]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = findEvenNumbers([9, 7, 5, 3, 2])
        assert result == [2], f"Test 26 failed: got {result}, expected {[2]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = findEvenNumbers([2, 9, 7, 5, 3])
        assert result == [2], f"Test 27 failed: got {result}, expected {[2]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = findEvenNumbers([1, 2, 4, 6, 7, 9])
        assert result == [2, 4, 6], f"Test 28 failed: got {result}, expected {[2, 4, 6]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = findEvenNumbers([2, 8, 1, 3, 5, 10])
        assert result == [2, 8, 10], f"Test 29 failed: got {result}, expected {[2, 8, 10]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = findEvenNumbers([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1])
        assert result == [-10, -8, -6, -4, -2, 0], f"Test 30 failed: got {result}, expected {[-10, -8, -6, -4, -2, 0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = findEvenNumbers([42, -17, 23, -24, 0, 19, 18, -2, 7, 8, -11, 14, 15, 16, -20])
        assert result == [42, -24, 0, 18, -2, 8, 14, 16, -20], f"Test 31 failed: got {result}, expected {[42, -24, 0, 18, -2, 8, 14, 16, -20]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = findEvenNumbers([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])
        assert result == [], f"Test 32 failed: got {result}, expected {[]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = findEvenNumbers([1, 1000000, 3, 1000001, 5, 1000002])
        assert result == [1000000, 1000002], f"Test 33 failed: got {result}, expected {[1000000, 1000002]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = findEvenNumbers([-1, -3, -5, -7, -9])
        assert result == [], f"Test 34 failed: got {result}, expected {[]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = findEvenNumbers([2, -2, 2, -2, 3, -3, 0, 0, 5, -6])
        assert result == [2, -2, 2, -2, 0, 0, -6], f"Test 35 failed: got {result}, expected {[2, -2, 2, -2, 0, 0, -6]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = findEvenNumbers([1, 3, 4, 5, 6])
        assert result == [4, 6], f"Test 36 failed: got {result}, expected {[4, 6]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = findEvenNumbers([1, 2, 3, 4, 5, 7, 0])
        assert result == [2, 4, 0], f"Test 37 failed: got {result}, expected {[2, 4, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = findEvenNumbers([-8, 2, 3, 4, 5, 6, 0, 0, -144])
        assert result == [-8, 2, 4, 6, 0, 0, -144], f"Test 38 failed: got {result}, expected {[-8, 2, 4, 6, 0, 0, -144]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = findEvenNumbers([2, 4, 3, 4, 5, 6, -101, 0])
        assert result == [2, 4, 4, 6, 0], f"Test 39 failed: got {result}, expected {[2, 4, 4, 6, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = findEvenNumbers([1, 2, 3, 4, 5, 6, 0])
        assert result == [2, 4, 6, 0], f"Test 40 failed: got {result}, expected {[2, 4, 6, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = findEvenNumbers([2, 2, 3, 5, 6, -9007199254740991])
        assert result == [2, 2, 6], f"Test 41 failed: got {result}, expected {[2, 2, 6]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = findEvenNumbers([2, 4, 5, 6, 0])
        assert result == [2, 4, 6, 0], f"Test 42 failed: got {result}, expected {[2, 4, 6, 0]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = findEvenNumbers([6, 5, 4, 3, 2])
        assert result == [6, 4, 2], f"Test 43 failed: got {result}, expected {[6, 4, 2]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = findEvenNumbers([9007199254740990, 5, 3, 3, 2])
        assert result == [9007199254740990, 2], f"Test 44 failed: got {result}, expected {[9007199254740990, 2]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = findEvenNumbers([1, 2, 3, 4, 5, 6, 0, 0])
        assert result == [2, 4, 6, 0, 0], f"Test 45 failed: got {result}, expected {[2, 4, 6, 0, 0]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = findEvenNumbers([-21, 14, 6, 5, 4, 3, 2, 1])
        assert result == [14, 6, 4, 2], f"Test 46 failed: got {result}, expected {[14, 6, 4, 2]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = findEvenNumbers([1, 2, 3, 4, 10, 6, 0])
        assert result == [2, 4, 10, 6, 0], f"Test 47 failed: got {result}, expected {[2, 4, 10, 6, 0]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = findEvenNumbers([1, 2, 3, 4, 5, 12, 0])
        assert result == [2, 4, 12, 0], f"Test 48 failed: got {result}, expected {[2, 4, 12, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = findEvenNumbers([0, 0, -9, 6, 5, 8, 3, 2, 1])
        assert result == [0, 0, 6, 8, 2], f"Test 49 failed: got {result}, expected {[0, 0, 6, 8, 2]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = findEvenNumbers([10, 14, 13, 10, 8, 7])
        assert result == [10, 14, 10, 8], f"Test 50 failed: got {result}, expected {[10, 14, 10, 8]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = findEvenNumbers([7, 8, 10, 13, 14, -12])
        assert result == [8, 10, 14, -12], f"Test 51 failed: got {result}, expected {[8, 10, 14, -12]}"
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
