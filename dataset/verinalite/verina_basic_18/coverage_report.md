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
        result = sumOfDigits(101)
        assert result == 2, f"Test 7 failed: got {result}, expected {2}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = sumOfDigits(109)
        assert result == 10, f"Test 8 failed: got {result}, expected {10}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = sumOfDigits(110)
        assert result == 2, f"Test 9 failed: got {result}, expected {2}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = sumOfDigits(909)
        assert result == 18, f"Test 10 failed: got {result}, expected {18}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = sumOfDigits(990)
        assert result == 18, f"Test 11 failed: got {result}, expected {18}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = sumOfDigits(999)
        assert result == 27, f"Test 12 failed: got {result}, expected {27}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = sumOfDigits(1009)
        assert result == 10, f"Test 13 failed: got {result}, expected {10}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = sumOfDigits(1010)
        assert result == 2, f"Test 14 failed: got {result}, expected {2}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = sumOfDigits(1099)
        assert result == 19, f"Test 15 failed: got {result}, expected {19}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = sumOfDigits(1100)
        assert result == 2, f"Test 16 failed: got {result}, expected {2}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = sumOfDigits(54321)
        assert result == 15, f"Test 17 failed: got {result}, expected {15}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = sumOfDigits(111111111)
        assert result == 9, f"Test 18 failed: got {result}, expected {9}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = sumOfDigits(2147483647)
        assert result == 46, f"Test 19 failed: got {result}, expected {46}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = sumOfDigits(4294967295)
        assert result == 57, f"Test 20 failed: got {result}, expected {57}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = sumOfDigits(9223372036854775807)
        assert result == 88, f"Test 21 failed: got {result}, expected {88}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = sumOfDigits(18446744073709551615)
        assert result == 87, f"Test 22 failed: got {result}, expected {87}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = sumOfDigits(99999999999999999999)
        assert result == 180, f"Test 23 failed: got {result}, expected {180}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = sumOfDigits(123456789012345678901234567890)
        assert result == 135, f"Test 24 failed: got {result}, expected {135}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = sumOfDigits(999999999999999999999999999999999999)
        assert result == 324, f"Test 25 failed: got {result}, expected {324}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = sumOfDigits(3141592653589793238462643383279502884)
        assert result == 177, f"Test 26 failed: got {result}, expected {177}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = sumOfDigits(2718281828459045235360287471352662497)
        assert result == 166, f"Test 27 failed: got {result}, expected {166}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = sumOfDigits(12346)
        assert result == 16, f"Test 28 failed: got {result}, expected {16}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = sumOfDigits(11110)
        assert result == 4, f"Test 29 failed: got {result}, expected {4}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = sumOfDigits(2718281828459045235360287471352662493)
        assert result == 162, f"Test 30 failed: got {result}, expected {162}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = sumOfDigits(1999999996)
        assert result == 79, f"Test 31 failed: got {result}, expected {79}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = sumOfDigits(2147483646)
        assert result == 45, f"Test 32 failed: got {result}, expected {45}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = sumOfDigits(1975308643)
        assert result == 46, f"Test 33 failed: got {result}, expected {46}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = sumOfDigits(1008)
        assert result == 9, f"Test 34 failed: got {result}, expected {9}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = sumOfDigits(2018)
        assert result == 11, f"Test 35 failed: got {result}, expected {11}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = sumOfDigits(987654323)
        assert result == 47, f"Test 36 failed: got {result}, expected {47}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = sumOfDigits(5436563656918090470720574942705324998)
        assert result == 174, f"Test 37 failed: got {result}, expected {174}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = sumOfDigits(24690)
        assert result == 21, f"Test 38 failed: got {result}, expected {21}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = sumOfDigits(2718281828459045235360287471352662496)
        assert result == 165, f"Test 39 failed: got {result}, expected {165}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = sumOfDigits(19996)
        assert result == 34, f"Test 40 failed: got {result}, expected {34}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = sumOfDigits(39994)
        assert result == 34, f"Test 41 failed: got {result}, expected {34}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = sumOfDigits(908)
        assert result == 17, f"Test 42 failed: got {result}, expected {17}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = sumOfDigits(9998)
        assert result == 35, f"Test 43 failed: got {result}, expected {35}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = sumOfDigits(19998)
        assert result == 36, f"Test 44 failed: got {result}, expected {36}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = sumOfDigits(49380)
        assert result == 24, f"Test 45 failed: got {result}, expected {24}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = sumOfDigits(218)
        assert result == 11, f"Test 46 failed: got {result}, expected {11}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = sumOfDigits(12343)
        assert result == 13, f"Test 47 failed: got {result}, expected {13}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = sumOfDigits(24691)
        assert result == 22, f"Test 48 failed: got {result}, expected {22}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = sumOfDigits(111111110)
        assert result == 8, f"Test 49 failed: got {result}, expected {8}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = sumOfDigits(20000)
        assert result == 2, f"Test 50 failed: got {result}, expected {2}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = sumOfDigits(219)
        assert result == 12, f"Test 51 failed: got {result}, expected {12}"
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
