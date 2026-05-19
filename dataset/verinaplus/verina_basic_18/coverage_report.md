# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def sumOfDigits(n):
2: ✓     return sum(int(digit) for digit in str(n))
```

## Complete Test File

```python
def sumOfDigits(n):
    return sum(int(digit) for digit in str(n))

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = sumOfDigits(12345)
        assert result == 15, f"Test 1 failed: got {result}, expected {15}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = sumOfDigits(0)
        assert result == 0, f"Test 2 failed: got {result}, expected {0}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = sumOfDigits(987654321)
        assert result == 45, f"Test 3 failed: got {result}, expected {45}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = sumOfDigits(11111)
        assert result == 5, f"Test 4 failed: got {result}, expected {5}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = sumOfDigits(1001)
        assert result == 2, f"Test 5 failed: got {result}, expected {2}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = sumOfDigits(9999)
        assert result == 36, f"Test 6 failed: got {result}, expected {36}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = sumOfDigits(1)
        assert result == 1, f"Test 7 failed: got {result}, expected {1}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = sumOfDigits(2)
        assert result == 2, f"Test 8 failed: got {result}, expected {2}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = sumOfDigits(5)
        assert result == 5, f"Test 9 failed: got {result}, expected {5}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = sumOfDigits(9)
        assert result == 9, f"Test 10 failed: got {result}, expected {9}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = sumOfDigits(10)
        assert result == 1, f"Test 11 failed: got {result}, expected {1}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = sumOfDigits(11)
        assert result == 2, f"Test 12 failed: got {result}, expected {2}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = sumOfDigits(19)
        assert result == 10, f"Test 13 failed: got {result}, expected {10}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = sumOfDigits(20)
        assert result == 2, f"Test 14 failed: got {result}, expected {2}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = sumOfDigits(21)
        assert result == 3, f"Test 15 failed: got {result}, expected {3}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = sumOfDigits(99)
        assert result == 18, f"Test 16 failed: got {result}, expected {18}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = sumOfDigits(100)
        assert result == 1, f"Test 17 failed: got {result}, expected {1}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = sumOfDigits(101)
        assert result == 2, f"Test 18 failed: got {result}, expected {2}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = sumOfDigits(109)
        assert result == 10, f"Test 19 failed: got {result}, expected {10}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = sumOfDigits(110)
        assert result == 2, f"Test 20 failed: got {result}, expected {2}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = sumOfDigits(909)
        assert result == 18, f"Test 21 failed: got {result}, expected {18}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = sumOfDigits(990)
        assert result == 18, f"Test 22 failed: got {result}, expected {18}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = sumOfDigits(999)
        assert result == 27, f"Test 23 failed: got {result}, expected {27}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = sumOfDigits(1000)
        assert result == 1, f"Test 24 failed: got {result}, expected {1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = sumOfDigits(1009)
        assert result == 10, f"Test 25 failed: got {result}, expected {10}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = sumOfDigits(1010)
        assert result == 2, f"Test 26 failed: got {result}, expected {2}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = sumOfDigits(1099)
        assert result == 19, f"Test 27 failed: got {result}, expected {19}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = sumOfDigits(1100)
        assert result == 2, f"Test 28 failed: got {result}, expected {2}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = sumOfDigits(54321)
        assert result == 15, f"Test 29 failed: got {result}, expected {15}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = sumOfDigits(111111111)
        assert result == 9, f"Test 30 failed: got {result}, expected {9}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = sumOfDigits(1000000000)
        assert result == 1, f"Test 31 failed: got {result}, expected {1}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = sumOfDigits(2147483647)
        assert result == 46, f"Test 32 failed: got {result}, expected {46}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = sumOfDigits(4294967295)
        assert result == 57, f"Test 33 failed: got {result}, expected {57}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = sumOfDigits(9223372036854775807)
        assert result == 88, f"Test 34 failed: got {result}, expected {88}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = sumOfDigits(18446744073709551615)
        assert result == 87, f"Test 35 failed: got {result}, expected {87}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = sumOfDigits(99999999999999999999)
        assert result == 180, f"Test 36 failed: got {result}, expected {180}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = sumOfDigits(100000000000000000000)
        assert result == 1, f"Test 37 failed: got {result}, expected {1}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = sumOfDigits(123456789012345678901234567890)
        assert result == 135, f"Test 38 failed: got {result}, expected {135}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = sumOfDigits(999999999999999999999999999999999999)
        assert result == 324, f"Test 39 failed: got {result}, expected {324}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = sumOfDigits(1000000000000000000000000000000000000)
        assert result == 1, f"Test 40 failed: got {result}, expected {1}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = sumOfDigits(3141592653589793238462643383279502884)
        assert result == 177, f"Test 41 failed: got {result}, expected {177}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = sumOfDigits(2718281828459045235360287471352662497)
        assert result == 166, f"Test 42 failed: got {result}, expected {166}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = sumOfDigits(12346)
        assert result == 16, f"Test 43 failed: got {result}, expected {16}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = sumOfDigits(12)
        assert result == 3, f"Test 44 failed: got {result}, expected {3}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = sumOfDigits(11110)
        assert result == 4, f"Test 45 failed: got {result}, expected {4}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = sumOfDigits(2718281828459045235360287471352662493)
        assert result == 162, f"Test 46 failed: got {result}, expected {162}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = sumOfDigits(13)
        assert result == 4, f"Test 47 failed: got {result}, expected {4}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = sumOfDigits(1999999996)
        assert result == 79, f"Test 48 failed: got {result}, expected {79}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = sumOfDigits(2147483646)
        assert result == 45, f"Test 49 failed: got {result}, expected {45}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = sumOfDigits(1975308643)
        assert result == 46, f"Test 50 failed: got {result}, expected {46}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = sumOfDigits(1008)
        assert result == 9, f"Test 51 failed: got {result}, expected {9}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = sumOfDigits(2018)
        assert result == 11, f"Test 52 failed: got {result}, expected {11}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = sumOfDigits(987654323)
        assert result == 47, f"Test 53 failed: got {result}, expected {47}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = sumOfDigits(40)
        assert result == 4, f"Test 54 failed: got {result}, expected {4}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = sumOfDigits(5436563656918090470720574942705324998)
        assert result == 174, f"Test 55 failed: got {result}, expected {174}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = sumOfDigits(24690)
        assert result == 21, f"Test 56 failed: got {result}, expected {21}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = sumOfDigits(2718281828459045235360287471352662496)
        assert result == 165, f"Test 57 failed: got {result}, expected {165}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = sumOfDigits(16)
        assert result == 7, f"Test 58 failed: got {result}, expected {7}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = sumOfDigits(17)
        assert result == 8, f"Test 59 failed: got {result}, expected {8}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = sumOfDigits(19996)
        assert result == 34, f"Test 60 failed: got {result}, expected {34}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = sumOfDigits(39994)
        assert result == 34, f"Test 61 failed: got {result}, expected {34}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = sumOfDigits(908)
        assert result == 17, f"Test 62 failed: got {result}, expected {17}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = sumOfDigits(9998)
        assert result == 35, f"Test 63 failed: got {result}, expected {35}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = sumOfDigits(19998)
        assert result == 36, f"Test 64 failed: got {result}, expected {36}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = sumOfDigits(26)
        assert result == 8, f"Test 65 failed: got {result}, expected {8}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = sumOfDigits(49380)
        assert result == 24, f"Test 66 failed: got {result}, expected {24}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = sumOfDigits(3)
        assert result == 3, f"Test 67 failed: got {result}, expected {3}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = sumOfDigits(4)
        assert result == 4, f"Test 68 failed: got {result}, expected {4}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = sumOfDigits(6)
        assert result == 6, f"Test 69 failed: got {result}, expected {6}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = sumOfDigits(7)
        assert result == 7, f"Test 70 failed: got {result}, expected {7}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = sumOfDigits(218)
        assert result == 11, f"Test 71 failed: got {result}, expected {11}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = sumOfDigits(12343)
        assert result == 13, f"Test 72 failed: got {result}, expected {13}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = sumOfDigits(24691)
        assert result == 22, f"Test 73 failed: got {result}, expected {22}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = sumOfDigits(111111110)
        assert result == 8, f"Test 74 failed: got {result}, expected {8}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = sumOfDigits(20000)
        assert result == 2, f"Test 75 failed: got {result}, expected {2}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = sumOfDigits(219)
        assert result == 12, f"Test 76 failed: got {result}, expected {12}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = sumOfDigits(14)
        assert result == 5, f"Test 77 failed: got {result}, expected {5}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = sumOfDigits(9223372036854775806)
        assert result == 87, f"Test 78 failed: got {result}, expected {87}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = sumOfDigits(220)
        assert result == 4, f"Test 79 failed: got {result}, expected {4}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = sumOfDigits(1818)
        assert result == 18, f"Test 80 failed: got {result}, expected {18}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = sumOfDigits(18)
        assert result == 9, f"Test 81 failed: got {result}, expected {9}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = sumOfDigits(8)
        assert result == 8, f"Test 82 failed: got {result}, expected {8}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = sumOfDigits(41)
        assert result == 5, f"Test 83 failed: got {result}, expected {5}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = sumOfDigits(5436563656918090470720574942705324997)
        assert result == 173, f"Test 84 failed: got {result}, expected {173}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = sumOfDigits(440)
        assert result == 8, f"Test 85 failed: got {result}, expected {8}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = sumOfDigits(2147483645)
        assert result == 44, f"Test 86 failed: got {result}, expected {44}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = sumOfDigits(198)
        assert result == 18, f"Test 87 failed: got {result}, expected {18}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = sumOfDigits(99999999999999999998)
        assert result == 179, f"Test 88 failed: got {result}, expected {179}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = sumOfDigits(4294967294)
        assert result == 56, f"Test 89 failed: got {result}, expected {56}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = sumOfDigits(2000000000000000000000000000000000002)
        assert result == 4, f"Test 90 failed: got {result}, expected {4}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = sumOfDigits(202)
        assert result == 4, f"Test 91 failed: got {result}, expected {4}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = sumOfDigits(19999)
        assert result == 37, f"Test 92 failed: got {result}, expected {37}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = sumOfDigits(439)
        assert result == 16, f"Test 93 failed: got {result}, expected {16}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = sumOfDigits(438)
        assert result == 15, f"Test 94 failed: got {result}, expected {15}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = sumOfDigits(112)
        assert result == 4, f"Test 95 failed: got {result}, expected {4}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = sumOfDigits(81)
        assert result == 9, f"Test 96 failed: got {result}, expected {9}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = sumOfDigits(108)
        assert result == 9, f"Test 97 failed: got {result}, expected {9}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = sumOfDigits(910)
        assert result == 10, f"Test 98 failed: got {result}, expected {10}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = sumOfDigits(989)
        assert result == 26, f"Test 99 failed: got {result}, expected {26}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = sumOfDigits(24689)
        assert result == 29, f"Test 100 failed: got {result}, expected {29}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = sumOfDigits(991)
        assert result == 19, f"Test 101 failed: got {result}, expected {19}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = sumOfDigits(113)
        assert result == 5, f"Test 102 failed: got {result}, expected {5}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = sumOfDigits(4294967293)
        assert result == 55, f"Test 103 failed: got {result}, expected {55}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = sumOfDigits(998)
        assert result == 26, f"Test 104 failed: got {result}, expected {26}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = sumOfDigits(3950617286)
        assert result == 47, f"Test 105 failed: got {result}, expected {47}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = sumOfDigits(99999999999999999996)
        assert result == 177, f"Test 106 failed: got {result}, expected {177}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = sumOfDigits(8589934588)
        assert result == 67, f"Test 107 failed: got {result}, expected {67}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = sumOfDigits(222)
        assert result == 6, f"Test 108 failed: got {result}, expected {6}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = sumOfDigits(1011)
        assert result == 3, f"Test 109 failed: got {result}, expected {3}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = sumOfDigits(1980)
        assert result == 18, f"Test 110 failed: got {result}, expected {18}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = sumOfDigits(38)
        assert result == 11, f"Test 111 failed: got {result}, expected {11}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = sumOfDigits(2198)
        assert result == 20, f"Test 112 failed: got {result}, expected {20}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = sumOfDigits(1098)
        assert result == 18, f"Test 113 failed: got {result}, expected {18}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = sumOfDigits(1101)
        assert result == 3, f"Test 114 failed: got {result}, expected {3}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = sumOfDigits(880)
        assert result == 16, f"Test 115 failed: got {result}, expected {16}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = sumOfDigits(444444444)
        assert result == 36, f"Test 116 failed: got {result}, expected {36}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = sumOfDigits(999999999)
        assert result == 81, f"Test 117 failed: got {result}, expected {81}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = sumOfDigits(1000000001)
        assert result == 2, f"Test 118 failed: got {result}, expected {2}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = sumOfDigits(9223372036854775805)
        assert result == 86, f"Test 119 failed: got {result}, expected {86}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = sumOfDigits(2147483648)
        assert result == 47, f"Test 120 failed: got {result}, expected {47}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = sumOfDigits(2718281828459045235360287471352662492)
        assert result == 161, f"Test 121 failed: got {result}, expected {161}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = sumOfDigits(34359738356)
        assert result == 56, f"Test 122 failed: got {result}, expected {56}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = sumOfDigits(987654324)
        assert result == 48, f"Test 123 failed: got {result}, expected {48}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = sumOfDigits(5436563656918090470720574942705324999)
        assert result == 175, f"Test 124 failed: got {result}, expected {175}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = sumOfDigits(1975308642)
        assert result == 45, f"Test 125 failed: got {result}, expected {45}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = sumOfDigits(54322)
        assert result == 16, f"Test 126 failed: got {result}, expected {16}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = sumOfDigits(1982)
        assert result == 20, f"Test 127 failed: got {result}, expected {20}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = sumOfDigits(80)
        assert result == 8, f"Test 128 failed: got {result}, expected {8}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = sumOfDigits(4294967296)
        assert result == 58, f"Test 129 failed: got {result}, expected {58}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = sumOfDigits(879)
        assert result == 24, f"Test 130 failed: got {result}, expected {24}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = sumOfDigits(1999999999999999999999999999999999998)
        assert result == 324, f"Test 131 failed: got {result}, expected {324}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = sumOfDigits(12342)
        assert result == 12, f"Test 132 failed: got {result}, expected {12}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = sumOfDigits(1000000000000000000000000000000000002)
        assert result == 3, f"Test 133 failed: got {result}, expected {3}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = sumOfDigits(8589934589)
        assert result == 68, f"Test 134 failed: got {result}, expected {68}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = sumOfDigits(1006)
        assert result == 7, f"Test 135 failed: got {result}, expected {7}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = sumOfDigits(42)
        assert result == 6, f"Test 136 failed: got {result}, expected {6}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = sumOfDigits(987654325)
        assert result == 49, f"Test 137 failed: got {result}, expected {49}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = sumOfDigits(5436563656918090470720574942705324988)
        assert result == 173, f"Test 138 failed: got {result}, expected {173}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = sumOfDigits(10000)
        assert result == 1, f"Test 139 failed: got {result}, expected {1}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = sumOfDigits(5436563656918090470720574942705324994)
        assert result == 170, f"Test 140 failed: got {result}, expected {170}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = sumOfDigits(23)
        assert result == 5, f"Test 141 failed: got {result}, expected {5}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
