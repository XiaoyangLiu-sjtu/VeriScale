# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def MultipleReturns(x, y):
2: ✓     return (x + y, x - y)
```

## Complete Test File

```python
def MultipleReturns(x, y):
    return (x + y, x - y)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = MultipleReturns(3, 2)
        assert result == (5, 1), f"Test 1 failed: got {result}, expected {(5, 1)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = MultipleReturns(-2, 3)
        assert result == (1, -5), f"Test 2 failed: got {result}, expected {(1, -5)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = MultipleReturns(0, 0)
        assert result == (0, 0), f"Test 3 failed: got {result}, expected {(0, 0)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = MultipleReturns(10, 5)
        assert result == (15, 5), f"Test 4 failed: got {result}, expected {(15, 5)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = MultipleReturns(-5, -10)
        assert result == (-15, 5), f"Test 5 failed: got {result}, expected {(-15, 5)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = MultipleReturns(-1, 0)
        assert result == (-1, -1), f"Test 6 failed: got {result}, expected {(-1, -1)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = MultipleReturns(0, -1)
        assert result == (-1, 1), f"Test 7 failed: got {result}, expected {(-1, 1)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = MultipleReturns(-1, -1)
        assert result == (-2, 0), f"Test 8 failed: got {result}, expected {(-2, 0)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = MultipleReturns(1, -1)
        assert result == (0, 2), f"Test 9 failed: got {result}, expected {(0, 2)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = MultipleReturns(-1, 1)
        assert result == (0, -2), f"Test 10 failed: got {result}, expected {(0, -2)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = MultipleReturns(123, -456)
        assert result == (-333, 579), f"Test 11 failed: got {result}, expected {(-333, 579)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = MultipleReturns(-123, 456)
        assert result == (333, -579), f"Test 12 failed: got {result}, expected {(333, -579)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = MultipleReturns(999999, -999999)
        assert result == (0, 1999998), f"Test 13 failed: got {result}, expected {(0, 1999998)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = MultipleReturns(-999999, 999999)
        assert result == (0, -1999998), f"Test 14 failed: got {result}, expected {(0, -1999998)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = MultipleReturns(2147483647, 1)
        assert result == (2147483648, 2147483646), f"Test 15 failed: got {result}, expected {(2147483648, 2147483646)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = MultipleReturns(9223372036854775807, -9223372036854775808)
        assert result == (-1, 18446744073709551615), f"Test 16 failed: got {result}, expected {(-1, 18446744073709551615)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = MultipleReturns(-9223372036854775808, 9223372036854775807)
        assert result == (-1, -18446744073709551615), f"Test 17 failed: got {result}, expected {(-1, -18446744073709551615)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = MultipleReturns(1000000000000000000, 1000000000000000000)
        assert result == (2000000000000000000, 0), f"Test 18 failed: got {result}, expected {(2000000000000000000, 0)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = MultipleReturns(-1000000000000000000, -1000000000000000000)
        assert result == (-2000000000000000000, 0), f"Test 19 failed: got {result}, expected {(-2000000000000000000, 0)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = MultipleReturns(-1000000000000000000, 1000000000000000000)
        assert result == (0, -2000000000000000000), f"Test 20 failed: got {result}, expected {(0, -2000000000000000000)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = MultipleReturns(42, -42)
        assert result == (0, 84), f"Test 21 failed: got {result}, expected {(0, 84)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = MultipleReturns(-42, 42)
        assert result == (0, -84), f"Test 22 failed: got {result}, expected {(0, -84)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = MultipleReturns(7, 13)
        assert result == (20, -6), f"Test 23 failed: got {result}, expected {(20, -6)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = MultipleReturns(-7, 13)
        assert result == (6, -20), f"Test 24 failed: got {result}, expected {(6, -20)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = MultipleReturns(7, -13)
        assert result == (-6, 20), f"Test 25 failed: got {result}, expected {(-6, 20)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = MultipleReturns(-7, -13)
        assert result == (-20, 6), f"Test 26 failed: got {result}, expected {(-20, 6)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = MultipleReturns(3141592653589793, 2718281828459045)
        assert result == (5859874482048838, 423310825130748), f"Test 27 failed: got {result}, expected {(5859874482048838, 423310825130748)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = MultipleReturns(-3141592653589793, 2718281828459045)
        assert result == (-423310825130748, -5859874482048838), f"Test 28 failed: got {result}, expected {(-423310825130748, -5859874482048838)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = MultipleReturns(3141592653589793, -2718281828459045)
        assert result == (423310825130748, 5859874482048838), f"Test 29 failed: got {result}, expected {(423310825130748, 5859874482048838)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = MultipleReturns(-3141592653589793, -2718281828459045)
        assert result == (-5859874482048838, -423310825130748), f"Test 30 failed: got {result}, expected {(-5859874482048838, -423310825130748)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = MultipleReturns(18446744073709551615, 1)
        assert result == (18446744073709551616, 18446744073709551614), f"Test 31 failed: got {result}, expected {(18446744073709551616, 18446744073709551614)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = MultipleReturns(-18446744073709551616, -1)
        assert result == (-18446744073709551617, -18446744073709551615), f"Test 32 failed: got {result}, expected {(-18446744073709551617, -18446744073709551615)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = MultipleReturns(4294967296, -4294967296)
        assert result == (0, 8589934592), f"Test 33 failed: got {result}, expected {(0, 8589934592)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = MultipleReturns(-4294967296, 4294967296)
        assert result == (0, -8589934592), f"Test 34 failed: got {result}, expected {(0, -8589934592)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = MultipleReturns(65535, -65536)
        assert result == (-1, 131071), f"Test 35 failed: got {result}, expected {(-1, 131071)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = MultipleReturns(0, 2)
        assert result == (2, -2), f"Test 36 failed: got {result}, expected {(2, -2)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = MultipleReturns(2, 2)
        assert result == (4, 0), f"Test 37 failed: got {result}, expected {(4, 0)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = MultipleReturns(-1, 3)
        assert result == (2, -4), f"Test 38 failed: got {result}, expected {(2, -4)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = MultipleReturns(0, -123456789012345678901234567890)
        assert result == (-123456789012345678901234567890, 123456789012345678901234567890), f"Test 39 failed: got {result}, expected {(-123456789012345678901234567890, 123456789012345678901234567890)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = MultipleReturns(-3, 1)
        assert result == (-2, -4), f"Test 40 failed: got {result}, expected {(-2, -4)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = MultipleReturns(0, -2)
        assert result == (-2, 2), f"Test 41 failed: got {result}, expected {(-2, 2)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = MultipleReturns(1, 1000000000000000000)
        assert result == (1000000000000000001, -999999999999999999), f"Test 42 failed: got {result}, expected {(1000000000000000001, -999999999999999999)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = MultipleReturns(3, 3)
        assert result == (6, 0), f"Test 43 failed: got {result}, expected {(6, 0)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = MultipleReturns(3, 0)
        assert result == (3, 3), f"Test 44 failed: got {result}, expected {(3, 3)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = MultipleReturns(3, -2)
        assert result == (1, 5), f"Test 45 failed: got {result}, expected {(1, 5)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = MultipleReturns(-123456789012345678901234567890, -4294967296)
        assert result == (-123456789012345678905529535186, -123456789012345678896939600594), f"Test 46 failed: got {result}, expected {(-123456789012345678905529535186, -123456789012345678896939600594)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = MultipleReturns(-18446744073709551616, 4)
        assert result == (-18446744073709551612, -18446744073709551620), f"Test 47 failed: got {result}, expected {(-18446744073709551612, -18446744073709551620)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = MultipleReturns(2, -5)
        assert result == (-3, 7), f"Test 48 failed: got {result}, expected {(-3, 7)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = MultipleReturns(-4, 456)
        assert result == (452, -460), f"Test 49 failed: got {result}, expected {(452, -460)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = MultipleReturns(246, -2)
        assert result == (244, 248), f"Test 50 failed: got {result}, expected {(244, 248)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = MultipleReturns(-65535, 3)
        assert result == (-65532, -65538), f"Test 51 failed: got {result}, expected {(-65532, -65538)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = MultipleReturns(-65535, -2147483647)
        assert result == (-2147549182, 2147418112), f"Test 52 failed: got {result}, expected {(-2147549182, 2147418112)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = MultipleReturns(2, 3)
        assert result == (5, -1), f"Test 53 failed: got {result}, expected {(5, -1)}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = MultipleReturns(-3, 4)
        assert result == (1, -7), f"Test 54 failed: got {result}, expected {(1, -7)}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = MultipleReturns(40, 4)
        assert result == (44, 36), f"Test 55 failed: got {result}, expected {(44, 36)}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = MultipleReturns(1000000000000000000, 2)
        assert result == (1000000000000000002, 999999999999999998), f"Test 56 failed: got {result}, expected {(1000000000000000002, 999999999999999998)}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = MultipleReturns(-3, 999998)
        assert result == (999995, -1000001), f"Test 57 failed: got {result}, expected {(999995, -1000001)}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = MultipleReturns(5, -123)
        assert result == (-118, 128), f"Test 58 failed: got {result}, expected {(-118, 128)}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = MultipleReturns(0, 999996)
        assert result == (999996, -999996), f"Test 59 failed: got {result}, expected {(999996, -999996)}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = MultipleReturns(0, 123)
        assert result == (123, -123), f"Test 60 failed: got {result}, expected {(123, -123)}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = MultipleReturns(-7, 1)
        assert result == (-6, -8), f"Test 61 failed: got {result}, expected {(-6, -8)}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = MultipleReturns(-10, -9223372036854775808)
        assert result == (-9223372036854775818, 9223372036854775798), f"Test 62 failed: got {result}, expected {(-9223372036854775818, 9223372036854775798)}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = MultipleReturns(-4294967296, 18446744073709551615)
        assert result == (18446744069414584319, -18446744078004518911), f"Test 63 failed: got {result}, expected {(18446744069414584319, -18446744078004518911)}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = MultipleReturns(-1, -4294967296)
        assert result == (-4294967297, 4294967295), f"Test 64 failed: got {result}, expected {(-4294967297, 4294967295)}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = MultipleReturns(0, 999998)
        assert result == (999998, -999998), f"Test 65 failed: got {result}, expected {(999998, -999998)}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = MultipleReturns(-18446744073709551616, 3141592653589792)
        assert result == (-18443602481055961824, -18449885666363141408), f"Test 66 failed: got {result}, expected {(-18443602481055961824, -18449885666363141408)}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = MultipleReturns(42, 0)
        assert result == (42, 42), f"Test 67 failed: got {result}, expected {(42, 42)}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = MultipleReturns(0, 5)
        assert result == (5, -5), f"Test 68 failed: got {result}, expected {(5, -5)}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = MultipleReturns(22, 0)
        assert result == (22, 22), f"Test 69 failed: got {result}, expected {(22, 22)}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = MultipleReturns(12, 0)
        assert result == (12, 12), f"Test 70 failed: got {result}, expected {(12, 12)}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = MultipleReturns(44, -1)
        assert result == (43, 45), f"Test 71 failed: got {result}, expected {(43, 45)}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = MultipleReturns(-9, 0)
        assert result == (-9, -9), f"Test 72 failed: got {result}, expected {(-9, -9)}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = MultipleReturns(-8, 5)
        assert result == (-3, -13), f"Test 73 failed: got {result}, expected {(-3, -13)}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = MultipleReturns(9, 10)
        assert result == (19, -1), f"Test 74 failed: got {result}, expected {(19, -1)}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = MultipleReturns(10, 0)
        assert result == (10, 10), f"Test 75 failed: got {result}, expected {(10, 10)}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = MultipleReturns(10, 4)
        assert result == (14, 6), f"Test 76 failed: got {result}, expected {(14, 6)}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = MultipleReturns(9, -5)
        assert result == (4, 14), f"Test 77 failed: got {result}, expected {(4, 14)}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = MultipleReturns(-5, 10)
        assert result == (5, -15), f"Test 78 failed: got {result}, expected {(5, -15)}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = MultipleReturns(-5, 25)
        assert result == (20, -30), f"Test 79 failed: got {result}, expected {(20, -30)}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = MultipleReturns(-5, 0)
        assert result == (-5, -5), f"Test 80 failed: got {result}, expected {(-5, -5)}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = MultipleReturns(-65535, 999996)
        assert result == (934461, -1065531), f"Test 81 failed: got {result}, expected {(934461, -1065531)}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = MultipleReturns(-5, -3)
        assert result == (-8, -2), f"Test 82 failed: got {result}, expected {(-8, -2)}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = MultipleReturns(-3, -10)
        assert result == (-13, 7), f"Test 83 failed: got {result}, expected {(-13, 7)}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = MultipleReturns(999999, -10)
        assert result == (999989, 1000009), f"Test 84 failed: got {result}, expected {(999989, 1000009)}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = MultipleReturns(0, -9)
        assert result == (-9, 9), f"Test 85 failed: got {result}, expected {(-9, 9)}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = MultipleReturns(6, -999998)
        assert result == (-999992, 1000004), f"Test 86 failed: got {result}, expected {(-999992, 1000004)}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = MultipleReturns(-2147483648, 10)
        assert result == (-2147483638, -2147483658), f"Test 87 failed: got {result}, expected {(-2147483638, -2147483658)}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = MultipleReturns(-6, 4294967296)
        assert result == (4294967290, -4294967302), f"Test 88 failed: got {result}, expected {(4294967290, -4294967302)}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = MultipleReturns(-2, 0)
        assert result == (-2, -2), f"Test 89 failed: got {result}, expected {(-2, -2)}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = MultipleReturns(2, 1)
        assert result == (3, 1), f"Test 90 failed: got {result}, expected {(3, 1)}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = MultipleReturns(1, 4)
        assert result == (5, -3), f"Test 91 failed: got {result}, expected {(5, -3)}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = MultipleReturns(65536, 0)
        assert result == (65536, 65536), f"Test 92 failed: got {result}, expected {(65536, 65536)}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = MultipleReturns(-2, -999997)
        assert result == (-999999, 999995), f"Test 93 failed: got {result}, expected {(-999999, 999995)}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = MultipleReturns(-999998, 1)
        assert result == (-999997, -999999), f"Test 94 failed: got {result}, expected {(-999997, -999999)}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = MultipleReturns(0, -5)
        assert result == (-5, 5), f"Test 95 failed: got {result}, expected {(-5, 5)}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = MultipleReturns(1, 12)
        assert result == (13, -11), f"Test 96 failed: got {result}, expected {(13, -11)}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = MultipleReturns(-457, -1)
        assert result == (-458, -456), f"Test 97 failed: got {result}, expected {(-458, -456)}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = MultipleReturns(-2718281828459044, 1)
        assert result == (-2718281828459043, -2718281828459045), f"Test 98 failed: got {result}, expected {(-2718281828459043, -2718281828459045)}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = MultipleReturns(-42, 0)
        assert result == (-42, -42), f"Test 99 failed: got {result}, expected {(-42, -42)}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = MultipleReturns(0, -123)
        assert result == (-123, 123), f"Test 100 failed: got {result}, expected {(-123, 123)}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = MultipleReturns(0, 3)
        assert result == (3, -3), f"Test 101 failed: got {result}, expected {(3, -3)}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = MultipleReturns(-8, -1)
        assert result == (-9, -7), f"Test 102 failed: got {result}, expected {(-9, -7)}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = MultipleReturns(40, 1)
        assert result == (41, 39), f"Test 103 failed: got {result}, expected {(41, 39)}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = MultipleReturns(2147483648, -2)
        assert result == (2147483646, 2147483650), f"Test 104 failed: got {result}, expected {(2147483646, 2147483650)}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = MultipleReturns(0, -456)
        assert result == (-456, 456), f"Test 105 failed: got {result}, expected {(-456, 456)}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = MultipleReturns(-12, 0)
        assert result == (-12, -12), f"Test 106 failed: got {result}, expected {(-12, -12)}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = MultipleReturns(-5, -123456789012345678901234567890)
        assert result == (-123456789012345678901234567895, 123456789012345678901234567885), f"Test 107 failed: got {result}, expected {(-123456789012345678901234567895, 123456789012345678901234567885)}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = MultipleReturns(-1, 10)
        assert result == (9, -11), f"Test 108 failed: got {result}, expected {(9, -11)}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = MultipleReturns(-1, -8)
        assert result == (-9, 7), f"Test 109 failed: got {result}, expected {(-9, 7)}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = MultipleReturns(492, -456)
        assert result == (36, 948), f"Test 110 failed: got {result}, expected {(36, 948)}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = MultipleReturns(-3, 0)
        assert result == (-3, -3), f"Test 111 failed: got {result}, expected {(-3, -3)}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = MultipleReturns(-2, -999998)
        assert result == (-1000000, 999996), f"Test 112 failed: got {result}, expected {(-1000000, 999996)}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = MultipleReturns(5436563656918090, 123)
        assert result == (5436563656918213, 5436563656917967), f"Test 113 failed: got {result}, expected {(5436563656918213, 5436563656917967)}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = MultipleReturns(2147483646, -1000000000000000000)
        assert result == (-999999997852516354, 1000000002147483646), f"Test 114 failed: got {result}, expected {(-999999997852516354, 1000000002147483646)}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = MultipleReturns(0, -2718281828459044)
        assert result == (-2718281828459044, 2718281828459044), f"Test 115 failed: got {result}, expected {(-2718281828459044, 2718281828459044)}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = MultipleReturns(-2, 25)
        assert result == (23, -27), f"Test 116 failed: got {result}, expected {(23, -27)}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = MultipleReturns(12, 4)
        assert result == (16, 8), f"Test 117 failed: got {result}, expected {(16, 8)}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = MultipleReturns(0, 7)
        assert result == (7, -7), f"Test 118 failed: got {result}, expected {(7, -7)}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = MultipleReturns(-1, 18446744073709551615)
        assert result == (18446744073709551614, -18446744073709551616), f"Test 119 failed: got {result}, expected {(18446744073709551614, -18446744073709551616)}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = MultipleReturns(0, 9)
        assert result == (9, -9), f"Test 120 failed: got {result}, expected {(9, -9)}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = MultipleReturns(18446744073709551616, 1)
        assert result == (18446744073709551617, 18446744073709551615), f"Test 121 failed: got {result}, expected {(18446744073709551617, 18446744073709551615)}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = MultipleReturns(2, -2147483647)
        assert result == (-2147483645, 2147483649), f"Test 122 failed: got {result}, expected {(-2147483645, 2147483649)}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = MultipleReturns(4, 0)
        assert result == (4, 4), f"Test 123 failed: got {result}, expected {(4, 4)}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = MultipleReturns(1, -8)
        assert result == (-7, 9), f"Test 124 failed: got {result}, expected {(-7, 9)}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = MultipleReturns(1, 22)
        assert result == (23, -21), f"Test 125 failed: got {result}, expected {(23, -21)}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = MultipleReturns(1, 65536)
        assert result == (65537, -65535), f"Test 126 failed: got {result}, expected {(65537, -65535)}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = MultipleReturns(-12, -1)
        assert result == (-13, -11), f"Test 127 failed: got {result}, expected {(-13, -11)}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = MultipleReturns(4, -1)
        assert result == (3, 5), f"Test 128 failed: got {result}, expected {(3, 5)}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = MultipleReturns(1, -18446744073709551616)
        assert result == (-18446744073709551615, 18446744073709551617), f"Test 129 failed: got {result}, expected {(-18446744073709551615, 18446744073709551617)}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = MultipleReturns(3, 1)
        assert result == (4, 2), f"Test 130 failed: got {result}, expected {(4, 2)}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = MultipleReturns(-2, 2)
        assert result == (0, -4), f"Test 131 failed: got {result}, expected {(0, -4)}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = MultipleReturns(5, -1)
        assert result == (4, 6), f"Test 132 failed: got {result}, expected {(4, 6)}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = MultipleReturns(-1, 2147483645)
        assert result == (2147483644, -2147483646), f"Test 133 failed: got {result}, expected {(2147483644, -2147483646)}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = MultipleReturns(-1, -2147483647)
        assert result == (-2147483648, 2147483646), f"Test 134 failed: got {result}, expected {(-2147483648, 2147483646)}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = MultipleReturns(-3, 2000000000000000002)
        assert result == (1999999999999999999, -2000000000000000005), f"Test 135 failed: got {result}, expected {(1999999999999999999, -2000000000000000005)}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = MultipleReturns(0, 4294967296)
        assert result == (4294967296, -4294967296), f"Test 136 failed: got {result}, expected {(4294967296, -4294967296)}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = MultipleReturns(-1000000000000000000, -6)
        assert result == (-1000000000000000006, -999999999999999994), f"Test 137 failed: got {result}, expected {(-1000000000000000006, -999999999999999994)}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = MultipleReturns(-1, -2)
        assert result == (-3, 1), f"Test 138 failed: got {result}, expected {(-3, 1)}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = MultipleReturns(-10, -2)
        assert result == (-12, -8), f"Test 139 failed: got {result}, expected {(-12, -8)}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = MultipleReturns(999999, 0)
        assert result == (999999, 999999), f"Test 140 failed: got {result}, expected {(999999, 999999)}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = MultipleReturns(-2, -3)
        assert result == (-5, 1), f"Test 141 failed: got {result}, expected {(-5, 1)}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = MultipleReturns(0, 4)
        assert result == (4, -4), f"Test 142 failed: got {result}, expected {(4, -4)}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = MultipleReturns(-999997, -1)
        assert result == (-999998, -999996), f"Test 143 failed: got {result}, expected {(-999998, -999996)}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = MultipleReturns(-2718281828459044, -2000000000000000000)
        assert result == (-2002718281828459044, 1997281718171540956), f"Test 144 failed: got {result}, expected {(-2002718281828459044, 1997281718171540956)}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = MultipleReturns(40, 456)
        assert result == (496, -416), f"Test 145 failed: got {result}, expected {(496, -416)}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = MultipleReturns(2147483646, -2000000000000000000)
        assert result == (-1999999997852516354, 2000000002147483646), f"Test 146 failed: got {result}, expected {(-1999999997852516354, 2000000002147483646)}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = MultipleReturns(2, -1)
        assert result == (1, 3), f"Test 147 failed: got {result}, expected {(1, 3)}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = MultipleReturns(-24, 1)
        assert result == (-23, -25), f"Test 148 failed: got {result}, expected {(-23, -25)}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = MultipleReturns(18446744073709551615, 2)
        assert result == (18446744073709551617, 18446744073709551613), f"Test 149 failed: got {result}, expected {(18446744073709551617, 18446744073709551613)}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = MultipleReturns(1, -10)
        assert result == (-9, 11), f"Test 150 failed: got {result}, expected {(-9, 11)}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = MultipleReturns(2, -2)
        assert result == (0, 4), f"Test 151 failed: got {result}, expected {(0, 4)}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = MultipleReturns(-1, 8)
        assert result == (7, -9), f"Test 152 failed: got {result}, expected {(7, -9)}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = MultipleReturns(-65535, 5436563656918090)
        assert result == (5436563656852555, -5436563656983625), f"Test 153 failed: got {result}, expected {(5436563656852555, -5436563656983625)}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = MultipleReturns(-1, 3141592653589793)
        assert result == (3141592653589792, -3141592653589794), f"Test 154 failed: got {result}, expected {(3141592653589792, -3141592653589794)}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = MultipleReturns(-1, -41)
        assert result == (-42, 40), f"Test 155 failed: got {result}, expected {(-42, 40)}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = MultipleReturns(-1, -3)
        assert result == (-4, 2), f"Test 156 failed: got {result}, expected {(-4, 2)}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = MultipleReturns(-1, -9)
        assert result == (-10, 8), f"Test 157 failed: got {result}, expected {(-10, 8)}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = MultipleReturns(-1, 2147483647)
        assert result == (2147483646, -2147483648), f"Test 158 failed: got {result}, expected {(2147483646, -2147483648)}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = MultipleReturns(-4, 1)
        assert result == (-3, -5), f"Test 159 failed: got {result}, expected {(-3, -5)}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = MultipleReturns(-18446744073709551616, -457)
        assert result == (-18446744073709552073, -18446744073709551159), f"Test 160 failed: got {result}, expected {(-18446744073709552073, -18446744073709551159)}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = MultipleReturns(-1, 4294967296)
        assert result == (4294967295, -4294967297), f"Test 161 failed: got {result}, expected {(4294967295, -4294967297)}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = MultipleReturns(2, 18446744073709551615)
        assert result == (18446744073709551617, -18446744073709551613), f"Test 162 failed: got {result}, expected {(18446744073709551617, -18446744073709551613)}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = MultipleReturns(65535, -3)
        assert result == (65532, 65538), f"Test 163 failed: got {result}, expected {(65532, 65538)}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = MultipleReturns(-4294967296, 0)
        assert result == (-4294967296, -4294967296), f"Test 164 failed: got {result}, expected {(-4294967296, -4294967296)}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = MultipleReturns(1, 5)
        assert result == (6, -4), f"Test 165 failed: got {result}, expected {(6, -4)}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = MultipleReturns(246, -9223372036854775808)
        assert result == (-9223372036854775562, 9223372036854776054), f"Test 166 failed: got {result}, expected {(-9223372036854775562, 9223372036854776054)}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = MultipleReturns(-999999, -3)
        assert result == (-1000002, -999996), f"Test 167 failed: got {result}, expected {(-1000002, -999996)}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = MultipleReturns(24, 0)
        assert result == (24, 24), f"Test 168 failed: got {result}, expected {(24, 24)}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = MultipleReturns(-9, -4)
        assert result == (-13, -5), f"Test 169 failed: got {result}, expected {(-13, -5)}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = MultipleReturns(4, -2)
        assert result == (2, 6), f"Test 170 failed: got {result}, expected {(2, 6)}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = MultipleReturns(-42, 6)
        assert result == (-36, -48), f"Test 171 failed: got {result}, expected {(-36, -48)}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = MultipleReturns(247, 9)
        assert result == (256, 238), f"Test 172 failed: got {result}, expected {(256, 238)}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = MultipleReturns(123, -912)
        assert result == (-789, 1035), f"Test 173 failed: got {result}, expected {(-789, 1035)}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = MultipleReturns(2, -123)
        assert result == (-121, 125), f"Test 174 failed: got {result}, expected {(-121, 125)}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = MultipleReturns(123, -2147483647)
        assert result == (-2147483524, 2147483770), f"Test 175 failed: got {result}, expected {(-2147483524, 2147483770)}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = MultipleReturns(-246, -457)
        assert result == (-703, 211), f"Test 176 failed: got {result}, expected {(-703, 211)}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = MultipleReturns(123, 0)
        assert result == (123, 123), f"Test 177 failed: got {result}, expected {(123, 123)}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = MultipleReturns(0, -1826)
        assert result == (-1826, 1826), f"Test 178 failed: got {result}, expected {(-1826, 1826)}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = MultipleReturns(122, -2718281828459045)
        assert result == (-2718281828458923, 2718281828459167), f"Test 179 failed: got {result}, expected {(-2718281828458923, 2718281828459167)}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = MultipleReturns(123, -4)
        assert result == (119, 127), f"Test 180 failed: got {result}, expected {(119, 127)}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = MultipleReturns(122, -455)
        assert result == (-333, 577), f"Test 181 failed: got {result}, expected {(-333, 577)}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = MultipleReturns(122, -4294967294)
        assert result == (-4294967172, 4294967416), f"Test 182 failed: got {result}, expected {(-4294967172, 4294967416)}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = MultipleReturns(-123, -456)
        assert result == (-579, 333), f"Test 183 failed: got {result}, expected {(-579, 333)}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = MultipleReturns(0, 458)
        assert result == (458, -458), f"Test 184 failed: got {result}, expected {(458, -458)}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = MultipleReturns(-911, 8)
        assert result == (-903, -919), f"Test 185 failed: got {result}, expected {(-903, -919)}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = MultipleReturns(-122, 912)
        assert result == (790, -1034), f"Test 186 failed: got {result}, expected {(790, -1034)}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = MultipleReturns(18446744073709551616, 455)
        assert result == (18446744073709552071, 18446744073709551161), f"Test 187 failed: got {result}, expected {(18446744073709552071, 18446744073709551161)}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = MultipleReturns(-123, 457)
        assert result == (334, -580), f"Test 188 failed: got {result}, expected {(334, -580)}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = MultipleReturns(-123, 18446744073709551616)
        assert result == (18446744073709551493, -18446744073709551739), f"Test 189 failed: got {result}, expected {(18446744073709551493, -18446744073709551739)}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = MultipleReturns(123, 9)
        assert result == (132, 114), f"Test 190 failed: got {result}, expected {(132, 114)}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = MultipleReturns(0, 456)
        assert result == (456, -456), f"Test 191 failed: got {result}, expected {(456, -456)}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = MultipleReturns(-123, -911)
        assert result == (-1034, 788), f"Test 192 failed: got {result}, expected {(-1034, 788)}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = MultipleReturns(0, 913)
        assert result == (913, -913), f"Test 193 failed: got {result}, expected {(913, -913)}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = MultipleReturns(-1000000, 0)
        assert result == (-1000000, -1000000), f"Test 194 failed: got {result}, expected {(-1000000, -1000000)}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = MultipleReturns(0, -1000000)
        assert result == (-1000000, 1000000), f"Test 195 failed: got {result}, expected {(-1000000, 1000000)}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = MultipleReturns(-999999, -999998)
        assert result == (-1999997, -1), f"Test 196 failed: got {result}, expected {(-1999997, -1)}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = MultipleReturns(43, -48)
        assert result == (-5, 91), f"Test 197 failed: got {result}, expected {(-5, 91)}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = MultipleReturns(0, -999998)
        assert result == (-999998, 999998), f"Test 198 failed: got {result}, expected {(-999998, 999998)}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = MultipleReturns(18, -999998)
        assert result == (-999980, 1000016), f"Test 199 failed: got {result}, expected {(-999980, 1000016)}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = MultipleReturns(999997, -1)
        assert result == (999996, 999998), f"Test 200 failed: got {result}, expected {(999996, 999998)}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = MultipleReturns(999998, -999997)
        assert result == (1, 1999995), f"Test 201 failed: got {result}, expected {(1, 1999995)}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = MultipleReturns(-1000000, -1999995)
        assert result == (-2999995, 999995), f"Test 202 failed: got {result}, expected {(-2999995, 999995)}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = MultipleReturns(1999998, -999998)
        assert result == (1000000, 2999996), f"Test 203 failed: got {result}, expected {(1000000, 2999996)}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = MultipleReturns(-999999, -999999)
        assert result == (-1999998, 0), f"Test 204 failed: got {result}, expected {(-1999998, 0)}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = MultipleReturns(1, -999999)
        assert result == (-999998, 1000000), f"Test 205 failed: got {result}, expected {(-999998, 1000000)}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = MultipleReturns(0, 999999)
        assert result == (999999, -999999), f"Test 206 failed: got {result}, expected {(999999, -999999)}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = MultipleReturns(-2000000000000000000, 458)
        assert result == (-1999999999999999542, -2000000000000000458), f"Test 207 failed: got {result}, expected {(-1999999999999999542, -2000000000000000458)}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = MultipleReturns(-999999, -123456789012345678901234567888)
        assert result == (-123456789012345678901235567887, 123456789012345678901233567889), f"Test 208 failed: got {result}, expected {(-123456789012345678901235567887, 123456789012345678901233567889)}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = MultipleReturns(-999999, 1999998)
        assert result == (999999, -2999997), f"Test 209 failed: got {result}, expected {(999999, -2999997)}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = MultipleReturns(1, 1000001)
        assert result == (1000002, -1000000), f"Test 210 failed: got {result}, expected {(1000002, -1000000)}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = MultipleReturns(-999999, 2000000000000000002)
        assert result == (1999999999999000003, -2000000000001000001), f"Test 211 failed: got {result}, expected {(1999999999999000003, -2000000000001000001)}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = MultipleReturns(-999998, 1000000)
        assert result == (2, -1999998), f"Test 212 failed: got {result}, expected {(2, -1999998)}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = MultipleReturns(2, -914)
        assert result == (-912, 916), f"Test 213 failed: got {result}, expected {(-912, 916)}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = MultipleReturns(999999, 1000000)
        assert result == (1999999, -1), f"Test 214 failed: got {result}, expected {(1999999, -1)}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = MultipleReturns(-999999, 0)
        assert result == (-999999, -999999), f"Test 215 failed: got {result}, expected {(-999999, -999999)}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = MultipleReturns(0, 1000000)
        assert result == (1000000, -1000000), f"Test 216 failed: got {result}, expected {(1000000, -1000000)}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = MultipleReturns(999999, 454)
        assert result == (1000453, 999545), f"Test 217 failed: got {result}, expected {(1000453, 999545)}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = MultipleReturns(-5, 999999)
        assert result == (999994, -1000004), f"Test 218 failed: got {result}, expected {(999994, -1000004)}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = MultipleReturns(-18, -456)
        assert result == (-474, 438), f"Test 219 failed: got {result}, expected {(-474, 438)}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = MultipleReturns(2147483647, -911)
        assert result == (2147482736, 2147484558), f"Test 220 failed: got {result}, expected {(2147482736, 2147484558)}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = MultipleReturns(4294967292, 1)
        assert result == (4294967293, 4294967291), f"Test 221 failed: got {result}, expected {(4294967293, 4294967291)}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = MultipleReturns(-2147483647, 1)
        assert result == (-2147483646, -2147483648), f"Test 222 failed: got {result}, expected {(-2147483646, -2147483648)}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = MultipleReturns(0, -4)
        assert result == (-4, 4), f"Test 223 failed: got {result}, expected {(-4, 4)}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = MultipleReturns(-65536, -1)
        assert result == (-65537, -65535), f"Test 224 failed: got {result}, expected {(-65537, -65535)}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = MultipleReturns(2147483646, 1)
        assert result == (2147483647, 2147483645), f"Test 225 failed: got {result}, expected {(2147483647, 2147483645)}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = MultipleReturns(2147483648, -1)
        assert result == (2147483647, 2147483649), f"Test 226 failed: got {result}, expected {(2147483647, 2147483649)}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = MultipleReturns(-4294967292, 458)
        assert result == (-4294966834, -4294967750), f"Test 227 failed: got {result}, expected {(-4294966834, -4294967750)}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = MultipleReturns(2147483647, 2147483644)
        assert result == (4294967291, 3), f"Test 228 failed: got {result}, expected {(4294967291, 3)}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = MultipleReturns(-2147483647, -1)
        assert result == (-2147483648, -2147483646), f"Test 229 failed: got {result}, expected {(-2147483648, -2147483646)}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = MultipleReturns(-999996, 0)
        assert result == (-999996, -999996), f"Test 230 failed: got {result}, expected {(-999996, -999996)}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = MultipleReturns(-1825, -1)
        assert result == (-1826, -1824), f"Test 231 failed: got {result}, expected {(-1826, -1824)}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = MultipleReturns(-2147483648, -2)
        assert result == (-2147483650, -2147483646), f"Test 232 failed: got {result}, expected {(-2147483650, -2147483646)}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = MultipleReturns(1000001, -1)
        assert result == (1000000, 1000002), f"Test 233 failed: got {result}, expected {(1000000, 1000002)}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = MultipleReturns(-999997, 20)
        assert result == (-999977, -1000017), f"Test 234 failed: got {result}, expected {(-999977, -1000017)}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = MultipleReturns(-4294967295, -1)
        assert result == (-4294967296, -4294967294), f"Test 235 failed: got {result}, expected {(-4294967296, -4294967294)}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = MultipleReturns(-3, 5436563656918090)
        assert result == (5436563656918087, -5436563656918093), f"Test 236 failed: got {result}, expected {(5436563656918087, -5436563656918093)}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = MultipleReturns(2147483645, -1)
        assert result == (2147483644, 2147483646), f"Test 237 failed: got {result}, expected {(2147483644, 2147483646)}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = MultipleReturns(-2147483648, 50)
        assert result == (-2147483598, -2147483698), f"Test 238 failed: got {result}, expected {(-2147483598, -2147483698)}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = MultipleReturns(999999, 1)
        assert result == (1000000, 999998), f"Test 239 failed: got {result}, expected {(1000000, 999998)}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = MultipleReturns(-4294967295, 2147483648)
        assert result == (-2147483647, -6442450943), f"Test 240 failed: got {result}, expected {(-2147483647, -6442450943)}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = MultipleReturns(2147483649, 912)
        assert result == (2147484561, 2147482737), f"Test 241 failed: got {result}, expected {(2147484561, 2147482737)}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = MultipleReturns(4, 9223372036854775808)
        assert result == (9223372036854775812, -9223372036854775804), f"Test 242 failed: got {result}, expected {(9223372036854775812, -9223372036854775804)}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = MultipleReturns(-18, 18446744073709551612)
        assert result == (18446744073709551594, -18446744073709551630), f"Test 243 failed: got {result}, expected {(18446744073709551594, -18446744073709551630)}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = MultipleReturns(0, -2147483650)
        assert result == (-2147483650, 2147483650), f"Test 244 failed: got {result}, expected {(-2147483650, 2147483650)}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = MultipleReturns(1000000000000000000, -9223372036854775807)
        assert result == (-8223372036854775807, 10223372036854775807), f"Test 245 failed: got {result}, expected {(-8223372036854775807, 10223372036854775807)}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = MultipleReturns(65536, -9223372036854775809)
        assert result == (-9223372036854710273, 9223372036854841345), f"Test 246 failed: got {result}, expected {(-9223372036854710273, 9223372036854841345)}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = MultipleReturns(9223372036854775807, -9223372036854775810)
        assert result == (-3, 18446744073709551617), f"Test 247 failed: got {result}, expected {(-3, 18446744073709551617)}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = MultipleReturns(0, -9223372036854775808)
        assert result == (-9223372036854775808, 9223372036854775808), f"Test 248 failed: got {result}, expected {(-9223372036854775808, 9223372036854775808)}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = MultipleReturns(123456789012345678901234567890, -9223372036854775808)
        assert result == (123456789003122306864379792082, 123456789021569050938089343698), f"Test 249 failed: got {result}, expected {(123456789003122306864379792082, 123456789021569050938089343698)}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = MultipleReturns(-999998, 9223372036854775808)
        assert result == (9223372036853775810, -9223372036855775806), f"Test 250 failed: got {result}, expected {(9223372036853775810, -9223372036855775806)}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = MultipleReturns(1000000, 0)
        assert result == (1000000, 1000000), f"Test 251 failed: got {result}, expected {(1000000, 1000000)}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = MultipleReturns(9223372036854775807, -18446744073709551616)
        assert result == (-9223372036854775809, 27670116110564327423), f"Test 252 failed: got {result}, expected {(-9223372036854775809, 27670116110564327423)}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = MultipleReturns(492, -9223372036854775808)
        assert result == (-9223372036854775316, 9223372036854776300), f"Test 253 failed: got {result}, expected {(-9223372036854775316, 9223372036854776300)}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = MultipleReturns(0, 9223372036854775807)
        assert result == (9223372036854775807, -9223372036854775807), f"Test 254 failed: got {result}, expected {(9223372036854775807, -9223372036854775807)}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = MultipleReturns(912, 9223372036854775806)
        assert result == (9223372036854776718, -9223372036854774894), f"Test 255 failed: got {result}, expected {(9223372036854776718, -9223372036854774894)}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = MultipleReturns(9223372036854775810, -2)
        assert result == (9223372036854775808, 9223372036854775812), f"Test 256 failed: got {result}, expected {(9223372036854775808, 9223372036854775812)}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = MultipleReturns(-121, 18446744073709551614)
        assert result == (18446744073709551493, -18446744073709551735), f"Test 257 failed: got {result}, expected {(18446744073709551493, -18446744073709551735)}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = MultipleReturns(-18446744073709551617, -4)
        assert result == (-18446744073709551621, -18446744073709551613), f"Test 258 failed: got {result}, expected {(-18446744073709551621, -18446744073709551613)}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = MultipleReturns(-9223372036854775809, -18446744073709551614)
        assert result == (-27670116110564327423, 9223372036854775805), f"Test 259 failed: got {result}, expected {(-27670116110564327423, 9223372036854775805)}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = MultipleReturns(-18446744073709551616, 9223372036854775806)
        assert result == (-9223372036854775810, -27670116110564327422), f"Test 260 failed: got {result}, expected {(-9223372036854775810, -27670116110564327422)}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = MultipleReturns(-9223372036854775809, 9223372036854775807)
        assert result == (-2, -18446744073709551616), f"Test 261 failed: got {result}, expected {(-2, -18446744073709551616)}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = MultipleReturns(-9223372036854775808, 0)
        assert result == (-9223372036854775808, -9223372036854775808), f"Test 262 failed: got {result}, expected {(-9223372036854775808, -9223372036854775808)}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = MultipleReturns(-5436563656918090, -1)
        assert result == (-5436563656918091, -5436563656918089), f"Test 263 failed: got {result}, expected {(-5436563656918091, -5436563656918089)}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = MultipleReturns(2000000000000000000, 2000000000000000000)
        assert result == (4000000000000000000, 0), f"Test 264 failed: got {result}, expected {(4000000000000000000, 0)}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = MultipleReturns(25, 248)
        assert result == (273, -223), f"Test 265 failed: got {result}, expected {(273, -223)}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = MultipleReturns(1000000000000000001, 999999999999999999)
        assert result == (2000000000000000000, 2), f"Test 266 failed: got {result}, expected {(2000000000000000000, 2)}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = MultipleReturns(-492, 1000000000000000000)
        assert result == (999999999999999508, -1000000000000000492), f"Test 267 failed: got {result}, expected {(999999999999999508, -1000000000000000492)}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = MultipleReturns(2000000000000000000, 999999999999999998)
        assert result == (2999999999999999998, 1000000000000000002), f"Test 268 failed: got {result}, expected {(2999999999999999998, 1000000000000000002)}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = MultipleReturns(1000000000000000001, 40)
        assert result == (1000000000000000041, 999999999999999961), f"Test 269 failed: got {result}, expected {(1000000000000000041, 999999999999999961)}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = MultipleReturns(2000000000000000000, -2147483650)
        assert result == (1999999997852516350, 2000000002147483650), f"Test 270 failed: got {result}, expected {(1999999997852516350, 2000000002147483650)}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = MultipleReturns(2000000000000000000, 3141592653589793)
        assert result == (2003141592653589793, 1996858407346410207), f"Test 271 failed: got {result}, expected {(2003141592653589793, 1996858407346410207)}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = MultipleReturns(-1000000000000000001, 999999999999999999)
        assert result == (-2, -2000000000000000000), f"Test 272 failed: got {result}, expected {(-2, -2000000000000000000)}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = MultipleReturns(1000001, -39)
        assert result == (999962, 1000040), f"Test 273 failed: got {result}, expected {(999962, 1000040)}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = MultipleReturns(1000000000000000001, 2147483645)
        assert result == (1000000002147483646, 999999997852516356), f"Test 274 failed: got {result}, expected {(1000000002147483646, 999999997852516356)}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = MultipleReturns(492, 999999999999999998)
        assert result == (1000000000000000490, -999999999999999506), f"Test 275 failed: got {result}, expected {(1000000000000000490, -999999999999999506)}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = MultipleReturns(-18446744073709551617, -2000000000000000000)
        assert result == (-20446744073709551617, -16446744073709551617), f"Test 276 failed: got {result}, expected {(-20446744073709551617, -16446744073709551617)}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = MultipleReturns(-1000000000000000000, -9223372036854775805)
        assert result == (-10223372036854775805, 8223372036854775805), f"Test 277 failed: got {result}, expected {(-10223372036854775805, 8223372036854775805)}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = MultipleReturns(-1000000000000000000, -2000000000000000002)
        assert result == (-3000000000000000002, 1000000000000000002), f"Test 278 failed: got {result}, expected {(-3000000000000000002, 1000000000000000002)}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = MultipleReturns(124, -1000000000000000001)
        assert result == (-999999999999999877, 1000000000000000125), f"Test 279 failed: got {result}, expected {(-999999999999999877, 1000000000000000125)}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = MultipleReturns(-2000000000000000000, 0)
        assert result == (-2000000000000000000, -2000000000000000000), f"Test 280 failed: got {result}, expected {(-2000000000000000000, -2000000000000000000)}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = MultipleReturns(-1000000000000000001, -1000000000000000001)
        assert result == (-2000000000000000002, 0), f"Test 281 failed: got {result}, expected {(-2000000000000000002, 0)}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = MultipleReturns(-9223372036854775810, -1000000000000000001)
        assert result == (-10223372036854775811, -8223372036854775809), f"Test 282 failed: got {result}, expected {(-10223372036854775811, -8223372036854775809)}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = MultipleReturns(-914, 0)
        assert result == (-914, -914), f"Test 283 failed: got {result}, expected {(-914, -914)}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = MultipleReturns(-1000000000000000003, -1000000000000000000)
        assert result == (-2000000000000000003, -3), f"Test 284 failed: got {result}, expected {(-2000000000000000003, -3)}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = MultipleReturns(-1000000000000000001, 0)
        assert result == (-1000000000000000001, -1000000000000000001), f"Test 285 failed: got {result}, expected {(-1000000000000000001, -1000000000000000001)}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = MultipleReturns(-1000000000000000001, -1000000000000000000)
        assert result == (-2000000000000000001, -1), f"Test 286 failed: got {result}, expected {(-2000000000000000001, -1)}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = MultipleReturns(5, -914)
        assert result == (-909, 919), f"Test 287 failed: got {result}, expected {(-909, 919)}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = MultipleReturns(-492, -1999999999999999998)
        assert result == (-2000000000000000490, 1999999999999999506), f"Test 288 failed: got {result}, expected {(-2000000000000000490, 1999999999999999506)}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = MultipleReturns(1999999999999999998, 1000000000000000000)
        assert result == (2999999999999999998, 999999999999999998), f"Test 289 failed: got {result}, expected {(2999999999999999998, 999999999999999998)}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = MultipleReturns(9223372036854775808, -1999996)
        assert result == (9223372036852775812, 9223372036856775804), f"Test 290 failed: got {result}, expected {(9223372036852775812, 9223372036856775804)}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = MultipleReturns(-1000000000000000000, -1000000000000000002)
        assert result == (-2000000000000000002, 2), f"Test 291 failed: got {result}, expected {(-2000000000000000002, 2)}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = MultipleReturns(999999999999999999, -1000000000000000000)
        assert result == (-1, 1999999999999999999), f"Test 292 failed: got {result}, expected {(-1, 1999999999999999999)}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = MultipleReturns(2000000000000000002, -1000000000000000001)
        assert result == (1000000000000000001, 3000000000000000003), f"Test 293 failed: got {result}, expected {(1000000000000000001, 3000000000000000003)}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = MultipleReturns(1000000000000000000, -1000000000000000001)
        assert result == (-1, 2000000000000000001), f"Test 294 failed: got {result}, expected {(-1, 2000000000000000001)}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = MultipleReturns(0, -1000000000000000002)
        assert result == (-1000000000000000002, 1000000000000000002), f"Test 295 failed: got {result}, expected {(-1000000000000000002, 1000000000000000002)}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = MultipleReturns(3141592653589793, -999997)
        assert result == (3141592652589796, 3141592654589790), f"Test 296 failed: got {result}, expected {(3141592652589796, 3141592654589790)}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = MultipleReturns(-1000000000000000002, 2147483645)
        assert result == (-999999997852516357, -1000000002147483647), f"Test 297 failed: got {result}, expected {(-999999997852516357, -1000000002147483647)}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = MultipleReturns(169, -1000000000000000000)
        assert result == (-999999999999999831, 1000000000000000169), f"Test 298 failed: got {result}, expected {(-999999999999999831, 1000000000000000169)}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = MultipleReturns(-999999999999999998, 1000000000000000000)
        assert result == (2, -1999999999999999998), f"Test 299 failed: got {result}, expected {(2, -1999999999999999998)}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = MultipleReturns(0, 1000000000000000001)
        assert result == (1000000000000000001, -1000000000000000001), f"Test 300 failed: got {result}, expected {(1000000000000000001, -1000000000000000001)}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = MultipleReturns(44, 10873127313836180)
        assert result == (10873127313836224, -10873127313836136), f"Test 301 failed: got {result}, expected {(10873127313836224, -10873127313836136)}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = MultipleReturns(999996, 999997)
        assert result == (1999993, -1), f"Test 302 failed: got {result}, expected {(1999993, -1)}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = MultipleReturns(-1000000000000000000, 0)
        assert result == (-1000000000000000000, -1000000000000000000), f"Test 303 failed: got {result}, expected {(-1000000000000000000, -1000000000000000000)}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = MultipleReturns(-123, -1000000000000000001)
        assert result == (-1000000000000000124, 999999999999999878), f"Test 304 failed: got {result}, expected {(-1000000000000000124, 999999999999999878)}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = MultipleReturns(-1000000000000000002, -1000000000000000000)
        assert result == (-2000000000000000002, -2), f"Test 305 failed: got {result}, expected {(-2000000000000000002, -2)}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = MultipleReturns(-999999999999999999, 1000000000000000000)
        assert result == (1, -1999999999999999999), f"Test 306 failed: got {result}, expected {(1, -1999999999999999999)}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = MultipleReturns(-18446744073709551614, 1000000000000000001)
        assert result == (-17446744073709551613, -19446744073709551615), f"Test 307 failed: got {result}, expected {(-17446744073709551613, -19446744073709551615)}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = MultipleReturns(-1000000000000000000, 1000000000000000002)
        assert result == (2, -2000000000000000002), f"Test 308 failed: got {result}, expected {(2, -2000000000000000002)}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = MultipleReturns(0, 999999999999999996)
        assert result == (999999999999999996, -999999999999999996), f"Test 309 failed: got {result}, expected {(999999999999999996, -999999999999999996)}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = MultipleReturns(0, 43)
        assert result == (43, -43), f"Test 310 failed: got {result}, expected {(43, -43)}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = MultipleReturns(3141592653589792, -41)
        assert result == (3141592653589751, 3141592653589833), f"Test 311 failed: got {result}, expected {(3141592653589751, 3141592653589833)}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = MultipleReturns(-42, 1000000000000000001)
        assert result == (999999999999999959, -1000000000000000043), f"Test 312 failed: got {result}, expected {(999999999999999959, -1000000000000000043)}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = MultipleReturns(84, 2147483643)
        assert result == (2147483727, -2147483559), f"Test 313 failed: got {result}, expected {(2147483727, -2147483559)}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = MultipleReturns(41, -41)
        assert result == (0, 82), f"Test 314 failed: got {result}, expected {(0, 82)}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = MultipleReturns(42, -18446744073709551616)
        assert result == (-18446744073709551574, 18446744073709551658), f"Test 315 failed: got {result}, expected {(-18446744073709551574, 18446744073709551658)}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = MultipleReturns(42, -44)
        assert result == (-2, 86), f"Test 316 failed: got {result}, expected {(-2, 86)}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = MultipleReturns(-42, 1)
        assert result == (-41, -43), f"Test 317 failed: got {result}, expected {(-41, -43)}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = MultipleReturns(43, -42)
        assert result == (1, 85), f"Test 318 failed: got {result}, expected {(1, 85)}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = MultipleReturns(-42, 84)
        assert result == (42, -126), f"Test 319 failed: got {result}, expected {(42, -126)}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = MultipleReturns(2000000000000000000, -41)
        assert result == (1999999999999999959, 2000000000000000041), f"Test 320 failed: got {result}, expected {(1999999999999999959, 2000000000000000041)}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = MultipleReturns(1, 44)
        assert result == (45, -43), f"Test 321 failed: got {result}, expected {(45, -43)}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = MultipleReturns(65536, -18446744073709551614)
        assert result == (-18446744073709486078, 18446744073709617150), f"Test 322 failed: got {result}, expected {(-18446744073709486078, 18446744073709617150)}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = MultipleReturns(999996, -912)
        assert result == (999084, 1000908), f"Test 323 failed: got {result}, expected {(999084, 1000908)}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = MultipleReturns(0, 42)
        assert result == (42, -42), f"Test 324 failed: got {result}, expected {(42, -42)}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = MultipleReturns(-4294967294, -84)
        assert result == (-4294967378, -4294967210), f"Test 325 failed: got {result}, expected {(-4294967378, -4294967210)}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = MultipleReturns(-42, -42)
        assert result == (-84, 0), f"Test 326 failed: got {result}, expected {(-84, 0)}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = MultipleReturns(-42, 43)
        assert result == (1, -85), f"Test 327 failed: got {result}, expected {(1, -85)}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = MultipleReturns(999998, 42)
        assert result == (1000040, 999956), f"Test 328 failed: got {result}, expected {(1000040, 999956)}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = MultipleReturns(0, -455)
        assert result == (-455, 455), f"Test 329 failed: got {result}, expected {(-455, 455)}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = MultipleReturns(0, 18446744073709551615)
        assert result == (18446744073709551615, -18446744073709551615), f"Test 330 failed: got {result}, expected {(18446744073709551615, -18446744073709551615)}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = MultipleReturns(-456, 13)
        assert result == (-443, -469), f"Test 331 failed: got {result}, expected {(-443, -469)}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = MultipleReturns(-6, -47)
        assert result == (-53, 41), f"Test 332 failed: got {result}, expected {(-53, 41)}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = MultipleReturns(-4294967295, 14)
        assert result == (-4294967281, -4294967309), f"Test 333 failed: got {result}, expected {(-4294967281, -4294967309)}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = MultipleReturns(-16, 1)
        assert result == (-15, -17), f"Test 334 failed: got {result}, expected {(-15, -17)}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = MultipleReturns(7, 0)
        assert result == (7, 7), f"Test 335 failed: got {result}, expected {(7, 7)}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = MultipleReturns(-2718281828459045, 13)
        assert result == (-2718281828459032, -2718281828459058), f"Test 336 failed: got {result}, expected {(-2718281828459032, -2718281828459058)}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = MultipleReturns(0, 123456789012345678901234567890)
        assert result == (123456789012345678901234567890, -123456789012345678901234567890), f"Test 337 failed: got {result}, expected {(123456789012345678901234567890, -123456789012345678901234567890)}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = MultipleReturns(-7, 0)
        assert result == (-7, -7), f"Test 338 failed: got {result}, expected {(-7, -7)}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = MultipleReturns(6, -2)
        assert result == (4, 8), f"Test 339 failed: got {result}, expected {(4, 8)}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = MultipleReturns(7, 28)
        assert result == (35, -21), f"Test 340 failed: got {result}, expected {(35, -21)}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = MultipleReturns(14, 1)
        assert result == (15, 13), f"Test 341 failed: got {result}, expected {(15, 13)}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = MultipleReturns(-14, 26)
        assert result == (12, -40), f"Test 342 failed: got {result}, expected {(12, -40)}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = MultipleReturns(7, 1000000000000000001)
        assert result == (1000000000000000008, -999999999999999994), f"Test 343 failed: got {result}, expected {(1000000000000000008, -999999999999999994)}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = MultipleReturns(7, 455)
        assert result == (462, -448), f"Test 344 failed: got {result}, expected {(462, -448)}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = MultipleReturns(-6, 9223372036854775808)
        assert result == (9223372036854775802, -9223372036854775814), f"Test 345 failed: got {result}, expected {(9223372036854775802, -9223372036854775814)}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = MultipleReturns(-8, 13)
        assert result == (5, -21), f"Test 346 failed: got {result}, expected {(5, -21)}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    # Test case 347
    try:
        result = MultipleReturns(-12, 15)
        assert result == (3, -27), f"Test 347 failed: got {result}, expected {(3, -27)}"
        print(f"Test 347 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 347 failed: {e}")
        test_results.append(False)

    # Test case 348
    try:
        result = MultipleReturns(-16, -16)
        assert result == (-32, 0), f"Test 348 failed: got {result}, expected {(-32, 0)}"
        print(f"Test 348 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 348 failed: {e}")
        test_results.append(False)

    # Test case 349
    try:
        result = MultipleReturns(-7, -16)
        assert result == (-23, 9), f"Test 349 failed: got {result}, expected {(-23, 9)}"
        print(f"Test 349 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 349 failed: {e}")
        test_results.append(False)

    # Test case 350
    try:
        result = MultipleReturns(7, -52)
        assert result == (-45, 59), f"Test 350 failed: got {result}, expected {(-45, 59)}"
        print(f"Test 350 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 350 failed: {e}")
        test_results.append(False)

    # Test case 351
    try:
        result = MultipleReturns(6, -9)
        assert result == (-3, 15), f"Test 351 failed: got {result}, expected {(-3, 15)}"
        print(f"Test 351 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 351 failed: {e}")
        test_results.append(False)

    # Test case 352
    try:
        result = MultipleReturns(122, -12)
        assert result == (110, 134), f"Test 352 failed: got {result}, expected {(110, 134)}"
        print(f"Test 352 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 352 failed: {e}")
        test_results.append(False)

    # Test case 353
    try:
        result = MultipleReturns(6, 0)
        assert result == (6, 6), f"Test 353 failed: got {result}, expected {(6, 6)}"
        print(f"Test 353 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 353 failed: {e}")
        test_results.append(False)

    # Test case 354
    try:
        result = MultipleReturns(12, -14)
        assert result == (-2, 26), f"Test 354 failed: got {result}, expected {(-2, 26)}"
        print(f"Test 354 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 354 failed: {e}")
        test_results.append(False)

    # Test case 355
    try:
        result = MultipleReturns(7, -999997)
        assert result == (-999990, 1000004), f"Test 355 failed: got {result}, expected {(-999990, 1000004)}"
        print(f"Test 355 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 355 failed: {e}")
        test_results.append(False)

    # Test case 356
    try:
        result = MultipleReturns(-122, -10873127313836180)
        assert result == (-10873127313836302, 10873127313836058), f"Test 356 failed: got {result}, expected {(-10873127313836302, 10873127313836058)}"
        print(f"Test 356 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 356 failed: {e}")
        test_results.append(False)

    # Test case 357
    try:
        result = MultipleReturns(0, -2147483647)
        assert result == (-2147483647, 2147483647), f"Test 357 failed: got {result}, expected {(-2147483647, 2147483647)}"
        print(f"Test 357 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 357 failed: {e}")
        test_results.append(False)

    # Test case 358
    try:
        result = MultipleReturns(-7, -44)
        assert result == (-51, 37), f"Test 358 failed: got {result}, expected {(-51, 37)}"
        print(f"Test 358 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 358 failed: {e}")
        test_results.append(False)

    # Test case 359
    try:
        result = MultipleReturns(-7, -8)
        assert result == (-15, 1), f"Test 359 failed: got {result}, expected {(-15, 1)}"
        print(f"Test 359 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 359 failed: {e}")
        test_results.append(False)

    # Test case 360
    try:
        result = MultipleReturns(-2147483647, 13)
        assert result == (-2147483634, -2147483660), f"Test 360 failed: got {result}, expected {(-2147483634, -2147483660)}"
        print(f"Test 360 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 360 failed: {e}")
        test_results.append(False)

    # Test case 361
    try:
        result = MultipleReturns(-912, 0)
        assert result == (-912, -912), f"Test 361 failed: got {result}, expected {(-912, -912)}"
        print(f"Test 361 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 361 failed: {e}")
        test_results.append(False)

    # Test case 362
    try:
        result = MultipleReturns(2147483644, 0)
        assert result == (2147483644, 2147483644), f"Test 362 failed: got {result}, expected {(2147483644, 2147483644)}"
        print(f"Test 362 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 362 failed: {e}")
        test_results.append(False)

    # Test case 363
    try:
        result = MultipleReturns(10, -13)
        assert result == (-3, 23), f"Test 363 failed: got {result}, expected {(-3, 23)}"
        print(f"Test 363 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 363 failed: {e}")
        test_results.append(False)

    # Test case 364
    try:
        result = MultipleReturns(40, -125)
        assert result == (-85, 165), f"Test 364 failed: got {result}, expected {(-85, 165)}"
        print(f"Test 364 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 364 failed: {e}")
        test_results.append(False)

    # Test case 365
    try:
        result = MultipleReturns(-2147483650, -2000000000000000002)
        assert result == (-2000000002147483652, 1999999997852516352), f"Test 365 failed: got {result}, expected {(-2000000002147483652, 1999999997852516352)}"
        print(f"Test 365 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 365 failed: {e}")
        test_results.append(False)

    # Test case 366
    try:
        result = MultipleReturns(999997, 1000002)
        assert result == (1999999, -5), f"Test 366 failed: got {result}, expected {(1999999, -5)}"
        print(f"Test 366 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 366 failed: {e}")
        test_results.append(False)

    # Test case 367
    try:
        result = MultipleReturns(65536, 2718281828459046)
        assert result == (2718281828524582, -2718281828393510), f"Test 367 failed: got {result}, expected {(2718281828524582, -2718281828393510)}"
        print(f"Test 367 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 367 failed: {e}")
        test_results.append(False)

    # Test case 368
    try:
        result = MultipleReturns(-3141592653589793, 18446744073709551619)
        assert result == (18443602481055961826, -18449885666363141412), f"Test 368 failed: got {result}, expected {(18443602481055961826, -18449885666363141412)}"
        print(f"Test 368 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 368 failed: {e}")
        test_results.append(False)

    # Test case 369
    try:
        result = MultipleReturns(3141592653589794, 2718281828459044)
        assert result == (5859874482048838, 423310825130750), f"Test 369 failed: got {result}, expected {(5859874482048838, 423310825130750)}"
        print(f"Test 369 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 369 failed: {e}")
        test_results.append(False)

    # Test case 370
    try:
        result = MultipleReturns(6283185307179586, -1)
        assert result == (6283185307179585, 6283185307179587), f"Test 370 failed: got {result}, expected {(6283185307179585, 6283185307179587)}"
        print(f"Test 370 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 370 failed: {e}")
        test_results.append(False)

    # Test case 371
    try:
        result = MultipleReturns(-16, 2718281828459046)
        assert result == (2718281828459030, -2718281828459062), f"Test 371 failed: got {result}, expected {(2718281828459030, -2718281828459062)}"
        print(f"Test 371 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 371 failed: {e}")
        test_results.append(False)

    # Test case 372
    try:
        result = MultipleReturns(10873127313836181, 2718281828459045)
        assert result == (13591409142295226, 8154845485377136), f"Test 372 failed: got {result}, expected {(13591409142295226, 8154845485377136)}"
        print(f"Test 372 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 372 failed: {e}")
        test_results.append(False)

    # Test case 373
    try:
        result = MultipleReturns(6283185307179587, -1)
        assert result == (6283185307179586, 6283185307179588), f"Test 373 failed: got {result}, expected {(6283185307179586, 6283185307179588)}"
        print(f"Test 373 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 373 failed: {e}")
        test_results.append(False)

    # Test case 374
    try:
        result = MultipleReturns(25, 999999999999999999)
        assert result == (1000000000000000024, -999999999999999974), f"Test 374 failed: got {result}, expected {(1000000000000000024, -999999999999999974)}"
        print(f"Test 374 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 374 failed: {e}")
        test_results.append(False)

    # Test case 375
    try:
        result = MultipleReturns(-3141592653589793, -999999999999999998)
        assert result == (-1003141592653589791, 996858407346410205), f"Test 375 failed: got {result}, expected {(-1003141592653589791, 996858407346410205)}"
        print(f"Test 375 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 375 failed: {e}")
        test_results.append(False)

    # Test case 376
    try:
        result = MultipleReturns(-912, -2718281828459044)
        assert result == (-2718281828459956, 2718281828458132), f"Test 376 failed: got {result}, expected {(-2718281828459956, 2718281828458132)}"
        print(f"Test 376 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 376 failed: {e}")
        test_results.append(False)

    # Test case 377
    try:
        result = MultipleReturns(-123456789012345678901234567890, -2718281828459047)
        assert result == (-123456789012348397183063026937, -123456789012342960619406108843), f"Test 377 failed: got {result}, expected {(-123456789012348397183063026937, -123456789012342960619406108843)}"
        print(f"Test 377 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 377 failed: {e}")
        test_results.append(False)

    # Test case 378
    try:
        result = MultipleReturns(-3141592653589793, 247)
        assert result == (-3141592653589546, -3141592653590040), f"Test 378 failed: got {result}, expected {(-3141592653589546, -3141592653590040)}"
        print(f"Test 378 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 378 failed: {e}")
        test_results.append(False)

    # Test case 379
    try:
        result = MultipleReturns(3141592653589793, 5436563656918090)
        assert result == (8578156310507883, -2294971003328297), f"Test 379 failed: got {result}, expected {(8578156310507883, -2294971003328297)}"
        print(f"Test 379 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 379 failed: {e}")
        test_results.append(False)

    # Test case 380
    try:
        result = MultipleReturns(-3141592653589794, 2718281828459046)
        assert result == (-423310825130748, -5859874482048840), f"Test 380 failed: got {result}, expected {(-423310825130748, -5859874482048840)}"
        print(f"Test 380 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 380 failed: {e}")
        test_results.append(False)

    # Test case 381
    try:
        result = MultipleReturns(-3141592653589793, 2718281828459044)
        assert result == (-423310825130749, -5859874482048837), f"Test 381 failed: got {result}, expected {(-423310825130749, -5859874482048837)}"
        print(f"Test 381 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 381 failed: {e}")
        test_results.append(False)

    # Test case 382
    try:
        result = MultipleReturns(-1000000000000000003, -14)
        assert result == (-1000000000000000017, -999999999999999989), f"Test 382 failed: got {result}, expected {(-1000000000000000017, -999999999999999989)}"
        print(f"Test 382 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 382 failed: {e}")
        test_results.append(False)

    # Test case 383
    try:
        result = MultipleReturns(-3141592653589793, -2718281828459044)
        assert result == (-5859874482048837, -423310825130749), f"Test 383 failed: got {result}, expected {(-5859874482048837, -423310825130749)}"
        print(f"Test 383 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 383 failed: {e}")
        test_results.append(False)

    # Test case 384
    try:
        result = MultipleReturns(1000000000000000002, 2718281828459045)
        assert result == (1002718281828459047, 997281718171540957), f"Test 384 failed: got {result}, expected {(1002718281828459047, 997281718171540957)}"
        print(f"Test 384 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 384 failed: {e}")
        test_results.append(False)

    # Test case 385
    try:
        result = MultipleReturns(-3141592653589793, -2718281828459046)
        assert result == (-5859874482048839, -423310825130747), f"Test 385 failed: got {result}, expected {(-5859874482048839, -423310825130747)}"
        print(f"Test 385 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 385 failed: {e}")
        test_results.append(False)

    # Test case 386
    try:
        result = MultipleReturns(0, -2718281828459046)
        assert result == (-2718281828459046, 2718281828459046), f"Test 386 failed: got {result}, expected {(-2718281828459046, 2718281828459046)}"
        print(f"Test 386 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 386 failed: {e}")
        test_results.append(False)

    # Test case 387
    try:
        result = MultipleReturns(-9223372036854775810, -2718281828459044)
        assert result == (-9226090318683234854, -9220653755026316766), f"Test 387 failed: got {result}, expected {(-9226090318683234854, -9220653755026316766)}"
        print(f"Test 387 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 387 failed: {e}")
        test_results.append(False)

    # Test case 388
    try:
        result = MultipleReturns(9223372036854775807, -14)
        assert result == (9223372036854775793, 9223372036854775821), f"Test 388 failed: got {result}, expected {(9223372036854775793, 9223372036854775821)}"
        print(f"Test 388 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 388 failed: {e}")
        test_results.append(False)

    # Test case 389
    try:
        result = MultipleReturns(0, -5436563656918090)
        assert result == (-5436563656918090, 5436563656918090), f"Test 389 failed: got {result}, expected {(-5436563656918090, 5436563656918090)}"
        print(f"Test 389 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 389 failed: {e}")
        test_results.append(False)

    # Test case 390
    try:
        result = MultipleReturns(1000000, -1000000000000000003)
        assert result == (-999999999999000003, 1000000000001000003), f"Test 390 failed: got {result}, expected {(-999999999999000003, 1000000000001000003)}"
        print(f"Test 390 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 390 failed: {e}")
        test_results.append(False)

    # Test case 391
    try:
        result = MultipleReturns(-1999995, -2718281828459044)
        assert result == (-2718281830459039, 2718281826459049), f"Test 391 failed: got {result}, expected {(-2718281830459039, 2718281826459049)}"
        print(f"Test 391 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 391 failed: {e}")
        test_results.append(False)

    # Test case 392
    try:
        result = MultipleReturns(-43, -2718281828459045)
        assert result == (-2718281828459088, 2718281828459002), f"Test 392 failed: got {result}, expected {(-2718281828459088, 2718281828459002)}"
        print(f"Test 392 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 392 failed: {e}")
        test_results.append(False)

    # Test case 393
    try:
        result = MultipleReturns(2718281828459046, -2718281828459045)
        assert result == (1, 5436563656918091), f"Test 393 failed: got {result}, expected {(1, 5436563656918091)}"
        print(f"Test 393 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 393 failed: {e}")
        test_results.append(False)

    # Test case 394
    try:
        result = MultipleReturns(6283185307179584, -1)
        assert result == (6283185307179583, 6283185307179585), f"Test 394 failed: got {result}, expected {(6283185307179583, 6283185307179585)}"
        print(f"Test 394 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 394 failed: {e}")
        test_results.append(False)

    # Test case 395
    try:
        result = MultipleReturns(3141592653589793, 0)
        assert result == (3141592653589793, 3141592653589793), f"Test 395 failed: got {result}, expected {(3141592653589793, 3141592653589793)}"
        print(f"Test 395 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 395 failed: {e}")
        test_results.append(False)

    # Test case 396
    try:
        result = MultipleReturns(2147483643, 1)
        assert result == (2147483644, 2147483642), f"Test 396 failed: got {result}, expected {(2147483644, 2147483642)}"
        print(f"Test 396 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 396 failed: {e}")
        test_results.append(False)

    # Test case 397
    try:
        result = MultipleReturns(-4294967296, -1000000000000000000)
        assert result == (-1000000004294967296, 999999995705032704), f"Test 397 failed: got {result}, expected {(-1000000004294967296, 999999995705032704)}"
        print(f"Test 397 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 397 failed: {e}")
        test_results.append(False)

    # Test case 398
    try:
        result = MultipleReturns(3141592653589793, -2718281828459047)
        assert result == (423310825130746, 5859874482048840), f"Test 398 failed: got {result}, expected {(423310825130746, 5859874482048840)}"
        print(f"Test 398 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 398 failed: {e}")
        test_results.append(False)

    # Test case 399
    try:
        result = MultipleReturns(-8589934590, -2718281828459044)
        assert result == (-2718290418393634, 2718273238524454), f"Test 399 failed: got {result}, expected {(-2718290418393634, 2718273238524454)}"
        print(f"Test 399 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 399 failed: {e}")
        test_results.append(False)

    # Test case 400
    try:
        result = MultipleReturns(-3141592653589793, 5436563656918089)
        assert result == (2294971003328296, -8578156310507882), f"Test 400 failed: got {result}, expected {(2294971003328296, -8578156310507882)}"
        print(f"Test 400 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 400 failed: {e}")
        test_results.append(False)

    # Test case 401
    try:
        result = MultipleReturns(-912, -5436563656918091)
        assert result == (-5436563656919003, 5436563656917179), f"Test 401 failed: got {result}, expected {(-5436563656919003, 5436563656917179)}"
        print(f"Test 401 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 401 failed: {e}")
        test_results.append(False)

    # Test case 402
    try:
        result = MultipleReturns(-3141592653589794, 2000000000000000002)
        assert result == (1996858407346410208, -2003141592653589796), f"Test 402 failed: got {result}, expected {(1996858407346410208, -2003141592653589796)}"
        print(f"Test 402 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 402 failed: {e}")
        test_results.append(False)

    # Test case 403
    try:
        result = MultipleReturns(-1826, -5436563656918089)
        assert result == (-5436563656919915, 5436563656916263), f"Test 403 failed: got {result}, expected {(-5436563656919915, 5436563656916263)}"
        print(f"Test 403 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 403 failed: {e}")
        test_results.append(False)

    # Test case 404
    try:
        result = MultipleReturns(-18446744073709551614, -5436563656918090)
        assert result == (-18452180637366469704, -18441307510052633524), f"Test 404 failed: got {result}, expected {(-18452180637366469704, -18441307510052633524)}"
        print(f"Test 404 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 404 failed: {e}")
        test_results.append(False)

    # Test case 405
    try:
        result = MultipleReturns(18446744073709551613, -2000000000000000000)
        assert result == (16446744073709551613, 20446744073709551613), f"Test 405 failed: got {result}, expected {(16446744073709551613, 20446744073709551613)}"
        print(f"Test 405 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 405 failed: {e}")
        test_results.append(False)

    # Test case 406
    try:
        result = MultipleReturns(18446744073709551615, 0)
        assert result == (18446744073709551615, 18446744073709551615), f"Test 406 failed: got {result}, expected {(18446744073709551615, 18446744073709551615)}"
        print(f"Test 406 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 406 failed: {e}")
        test_results.append(False)

    # Test case 407
    try:
        result = MultipleReturns(18446744073709551615, -912)
        assert result == (18446744073709550703, 18446744073709552527), f"Test 407 failed: got {result}, expected {(18446744073709550703, 18446744073709552527)}"
        print(f"Test 407 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 407 failed: {e}")
        test_results.append(False)

    # Test case 408
    try:
        result = MultipleReturns(-3650, 1000000000000000000)
        assert result == (999999999999996350, -1000000000000003650), f"Test 408 failed: got {result}, expected {(999999999999996350, -1000000000000003650)}"
        print(f"Test 408 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 408 failed: {e}")
        test_results.append(False)

    # Test case 409
    try:
        result = MultipleReturns(-13, 1)
        assert result == (-12, -14), f"Test 409 failed: got {result}, expected {(-12, -14)}"
        print(f"Test 409 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 409 failed: {e}")
        test_results.append(False)

    # Test case 410
    try:
        result = MultipleReturns(-9223372036854775806, -12566370614359176)
        assert result == (-9235938407469134982, -9210805666240416630), f"Test 410 failed: got {result}, expected {(-9235938407469134982, -9210805666240416630)}"
        print(f"Test 410 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 410 failed: {e}")
        test_results.append(False)

    # Test case 411
    try:
        result = MultipleReturns(18446744073709551613, -1)
        assert result == (18446744073709551612, 18446744073709551614), f"Test 411 failed: got {result}, expected {(18446744073709551612, 18446744073709551614)}"
        print(f"Test 411 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 411 failed: {e}")
        test_results.append(False)

    # Test case 412
    try:
        result = MultipleReturns(18446744073709551614, -9223372036854775805)
        assert result == (9223372036854775809, 27670116110564327419), f"Test 412 failed: got {result}, expected {(9223372036854775809, 27670116110564327419)}"
        print(f"Test 412 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 412 failed: {e}")
        test_results.append(False)

    # Test case 413
    try:
        result = MultipleReturns(2147483649, 1)
        assert result == (2147483650, 2147483648), f"Test 413 failed: got {result}, expected {(2147483650, 2147483648)}"
        print(f"Test 413 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 413 failed: {e}")
        test_results.append(False)

    # Test case 414
    try:
        result = MultipleReturns(10873127313836180, -1)
        assert result == (10873127313836179, 10873127313836181), f"Test 414 failed: got {result}, expected {(10873127313836179, 10873127313836181)}"
        print(f"Test 414 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 414 failed: {e}")
        test_results.append(False)

    # Test case 415
    try:
        result = MultipleReturns(-18446744073709551615, -4)
        assert result == (-18446744073709551619, -18446744073709551611), f"Test 415 failed: got {result}, expected {(-18446744073709551619, -18446744073709551611)}"
        print(f"Test 415 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 415 failed: {e}")
        test_results.append(False)

    # Test case 416
    try:
        result = MultipleReturns(-18446744073709551616, -3)
        assert result == (-18446744073709551619, -18446744073709551613), f"Test 416 failed: got {result}, expected {(-18446744073709551619, -18446744073709551613)}"
        print(f"Test 416 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 416 failed: {e}")
        test_results.append(False)

    # Test case 417
    try:
        result = MultipleReturns(-18446744073709551615, 0)
        assert result == (-18446744073709551615, -18446744073709551615), f"Test 417 failed: got {result}, expected {(-18446744073709551615, -18446744073709551615)}"
        print(f"Test 417 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 417 failed: {e}")
        test_results.append(False)

    # Test case 418
    try:
        result = MultipleReturns(-37, 2)
        assert result == (-35, -39), f"Test 418 failed: got {result}, expected {(-35, -39)}"
        print(f"Test 418 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 418 failed: {e}")
        test_results.append(False)

    # Test case 419
    try:
        result = MultipleReturns(-18446744073709551616, -1999995)
        assert result == (-18446744073711551611, -18446744073707551621), f"Test 419 failed: got {result}, expected {(-18446744073711551611, -18446744073707551621)}"
        print(f"Test 419 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 419 failed: {e}")
        test_results.append(False)

    # Test case 420
    try:
        result = MultipleReturns(8, -911)
        assert result == (-903, 919), f"Test 420 failed: got {result}, expected {(-903, 919)}"
        print(f"Test 420 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 420 failed: {e}")
        test_results.append(False)

    # Test case 421
    try:
        result = MultipleReturns(-18446744073709551616, 1)
        assert result == (-18446744073709551615, -18446744073709551617), f"Test 421 failed: got {result}, expected {(-18446744073709551615, -18446744073709551617)}"
        print(f"Test 421 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 421 failed: {e}")
        test_results.append(False)

    # Test case 422
    try:
        result = MultipleReturns(-1999996, 15)
        assert result == (-1999981, -2000011), f"Test 422 failed: got {result}, expected {(-1999981, -2000011)}"
        print(f"Test 422 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 422 failed: {e}")
        test_results.append(False)

    # Test case 423
    try:
        result = MultipleReturns(4294967295, -123456789012345678901234567890)
        assert result == (-123456789012345678896939600595, 123456789012345678905529535185), f"Test 423 failed: got {result}, expected {(-123456789012345678896939600595, 123456789012345678905529535185)}"
        print(f"Test 423 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 423 failed: {e}")
        test_results.append(False)

    # Test case 424
    try:
        result = MultipleReturns(4294967293, -4294967296)
        assert result == (-3, 8589934589), f"Test 424 failed: got {result}, expected {(-3, 8589934589)}"
        print(f"Test 424 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 424 failed: {e}")
        test_results.append(False)

    # Test case 425
    try:
        result = MultipleReturns(-48, -4294967296)
        assert result == (-4294967344, 4294967248), f"Test 425 failed: got {result}, expected {(-4294967344, 4294967248)}"
        print(f"Test 425 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 425 failed: {e}")
        test_results.append(False)

    # Test case 426
    try:
        result = MultipleReturns(4294967295, -4294967297)
        assert result == (-2, 8589934592), f"Test 426 failed: got {result}, expected {(-2, 8589934592)}"
        print(f"Test 426 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 426 failed: {e}")
        test_results.append(False)

    # Test case 427
    try:
        result = MultipleReturns(8589934592, -2718281828459047)
        assert result == (-2718273238524455, 2718290418393639), f"Test 427 failed: got {result}, expected {(-2718273238524455, 2718290418393639)}"
        print(f"Test 427 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 427 failed: {e}")
        test_results.append(False)

    # Test case 428
    try:
        result = MultipleReturns(8, 2000000000000000002)
        assert result == (2000000000000000010, -1999999999999999994), f"Test 428 failed: got {result}, expected {(2000000000000000010, -1999999999999999994)}"
        print(f"Test 428 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 428 failed: {e}")
        test_results.append(False)

    # Test case 429
    try:
        result = MultipleReturns(-452, 0)
        assert result == (-452, -452), f"Test 429 failed: got {result}, expected {(-452, -452)}"
        print(f"Test 429 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 429 failed: {e}")
        test_results.append(False)

    # Test case 430
    try:
        result = MultipleReturns(-8589934592, 4294967296)
        assert result == (-4294967296, -12884901888), f"Test 430 failed: got {result}, expected {(-4294967296, -12884901888)}"
        print(f"Test 430 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 430 failed: {e}")
        test_results.append(False)

    # Test case 431
    try:
        result = MultipleReturns(4294967296, 4294967297)
        assert result == (8589934593, -1), f"Test 431 failed: got {result}, expected {(8589934593, -1)}"
        print(f"Test 431 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 431 failed: {e}")
        test_results.append(False)

    # Test case 432
    try:
        result = MultipleReturns(9223372036854775811, -3141592653589792)
        assert result == (9220230444201186019, 9226513629508365603), f"Test 432 failed: got {result}, expected {(9220230444201186019, 9226513629508365603)}"
        print(f"Test 432 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 432 failed: {e}")
        test_results.append(False)

    # Test case 433
    try:
        result = MultipleReturns(-48, 4294967296)
        assert result == (4294967248, -4294967344), f"Test 433 failed: got {result}, expected {(4294967248, -4294967344)}"
        print(f"Test 433 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 433 failed: {e}")
        test_results.append(False)

    # Test case 434
    try:
        result = MultipleReturns(-9223372036854775805, 0)
        assert result == (-9223372036854775805, -9223372036854775805), f"Test 434 failed: got {result}, expected {(-9223372036854775805, -9223372036854775805)}"
        print(f"Test 434 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 434 failed: {e}")
        test_results.append(False)

    # Test case 435
    try:
        result = MultipleReturns(-4294967297, -4294967296)
        assert result == (-8589934593, -1), f"Test 435 failed: got {result}, expected {(-8589934593, -1)}"
        print(f"Test 435 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 435 failed: {e}")
        test_results.append(False)

    # Test case 436
    try:
        result = MultipleReturns(-83, 6283185307179588)
        assert result == (6283185307179505, -6283185307179671), f"Test 436 failed: got {result}, expected {(6283185307179505, -6283185307179671)}"
        print(f"Test 436 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 436 failed: {e}")
        test_results.append(False)

    # Test case 437
    try:
        result = MultipleReturns(-1825, -4294967296)
        assert result == (-4294969121, 4294965471), f"Test 437 failed: got {result}, expected {(-4294969121, 4294965471)}"
        print(f"Test 437 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 437 failed: {e}")
        test_results.append(False)

    # Test case 438
    try:
        result = MultipleReturns(8589934592, -9223372036854775808)
        assert result == (-9223372028264841216, 9223372045444710400), f"Test 438 failed: got {result}, expected {(-9223372028264841216, 9223372045444710400)}"
        print(f"Test 438 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 438 failed: {e}")
        test_results.append(False)

    # Test case 439
    try:
        result = MultipleReturns(-999998, 0)
        assert result == (-999998, -999998), f"Test 439 failed: got {result}, expected {(-999998, -999998)}"
        print(f"Test 439 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 439 failed: {e}")
        test_results.append(False)

    # Test case 440
    try:
        result = MultipleReturns(0, -65537)
        assert result == (-65537, 65537), f"Test 440 failed: got {result}, expected {(-65537, 65537)}"
        print(f"Test 440 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 440 failed: {e}")
        test_results.append(False)

    # Test case 441
    try:
        result = MultipleReturns(-10873127313836180, -2147483647)
        assert result == (-10873129461319827, -10873125166352533), f"Test 441 failed: got {result}, expected {(-10873129461319827, -10873125166352533)}"
        print(f"Test 441 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 441 failed: {e}")
        test_results.append(False)

    # Test case 442
    try:
        result = MultipleReturns(65536, 169)
        assert result == (65705, 65367), f"Test 442 failed: got {result}, expected {(65705, 65367)}"
        print(f"Test 442 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 442 failed: {e}")
        test_results.append(False)

    # Test case 443
    try:
        result = MultipleReturns(3141592653589794, -131072)
        assert result == (3141592653458722, 3141592653720866), f"Test 443 failed: got {result}, expected {(3141592653458722, 3141592653720866)}"
        print(f"Test 443 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 443 failed: {e}")
        test_results.append(False)

    # Test case 444
    try:
        result = MultipleReturns(65534, -65536)
        assert result == (-2, 131070), f"Test 444 failed: got {result}, expected {(-2, 131070)}"
        print(f"Test 444 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 444 failed: {e}")
        test_results.append(False)

    # Test case 445
    try:
        result = MultipleReturns(124, -65537)
        assert result == (-65413, 65661), f"Test 445 failed: got {result}, expected {(-65413, 65661)}"
        print(f"Test 445 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 445 failed: {e}")
        test_results.append(False)

    # Test case 446
    try:
        result = MultipleReturns(0, -131076)
        assert result == (-131076, 131076), f"Test 446 failed: got {result}, expected {(-131076, 131076)}"
        print(f"Test 446 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 446 failed: {e}")
        test_results.append(False)

    # Test case 447
    try:
        result = MultipleReturns(494, -65532)
        assert result == (-65038, 66026), f"Test 447 failed: got {result}, expected {(-65038, 66026)}"
        print(f"Test 447 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 447 failed: {e}")
        test_results.append(False)

    # Test case 448
    try:
        result = MultipleReturns(-65535, -16)
        assert result == (-65551, -65519), f"Test 448 failed: got {result}, expected {(-65551, -65519)}"
        print(f"Test 448 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 448 failed: {e}")
        test_results.append(False)

    # Test case 449
    try:
        result = MultipleReturns(65535, -491)
        assert result == (65044, 66026), f"Test 449 failed: got {result}, expected {(65044, 66026)}"
        print(f"Test 449 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 449 failed: {e}")
        test_results.append(False)

    # Test case 450
    try:
        result = MultipleReturns(131070, 12)
        assert result == (131082, 131058), f"Test 450 failed: got {result}, expected {(131082, 131058)}"
        print(f"Test 450 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 450 failed: {e}")
        test_results.append(False)

    # Test case 451
    try:
        result = MultipleReturns(0, 65536)
        assert result == (65536, -65536), f"Test 451 failed: got {result}, expected {(65536, -65536)}"
        print(f"Test 451 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 451 failed: {e}")
        test_results.append(False)

    # Test case 452
    try:
        result = MultipleReturns(65535, 65536)
        assert result == (131071, -1), f"Test 452 failed: got {result}, expected {(131071, -1)}"
        print(f"Test 452 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 452 failed: {e}")
        test_results.append(False)

    # Test case 453
    try:
        result = MultipleReturns(-65535, 65535)
        assert result == (0, -131070), f"Test 453 failed: got {result}, expected {(0, -131070)}"
        print(f"Test 453 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 453 failed: {e}")
        test_results.append(False)

    # Test case 454
    try:
        result = MultipleReturns(-11, 131072)
        assert result == (131061, -131083), f"Test 454 failed: got {result}, expected {(131061, -131083)}"
        print(f"Test 454 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 454 failed: {e}")
        test_results.append(False)

    # Test case 455
    try:
        result = MultipleReturns(-131070, 65536)
        assert result == (-65534, -196606), f"Test 455 failed: got {result}, expected {(-65534, -196606)}"
        print(f"Test 455 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 455 failed: {e}")
        test_results.append(False)

    # Test case 456
    try:
        result = MultipleReturns(-131071, -65536)
        assert result == (-196607, -65535), f"Test 456 failed: got {result}, expected {(-196607, -65535)}"
        print(f"Test 456 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 456 failed: {e}")
        test_results.append(False)

    # Test case 457
    try:
        result = MultipleReturns(-131069, -65537)
        assert result == (-196606, -65532), f"Test 457 failed: got {result}, expected {(-196606, -65532)}"
        print(f"Test 457 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 457 failed: {e}")
        test_results.append(False)

    # Test case 458
    try:
        result = MultipleReturns(-65536, -131069)
        assert result == (-196605, 65533), f"Test 458 failed: got {result}, expected {(-196605, 65533)}"
        print(f"Test 458 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 458 failed: {e}")
        test_results.append(False)

    # Test case 459
    try:
        result = MultipleReturns(0, -65535)
        assert result == (-65535, 65535), f"Test 459 failed: got {result}, expected {(-65535, 65535)}"
        print(f"Test 459 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 459 failed: {e}")
        test_results.append(False)

    # Test case 460
    try:
        result = MultipleReturns(8589934592, 4294967293)
        assert result == (12884901885, 4294967299), f"Test 460 failed: got {result}, expected {(12884901885, 4294967299)}"
        print(f"Test 460 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 460 failed: {e}")
        test_results.append(False)

    # Test case 461
    try:
        result = MultipleReturns(123456789012345678901234567890, -248)
        assert result == (123456789012345678901234567642, 123456789012345678901234568138), f"Test 461 failed: got {result}, expected {(123456789012345678901234567642, 123456789012345678901234568138)}"
        print(f"Test 461 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 461 failed: {e}")
        test_results.append(False)

    # Test case 462
    try:
        result = MultipleReturns(246913578024691357802469135780, -9)
        assert result == (246913578024691357802469135771, 246913578024691357802469135789), f"Test 462 failed: got {result}, expected {(246913578024691357802469135771, 246913578024691357802469135789)}"
        print(f"Test 462 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 462 failed: {e}")
        test_results.append(False)

    # Test case 463
    try:
        result = MultipleReturns(122, -9223372036854775808)
        assert result == (-9223372036854775686, 9223372036854775930), f"Test 463 failed: got {result}, expected {(-9223372036854775686, 9223372036854775930)}"
        print(f"Test 463 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 463 failed: {e}")
        test_results.append(False)

    # Test case 464
    try:
        result = MultipleReturns(-18446744073709551615, -2147483648)
        assert result == (-18446744075857035263, -18446744071562067967), f"Test 464 failed: got {result}, expected {(-18446744075857035263, -18446744071562067967)}"
        print(f"Test 464 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 464 failed: {e}")
        test_results.append(False)

    # Test case 465
    try:
        result = MultipleReturns(-123456789012345678901234567890, -246913578024691357802469135780)
        assert result == (-370370367037037036703703703670, 123456789012345678901234567890), f"Test 465 failed: got {result}, expected {(-370370367037037036703703703670, 123456789012345678901234567890)}"
        print(f"Test 465 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 465 failed: {e}")
        test_results.append(False)

    # Test case 466
    try:
        result = MultipleReturns(-123456789012345678901234567890, -123456789012345678901234567891)
        assert result == (-246913578024691357802469135781, 1), f"Test 466 failed: got {result}, expected {(-246913578024691357802469135781, 1)}"
        print(f"Test 466 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 466 failed: {e}")
        test_results.append(False)

    # Test case 467
    try:
        result = MultipleReturns(123456789012345678901234567890, -85)
        assert result == (123456789012345678901234567805, 123456789012345678901234567975), f"Test 467 failed: got {result}, expected {(123456789012345678901234567805, 123456789012345678901234567975)}"
        print(f"Test 467 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 467 failed: {e}")
        test_results.append(False)

    # Test case 468
    try:
        result = MultipleReturns(-10873127313836181, 0)
        assert result == (-10873127313836181, -10873127313836181), f"Test 468 failed: got {result}, expected {(-10873127313836181, -10873127313836181)}"
        print(f"Test 468 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 468 failed: {e}")
        test_results.append(False)

    # Test case 469
    try:
        result = MultipleReturns(-44, -123456789012345678901234567890)
        assert result == (-123456789012345678901234567934, 123456789012345678901234567846), f"Test 469 failed: got {result}, expected {(-123456789012345678901234567934, 123456789012345678901234567846)}"
        print(f"Test 469 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 469 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
