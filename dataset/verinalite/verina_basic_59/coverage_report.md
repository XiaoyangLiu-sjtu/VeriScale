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
        result = DoubleQuadruple(-7)
        assert result == (-14, -28), f"Test 8 failed: got {result}, expected {(-14, -28)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = DoubleQuadruple(99)
        assert result == (198, 396), f"Test 9 failed: got {result}, expected {(198, 396)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = DoubleQuadruple(123456)
        assert result == (246912, 493824), f"Test 10 failed: got {result}, expected {(246912, 493824)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = DoubleQuadruple(2147483647)
        assert result == (4294967294, 8589934588), f"Test 11 failed: got {result}, expected {(4294967294, 8589934588)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = DoubleQuadruple(-2147483649)
        assert result == (-4294967298, -8589934596), f"Test 12 failed: got {result}, expected {(-4294967298, -8589934596)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = DoubleQuadruple(-4294967296)
        assert result == (-8589934592, -17179869184), f"Test 13 failed: got {result}, expected {(-8589934592, -17179869184)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = DoubleQuadruple(9223372036854775807)
        assert result == (18446744073709551614, 36893488147419103228), f"Test 14 failed: got {result}, expected {(18446744073709551614, 36893488147419103228)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = DoubleQuadruple(9223372036854775808)
        assert result == (18446744073709551616, 36893488147419103232), f"Test 15 failed: got {result}, expected {(18446744073709551616, 36893488147419103232)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = DoubleQuadruple(-4611686018427387904)
        assert result == (-9223372036854775808, -18446744073709551616), f"Test 16 failed: got {result}, expected {(-9223372036854775808, -18446744073709551616)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = DoubleQuadruple(-999999999999999999)
        assert result == (-1999999999999999998, -3999999999999999996), f"Test 17 failed: got {result}, expected {(-1999999999999999998, -3999999999999999996)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = DoubleQuadruple(-1000000000000000000000000)
        assert result == (-2000000000000000000000000, -4000000000000000000000000), f"Test 18 failed: got {result}, expected {(-2000000000000000000000000, -4000000000000000000000000)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = DoubleQuadruple(100000000000000000000000000000000000000000000000000)
        assert result == (200000000000000000000000000000000000000000000000000, 400000000000000000000000000000000000000000000000000), f"Test 19 failed: got {result}, expected {(200000000000000000000000000000000000000000000000000, 400000000000000000000000000000000000000000000000000)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = DoubleQuadruple(42)
        assert result == (84, 168), f"Test 20 failed: got {result}, expected {(84, 168)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = DoubleQuadruple(-42)
        assert result == (-84, -168), f"Test 21 failed: got {result}, expected {(-84, -168)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = DoubleQuadruple(8)
        assert result == (16, 32), f"Test 22 failed: got {result}, expected {(16, 32)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = DoubleQuadruple(-6)
        assert result == (-12, -24), f"Test 23 failed: got {result}, expected {(-12, -24)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = DoubleQuadruple(-98)
        assert result == (-196, -392), f"Test 24 failed: got {result}, expected {(-196, -392)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = DoubleQuadruple(99999999999999999999999999999999999999999999999998)
        assert result == (199999999999999999999999999999999999999999999999996, 399999999999999999999999999999999999999999999999992), f"Test 25 failed: got {result}, expected {(199999999999999999999999999999999999999999999999996, 399999999999999999999999999999999999999999999999992)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = DoubleQuadruple(17)
        assert result == (34, 68), f"Test 26 failed: got {result}, expected {(34, 68)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = DoubleQuadruple(20)
        assert result == (40, 80), f"Test 27 failed: got {result}, expected {(40, 80)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = DoubleQuadruple(9223372036854775809)
        assert result == (18446744073709551618, 36893488147419103236), f"Test 28 failed: got {result}, expected {(18446744073709551618, 36893488147419103236)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = DoubleQuadruple(4)
        assert result == (8, 16), f"Test 29 failed: got {result}, expected {(8, 16)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = DoubleQuadruple(8589934591)
        assert result == (17179869182, 34359738364), f"Test 30 failed: got {result}, expected {(17179869182, 34359738364)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = DoubleQuadruple(-86)
        assert result == (-172, -344), f"Test 31 failed: got {result}, expected {(-172, -344)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = DoubleQuadruple(4611686018427387902)
        assert result == (9223372036854775804, 18446744073709551608), f"Test 32 failed: got {result}, expected {(9223372036854775804, 18446744073709551608)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = DoubleQuadruple(4294967298)
        assert result == (8589934596, 17179869192), f"Test 33 failed: got {result}, expected {(8589934596, 17179869192)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = DoubleQuadruple(-198)
        assert result == (-396, -792), f"Test 34 failed: got {result}, expected {(-396, -792)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = DoubleQuadruple(-21)
        assert result == (-42, -84), f"Test 35 failed: got {result}, expected {(-42, -84)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = DoubleQuadruple(-246911)
        assert result == (-493822, -987644), f"Test 36 failed: got {result}, expected {(-493822, -987644)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = DoubleQuadruple(2000000006)
        assert result == (4000000012, 8000000024), f"Test 37 failed: got {result}, expected {(4000000012, 8000000024)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = DoubleQuadruple(1000000001)
        assert result == (2000000002, 4000000004), f"Test 38 failed: got {result}, expected {(2000000002, 4000000004)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = DoubleQuadruple(-2000000001)
        assert result == (-4000000002, -8000000004), f"Test 39 failed: got {result}, expected {(-4000000002, -8000000004)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = DoubleQuadruple(-8589934593)
        assert result == (-17179869186, -34359738372), f"Test 40 failed: got {result}, expected {(-17179869186, -34359738372)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = DoubleQuadruple(2000000002)
        assert result == (4000000004, 8000000008), f"Test 41 failed: got {result}, expected {(4000000004, 8000000008)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = DoubleQuadruple(-174)
        assert result == (-348, -696), f"Test 42 failed: got {result}, expected {(-348, -696)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = DoubleQuadruple(-45)
        assert result == (-90, -180), f"Test 43 failed: got {result}, expected {(-90, -180)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = DoubleQuadruple(-4611686018427387906)
        assert result == (-9223372036854775812, -18446744073709551624), f"Test 44 failed: got {result}, expected {(-9223372036854775812, -18446744073709551624)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = DoubleQuadruple(999999999999999999999999)
        assert result == (1999999999999999999999998, 3999999999999999999999996), f"Test 45 failed: got {result}, expected {(1999999999999999999999998, 3999999999999999999999996)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = DoubleQuadruple(-493822)
        assert result == (-987644, -1975288), f"Test 46 failed: got {result}, expected {(-987644, -1975288)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = DoubleQuadruple(3141592653589793238462643383281)
        assert result == (6283185307179586476925286766562, 12566370614359172953850573533124), f"Test 47 failed: got {result}, expected {(6283185307179586476925286766562, 12566370614359172953850573533124)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = DoubleQuadruple(100000000000000000000000000000000000000000000000001)
        assert result == (200000000000000000000000000000000000000000000000002, 400000000000000000000000000000000000000000000000004), f"Test 48 failed: got {result}, expected {(200000000000000000000000000000000000000000000000002, 400000000000000000000000000000000000000000000000004)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = DoubleQuadruple(199999999999999999999999999999999999999999999999999)
        assert result == (399999999999999999999999999999999999999999999999998, 799999999999999999999999999999999999999999999999996), f"Test 49 failed: got {result}, expected {(399999999999999999999999999999999999999999999999998, 799999999999999999999999999999999999999999999999996)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = DoubleQuadruple(2000000000000000000000001)
        assert result == (4000000000000000000000002, 8000000000000000000000004), f"Test 50 failed: got {result}, expected {(4000000000000000000000002, 8000000000000000000000004)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = DoubleQuadruple(123453)
        assert result == (246906, 493812), f"Test 51 failed: got {result}, expected {(246906, 493812)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = DoubleQuadruple(-493821)
        assert result == (-987642, -1975284), f"Test 52 failed: got {result}, expected {(-987642, -1975284)}"
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
