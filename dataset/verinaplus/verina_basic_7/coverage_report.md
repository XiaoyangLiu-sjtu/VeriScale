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

    # Test case 53
    try:
        result = sumOfSquaresOfFirstNOddNumbers(1002)
        assert result == 1341349010, f"Test 53 failed: got {result}, expected {1341349010}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = sumOfSquaresOfFirstNOddNumbers(47)
        assert result == 138415, f"Test 54 failed: got {result}, expected {138415}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = sumOfSquaresOfFirstNOddNumbers(54)
        assert result == 209934, f"Test 55 failed: got {result}, expected {209934}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = sumOfSquaresOfFirstNOddNumbers(96)
        assert result == 1179616, f"Test 56 failed: got {result}, expected {1179616}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = sumOfSquaresOfFirstNOddNumbers(36)
        assert result == 62196, f"Test 57 failed: got {result}, expected {62196}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = sumOfSquaresOfFirstNOddNumbers(38)
        assert result == 73150, f"Test 58 failed: got {result}, expected {73150}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = sumOfSquaresOfFirstNOddNumbers(115)
        assert result == 2027795, f"Test 59 failed: got {result}, expected {2027795}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = sumOfSquaresOfFirstNOddNumbers(1001)
        assert result == 1337337001, f"Test 60 failed: got {result}, expected {1337337001}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = sumOfSquaresOfFirstNOddNumbers(230)
        assert result == 16222590, f"Test 61 failed: got {result}, expected {16222590}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = sumOfSquaresOfFirstNOddNumbers(231)
        assert result == 16435111, f"Test 62 failed: got {result}, expected {16435111}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = sumOfSquaresOfFirstNOddNumbers(29)
        assert result == 32509, f"Test 63 failed: got {result}, expected {32509}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = sumOfSquaresOfFirstNOddNumbers(257)
        assert result == 22632705, f"Test 64 failed: got {result}, expected {22632705}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = sumOfSquaresOfFirstNOddNumbers(41)
        assert result == 91881, f"Test 65 failed: got {result}, expected {91881}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = sumOfSquaresOfFirstNOddNumbers(232)
        assert result == 16649480, f"Test 66 failed: got {result}, expected {16649480}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = sumOfSquaresOfFirstNOddNumbers(200)
        assert result == 10666600, f"Test 67 failed: got {result}, expected {10666600}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = sumOfSquaresOfFirstNOddNumbers(129)
        assert result == 2862209, f"Test 68 failed: got {result}, expected {2862209}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = sumOfSquaresOfFirstNOddNumbers(63)
        assert result == 333375, f"Test 69 failed: got {result}, expected {333375}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = sumOfSquaresOfFirstNOddNumbers(508)
        assert result == 174795180, f"Test 70 failed: got {result}, expected {174795180}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = sumOfSquaresOfFirstNOddNumbers(53)
        assert result == 198485, f"Test 71 failed: got {result}, expected {198485}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = sumOfSquaresOfFirstNOddNumbers(68)
        assert result == 419220, f"Test 72 failed: got {result}, expected {419220}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = sumOfSquaresOfFirstNOddNumbers(510)
        assert result == 176867830, f"Test 73 failed: got {result}, expected {176867830}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = sumOfSquaresOfFirstNOddNumbers(1998)
        assert result == 10634697990, f"Test 74 failed: got {result}, expected {10634697990}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = sumOfSquaresOfFirstNOddNumbers(20000)
        assert result == 10666666660000, f"Test 75 failed: got {result}, expected {10666666660000}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = sumOfSquaresOfFirstNOddNumbers(102)
        assert result == 1414910, f"Test 76 failed: got {result}, expected {1414910}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = sumOfSquaresOfFirstNOddNumbers(70)
        assert result == 457310, f"Test 77 failed: got {result}, expected {457310}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = sumOfSquaresOfFirstNOddNumbers(1021)
        assert result == 1419109341, f"Test 78 failed: got {result}, expected {1419109341}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = sumOfSquaresOfFirstNOddNumbers(128)
        assert result == 2796160, f"Test 79 failed: got {result}, expected {2796160}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
