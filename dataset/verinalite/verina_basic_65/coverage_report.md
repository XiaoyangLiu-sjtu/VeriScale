# Coverage Report

Total executable lines: 6
Covered lines: 6
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def SquareRoot(N):
2: ✓     def helper(r):
3: ✓         if (r + 1) * (r + 1) > N:
4: ✓             return r
5: ✓         return helper(r + 1)
6: ✓     return helper(0)
```

## Complete Test File

```python
def SquareRoot(N):
    def helper(r):
        if (r + 1) * (r + 1) > N:
            return r
        return helper(r + 1)
    return helper(0)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = SquareRoot(0)
        assert result == 0, f"Test 1 failed: got {result}, expected {0}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = SquareRoot(1)
        assert result == 1, f"Test 2 failed: got {result}, expected {1}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = SquareRoot(15)
        assert result == 3, f"Test 3 failed: got {result}, expected {3}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = SquareRoot(16)
        assert result == 4, f"Test 4 failed: got {result}, expected {4}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = SquareRoot(26)
        assert result == 5, f"Test 5 failed: got {result}, expected {5}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = SquareRoot(8)
        assert result == 2, f"Test 6 failed: got {result}, expected {2}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = SquareRoot(9)
        assert result == 3, f"Test 7 failed: got {result}, expected {3}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = SquareRoot(10)
        assert result == 3, f"Test 8 failed: got {result}, expected {3}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = SquareRoot(17)
        assert result == 4, f"Test 9 failed: got {result}, expected {4}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = SquareRoot(24)
        assert result == 4, f"Test 10 failed: got {result}, expected {4}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = SquareRoot(25)
        assert result == 5, f"Test 11 failed: got {result}, expected {5}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = SquareRoot(35)
        assert result == 5, f"Test 12 failed: got {result}, expected {5}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = SquareRoot(36)
        assert result == 6, f"Test 13 failed: got {result}, expected {6}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = SquareRoot(37)
        assert result == 6, f"Test 14 failed: got {result}, expected {6}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = SquareRoot(48)
        assert result == 6, f"Test 15 failed: got {result}, expected {6}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = SquareRoot(49)
        assert result == 7, f"Test 16 failed: got {result}, expected {7}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = SquareRoot(50)
        assert result == 7, f"Test 17 failed: got {result}, expected {7}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = SquareRoot(63)
        assert result == 7, f"Test 18 failed: got {result}, expected {7}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = SquareRoot(64)
        assert result == 8, f"Test 19 failed: got {result}, expected {8}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = SquareRoot(65)
        assert result == 8, f"Test 20 failed: got {result}, expected {8}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = SquareRoot(80)
        assert result == 8, f"Test 21 failed: got {result}, expected {8}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = SquareRoot(81)
        assert result == 9, f"Test 22 failed: got {result}, expected {9}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = SquareRoot(82)
        assert result == 9, f"Test 23 failed: got {result}, expected {9}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = SquareRoot(99)
        assert result == 9, f"Test 24 failed: got {result}, expected {9}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = SquareRoot(100)
        assert result == 10, f"Test 25 failed: got {result}, expected {10}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = SquareRoot(101)
        assert result == 10, f"Test 26 failed: got {result}, expected {10}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = SquareRoot(255)
        assert result == 15, f"Test 27 failed: got {result}, expected {15}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = SquareRoot(256)
        assert result == 16, f"Test 28 failed: got {result}, expected {16}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = SquareRoot(257)
        assert result == 16, f"Test 29 failed: got {result}, expected {16}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = SquareRoot(1023)
        assert result == 31, f"Test 30 failed: got {result}, expected {31}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = SquareRoot(1024)
        assert result == 32, f"Test 31 failed: got {result}, expected {32}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = SquareRoot(1025)
        assert result == 32, f"Test 32 failed: got {result}, expected {32}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = SquareRoot(18)
        assert result == 4, f"Test 33 failed: got {result}, expected {4}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = SquareRoot(44)
        assert result == 6, f"Test 34 failed: got {result}, expected {6}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = SquareRoot(19)
        assert result == 4, f"Test 35 failed: got {result}, expected {4}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = SquareRoot(20)
        assert result == 4, f"Test 36 failed: got {result}, expected {4}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = SquareRoot(45)
        assert result == 6, f"Test 37 failed: got {result}, expected {6}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = SquareRoot(34)
        assert result == 5, f"Test 38 failed: got {result}, expected {5}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = SquareRoot(13)
        assert result == 3, f"Test 39 failed: got {result}, expected {3}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = SquareRoot(2047)
        assert result == 45, f"Test 40 failed: got {result}, expected {45}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = SquareRoot(199)
        assert result == 14, f"Test 41 failed: got {result}, expected {14}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = SquareRoot(162)
        assert result == 12, f"Test 42 failed: got {result}, expected {12}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = SquareRoot(125)
        assert result == 11, f"Test 43 failed: got {result}, expected {11}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = SquareRoot(6)
        assert result == 2, f"Test 44 failed: got {result}, expected {2}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = SquareRoot(514)
        assert result == 22, f"Test 45 failed: got {result}, expected {22}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = SquareRoot(258)
        assert result == 16, f"Test 46 failed: got {result}, expected {16}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = SquareRoot(1028)
        assert result == 32, f"Test 47 failed: got {result}, expected {32}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = SquareRoot(32)
        assert result == 5, f"Test 48 failed: got {result}, expected {5}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = SquareRoot(127)
        assert result == 11, f"Test 49 failed: got {result}, expected {11}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = SquareRoot(7)
        assert result == 2, f"Test 50 failed: got {result}, expected {2}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = SquareRoot(86)
        assert result == 9, f"Test 51 failed: got {result}, expected {9}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = SquareRoot(198)
        assert result == 14, f"Test 52 failed: got {result}, expected {14}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
