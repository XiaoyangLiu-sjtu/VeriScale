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
        result = productExceptSelf([1])
        assert result == [1], f"Test 6 failed: got {result}, expected {[1]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = productExceptSelf([0])
        assert result == [1], f"Test 7 failed: got {result}, expected {[1]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = productExceptSelf([1, 2])
        assert result == [2, 1], f"Test 8 failed: got {result}, expected {[2, 1]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = productExceptSelf([2, 3, 4])
        assert result == [12, 8, 6], f"Test 9 failed: got {result}, expected {[12, 8, 6]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = productExceptSelf([0, 0, 1, 2])
        assert result == [0, 0, 0, 0], f"Test 10 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = productExceptSelf([0, 0, 0])
        assert result == [0, 0, 0], f"Test 11 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = productExceptSelf([-1, -2, -3, -4])
        assert result == [-24, -12, -8, -6], f"Test 12 failed: got {result}, expected {[-24, -12, -8, -6]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = productExceptSelf([-1, 2, -3, 4])
        assert result == [-24, 12, -8, 6], f"Test 13 failed: got {result}, expected {[-24, 12, -8, 6]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = productExceptSelf([2, -2, 2, -2])
        assert result == [8, -8, 8, -8], f"Test 14 failed: got {result}, expected {[8, -8, 8, -8]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = productExceptSelf([10, -10])
        assert result == [-10, 10], f"Test 15 failed: got {result}, expected {[-10, 10]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = productExceptSelf([3, 1, 2, 5, 4])
        assert result == [40, 120, 60, 24, 30], f"Test 16 failed: got {result}, expected {[40, 120, 60, 24, 30]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = productExceptSelf([1, 1, 1, 1, 1])
        assert result == [1, 1, 1, 1, 1], f"Test 17 failed: got {result}, expected {[1, 1, 1, 1, 1]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = productExceptSelf([9])
        assert result == [1], f"Test 18 failed: got {result}, expected {[1]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = productExceptSelf([7, 8])
        assert result == [8, 7], f"Test 19 failed: got {result}, expected {[8, 7]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = productExceptSelf([100, 200, 300])
        assert result == [60000, 30000, 20000], f"Test 20 failed: got {result}, expected {[60000, 30000, 20000]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = productExceptSelf([46340, 46340])
        assert result == [46340, 46340], f"Test 21 failed: got {result}, expected {[46340, 46340]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = productExceptSelf([-46340, 46340, 1])
        assert result == [46340, -46340, -2147395600], f"Test 22 failed: got {result}, expected {[46340, -46340, -2147395600]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = productExceptSelf([2, 0, 0, 4, 5])
        assert result == [0, 0, 0, 0, 0], f"Test 23 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = productExceptSelf([6, 3, 0, 2])
        assert result == [0, 0, 36, 0], f"Test 24 failed: got {result}, expected {[0, 0, 36, 0]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = productExceptSelf([8, -1, 0, -2, 4])
        assert result == [0, 0, 64, 0, 0], f"Test 25 failed: got {result}, expected {[0, 0, 64, 0, 0]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = productExceptSelf([11, 13, 17, 19])
        assert result == [4199, 3553, 2717, 2431], f"Test 26 failed: got {result}, expected {[4199, 3553, 2717, 2431]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = productExceptSelf([-5, -5, -5])
        assert result == [25, 25, 25], f"Test 27 failed: got {result}, expected {[25, 25, 25]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = productExceptSelf([1, -1, 1, -1, 1, -1])
        assert result == [-1, 1, -1, 1, -1, 1], f"Test 28 failed: got {result}, expected {[-1, 1, -1, 1, -1, 1]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = productExceptSelf([4, 4, 2, 2, 1, 1])
        assert result == [16, 16, 32, 32, 64, 64], f"Test 29 failed: got {result}, expected {[16, 16, 32, 32, 64, 64]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = productExceptSelf([12, 0, -12])
        assert result == [0, -144, 0], f"Test 30 failed: got {result}, expected {[0, -144, 0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = productExceptSelf([2147483647, 1, -1])
        assert result == [-1, -2147483647, 2147483647], f"Test 31 failed: got {result}, expected {[-1, -2147483647, 2147483647]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = productExceptSelf([-2147483648, 1])
        assert result == [1, -2147483648], f"Test 32 failed: got {result}, expected {[1, -2147483648]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = productExceptSelf([50000, 50000, 50000])
        assert result == [2500000000, 2500000000, 2500000000], f"Test 33 failed: got {result}, expected {[2500000000, 2500000000, 2500000000]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = productExceptSelf([100000, 100000, 100000, 100000])
        assert result == [1000000000000000, 1000000000000000, 1000000000000000, 1000000000000000], f"Test 34 failed: got {result}, expected {[1000000000000000, 1000000000000000, 1000000000000000, 1000000000000000]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = productExceptSelf([2147483647, 2, 2])
        assert result == [4, 4294967294, 4294967294], f"Test 35 failed: got {result}, expected {[4, 4294967294, 4294967294]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = productExceptSelf([-2147483648, -1, 1])
        assert result == [-1, -2147483648, 2147483648], f"Test 36 failed: got {result}, expected {[-1, -2147483648, 2147483648]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = productExceptSelf([3037000500, 3037000500])
        assert result == [3037000500, 3037000500], f"Test 37 failed: got {result}, expected {[3037000500, 3037000500]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = productExceptSelf([99999, -99999, 99999, -99999])
        assert result == [999970000299999, -999970000299999, 999970000299999, -999970000299999], f"Test 38 failed: got {result}, expected {[999970000299999, -999970000299999, 999970000299999, -999970000299999]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = productExceptSelf([1000000, 0, 1000000, 1000000])
        assert result == [0, 1000000000000000000, 0, 0], f"Test 39 failed: got {result}, expected {[0, 1000000000000000000, 0, 0]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = productExceptSelf([2147483647, 2147483647, 2147483647])
        assert result == [4611686014132420609, 4611686014132420609, 4611686014132420609], f"Test 40 failed: got {result}, expected {[4611686014132420609, 4611686014132420609, 4611686014132420609]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = productExceptSelf([1, 3, 4])
        assert result == [12, 4, 3], f"Test 41 failed: got {result}, expected {[12, 4, 3]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = productExceptSelf([-1, 2, 3, 4, 12])
        assert result == [288, -144, -96, -72, -24], f"Test 42 failed: got {result}, expected {[288, -144, -96, -72, -24]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = productExceptSelf([1, 2, 4, 0, 0, -13])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 43 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = productExceptSelf([4, 3, 2])
        assert result == [6, 8, 12], f"Test 44 failed: got {result}, expected {[6, 8, 12]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = productExceptSelf([1, 2, 4])
        assert result == [8, 4, 2], f"Test 45 failed: got {result}, expected {[8, 4, 2]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = productExceptSelf([1, 2, 3, 4, 0])
        assert result == [0, 0, 0, 0, 24], f"Test 46 failed: got {result}, expected {[0, 0, 0, 0, 24]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = productExceptSelf([1, 2, 4, 4])
        assert result == [32, 16, 8, 8], f"Test 47 failed: got {result}, expected {[32, 16, 8, 8]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = productExceptSelf([2, 2, 3, 46340])
        assert result == [278040, 278040, 185360, 12], f"Test 48 failed: got {result}, expected {[278040, 278040, 185360, 12]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = productExceptSelf([1, 2, 0])
        assert result == [0, 0, 2], f"Test 49 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = productExceptSelf([4, 3, 4])
        assert result == [12, 16, 12], f"Test 50 failed: got {result}, expected {[12, 16, 12]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = productExceptSelf([-1, 4, 3, 2, 1])
        assert result == [24, -6, -8, -12, -24], f"Test 51 failed: got {result}, expected {[24, -6, -8, -12, -24]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = productExceptSelf([1, 2, 3, 4, -2147483648, 0])
        assert result == [0, 0, 0, 0, 0, -51539607552], f"Test 52 failed: got {result}, expected {[0, 0, 0, 0, 0, -51539607552]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = productExceptSelf([0, 4, 3, -1])
        assert result == [-12, 0, 0, 0], f"Test 53 failed: got {result}, expected {[-12, 0, 0, 0]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = productExceptSelf([4, 3, 2, 1, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 54 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = productExceptSelf([3, 2])
        assert result == [2, 3], f"Test 55 failed: got {result}, expected {[2, 3]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = productExceptSelf([-1, 1, 0, -3, -46340])
        assert result == [0, 0, -139020, 0, 0], f"Test 56 failed: got {result}, expected {[0, 0, -139020, 0, 0]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = productExceptSelf([0, 3, -3, 0, 1, -1])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 57 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = productExceptSelf([-1, 1, -3, 3])
        assert result == [-9, 9, -3, 3], f"Test 58 failed: got {result}, expected {[-9, 9, -3, 3]}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = productExceptSelf([-1, 1, 0, -3, 3, 2147483649])
        assert result == [0, 0, 19327352841, 0, 0, 0], f"Test 59 failed: got {result}, expected {[0, 0, 19327352841, 0, 0, 0]}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = productExceptSelf([3, -3, 0, 1])
        assert result == [0, 0, -9, 0], f"Test 60 failed: got {result}, expected {[0, 0, -9, 0]}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = productExceptSelf([-4, 300, 0, 1, -1, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 61 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = productExceptSelf([0, 3, -3, -2147483648, 1, -2, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 62 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = productExceptSelf([-1, 1, 0, -3, 3, -12, 46340])
        assert result == [0, 0, -5004720, 0, 0, 0, 0], f"Test 63 failed: got {result}, expected {[0, 0, -5004720, 0, 0, 0, 0]}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = productExceptSelf([-1, 1, 0, 3])
        assert result == [0, 0, -3, 0], f"Test 64 failed: got {result}, expected {[0, 0, -3, 0]}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = productExceptSelf([300, 1, 0, -3, 3, 11, 0, -99999])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0], f"Test 65 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = productExceptSelf([3, -3, 0, 2, -1])
        assert result == [0, 0, 18, 0, 0], f"Test 66 failed: got {result}, expected {[0, 0, 18, 0, 0]}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = productExceptSelf([-1, 1, 0, -3, 3, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 67 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = productExceptSelf([-1, 1, 0, -3, 3, 10])
        assert result == [0, 0, 90, 0, 0, 0], f"Test 68 failed: got {result}, expected {[0, 0, 90, 0, 0, 0]}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = productExceptSelf([-46340, 3, -3, 0, 1, -1])
        assert result == [0, 0, 0, -417060, 0, 0], f"Test 69 failed: got {result}, expected {[0, 0, 0, -417060, 0, 0]}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = productExceptSelf([-1, 1, 0, 3, 11, 3])
        assert result == [0, 0, -99, 0, 0, 0], f"Test 70 failed: got {result}, expected {[0, 0, -99, 0, 0, 0]}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = productExceptSelf([3, 0, 6, 0])
        assert result == [0, 0, 0, 0], f"Test 71 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = productExceptSelf([2, 3, 0])
        assert result == [0, 0, 6], f"Test 72 failed: got {result}, expected {[0, 0, 6]}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = productExceptSelf([3, 2, 17, 100000])
        assert result == [3400000, 5100000, 600000, 102], f"Test 73 failed: got {result}, expected {[3400000, 5100000, 600000, 102]}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = productExceptSelf([3, 3, 0])
        assert result == [0, 0, 9], f"Test 74 failed: got {result}, expected {[0, 0, 9]}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = productExceptSelf([46340, 0])
        assert result == [0, 46340], f"Test 75 failed: got {result}, expected {[0, 46340]}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = productExceptSelf([0])
        assert result == [1], f"Test 76 failed: got {result}, expected {[1]}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = productExceptSelf([2, 2, 0])
        assert result == [0, 0, 4], f"Test 77 failed: got {result}, expected {[0, 0, 4]}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = productExceptSelf([2, 10])
        assert result == [10, 2], f"Test 78 failed: got {result}, expected {[10, 2]}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = productExceptSelf([4, 3, 19])
        assert result == [57, 76, 12], f"Test 79 failed: got {result}, expected {[57, 76, 12]}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = productExceptSelf([2])
        assert result == [1], f"Test 80 failed: got {result}, expected {[1]}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = productExceptSelf([3, 200])
        assert result == [200, 3], f"Test 81 failed: got {result}, expected {[200, 3]}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = productExceptSelf([4, 3, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 82 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = productExceptSelf([3, 4])
        assert result == [4, 3], f"Test 83 failed: got {result}, expected {[4, 3]}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = productExceptSelf([5])
        assert result == [1], f"Test 84 failed: got {result}, expected {[1]}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = productExceptSelf([5, 5, 5, 5, 0])
        assert result == [0, 0, 0, 0, 625], f"Test 85 failed: got {result}, expected {[0, 0, 0, 0, 625]}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = productExceptSelf([5, 5, 5, 0, 50000])
        assert result == [0, 0, 0, 6250000, 0], f"Test 86 failed: got {result}, expected {[0, 0, 0, 6250000, 0]}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = productExceptSelf([5, 5, 5, 0])
        assert result == [0, 0, 0, 125], f"Test 87 failed: got {result}, expected {[0, 0, 0, 125]}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = productExceptSelf([5, 5, 5, 5, 0, 5, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 88 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = productExceptSelf([-12, 1, 5, 5, -5, 5, 0])
        assert result == [0, 0, 0, 0, 0, 0, 7500], f"Test 89 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 7500]}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = productExceptSelf([5, 5, 5, 5, 9])
        assert result == [1125, 1125, 1125, 1125, 625], f"Test 90 failed: got {result}, expected {[1125, 1125, 1125, 1125, 625]}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = productExceptSelf([5, 5, 5, 5, 7])
        assert result == [875, 875, 875, 875, 625], f"Test 91 failed: got {result}, expected {[875, 875, 875, 875, 625]}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = productExceptSelf([5, 5, 5, 5, 0, -12])
        assert result == [0, 0, 0, 0, -7500, 0], f"Test 92 failed: got {result}, expected {[0, 0, 0, 0, -7500, 0]}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = productExceptSelf([5, 5, 5, 5, 19])
        assert result == [2375, 2375, 2375, 2375, 625], f"Test 93 failed: got {result}, expected {[2375, 2375, 2375, 2375, 625]}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = productExceptSelf([5, 5, 5, 5, 12])
        assert result == [1500, 1500, 1500, 1500, 625], f"Test 94 failed: got {result}, expected {[1500, 1500, 1500, 1500, 625]}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = productExceptSelf([0, 5, 5, 5, 5, 4])
        assert result == [2500, 0, 0, 0, 0, 0], f"Test 95 failed: got {result}, expected {[2500, 0, 0, 0, 0, 0]}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = productExceptSelf([5, 4, 5, -13, 0])
        assert result == [0, 0, 0, 0, -1300], f"Test 96 failed: got {result}, expected {[0, 0, 0, 0, -1300]}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = productExceptSelf([5, -13])
        assert result == [-13, 5], f"Test 97 failed: got {result}, expected {[-13, 5]}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = productExceptSelf([2, 0, 0])
        assert result == [0, 0, 0], f"Test 98 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = productExceptSelf([1, 1, 2])
        assert result == [2, 2, 1], f"Test 99 failed: got {result}, expected {[2, 2, 1]}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = productExceptSelf([2, 2, 8])
        assert result == [16, 16, 4], f"Test 100 failed: got {result}, expected {[16, 16, 4]}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = productExceptSelf([0, 1, 0])
        assert result == [0, 0, 0], f"Test 101 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = productExceptSelf([1, 2, 1, 0])
        assert result == [0, 0, 0, 2], f"Test 102 failed: got {result}, expected {[0, 0, 0, 2]}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = productExceptSelf([0, 1, 2, -5, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 103 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = productExceptSelf([0, 2])
        assert result == [2, 0], f"Test 104 failed: got {result}, expected {[2, 0]}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = productExceptSelf([2, 0])
        assert result == [0, 2], f"Test 105 failed: got {result}, expected {[0, 2]}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = productExceptSelf([0, 2, -2147483648, 0])
        assert result == [0, 0, 0, 0], f"Test 106 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = productExceptSelf([7])
        assert result == [1], f"Test 107 failed: got {result}, expected {[1]}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = productExceptSelf([0, 13, 199998])
        assert result == [2599974, 0, 0], f"Test 108 failed: got {result}, expected {[2599974, 0, 0]}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = productExceptSelf([0, 1, 2, 0])
        assert result == [0, 0, 0, 0], f"Test 109 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = productExceptSelf([1, -13])
        assert result == [-13, 1], f"Test 110 failed: got {result}, expected {[-13, 1]}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = productExceptSelf([2, 1, 0])
        assert result == [0, 0, 2], f"Test 111 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = productExceptSelf([200, 9, 0])
        assert result == [0, 0, 1800], f"Test 112 failed: got {result}, expected {[0, 0, 1800]}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = productExceptSelf([0, 13])
        assert result == [13, 0], f"Test 113 failed: got {result}, expected {[13, 0]}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = productExceptSelf([-2147483648, 0, 0])
        assert result == [0, 0, 0], f"Test 114 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = productExceptSelf([99999, 0, 0])
        assert result == [0, 0, 0], f"Test 115 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = productExceptSelf([19, 0, 100000])
        assert result == [0, 1900000, 0], f"Test 116 failed: got {result}, expected {[0, 1900000, 0]}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = productExceptSelf([0, 0])
        assert result == [0, 0], f"Test 117 failed: got {result}, expected {[0, 0]}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = productExceptSelf([-3])
        assert result == [1], f"Test 118 failed: got {result}, expected {[1]}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = productExceptSelf([-1, 0])
        assert result == [0, -1], f"Test 119 failed: got {result}, expected {[0, -1]}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = productExceptSelf([3, 0, -12])
        assert result == [0, -36, 0], f"Test 120 failed: got {result}, expected {[0, -36, 0]}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = productExceptSelf([1, 1, 0])
        assert result == [0, 0, 1], f"Test 121 failed: got {result}, expected {[0, 0, 1]}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = productExceptSelf([1, -2147483648, 200])
        assert result == [-429496729600, 200, -2147483648], f"Test 122 failed: got {result}, expected {[-429496729600, 200, -2147483648]}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = productExceptSelf([1, 100, -10, 200])
        assert result == [-200000, -2000, 20000, -1000], f"Test 123 failed: got {result}, expected {[-200000, -2000, 20000, -1000]}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = productExceptSelf([1, 0])
        assert result == [0, 1], f"Test 124 failed: got {result}, expected {[0, 1]}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = productExceptSelf([2, 0, 0, 0, 99999])
        assert result == [0, 0, 0, 0, 0], f"Test 125 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = productExceptSelf([100000])
        assert result == [1], f"Test 126 failed: got {result}, expected {[1]}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = productExceptSelf([1, -2147483648, 0, 6])
        assert result == [0, 0, -12884901888, 0], f"Test 127 failed: got {result}, expected {[0, 0, -12884901888, 0]}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = productExceptSelf([1, 0, 100])
        assert result == [0, 100, 0], f"Test 128 failed: got {result}, expected {[0, 100, 0]}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = productExceptSelf([0, 1, 0])
        assert result == [0, 0, 0], f"Test 129 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = productExceptSelf([0, 0, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 130 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = productExceptSelf([0, 2147483647, 11])
        assert result == [23622320117, 0, 0], f"Test 131 failed: got {result}, expected {[23622320117, 0, 0]}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = productExceptSelf([0, 5])
        assert result == [5, 0], f"Test 132 failed: got {result}, expected {[5, 0]}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = productExceptSelf([0, 8, 0])
        assert result == [0, 0, 0], f"Test 133 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = productExceptSelf([0, 12, 0])
        assert result == [0, 0, 0], f"Test 134 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = productExceptSelf([0, -5])
        assert result == [-5, 0], f"Test 135 failed: got {result}, expected {[-5, 0]}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = productExceptSelf([0, 7])
        assert result == [7, 0], f"Test 136 failed: got {result}, expected {[7, 0]}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = productExceptSelf([0, 8, 2147483647])
        assert result == [17179869176, 0, 0], f"Test 137 failed: got {result}, expected {[17179869176, 0, 0]}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = productExceptSelf([0, 8])
        assert result == [8, 0], f"Test 138 failed: got {result}, expected {[8, 0]}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = productExceptSelf([0, 8, 0, -2, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 139 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = productExceptSelf([-1])
        assert result == [1], f"Test 140 failed: got {result}, expected {[1]}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = productExceptSelf([0, 2])
        assert result == [2, 0], f"Test 141 failed: got {result}, expected {[2, 0]}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = productExceptSelf([2, 200])
        assert result == [200, 2], f"Test 142 failed: got {result}, expected {[200, 2]}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = productExceptSelf([3, 0])
        assert result == [0, 3], f"Test 143 failed: got {result}, expected {[0, 3]}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = productExceptSelf([-26, 0])
        assert result == [0, -26], f"Test 144 failed: got {result}, expected {[0, -26]}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = productExceptSelf([1, 0, -4])
        assert result == [0, -4, 0], f"Test 145 failed: got {result}, expected {[0, -4, 0]}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = productExceptSelf([1, 2, 1, 0])
        assert result == [0, 0, 0, 2], f"Test 146 failed: got {result}, expected {[0, 0, 0, 2]}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = productExceptSelf([2147483647, 0])
        assert result == [0, 2147483647], f"Test 147 failed: got {result}, expected {[0, 2147483647]}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = productExceptSelf([0, 2, 1])
        assert result == [2, 0, 0], f"Test 148 failed: got {result}, expected {[2, 0, 0]}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = productExceptSelf([1, 2, 0])
        assert result == [0, 0, 2], f"Test 149 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = productExceptSelf([2, 1, 0])
        assert result == [0, 0, 2], f"Test 150 failed: got {result}, expected {[0, 0, 2]}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = productExceptSelf([2147483649])
        assert result == [1], f"Test 151 failed: got {result}, expected {[1]}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = productExceptSelf([3, 2, 0])
        assert result == [0, 0, 6], f"Test 152 failed: got {result}, expected {[0, 0, 6]}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = productExceptSelf([5, 3, 4])
        assert result == [12, 20, 15], f"Test 153 failed: got {result}, expected {[12, 20, 15]}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = productExceptSelf([2, 4, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 154 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = productExceptSelf([4])
        assert result == [1], f"Test 155 failed: got {result}, expected {[1]}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = productExceptSelf([2, 3, 4, 0])
        assert result == [0, 0, 0, 24], f"Test 156 failed: got {result}, expected {[0, 0, 0, 24]}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = productExceptSelf([2, 300, 0])
        assert result == [0, 0, 600], f"Test 157 failed: got {result}, expected {[0, 0, 600]}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = productExceptSelf([0, 3, 4])
        assert result == [12, 0, 0], f"Test 158 failed: got {result}, expected {[12, 0, 0]}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = productExceptSelf([1000000, 0])
        assert result == [0, 1000000], f"Test 159 failed: got {result}, expected {[0, 1000000]}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = productExceptSelf([3, -10])
        assert result == [-10, 3], f"Test 160 failed: got {result}, expected {[-10, 3]}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = productExceptSelf([2, 4, 300, 12])
        assert result == [14400, 7200, 96, 2400], f"Test 161 failed: got {result}, expected {[14400, 7200, 96, 2400]}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = productExceptSelf([2, 5])
        assert result == [5, 2], f"Test 162 failed: got {result}, expected {[5, 2]}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = productExceptSelf([2, 3, 4, 10, 0])
        assert result == [0, 0, 0, 0, 240], f"Test 163 failed: got {result}, expected {[0, 0, 0, 0, 240]}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = productExceptSelf([4, 2, 2])
        assert result == [4, 8, 8], f"Test 164 failed: got {result}, expected {[4, 8, 8]}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = productExceptSelf([3, 4])
        assert result == [4, 3], f"Test 165 failed: got {result}, expected {[4, 3]}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = productExceptSelf([2, 3, 4, 0, 11])
        assert result == [0, 0, 0, 264, 0], f"Test 166 failed: got {result}, expected {[0, 0, 0, 264, 0]}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = productExceptSelf([4, 2, -12, -99999, 1000000])
        assert result == [2399976000000, 4799952000000, -799992000000, -96000000, 9599904], f"Test 167 failed: got {result}, expected {[2399976000000, 4799952000000, -799992000000, -96000000, 9599904]}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = productExceptSelf([1, 2, -3, 4])
        assert result == [-24, -12, 8, -6], f"Test 168 failed: got {result}, expected {[-24, -12, 8, -6]}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = productExceptSelf([4, 3, 2, 1])
        assert result == [6, 8, 12, 24], f"Test 169 failed: got {result}, expected {[6, 8, 12, 24]}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = productExceptSelf([9, 3, 2, 1])
        assert result == [6, 18, 27, 54], f"Test 170 failed: got {result}, expected {[6, 18, 27, 54]}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = productExceptSelf([0, 2, 7, 4, 200, 0, 99999])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 171 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = productExceptSelf([1, 2, 3, 4, 1, -4, 5])
        assert result == [-480, -240, -160, -120, -480, 120, -96], f"Test 172 failed: got {result}, expected {[-480, -240, -160, -120, -480, 120, -96]}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = productExceptSelf([3, 2, 2, 46340, 2])
        assert result == [370720, 556080, 556080, 24, 556080], f"Test 173 failed: got {result}, expected {[370720, 556080, 556080, 24, 556080]}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = productExceptSelf([8, 100, 4, 3, 2, 1])
        assert result == [2400, 192, 4800, 6400, 9600, 19200], f"Test 174 failed: got {result}, expected {[2400, 192, 4800, 6400, 9600, 19200]}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = productExceptSelf([1, 2, 3, 4, 2])
        assert result == [48, 24, 16, 12, 24], f"Test 175 failed: got {result}, expected {[48, 24, 16, 12, 24]}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = productExceptSelf([1, 2, 4, 0])
        assert result == [0, 0, 0, 8], f"Test 176 failed: got {result}, expected {[0, 0, 0, 8]}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = productExceptSelf([3, 3, 4])
        assert result == [12, 12, 9], f"Test 177 failed: got {result}, expected {[12, 12, 9]}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = productExceptSelf([1, 2, 3, -2, 0])
        assert result == [0, 0, 0, 0, -12], f"Test 178 failed: got {result}, expected {[0, 0, 0, 0, -12]}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = productExceptSelf([4, 3, 2, 2, -99999])
        assert result == [-1199988, -1599984, -2399976, -2399976, 48], f"Test 179 failed: got {result}, expected {[-1199988, -1599984, -2399976, -2399976, 48]}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = productExceptSelf([0, 1, 0, -3, 3, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 180 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = productExceptSelf([-1, 199998, 0, -3, 3, -2])
        assert result == [0, 0, -3599964, 0, 0, 0], f"Test 181 failed: got {result}, expected {[0, 0, -3599964, 0, 0, 0]}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = productExceptSelf([0, 0, 3, -3, 0, 1, -1])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 182 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = productExceptSelf([3, -3, 0, 1, -1, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 183 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = productExceptSelf([0, 1, -3, 3, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 184 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = productExceptSelf([-1, 1, 0, 3])
        assert result == [0, 0, -3, 0], f"Test 185 failed: got {result}, expected {[0, 0, -3, 0]}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = productExceptSelf([3, 0, 0, 1, -1])
        assert result == [0, 0, 0, 0, 0], f"Test 186 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = productExceptSelf([-1, 1, -1, -3, 3, 0])
        assert result == [0, 0, 0, 0, 0, -9], f"Test 187 failed: got {result}, expected {[0, 0, 0, 0, 0, -9]}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = productExceptSelf([8, 3, -1])
        assert result == [-3, -8, 24], f"Test 188 failed: got {result}, expected {[-3, -8, 24]}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = productExceptSelf([0, 0, 3, -3, -1, 1, -1])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 189 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = productExceptSelf([2147483649, 3, -3, 0, 1, -1, 0, -5, 50000])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 190 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = productExceptSelf([-1, 0, -5, 10, 0, 100000])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 191 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = productExceptSelf([-1, -4, 0, -3, 3, 0, 0, 2147483647, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 192 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = productExceptSelf([-1, 0, 0, 3, 300])
        assert result == [0, 0, 0, 0, 0], f"Test 193 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = productExceptSelf([-5])
        assert result == [1], f"Test 194 failed: got {result}, expected {[1]}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = productExceptSelf([5, 5, 5])
        assert result == [25, 25, 25], f"Test 195 failed: got {result}, expected {[25, 25, 25]}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = productExceptSelf([0, 10, 0, 10, 5, 5, 5, 5])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0], f"Test 196 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = productExceptSelf([-2, 5, 5, 5, 13])
        assert result == [1625, -650, -650, -650, -250], f"Test 197 failed: got {result}, expected {[1625, -650, -650, -650, -250]}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = productExceptSelf([0, 17, 5, -5, 5])
        assert result == [-2125, 0, 0, 0, 0], f"Test 198 failed: got {result}, expected {[-2125, 0, 0, 0, 0]}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = productExceptSelf([5, 5, 5, 6, 0])
        assert result == [0, 0, 0, 0, 750], f"Test 199 failed: got {result}, expected {[0, 0, 0, 0, 750]}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = productExceptSelf([5, 5, 5, 46340, 11])
        assert result == [12743500, 12743500, 12743500, 1375, 5792500], f"Test 200 failed: got {result}, expected {[12743500, 12743500, 12743500, 1375, 5792500]}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = productExceptSelf([300, 5, 5, 5, 0, -2])
        assert result == [0, 0, 0, 0, -75000, 0], f"Test 201 failed: got {result}, expected {[0, 0, 0, 0, -75000, 0]}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = productExceptSelf([5, 5, 5, 5, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 202 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = productExceptSelf([5, 5, 5, -3])
        assert result == [-75, -75, -75, 125], f"Test 203 failed: got {result}, expected {[-75, -75, -75, 125]}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = productExceptSelf([5, 5, 5, -2147483648, 0, 1])
        assert result == [0, 0, 0, 0, -268435456000, 0], f"Test 204 failed: got {result}, expected {[0, 0, 0, 0, -268435456000, 0]}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = productExceptSelf([5, 6, 5, 5, 200])
        assert result == [30000, 25000, 30000, 30000, 750], f"Test 205 failed: got {result}, expected {[30000, 25000, 30000, 30000, 750]}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = productExceptSelf([5, 5, 5, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 206 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = productExceptSelf([5, 5, 5, 19, 100000])
        assert result == [47500000, 47500000, 47500000, 12500000, 2375], f"Test 207 failed: got {result}, expected {[47500000, 47500000, 47500000, 12500000, 2375]}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = productExceptSelf([5, 5, 5, 5, 0])
        assert result == [0, 0, 0, 0, 625], f"Test 208 failed: got {result}, expected {[0, 0, 0, 0, 625]}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = productExceptSelf([2, 1, 0, -1, 0, 46340])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 209 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = productExceptSelf([0, 1, 2, 3, 3, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 210 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = productExceptSelf([0, 2, 200])
        assert result == [400, 0, 0], f"Test 211 failed: got {result}, expected {[400, 0, 0]}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = productExceptSelf([2, 1, 0, 99999])
        assert result == [0, 0, 199998, 0], f"Test 212 failed: got {result}, expected {[0, 0, 199998, 0]}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = productExceptSelf([0, 1])
        assert result == [1, 0], f"Test 213 failed: got {result}, expected {[1, 0]}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = productExceptSelf([0, -12])
        assert result == [-12, 0], f"Test 214 failed: got {result}, expected {[-12, 0]}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = productExceptSelf([0, 0, 2, 0])
        assert result == [0, 0, 0, 0], f"Test 215 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = productExceptSelf([2, -1, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 216 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = productExceptSelf([0, 1, 4, 0, 8, 100])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 217 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = productExceptSelf([2, 1, 0, 0, -2, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 218 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = productExceptSelf([0, -1, 2])
        assert result == [-2, 0, 0], f"Test 219 failed: got {result}, expected {[-2, 0, 0]}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = productExceptSelf([0, 1, 2, 0])
        assert result == [0, 0, 0, 0], f"Test 220 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = productExceptSelf([0, 1, 2, 200, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 221 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = productExceptSelf([0, 0, 1, 200, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 222 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = productExceptSelf([1, 0, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 223 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = productExceptSelf([0, 0, 1, 0, 0, -2147483648])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 224 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = productExceptSelf([0, 0, 1, 2, -2, 13])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 225 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = productExceptSelf([0, 0, 1, 3])
        assert result == [0, 0, 0, 0], f"Test 226 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = productExceptSelf([0, 0, 1, 2, -12, -4])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 227 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = productExceptSelf([0, 100000, 2, 1, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 228 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = productExceptSelf([0, 0, 0, 2, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 229 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = productExceptSelf([2, 1, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 230 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = productExceptSelf([0, 0, 0, 1, 2, 100000])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 231 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = productExceptSelf([3, 3, 0])
        assert result == [0, 0, 9], f"Test 232 failed: got {result}, expected {[0, 0, 9]}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = productExceptSelf([11, 0, 1, 2, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 233 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = productExceptSelf([0, 0, 1, -5])
        assert result == [0, 0, 0, 0], f"Test 234 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = productExceptSelf([0, 1, 1])
        assert result == [1, 0, 0], f"Test 235 failed: got {result}, expected {[1, 0, 0]}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = productExceptSelf([0, 0, 0, 3037000500, -1, -1, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 236 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = productExceptSelf([0, 0, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 237 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = productExceptSelf([1, 0, -2, 0])
        assert result == [0, 0, 0, 0], f"Test 238 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = productExceptSelf([0, 0, 0, 0, 46340, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 239 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = productExceptSelf([0, 0, 2147483647])
        assert result == [0, 0, 0], f"Test 240 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = productExceptSelf([0, 0, 0, 100000])
        assert result == [0, 0, 0, 0], f"Test 241 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = productExceptSelf([10, 0, 0, 13])
        assert result == [0, 0, 0, 0], f"Test 242 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = productExceptSelf([-3, 0, 0])
        assert result == [0, 0, 0], f"Test 243 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = productExceptSelf([0, 0, 0, -4])
        assert result == [0, 0, 0, 0], f"Test 244 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = productExceptSelf([3037000500, 0, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 245 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = productExceptSelf([0, 0, 0, 4, 1000000])
        assert result == [0, 0, 0, 0, 0], f"Test 246 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = productExceptSelf([100000, -2, -4, 5])
        assert result == [40, -2000000, -1000000, 800000], f"Test 247 failed: got {result}, expected {[40, -2000000, -1000000, 800000]}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = productExceptSelf([-5, -3, -2, -1])
        assert result == [-6, -10, -15, -30], f"Test 248 failed: got {result}, expected {[-6, -10, -15, -30]}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = productExceptSelf([-4, -3, -2, -1])
        assert result == [-6, -8, -12, -24], f"Test 249 failed: got {result}, expected {[-6, -8, -12, -24]}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = productExceptSelf([0, 0, -4, -3, -2, -1, 19])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 250 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = productExceptSelf([-1, -2, 0, -4])
        assert result == [0, 0, -8, 0], f"Test 251 failed: got {result}, expected {[0, 0, -8, 0]}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = productExceptSelf([-1, -3, -4])
        assert result == [12, 4, 3], f"Test 252 failed: got {result}, expected {[12, 4, 3]}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = productExceptSelf([100000, -1, -2, -3, -4, 0])
        assert result == [0, 0, 0, 0, 0, 2400000], f"Test 253 failed: got {result}, expected {[0, 0, 0, 0, 0, 2400000]}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = productExceptSelf([-4, -2, -1])
        assert result == [2, 4, 8], f"Test 254 failed: got {result}, expected {[2, 4, 8]}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = productExceptSelf([-4, -2])
        assert result == [-2, -4], f"Test 255 failed: got {result}, expected {[-2, -4]}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = productExceptSelf([-2, -3, -4, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 256 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = productExceptSelf([-1, -2, -3, -4, -99999])
        assert result == [2399976, 1199988, 799992, 599994, 24], f"Test 257 failed: got {result}, expected {[2399976, 1199988, 799992, 599994, 24]}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = productExceptSelf([-4, -2, -1, 100000])
        assert result == [200000, 400000, 800000, -8], f"Test 258 failed: got {result}, expected {[200000, 400000, 800000, -8]}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = productExceptSelf([-1, -2, -3, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 259 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = productExceptSelf([-12, -4, -3, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 260 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = productExceptSelf([2, -3, 2, 0])
        assert result == [0, 0, 0, -12], f"Test 261 failed: got {result}, expected {[0, 0, 0, -12]}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = productExceptSelf([-1, 2, 4, -10])
        assert result == [-80, 40, 20, -8], f"Test 262 failed: got {result}, expected {[-80, 40, 20, -8]}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = productExceptSelf([2, -3, 300])
        assert result == [-900, 600, -6], f"Test 263 failed: got {result}, expected {[-900, 600, -6]}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = productExceptSelf([-1, 2, -3, 4, -10])
        assert result == [240, -120, 80, -60, 24], f"Test 264 failed: got {result}, expected {[240, -120, 80, -60, 24]}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = productExceptSelf([-1, 2, -3, -46340])
        assert result == [278040, -139020, 92680, 6], f"Test 265 failed: got {result}, expected {[278040, -139020, 92680, 6]}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = productExceptSelf([4, 0, 2, -1])
        assert result == [0, -8, 0, 0], f"Test 266 failed: got {result}, expected {[0, -8, 0, 0]}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = productExceptSelf([-1, 4, 2, -1])
        assert result == [-8, 2, 4, -8], f"Test 267 failed: got {result}, expected {[-8, 2, 4, -8]}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = productExceptSelf([4, -3, 2, -1])
        assert result == [6, -8, 12, -24], f"Test 268 failed: got {result}, expected {[6, -8, 12, -24]}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = productExceptSelf([-1, 2, 4, 0, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 269 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = productExceptSelf([-1, 2, -3, 4, 0, 2147483649])
        assert result == [0, 0, 0, 0, 51539607576, 0], f"Test 270 failed: got {result}, expected {[0, 0, 0, 0, 51539607576, 0]}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = productExceptSelf([2, -3, 4])
        assert result == [-12, 8, -6], f"Test 271 failed: got {result}, expected {[-12, 8, -6]}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = productExceptSelf([-12, 4, -3, 2, -1])
        assert result == [24, -72, 96, -144, 288], f"Test 272 failed: got {result}, expected {[24, -72, 96, -144, 288]}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = productExceptSelf([0, 0, 4, -3, 2, -1])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 273 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = productExceptSelf([2, -3, 4, 2147483649, 0])
        assert result == [0, 0, 0, 0, -51539607576], f"Test 274 failed: got {result}, expected {[0, 0, 0, 0, -51539607576]}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = productExceptSelf([1000000, 4, -3, 2, -1])
        assert result == [24, 6000000, -8000000, 12000000, -24000000], f"Test 275 failed: got {result}, expected {[24, 6000000, -8000000, 12000000, -24000000]}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = productExceptSelf([2, -2, 2, -2, 0, 99999])
        assert result == [0, 0, 0, 0, 1599984, 0], f"Test 276 failed: got {result}, expected {[0, 0, 0, 0, 1599984, 0]}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = productExceptSelf([2, -2, 2, -2, -1])
        assert result == [-8, 8, -8, 8, 16], f"Test 277 failed: got {result}, expected {[-8, 8, -8, 8, 16]}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = productExceptSelf([-2, 2, -2, 2, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 278 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = productExceptSelf([2, -2, 2, -2, 0])
        assert result == [0, 0, 0, 0, 16], f"Test 279 failed: got {result}, expected {[0, 0, 0, 0, 16]}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = productExceptSelf([2, -2, 2, -2, 100000])
        assert result == [800000, -800000, 800000, -800000, 16], f"Test 280 failed: got {result}, expected {[800000, -800000, 800000, -800000, 16]}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = productExceptSelf([2, -2, -2])
        assert result == [4, -4, -4], f"Test 281 failed: got {result}, expected {[4, -4, -4]}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = productExceptSelf([2, -3, 2, -2])
        assert result == [12, -8, 12, -12], f"Test 282 failed: got {result}, expected {[12, -8, 12, -12]}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = productExceptSelf([2, -2, 2, -2, 2147483647, 13, 0])
        assert result == [0, 0, 0, 0, 0, 0, 446676598576], f"Test 283 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 446676598576]}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = productExceptSelf([2, -2, -2, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 284 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = productExceptSelf([2, 2, -2, 200, 9])
        assert result == [-7200, -7200, 7200, -72, -1600], f"Test 285 failed: got {result}, expected {[-7200, -7200, 7200, -72, -1600]}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = productExceptSelf([-4, 2, -2, 2, -2])
        assert result == [16, -32, 32, -32, 32], f"Test 286 failed: got {result}, expected {[16, -32, 32, -32, 32]}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = productExceptSelf([1, -3])
        assert result == [-3, 1], f"Test 287 failed: got {result}, expected {[-3, 1]}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = productExceptSelf([50000, 0, -2, 2, -2, 2])
        assert result == [0, 800000, 0, 0, 0, 0], f"Test 288 failed: got {result}, expected {[0, 800000, 0, 0, 0, 0]}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = productExceptSelf([-2, -2, 0])
        assert result == [0, 0, 4], f"Test 289 failed: got {result}, expected {[0, 0, 4]}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = productExceptSelf([-2, 2, -2, 2])
        assert result == [-8, 8, -8, 8], f"Test 290 failed: got {result}, expected {[-8, 8, -8, 8]}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = productExceptSelf([10, -10, -99999])
        assert result == [999990, -999990, -100], f"Test 291 failed: got {result}, expected {[999990, -999990, -100]}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = productExceptSelf([4, 10])
        assert result == [10, 4], f"Test 292 failed: got {result}, expected {[10, 4]}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = productExceptSelf([11, -10, 0])
        assert result == [0, 0, -110], f"Test 293 failed: got {result}, expected {[0, 0, -110]}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = productExceptSelf([9, -20])
        assert result == [-20, 9], f"Test 294 failed: got {result}, expected {[-20, 9]}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = productExceptSelf([10, -10, 9, 0])
        assert result == [0, 0, 0, -900], f"Test 295 failed: got {result}, expected {[0, 0, 0, -900]}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = productExceptSelf([2147483647, 10, -10, 0, 5])
        assert result == [0, 0, 0, -1073741823500, 0], f"Test 296 failed: got {result}, expected {[0, 0, 0, -1073741823500, 0]}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = productExceptSelf([10, 0])
        assert result == [0, 10], f"Test 297 failed: got {result}, expected {[0, 10]}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = productExceptSelf([10, -10, -3, -1])
        assert result == [-30, 30, 100, 300], f"Test 298 failed: got {result}, expected {[-30, 30, 100, 300]}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = productExceptSelf([-11, 10, 0])
        assert result == [0, 0, -110], f"Test 299 failed: got {result}, expected {[0, 0, -110]}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = productExceptSelf([0, -10])
        assert result == [-10, 0], f"Test 300 failed: got {result}, expected {[-10, 0]}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = productExceptSelf([10, 11])
        assert result == [11, 10], f"Test 301 failed: got {result}, expected {[11, 10]}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = productExceptSelf([50000, 0])
        assert result == [0, 50000], f"Test 302 failed: got {result}, expected {[0, 50000]}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = productExceptSelf([-10])
        assert result == [1], f"Test 303 failed: got {result}, expected {[1]}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = productExceptSelf([10, -20, 19])
        assert result == [-380, 190, -200], f"Test 304 failed: got {result}, expected {[-380, 190, -200]}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = productExceptSelf([5, 2, 1, -3, 0, 17])
        assert result == [0, 0, 0, 0, -510, 0], f"Test 305 failed: got {result}, expected {[0, 0, 0, 0, -510, 0]}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = productExceptSelf([3, 1, 2, 5, 4, -13])
        assert result == [-520, -1560, -780, -312, -390, 120], f"Test 306 failed: got {result}, expected {[-520, -1560, -780, -312, -390, 120]}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = productExceptSelf([3, 199998, 2, 5, 4])
        assert result == [7999920, 120, 11999880, 4799952, 5999940], f"Test 307 failed: got {result}, expected {[7999920, 120, 11999880, 4799952, 5999940]}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = productExceptSelf([2147483649, 2, 4, 5, 2, 1])
        assert result == [80, 85899345960, 42949672980, 34359738384, 85899345960, 171798691920], f"Test 308 failed: got {result}, expected {[80, 85899345960, 42949672980, 34359738384, 85899345960, 171798691920]}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = productExceptSelf([3, 1, 2, 5, 3])
        assert result == [30, 90, 45, 18, 30], f"Test 309 failed: got {result}, expected {[30, 90, 45, 18, 30]}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = productExceptSelf([1, 2, -1, 4, 0])
        assert result == [0, 0, 0, 0, -8], f"Test 310 failed: got {result}, expected {[0, 0, 0, 0, -8]}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = productExceptSelf([3, 1, 2, 5, -11])
        assert result == [-110, -330, -165, -66, 30], f"Test 311 failed: got {result}, expected {[-110, -330, -165, -66, 30]}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = productExceptSelf([3, 1, 1000000, -11, 4])
        assert result == [-44000000, -132000000, -132, 12000000, -33000000], f"Test 312 failed: got {result}, expected {[-44000000, -132000000, -132, 12000000, -33000000]}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = productExceptSelf([-12, 2, 5, 2, 1, 3])
        assert result == [60, -360, -144, -360, -720, -240], f"Test 313 failed: got {result}, expected {[60, -360, -144, -360, -720, -240]}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = productExceptSelf([3, 1, 2, 4, 0])
        assert result == [0, 0, 0, 0, 24], f"Test 314 failed: got {result}, expected {[0, 0, 0, 0, 24]}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = productExceptSelf([4, 5, 2, 1, 3])
        assert result == [30, 24, 60, 120, 40], f"Test 315 failed: got {result}, expected {[30, 24, 60, 120, 40]}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = productExceptSelf([4, 5, 1, 3])
        assert result == [15, 12, 60, 20], f"Test 316 failed: got {result}, expected {[15, 12, 60, 20]}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = productExceptSelf([4, 5, 2, 1, 3, 4, -5])
        assert result == [-600, -480, -1200, -2400, -800, -600, 480], f"Test 317 failed: got {result}, expected {[-600, -480, -1200, -2400, -800, -600, 480]}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = productExceptSelf([3, 2, 2, 5, 4])
        assert result == [80, 120, 120, 48, 60], f"Test 318 failed: got {result}, expected {[80, 120, 120, 48, 60]}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = productExceptSelf([100000, 0, 1, 1, 1, 1, 1])
        assert result == [0, 100000, 0, 0, 0, 0, 0], f"Test 319 failed: got {result}, expected {[0, 100000, 0, 0, 0, 0, 0]}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = productExceptSelf([1, 1, 1, 2, 3037000500, 0])
        assert result == [0, 0, 0, 0, 0, 6074001000], f"Test 320 failed: got {result}, expected {[0, 0, 0, 0, 0, 6074001000]}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = productExceptSelf([-1, 1, 1, 8, -1, -46340, 2147483647])
        assert result == [796115137615840, -796115137615840, -796115137615840, -99514392201980, 796115137615840, 17179869176, -370720], f"Test 321 failed: got {result}, expected {[796115137615840, -796115137615840, -796115137615840, -99514392201980, 796115137615840, 17179869176, -370720]}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = productExceptSelf([-1, 1, 1, -100, 1, 1])
        assert result == [-100, 100, 100, -1, 100, 100], f"Test 322 failed: got {result}, expected {[-100, 100, 100, -1, 100, 100]}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = productExceptSelf([19, 1, 1, 1, -1, 1])
        assert result == [-1, -19, -19, -19, 19, -19], f"Test 323 failed: got {result}, expected {[-1, -19, -19, -19, 19, -19]}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = productExceptSelf([8, 1, 1, 1, 1, -2])
        assert result == [-2, -16, -16, -16, -16, 8], f"Test 324 failed: got {result}, expected {[-2, -16, -16, -16, -16, 8]}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = productExceptSelf([0, 1, 1, 1, 1])
        assert result == [1, 0, 0, 0, 0], f"Test 325 failed: got {result}, expected {[1, 0, 0, 0, 0]}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = productExceptSelf([1, 1, 1, 1, 1, 0])
        assert result == [0, 0, 0, 0, 0, 1], f"Test 326 failed: got {result}, expected {[0, 0, 0, 0, 0, 1]}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = productExceptSelf([1, 2, 1, 1, 1, -10])
        assert result == [-20, -10, -20, -20, -20, 2], f"Test 327 failed: got {result}, expected {[-20, -10, -20, -20, -20, 2]}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = productExceptSelf([1, 1, 1, 1, 0])
        assert result == [0, 0, 0, 0, 1], f"Test 328 failed: got {result}, expected {[0, 0, 0, 0, 1]}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = productExceptSelf([12, 1, 1, 1, 1, 1, -26, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, -312], f"Test 329 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, -312]}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = productExceptSelf([1, 1, 1, 2147483649, -1])
        assert result == [-2147483649, -2147483649, -2147483649, -1, 2147483649], f"Test 330 failed: got {result}, expected {[-2147483649, -2147483649, -2147483649, -1, 2147483649]}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = productExceptSelf([1, 1, 0, 1, 1, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 331 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = productExceptSelf([10, 1, 1, 1, 1, -11])
        assert result == [-11, -110, -110, -110, -110, 10], f"Test 332 failed: got {result}, expected {[-11, -110, -110, -110, -110, 10]}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = productExceptSelf([2147483647, 1, 1, 1, 2, -5])
        assert result == [-10, -21474836470, -21474836470, -21474836470, -10737418235, 4294967294], f"Test 333 failed: got {result}, expected {[-10, -21474836470, -21474836470, -21474836470, -10737418235, 4294967294]}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = productExceptSelf([9, 0])
        assert result == [0, 9], f"Test 334 failed: got {result}, expected {[0, 9]}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = productExceptSelf([11, 199998])
        assert result == [199998, 11], f"Test 335 failed: got {result}, expected {[199998, 11]}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = productExceptSelf([0, 3])
        assert result == [3, 0], f"Test 336 failed: got {result}, expected {[3, 0]}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = productExceptSelf([5])
        assert result == [1], f"Test 337 failed: got {result}, expected {[1]}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = productExceptSelf([9, 92680, 10])
        assert result == [926800, 90, 834120], f"Test 338 failed: got {result}, expected {[926800, 90, 834120]}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = productExceptSelf([3037000500])
        assert result == [1], f"Test 339 failed: got {result}, expected {[1]}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = productExceptSelf([9, 17, -1, 0])
        assert result == [0, 0, 0, -153], f"Test 340 failed: got {result}, expected {[0, 0, 0, -153]}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = productExceptSelf([8, 10])
        assert result == [10, 8], f"Test 341 failed: got {result}, expected {[10, 8]}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = productExceptSelf([9, -4])
        assert result == [-4, 9], f"Test 342 failed: got {result}, expected {[-4, 9]}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = productExceptSelf([9, 1])
        assert result == [1, 9], f"Test 343 failed: got {result}, expected {[1, 9]}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = productExceptSelf([9, 9, 0])
        assert result == [0, 0, 81], f"Test 344 failed: got {result}, expected {[0, 0, 81]}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = productExceptSelf([200, 0])
        assert result == [0, 200], f"Test 345 failed: got {result}, expected {[0, 200]}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = productExceptSelf([200, 7, 8])
        assert result == [56, 1600, 1400], f"Test 346 failed: got {result}, expected {[56, 1600, 1400]}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    # Test case 347
    try:
        result = productExceptSelf([-26, 3, -20, 11])
        assert result == [-660, 5720, -858, 1560], f"Test 347 failed: got {result}, expected {[-660, 5720, -858, 1560]}"
        print(f"Test 347 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 347 failed: {e}")
        test_results.append(False)

    # Test case 348
    try:
        result = productExceptSelf([100, 0])
        assert result == [0, 100], f"Test 348 failed: got {result}, expected {[0, 100]}"
        print(f"Test 348 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 348 failed: {e}")
        test_results.append(False)

    # Test case 349
    try:
        result = productExceptSelf([8, 3, 0, -3])
        assert result == [0, 0, -72, 0], f"Test 349 failed: got {result}, expected {[0, 0, -72, 0]}"
        print(f"Test 349 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 349 failed: {e}")
        test_results.append(False)

    # Test case 350
    try:
        result = productExceptSelf([6])
        assert result == [1], f"Test 350 failed: got {result}, expected {[1]}"
        print(f"Test 350 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 350 failed: {e}")
        test_results.append(False)

    # Test case 351
    try:
        result = productExceptSelf([7, 92680])
        assert result == [92680, 7], f"Test 351 failed: got {result}, expected {[92680, 7]}"
        print(f"Test 351 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 351 failed: {e}")
        test_results.append(False)

    # Test case 352
    try:
        result = productExceptSelf([8, 7, 50000, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 352 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 352 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 352 failed: {e}")
        test_results.append(False)

    # Test case 353
    try:
        result = productExceptSelf([7, 8, 0])
        assert result == [0, 0, 56], f"Test 353 failed: got {result}, expected {[0, 0, 56]}"
        print(f"Test 353 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 353 failed: {e}")
        test_results.append(False)

    # Test case 354
    try:
        result = productExceptSelf([7, 0])
        assert result == [0, 7], f"Test 354 failed: got {result}, expected {[0, 7]}"
        print(f"Test 354 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 354 failed: {e}")
        test_results.append(False)

    # Test case 355
    try:
        result = productExceptSelf([7, 8, 36])
        assert result == [288, 252, 56], f"Test 355 failed: got {result}, expected {[288, 252, 56]}"
        print(f"Test 355 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 355 failed: {e}")
        test_results.append(False)

    # Test case 356
    try:
        result = productExceptSelf([7, 7, 0])
        assert result == [0, 0, 49], f"Test 356 failed: got {result}, expected {[0, 0, 49]}"
        print(f"Test 356 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 356 failed: {e}")
        test_results.append(False)

    # Test case 357
    try:
        result = productExceptSelf([8, 0, -3, 92680])
        assert result == [0, -2224320, 0, 0], f"Test 357 failed: got {result}, expected {[0, -2224320, 0, 0]}"
        print(f"Test 357 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 357 failed: {e}")
        test_results.append(False)

    # Test case 358
    try:
        result = productExceptSelf([-5, 7, 0])
        assert result == [0, 0, -35], f"Test 358 failed: got {result}, expected {[0, 0, -35]}"
        print(f"Test 358 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 358 failed: {e}")
        test_results.append(False)

    # Test case 359
    try:
        result = productExceptSelf([100, 200, 300, 0])
        assert result == [0, 0, 0, 6000000], f"Test 359 failed: got {result}, expected {[0, 0, 0, 6000000]}"
        print(f"Test 359 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 359 failed: {e}")
        test_results.append(False)

    # Test case 360
    try:
        result = productExceptSelf([300, 200, 11, 99999])
        assert result == [219997800, 329996700, 5999940000, 660000], f"Test 360 failed: got {result}, expected {[219997800, 329996700, 5999940000, 660000]}"
        print(f"Test 360 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 360 failed: {e}")
        test_results.append(False)

    # Test case 361
    try:
        result = productExceptSelf([300, 200, 100, 99999])
        assert result == [1999980000, 2999970000, 5999940000, 6000000], f"Test 361 failed: got {result}, expected {[1999980000, 2999970000, 5999940000, 6000000]}"
        print(f"Test 361 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 361 failed: {e}")
        test_results.append(False)

    # Test case 362
    try:
        result = productExceptSelf([300, 200, 100])
        assert result == [20000, 30000, 60000], f"Test 362 failed: got {result}, expected {[20000, 30000, 60000]}"
        print(f"Test 362 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 362 failed: {e}")
        test_results.append(False)

    # Test case 363
    try:
        result = productExceptSelf([-12, 300, 200, 100, -1])
        assert result == [-6000000, 240000, 360000, 720000, -72000000], f"Test 363 failed: got {result}, expected {[-6000000, 240000, 360000, 720000, -72000000]}"
        print(f"Test 363 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 363 failed: {e}")
        test_results.append(False)

    # Test case 364
    try:
        result = productExceptSelf([99, 201, 300])
        assert result == [60300, 29700, 19899], f"Test 364 failed: got {result}, expected {[60300, 29700, 19899]}"
        print(f"Test 364 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 364 failed: {e}")
        test_results.append(False)

    # Test case 365
    try:
        result = productExceptSelf([200, -300])
        assert result == [-300, 200], f"Test 365 failed: got {result}, expected {[-300, 200]}"
        print(f"Test 365 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 365 failed: {e}")
        test_results.append(False)

    # Test case 366
    try:
        result = productExceptSelf([0, 4, 200])
        assert result == [800, 0, 0], f"Test 366 failed: got {result}, expected {[800, 0, 0]}"
        print(f"Test 366 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 366 failed: {e}")
        test_results.append(False)

    # Test case 367
    try:
        result = productExceptSelf([100, 200, 300, 3037000500, 12, -2])
        assert result == [-4373280720000000, -2186640360000000, -1457760240000000, -144000000, -36444006000000000, 218664036000000000], f"Test 367 failed: got {result}, expected {[-4373280720000000, -2186640360000000, -1457760240000000, -144000000, -36444006000000000, 218664036000000000]}"
        print(f"Test 367 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 367 failed: {e}")
        test_results.append(False)

    # Test case 368
    try:
        result = productExceptSelf([100, 201, 300])
        assert result == [60300, 30000, 20100], f"Test 368 failed: got {result}, expected {[60300, 30000, 20100]}"
        print(f"Test 368 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 368 failed: {e}")
        test_results.append(False)

    # Test case 369
    try:
        result = productExceptSelf([0, 300, 200, 7])
        assert result == [420000, 0, 0, 0], f"Test 369 failed: got {result}, expected {[420000, 0, 0, 0]}"
        print(f"Test 369 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 369 failed: {e}")
        test_results.append(False)

    # Test case 370
    try:
        result = productExceptSelf([0, 300, 200, -4])
        assert result == [-240000, 0, 0, 0], f"Test 370 failed: got {result}, expected {[-240000, 0, 0, 0]}"
        print(f"Test 370 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 370 failed: {e}")
        test_results.append(False)

    # Test case 371
    try:
        result = productExceptSelf([0, 100, 200, 0])
        assert result == [0, 0, 0, 0], f"Test 371 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 371 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 371 failed: {e}")
        test_results.append(False)

    # Test case 372
    try:
        result = productExceptSelf([46340, 2, 7])
        assert result == [14, 324380, 92680], f"Test 372 failed: got {result}, expected {[14, 324380, 92680]}"
        print(f"Test 372 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 372 failed: {e}")
        test_results.append(False)

    # Test case 373
    try:
        result = productExceptSelf([92680])
        assert result == [1], f"Test 373 failed: got {result}, expected {[1]}"
        print(f"Test 373 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 373 failed: {e}")
        test_results.append(False)

    # Test case 374
    try:
        result = productExceptSelf([46339, 46340])
        assert result == [46340, 46339], f"Test 374 failed: got {result}, expected {[46340, 46339]}"
        print(f"Test 374 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 374 failed: {e}")
        test_results.append(False)

    # Test case 375
    try:
        result = productExceptSelf([-46340])
        assert result == [1], f"Test 375 failed: got {result}, expected {[1]}"
        print(f"Test 375 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 375 failed: {e}")
        test_results.append(False)

    # Test case 376
    try:
        result = productExceptSelf([46340, 46339])
        assert result == [46339, 46340], f"Test 376 failed: got {result}, expected {[46339, 46340]}"
        print(f"Test 376 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 376 failed: {e}")
        test_results.append(False)

    # Test case 377
    try:
        result = productExceptSelf([-13, 0, 46340])
        assert result == [0, -602420, 0], f"Test 377 failed: got {result}, expected {[0, -602420, 0]}"
        print(f"Test 377 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 377 failed: {e}")
        test_results.append(False)

    # Test case 378
    try:
        result = productExceptSelf([46340, 0])
        assert result == [0, 46340], f"Test 378 failed: got {result}, expected {[0, 46340]}"
        print(f"Test 378 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 378 failed: {e}")
        test_results.append(False)

    # Test case 379
    try:
        result = productExceptSelf([4, 0])
        assert result == [0, 4], f"Test 379 failed: got {result}, expected {[0, 4]}"
        print(f"Test 379 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 379 failed: {e}")
        test_results.append(False)

    # Test case 380
    try:
        result = productExceptSelf([5, 46342, 46340])
        assert result == [2147488280, 231700, 231710], f"Test 380 failed: got {result}, expected {[2147488280, 231700, 231710]}"
        print(f"Test 380 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 380 failed: {e}")
        test_results.append(False)

    # Test case 381
    try:
        result = productExceptSelf([46340, 46340, 0])
        assert result == [0, 0, 2147395600], f"Test 381 failed: got {result}, expected {[0, 0, 2147395600]}"
        print(f"Test 381 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 381 failed: {e}")
        test_results.append(False)

    # Test case 382
    try:
        result = productExceptSelf([46340, -13])
        assert result == [-13, 46340], f"Test 382 failed: got {result}, expected {[-13, 46340]}"
        print(f"Test 382 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 382 failed: {e}")
        test_results.append(False)

    # Test case 383
    try:
        result = productExceptSelf([0, 46340, 46340, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 383 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 383 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 383 failed: {e}")
        test_results.append(False)

    # Test case 384
    try:
        result = productExceptSelf([46340, 46340, 0, 0, 46340, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 384 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 384 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 384 failed: {e}")
        test_results.append(False)

    # Test case 385
    try:
        result = productExceptSelf([0, 46340, 46339])
        assert result == [2147349260, 0, 0], f"Test 385 failed: got {result}, expected {[2147349260, 0, 0]}"
        print(f"Test 385 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 385 failed: {e}")
        test_results.append(False)

    # Test case 386
    try:
        result = productExceptSelf([-46340, 46340, 1, 0, 0, 201])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 386 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 386 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 386 failed: {e}")
        test_results.append(False)

    # Test case 387
    try:
        result = productExceptSelf([0, 1, 46341, -11, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 387 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 387 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 387 failed: {e}")
        test_results.append(False)

    # Test case 388
    try:
        result = productExceptSelf([46340, 1])
        assert result == [1, 46340], f"Test 388 failed: got {result}, expected {[1, 46340]}"
        print(f"Test 388 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 388 failed: {e}")
        test_results.append(False)

    # Test case 389
    try:
        result = productExceptSelf([-46340, 46340, 1, -3])
        assert result == [-139020, 139020, 6442186800, -2147395600], f"Test 389 failed: got {result}, expected {[-139020, 139020, 6442186800, -2147395600]}"
        print(f"Test 389 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 389 failed: {e}")
        test_results.append(False)

    # Test case 390
    try:
        result = productExceptSelf([-46340, 46340, 1, 0])
        assert result == [0, 0, 0, -2147395600], f"Test 390 failed: got {result}, expected {[0, 0, 0, -2147395600]}"
        print(f"Test 390 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 390 failed: {e}")
        test_results.append(False)

    # Test case 391
    try:
        result = productExceptSelf([-46340, 46340, -2, -1, 0])
        assert result == [0, 0, 0, 0, -4294791200], f"Test 391 failed: got {result}, expected {[0, 0, 0, 0, -4294791200]}"
        print(f"Test 391 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 391 failed: {e}")
        test_results.append(False)

    # Test case 392
    try:
        result = productExceptSelf([-46340, 46340, 19, -11, 6])
        assert result == [-58110360, 58110360, 141728109600, -244803098400, 448805680400], f"Test 392 failed: got {result}, expected {[-58110360, 58110360, 141728109600, -244803098400, 448805680400]}"
        print(f"Test 392 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 392 failed: {e}")
        test_results.append(False)

    # Test case 393
    try:
        result = productExceptSelf([-46340, 46340, -1, 0, 10])
        assert result == [0, 0, 0, 21473956000, 0], f"Test 393 failed: got {result}, expected {[0, 0, 0, 21473956000, 0]}"
        print(f"Test 393 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 393 failed: {e}")
        test_results.append(False)

    # Test case 394
    try:
        result = productExceptSelf([-46340, 46340])
        assert result == [46340, -46340], f"Test 394 failed: got {result}, expected {[46340, -46340]}"
        print(f"Test 394 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 394 failed: {e}")
        test_results.append(False)

    # Test case 395
    try:
        result = productExceptSelf([1, 46340, -46340])
        assert result == [-2147395600, -46340, 46340], f"Test 395 failed: got {result}, expected {[-2147395600, -46340, 46340]}"
        print(f"Test 395 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 395 failed: {e}")
        test_results.append(False)

    # Test case 396
    try:
        result = productExceptSelf([0, 0, 13, 46340, -46340])
        assert result == [0, 0, 0, 0, 0], f"Test 396 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 396 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 396 failed: {e}")
        test_results.append(False)

    # Test case 397
    try:
        result = productExceptSelf([-46340, 1, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 397 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 397 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 397 failed: {e}")
        test_results.append(False)

    # Test case 398
    try:
        result = productExceptSelf([-46340, 1])
        assert result == [1, -46340], f"Test 398 failed: got {result}, expected {[1, -46340]}"
        print(f"Test 398 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 398 failed: {e}")
        test_results.append(False)

    # Test case 399
    try:
        result = productExceptSelf([0, 46340, -46340])
        assert result == [-2147395600, 0, 0], f"Test 399 failed: got {result}, expected {[-2147395600, 0, 0]}"
        print(f"Test 399 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 399 failed: {e}")
        test_results.append(False)

    # Test case 400
    try:
        result = productExceptSelf([10, 0, 0, 2])
        assert result == [0, 0, 0, 0], f"Test 400 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 400 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 400 failed: {e}")
        test_results.append(False)

    # Test case 401
    try:
        result = productExceptSelf([2, -2, 0, 4, 5])
        assert result == [0, 0, -80, 0, 0], f"Test 401 failed: got {result}, expected {[0, 0, -80, 0, 0]}"
        print(f"Test 401 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 401 failed: {e}")
        test_results.append(False)

    # Test case 402
    try:
        result = productExceptSelf([92680, 0, 4, 5, 1, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 402 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 402 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 402 failed: {e}")
        test_results.append(False)

    # Test case 403
    try:
        result = productExceptSelf([1, 0, 4, 5, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 403 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 403 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 403 failed: {e}")
        test_results.append(False)

    # Test case 404
    try:
        result = productExceptSelf([2, 0, 0, 5])
        assert result == [0, 0, 0, 0], f"Test 404 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 404 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 404 failed: {e}")
        test_results.append(False)

    # Test case 405
    try:
        result = productExceptSelf([2, 0, 0, 4, 5, -4, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 405 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 405 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 405 failed: {e}")
        test_results.append(False)

    # Test case 406
    try:
        result = productExceptSelf([100, 0, 4, 5, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 406 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 406 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 406 failed: {e}")
        test_results.append(False)

    # Test case 407
    try:
        result = productExceptSelf([2, 0, 4, 5, 46339, 6, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 407 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 407 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 407 failed: {e}")
        test_results.append(False)

    # Test case 408
    try:
        result = productExceptSelf([2, 1, 0, 4, 5, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 408 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 408 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 408 failed: {e}")
        test_results.append(False)

    # Test case 409
    try:
        result = productExceptSelf([2, 0, -5, 4, 5])
        assert result == [0, -200, 0, 0, 0], f"Test 409 failed: got {result}, expected {[0, -200, 0, 0, 0]}"
        print(f"Test 409 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 409 failed: {e}")
        test_results.append(False)

    # Test case 410
    try:
        result = productExceptSelf([99999, 0, 46340, 5, 4, 0, 2])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 410 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 410 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 410 failed: {e}")
        test_results.append(False)

    # Test case 411
    try:
        result = productExceptSelf([2, 0, 0, 5, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 411 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 411 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 411 failed: {e}")
        test_results.append(False)

    # Test case 412
    try:
        result = productExceptSelf([5, 4, 0, 2])
        assert result == [0, 0, 40, 0], f"Test 412 failed: got {result}, expected {[0, 0, 40, 0]}"
        print(f"Test 412 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 412 failed: {e}")
        test_results.append(False)

    # Test case 413
    try:
        result = productExceptSelf([2, 0, 0, 4, 5, -11])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 413 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 413 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 413 failed: {e}")
        test_results.append(False)

    # Test case 414
    try:
        result = productExceptSelf([5, 0, 0, 2, -13])
        assert result == [0, 0, 0, 0, 0], f"Test 414 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 414 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 414 failed: {e}")
        test_results.append(False)

    # Test case 415
    try:
        result = productExceptSelf([3, 0, 4, 0, 36])
        assert result == [0, 0, 0, 0, 0], f"Test 415 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 415 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 415 failed: {e}")
        test_results.append(False)

    # Test case 416
    try:
        result = productExceptSelf([46341, 0, 2, 0, 3, 6, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 416 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 416 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 416 failed: {e}")
        test_results.append(False)

    # Test case 417
    try:
        result = productExceptSelf([6, 3, 0, 2, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 417 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 417 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 417 failed: {e}")
        test_results.append(False)

    # Test case 418
    try:
        result = productExceptSelf([2, 0, 3, 6, -99999])
        assert result == [0, -3599964, 0, 0, 0], f"Test 418 failed: got {result}, expected {[0, -3599964, 0, 0, 0]}"
        print(f"Test 418 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 418 failed: {e}")
        test_results.append(False)

    # Test case 419
    try:
        result = productExceptSelf([2147483647, 0, 2])
        assert result == [0, 4294967294, 0], f"Test 419 failed: got {result}, expected {[0, 4294967294, 0]}"
        print(f"Test 419 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 419 failed: {e}")
        test_results.append(False)

    # Test case 420
    try:
        result = productExceptSelf([2, 0, 3, 12])
        assert result == [0, 72, 0, 0], f"Test 420 failed: got {result}, expected {[0, 72, 0, 0]}"
        print(f"Test 420 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 420 failed: {e}")
        test_results.append(False)

    # Test case 421
    try:
        result = productExceptSelf([0, 0, 2, 0, 3, 6, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 421 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 421 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 421 failed: {e}")
        test_results.append(False)

    # Test case 422
    try:
        result = productExceptSelf([0, 0, 0, 3, 6])
        assert result == [0, 0, 0, 0, 0], f"Test 422 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 422 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 422 failed: {e}")
        test_results.append(False)

    # Test case 423
    try:
        result = productExceptSelf([3, 6, 2])
        assert result == [12, 6, 18], f"Test 423 failed: got {result}, expected {[12, 6, 18]}"
        print(f"Test 423 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 423 failed: {e}")
        test_results.append(False)

    # Test case 424
    try:
        result = productExceptSelf([2, 0, 3])
        assert result == [0, 6, 0], f"Test 424 failed: got {result}, expected {[0, 6, 0]}"
        print(f"Test 424 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 424 failed: {e}")
        test_results.append(False)

    # Test case 425
    try:
        result = productExceptSelf([0, 2, 0, 3, 6, 2, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 425 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 425 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 425 failed: {e}")
        test_results.append(False)

    # Test case 426
    try:
        result = productExceptSelf([6, 0, 2, -20, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 426 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 426 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 426 failed: {e}")
        test_results.append(False)

    # Test case 427
    try:
        result = productExceptSelf([0, 2, 0, 3, 6])
        assert result == [0, 0, 0, 0, 0], f"Test 427 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 427 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 427 failed: {e}")
        test_results.append(False)

    # Test case 428
    try:
        result = productExceptSelf([2, 0, 3, 6, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 428 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 428 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 428 failed: {e}")
        test_results.append(False)

    # Test case 429
    try:
        result = productExceptSelf([-5, 2, 0, 3, 6])
        assert result == [0, 0, -180, 0, 0], f"Test 429 failed: got {result}, expected {[0, 0, -180, 0, 0]}"
        print(f"Test 429 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 429 failed: {e}")
        test_results.append(False)

    # Test case 430
    try:
        result = productExceptSelf([8, -1, 0, -2, 4, 300, 46340, 201, 100, -46340])
        assert result == [0, 0, -828722909952000000, 0, 0, 0, 0, 0, 0, 0], f"Test 430 failed: got {result}, expected {[0, 0, -828722909952000000, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 430 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 430 failed: {e}")
        test_results.append(False)

    # Test case 431
    try:
        result = productExceptSelf([4, -1, 0, -1, 8, -46340])
        assert result == [0, 0, -1482880, 0, 0, 0], f"Test 431 failed: got {result}, expected {[0, 0, -1482880, 0, 0, 0]}"
        print(f"Test 431 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 431 failed: {e}")
        test_results.append(False)

    # Test case 432
    try:
        result = productExceptSelf([0, 4, -1, -1, 8])
        assert result == [32, 0, 0, 0, 0], f"Test 432 failed: got {result}, expected {[32, 0, 0, 0, 0]}"
        print(f"Test 432 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 432 failed: {e}")
        test_results.append(False)

    # Test case 433
    try:
        result = productExceptSelf([0, 0, 0, 4, -2, 0, -1, 8])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0], f"Test 433 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 433 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 433 failed: {e}")
        test_results.append(False)

    # Test case 434
    try:
        result = productExceptSelf([4, -1, 0, -1, 8])
        assert result == [0, 0, 32, 0, 0], f"Test 434 failed: got {result}, expected {[0, 0, 32, 0, 0]}"
        print(f"Test 434 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 434 failed: {e}")
        test_results.append(False)

    # Test case 435
    try:
        result = productExceptSelf([8, -1, 0, -2, 4, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0], f"Test 435 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 435 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 435 failed: {e}")
        test_results.append(False)

    # Test case 436
    try:
        result = productExceptSelf([8, -1, -2, 4, 46339, 36])
        assert result == [13345632, -106765056, -53382528, 26691264, 2304, 2965696], f"Test 436 failed: got {result}, expected {[13345632, -106765056, -53382528, 26691264, 2304, 2965696]}"
        print(f"Test 436 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 436 failed: {e}")
        test_results.append(False)

    # Test case 437
    try:
        result = productExceptSelf([4, -5, 0, -1, 8, 300])
        assert result == [0, 0, 48000, 0, 0, 0], f"Test 437 failed: got {result}, expected {[0, 0, 48000, 0, 0, 0]}"
        print(f"Test 437 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 437 failed: {e}")
        test_results.append(False)

    # Test case 438
    try:
        result = productExceptSelf([4, -2, 5, -1, 8, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 438 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 438 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 438 failed: {e}")
        test_results.append(False)

    # Test case 439
    try:
        result = productExceptSelf([4, -2, 0, -1, 8])
        assert result == [0, 0, 64, 0, 0], f"Test 439 failed: got {result}, expected {[0, 0, 64, 0, 0]}"
        print(f"Test 439 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 439 failed: {e}")
        test_results.append(False)

    # Test case 440
    try:
        result = productExceptSelf([8, -1, 0, -2, 4, 0, 2, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0], f"Test 440 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 440 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 440 failed: {e}")
        test_results.append(False)

    # Test case 441
    try:
        result = productExceptSelf([4, 0, -1, 8])
        assert result == [0, -32, 0, 0], f"Test 441 failed: got {result}, expected {[0, -32, 0, 0]}"
        print(f"Test 441 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 441 failed: {e}")
        test_results.append(False)

    # Test case 442
    try:
        result = productExceptSelf([7, -1, -2, 4, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 442 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 442 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 442 failed: {e}")
        test_results.append(False)

    # Test case 443
    try:
        result = productExceptSelf([-1, 0, -2, 4, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 443 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 443 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 443 failed: {e}")
        test_results.append(False)

    # Test case 444
    try:
        result = productExceptSelf([-3, 0, 11, 13, 17, 19, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 444 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 444 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 444 failed: {e}")
        test_results.append(False)

    # Test case 445
    try:
        result = productExceptSelf([11, 13, -20, 19])
        assert result == [-4940, -4180, 2717, -2860], f"Test 445 failed: got {result}, expected {[-4940, -4180, 2717, -2860]}"
        print(f"Test 445 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 445 failed: {e}")
        test_results.append(False)

    # Test case 446
    try:
        result = productExceptSelf([11, 13, 17, 0])
        assert result == [0, 0, 0, 2431], f"Test 446 failed: got {result}, expected {[0, 0, 0, 2431]}"
        print(f"Test 446 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 446 failed: {e}")
        test_results.append(False)

    # Test case 447
    try:
        result = productExceptSelf([0, 34, 11])
        assert result == [374, 0, 0], f"Test 447 failed: got {result}, expected {[374, 0, 0]}"
        print(f"Test 447 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 447 failed: {e}")
        test_results.append(False)

    # Test case 448
    try:
        result = productExceptSelf([-5, 17, 13, 11, -5, -2147483648])
        assert result == [26102663741440, -7677254041600, -10039486054400, -11864847155200, 26102663741440, 60775], f"Test 448 failed: got {result}, expected {[26102663741440, -7677254041600, -10039486054400, -11864847155200, 26102663741440, 60775]}"
        print(f"Test 448 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 448 failed: {e}")
        test_results.append(False)

    # Test case 449
    try:
        result = productExceptSelf([0, 0, -3, 19, 17, 13, 10])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 449 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 449 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 449 failed: {e}")
        test_results.append(False)

    # Test case 450
    try:
        result = productExceptSelf([11, 13, 17, 19, 0])
        assert result == [0, 0, 0, 0, 46189], f"Test 450 failed: got {result}, expected {[0, 0, 0, 0, 46189]}"
        print(f"Test 450 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 450 failed: {e}")
        test_results.append(False)

    # Test case 451
    try:
        result = productExceptSelf([11, 13, 17, 19, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 451 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 451 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 451 failed: {e}")
        test_results.append(False)

    # Test case 452
    try:
        result = productExceptSelf([11, 13, 17, 19, 1000000])
        assert result == [4199000000, 3553000000, 2717000000, 2431000000, 46189], f"Test 452 failed: got {result}, expected {[4199000000, 3553000000, 2717000000, 2431000000, 46189]}"
        print(f"Test 452 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 452 failed: {e}")
        test_results.append(False)

    # Test case 453
    try:
        result = productExceptSelf([11, 13, 17, 19, 36])
        assert result == [151164, 127908, 97812, 87516, 46189], f"Test 453 failed: got {result}, expected {[151164, 127908, 97812, 87516, 46189]}"
        print(f"Test 453 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 453 failed: {e}")
        test_results.append(False)

    # Test case 454
    try:
        result = productExceptSelf([11, 19, 50000, 17, 0])
        assert result == [0, 0, 0, 0, 177650000], f"Test 454 failed: got {result}, expected {[0, 0, 0, 0, 177650000]}"
        print(f"Test 454 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 454 failed: {e}")
        test_results.append(False)

    # Test case 455
    try:
        result = productExceptSelf([3037000500, 17, 13, 11, 0])
        assert result == [0, 0, 0, 0, 7382948215500], f"Test 455 failed: got {result}, expected {[0, 0, 0, 0, 7382948215500]}"
        print(f"Test 455 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 455 failed: {e}")
        test_results.append(False)

    # Test case 456
    try:
        result = productExceptSelf([19, 18, 13, 11])
        assert result == [2574, 2717, 3762, 4446], f"Test 456 failed: got {result}, expected {[2574, 2717, 3762, 4446]}"
        print(f"Test 456 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 456 failed: {e}")
        test_results.append(False)

    # Test case 457
    try:
        result = productExceptSelf([11, 13, 17, 19, 1000000, 300])
        assert result == [1259700000000, 1065900000000, 815100000000, 729300000000, 13856700, 46189000000], f"Test 457 failed: got {result}, expected {[1259700000000, 1065900000000, 815100000000, 729300000000, 13856700, 46189000000]}"
        print(f"Test 457 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 457 failed: {e}")
        test_results.append(False)

    # Test case 458
    try:
        result = productExceptSelf([13, 17, 19, 0])
        assert result == [0, 0, 0, 4199], f"Test 458 failed: got {result}, expected {[0, 0, 0, 4199]}"
        print(f"Test 458 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 458 failed: {e}")
        test_results.append(False)

    # Test case 459
    try:
        result = productExceptSelf([0, -5, -5])
        assert result == [25, 0, 0], f"Test 459 failed: got {result}, expected {[25, 0, 0]}"
        print(f"Test 459 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 459 failed: {e}")
        test_results.append(False)

    # Test case 460
    try:
        result = productExceptSelf([-5, -5])
        assert result == [-5, -5], f"Test 460 failed: got {result}, expected {[-5, -5]}"
        print(f"Test 460 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 460 failed: {e}")
        test_results.append(False)

    # Test case 461
    try:
        result = productExceptSelf([-5, -4, 0])
        assert result == [0, 0, 20], f"Test 461 failed: got {result}, expected {[0, 0, 20]}"
        print(f"Test 461 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 461 failed: {e}")
        test_results.append(False)

    # Test case 462
    try:
        result = productExceptSelf([-5, -5, 0])
        assert result == [0, 0, 25], f"Test 462 failed: got {result}, expected {[0, 0, 25]}"
        print(f"Test 462 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 462 failed: {e}")
        test_results.append(False)

    # Test case 463
    try:
        result = productExceptSelf([12, -5, 0, -5])
        assert result == [0, 0, 300, 0], f"Test 463 failed: got {result}, expected {[0, 0, 300, 0]}"
        print(f"Test 463 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 463 failed: {e}")
        test_results.append(False)

    # Test case 464
    try:
        result = productExceptSelf([-5, 0])
        assert result == [0, -5], f"Test 464 failed: got {result}, expected {[0, -5]}"
        print(f"Test 464 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 464 failed: {e}")
        test_results.append(False)

    # Test case 465
    try:
        result = productExceptSelf([-5, -5, -5, 1, -20])
        assert result == [-500, -500, -500, 2500, -125], f"Test 465 failed: got {result}, expected {[-500, -500, -500, 2500, -125]}"
        print(f"Test 465 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 465 failed: {e}")
        test_results.append(False)

    # Test case 466
    try:
        result = productExceptSelf([1000000, -5, -5, 8])
        assert result == [200, -40000000, -40000000, 25000000], f"Test 466 failed: got {result}, expected {[200, -40000000, -40000000, 25000000]}"
        print(f"Test 466 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 466 failed: {e}")
        test_results.append(False)

    # Test case 467
    try:
        result = productExceptSelf([-2147483648, 0, -5, -5])
        assert result == [0, -53687091200, 0, 0], f"Test 467 failed: got {result}, expected {[0, -53687091200, 0, 0]}"
        print(f"Test 467 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 467 failed: {e}")
        test_results.append(False)

    # Test case 468
    try:
        result = productExceptSelf([-10, -5, -5, 0])
        assert result == [0, 0, 0, -250], f"Test 468 failed: got {result}, expected {[0, 0, 0, -250]}"
        print(f"Test 468 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 468 failed: {e}")
        test_results.append(False)

    # Test case 469
    try:
        result = productExceptSelf([-5, -5, -5, 0, 0, -12, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 469 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 469 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 469 failed: {e}")
        test_results.append(False)

    # Test case 470
    try:
        result = productExceptSelf([-5, -5, -5, 0, 19])
        assert result == [0, 0, 0, -2375, 0], f"Test 470 failed: got {result}, expected {[0, 0, 0, -2375, 0]}"
        print(f"Test 470 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 470 failed: {e}")
        test_results.append(False)

    # Test case 471
    try:
        result = productExceptSelf([-5, -5, -5, 0])
        assert result == [0, 0, 0, -125], f"Test 471 failed: got {result}, expected {[0, 0, 0, -125]}"
        print(f"Test 471 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 471 failed: {e}")
        test_results.append(False)

    # Test case 472
    try:
        result = productExceptSelf([0, -4, -5, -11])
        assert result == [-220, 0, 0, 0], f"Test 472 failed: got {result}, expected {[-220, 0, 0, 0]}"
        print(f"Test 472 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 472 failed: {e}")
        test_results.append(False)

    # Test case 473
    try:
        result = productExceptSelf([92680, -1, 1, -1, -1, 1, 0])
        assert result == [0, 0, 0, 0, 0, 0, -92680], f"Test 473 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, -92680]}"
        print(f"Test 473 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 473 failed: {e}")
        test_results.append(False)

    # Test case 474
    try:
        result = productExceptSelf([1, 7, 1, -1, 1, 0, -100])
        assert result == [0, 0, 0, 0, 0, 700, 0], f"Test 474 failed: got {result}, expected {[0, 0, 0, 0, 0, 700, 0]}"
        print(f"Test 474 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 474 failed: {e}")
        test_results.append(False)

    # Test case 475
    try:
        result = productExceptSelf([1, -1, 1, -1, 46340, -1])
        assert result == [-46340, 46340, -46340, 46340, -1, 46340], f"Test 475 failed: got {result}, expected {[-46340, 46340, -46340, 46340, -1, 46340]}"
        print(f"Test 475 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 475 failed: {e}")
        test_results.append(False)

    # Test case 476
    try:
        result = productExceptSelf([1, 0, 1, -1, 1, -1, -11, 99999])
        assert result == [0, -1099989, 0, 0, 0, 0, 0, 0], f"Test 476 failed: got {result}, expected {[0, -1099989, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 476 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 476 failed: {e}")
        test_results.append(False)

    # Test case 477
    try:
        result = productExceptSelf([-1, 1, 1, 1, -1])
        assert result == [-1, 1, 1, 1, -1], f"Test 477 failed: got {result}, expected {[-1, 1, 1, 1, -1]}"
        print(f"Test 477 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 477 failed: {e}")
        test_results.append(False)

    # Test case 478
    try:
        result = productExceptSelf([92680, -1, 1, -1, 1, -1, 0, -1])
        assert result == [0, 0, 0, 0, 0, 0, 92680, 0], f"Test 478 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 92680, 0]}"
        print(f"Test 478 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 478 failed: {e}")
        test_results.append(False)

    # Test case 479
    try:
        result = productExceptSelf([-1, 1, -1, 1, -1, 1])
        assert result == [1, -1, 1, -1, 1, -1], f"Test 479 failed: got {result}, expected {[1, -1, 1, -1, 1, -1]}"
        print(f"Test 479 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 479 failed: {e}")
        test_results.append(False)

    # Test case 480
    try:
        result = productExceptSelf([1, 1, -1, -1, 0, 2147483649])
        assert result == [0, 0, 0, 0, 2147483649, 0], f"Test 480 failed: got {result}, expected {[0, 0, 0, 0, 2147483649, 0]}"
        print(f"Test 480 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 480 failed: {e}")
        test_results.append(False)

    # Test case 481
    try:
        result = productExceptSelf([1, -2, 1, -1, 1, -1])
        assert result == [-2, 1, -2, 2, -2, 2], f"Test 481 failed: got {result}, expected {[-2, 1, -2, 2, -2, 2]}"
        print(f"Test 481 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 481 failed: {e}")
        test_results.append(False)

    # Test case 482
    try:
        result = productExceptSelf([1, -1, 1, -1, -1])
        assert result == [-1, 1, -1, 1, 1], f"Test 482 failed: got {result}, expected {[-1, 1, -1, 1, 1]}"
        print(f"Test 482 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 482 failed: {e}")
        test_results.append(False)

    # Test case 483
    try:
        result = productExceptSelf([1, -1, 1, -1, 1, -1, 0])
        assert result == [0, 0, 0, 0, 0, 0, -1], f"Test 483 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, -1]}"
        print(f"Test 483 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 483 failed: {e}")
        test_results.append(False)

    # Test case 484
    try:
        result = productExceptSelf([-1, 5, 1, -1, 1, -1])
        assert result == [5, -1, -5, 5, -5, 5], f"Test 484 failed: got {result}, expected {[5, -1, -5, 5, -5, 5]}"
        print(f"Test 484 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 484 failed: {e}")
        test_results.append(False)

    # Test case 485
    try:
        result = productExceptSelf([-1, -1, 1, -1, 0])
        assert result == [0, 0, 0, 0, -1], f"Test 485 failed: got {result}, expected {[0, 0, 0, 0, -1]}"
        print(f"Test 485 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 485 failed: {e}")
        test_results.append(False)

    # Test case 486
    try:
        result = productExceptSelf([4, 4, 2, 2, 1, 1, 0, 0, 50000, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 486 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 486 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 486 failed: {e}")
        test_results.append(False)

    # Test case 487
    try:
        result = productExceptSelf([1, 1, 2, 2, 18, 4, 0])
        assert result == [0, 0, 0, 0, 0, 0, 288], f"Test 487 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 288]}"
        print(f"Test 487 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 487 failed: {e}")
        test_results.append(False)

    # Test case 488
    try:
        result = productExceptSelf([1, 1, 2, 2, 4, 4, 0, 1])
        assert result == [0, 0, 0, 0, 0, 0, 64, 0], f"Test 488 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 64, 0]}"
        print(f"Test 488 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 488 failed: {e}")
        test_results.append(False)

    # Test case 489
    try:
        result = productExceptSelf([4, 4, 2, 2, 1, 0, 0, 46342, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 489 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 489 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 489 failed: {e}")
        test_results.append(False)

    # Test case 490
    try:
        result = productExceptSelf([2, 4, 2, 1, 1])
        assert result == [8, 4, 8, 16, 16], f"Test 490 failed: got {result}, expected {[8, 4, 8, 16, 16]}"
        print(f"Test 490 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 490 failed: {e}")
        test_results.append(False)

    # Test case 491
    try:
        result = productExceptSelf([4, 11, 2, 2, 0, 1])
        assert result == [0, 0, 0, 0, 176, 0], f"Test 491 failed: got {result}, expected {[0, 0, 0, 0, 176, 0]}"
        print(f"Test 491 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 491 failed: {e}")
        test_results.append(False)

    # Test case 492
    try:
        result = productExceptSelf([5, -11, 2, 1])
        assert result == [-22, 10, -55, -110], f"Test 492 failed: got {result}, expected {[-22, 10, -55, -110]}"
        print(f"Test 492 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 492 failed: {e}")
        test_results.append(False)

    # Test case 493
    try:
        result = productExceptSelf([4, 4, 2, 2, 1, 34, 0, 46342, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0, 0], f"Test 493 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 493 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 493 failed: {e}")
        test_results.append(False)

    # Test case 494
    try:
        result = productExceptSelf([0, 1, 2, 2, 4, 4])
        assert result == [64, 0, 0, 0, 0, 0], f"Test 494 failed: got {result}, expected {[64, 0, 0, 0, 0, 0]}"
        print(f"Test 494 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 494 failed: {e}")
        test_results.append(False)

    # Test case 495
    try:
        result = productExceptSelf([4, 4, 2, 2, 1, 1, 201])
        assert result == [3216, 3216, 6432, 6432, 12864, 12864, 64], f"Test 495 failed: got {result}, expected {[3216, 3216, 6432, 6432, 12864, 12864, 64]}"
        print(f"Test 495 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 495 failed: {e}")
        test_results.append(False)

    # Test case 496
    try:
        result = productExceptSelf([4, 4, 2, 1])
        assert result == [8, 8, 16, 32], f"Test 496 failed: got {result}, expected {[8, 8, 16, 32]}"
        print(f"Test 496 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 496 failed: {e}")
        test_results.append(False)

    # Test case 497
    try:
        result = productExceptSelf([1, 1, 2, 4, 4])
        assert result == [32, 32, 16, 8, 8], f"Test 497 failed: got {result}, expected {[32, 32, 16, 8, 8]}"
        print(f"Test 497 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 497 failed: {e}")
        test_results.append(False)

    # Test case 498
    try:
        result = productExceptSelf([4, 2, 2, 1, 18, 0, 13])
        assert result == [0, 0, 0, 0, 0, 3744, 0], f"Test 498 failed: got {result}, expected {[0, 0, 0, 0, 0, 3744, 0]}"
        print(f"Test 498 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 498 failed: {e}")
        test_results.append(False)

    # Test case 499
    try:
        result = productExceptSelf([-4, 4, 2, 1])
        assert result == [8, -8, -16, -32], f"Test 499 failed: got {result}, expected {[8, -8, -16, -32]}"
        print(f"Test 499 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 499 failed: {e}")
        test_results.append(False)

    # Test case 500
    try:
        result = productExceptSelf([4, 4, 2, 2, -1, 1, 46341, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, -2965824], f"Test 500 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, -2965824]}"
        print(f"Test 500 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 500 failed: {e}")
        test_results.append(False)

    # Test case 501
    try:
        result = productExceptSelf([0, -12, 0, 24])
        assert result == [0, 0, 0, 0], f"Test 501 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 501 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 501 failed: {e}")
        test_results.append(False)

    # Test case 502
    try:
        result = productExceptSelf([-12, 0, 12, 0])
        assert result == [0, 0, 0, 0], f"Test 502 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 502 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 502 failed: {e}")
        test_results.append(False)

    # Test case 503
    try:
        result = productExceptSelf([300, 12, 0, 3])
        assert result == [0, 0, 10800, 0], f"Test 503 failed: got {result}, expected {[0, 0, 10800, 0]}"
        print(f"Test 503 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 503 failed: {e}")
        test_results.append(False)

    # Test case 504
    try:
        result = productExceptSelf([0, -12, 0])
        assert result == [0, 0, 0], f"Test 504 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 504 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 504 failed: {e}")
        test_results.append(False)

    # Test case 505
    try:
        result = productExceptSelf([12, 0, -12, -1, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 505 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 505 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 505 failed: {e}")
        test_results.append(False)

    # Test case 506
    try:
        result = productExceptSelf([4, -12, 0, 12])
        assert result == [0, 0, -576, 0], f"Test 506 failed: got {result}, expected {[0, 0, -576, 0]}"
        print(f"Test 506 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 506 failed: {e}")
        test_results.append(False)

    # Test case 507
    try:
        result = productExceptSelf([12, 0, -24, 24, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 507 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 507 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 507 failed: {e}")
        test_results.append(False)

    # Test case 508
    try:
        result = productExceptSelf([12, 0, -12, 99999])
        assert result == [0, -14399856, 0, 0], f"Test 508 failed: got {result}, expected {[0, -14399856, 0, 0]}"
        print(f"Test 508 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 508 failed: {e}")
        test_results.append(False)

    # Test case 509
    try:
        result = productExceptSelf([0, -12, 0, 12, 11, -99999])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 509 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 509 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 509 failed: {e}")
        test_results.append(False)

    # Test case 510
    try:
        result = productExceptSelf([-12, 0, 12])
        assert result == [0, -144, 0], f"Test 510 failed: got {result}, expected {[0, -144, 0]}"
        print(f"Test 510 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 510 failed: {e}")
        test_results.append(False)

    # Test case 511
    try:
        result = productExceptSelf([12, 0, -12, -11])
        assert result == [0, 1584, 0, 0], f"Test 511 failed: got {result}, expected {[0, 1584, 0, 0]}"
        print(f"Test 511 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 511 failed: {e}")
        test_results.append(False)

    # Test case 512
    try:
        result = productExceptSelf([12, -12, 46341, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 512 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 512 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 512 failed: {e}")
        test_results.append(False)

    # Test case 513
    try:
        result = productExceptSelf([12, 0, -12, -5])
        assert result == [0, 720, 0, 0], f"Test 513 failed: got {result}, expected {[0, 720, 0, 0]}"
        print(f"Test 513 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 513 failed: {e}")
        test_results.append(False)

    # Test case 514
    try:
        result = productExceptSelf([100, 2147483649])
        assert result == [2147483649, 100], f"Test 514 failed: got {result}, expected {[2147483649, 100]}"
        print(f"Test 514 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 514 failed: {e}")
        test_results.append(False)

    # Test case 515
    try:
        result = productExceptSelf([0, 11, -1, 2, 2147483647, 1])
        assert result == [-47244640234, 0, 0, 0, 0, 0], f"Test 515 failed: got {result}, expected {[-47244640234, 0, 0, 0, 0, 0]}"
        print(f"Test 515 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 515 failed: {e}")
        test_results.append(False)

    # Test case 516
    try:
        result = productExceptSelf([2147483647, 1, 2147483649])
        assert result == [2147483649, 4611686018427387903, 2147483647], f"Test 516 failed: got {result}, expected {[2147483649, 4611686018427387903, 2147483647]}"
        print(f"Test 516 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 516 failed: {e}")
        test_results.append(False)

    # Test case 517
    try:
        result = productExceptSelf([2147483647, 1, -1, 9])
        assert result == [-9, -19327352823, 19327352823, -2147483647], f"Test 517 failed: got {result}, expected {[-9, -19327352823, 19327352823, -2147483647]}"
        print(f"Test 517 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 517 failed: {e}")
        test_results.append(False)

    # Test case 518
    try:
        result = productExceptSelf([0, 5, -1, 1, 2147483647])
        assert result == [-10737418235, 0, 0, 0, 0], f"Test 518 failed: got {result}, expected {[-10737418235, 0, 0, 0, 0]}"
        print(f"Test 518 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 518 failed: {e}")
        test_results.append(False)

    # Test case 519
    try:
        result = productExceptSelf([-1, 1, 2147483647, 0])
        assert result == [0, 0, 0, -2147483647], f"Test 519 failed: got {result}, expected {[0, 0, 0, -2147483647]}"
        print(f"Test 519 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 519 failed: {e}")
        test_results.append(False)

    # Test case 520
    try:
        result = productExceptSelf([2147483647, 1, -1, 0, 100, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 520 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 520 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 520 failed: {e}")
        test_results.append(False)

    # Test case 521
    try:
        result = productExceptSelf([-1, 1, 2147483647, 0, 24])
        assert result == [0, 0, 0, -51539607528, 0], f"Test 521 failed: got {result}, expected {[0, 0, 0, -51539607528, 0]}"
        print(f"Test 521 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 521 failed: {e}")
        test_results.append(False)

    # Test case 522
    try:
        result = productExceptSelf([2147483647])
        assert result == [1], f"Test 522 failed: got {result}, expected {[1]}"
        print(f"Test 522 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 522 failed: {e}")
        test_results.append(False)

    # Test case 523
    try:
        result = productExceptSelf([2147483647, 1, -1, 46340, 1, 0])
        assert result == [0, 0, 0, 0, 0, -99514392201980], f"Test 523 failed: got {result}, expected {[0, 0, 0, 0, 0, -99514392201980]}"
        print(f"Test 523 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 523 failed: {e}")
        test_results.append(False)

    # Test case 524
    try:
        result = productExceptSelf([1, 0, -24, 46341])
        assert result == [0, -1112184, 0, 0], f"Test 524 failed: got {result}, expected {[0, -1112184, 0, 0]}"
        print(f"Test 524 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 524 failed: {e}")
        test_results.append(False)

    # Test case 525
    try:
        result = productExceptSelf([-1, 1, 2147483647, 11, -11])
        assert result == [-259845521287, 259845521287, 121, 23622320117, -23622320117], f"Test 525 failed: got {result}, expected {[-259845521287, 259845521287, 121, 23622320117, -23622320117]}"
        print(f"Test 525 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 525 failed: {e}")
        test_results.append(False)

    # Test case 526
    try:
        result = productExceptSelf([0, -1])
        assert result == [-1, 0], f"Test 526 failed: got {result}, expected {[-1, 0]}"
        print(f"Test 526 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 526 failed: {e}")
        test_results.append(False)

    # Test case 527
    try:
        result = productExceptSelf([0, 0, 1, -1])
        assert result == [0, 0, 0, 0], f"Test 527 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 527 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 527 failed: {e}")
        test_results.append(False)

    # Test case 528
    try:
        result = productExceptSelf([2147483647, 1, -1, 0])
        assert result == [0, 0, 0, -2147483647], f"Test 528 failed: got {result}, expected {[0, 0, 0, -2147483647]}"
        print(f"Test 528 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 528 failed: {e}")
        test_results.append(False)

    # Test case 529
    try:
        result = productExceptSelf([-2147483648])
        assert result == [1], f"Test 529 failed: got {result}, expected {[1]}"
        print(f"Test 529 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 529 failed: {e}")
        test_results.append(False)

    # Test case 530
    try:
        result = productExceptSelf([1, -2147483648, 0])
        assert result == [0, 0, -2147483648], f"Test 530 failed: got {result}, expected {[0, 0, -2147483648]}"
        print(f"Test 530 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 530 failed: {e}")
        test_results.append(False)

    # Test case 531
    try:
        result = productExceptSelf([-2147483648, 1, 0])
        assert result == [0, 0, -2147483648], f"Test 531 failed: got {result}, expected {[0, 0, -2147483648]}"
        print(f"Test 531 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 531 failed: {e}")
        test_results.append(False)

    # Test case 532
    try:
        result = productExceptSelf([46339])
        assert result == [1], f"Test 532 failed: got {result}, expected {[1]}"
        print(f"Test 532 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 532 failed: {e}")
        test_results.append(False)

    # Test case 533
    try:
        result = productExceptSelf([-2147483649, 2])
        assert result == [2, -2147483649], f"Test 533 failed: got {result}, expected {[2, -2147483649]}"
        print(f"Test 533 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 533 failed: {e}")
        test_results.append(False)

    # Test case 534
    try:
        result = productExceptSelf([-10, 2147483647, -2147483648, 2])
        assert result == [-9223372032559808512, 42949672960, -42949672940, 46116860162799042560], f"Test 534 failed: got {result}, expected {[-9223372032559808512, 42949672960, -42949672940, 46116860162799042560]}"
        print(f"Test 534 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 534 failed: {e}")
        test_results.append(False)

    # Test case 535
    try:
        result = productExceptSelf([1, -2147483648, 7, 0])
        assert result == [0, 0, 0, -15032385536], f"Test 535 failed: got {result}, expected {[0, 0, 0, -15032385536]}"
        print(f"Test 535 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 535 failed: {e}")
        test_results.append(False)

    # Test case 536
    try:
        result = productExceptSelf([-2147483648, 0, 0, 13])
        assert result == [0, 0, 0, 0], f"Test 536 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 536 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 536 failed: {e}")
        test_results.append(False)

    # Test case 537
    try:
        result = productExceptSelf([-2147483648, 1, 200])
        assert result == [200, -429496729600, -2147483648], f"Test 537 failed: got {result}, expected {[200, -429496729600, -2147483648]}"
        print(f"Test 537 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 537 failed: {e}")
        test_results.append(False)

    # Test case 538
    try:
        result = productExceptSelf([1, -2147483648])
        assert result == [-2147483648, 1], f"Test 538 failed: got {result}, expected {[-2147483648, 1]}"
        print(f"Test 538 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 538 failed: {e}")
        test_results.append(False)

    # Test case 539
    try:
        result = productExceptSelf([-2147483648, 0])
        assert result == [0, -2147483648], f"Test 539 failed: got {result}, expected {[0, -2147483648]}"
        print(f"Test 539 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 539 failed: {e}")
        test_results.append(False)

    # Test case 540
    try:
        result = productExceptSelf([49999, 50000, 50000, 0])
        assert result == [0, 0, 0, 124997500000000], f"Test 540 failed: got {result}, expected {[0, 0, 0, 124997500000000]}"
        print(f"Test 540 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 540 failed: {e}")
        test_results.append(False)

    # Test case 541
    try:
        result = productExceptSelf([0, -300, 50000, 50000])
        assert result == [-750000000000, 0, 0, 0], f"Test 541 failed: got {result}, expected {[-750000000000, 0, 0, 0]}"
        print(f"Test 541 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 541 failed: {e}")
        test_results.append(False)

    # Test case 542
    try:
        result = productExceptSelf([49999, 50000])
        assert result == [50000, 49999], f"Test 542 failed: got {result}, expected {[50000, 49999]}"
        print(f"Test 542 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 542 failed: {e}")
        test_results.append(False)

    # Test case 543
    try:
        result = productExceptSelf([200000])
        assert result == [1], f"Test 543 failed: got {result}, expected {[1]}"
        print(f"Test 543 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 543 failed: {e}")
        test_results.append(False)

    # Test case 544
    try:
        result = productExceptSelf([50000, 50000, 9, 0])
        assert result == [0, 0, 0, 22500000000], f"Test 544 failed: got {result}, expected {[0, 0, 0, 22500000000]}"
        print(f"Test 544 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 544 failed: {e}")
        test_results.append(False)

    # Test case 545
    try:
        result = productExceptSelf([50000, 200])
        assert result == [200, 50000], f"Test 545 failed: got {result}, expected {[200, 50000]}"
        print(f"Test 545 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 545 failed: {e}")
        test_results.append(False)

    # Test case 546
    try:
        result = productExceptSelf([50000, 50000, 50000, 0, 0, 49999])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 546 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 546 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 546 failed: {e}")
        test_results.append(False)

    # Test case 547
    try:
        result = productExceptSelf([50000, 50000])
        assert result == [50000, 50000], f"Test 547 failed: got {result}, expected {[50000, 50000]}"
        print(f"Test 547 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 547 failed: {e}")
        test_results.append(False)

    # Test case 548
    try:
        result = productExceptSelf([50000, 50000, 50000, 100000])
        assert result == [250000000000000, 250000000000000, 250000000000000, 125000000000000], f"Test 548 failed: got {result}, expected {[250000000000000, 250000000000000, 250000000000000, 125000000000000]}"
        print(f"Test 548 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 548 failed: {e}")
        test_results.append(False)

    # Test case 549
    try:
        result = productExceptSelf([7, 46341, 50000, 0, 50000])
        assert result == [0, 0, 0, 810967500000000, 0], f"Test 549 failed: got {result}, expected {[0, 0, 0, 810967500000000, 0]}"
        print(f"Test 549 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 549 failed: {e}")
        test_results.append(False)

    # Test case 550
    try:
        result = productExceptSelf([50000, 50000, -100, 0, 0, -24])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 550 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 550 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 550 failed: {e}")
        test_results.append(False)

    # Test case 551
    try:
        result = productExceptSelf([50000, -13, 24, 18])
        assert result == [-5616, 21600000, -11700000, -15600000], f"Test 551 failed: got {result}, expected {[-5616, 21600000, -11700000, -15600000]}"
        print(f"Test 551 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 551 failed: {e}")
        test_results.append(False)

    # Test case 552
    try:
        result = productExceptSelf([50000])
        assert result == [1], f"Test 552 failed: got {result}, expected {[1]}"
        print(f"Test 552 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 552 failed: {e}")
        test_results.append(False)

    # Test case 553
    try:
        result = productExceptSelf([50000, 50000, 50000, -46340])
        assert result == [-115850000000000, -115850000000000, -115850000000000, 125000000000000], f"Test 553 failed: got {result}, expected {[-115850000000000, -115850000000000, -115850000000000, 125000000000000]}"
        print(f"Test 553 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 553 failed: {e}")
        test_results.append(False)

    # Test case 554
    try:
        result = productExceptSelf([100000, 100000, 100000, 0, 4])
        assert result == [0, 0, 0, 4000000000000000, 0], f"Test 554 failed: got {result}, expected {[0, 0, 0, 4000000000000000, 0]}"
        print(f"Test 554 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 554 failed: {e}")
        test_results.append(False)

    # Test case 555
    try:
        result = productExceptSelf([100000, 2147483647, 100000, 300, 0])
        assert result == [0, 0, 0, 0, 6442450941000000000000], f"Test 555 failed: got {result}, expected {[0, 0, 0, 0, 6442450941000000000000]}"
        print(f"Test 555 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 555 failed: {e}")
        test_results.append(False)

    # Test case 556
    try:
        result = productExceptSelf([100000, 100000, 100000, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 556 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 556 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 556 failed: {e}")
        test_results.append(False)

    # Test case 557
    try:
        result = productExceptSelf([100000, 100000, 100000, 100000, 0])
        assert result == [0, 0, 0, 0, 100000000000000000000], f"Test 557 failed: got {result}, expected {[0, 0, 0, 0, 100000000000000000000]}"
        print(f"Test 557 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 557 failed: {e}")
        test_results.append(False)

    # Test case 558
    try:
        result = productExceptSelf([100000, 100000, 100000, 9])
        assert result == [90000000000, 90000000000, 90000000000, 1000000000000000], f"Test 558 failed: got {result}, expected {[90000000000, 90000000000, 90000000000, 1000000000000000]}"
        print(f"Test 558 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 558 failed: {e}")
        test_results.append(False)

    # Test case 559
    try:
        result = productExceptSelf([200000, 100000, 100000])
        assert result == [10000000000, 20000000000, 20000000000], f"Test 559 failed: got {result}, expected {[10000000000, 20000000000, 20000000000]}"
        print(f"Test 559 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 559 failed: {e}")
        test_results.append(False)

    # Test case 560
    try:
        result = productExceptSelf([0, 0, 18, 100000, 100000, 100000, 100000])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 560 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 560 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 560 failed: {e}")
        test_results.append(False)

    # Test case 561
    try:
        result = productExceptSelf([0, 50000, 0, 100000, 100000, 100000, 100000])
        assert result == [0, 0, 0, 0, 0, 0, 0], f"Test 561 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 561 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 561 failed: {e}")
        test_results.append(False)

    # Test case 562
    try:
        result = productExceptSelf([100000, 100000, 100000, 0, 99])
        assert result == [0, 0, 0, 99000000000000000, 0], f"Test 562 failed: got {result}, expected {[0, 0, 0, 99000000000000000, 0]}"
        print(f"Test 562 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 562 failed: {e}")
        test_results.append(False)

    # Test case 563
    try:
        result = productExceptSelf([100000, 100000, 100000, 100001])
        assert result == [1000010000000000, 1000010000000000, 1000010000000000, 1000000000000000], f"Test 563 failed: got {result}, expected {[1000010000000000, 1000010000000000, 1000010000000000, 1000000000000000]}"
        print(f"Test 563 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 563 failed: {e}")
        test_results.append(False)

    # Test case 564
    try:
        result = productExceptSelf([100000, 100000, 100000])
        assert result == [10000000000, 10000000000, 10000000000], f"Test 564 failed: got {result}, expected {[10000000000, 10000000000, 10000000000]}"
        print(f"Test 564 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 564 failed: {e}")
        test_results.append(False)

    # Test case 565
    try:
        result = productExceptSelf([100000, 100000, 100000, 100000, -10])
        assert result == [-10000000000000000, -10000000000000000, -10000000000000000, -10000000000000000, 100000000000000000000], f"Test 565 failed: got {result}, expected {[-10000000000000000, -10000000000000000, -10000000000000000, -10000000000000000, 100000000000000000000]}"
        print(f"Test 565 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 565 failed: {e}")
        test_results.append(False)

    # Test case 566
    try:
        result = productExceptSelf([-99999, 2, 2, 2147483647])
        assert result == [8589934588, -429492434432706, -429492434432706, -399996], f"Test 566 failed: got {result}, expected {[8589934588, -429492434432706, -429492434432706, -399996]}"
        print(f"Test 566 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 566 failed: {e}")
        test_results.append(False)

    # Test case 567
    try:
        result = productExceptSelf([2, 13, 0])
        assert result == [0, 0, 26], f"Test 567 failed: got {result}, expected {[0, 0, 26]}"
        print(f"Test 567 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 567 failed: {e}")
        test_results.append(False)

    # Test case 568
    try:
        result = productExceptSelf([2147483647, 2, 0, 0])
        assert result == [0, 0, 0, 0], f"Test 568 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 568 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 568 failed: {e}")
        test_results.append(False)

    # Test case 569
    try:
        result = productExceptSelf([2, 2, 2147483647, -46340])
        assert result == [-199028784403960, -199028784403960, -185360, 8589934588], f"Test 569 failed: got {result}, expected {[-199028784403960, -199028784403960, -185360, 8589934588]}"
        print(f"Test 569 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 569 failed: {e}")
        test_results.append(False)

    # Test case 570
    try:
        result = productExceptSelf([-3, 2, 2, 8])
        assert result == [32, -48, -48, -12], f"Test 570 failed: got {result}, expected {[32, -48, -48, -12]}"
        print(f"Test 570 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 570 failed: {e}")
        test_results.append(False)

    # Test case 571
    try:
        result = productExceptSelf([5, 2, 2, 2147483647, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 571 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 571 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 571 failed: {e}")
        test_results.append(False)

    # Test case 572
    try:
        result = productExceptSelf([2147483647, 2, 2, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 572 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 572 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 572 failed: {e}")
        test_results.append(False)

    # Test case 573
    try:
        result = productExceptSelf([2, 2, 0, -26])
        assert result == [0, 0, -104, 0], f"Test 573 failed: got {result}, expected {[0, 0, -104, 0]}"
        print(f"Test 573 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 573 failed: {e}")
        test_results.append(False)

    # Test case 574
    try:
        result = productExceptSelf([-2147483649, 2147483646, 2, 1])
        assert result == [4294967292, -4294967298, -4611686016279904254, -9223372032559808508], f"Test 574 failed: got {result}, expected {[4294967292, -4294967298, -4611686016279904254, -9223372032559808508]}"
        print(f"Test 574 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 574 failed: {e}")
        test_results.append(False)

    # Test case 575
    try:
        result = productExceptSelf([2147483647, 2, 2, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 575 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 575 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 575 failed: {e}")
        test_results.append(False)

    # Test case 576
    try:
        result = productExceptSelf([2, 2, 2147483647])
        assert result == [4294967294, 4294967294, 4], f"Test 576 failed: got {result}, expected {[4294967294, 4294967294, 4]}"
        print(f"Test 576 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 576 failed: {e}")
        test_results.append(False)

    # Test case 577
    try:
        result = productExceptSelf([0, 2, 2147483646, 0])
        assert result == [0, 0, 0, 0], f"Test 577 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 577 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 577 failed: {e}")
        test_results.append(False)

    # Test case 578
    try:
        result = productExceptSelf([2, 2147483647, 0])
        assert result == [0, 0, 4294967294], f"Test 578 failed: got {result}, expected {[0, 0, 4294967294]}"
        print(f"Test 578 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 578 failed: {e}")
        test_results.append(False)

    # Test case 579
    try:
        result = productExceptSelf([4294967294, 2, 49999])
        assert result == [99998, 214744069732706, 8589934588], f"Test 579 failed: got {result}, expected {[99998, 214744069732706, 8589934588]}"
        print(f"Test 579 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 579 failed: {e}")
        test_results.append(False)

    # Test case 580
    try:
        result = productExceptSelf([2147483647, 2, 2, 0])
        assert result == [0, 0, 0, 8589934588], f"Test 580 failed: got {result}, expected {[0, 0, 0, 8589934588]}"
        print(f"Test 580 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 580 failed: {e}")
        test_results.append(False)

    # Test case 581
    try:
        result = productExceptSelf([1, -1, -2147483648, 92680])
        assert result == [199028784496640, -199028784496640, -92680, 2147483648], f"Test 581 failed: got {result}, expected {[199028784496640, -199028784496640, -92680, 2147483648]}"
        print(f"Test 581 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 581 failed: {e}")
        test_results.append(False)

    # Test case 582
    try:
        result = productExceptSelf([-1, 1, -11])
        assert result == [-11, 11, -1], f"Test 582 failed: got {result}, expected {[-11, 11, -1]}"
        print(f"Test 582 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 582 failed: {e}")
        test_results.append(False)

    # Test case 583
    try:
        result = productExceptSelf([-2147483648, -1, -1, 13])
        assert result == [13, 27917287424, 27917287424, -2147483648], f"Test 583 failed: got {result}, expected {[13, 27917287424, 27917287424, -2147483648]}"
        print(f"Test 583 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 583 failed: {e}")
        test_results.append(False)

    # Test case 584
    try:
        result = productExceptSelf([-1, 0, 200000])
        assert result == [0, -200000, 0], f"Test 584 failed: got {result}, expected {[0, -200000, 0]}"
        print(f"Test 584 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 584 failed: {e}")
        test_results.append(False)

    # Test case 585
    try:
        result = productExceptSelf([1, -1, -2147483648])
        assert result == [2147483648, -2147483648, -1], f"Test 585 failed: got {result}, expected {[2147483648, -2147483648, -1]}"
        print(f"Test 585 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 585 failed: {e}")
        test_results.append(False)

    # Test case 586
    try:
        result = productExceptSelf([-2147483648, 0, -2147483649, 0, 24])
        assert result == [0, 0, 0, 0, 0], f"Test 586 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 586 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 586 failed: {e}")
        test_results.append(False)

    # Test case 587
    try:
        result = productExceptSelf([1, 46340, 2147483647])
        assert result == [99514392201980, 2147483647, 46340], f"Test 587 failed: got {result}, expected {[99514392201980, 2147483647, 46340]}"
        print(f"Test 587 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 587 failed: {e}")
        test_results.append(False)

    # Test case 588
    try:
        result = productExceptSelf([2147483648, 1, -1, -2147483648, 0])
        assert result == [0, 0, 0, 0, 4611686018427387904], f"Test 588 failed: got {result}, expected {[0, 0, 0, 0, 4611686018427387904]}"
        print(f"Test 588 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 588 failed: {e}")
        test_results.append(False)

    # Test case 589
    try:
        result = productExceptSelf([201, 200000, -2147483648, -1, 1])
        assert result == [429496729600000, 431644213248, -40200000, -86328842649600000, 86328842649600000], f"Test 589 failed: got {result}, expected {[429496729600000, 431644213248, -40200000, -86328842649600000, 86328842649600000]}"
        print(f"Test 589 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 589 failed: {e}")
        test_results.append(False)

    # Test case 590
    try:
        result = productExceptSelf([-26, -1, 1])
        assert result == [-1, -26, 26], f"Test 590 failed: got {result}, expected {[-1, -26, 26]}"
        print(f"Test 590 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 590 failed: {e}")
        test_results.append(False)

    # Test case 591
    try:
        result = productExceptSelf([-1, -1, -2147483648])
        assert result == [2147483648, 2147483648, 1], f"Test 591 failed: got {result}, expected {[2147483648, 2147483648, 1]}"
        print(f"Test 591 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 591 failed: {e}")
        test_results.append(False)

    # Test case 592
    try:
        result = productExceptSelf([-2147483648, -1, 1, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 592 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 592 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 592 failed: {e}")
        test_results.append(False)

    # Test case 593
    try:
        result = productExceptSelf([6, 3037000500, 6074001000])
        assert result == [18446744074000500000, 36444006000, 18222003000], f"Test 593 failed: got {result}, expected {[18446744074000500000, 36444006000, 18222003000]}"
        print(f"Test 593 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 593 failed: {e}")
        test_results.append(False)

    # Test case 594
    try:
        result = productExceptSelf([3037000500, 3037000500, 8])
        assert result == [24296004000, 24296004000, 9223372037000250000], f"Test 594 failed: got {result}, expected {[24296004000, 24296004000, 9223372037000250000]}"
        print(f"Test 594 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 594 failed: {e}")
        test_results.append(False)

    # Test case 595
    try:
        result = productExceptSelf([3037000502, 3037000500])
        assert result == [3037000500, 3037000502], f"Test 595 failed: got {result}, expected {[3037000500, 3037000502]}"
        print(f"Test 595 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 595 failed: {e}")
        test_results.append(False)

    # Test case 596
    try:
        result = productExceptSelf([0, 3037000500, 6074001000])
        assert result == [18446744074000500000, 0, 0], f"Test 596 failed: got {result}, expected {[18446744074000500000, 0, 0]}"
        print(f"Test 596 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 596 failed: {e}")
        test_results.append(False)

    # Test case 597
    try:
        result = productExceptSelf([3037000500, 3037000500, 0])
        assert result == [0, 0, 9223372037000250000], f"Test 597 failed: got {result}, expected {[0, 0, 9223372037000250000]}"
        print(f"Test 597 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 597 failed: {e}")
        test_results.append(False)

    # Test case 598
    try:
        result = productExceptSelf([0, 3037000500, 0, 92680])
        assert result == [0, 0, 0, 0], f"Test 598 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 598 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 598 failed: {e}")
        test_results.append(False)

    # Test case 599
    try:
        result = productExceptSelf([3037000500, 3037000501])
        assert result == [3037000501, 3037000500], f"Test 599 failed: got {result}, expected {[3037000501, 3037000500]}"
        print(f"Test 599 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 599 failed: {e}")
        test_results.append(False)

    # Test case 600
    try:
        result = productExceptSelf([3037000500, 3037000500, -13])
        assert result == [-39481006500, -39481006500, 9223372037000250000], f"Test 600 failed: got {result}, expected {[-39481006500, -39481006500, 9223372037000250000]}"
        print(f"Test 600 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 600 failed: {e}")
        test_results.append(False)

    # Test case 601
    try:
        result = productExceptSelf([0, 3037000500, 3037000500])
        assert result == [9223372037000250000, 0, 0], f"Test 601 failed: got {result}, expected {[9223372037000250000, 0, 0]}"
        print(f"Test 601 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 601 failed: {e}")
        test_results.append(False)

    # Test case 602
    try:
        result = productExceptSelf([3037000500, 3037000500, 11, 2])
        assert result == [66814011000, 66814011000, 18446744074000500000, 101457092407002750000], f"Test 602 failed: got {result}, expected {[66814011000, 66814011000, 18446744074000500000, 101457092407002750000]}"
        print(f"Test 602 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 602 failed: {e}")
        test_results.append(False)

    # Test case 603
    try:
        result = productExceptSelf([3037000500, 6])
        assert result == [6, 3037000500], f"Test 603 failed: got {result}, expected {[6, 3037000500]}"
        print(f"Test 603 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 603 failed: {e}")
        test_results.append(False)

    # Test case 604
    try:
        result = productExceptSelf([0, 99999, 99999, -99999, 99999])
        assert result == [-99996000059999600001, 0, 0, 0, 0], f"Test 604 failed: got {result}, expected {[-99996000059999600001, 0, 0, 0, 0]}"
        print(f"Test 604 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 604 failed: {e}")
        test_results.append(False)

    # Test case 605
    try:
        result = productExceptSelf([99999, -99999, 99999, -99999, 0, -2147483648, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0, 0, 0], f"Test 605 failed: got {result}, expected {[0, 0, 0, 0, 0, 0, 0, 0]}"
        print(f"Test 605 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 605 failed: {e}")
        test_results.append(False)

    # Test case 606
    try:
        result = productExceptSelf([0, -99999, -11, 24])
        assert result == [26399736, 0, 0, 0], f"Test 606 failed: got {result}, expected {[26399736, 0, 0, 0]}"
        print(f"Test 606 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 606 failed: {e}")
        test_results.append(False)

    # Test case 607
    try:
        result = productExceptSelf([100000, -99999, 99999, -99999, 0, 3])
        assert result == [0, 0, 0, 0, 299991000089999700000, 0], f"Test 607 failed: got {result}, expected {[0, 0, 0, 0, 299991000089999700000, 0]}"
        print(f"Test 607 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 607 failed: {e}")
        test_results.append(False)

    # Test case 608
    try:
        result = productExceptSelf([-99998, 99999])
        assert result == [99999, -99998], f"Test 608 failed: got {result}, expected {[99999, -99998]}"
        print(f"Test 608 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 608 failed: {e}")
        test_results.append(False)

    # Test case 609
    try:
        result = productExceptSelf([-99999, 99999, -99999, 99999])
        assert result == [-999970000299999, 999970000299999, -999970000299999, 999970000299999], f"Test 609 failed: got {result}, expected {[-999970000299999, 999970000299999, -999970000299999, 999970000299999]}"
        print(f"Test 609 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 609 failed: {e}")
        test_results.append(False)

    # Test case 610
    try:
        result = productExceptSelf([99999, -99999, 99999, -99999, 9, 0])
        assert result == [0, 0, 0, 0, 0, 899964000539996400009], f"Test 610 failed: got {result}, expected {[0, 0, 0, 0, 0, 899964000539996400009]}"
        print(f"Test 610 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 610 failed: {e}")
        test_results.append(False)

    # Test case 611
    try:
        result = productExceptSelf([-1, 99999, -99999, 99999, -99999, -1])
        assert result == [-99996000059999600001, 999970000299999, -999970000299999, 999970000299999, -999970000299999, -99996000059999600001], f"Test 611 failed: got {result}, expected {[-99996000059999600001, 999970000299999, -999970000299999, 999970000299999, -999970000299999, -99996000059999600001]}"
        print(f"Test 611 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 611 failed: {e}")
        test_results.append(False)

    # Test case 612
    try:
        result = productExceptSelf([99999, 99999, -99999, 4])
        assert result == [-39999200004, -39999200004, 39999200004, -999970000299999], f"Test 612 failed: got {result}, expected {[-39999200004, -39999200004, 39999200004, -999970000299999]}"
        print(f"Test 612 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 612 failed: {e}")
        test_results.append(False)

    # Test case 613
    try:
        result = productExceptSelf([99999, -99999, 0])
        assert result == [0, 0, -9999800001], f"Test 613 failed: got {result}, expected {[0, 0, -9999800001]}"
        print(f"Test 613 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 613 failed: {e}")
        test_results.append(False)

    # Test case 614
    try:
        result = productExceptSelf([99999, -99999, 99999, 0, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 614 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 614 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 614 failed: {e}")
        test_results.append(False)

    # Test case 615
    try:
        result = productExceptSelf([-99999, 99999, -99999, -99999])
        assert result == [999970000299999, -999970000299999, 999970000299999, 999970000299999], f"Test 615 failed: got {result}, expected {[999970000299999, -999970000299999, 999970000299999, 999970000299999]}"
        print(f"Test 615 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 615 failed: {e}")
        test_results.append(False)

    # Test case 616
    try:
        result = productExceptSelf([-99999, 99999, -99999, 99999, 0])
        assert result == [0, 0, 0, 0, 99996000059999600001], f"Test 616 failed: got {result}, expected {[0, 0, 0, 0, 99996000059999600001]}"
        print(f"Test 616 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 616 failed: {e}")
        test_results.append(False)

    # Test case 617
    try:
        result = productExceptSelf([-99999, 99999, -99999, 100000])
        assert result == [-999980000100000, 999980000100000, -999980000100000, 999970000299999], f"Test 617 failed: got {result}, expected {[-999980000100000, 999980000100000, -999980000100000, 999970000299999]}"
        print(f"Test 617 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 617 failed: {e}")
        test_results.append(False)

    # Test case 618
    try:
        result = productExceptSelf([99999, -99999, 99999, -99999, 0])
        assert result == [0, 0, 0, 0, 99996000059999600001], f"Test 618 failed: got {result}, expected {[0, 0, 0, 0, 99996000059999600001]}"
        print(f"Test 618 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 618 failed: {e}")
        test_results.append(False)

    # Test case 619
    try:
        result = productExceptSelf([1000002, 1000000, 0, 1000000, -99999, 6])
        assert result == [0, 0, -599995199988000000000000, 0, 0, 0], f"Test 619 failed: got {result}, expected {[0, 0, -599995199988000000000000, 0, 0, 0]}"
        print(f"Test 619 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 619 failed: {e}")
        test_results.append(False)

    # Test case 620
    try:
        result = productExceptSelf([1000000, 1000000, 1000000])
        assert result == [1000000000000, 1000000000000, 1000000000000], f"Test 620 failed: got {result}, expected {[1000000000000, 1000000000000, 1000000000000]}"
        print(f"Test 620 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 620 failed: {e}")
        test_results.append(False)

    # Test case 621
    try:
        result = productExceptSelf([1000000, 1000000, 0, -4294967298])
        assert result == [0, 0, -4294967298000000000000, 0], f"Test 621 failed: got {result}, expected {[0, 0, -4294967298000000000000, 0]}"
        print(f"Test 621 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 621 failed: {e}")
        test_results.append(False)

    # Test case 622
    try:
        result = productExceptSelf([1000000, 0, 1000000, 1000000, 0, 201])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 622 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 622 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 622 failed: {e}")
        test_results.append(False)

    # Test case 623
    try:
        result = productExceptSelf([1000000, 1000000, 0, 1000000, 200])
        assert result == [0, 0, 200000000000000000000, 0, 0], f"Test 623 failed: got {result}, expected {[0, 0, 200000000000000000000, 0, 0]}"
        print(f"Test 623 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 623 failed: {e}")
        test_results.append(False)

    # Test case 624
    try:
        result = productExceptSelf([0, 1000000, 0])
        assert result == [0, 0, 0], f"Test 624 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 624 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 624 failed: {e}")
        test_results.append(False)

    # Test case 625
    try:
        result = productExceptSelf([1000000, 0, 1000000, 1000000, 0])
        assert result == [0, 0, 0, 0, 0], f"Test 625 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 625 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 625 failed: {e}")
        test_results.append(False)

    # Test case 626
    try:
        result = productExceptSelf([1000000, 1000000, 0, 1000000])
        assert result == [0, 0, 1000000000000000000, 0], f"Test 626 failed: got {result}, expected {[0, 0, 1000000000000000000, 0]}"
        print(f"Test 626 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 626 failed: {e}")
        test_results.append(False)

    # Test case 627
    try:
        result = productExceptSelf([1000000, 1000000, 0, 12])
        assert result == [0, 0, 12000000000000, 0], f"Test 627 failed: got {result}, expected {[0, 0, 12000000000000, 0]}"
        print(f"Test 627 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 627 failed: {e}")
        test_results.append(False)

    # Test case 628
    try:
        result = productExceptSelf([1000000, 0, 1000000, 0])
        assert result == [0, 0, 0, 0], f"Test 628 failed: got {result}, expected {[0, 0, 0, 0]}"
        print(f"Test 628 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 628 failed: {e}")
        test_results.append(False)

    # Test case 629
    try:
        result = productExceptSelf([0, 1000000, 2, 0, 1000000])
        assert result == [0, 0, 0, 0, 0], f"Test 629 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 629 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 629 failed: {e}")
        test_results.append(False)

    # Test case 630
    try:
        result = productExceptSelf([1000000, 1000000, 0, 4294967294])
        assert result == [0, 0, 4294967294000000000000, 0], f"Test 630 failed: got {result}, expected {[0, 0, 4294967294000000000000, 0]}"
        print(f"Test 630 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 630 failed: {e}")
        test_results.append(False)

    # Test case 631
    try:
        result = productExceptSelf([1000000, 0, 1000000, 1000000, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 631 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 631 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 631 failed: {e}")
        test_results.append(False)

    # Test case 632
    try:
        result = productExceptSelf([1000000, 0, 1000000, 1000000, 12])
        assert result == [0, 12000000000000000000, 0, 0, 0], f"Test 632 failed: got {result}, expected {[0, 12000000000000000000, 0, 0, 0]}"
        print(f"Test 632 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 632 failed: {e}")
        test_results.append(False)

    # Test case 633
    try:
        result = productExceptSelf([2147483647, 2147483647, 4])
        assert result == [8589934588, 8589934588, 4611686014132420609], f"Test 633 failed: got {result}, expected {[8589934588, 8589934588, 4611686014132420609]}"
        print(f"Test 633 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 633 failed: {e}")
        test_results.append(False)

    # Test case 634
    try:
        result = productExceptSelf([2147483647, 2147483647, 2147483647, -99998, 0, 0])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 634 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 634 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 634 failed: {e}")
        test_results.append(False)

    # Test case 635
    try:
        result = productExceptSelf([-2147483647, 2147483647, 0])
        assert result == [0, 0, -4611686014132420609], f"Test 635 failed: got {result}, expected {[0, 0, -4611686014132420609]}"
        print(f"Test 635 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 635 failed: {e}")
        test_results.append(False)

    # Test case 636
    try:
        result = productExceptSelf([2147483647, 0, 0])
        assert result == [0, 0, 0], f"Test 636 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 636 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 636 failed: {e}")
        test_results.append(False)

    # Test case 637
    try:
        result = productExceptSelf([2147483647, 2147483647, 2147483647, 0])
        assert result == [0, 0, 0, 9903520300447984150353281023], f"Test 637 failed: got {result}, expected {[0, 0, 0, 9903520300447984150353281023]}"
        print(f"Test 637 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 637 failed: {e}")
        test_results.append(False)

    # Test case 638
    try:
        result = productExceptSelf([-2147483647, 2147483647])
        assert result == [2147483647, -2147483647], f"Test 638 failed: got {result}, expected {[2147483647, -2147483647]}"
        print(f"Test 638 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 638 failed: {e}")
        test_results.append(False)

    # Test case 639
    try:
        result = productExceptSelf([0, 2147483647, 2147483647, 0, 4294967294])
        assert result == [0, 0, 0, 0, 0], f"Test 639 failed: got {result}, expected {[0, 0, 0, 0, 0]}"
        print(f"Test 639 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 639 failed: {e}")
        test_results.append(False)

    # Test case 640
    try:
        result = productExceptSelf([2147483647, 2147483647])
        assert result == [2147483647, 2147483647], f"Test 640 failed: got {result}, expected {[2147483647, 2147483647]}"
        print(f"Test 640 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 640 failed: {e}")
        test_results.append(False)

    # Test case 641
    try:
        result = productExceptSelf([2147483647, -13])
        assert result == [-13, 2147483647], f"Test 641 failed: got {result}, expected {[-13, 2147483647]}"
        print(f"Test 641 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 641 failed: {e}")
        test_results.append(False)

    # Test case 642
    try:
        result = productExceptSelf([2147483647, 2147483647, 0, 100001])
        assert result == [0, 0, 461173213099256193320609, 0], f"Test 642 failed: got {result}, expected {[0, 0, 461173213099256193320609, 0]}"
        print(f"Test 642 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 642 failed: {e}")
        test_results.append(False)

    # Test case 643
    try:
        result = productExceptSelf([-2147483649, 2147483647, 2147483647, 2147483647])
        assert result == '-9903520309671356178618122241]', f"Test 643 failed: got {result}, expected {'-9903520309671356178618122241]'}"
        print(f"Test 643 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 643 failed: {e}")
        test_results.append(False)

    # Test case 644
    try:
        result = productExceptSelf([2147483647, 2147483647, 2147483647, 0, 100000])
        assert result == [0, 0, 0, 990352030044798415035328102300000, 0], f"Test 644 failed: got {result}, expected {[0, 0, 0, 990352030044798415035328102300000, 0]}"
        print(f"Test 644 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 644 failed: {e}")
        test_results.append(False)

    # Test case 645
    try:
        result = productExceptSelf([2147483647, 2147483647, 4294967294, 0, 0, 3])
        assert result == [0, 0, 0, 0, 0, 0], f"Test 645 failed: got {result}, expected {[0, 0, 0, 0, 0, 0]}"
        print(f"Test 645 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 645 failed: {e}")
        test_results.append(False)

    # Test case 646
    try:
        result = productExceptSelf([0, 2147483647, 0])
        assert result == [0, 0, 0], f"Test 646 failed: got {result}, expected {[0, 0, 0]}"
        print(f"Test 646 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 646 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
