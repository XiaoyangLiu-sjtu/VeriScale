# Coverage Report

Total executable lines: 7
Covered lines: 7
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def maxSubarraySum(numbers):
2: ✓     max_sum = 0
3: ✓     current_sum = 0
4: ✓     for number in numbers:
5: ✓         current_sum = max(0, current_sum + number)
6: ✓         max_sum = max(max_sum, current_sum)
7: ✓     return max_sum
```

## Complete Test File

```python
def maxSubarraySum(numbers):
    max_sum = 0
    current_sum = 0
    for number in numbers:
        current_sum = max(0, current_sum + number)
        max_sum = max(max_sum, current_sum)
    return max_sum

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = maxSubarraySum([1, 2, 3, -2, 5])
        assert result == 9, f"Test 1 failed: got {result}, expected {9}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = maxSubarraySum([-2, -3, 4, -1, -2, 1, 5, -3])
        assert result == 7, f"Test 2 failed: got {result}, expected {7}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = maxSubarraySum([-1, -2, -3, -4])
        assert result == 0, f"Test 3 failed: got {result}, expected {0}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = maxSubarraySum([5, -3, 2, 1, -2])
        assert result == 5, f"Test 4 failed: got {result}, expected {5}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = maxSubarraySum([0, 0, 0, 0])
        assert result == 0, f"Test 5 failed: got {result}, expected {0}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = maxSubarraySum([])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = maxSubarraySum([10])
        assert result == 10, f"Test 7 failed: got {result}, expected {10}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = maxSubarraySum([-5, 8, -3, 4, -1])
        assert result == 9, f"Test 8 failed: got {result}, expected {9}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = maxSubarraySum([-1, 1, -1, 1, -1, 1])
        assert result == 1, f"Test 9 failed: got {result}, expected {1}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = maxSubarraySum([-100, 1, 2, 3])
        assert result == 6, f"Test 10 failed: got {result}, expected {6}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = maxSubarraySum([10, 20, -100, 5, 6])
        assert result == 30, f"Test 11 failed: got {result}, expected {30}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = maxSubarraySum([2, -8, 3, -2, 4, -10])
        assert result == 5, f"Test 12 failed: got {result}, expected {5}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = maxSubarraySum([3, -2, 5, -1])
        assert result == 6, f"Test 13 failed: got {result}, expected {6}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = maxSubarraySum([-10, 2, 3, -2, 0, 5, -15, 20, -1])
        assert result == 20, f"Test 14 failed: got {result}, expected {20}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = maxSubarraySum([-1, 5, -2, 3, 2, 2])
        assert result == 10, f"Test 15 failed: got {result}, expected {10}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = maxSubarraySum([1, -2, 6])
        assert result == 6, f"Test 16 failed: got {result}, expected {6}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = maxSubarraySum([0, -3, 5, 1, -2, -1, 4, -3, -2])
        assert result == 7, f"Test 17 failed: got {result}, expected {7}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = maxSubarraySum([-3, 1, -2, -1, 4, -3, -2])
        assert result == 4, f"Test 18 failed: got {result}, expected {4}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = maxSubarraySum([-2, -3, 4, -1, -2, 1, 5, -3, -19, 0, -4])
        assert result == 7, f"Test 19 failed: got {result}, expected {7}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = maxSubarraySum([-2, -3, 4, -1, -2, 1, 4, -3])
        assert result == 6, f"Test 20 failed: got {result}, expected {6}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = maxSubarraySum([-2, -3, 4, -1, -2, 1, 5, -3, 0, 9])
        assert result == 13, f"Test 21 failed: got {result}, expected {13}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = maxSubarraySum([-3, 5, 1, -2, -1, 4, -3, -1])
        assert result == 7, f"Test 22 failed: got {result}, expected {7}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = maxSubarraySum([-2, 9, -2, 1, 2, -3, 5])
        assert result == 12, f"Test 23 failed: got {result}, expected {12}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = maxSubarraySum([-1, -4, -3, 1000000000000, -5])
        assert result == 1000000000000, f"Test 24 failed: got {result}, expected {1000000000000}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = maxSubarraySum([-5, 8, -3, 4, -1, 1000000000000, 0, -15, -100, -6])
        assert result == 1000000000008, f"Test 25 failed: got {result}, expected {1000000000008}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = maxSubarraySum([0, 0, -5, 8, -3, 8, -1])
        assert result == 13, f"Test 26 failed: got {result}, expected {13}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = maxSubarraySum([-6, -2, 4, -3, 8, -5])
        assert result == 9, f"Test 27 failed: got {result}, expected {9}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = maxSubarraySum([0, 10, 0, 0, -5])
        assert result == 10, f"Test 28 failed: got {result}, expected {10}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = maxSubarraySum([-100, 2, 3, 4, -13])
        assert result == 9, f"Test 29 failed: got {result}, expected {9}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = maxSubarraySum([1, -1, 1, -1, 1, -1, 8, 0, -7, 0])
        assert result == 8, f"Test 30 failed: got {result}, expected {8}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = maxSubarraySum([10, -100, 5, 6, 0, 4, -10])
        assert result == 15, f"Test 31 failed: got {result}, expected {15}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = maxSubarraySum([-1, 1000000000000, 0, 1000000000000])
        assert result == 2000000000000, f"Test 32 failed: got {result}, expected {2000000000000}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = maxSubarraySum([2, 3, -2, 4, -10])
        assert result == 7, f"Test 33 failed: got {result}, expected {7}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = maxSubarraySum([2, -8, 3, 2, 4, -10, 999999999998, 0, -6])
        assert result == 999999999998, f"Test 34 failed: got {result}, expected {999999999998}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = maxSubarraySum([-100, -10, 4, -2, 3, -8, 2])
        assert result == 5, f"Test 35 failed: got {result}, expected {5}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = maxSubarraySum([2, -8, -1, -2, 4, -10])
        assert result == 4, f"Test 36 failed: got {result}, expected {4}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = maxSubarraySum([4, -3, 1, 2, -1, 4, 3, 1, -2])
        assert result == 11, f"Test 37 failed: got {result}, expected {11}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = maxSubarraySum([4, 8, 1, 2, -1, 4, -3, 1, -2, -6])
        assert result == 18, f"Test 38 failed: got {result}, expected {18}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = maxSubarraySum([-5, 1, 2, -1, -10, -3, 1, -2, 1, 0])
        assert result == 3, f"Test 39 failed: got {result}, expected {3}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = maxSubarraySum([20, -4, 999999999998, -19, 8])
        assert result == 1000000000014, f"Test 40 failed: got {result}, expected {1000000000014}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = maxSubarraySum([3, -2, 5, -1, 6, 0])
        assert result == 11, f"Test 41 failed: got {result}, expected {11}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = maxSubarraySum([-12, 5, -2, 3, 0])
        assert result == 6, f"Test 42 failed: got {result}, expected {6}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = maxSubarraySum([-3, 4, -1, 2, 1, -5, 4, 0])
        assert result == 6, f"Test 43 failed: got {result}, expected {6}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = maxSubarraySum([0, -5, 2, -3, 0, -1, 2, 1000000000000])
        assert result == 1000000000002, f"Test 44 failed: got {result}, expected {1000000000002}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = maxSubarraySum([4, -1, 2, 1, 0, 9, -7])
        assert result == 15, f"Test 45 failed: got {result}, expected {15}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = maxSubarraySum([-4, -1, 2, -7, -1, -100])
        assert result == 2, f"Test 46 failed: got {result}, expected {2}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = maxSubarraySum([-7, -5, 7, -999999999998])
        assert result == 7, f"Test 47 failed: got {result}, expected {7}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = maxSubarraySum([1, 0, 0, -3, 4, 0, -6, 999999999998, 0])
        assert result == 999999999998, f"Test 48 failed: got {result}, expected {999999999998}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = maxSubarraySum([1, 0, 2, 0, -3, 0, 4, 0, -12, -19])
        assert result == 4, f"Test 49 failed: got {result}, expected {4}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = maxSubarraySum([0, -12, 0, -3, 0, 2, 0, 1, 1, 13, 10])
        assert result == 27, f"Test 50 failed: got {result}, expected {27}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = maxSubarraySum([-1, -2, -1, -1, -1, 999999999998])
        assert result == 999999999998, f"Test 51 failed: got {result}, expected {999999999998}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = maxSubarraySum([-1, 7, -1, -1, 0])
        assert result == 7, f"Test 52 failed: got {result}, expected {7}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = maxSubarraySum([10, 1, 3, -1, 2, -3, 4, 0, 999999999999, -13])
        assert result == 1000000000015, f"Test 53 failed: got {result}, expected {1000000000015}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = maxSubarraySum([-1, 20, -15, 5, 0, -2, 2, -10, 101, -15])
        assert result == 101, f"Test 54 failed: got {result}, expected {101}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = maxSubarraySum([-24, 2, 3, -2, 0, 5, -15, 20, -1, 8])
        assert result == 27, f"Test 55 failed: got {result}, expected {27}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = maxSubarraySum([1, -2, 3, 10, -6, 7, 2, -5, -13])
        assert result == 16, f"Test 56 failed: got {result}, expected {16}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = maxSubarraySum([-5, -11, 7, 10, 3, -2, 1, -3, 0])
        assert result == 20, f"Test 57 failed: got {result}, expected {20}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
