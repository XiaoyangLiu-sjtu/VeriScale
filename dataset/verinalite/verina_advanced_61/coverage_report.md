# Coverage Report

Total executable lines: 10
Covered lines: 10
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def productExceptSelf(nums):
2: ✓     n = len(nums)
3: ✓     output = [1] * n
4: ✓     for i in range(1, n):
5: ✓         output[i] = output[i - 1] * nums[i - 1]
6: ✓     right_product = 1
7: ✓     for i in range(n - 1, -1, -1):
8: ✓         output[i] *= right_product
9: ✓         right_product *= nums[i]
10: ✓     return output
```

## Complete Test File

```python
def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n
    for i in range(1, n):
        output[i] = output[i - 1] * nums[i - 1]
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    return output

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = productExceptSelf([1, 2, 3, 4])
        assert result == [24, 12, 8, 6], f"Test 1 failed: got {result}, expected {[24, 12, 8, 6]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = productExceptSelf([-1, 1, 0, -3, 3])
        assert result == [0, 0, 9, 0, 0], f"Test 2 failed: got {result}, expected {[0, 0, 9, 0, 0]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = productExceptSelf([2, 3])
        assert result == [3, 2], f"Test 3 failed: got {result}, expected {[3, 2]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = productExceptSelf([5, 5, 5, 5])
        assert result == [125, 125, 125, 125], f"Test 4 failed: got {result}, expected {[125, 125, 125, 125]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = productExceptSelf([0, 1, 2])
        assert result == [2, 0, 0], f"Test 5 failed: got {result}, expected {[2, 0, 0]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = productExceptSelf([0])
        assert result == [1], f"Test 6 failed: got {result}, expected {[1]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = productExceptSelf([2, 3, 4])
        assert result == [12, 8, 6], f"Test 7 failed: got {result}, expected {[12, 8, 6]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = productExceptSelf([3, 1, 2, 5, 4])
        assert result == [40, 120, 60, 24, 30], f"Test 8 failed: got {result}, expected {[40, 120, 60, 24, 30]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = productExceptSelf([1, 2, 0])
        assert result == [0, 0, 2], f"Test 9 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = productExceptSelf([4, 3, 4])
        assert result == [12, 16, 12], f"Test 10 failed: got {result}, expected {[12, 16, 12]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = productExceptSelf([-1, 1, 0, 3])
        assert result == [0, 0, -3, 0], f"Test 11 failed: got {result}, expected {[0, 0, -3, 0]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = productExceptSelf([3, 3, 0])
        assert result == [0, 0, 9], f"Test 12 failed: got {result}, expected {[0, 0, 9]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = productExceptSelf([46340, 0])
        assert result == [0, 46340], f"Test 13 failed: got {result}, expected {[0, 46340]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = productExceptSelf([0])
        assert result == [1], f"Test 14 failed: got {result}, expected {[1]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = productExceptSelf([5, 5, 5, 5, 0])
        assert result == [0, 0, 0, 0, 625], f"Test 15 failed: got {result}, expected {[0, 0, 0, 0, 625]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = productExceptSelf([5, 5, 5, 5, 7])
        assert result == [875, 875, 875, 875, 625], f"Test 16 failed: got {result}, expected {[875, 875, 875, 875, 625]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = productExceptSelf([1, 1, 2])
        assert result == [2, 2, 1], f"Test 17 failed: got {result}, expected {[2, 2, 1]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = productExceptSelf([2, 1, 0])
        assert result == [0, 0, 2], f"Test 18 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = productExceptSelf([1, 100, -10, 200])
        assert result == [-200000, -2000, 20000, -1000], f"Test 19 failed: got {result}, expected {[-200000, -2000, 20000, -1000]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = productExceptSelf([1, 2, 0])
        assert result == [0, 0, 2], f"Test 20 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = productExceptSelf([2, 1, 0])
        assert result == [0, 0, 2], f"Test 21 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = productExceptSelf([2, 3, 4, 10, 0])
        assert result == [0, 0, 0, 0, 240], f"Test 22 failed: got {result}, expected {[0, 0, 0, 0, 240]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = productExceptSelf([1, 2, 3, 4, 1, -4, 5])
        assert result == [-480, -240, -160, -120, -480, 120, -96], f"Test 23 failed: got {result}, expected {[-480, -240, -160, -120, -480, 120, -96]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = productExceptSelf([-1, 1, 0, 3])
        assert result == [0, 0, -3, 0], f"Test 24 failed: got {result}, expected {[0, 0, -3, 0]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = productExceptSelf([5, 5, 5, -3])
        assert result == [-75, -75, -75, 125], f"Test 25 failed: got {result}, expected {[-75, -75, -75, 125]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = productExceptSelf([5, 6, 5, 5, 200])
        assert result == [30000, 25000, 30000, 30000, 750], f"Test 26 failed: got {result}, expected {[30000, 25000, 30000, 30000, 750]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = productExceptSelf([5, 5, 5, 5, 0])
        assert result == [0, 0, 0, 0, 625], f"Test 27 failed: got {result}, expected {[0, 0, 0, 0, 625]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = productExceptSelf([0, 2, 200])
        assert result == [400, 0, 0], f"Test 28 failed: got {result}, expected {[400, 0, 0]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = productExceptSelf([3, 3, 0])
        assert result == [0, 0, 9], f"Test 29 failed: got {result}, expected {[0, 0, 9]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = productExceptSelf([2, -3, 300])
        assert result == [-900, 600, -6], f"Test 30 failed: got {result}, expected {[-900, 600, -6]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = productExceptSelf([-1, 2, -3, -46340])
        assert result == [278040, -139020, 92680, 6], f"Test 31 failed: got {result}, expected {[278040, -139020, 92680, 6]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = productExceptSelf([2, -2, 2, -2, 0, 99999])
        assert result == [0, 0, 0, 0, 1599984, 0], f"Test 32 failed: got {result}, expected {[0, 0, 0, 0, 1599984, 0]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = productExceptSelf([4, 10])
        assert result == [10, 4], f"Test 33 failed: got {result}, expected {[10, 4]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = productExceptSelf([10, -10, 9, 0])
        assert result == [0, 0, 0, -900], f"Test 34 failed: got {result}, expected {[0, 0, 0, -900]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = productExceptSelf([3, 1, 2, 5, 3])
        assert result == [30, 90, 45, 18, 30], f"Test 35 failed: got {result}, expected {[30, 90, 45, 18, 30]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = productExceptSelf([1, 1, 1, 1, 0])
        assert result == [0, 0, 0, 0, 1], f"Test 36 failed: got {result}, expected {[0, 0, 0, 0, 1]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = productExceptSelf([300, 200, 11, 99999])
        assert result == [219997800, 329996700, 5999940000, 660000], f"Test 37 failed: got {result}, expected {[219997800, 329996700, 5999940000, 660000]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = productExceptSelf([0, 4, 200])
        assert result == [800, 0, 0], f"Test 38 failed: got {result}, expected {[800, 0, 0]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = productExceptSelf([100, 201, 300])
        assert result == [60300, 30000, 20100], f"Test 39 failed: got {result}, expected {[60300, 30000, 20100]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = productExceptSelf([0, 300, 200, -4])
        assert result == [-240000, 0, 0, 0], f"Test 40 failed: got {result}, expected {[-240000, 0, 0, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = productExceptSelf([46340, 0])
        assert result == [0, 46340], f"Test 41 failed: got {result}, expected {[0, 46340]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = productExceptSelf([-46340, 46340, 1, 0])
        assert result == [0, 0, 0, -2147395600], f"Test 42 failed: got {result}, expected {[0, 0, 0, -2147395600]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = productExceptSelf([2, 0, 3])
        assert result == [0, 6, 0], f"Test 43 failed: got {result}, expected {[0, 6, 0]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = productExceptSelf([0, 4, -1, -1, 8])
        assert result == [32, 0, 0, 0, 0], f"Test 44 failed: got {result}, expected {[32, 0, 0, 0, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = productExceptSelf([11, 13, 17, 19, 36])
        assert result == [151164, 127908, 97812, 87516, 46189], f"Test 45 failed: got {result}, expected {[151164, 127908, 97812, 87516, 46189]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = productExceptSelf([12, -5, 0, -5])
        assert result == [0, 0, 300, 0], f"Test 46 failed: got {result}, expected {[0, 0, 300, 0]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = productExceptSelf([1, -2, 1, -1, 1, -1])
        assert result == [-2, 1, -2, 2, -2, 2], f"Test 47 failed: got {result}, expected {[-2, 1, -2, 2, -2, 2]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = productExceptSelf([1, 1, 2, 2, 4, 4, 0, 1])
        assert result == [0, 0, 0, 0, 0, 0, 64, 0], f"Test 48 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 64, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = productExceptSelf([4, 4, 2, 2, -1, 1, 46341, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, -2965824], f"Test 49 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, -2965824]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = productExceptSelf([0, -300, 50000, 50000])
        assert result == [-750000000000, 0, 0, 0], f"Test 50 failed: got {result}, expected {[-750000000000, 0, 0, 0]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = productExceptSelf([1000000, 1000000, 0, -4294967298])
        assert result == [0, 0, -4294967298000000000000, 0], f"Test 51 failed: got {result}, expected {[0, 0, -4294967298000000000000, 0]}"
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
