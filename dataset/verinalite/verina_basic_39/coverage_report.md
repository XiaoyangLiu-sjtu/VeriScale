# Coverage Report

Total executable lines: 5
Covered lines: 5
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def rotateRight(l, n):
2: ✓     if not l:
3: ✓         return l
4: ✓     n %= len(l)
5: ✓     return l[-n:] + l[:-n]
```

## Complete Test File

```python
def rotateRight(l, n):
    if not l:
        return l
    n %= len(l)
    return l[-n:] + l[:-n]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = rotateRight([1, 2, 3, 4, 5], 2)
        assert result == [4, 5, 1, 2, 3], f"Test 1 failed: got {result}, expected {[4, 5, 1, 2, 3]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = rotateRight([1, 2, 3, 4, 5], 7)
        assert result == [4, 5, 1, 2, 3], f"Test 2 failed: got {result}, expected {[4, 5, 1, 2, 3]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = rotateRight([1, 2, 3, 4, 5], 0)
        assert result == [1, 2, 3, 4, 5], f"Test 3 failed: got {result}, expected {[1, 2, 3, 4, 5]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = rotateRight([], 2)
        assert result == [], f"Test 4 failed: got {result}, expected {[]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = rotateRight([42, 17, -5, 99, -100, 0, 8], 8)
        assert result == [8, 42, 17, -5, 99, -100, 0], f"Test 5 failed: got {result}, expected {[8, 42, 17, -5, 99, -100, 0]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = rotateRight([11, 22, 33, 44, 55, 66, 77], 14)
        assert result == [11, 22, 33, 44, 55, 66, 77], f"Test 6 failed: got {result}, expected {[11, 22, 33, 44, 55, 66, 77]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = rotateRight([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 12345)
        assert result == [34, 55, 89, 1, 1, 2, 3, 5, 8, 13, 21], f"Test 7 failed: got {result}, expected {[34, 55, 89, 1, 1, 2, 3, 5, 8, 13, 21]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = rotateRight([1, 2, 3, 4, 5], 3)
        assert result == [3, 4, 5, 1, 2], f"Test 8 failed: got {result}, expected {[3, 4, 5, 1, 2]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = rotateRight([1, 2, 3, 4, 6, 0, 800, 0], 7)
        assert result == [2, 3, 4, 6, 0, 800, 0, 1], f"Test 9 failed: got {result}, expected {[2, 3, 4, 6, 0, 800, 0, 1]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = rotateRight([1, 2, 3, 4, 5, -100], 65)
        assert result == [2, 3, 4, 5, -100, 1], f"Test 10 failed: got {result}, expected {[2, 3, 4, 5, -100, 1]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = rotateRight([1, 2, 3, 5], 2147483647)
        assert result == [2, 3, 5, 1], f"Test 11 failed: got {result}, expected {[2, 3, 5, 1]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = rotateRight([5, 4, 3, 2, 44], 11)
        assert result == [44, 5, 4, 3, 2], f"Test 12 failed: got {result}, expected {[44, 5, 4, 3, 2]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = rotateRight([5, -10, 3, 2, 1], 15)
        assert result == [5, -10, 3, 2, 1], f"Test 13 failed: got {result}, expected {[5, -10, 3, 2, 1]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = rotateRight([7, 1000000, 0], 28)
        assert result == [0, 7, 1000000], f"Test 14 failed: got {result}, expected {[0, 7, 1000000]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = rotateRight([1, 2, 0, -28], 2)
        assert result == [0, -28, 1, 2], f"Test 15 failed: got {result}, expected {[0, -28, 1, 2]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = rotateRight([1, 2, 17], 98)
        assert result == [2, 17, 1], f"Test 16 failed: got {result}, expected {[2, 17, 1]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = rotateRight([-1], 17)
        assert result == [-1], f"Test 17 failed: got {result}, expected {[-1]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = rotateRight([2, 1, 0], 1)
        assert result == [0, 2, 1], f"Test 18 failed: got {result}, expected {[0, 2, 1]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = rotateRight([0, 0, 2, 1], 5)
        assert result == [1, 0, 0, 2], f"Test 19 failed: got {result}, expected {[1, 0, 0, 2]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = rotateRight([0, 2, 1], 20)
        assert result == [2, 1, 0], f"Test 20 failed: got {result}, expected {[2, 1, 0]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = rotateRight([1, 2, 3, 15], 1)
        assert result == [15, 1, 2, 3], f"Test 21 failed: got {result}, expected {[15, 1, 2, 3]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = rotateRight([0, 2, 40], 2147483646)
        assert result == [0, 2, 40], f"Test 22 failed: got {result}, expected {[0, 2, 40]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = rotateRight([-28, 2, 3, 0, -14], 1)
        assert result == [-14, -28, 2, 3, 0], f"Test 23 failed: got {result}, expected {[-14, -28, 2, 3, 0]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = rotateRight([799, 0, 3, 2, 1], 1)
        assert result == [1, 799, 0, 3, 2], f"Test 24 failed: got {result}, expected {[1, 799, 0, 3, 2]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = rotateRight([1, 2, 3], 1000)
        assert result == [3, 1, 2], f"Test 25 failed: got {result}, expected {[3, 1, 2]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = rotateRight([1, 2, 3, 0, 11], 27)
        assert result == [0, 11, 1, 2, 3], f"Test 26 failed: got {result}, expected {[0, 11, 1, 2, 3]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = rotateRight([1, 0, 12345], 301)
        assert result == [12345, 1, 0], f"Test 27 failed: got {result}, expected {[12345, 1, 0]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = rotateRight([1, 2, 3, -3], 1)
        assert result == [-3, 1, 2, 3], f"Test 28 failed: got {result}, expected {[-3, 1, 2, 3]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = rotateRight([0, 5, 2, 1], 1000)
        assert result == [0, 5, 2, 1], f"Test 29 failed: got {result}, expected {[0, 5, 2, 1]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = rotateRight([1, 2, 0, 90, 0], 0)
        assert result == [1, 2, 0, 90, 0], f"Test 30 failed: got {result}, expected {[1, 2, 0, 90, 0]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = rotateRight([1, 2, 3], 13)
        assert result == [3, 1, 2], f"Test 31 failed: got {result}, expected {[3, 1, 2]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = rotateRight([1, 2, 3, 4, 5, 66], 4)
        assert result == [3, 4, 5, 66, 1, 2], f"Test 32 failed: got {result}, expected {[3, 4, 5, 66, 1, 2]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = rotateRight([1, 2, 3, 4, 5], 299)
        assert result == [2, 3, 4, 5, 1], f"Test 33 failed: got {result}, expected {[2, 3, 4, 5, 1]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = rotateRight([1, 2, 3, 4, 5], 9)
        assert result == [2, 3, 4, 5, 1], f"Test 34 failed: got {result}, expected {[2, 3, 4, 5, 1]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = rotateRight([14, 2, 4, 4, 5], 1)
        assert result == [5, 14, 2, 4, 4], f"Test 35 failed: got {result}, expected {[5, 14, 2, 4, 4]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = rotateRight([1, 2, 4, 12], 27)
        assert result == [2, 4, 12, 1], f"Test 36 failed: got {result}, expected {[2, 4, 12, 1]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = rotateRight([0, 0, 0, 1], 499)
        assert result == [0, 0, 1, 0], f"Test 37 failed: got {result}, expected {[0, 0, 1, 0]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = rotateRight([-1, -2, -3, -4], 2)
        assert result == [-3, -4, -1, -2], f"Test 38 failed: got {result}, expected {[-3, -4, -1, -2]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = rotateRight([0, -3, -2, -1, 0], 2)
        assert result == [-1, 0, 0, -3, -2], f"Test 39 failed: got {result}, expected {[-1, 0, 0, -3, -2]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = rotateRight([-1, 1, 1, 0, -1, 0], 8)
        assert result == [-1, 0, -1, 1, 1, 0], f"Test 40 failed: got {result}, expected {[-1, 0, -1, 1, 1, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = rotateRight([-1, 0, 1, 0, -1], 33)
        assert result == [1, 0, -1, -1, 0], f"Test 41 failed: got {result}, expected {[1, 0, -1, -1, 0]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = rotateRight([3, 3, 3, 3, 3, 2002], 9)
        assert result == [3, 3, 2002, 3, 3, 3], f"Test 42 failed: got {result}, expected {[3, 3, 2002, 3, 3, 3]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = rotateRight([1, -1, 999999999], 1)
        assert result == [999999999, 1, -1], f"Test 43 failed: got {result}, expected {[999999999, 1, -1]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = rotateRight([2147483647, -2147483648, -1, -100, 0], 5)
        assert result == [2147483647, -2147483648, -1, -100, 0], f"Test 44 failed: got {result}, expected {[2147483647, -2147483648, -1, -100, 0]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = rotateRight([2147483647, -2147483648, 0], 8)
        assert result == [-2147483648, 0, 2147483647], f"Test 45 failed: got {result}, expected {[-2147483648, 0, 2147483647]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = rotateRight([42, 17, -5, 99, -100, 0, 8, 0], 6)
        assert result == [-5, 99, -100, 0, 8, 0, 42, 17], f"Test 46 failed: got {result}, expected {[-5, 99, -100, 0, 8, 0, 42, 17]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = rotateRight([42, 17, -5, 99, -100, 0, 8], 5)
        assert result == [-5, 99, -100, 0, 8, 42, 17], f"Test 47 failed: got {result}, expected {[-5, 99, -100, 0, 8, 42, 17]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = rotateRight([42, -5, 99, -100, 0, 8, -3], 200)
        assert result == [-100, 0, 8, -3, 42, -5, 99], f"Test 48 failed: got {result}, expected {[-100, 0, 8, -3, 42, -5, 99]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = rotateRight([42, 19, -5, 99, -100, 0, 8], 398)
        assert result == [19, -5, 99, -100, 0, 8, 42], f"Test 49 failed: got {result}, expected {[19, -5, 99, -100, 0, 8, 42]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = rotateRight([42, 17, -5, 99, -100, 0, 8, 0], 9)
        assert result == [0, 42, 17, -5, 99, -100, 0, 8], f"Test 50 failed: got {result}, expected {[0, 42, 17, -5, 99, -100, 0, 8]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = rotateRight([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 99)
        assert result == [9, 8, 7, 6, 5, 4, 3, 2, 1, 10], f"Test 51 failed: got {result}, expected {[9, 8, 7, 6, 5, 4, 3, 2, 1, 10]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = rotateRight([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -5, 198, 0], 997)
        assert result == [6, 5, 4, 3, 2, 1, -5, 198, 0, 10, 9, 8, 7], f"Test 52 failed: got {result}, expected {[6, 5, 4, 3, 2, 1, -5, 198, 0, 10, 9, 8, 7]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = rotateRight([2, 4, 6, 8, 10, 12, 0], 11)
        assert result == [8, 10, 12, 0, 2, 4, 6], f"Test 53 failed: got {result}, expected {[8, 10, 12, 0, 2, 4, 6]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = rotateRight([89, 55, 21, 13, 8, 5, 3, 2, 1, 1], 12345)
        assert result == [5, 3, 2, 1, 1, 89, 55, 21, 13, 8], f"Test 54 failed: got {result}, expected {[5, 3, 2, 1, 1, 89, 55, 21, 13, 8]}"
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
