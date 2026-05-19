# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def kthElement(arr, k):
2: ✓     return arr[k-1]
```

## Complete Test File

```python
def kthElement(arr, k):
    return arr[k-1]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = kthElement([10, 20, 30, 40, 50], 1)
        assert result == 10, f"Test 1 failed: got {result}, expected {10}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = kthElement([10, 20, 30, 40, 50], 3)
        assert result == 30, f"Test 2 failed: got {result}, expected {30}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = kthElement([10, 20, 30, 40, 50], 5)
        assert result == 50, f"Test 3 failed: got {result}, expected {50}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = kthElement([5], 1)
        assert result == 5, f"Test 4 failed: got {result}, expected {5}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = kthElement([1, 2, 3], 3)
        assert result == 3, f"Test 5 failed: got {result}, expected {3}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = kthElement([1, 2, 3], 2)
        assert result == 2, f"Test 6 failed: got {result}, expected {2}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = kthElement([9, 9, 9], 2)
        assert result == 9, f"Test 7 failed: got {result}, expected {9}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = kthElement([0, -1, -2], 1)
        assert result == 0, f"Test 8 failed: got {result}, expected {0}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = kthElement([0, -1, -2], 2)
        assert result == -1, f"Test 9 failed: got {result}, expected {-1}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = kthElement([0, -1, -2], 3)
        assert result == -2, f"Test 10 failed: got {result}, expected {-2}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = kthElement([10, 20, 30, 40], 2)
        assert result == 20, f"Test 11 failed: got {result}, expected {20}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = kthElement([10, 20, 30, 40], 3)
        assert result == 30, f"Test 12 failed: got {result}, expected {30}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = kthElement([9, 8, 7, 6, 5], 4)
        assert result == 6, f"Test 13 failed: got {result}, expected {6}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = kthElement([42, 0, -42, 84, -84, 168], 5)
        assert result == -84, f"Test 14 failed: got {result}, expected {-84}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = kthElement([6, 5, 4, 3, 2, 1], 3)
        assert result == 4, f"Test 15 failed: got {result}, expected {4}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = kthElement([-10, -20, -30, -40], 2)
        assert result == -20, f"Test 16 failed: got {result}, expected {-20}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = kthElement([1, 3, 3, 7, 9, 9, 9, 10], 6)
        assert result == 9, f"Test 17 failed: got {result}, expected {9}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = kthElement([100, 40, 30, 20, 10, 0], 2)
        assert result == 40, f"Test 18 failed: got {result}, expected {40}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = kthElement([66, 50, 40, 30, 20, 10], 3)
        assert result == 40, f"Test 19 failed: got {result}, expected {40}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = kthElement([10, 20, 30, 40, 50], 2)
        assert result == 20, f"Test 20 failed: got {result}, expected {20}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = kthElement([10, 20, 30, 40, 50, 0], 2)
        assert result == 20, f"Test 21 failed: got {result}, expected {20}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = kthElement([50, 40, 30, 20], 3)
        assert result == 30, f"Test 22 failed: got {result}, expected {30}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = kthElement([20, 30, 40, 50], 3)
        assert result == 40, f"Test 23 failed: got {result}, expected {40}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = kthElement([-50, 40, 30, 11], 3)
        assert result == 30, f"Test 24 failed: got {result}, expected {30}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = kthElement([10, 20, 30, 40, 50, 0], 3)
        assert result == 30, f"Test 25 failed: got {result}, expected {30}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = kthElement([10, 20, 30, 40, -2147483648, 0, 32, 0], 3)
        assert result == 30, f"Test 26 failed: got {result}, expected {30}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = kthElement([0, 50, 40, 30, 20, 10], 3)
        assert result == 40, f"Test 27 failed: got {result}, expected {40}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = kthElement([10, 20, 30, 40, 50], 4)
        assert result == 40, f"Test 28 failed: got {result}, expected {40}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = kthElement([0, -1, -2, 0], 3)
        assert result == -2, f"Test 29 failed: got {result}, expected {-2}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = kthElement([0, 0, 2, 1], 3)
        assert result == 2, f"Test 30 failed: got {result}, expected {2}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = kthElement([3, 1, 4, -40], 3)
        assert result == 4, f"Test 31 failed: got {result}, expected {4}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = kthElement([4, 1, 4, 0], 2)
        assert result == 1, f"Test 32 failed: got {result}, expected {1}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = kthElement([10, 20, 30, 40, 0], 2)
        assert result == 20, f"Test 33 failed: got {result}, expected {20}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = kthElement([40, 30, 20, 10], 3)
        assert result == 20, f"Test 34 failed: got {result}, expected {20}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = kthElement([0, -7, 5, 6, 7, 8, 9], 5)
        assert result == 7, f"Test 35 failed: got {result}, expected {7}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = kthElement([0, 5, 6, 7, 8, 9], 5)
        assert result == 8, f"Test 36 failed: got {result}, expected {8}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = kthElement([5, 6, 7, 8, 9], 2)
        assert result == 6, f"Test 37 failed: got {result}, expected {6}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = kthElement([5, 6, 10, 8, 9, -4], 3)
        assert result == 10, f"Test 38 failed: got {result}, expected {10}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = kthElement([100, -100, 200, -200, -300, -300], 2)
        assert result == -100, f"Test 39 failed: got {result}, expected {-100}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = kthElement([100, -100, 200, -200, 300, -299], 2)
        assert result == -100, f"Test 40 failed: got {result}, expected {-100}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = kthElement([100, -100, 200, -200, 300, -300], 5)
        assert result == 300, f"Test 41 failed: got {result}, expected {300}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = kthElement([1, 1, 2, 3, 5, 13, -300], 6)
        assert result == 13, f"Test 42 failed: got {result}, expected {13}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = kthElement([1, 1, 2, 3, 5, 102, -13, 301], 7)
        assert result == -13, f"Test 43 failed: got {result}, expected {-13}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, 0], 7)
        assert result == 13, f"Test 44 failed: got {result}, expected {13}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, 0], 4)
        assert result == 3, f"Test 45 failed: got {result}, expected {3}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = kthElement([1, 1, 2, 3, 8, 13, 6], 5)
        assert result == 8, f"Test 46 failed: got {result}, expected {8}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = kthElement([1, 1, 2, 3, 5, 8, 13, -5], 4)
        assert result == 3, f"Test 47 failed: got {result}, expected {3}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = kthElement([13, 8, 5, 3, 1], 2)
        assert result == 8, f"Test 48 failed: got {result}, expected {8}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = kthElement([1, 1, 2, 3, 5, 8], 4)
        assert result == 3, f"Test 49 failed: got {result}, expected {3}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = kthElement([13, 8, 5, 2, 1, 1, 30], 3)
        assert result == 5, f"Test 50 failed: got {result}, expected {5}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = kthElement([42, 0, -42, 84, -84, 168, -50, 66], 5)
        assert result == -84, f"Test 51 failed: got {result}, expected {-84}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = kthElement([-84, 84, -42, 0, 42, 0, 0], 5)
        assert result == 42, f"Test 52 failed: got {result}, expected {42}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = kthElement([42, 0, -42, 84, -84, 168, 0], 5)
        assert result == -84, f"Test 53 failed: got {result}, expected {-84}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = kthElement([42, 0, -42, 84, -84, 168, 0], 6)
        assert result == 168, f"Test 54 failed: got {result}, expected {168}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = kthElement([2147483647, -2147483648, 0, 50, 0], 4)
        assert result == 50, f"Test 55 failed: got {result}, expected {50}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = kthElement([999999999999, -999999999999, 0, 2147483645], 2)
        assert result == -999999999999, f"Test 56 failed: got {result}, expected {-999999999999}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = kthElement([6, 5, 4, 3, 2, 1, 0], 5)
        assert result == 2, f"Test 57 failed: got {result}, expected {2}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = kthElement([6, 5, 4, 3, 2, 1, 0], 3)
        assert result == 4, f"Test 58 failed: got {result}, expected {4}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = kthElement([6, 5, 4, 3, 2, 1, 169], 3)
        assert result == 4, f"Test 59 failed: got {result}, expected {4}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = kthElement([6, 5, 4, 3, 2, 1, 0], 6)
        assert result == 1, f"Test 60 failed: got {result}, expected {1}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
