# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def sumOfSquaresOfFirstNOddNumbers(n):
2: ✓     return (n * (2 * n - 1) * (2 * n + 1)) // 3
```

## Complete Test File

```python
def sumOfSquaresOfFirstNOddNumbers(n):
    return (n * (2 * n - 1) * (2 * n + 1)) // 3

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = sumOfSquaresOfFirstNOddNumbers(0)
        assert result == 0, f"Test 1 failed: got {result}, expected {0}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = sumOfSquaresOfFirstNOddNumbers(1)
        assert result == 1, f"Test 2 failed: got {result}, expected {1}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = sumOfSquaresOfFirstNOddNumbers(2)
        assert result == 10, f"Test 3 failed: got {result}, expected {10}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = sumOfSquaresOfFirstNOddNumbers(3)
        assert result == 35, f"Test 4 failed: got {result}, expected {35}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = sumOfSquaresOfFirstNOddNumbers(4)
        assert result == 84, f"Test 5 failed: got {result}, expected {84}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = sumOfSquaresOfFirstNOddNumbers(5)
        assert result == 165, f"Test 6 failed: got {result}, expected {165}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = sumOfSquaresOfFirstNOddNumbers(10)
        assert result == 1330, f"Test 7 failed: got {result}, expected {1330}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = sumOfSquaresOfFirstNOddNumbers(6)
        assert result == 286, f"Test 8 failed: got {result}, expected {286}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = sumOfSquaresOfFirstNOddNumbers(7)
        assert result == 455, f"Test 9 failed: got {result}, expected {455}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = sumOfSquaresOfFirstNOddNumbers(8)
        assert result == 680, f"Test 10 failed: got {result}, expected {680}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = sumOfSquaresOfFirstNOddNumbers(9)
        assert result == 969, f"Test 11 failed: got {result}, expected {969}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = sumOfSquaresOfFirstNOddNumbers(11)
        assert result == 1771, f"Test 12 failed: got {result}, expected {1771}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = sumOfSquaresOfFirstNOddNumbers(12)
        assert result == 2300, f"Test 13 failed: got {result}, expected {2300}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = sumOfSquaresOfFirstNOddNumbers(13)
        assert result == 2925, f"Test 14 failed: got {result}, expected {2925}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = sumOfSquaresOfFirstNOddNumbers(14)
        assert result == 3654, f"Test 15 failed: got {result}, expected {3654}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = sumOfSquaresOfFirstNOddNumbers(15)
        assert result == 4495, f"Test 16 failed: got {result}, expected {4495}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = sumOfSquaresOfFirstNOddNumbers(16)
        assert result == 5456, f"Test 17 failed: got {result}, expected {5456}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = sumOfSquaresOfFirstNOddNumbers(17)
        assert result == 6545, f"Test 18 failed: got {result}, expected {6545}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = sumOfSquaresOfFirstNOddNumbers(18)
        assert result == 7770, f"Test 19 failed: got {result}, expected {7770}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = sumOfSquaresOfFirstNOddNumbers(19)
        assert result == 9139, f"Test 20 failed: got {result}, expected {9139}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = sumOfSquaresOfFirstNOddNumbers(20)
        assert result == 10660, f"Test 21 failed: got {result}, expected {10660}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = sumOfSquaresOfFirstNOddNumbers(21)
        assert result == 12341, f"Test 22 failed: got {result}, expected {12341}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = sumOfSquaresOfFirstNOddNumbers(22)
        assert result == 14190, f"Test 23 failed: got {result}, expected {14190}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = sumOfSquaresOfFirstNOddNumbers(23)
        assert result == 16215, f"Test 24 failed: got {result}, expected {16215}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = sumOfSquaresOfFirstNOddNumbers(24)
        assert result == 18424, f"Test 25 failed: got {result}, expected {18424}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = sumOfSquaresOfFirstNOddNumbers(25)
        assert result == 20825, f"Test 26 failed: got {result}, expected {20825}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = sumOfSquaresOfFirstNOddNumbers(30)
        assert result == 35990, f"Test 27 failed: got {result}, expected {35990}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = sumOfSquaresOfFirstNOddNumbers(31)
        assert result == 39711, f"Test 28 failed: got {result}, expected {39711}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = sumOfSquaresOfFirstNOddNumbers(32)
        assert result == 43680, f"Test 29 failed: got {result}, expected {43680}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = sumOfSquaresOfFirstNOddNumbers(33)
        assert result == 47905, f"Test 30 failed: got {result}, expected {47905}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = sumOfSquaresOfFirstNOddNumbers(50)
        assert result == 166650, f"Test 31 failed: got {result}, expected {166650}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = sumOfSquaresOfFirstNOddNumbers(64)
        assert result == 349504, f"Test 32 failed: got {result}, expected {349504}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = sumOfSquaresOfFirstNOddNumbers(100)
        assert result == 1333300, f"Test 33 failed: got {result}, expected {1333300}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = sumOfSquaresOfFirstNOddNumbers(999)
        assert result == 1329336999, f"Test 34 failed: got {result}, expected {1329336999}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = sumOfSquaresOfFirstNOddNumbers(1000)
        assert result == 1333333000, f"Test 35 failed: got {result}, expected {1333333000}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = sumOfSquaresOfFirstNOddNumbers(10000)
        assert result == 1333333330000, f"Test 36 failed: got {result}, expected {1333333330000}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = sumOfSquaresOfFirstNOddNumbers(65535)
        assert result == 375282789318655, f"Test 37 failed: got {result}, expected {375282789318655}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = sumOfSquaresOfFirstNOddNumbers(27)
        assert result == 26235, f"Test 38 failed: got {result}, expected {26235}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = sumOfSquaresOfFirstNOddNumbers(26)
        assert result == 23426, f"Test 39 failed: got {result}, expected {23426}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = sumOfSquaresOfFirstNOddNumbers(51)
        assert result == 176851, f"Test 40 failed: got {result}, expected {176851}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = sumOfSquaresOfFirstNOddNumbers(255)
        assert result == 22108415, f"Test 41 failed: got {result}, expected {22108415}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = sumOfSquaresOfFirstNOddNumbers(998)
        assert result == 1325348990, f"Test 42 failed: got {result}, expected {1325348990}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = sumOfSquaresOfFirstNOddNumbers(34)
        assert result == 52394, f"Test 43 failed: got {result}, expected {52394}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = sumOfSquaresOfFirstNOddNumbers(60)
        assert result == 287980, f"Test 44 failed: got {result}, expected {287980}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = sumOfSquaresOfFirstNOddNumbers(48)
        assert result == 147440, f"Test 45 failed: got {result}, expected {147440}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = sumOfSquaresOfFirstNOddNumbers(39)
        assert result == 79079, f"Test 46 failed: got {result}, expected {79079}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = sumOfSquaresOfFirstNOddNumbers(116)
        assert result == 2081156, f"Test 47 failed: got {result}, expected {2081156}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = sumOfSquaresOfFirstNOddNumbers(40)
        assert result == 85320, f"Test 48 failed: got {result}, expected {85320}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = sumOfSquaresOfFirstNOddNumbers(997)
        assert result == 1321368965, f"Test 49 failed: got {result}, expected {1321368965}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = sumOfSquaresOfFirstNOddNumbers(120)
        assert result == 2303960, f"Test 50 failed: got {result}, expected {2303960}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = sumOfSquaresOfFirstNOddNumbers(35)
        assert result == 57155, f"Test 51 failed: got {result}, expected {57155}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = sumOfSquaresOfFirstNOddNumbers(97)
        assert result == 1216865, f"Test 52 failed: got {result}, expected {1216865}"
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
