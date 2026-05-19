# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def DoubleQuadruple(x):
2: ✓     return (2 * x, 4 * x)
```

## Complete Test File

```python
def DoubleQuadruple(x):
    return (2 * x, 4 * x)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = DoubleQuadruple(0)
        assert result == (0, 0), f"Test 1 failed: got {result}, expected {(0, 0)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = DoubleQuadruple(1)
        assert result == (2, 4), f"Test 2 failed: got {result}, expected {(2, 4)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = DoubleQuadruple(-1)
        assert result == (-2, -4), f"Test 3 failed: got {result}, expected {(-2, -4)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = DoubleQuadruple(10)
        assert result == (20, 40), f"Test 4 failed: got {result}, expected {(20, 40)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = DoubleQuadruple(-5)
        assert result == (-10, -20), f"Test 5 failed: got {result}, expected {(-10, -20)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = DoubleQuadruple(2)
        assert result == (4, 8), f"Test 6 failed: got {result}, expected {(4, 8)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = DoubleQuadruple(-2)
        assert result == (-4, -8), f"Test 7 failed: got {result}, expected {(-4, -8)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = DoubleQuadruple(7)
        assert result == (14, 28), f"Test 8 failed: got {result}, expected {(14, 28)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = DoubleQuadruple(-7)
        assert result == (-14, -28), f"Test 9 failed: got {result}, expected {(-14, -28)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = DoubleQuadruple(-10)
        assert result == (-20, -40), f"Test 10 failed: got {result}, expected {(-20, -40)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = DoubleQuadruple(99)
        assert result == (198, 396), f"Test 11 failed: got {result}, expected {(198, 396)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = DoubleQuadruple(-99)
        assert result == (-198, -396), f"Test 12 failed: got {result}, expected {(-198, -396)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = DoubleQuadruple(123456)
        assert result == (246912, 493824), f"Test 13 failed: got {result}, expected {(246912, 493824)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = DoubleQuadruple(-123456)
        assert result == (-246912, -493824), f"Test 14 failed: got {result}, expected {(-246912, -493824)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = DoubleQuadruple(1000000000)
        assert result == (2000000000, 4000000000), f"Test 15 failed: got {result}, expected {(2000000000, 4000000000)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = DoubleQuadruple(-1000000000)
        assert result == (-2000000000, -4000000000), f"Test 16 failed: got {result}, expected {(-2000000000, -4000000000)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = DoubleQuadruple(2147483647)
        assert result == (4294967294, 8589934588), f"Test 17 failed: got {result}, expected {(4294967294, 8589934588)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = DoubleQuadruple(-2147483648)
        assert result == (-4294967296, -8589934592), f"Test 18 failed: got {result}, expected {(-4294967296, -8589934592)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = DoubleQuadruple(2147483648)
        assert result == (4294967296, 8589934592), f"Test 19 failed: got {result}, expected {(4294967296, 8589934592)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = DoubleQuadruple(-2147483649)
        assert result == (-4294967298, -8589934596), f"Test 20 failed: got {result}, expected {(-4294967298, -8589934596)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = DoubleQuadruple(4294967295)
        assert result == (8589934590, 17179869180), f"Test 21 failed: got {result}, expected {(8589934590, 17179869180)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = DoubleQuadruple(-4294967296)
        assert result == (-8589934592, -17179869184), f"Test 22 failed: got {result}, expected {(-8589934592, -17179869184)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = DoubleQuadruple(9223372036854775807)
        assert result == (18446744073709551614, 36893488147419103228), f"Test 23 failed: got {result}, expected {(18446744073709551614, 36893488147419103228)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = DoubleQuadruple(-9223372036854775808)
        assert result == (-18446744073709551616, -36893488147419103232), f"Test 24 failed: got {result}, expected {(-18446744073709551616, -36893488147419103232)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = DoubleQuadruple(9223372036854775808)
        assert result == (18446744073709551616, 36893488147419103232), f"Test 25 failed: got {result}, expected {(18446744073709551616, 36893488147419103232)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = DoubleQuadruple(-9223372036854775809)
        assert result == (-18446744073709551618, -36893488147419103236), f"Test 26 failed: got {result}, expected {(-18446744073709551618, -36893488147419103236)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = DoubleQuadruple(4611686018427387903)
        assert result == (9223372036854775806, 18446744073709551612), f"Test 27 failed: got {result}, expected {(9223372036854775806, 18446744073709551612)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = DoubleQuadruple(-4611686018427387904)
        assert result == (-9223372036854775808, -18446744073709551616), f"Test 28 failed: got {result}, expected {(-9223372036854775808, -18446744073709551616)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = DoubleQuadruple(4611686018427387904)
        assert result == (9223372036854775808, 18446744073709551616), f"Test 29 failed: got {result}, expected {(9223372036854775808, 18446744073709551616)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = DoubleQuadruple(-4611686018427387905)
        assert result == (-9223372036854775810, -18446744073709551620), f"Test 30 failed: got {result}, expected {(-9223372036854775810, -18446744073709551620)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = DoubleQuadruple(999999999999999999)
        assert result == (1999999999999999998, 3999999999999999996), f"Test 31 failed: got {result}, expected {(1999999999999999998, 3999999999999999996)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = DoubleQuadruple(-999999999999999999)
        assert result == (-1999999999999999998, -3999999999999999996), f"Test 32 failed: got {result}, expected {(-1999999999999999998, -3999999999999999996)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = DoubleQuadruple(1000000000000000000000000)
        assert result == (2000000000000000000000000, 4000000000000000000000000), f"Test 33 failed: got {result}, expected {(2000000000000000000000000, 4000000000000000000000000)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = DoubleQuadruple(-1000000000000000000000000)
        assert result == (-2000000000000000000000000, -4000000000000000000000000), f"Test 34 failed: got {result}, expected {(-2000000000000000000000000, -4000000000000000000000000)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = DoubleQuadruple(3141592653589793238462643383279)
        assert result == (6283185307179586476925286766558, 12566370614359172953850573533116), f"Test 35 failed: got {result}, expected {(6283185307179586476925286766558, 12566370614359172953850573533116)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = DoubleQuadruple(-3141592653589793238462643383279)
        assert result == (-6283185307179586476925286766558, -12566370614359172953850573533116), f"Test 36 failed: got {result}, expected {(-6283185307179586476925286766558, -12566370614359172953850573533116)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = DoubleQuadruple(100000000000000000000000000000000000000000000000000)
        assert result == (200000000000000000000000000000000000000000000000000, 400000000000000000000000000000000000000000000000000), f"Test 37 failed: got {result}, expected {(200000000000000000000000000000000000000000000000000, 400000000000000000000000000000000000000000000000000)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = DoubleQuadruple(-100000000000000000000000000000000000000000000000000)
        assert result == (-200000000000000000000000000000000000000000000000000, -400000000000000000000000000000000000000000000000000), f"Test 38 failed: got {result}, expected {(-200000000000000000000000000000000000000000000000000, -400000000000000000000000000000000000000000000000000)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = DoubleQuadruple(42)
        assert result == (84, 168), f"Test 39 failed: got {result}, expected {(84, 168)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = DoubleQuadruple(-42)
        assert result == (-84, -168), f"Test 40 failed: got {result}, expected {(-84, -168)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = DoubleQuadruple(-65536)
        assert result == (-131072, -262144), f"Test 41 failed: got {result}, expected {(-131072, -262144)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = DoubleQuadruple(-3)
        assert result == (-6, -12), f"Test 42 failed: got {result}, expected {(-6, -12)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = DoubleQuadruple(-4294967295)
        assert result == (-8589934590, -17179869180), f"Test 43 failed: got {result}, expected {(-8589934590, -17179869180)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = DoubleQuadruple(8)
        assert result == (16, 32), f"Test 44 failed: got {result}, expected {(16, 32)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = DoubleQuadruple(-6)
        assert result == (-12, -24), f"Test 45 failed: got {result}, expected {(-12, -24)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = DoubleQuadruple(-4)
        assert result == (-8, -16), f"Test 46 failed: got {result}, expected {(-8, -16)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = DoubleQuadruple(-98)
        assert result == (-196, -392), f"Test 47 failed: got {result}, expected {(-196, -392)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = DoubleQuadruple(-4294967297)
        assert result == (-8589934594, -17179869188), f"Test 48 failed: got {result}, expected {(-8589934594, -17179869188)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = DoubleQuadruple(-43)
        assert result == (-86, -172), f"Test 49 failed: got {result}, expected {(-86, -172)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = DoubleQuadruple(3)
        assert result == (6, 12), f"Test 50 failed: got {result}, expected {(6, 12)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = DoubleQuadruple(99999999999999999999999999999999999999999999999998)
        assert result == (199999999999999999999999999999999999999999999999996, 399999999999999999999999999999999999999999999999992), f"Test 51 failed: got {result}, expected {(199999999999999999999999999999999999999999999999996, 399999999999999999999999999999999999999999999999992)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = DoubleQuadruple(17)
        assert result == (34, 68), f"Test 52 failed: got {result}, expected {(34, 68)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = DoubleQuadruple(20)
        assert result == (40, 80), f"Test 53 failed: got {result}, expected {(40, 80)}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = DoubleQuadruple(9223372036854775809)
        assert result == (18446744073709551618, 36893488147419103236), f"Test 54 failed: got {result}, expected {(18446744073709551618, 36893488147419103236)}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = DoubleQuadruple(4)
        assert result == (8, 16), f"Test 55 failed: got {result}, expected {(8, 16)}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = DoubleQuadruple(8589934591)
        assert result == (17179869182, 34359738364), f"Test 56 failed: got {result}, expected {(17179869182, 34359738364)}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = DoubleQuadruple(9)
        assert result == (18, 36), f"Test 57 failed: got {result}, expected {(18, 36)}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = DoubleQuadruple(-86)
        assert result == (-172, -344), f"Test 58 failed: got {result}, expected {(-172, -344)}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = DoubleQuadruple(4611686018427387902)
        assert result == (9223372036854775804, 18446744073709551608), f"Test 59 failed: got {result}, expected {(9223372036854775804, 18446744073709551608)}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = DoubleQuadruple(-12)
        assert result == (-24, -48), f"Test 60 failed: got {result}, expected {(-24, -48)}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = DoubleQuadruple(-9223372036854775807)
        assert result == (-18446744073709551614, -36893488147419103228), f"Test 61 failed: got {result}, expected {(-18446744073709551614, -36893488147419103228)}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = DoubleQuadruple(4294967298)
        assert result == (8589934596, 17179869192), f"Test 62 failed: got {result}, expected {(8589934596, 17179869192)}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = DoubleQuadruple(-2147483647)
        assert result == (-4294967294, -8589934588), f"Test 63 failed: got {result}, expected {(-4294967294, -8589934588)}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = DoubleQuadruple(18)
        assert result == (36, 72), f"Test 64 failed: got {result}, expected {(36, 72)}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = DoubleQuadruple(5)
        assert result == (10, 20), f"Test 65 failed: got {result}, expected {(10, 20)}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = DoubleQuadruple(-8)
        assert result == (-16, -32), f"Test 66 failed: got {result}, expected {(-16, -32)}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = DoubleQuadruple(9223372036854775810)
        assert result == (18446744073709551620, 36893488147419103240), f"Test 67 failed: got {result}, expected {(18446744073709551620, 36893488147419103240)}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = DoubleQuadruple(-2147483646)
        assert result == (-4294967292, -8589934584), f"Test 68 failed: got {result}, expected {(-4294967292, -8589934584)}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = DoubleQuadruple(199)
        assert result == (398, 796), f"Test 69 failed: got {result}, expected {(398, 796)}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = DoubleQuadruple(98)
        assert result == (196, 392), f"Test 70 failed: got {result}, expected {(196, 392)}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = DoubleQuadruple(-17179869184)
        assert result == (-34359738368, -68719476736), f"Test 71 failed: got {result}, expected {(-34359738368, -68719476736)}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = DoubleQuadruple(-198)
        assert result == (-396, -792), f"Test 72 failed: got {result}, expected {(-396, -792)}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = DoubleQuadruple(96)
        assert result == (192, 384), f"Test 73 failed: got {result}, expected {(192, 384)}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = DoubleQuadruple(-195)
        assert result == (-390, -780), f"Test 74 failed: got {result}, expected {(-390, -780)}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = DoubleQuadruple(-196)
        assert result == (-392, -784), f"Test 75 failed: got {result}, expected {(-392, -784)}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = DoubleQuadruple(198)
        assert result == (396, 792), f"Test 76 failed: got {result}, expected {(396, 792)}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = DoubleQuadruple(246913)
        assert result == (493826, 987652), f"Test 77 failed: got {result}, expected {(493826, 987652)}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = DoubleQuadruple(493828)
        assert result == (987656, 1975312), f"Test 78 failed: got {result}, expected {(987656, 1975312)}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = DoubleQuadruple(246912)
        assert result == (493824, 987648), f"Test 79 failed: got {result}, expected {(493824, 987648)}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = DoubleQuadruple(123457)
        assert result == (246914, 493828), f"Test 80 failed: got {result}, expected {(246914, 493828)}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = DoubleQuadruple(-4294967299)
        assert result == (-8589934598, -17179869196), f"Test 81 failed: got {result}, expected {(-8589934598, -17179869196)}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = DoubleQuadruple(-9)
        assert result == (-18, -36), f"Test 82 failed: got {result}, expected {(-18, -36)}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = DoubleQuadruple(-21)
        assert result == (-42, -84), f"Test 83 failed: got {result}, expected {(-42, -84)}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = DoubleQuadruple(-246908)
        assert result == (-493816, -987632), f"Test 84 failed: got {result}, expected {(-493816, -987632)}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = DoubleQuadruple(3141592653589793238462643383277)
        assert result == (6283185307179586476925286766554, 12566370614359172953850573533108), f"Test 85 failed: got {result}, expected {(6283185307179586476925286766554, 12566370614359172953850573533108)}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = DoubleQuadruple(-246911)
        assert result == (-493822, -987644), f"Test 86 failed: got {result}, expected {(-493822, -987644)}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = DoubleQuadruple(95)
        assert result == (190, 380), f"Test 87 failed: got {result}, expected {(190, 380)}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = DoubleQuadruple(2000000006)
        assert result == (4000000012, 8000000024), f"Test 88 failed: got {result}, expected {(4000000012, 8000000024)}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = DoubleQuadruple(1000000001)
        assert result == (2000000002, 4000000004), f"Test 89 failed: got {result}, expected {(2000000002, 4000000004)}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = DoubleQuadruple(-2000000001)
        assert result == (-4000000002, -8000000004), f"Test 90 failed: got {result}, expected {(-4000000002, -8000000004)}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = DoubleQuadruple(-123457)
        assert result == (-246914, -493828), f"Test 91 failed: got {result}, expected {(-246914, -493828)}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = DoubleQuadruple(-9223372036854775811)
        assert result == (-18446744073709551622, -36893488147419103244), f"Test 92 failed: got {result}, expected {(-18446744073709551622, -36893488147419103244)}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = DoubleQuadruple(87)
        assert result == (174, 348), f"Test 93 failed: got {result}, expected {(174, 348)}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = DoubleQuadruple(-1999999998)
        assert result == (-3999999996, -7999999992), f"Test 94 failed: got {result}, expected {(-3999999996, -7999999992)}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = DoubleQuadruple(-1000000000000000000000001)
        assert result == (-2000000000000000000000002, -4000000000000000000000004), f"Test 95 failed: got {result}, expected {(-2000000000000000000000002, -4000000000000000000000004)}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = DoubleQuadruple(-3141592653589793238462643383280)
        assert result == (-6283185307179586476925286766560, -12566370614359172953850573533120), f"Test 96 failed: got {result}, expected {(-6283185307179586476925286766560, -12566370614359172953850573533120)}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = DoubleQuadruple(4294967297)
        assert result == (8589934594, 17179869188), f"Test 97 failed: got {result}, expected {(8589934594, 17179869188)}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = DoubleQuadruple(2147483646)
        assert result == (4294967292, 8589934584), f"Test 98 failed: got {result}, expected {(4294967292, 8589934584)}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = DoubleQuadruple(-14)
        assert result == (-28, -56), f"Test 99 failed: got {result}, expected {(-28, -56)}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = DoubleQuadruple(2147483644)
        assert result == (4294967288, 8589934576), f"Test 100 failed: got {result}, expected {(4294967288, 8589934576)}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = DoubleQuadruple(-4294967294)
        assert result == (-8589934588, -17179869176), f"Test 101 failed: got {result}, expected {(-8589934588, -17179869176)}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = DoubleQuadruple(-193)
        assert result == (-386, -772), f"Test 102 failed: got {result}, expected {(-386, -772)}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = DoubleQuadruple(12)
        assert result == (24, 48), f"Test 103 failed: got {result}, expected {(24, 48)}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = DoubleQuadruple(2147483649)
        assert result == (4294967298, 8589934596), f"Test 104 failed: got {result}, expected {(4294967298, 8589934596)}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = DoubleQuadruple(-13)
        assert result == (-26, -52), f"Test 105 failed: got {result}, expected {(-26, -52)}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = DoubleQuadruple(4294967294)
        assert result == (8589934588, 17179869176), f"Test 106 failed: got {result}, expected {(8589934588, 17179869176)}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = DoubleQuadruple(4294967296)
        assert result == (8589934592, 17179869184), f"Test 107 failed: got {result}, expected {(8589934592, 17179869184)}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = DoubleQuadruple(11)
        assert result == (22, 44), f"Test 108 failed: got {result}, expected {(22, 44)}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = DoubleQuadruple(-4294967292)
        assert result == (-8589934584, -17179869168), f"Test 109 failed: got {result}, expected {(-8589934584, -17179869168)}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = DoubleQuadruple(3141592653589793238462643383278)
        assert result == (6283185307179586476925286766556, 12566370614359172953850573533112), f"Test 110 failed: got {result}, expected {(6283185307179586476925286766556, 12566370614359172953850573533112)}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = DoubleQuadruple(-2147483650)
        assert result == (-4294967300, -8589934600), f"Test 111 failed: got {result}, expected {(-4294967300, -8589934600)}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = DoubleQuadruple(-99999999999999999999999999999999999999999999999999)
        assert result == (-199999999999999999999999999999999999999999999999998, -399999999999999999999999999999999999999999999999996), f"Test 112 failed: got {result}, expected {(-199999999999999999999999999999999999999999999999998, -399999999999999999999999999999999999999999999999996)}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = DoubleQuadruple(-2147483651)
        assert result == (-4294967302, -8589934604), f"Test 113 failed: got {result}, expected {(-4294967302, -8589934604)}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = DoubleQuadruple(1000000002)
        assert result == (2000000004, 4000000008), f"Test 114 failed: got {result}, expected {(2000000004, 4000000008)}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = DoubleQuadruple(123455)
        assert result == (246910, 493820), f"Test 115 failed: got {result}, expected {(246910, 493820)}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = DoubleQuadruple(4294967293)
        assert result == (8589934586, 17179869172), f"Test 116 failed: got {result}, expected {(8589934586, 17179869172)}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = DoubleQuadruple(8589934590)
        assert result == (17179869180, 34359738360), f"Test 117 failed: got {result}, expected {(17179869180, 34359738360)}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = DoubleQuadruple(-8589934590)
        assert result == (-17179869180, -34359738360), f"Test 118 failed: got {result}, expected {(-17179869180, -34359738360)}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = DoubleQuadruple(-87)
        assert result == (-174, -348), f"Test 119 failed: got {result}, expected {(-174, -348)}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = DoubleQuadruple(-172)
        assert result == (-344, -688), f"Test 120 failed: got {result}, expected {(-344, -688)}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = DoubleQuadruple(-40)
        assert result == (-80, -160), f"Test 121 failed: got {result}, expected {(-80, -160)}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = DoubleQuadruple(-18)
        assert result == (-36, -72), f"Test 122 failed: got {result}, expected {(-36, -72)}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = DoubleQuadruple(-8589934593)
        assert result == (-17179869186, -34359738372), f"Test 123 failed: got {result}, expected {(-17179869186, -34359738372)}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = DoubleQuadruple(2000000002)
        assert result == (4000000004, 8000000008), f"Test 124 failed: got {result}, expected {(4000000004, 8000000008)}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = DoubleQuadruple(9223372036854775806)
        assert result == (18446744073709551612, 36893488147419103224), f"Test 125 failed: got {result}, expected {(18446744073709551612, 36893488147419103224)}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = DoubleQuadruple(-2147483645)
        assert result == (-4294967290, -8589934580), f"Test 126 failed: got {result}, expected {(-4294967290, -8589934580)}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = DoubleQuadruple(-18446744073709551617)
        assert result == (-36893488147419103234, -73786976294838206468), f"Test 127 failed: got {result}, expected {(-36893488147419103234, -73786976294838206468)}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = DoubleQuadruple(-246909)
        assert result == (-493818, -987636), f"Test 128 failed: got {result}, expected {(-493818, -987636)}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = DoubleQuadruple(-4611686018427387903)
        assert result == (-9223372036854775806, -18446744073709551612), f"Test 129 failed: got {result}, expected {(-9223372036854775806, -18446744073709551612)}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = DoubleQuadruple(-390)
        assert result == (-780, -1560), f"Test 130 failed: got {result}, expected {(-780, -1560)}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = DoubleQuadruple(-9223372036854775810)
        assert result == (-18446744073709551620, -36893488147419103240), f"Test 131 failed: got {result}, expected {(-18446744073709551620, -36893488147419103240)}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = DoubleQuadruple(-15)
        assert result == (-30, -60), f"Test 132 failed: got {result}, expected {(-30, -60)}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = DoubleQuadruple(9223372036854775805)
        assert result == (18446744073709551610, 36893488147419103220), f"Test 133 failed: got {result}, expected {(18446744073709551610, 36893488147419103220)}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = DoubleQuadruple(9223372036854775812)
        assert result == (18446744073709551624, 36893488147419103248), f"Test 134 failed: got {result}, expected {(18446744073709551624, 36893488147419103248)}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = DoubleQuadruple(-18446744073709551618)
        assert result == (-36893488147419103236, -73786976294838206472), f"Test 135 failed: got {result}, expected {(-36893488147419103236, -73786976294838206472)}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = DoubleQuadruple(-174)
        assert result == (-348, -696), f"Test 136 failed: got {result}, expected {(-348, -696)}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = DoubleQuadruple(-45)
        assert result == (-90, -180), f"Test 137 failed: got {result}, expected {(-90, -180)}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = DoubleQuadruple(194)
        assert result == (388, 776), f"Test 138 failed: got {result}, expected {(388, 776)}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = DoubleQuadruple(246910)
        assert result == (493820, 987640), f"Test 139 failed: got {result}, expected {(493820, 987640)}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = DoubleQuadruple(4611686018427387905)
        assert result == (9223372036854775810, 18446744073709551620), f"Test 140 failed: got {result}, expected {(9223372036854775810, 18446744073709551620)}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = DoubleQuadruple(-4611686018427387906)
        assert result == (-9223372036854775812, -18446744073709551624), f"Test 141 failed: got {result}, expected {(-9223372036854775812, -18446744073709551624)}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = DoubleQuadruple(13)
        assert result == (26, 52), f"Test 142 failed: got {result}, expected {(26, 52)}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = DoubleQuadruple(199999999999999999999999999999999999999999999999996)
        assert result == (399999999999999999999999999999999999999999999999992, 799999999999999999999999999999999999999999999999984), f"Test 143 failed: got {result}, expected {(399999999999999999999999999999999999999999999999992, 799999999999999999999999999999999999999999999999984)}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = DoubleQuadruple(-36)
        assert result == (-72, -144), f"Test 144 failed: got {result}, expected {(-72, -144)}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = DoubleQuadruple(-999999999999999999999998)
        assert result == (-1999999999999999999999996, -3999999999999999999999992), f"Test 145 failed: got {result}, expected {(-1999999999999999999999996, -3999999999999999999999992)}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = DoubleQuadruple(-8589934595)
        assert result == (-17179869190, -34359738380), f"Test 146 failed: got {result}, expected {(-17179869190, -34359738380)}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = DoubleQuadruple(-36893488147419103232)
        assert result == (-73786976294838206464, -147573952589676412928), f"Test 147 failed: got {result}, expected {(-73786976294838206464, -147573952589676412928)}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = DoubleQuadruple(-18446744073709551620)
        assert result == (-36893488147419103240, -73786976294838206480), f"Test 148 failed: got {result}, expected {(-36893488147419103240, -73786976294838206480)}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = DoubleQuadruple(8589934593)
        assert result == (17179869186, 34359738372), f"Test 149 failed: got {result}, expected {(17179869186, 34359738372)}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = DoubleQuadruple(999999999999999998)
        assert result == (1999999999999999996, 3999999999999999992), f"Test 150 failed: got {result}, expected {(1999999999999999996, 3999999999999999992)}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = DoubleQuadruple(2000000000000000002)
        assert result == (4000000000000000004, 8000000000000000008), f"Test 151 failed: got {result}, expected {(4000000000000000004, 8000000000000000008)}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = DoubleQuadruple(-11)
        assert result == (-22, -44), f"Test 152 failed: got {result}, expected {(-22, -44)}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = DoubleQuadruple(-1000000000000000002)
        assert result == (-2000000000000000004, -4000000000000000008), f"Test 153 failed: got {result}, expected {(-2000000000000000004, -4000000000000000008)}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = DoubleQuadruple(3999999999999999996)
        assert result == (7999999999999999992, 15999999999999999984), f"Test 154 failed: got {result}, expected {(7999999999999999992, 15999999999999999984)}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = DoubleQuadruple(2000000000000000003)
        assert result == (4000000000000000006, 8000000000000000012), f"Test 155 failed: got {result}, expected {(4000000000000000006, 8000000000000000012)}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = DoubleQuadruple(-2000000000000000002)
        assert result == (-4000000000000000004, -8000000000000000008), f"Test 156 failed: got {result}, expected {(-4000000000000000004, -8000000000000000008)}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = DoubleQuadruple(-18446744073709551619)
        assert result == (-36893488147419103238, -73786976294838206476), f"Test 157 failed: got {result}, expected {(-36893488147419103238, -73786976294838206476)}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = DoubleQuadruple(999999999999999999999998)
        assert result == (1999999999999999999999996, 3999999999999999999999992), f"Test 158 failed: got {result}, expected {(1999999999999999999999996, 3999999999999999999999992)}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = DoubleQuadruple(84)
        assert result == (168, 336), f"Test 159 failed: got {result}, expected {(168, 336)}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = DoubleQuadruple(-194)
        assert result == (-388, -776), f"Test 160 failed: got {result}, expected {(-388, -776)}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = DoubleQuadruple(999999999999999999999999)
        assert result == (1999999999999999999999998, 3999999999999999999999996), f"Test 161 failed: got {result}, expected {(1999999999999999999999998, 3999999999999999999999996)}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = DoubleQuadruple(-493822)
        assert result == (-987644, -1975288), f"Test 162 failed: got {result}, expected {(-987644, -1975288)}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = DoubleQuadruple(1000000000000000000000001)
        assert result == (2000000000000000000000002, 4000000000000000000000004), f"Test 163 failed: got {result}, expected {(2000000000000000000000002, 4000000000000000000000004)}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = DoubleQuadruple(-2000000000000000003)
        assert result == (-4000000000000000006, -8000000000000000012), f"Test 164 failed: got {result}, expected {(-4000000000000000006, -8000000000000000012)}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = DoubleQuadruple(-4294967300)
        assert result == (-8589934600, -17179869200), f"Test 165 failed: got {result}, expected {(-8589934600, -17179869200)}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = DoubleQuadruple(-4611686018427387901)
        assert result == (-9223372036854775802, -18446744073709551604), f"Test 166 failed: got {result}, expected {(-9223372036854775802, -18446744073709551604)}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = DoubleQuadruple(1999999999999999999999994)
        assert result == (3999999999999999999999988, 7999999999999999999999976), f"Test 167 failed: got {result}, expected {(3999999999999999999999988, 7999999999999999999999976)}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = DoubleQuadruple(4000000000000000000000000)
        assert result == (8000000000000000000000000, 16000000000000000000000000), f"Test 168 failed: got {result}, expected {(8000000000000000000000000, 16000000000000000000000000)}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = DoubleQuadruple(6283185307179586476925286766558)
        assert result == (12566370614359172953850573533116, 25132741228718345907701147066232), f"Test 169 failed: got {result}, expected {(12566370614359172953850573533116, 25132741228718345907701147066232)}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = DoubleQuadruple(-171)
        assert result == (-342, -684), f"Test 170 failed: got {result}, expected {(-342, -684)}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = DoubleQuadruple(6283185307179586476925286766556)
        assert result == (12566370614359172953850573533112, 25132741228718345907701147066224), f"Test 171 failed: got {result}, expected {(12566370614359172953850573533112, 25132741228718345907701147066224)}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = DoubleQuadruple(-9223372036854775806)
        assert result == (-18446744073709551612, -36893488147419103224), f"Test 172 failed: got {result}, expected {(-18446744073709551612, -36893488147419103224)}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = DoubleQuadruple(-100000000000000000000000000000000000000000000000003)
        assert result == (-200000000000000000000000000000000000000000000000006, -400000000000000000000000000000000000000000000000012), f"Test 173 failed: got {result}, expected {(-200000000000000000000000000000000000000000000000006, -400000000000000000000000000000000000000000000000012)}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = DoubleQuadruple(-3141592653589793238462643383277)
        assert result == (-6283185307179586476925286766554, -12566370614359172953850573533108), f"Test 174 failed: got {result}, expected {(-6283185307179586476925286766554, -12566370614359172953850573533108)}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = DoubleQuadruple(8589934594)
        assert result == (17179869188, 34359738376), f"Test 175 failed: got {result}, expected {(17179869188, 34359738376)}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = DoubleQuadruple(3141592653589793238462643383281)
        assert result == (6283185307179586476925286766562, 12566370614359172953850573533124), f"Test 176 failed: got {result}, expected {(6283185307179586476925286766562, 12566370614359172953850573533124)}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = DoubleQuadruple(6283185307179586476925286766557)
        assert result == (12566370614359172953850573533114, 25132741228718345907701147066228), f"Test 177 failed: got {result}, expected {(12566370614359172953850573533114, 25132741228718345907701147066228)}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = DoubleQuadruple(171)
        assert result == (342, 684), f"Test 178 failed: got {result}, expected {(342, 684)}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = DoubleQuadruple(493829)
        assert result == (987658, 1975316), f"Test 179 failed: got {result}, expected {(987658, 1975316)}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = DoubleQuadruple(99999999999999999999999999999999999999999999999999)
        assert result == (199999999999999999999999999999999999999999999999998, 399999999999999999999999999999999999999999999999996), f"Test 180 failed: got {result}, expected {(199999999999999999999999999999999999999999999999998, 399999999999999999999999999999999999999999999999996)}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = DoubleQuadruple(17179869180)
        assert result == (34359738360, 68719476720), f"Test 181 failed: got {result}, expected {(34359738360, 68719476720)}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = DoubleQuadruple(2000000004)
        assert result == (4000000008, 8000000016), f"Test 182 failed: got {result}, expected {(4000000008, 8000000016)}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = DoubleQuadruple(-3141592653589793238462643383276)
        assert result == (-6283185307179586476925286766552, -12566370614359172953850573533104), f"Test 183 failed: got {result}, expected {(-6283185307179586476925286766552, -12566370614359172953850573533104)}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = DoubleQuadruple(100000000000000000000000000000000000000000000000001)
        assert result == (200000000000000000000000000000000000000000000000002, 400000000000000000000000000000000000000000000000004), f"Test 184 failed: got {result}, expected {(200000000000000000000000000000000000000000000000002, 400000000000000000000000000000000000000000000000004)}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = DoubleQuadruple(199999999999999999999999999999999999999999999999999)
        assert result == (399999999999999999999999999999999999999999999999998, 799999999999999999999999999999999999999999999999996), f"Test 185 failed: got {result}, expected {(399999999999999999999999999999999999999999999999998, 799999999999999999999999999999999999999999999999996)}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = DoubleQuadruple(999999999999999997)
        assert result == (1999999999999999994, 3999999999999999988), f"Test 186 failed: got {result}, expected {(1999999999999999994, 3999999999999999988)}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = DoubleQuadruple(-399999999999999999999999999999999999999999999999998)
        assert result == (-799999999999999999999999999999999999999999999999996, -1599999999999999999999999999999999999999999999999992), f"Test 187 failed: got {result}, expected {(-799999999999999999999999999999999999999999999999996, -1599999999999999999999999999999999999999999999999992)}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = DoubleQuadruple(-100000000000000000000000000000000000000000000000002)
        assert result == (-200000000000000000000000000000000000000000000000004, -400000000000000000000000000000000000000000000000008), f"Test 188 failed: got {result}, expected {(-200000000000000000000000000000000000000000000000004, -400000000000000000000000000000000000000000000000008)}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = DoubleQuadruple(2000000000000000000000001)
        assert result == (4000000000000000000000002, 8000000000000000000000004), f"Test 189 failed: got {result}, expected {(4000000000000000000000002, 8000000000000000000000004)}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = DoubleQuadruple(-99999999999999999999999999999999999999999999999998)
        assert result == (-199999999999999999999999999999999999999999999999996, -399999999999999999999999999999999999999999999999992), f"Test 190 failed: got {result}, expected {(-199999999999999999999999999999999999999999999999996, -399999999999999999999999999999999999999999999999992)}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = DoubleQuadruple(3999999999999999999999986)
        assert result == (7999999999999999999999972, 15999999999999999999999944), f"Test 191 failed: got {result}, expected {(7999999999999999999999972, 15999999999999999999999944)}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = DoubleQuadruple(2147483645)
        assert result == (4294967290, 8589934580), f"Test 192 failed: got {result}, expected {(4294967290, 8589934580)}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = DoubleQuadruple(40)
        assert result == (80, 160), f"Test 193 failed: got {result}, expected {(80, 160)}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = DoubleQuadruple(-8589934594)
        assert result == (-17179869188, -34359738376), f"Test 194 failed: got {result}, expected {(-17179869188, -34359738376)}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = DoubleQuadruple(-41)
        assert result == (-82, -164), f"Test 195 failed: got {result}, expected {(-82, -164)}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = DoubleQuadruple(-84)
        assert result == (-168, -336), f"Test 196 failed: got {result}, expected {(-168, -336)}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = DoubleQuadruple(123453)
        assert result == (246906, 493812), f"Test 197 failed: got {result}, expected {(246906, 493812)}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = DoubleQuadruple(-493821)
        assert result == (-987642, -1975284), f"Test 198 failed: got {result}, expected {(-987642, -1975284)}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = DoubleQuadruple(65535)
        assert result == (131070, 262140), f"Test 199 failed: got {result}, expected {(131070, 262140)}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = DoubleQuadruple(-65537)
        assert result == (-131074, -262148), f"Test 200 failed: got {result}, expected {(-131074, -262148)}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = DoubleQuadruple(-999999999999999999999997)
        assert result == (-1999999999999999999999994, -3999999999999999999999988), f"Test 201 failed: got {result}, expected {(-1999999999999999999999994, -3999999999999999999999988)}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
