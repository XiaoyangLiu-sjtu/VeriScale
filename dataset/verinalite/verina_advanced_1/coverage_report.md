# Coverage Report

Total executable lines: 5
Covered lines: 5
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def FindSingleNumber(nums):
2: ✓     result = 0
3: ✓     for num in nums:
4: ✓         result ^= num
5: ✓     return result
```

## Complete Test File

```python
def FindSingleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = FindSingleNumber([2, 2, 3])
        assert result == 3, f"Test 1 failed: got {result}, expected {3}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = FindSingleNumber([1, 2, 2])
        assert result == 1, f"Test 2 failed: got {result}, expected {1}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = FindSingleNumber([3, 3, 4, 4, 1])
        assert result == 1, f"Test 3 failed: got {result}, expected {1}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = FindSingleNumber([0, 1, 3, 1, 3, 88, 88, 100, 100])
        assert result == 0, f"Test 4 failed: got {result}, expected {0}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = FindSingleNumber([-1, -1, 7, 9, 7])
        assert result == 9, f"Test 5 failed: got {result}, expected {9}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = FindSingleNumber([10, 14, 10, 14, -3])
        assert result == -3, f"Test 6 failed: got {result}, expected {-3}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = FindSingleNumber([-5, 0, -5, 0, 11])
        assert result == 11, f"Test 7 failed: got {result}, expected {11}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = FindSingleNumber([-2, -2, -1, -1, -3])
        assert result == -3, f"Test 8 failed: got {result}, expected {-3}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = FindSingleNumber([42, 17, 42, 17, 99, 99, -100])
        assert result == -100, f"Test 9 failed: got {result}, expected {-100}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = FindSingleNumber([4, 5, 4, 6, 5, 6, 9])
        assert result == 9, f"Test 10 failed: got {result}, expected {9}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = FindSingleNumber([2147483647, -2147483648, 2147483647])
        assert result == -2147483648, f"Test 11 failed: got {result}, expected {-2147483648}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = FindSingleNumber([-2147483648, 7, 7])
        assert result == -2147483648, f"Test 12 failed: got {result}, expected {-2147483648}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = FindSingleNumber([9, 9, 8, 8, 7, 7, 6])
        assert result == 6, f"Test 13 failed: got {result}, expected {6}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = FindSingleNumber([1, 1, 2, 2, 3, 3, 4, 4, -9])
        assert result == -9, f"Test 14 failed: got {result}, expected {-9}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = FindSingleNumber([11, 12, 11, 13, 12, 14, 13, 14, 15])
        assert result == 15, f"Test 15 failed: got {result}, expected {15}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = FindSingleNumber([30, 31, 32, 31, 30, 32, -1])
        assert result == -1, f"Test 16 failed: got {result}, expected {-1}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = FindSingleNumber([-10, -20, -10, -30, -20, -30, 5])
        assert result == 5, f"Test 17 failed: got {result}, expected {5}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = FindSingleNumber([2, 3, 2, 4, 3, 5, 4, 5, 6])
        assert result == 6, f"Test 18 failed: got {result}, expected {6}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = FindSingleNumber([0, 0, -1, -1, -2, -2, -3])
        assert result == -3, f"Test 19 failed: got {result}, expected {-3}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = FindSingleNumber([50, 60, 50, 70, 80, 70, 60, 80, 90])
        assert result == 90, f"Test 20 failed: got {result}, expected {90}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = FindSingleNumber([7, 8, 9, 8, 7, 10, 9, 10, 11])
        assert result == 11, f"Test 21 failed: got {result}, expected {11}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = FindSingleNumber([100, 200, 300, 100, 200, 300, 400])
        assert result == 400, f"Test 22 failed: got {result}, expected {400}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = FindSingleNumber([-7, -8, -7, -9, -8, -9, -10])
        assert result == -10, f"Test 23 failed: got {result}, expected {-10}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = FindSingleNumber([1, 3, 1, 4, 3, 5, 4, 5, 6, 6, 7])
        assert result == 7, f"Test 24 failed: got {result}, expected {7}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = FindSingleNumber([12, 13, 14, 12, 15, 13, 14, 15, 16])
        assert result == 16, f"Test 25 failed: got {result}, expected {16}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = FindSingleNumber([99, 98, 97, 99, 98, 97, 96, 95, 95])
        assert result == 96, f"Test 26 failed: got {result}, expected {96}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = FindSingleNumber([2, 2, 3, 0, 0])
        assert result == 3, f"Test 27 failed: got {result}, expected {3}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = FindSingleNumber([0, 0, 31, 2, 2])
        assert result == 31, f"Test 28 failed: got {result}, expected {31}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = FindSingleNumber([1, 1, 2])
        assert result == 2, f"Test 29 failed: got {result}, expected {2}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = FindSingleNumber([4, 4, 2])
        assert result == 2, f"Test 30 failed: got {result}, expected {2}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = FindSingleNumber([100, 100, 88, 88, 1, 3, 1, 0, 0])
        assert result == 3, f"Test 31 failed: got {result}, expected {3}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = FindSingleNumber([0, 1, 3, 1, 3, 88, 88, 100, 100, 0, -10])
        assert result == -10, f"Test 32 failed: got {result}, expected {-10}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = FindSingleNumber([0, 100, 100, 88, 3, 1, 3, 1, 0])
        assert result == 88, f"Test 33 failed: got {result}, expected {88}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = FindSingleNumber([7, 9, 7, -1, -1])
        assert result == 9, f"Test 34 failed: got {result}, expected {9}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = FindSingleNumber([2, 2, -3])
        assert result == -3, f"Test 35 failed: got {result}, expected {-3}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = FindSingleNumber([3, 3, 2])
        assert result == 2, f"Test 36 failed: got {result}, expected {2}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = FindSingleNumber([0, 0, 11, 3, 3, 2, 2])
        assert result == 11, f"Test 37 failed: got {result}, expected {11}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = FindSingleNumber([2, 2, 3, 3, 60])
        assert result == 60, f"Test 38 failed: got {result}, expected {60}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = FindSingleNumber([200, 2, 2])
        assert result == 200, f"Test 39 failed: got {result}, expected {200}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = FindSingleNumber([0, 1, 3, 1, 88, 88, 100, 100, 0])
        assert result == 3, f"Test 40 failed: got {result}, expected {3}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = FindSingleNumber([100, 100, 0, 88, 3, 1, 3, 1, 0])
        assert result == 88, f"Test 41 failed: got {result}, expected {88}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = FindSingleNumber([-1, -1, 7, 9, 7, 0, 0])
        assert result == 9, f"Test 42 failed: got {result}, expected {9}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = FindSingleNumber([0, 0, -3, -1, -1, -2, -2])
        assert result == -3, f"Test 43 failed: got {result}, expected {-3}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = FindSingleNumber([42, 17, 42, 17, 99, 99, -100, 0, 0])
        assert result == -100, f"Test 44 failed: got {result}, expected {-100}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = FindSingleNumber([11, 12, 11, 13, 12, 14, 13])
        assert result == 14, f"Test 45 failed: got {result}, expected {14}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = FindSingleNumber([2, 3, 2, 4, 6, 4, 6])
        assert result == 3, f"Test 46 failed: got {result}, expected {3}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = FindSingleNumber([-7, -8, -7, -9, -8, -9, -10, 0, 0])
        assert result == -10, f"Test 47 failed: got {result}, expected {-10}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = FindSingleNumber([99, 98, 97, 99, 98, 97, 96, 0, 0])
        assert result == 96, f"Test 48 failed: got {result}, expected {96}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = FindSingleNumber([3, 3, 2])
        assert result == 2, f"Test 49 failed: got {result}, expected {2}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
