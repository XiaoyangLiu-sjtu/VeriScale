# Coverage Report

Total executable lines: 4
Covered lines: 4
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def UpdateElements(a):
2: ✓     a[4] += 3
3: ✓     a[7] = 516
4: ✓     return a
```

## Complete Test File

```python
def UpdateElements(a):
    a[4] += 3
    a[7] = 516
    return a

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = UpdateElements([0, 1, 2, 3, 4, 5, 6, 7, 8])
        assert result == [0, 1, 2, 3, 7, 5, 6, 516, 8], f"Test 1 failed: got {result}, expected {[0, 1, 2, 3, 7, 5, 6, 516, 8]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = UpdateElements([10, 20, 30, 40, 50, 60, 70, 80])
        assert result == [10, 20, 30, 40, 53, 60, 70, 516], f"Test 2 failed: got {result}, expected {[10, 20, 30, 40, 53, 60, 70, 516]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = UpdateElements([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
        assert result == [-1, -2, -3, -4, -2, -6, -7, 516, -9, -10], f"Test 3 failed: got {result}, expected {[-1, -2, -3, -4, -2, -6, -7, 516, -9, -10]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = UpdateElements([0, 0, 0, 0, 0, 0, 0, 0])
        assert result == [0, 0, 0, 0, 3, 0, 0, 516], f"Test 4 failed: got {result}, expected {[0, 0, 0, 0, 3, 0, 0, 516]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = UpdateElements([5, 5, 5, 5, 5, 5, 5, 5])
        assert result == [5, 5, 5, 5, 8, 5, 5, 516], f"Test 5 failed: got {result}, expected {[5, 5, 5, 5, 8, 5, 5, 516]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = UpdateElements([7, 6, 5, 4, 3, 2, 1, 0])
        assert result == [7, 6, 5, 4, 6, 2, 1, 516], f"Test 6 failed: got {result}, expected {[7, 6, 5, 4, 6, 2, 1, 516]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = UpdateElements([1, 2, 3, 4, 1000000000, 6, 7, 8])
        assert result == [1, 2, 3, 4, 1000000003, 6, 7, 516], f"Test 7 failed: got {result}, expected {[1, 2, 3, 4, 1000000003, 6, 7, 516]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = UpdateElements([0, 0, 0, 0, 0, 0, 0, 0, 0])
        assert result == [0, 0, 0, 0, 3, 0, 0, 516, 0], f"Test 8 failed: got {result}, expected {[0, 0, 0, 0, 3, 0, 0, 516, 0]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = UpdateElements([5, -4, 3, -2, 1, 0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14])
        assert result == [5, -4, 3, -2, 4, 0, -1, 516, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14], f"Test 9 failed: got {result}, expected {[5, -4, 3, -2, 4, 0, -1, 516, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = UpdateElements([10, 19, 30, 81, 50, -2000, 70, 80, 0, 0])
        assert result == [10, 19, 30, 81, 53, -2000, 70, 516, 0, 0], f"Test 10 failed: got {result}, expected {[10, 19, 30, 81, 53, -2000, 70, 516, 0, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = UpdateElements([80, 81, 60, 50, 40, 30, 40, 10, 192021])
        assert result == [80, 81, 60, 50, 43, 30, 40, 516, 192021], f"Test 11 failed: got {result}, expected {[80, 81, 60, 50, 43, 30, 40, 516, 192021]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = UpdateElements([-1, -2, 13, -4, -6, -7, -8, -9, -10, 0])
        assert result == [-1, -2, 13, -4, -3, -7, -8, 516, -10, 0], f"Test 12 failed: got {result}, expected {[-1, -2, 13, -4, -3, -7, -8, 516, -10, 0]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = UpdateElements([0, 0, 0, 0, 0, 0, -789, 0])
        assert result == [0, 0, 0, 0, 3, 0, -789, 516], f"Test 13 failed: got {result}, expected {[0, 0, 0, 0, 3, 0, -789, 516]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = UpdateElements([0, 0, 0, 0, 0, 0, 0, -600])
        assert result == [0, 0, 0, 0, 3, 0, 0, 516], f"Test 14 failed: got {result}, expected {[0, 0, 0, 0, 3, 0, 0, 516]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = UpdateElements([5, 5, 5, 5, 5, 121, 4, 5, 130, 0])
        assert result == [5, 5, 5, 5, 8, 121, 4, 516, 130, 0], f"Test 15 failed: got {result}, expected {[5, 5, 5, 5, 8, 121, 4, 516, 130, 0]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = UpdateElements([5, -400, 5, 5, 5, 5, 5, 5])
        assert result == [5, -400, 5, 5, 8, 5, 5, 516], f"Test 16 failed: got {result}, expected {[5, -400, 5, 5, 8, 5, 5, 516]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = UpdateElements([1, 2, 3, 4, 5, 6, 15, 0, 0])
        assert result == [1, 2, 3, 4, 8, 6, 15, 516, 0], f"Test 17 failed: got {result}, expected {[1, 2, 3, 4, 8, 6, 15, 516, 0]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = UpdateElements([0, 161718, 0, 6, 5, 4, 3, 2, -1])
        assert result == [0, 161718, 0, 6, 8, 4, 3, 516, -1], f"Test 18 failed: got {result}, expected {[0, 161718, 0, 6, 8, 4, 3, 516, -1]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = UpdateElements([0, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0])
        assert result == [0, 0, 0, 0, 3, 0, 0, 516, 0, -5, 0, 0], f"Test 19 failed: got {result}, expected {[0, 0, 0, 0, 3, 0, 0, 516, 0, -5, 0, 0]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = UpdateElements([0, 0, 0, 0, 0, 0, 0, 0, 0, -2000])
        assert result == [0, 0, 0, 0, 3, 0, 0, 516, 0, -2000], f"Test 20 failed: got {result}, expected {[0, 0, 0, 0, 3, 0, 0, 516, 0, -2000]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = UpdateElements([0, 0, 0, 0, 0, 0, 0, 0, 60, 2000])
        assert result == [0, 0, 0, 0, 3, 0, 0, 516, 60, 2000], f"Test 21 failed: got {result}, expected {[0, 0, 0, 0, 3, 0, 0, 516, 60, 2000]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = UpdateElements([0, 1, 2, 3, 4, 5, 7, -6])
        assert result == [0, 1, 2, 3, 7, 5, 7, 516], f"Test 22 failed: got {result}, expected {[0, 1, 2, 3, 7, 5, 7, 516]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = UpdateElements([7, 5, 4, 3, 2, 1, 0, 0, 0])
        assert result == [7, 5, 4, 3, 5, 1, 0, 516, 0], f"Test 23 failed: got {result}, expected {[7, 5, 4, 3, 5, 1, 0, 516, 0]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = UpdateElements([-1, -2, -3, -4, -200, -6, -7, -8])
        assert result == [-1, -2, -3, -4, -197, -6, -7, 516], f"Test 24 failed: got {result}, expected {[-1, -2, -3, -4, -197, -6, -7, 516]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = UpdateElements([-8, -7, -6, 0, -4, -3, -2, -1])
        assert result == [-8, -7, -6, 0, -1, -3, -2, 516], f"Test 25 failed: got {result}, expected {[-8, -7, -6, 0, -1, -3, -2, 516]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = UpdateElements([-1, -2, -3, -4, -5, -6, -7, -8, 0, -161718])
        assert result == [-1, -2, -3, -4, -2, -6, -7, 516, 0, -161718], f"Test 26 failed: got {result}, expected {[-1, -2, -3, -4, -2, -6, -7, 516, 0, -161718]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = UpdateElements([5, 5, 5, 5, 5, 5, 5, 5, 124])
        assert result == [5, 5, 5, 5, 8, 5, 5, 516, 124], f"Test 27 failed: got {result}, expected {[5, 5, 5, 5, 8, 5, 5, 516, 124]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = UpdateElements([5, 5, 5, 5, 5, 5, 5, -1, 60])
        assert result == [5, 5, 5, 5, 8, 5, 5, 516, 60], f"Test 28 failed: got {result}, expected {[5, 5, 5, 5, 8, 5, 5, 516, 60]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = UpdateElements([516, 60, 50, -40, 30, 20, 10, 0])
        assert result == [516, 60, 50, -40, 33, 20, 10, 516], f"Test 29 failed: got {result}, expected {[516, 60, 50, -40, 33, 20, 10, 516]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = UpdateElements([10, 20, 30, 40, 60, 70, 516, 0])
        assert result == [10, 20, 30, 40, 63, 70, 516, 516], f"Test 30 failed: got {result}, expected {[10, 20, 30, 40, 63, 70, 516, 516]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = UpdateElements([0, -40, 8, 7, 6, 1000000000, 4, 3, 17, 1])
        assert result == [0, -40, 8, 7, 9, 1000000000, 4, 516, 17, 1], f"Test 31 failed: got {result}, expected {[0, -40, 8, 7, 9, 1000000000, 4, 516, 17, 1]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = UpdateElements([8, 7, 6, -1000000000, 50, 3, 2, 1])
        assert result == [8, 7, 6, -1000000000, 53, 3, 2, 516], f"Test 32 failed: got {result}, expected {[8, 7, 6, -1000000000, 53, 3, 2, 516]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = UpdateElements([-516, 3, 4, 5, 6, 7, 90, 123])
        assert result == [-516, 3, 4, 5, 9, 7, 90, 516], f"Test 33 failed: got {result}, expected {[-516, 3, 4, 5, 9, 7, 90, 516]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = UpdateElements([2, 3, 5, 7, 11, 13, 19, 0])
        assert result == [2, 3, 5, 7, 14, 13, 19, 516], f"Test 34 failed: got {result}, expected {[2, 3, 5, 7, 14, 13, 19, 516]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = UpdateElements([10, 21, 13, 8, 5, 3, 3, 2, 1])
        assert result == [10, 21, 13, 8, 8, 3, 3, 516, 1], f"Test 35 failed: got {result}, expected {[10, 21, 13, 8, 8, 3, 3, 516, 1]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = UpdateElements([-600, 0, 0, 0, 516, 0, 0, 0])
        assert result == [-600, 0, 0, 0, 519, 0, 0, 516], f"Test 36 failed: got {result}, expected {[-600, 0, 0, 0, 519, 0, 0, 516]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = UpdateElements([8, 7, 6, 5, 4, 3, 2, 1, 0, 0])
        assert result == [8, 7, 6, 5, 7, 3, 2, 516, 0, 0], f"Test 37 failed: got {result}, expected {[8, 7, 6, 5, 7, 3, 2, 516, 0, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = UpdateElements([8, 7, 6, 5, 4, 3, 2, 1, 0, -9, 0])
        assert result == [8, 7, 6, 5, 7, 3, 2, 516, 0, -9, 0], f"Test 38 failed: got {result}, expected {[8, 7, 6, 5, 7, 3, 2, 516, 0, -9, 0]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = UpdateElements([7, 6, 5, 4, 3, 2, 1, 0, 120, 0])
        assert result == [7, 6, 5, 4, 6, 2, 1, 516, 120, 0], f"Test 39 failed: got {result}, expected {[7, 6, 5, 4, 6, 2, 1, 516, 120, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = UpdateElements([8, 7, 5, 4, 2, 1, 0, 300, -2000, 0])
        assert result == [8, 7, 5, 4, 5, 1, 0, 516, -2000, 0], f"Test 40 failed: got {result}, expected {[8, 7, 5, 4, 5, 1, 0, 516, -2000, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = UpdateElements([44, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        assert result == [44, 0, 0, 0, 3, 0, 0, 516, 0, 0], f"Test 41 failed: got {result}, expected {[44, 0, 0, 0, 3, 0, 0, 516, 0, 0]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = UpdateElements([0, 0, 0, 1, 0, 0, 0, 0, 0, -4, -3000])
        assert result == [0, 0, 0, 1, 3, 0, 0, 516, 0, -4, -3000], f"Test 42 failed: got {result}, expected {[0, 0, 0, 1, 3, 0, 0, 516, 0, -4, -3000]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = UpdateElements([0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 192021])
        assert result == [0, 9, 8, 7, 9, 5, 4, 516, 2, 1, 0, 192021], f"Test 43 failed: got {result}, expected {[0, 9, 8, 7, 9, 5, 4, 516, 2, 1, 0, 192021]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = UpdateElements([-456, 0, 161718, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0])
        assert result == [-456, 0, 161718, 9, 11, 7, 6, 516, 4, 3, 2, 1, 0, 0], f"Test 44 failed: got {result}, expected {[-456, 0, 161718, 9, 11, 7, 6, 516, 4, 3, 2, 1, 0, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = UpdateElements([-10, -10, 0, -10, -10, -10, -10, -10, -10])
        assert result == [-10, -10, 0, -10, -7, -10, -10, 516, -10], f"Test 45 failed: got {result}, expected {[-10, -10, 0, -10, -7, -10, -10, 516, -10]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = UpdateElements([3, 2, 4, 1, 0, 9, 2, 5, 3])
        assert result == [3, 2, 4, 1, 3, 9, 2, 516, 3], f"Test 46 failed: got {result}, expected {[3, 2, 4, 1, 3, 9, 2, 516, 3]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = UpdateElements([11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121])
        assert result == [11, 22, 33, 44, 58, 66, 77, 516, 99, 110, 121], f"Test 47 failed: got {result}, expected {[11, 22, 33, 44, 58, 66, 77, 516, 99, 110, 121]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = UpdateElements([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 100])
        assert result == [-6, -5, -4, -3, 1, -1, 0, 516, 2, 3, 4, 5, 100], f"Test 48 failed: got {result}, expected {[-6, -5, -4, -3, 1, -1, 0, 516, 2, 3, 4, 5, 100]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = UpdateElements([123, -123, 456, -456, 789, 101112, -101112, 131415, -131415, 161718, -161718, 192021, 0])
        assert result == [123, -123, 456, -456, 792, 101112, -101112, 516, -131415, 161718, -161718, 192021, 0], f"Test 49 failed: got {result}, expected {[123, -123, 456, -456, 792, 101112, -101112, 516, -131415, 161718, -161718, 192021, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = UpdateElements([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 14])
        assert result == [0, 10, 20, 30, 43, 50, 60, 516, 80, 90, 100, 110, 120, 130, 14], f"Test 50 failed: got {result}, expected {[0, 10, 20, 30, 43, 50, 60, 516, 80, 90, 100, 110, 120, 130, 14]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = UpdateElements([130, 120, 110, 100, 90, 80, 72, 60, 50, 40, 30, 20, 10, 0, 999999, 300])
        assert result == [130, 120, 110, 100, 93, 80, 72, 516, 50, 40, 30, 20, 10, 0, 999999, 300], f"Test 51 failed: got {result}, expected {[130, 120, 110, 100, 93, 80, 72, 516, 50, 40, 30, 20, 10, 0, 999999, 300]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = UpdateElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 12, 13, 14, 15])
        assert result == [0, 1, 2, 3, 7, 5, 6, 516, 8, 9, 10, 2, 12, 13, 14, 15], f"Test 52 failed: got {result}, expected {[0, 1, 2, 3, 7, 5, 6, 516, 8, 9, 10, 2, 12, 13, 14, 15]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = UpdateElements([5, -4, 0, -2, 1, 0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, 0, -4000])
        assert result == [5, -4, 0, -2, 4, 0, -1, 516, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, 0, -4000], f"Test 53 failed: got {result}, expected {[5, -4, 0, -2, 4, 0, -1, 516, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, 0, -4000]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = UpdateElements([5, -4, 3, -2, 1, 0, -1, 2, -3, 4, -5, 6, -7, -9, 10, -11, 12, -13, 14, 6])
        assert result == [5, -4, 3, -2, 4, 0, -1, 516, -3, 4, -5, 6, -7, -9, 10, -11, 12, -13, 14, 6], f"Test 54 failed: got {result}, expected {[5, -4, 3, -2, 4, 0, -1, 516, -3, 4, -5, 6, -7, -9, 10, -11, 12, -13, 14, 6]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
