# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def SwapArithmetic(X, Y):
2: ✓     return (Y, X)
```

## Complete Test File

```python
def SwapArithmetic(X, Y):
    return (Y, X)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = SwapArithmetic(3, 4)
        assert result == (4, 3), f"Test 1 failed: got {result}, expected {(4, 3)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = SwapArithmetic(-1, 10)
        assert result == (10, -1), f"Test 2 failed: got {result}, expected {(10, -1)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = SwapArithmetic(0, 0)
        assert result == (0, 0), f"Test 3 failed: got {result}, expected {(0, 0)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = SwapArithmetic(100, 50)
        assert result == (50, 100), f"Test 4 failed: got {result}, expected {(50, 100)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = SwapArithmetic(-5, -10)
        assert result == (-10, -5), f"Test 5 failed: got {result}, expected {(-10, -5)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = SwapArithmetic(2, 1)
        assert result == (1, 2), f"Test 6 failed: got {result}, expected {(1, 2)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = SwapArithmetic(9223372036854775807, -9223372036854775808)
        assert result == (-9223372036854775808, 9223372036854775807), f"Test 7 failed: got {result}, expected {(-9223372036854775808, 9223372036854775807)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = SwapArithmetic(-1000000000000, 1000000000000)
        assert result == (1000000000000, -1000000000000), f"Test 8 failed: got {result}, expected {(1000000000000, -1000000000000)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = SwapArithmetic(-3141592653589793, -2718281828459045)
        assert result == (-2718281828459045, -3141592653589793), f"Test 9 failed: got {result}, expected {(-2718281828459045, -3141592653589793)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = SwapArithmetic(-8080, 9090)
        assert result == (9090, -8080), f"Test 10 failed: got {result}, expected {(9090, -8080)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = SwapArithmetic(-1, 4)
        assert result == (4, -1), f"Test 11 failed: got {result}, expected {(4, -1)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = SwapArithmetic(2, 4)
        assert result == (4, 2), f"Test 12 failed: got {result}, expected {(4, 2)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = SwapArithmetic(-1, 5)
        assert result == (5, -1), f"Test 13 failed: got {result}, expected {(5, -1)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = SwapArithmetic(0, -123456789012345678901234567890)
        assert result == (-123456789012345678901234567890, 0), f"Test 14 failed: got {result}, expected {(-123456789012345678901234567890, 0)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = SwapArithmetic(-3, 3)
        assert result == (3, -3), f"Test 15 failed: got {result}, expected {(3, -3)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = SwapArithmetic(-2, -3141592653589793)
        assert result == (-3141592653589793, -2), f"Test 16 failed: got {result}, expected {(-3141592653589793, -2)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = SwapArithmetic(1, 10)
        assert result == (10, 1), f"Test 17 failed: got {result}, expected {(10, 1)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = SwapArithmetic(2, -2)
        assert result == (-2, 2), f"Test 18 failed: got {result}, expected {(-2, 2)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = SwapArithmetic(0, 456)
        assert result == (456, 0), f"Test 19 failed: got {result}, expected {(456, 0)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = SwapArithmetic(-3, 2718281828459044)
        assert result == (2718281828459044, -3), f"Test 20 failed: got {result}, expected {(2718281828459044, -3)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = SwapArithmetic(6283185307179586, -123456789012345678901234567890)
        assert result == (-123456789012345678901234567890, 6283185307179586), f"Test 21 failed: got {result}, expected {(-123456789012345678901234567890, 6283185307179586)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = SwapArithmetic(6283185307179586, 50)
        assert result == (50, 6283185307179586), f"Test 22 failed: got {result}, expected {(50, 6283185307179586)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = SwapArithmetic(-100, 0)
        assert result == (0, -100), f"Test 23 failed: got {result}, expected {(0, -100)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = SwapArithmetic(4, 10)
        assert result == (10, 4), f"Test 24 failed: got {result}, expected {(10, 4)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = SwapArithmetic(-2, 201)
        assert result == (201, -2), f"Test 25 failed: got {result}, expected {(201, -2)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = SwapArithmetic(5, 1)
        assert result == (1, 5), f"Test 26 failed: got {result}, expected {(1, 5)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = SwapArithmetic(1, 3)
        assert result == (3, 1), f"Test 27 failed: got {result}, expected {(3, 1)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = SwapArithmetic(-9090, 1)
        assert result == (1, -9090), f"Test 28 failed: got {result}, expected {(1, -9090)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = SwapArithmetic(50, 1000000000000000001)
        assert result == (1000000000000000001, 50), f"Test 29 failed: got {result}, expected {(1000000000000000001, 50)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = SwapArithmetic(123, -10)
        assert result == (-10, 123), f"Test 30 failed: got {result}, expected {(-10, 123)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = SwapArithmetic(455, 126)
        assert result == (126, 455), f"Test 31 failed: got {result}, expected {(126, 455)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = SwapArithmetic(999999, -1000001)
        assert result == (-1000001, 999999), f"Test 32 failed: got {result}, expected {(-1000001, 999999)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = SwapArithmetic(999999, 2147483647)
        assert result == (2147483647, 999999), f"Test 33 failed: got {result}, expected {(2147483647, 999999)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = SwapArithmetic(9223372036854775807, 1000000)
        assert result == (1000000, 9223372036854775807), f"Test 34 failed: got {result}, expected {(1000000, 9223372036854775807)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = SwapArithmetic(0, -490)
        assert result == (-490, 0), f"Test 35 failed: got {result}, expected {(-490, 0)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = SwapArithmetic(-41, -84)
        assert result == (-84, -41), f"Test 36 failed: got {result}, expected {(-84, -41)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = SwapArithmetic(-9223372036854775807, 9223372036854775808)
        assert result == (9223372036854775808, -9223372036854775807), f"Test 37 failed: got {result}, expected {(9223372036854775808, -9223372036854775807)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = SwapArithmetic(18446744073709551612, 9223372036854775807)
        assert result == (9223372036854775807, 18446744073709551612), f"Test 38 failed: got {result}, expected {(9223372036854775807, 18446744073709551612)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = SwapArithmetic(2, -9223372036854775807)
        assert result == (-9223372036854775807, 2), f"Test 39 failed: got {result}, expected {(-9223372036854775807, 2)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = SwapArithmetic(-9223372036854775808, -1000000000000000001)
        assert result == (-1000000000000000001, -9223372036854775808), f"Test 40 failed: got {result}, expected {(-1000000000000000001, -9223372036854775808)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = SwapArithmetic(-4294967296, 2147483646)
        assert result == (2147483646, -4294967296), f"Test 41 failed: got {result}, expected {(2147483646, -4294967296)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = SwapArithmetic(-2147483648, 246913578024691357802469135782)
        assert result == (246913578024691357802469135782, -2147483648), f"Test 42 failed: got {result}, expected {(246913578024691357802469135782, -2147483648)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = SwapArithmetic(122, -2147483649)
        assert result == (-2147483649, 122), f"Test 43 failed: got {result}, expected {(-2147483649, 122)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = SwapArithmetic(-2147483651, -2147483648)
        assert result == (-2147483648, -2147483651), f"Test 44 failed: got {result}, expected {(-2147483648, -2147483651)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = SwapArithmetic(-1000000000000, 1000000000002)
        assert result == (1000000000002, -1000000000000), f"Test 45 failed: got {result}, expected {(1000000000002, -1000000000000)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = SwapArithmetic(0, 1000000000000000001)
        assert result == (1000000000000000001, 0), f"Test 46 failed: got {result}, expected {(1000000000000000001, 0)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = SwapArithmetic(999999, -912)
        assert result == (-912, 999999), f"Test 47 failed: got {result}, expected {(-912, 999999)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = SwapArithmetic(121, 0)
        assert result == (0, 121), f"Test 48 failed: got {result}, expected {(0, 121)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = SwapArithmetic(-2718281828459046, -86)
        assert result == (-86, -2718281828459046), f"Test 49 failed: got {result}, expected {(-86, -2718281828459046)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = SwapArithmetic(-3141592653589793, 2718281828459046)
        assert result == (2718281828459046, -3141592653589793), f"Test 50 failed: got {result}, expected {(2718281828459046, -3141592653589793)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = SwapArithmetic(-18446744073709551615, 18446744073709551614)
        assert result == (18446744073709551614, -18446744073709551615), f"Test 51 failed: got {result}, expected {(18446744073709551614, -18446744073709551615)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = SwapArithmetic(123456789012345678901234567891, -493827156049382715604938271560)
        assert result == (-493827156049382715604938271560, 123456789012345678901234567891), f"Test 52 failed: got {result}, expected {(-493827156049382715604938271560, 123456789012345678901234567891)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = SwapArithmetic(999999999998, -2718281828459045)
        assert result == (-2718281828459045, 999999999998), f"Test 53 failed: got {result}, expected {(-2718281828459045, 999999999998)}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = SwapArithmetic(2147483647, -8080)
        assert result == (-8080, 2147483647), f"Test 54 failed: got {result}, expected {(-8080, 2147483647)}"
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
