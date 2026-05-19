# Coverage Report

Total executable lines: 3
Covered lines: 3
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def missingNumber(nums):
2: ✓     n = len(nums)
3: ✓     return n * (n + 1) // 2 - sum(nums)
```

## Complete Test File

```python
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = missingNumber([3, 0, 1])
        assert result == 2, f"Test 1 failed: got {result}, expected {2}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = missingNumber([0, 1])
        assert result == 2, f"Test 2 failed: got {result}, expected {2}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        assert result == 8, f"Test 3 failed: got {result}, expected {8}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = missingNumber([0])
        assert result == 1, f"Test 4 failed: got {result}, expected {1}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = missingNumber([1])
        assert result == 0, f"Test 5 failed: got {result}, expected {0}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = missingNumber([])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = missingNumber([2, 0])
        assert result == 1, f"Test 7 failed: got {result}, expected {1}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = missingNumber([1, 2])
        assert result == 0, f"Test 8 failed: got {result}, expected {0}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = missingNumber([0, 2])
        assert result == 1, f"Test 9 failed: got {result}, expected {1}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = missingNumber([3, 2, 1])
        assert result == 0, f"Test 10 failed: got {result}, expected {0}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = missingNumber([0, 1, 2])
        assert result == 3, f"Test 11 failed: got {result}, expected {3}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = missingNumber([2, 0, 3])
        assert result == 1, f"Test 12 failed: got {result}, expected {1}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = missingNumber([4, 0, 1, 2])
        assert result == 3, f"Test 13 failed: got {result}, expected {3}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = missingNumber([4, 3, 2, 1])
        assert result == 0, f"Test 14 failed: got {result}, expected {0}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = missingNumber([0, 2, 3, 4])
        assert result == 1, f"Test 15 failed: got {result}, expected {1}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = missingNumber([1, 3, 0, 4])
        assert result == 2, f"Test 16 failed: got {result}, expected {2}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = missingNumber([5, 0, 1, 2, 3])
        assert result == 4, f"Test 17 failed: got {result}, expected {4}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = missingNumber([5, 4, 3, 2, 1])
        assert result == 0, f"Test 18 failed: got {result}, expected {0}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = missingNumber([0, 1, 2, 3, 4])
        assert result == 5, f"Test 19 failed: got {result}, expected {5}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = missingNumber([2, 5, 1, 0, 4])
        assert result == 3, f"Test 20 failed: got {result}, expected {3}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = missingNumber([6, 0, 1, 2, 3, 4])
        assert result == 5, f"Test 21 failed: got {result}, expected {5}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = missingNumber([6, 5, 4, 3, 2, 1])
        assert result == 0, f"Test 22 failed: got {result}, expected {0}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = missingNumber([0, 2, 4, 6, 1, 3])
        assert result == 5, f"Test 23 failed: got {result}, expected {5}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = missingNumber([1, 6, 0, 5, 2, 4])
        assert result == 3, f"Test 24 failed: got {result}, expected {3}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = missingNumber([7, 0, 1, 2, 3, 4, 5])
        assert result == 6, f"Test 25 failed: got {result}, expected {6}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = missingNumber([7, 6, 5, 4, 3, 2, 1])
        assert result == 0, f"Test 26 failed: got {result}, expected {0}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = missingNumber([0, 1, 2, 3, 4, 5, 6])
        assert result == 7, f"Test 27 failed: got {result}, expected {7}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = missingNumber([3, 7, 0, 6, 2, 5, 1])
        assert result == 4, f"Test 28 failed: got {result}, expected {4}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = missingNumber([8, 0, 1, 2, 3, 4, 5, 6])
        assert result == 7, f"Test 29 failed: got {result}, expected {7}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = missingNumber([8, 7, 6, 5, 4, 3, 2, 1])
        assert result == 0, f"Test 30 failed: got {result}, expected {0}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = missingNumber([0, 2, 4, 6, 8, 1, 3, 5])
        assert result == 7, f"Test 31 failed: got {result}, expected {7}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = missingNumber([9, 0, 1, 2, 3, 4, 5, 6, 7])
        assert result == 8, f"Test 32 failed: got {result}, expected {8}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = missingNumber([9, 8, 7, 6, 5, 4, 3, 2, 1])
        assert result == 0, f"Test 33 failed: got {result}, expected {0}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = missingNumber([3, 0, 2])
        assert result == 1, f"Test 34 failed: got {result}, expected {1}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = missingNumber([1, 0])
        assert result == 2, f"Test 35 failed: got {result}, expected {2}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = missingNumber([1, 0, 3])
        assert result == 2, f"Test 36 failed: got {result}, expected {2}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = missingNumber([2, 1])
        assert result == 0, f"Test 37 failed: got {result}, expected {0}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = missingNumber([2, 4, 3, 1, 0])
        assert result == 5, f"Test 38 failed: got {result}, expected {5}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = missingNumber([2, 1, 0])
        assert result == 3, f"Test 39 failed: got {result}, expected {3}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = missingNumber([0, 3, 2, 1])
        assert result == 4, f"Test 40 failed: got {result}, expected {4}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = missingNumber([5, 3, 2, 1, 0])
        assert result == 4, f"Test 41 failed: got {result}, expected {4}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = missingNumber([2, 1, 0, 4])
        assert result == 3, f"Test 42 failed: got {result}, expected {3}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = missingNumber([3, 4, 2, 1, 0])
        assert result == 5, f"Test 43 failed: got {result}, expected {5}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = missingNumber([4, 3, 1, 0])
        assert result == 2, f"Test 44 failed: got {result}, expected {2}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = missingNumber([4, 3, 2, 1, 0])
        assert result == 5, f"Test 45 failed: got {result}, expected {5}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = missingNumber([4, 3, 2, 0])
        assert result == 1, f"Test 46 failed: got {result}, expected {1}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = missingNumber([4, 0, 3, 1])
        assert result == 2, f"Test 47 failed: got {result}, expected {2}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = missingNumber([5, 0, 1, 2, 3, 4])
        assert result == 6, f"Test 48 failed: got {result}, expected {6}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = missingNumber([3, 2, 1, 0, 5])
        assert result == 4, f"Test 49 failed: got {result}, expected {4}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = missingNumber([5, 4, 3, 2, 0])
        assert result == 1, f"Test 50 failed: got {result}, expected {1}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = missingNumber([2, 3, 4, 5, 0])
        assert result == 1, f"Test 51 failed: got {result}, expected {1}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = missingNumber([5, 4, 3, 2, 1, 0])
        assert result == 6, f"Test 52 failed: got {result}, expected {6}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = missingNumber([1, 2, 3, 4, 5])
        assert result == 0, f"Test 53 failed: got {result}, expected {0}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = missingNumber([0, 1, 3, 4])
        assert result == 2, f"Test 54 failed: got {result}, expected {2}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = missingNumber([0, 3, 4, 2])
        assert result == 1, f"Test 55 failed: got {result}, expected {1}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = missingNumber([0, 1, 2, 4])
        assert result == 3, f"Test 56 failed: got {result}, expected {3}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = missingNumber([2, 3, 1, 0])
        assert result == 4, f"Test 57 failed: got {result}, expected {4}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = missingNumber([1, 2, 3, 4, 5, 6])
        assert result == 0, f"Test 58 failed: got {result}, expected {0}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = missingNumber([6, 5, 4, 3, 2, 1, 0])
        assert result == 7, f"Test 59 failed: got {result}, expected {7}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = missingNumber([6, 5, 4, 3, 0, 2])
        assert result == 1, f"Test 60 failed: got {result}, expected {1}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = missingNumber([3, 1, 6, 4, 2, 0])
        assert result == 5, f"Test 61 failed: got {result}, expected {5}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = missingNumber([4, 2, 5, 0, 6, 1])
        assert result == 3, f"Test 62 failed: got {result}, expected {3}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = missingNumber([5, 4, 3, 2, 1, 0, 7])
        assert result == 6, f"Test 63 failed: got {result}, expected {6}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = missingNumber([7, 0, 1, 2, 3, 4, 5, 8])
        assert result == 6, f"Test 64 failed: got {result}, expected {6}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = missingNumber([7, 6, 5, 4, 3, 2, 1, 0])
        assert result == 8, f"Test 65 failed: got {result}, expected {8}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = missingNumber([6, 5, 4, 3, 2, 1, 0, 8])
        assert result == 7, f"Test 66 failed: got {result}, expected {7}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = missingNumber([0, 1, 3, 4, 5, 6])
        assert result == 2, f"Test 67 failed: got {result}, expected {2}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = missingNumber([8, 7, 6, 5, 4, 3, 1, 0])
        assert result == 2, f"Test 68 failed: got {result}, expected {2}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = missingNumber([1, 2, 3, 4, 5, 6, 7, 8])
        assert result == 0, f"Test 69 failed: got {result}, expected {0}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = missingNumber([8, 7, 6, 0, 4, 3, 2, 1])
        assert result == 5, f"Test 70 failed: got {result}, expected {5}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = missingNumber([5, 3, 1, 8, 6, 4, 2, 0])
        assert result == 7, f"Test 71 failed: got {result}, expected {7}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = missingNumber([9, 1, 2, 3, 4, 5, 6, 7, 0])
        assert result == 8, f"Test 72 failed: got {result}, expected {8}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = missingNumber([1, 2, 3, 4, 5, 7, 8, 9, 0])
        assert result == 6, f"Test 73 failed: got {result}, expected {6}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = missingNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        assert result == 10, f"Test 74 failed: got {result}, expected {10}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = missingNumber([9, 7, 5, 4, 3, 2, 1, 0, 10, 8])
        assert result == 6, f"Test 75 failed: got {result}, expected {6}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = missingNumber([0, 1, 4, 2])
        assert result == 3, f"Test 76 failed: got {result}, expected {3}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = missingNumber([3, 4, 1, 0])
        assert result == 2, f"Test 77 failed: got {result}, expected {2}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = missingNumber([1, 3, 4, 0])
        assert result == 2, f"Test 78 failed: got {result}, expected {2}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
