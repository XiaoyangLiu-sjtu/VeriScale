# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def Swap(X, Y):
2: ✓     return (Y, X)
```

## Complete Test File

```python
def Swap(X, Y):
    return (Y, X)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = Swap(1, 2)
        assert result == (2, 1), f"Test 1 failed: got {result}, expected {(2, 1)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = Swap(0, 0)
        assert result == (0, 0), f"Test 2 failed: got {result}, expected {(0, 0)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = Swap(-1, 5)
        assert result == (5, -1), f"Test 3 failed: got {result}, expected {(5, -1)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = Swap(100, -100)
        assert result == (-100, 100), f"Test 4 failed: got {result}, expected {(-100, 100)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = Swap(42, 42)
        assert result == (42, 42), f"Test 5 failed: got {result}, expected {(42, 42)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = Swap(2147483647, -2147483648)
        assert result == (-2147483648, 2147483647), f"Test 6 failed: got {result}, expected {(-2147483648, 2147483647)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = Swap(-2147483648, 2147483647)
        assert result == (2147483647, -2147483648), f"Test 7 failed: got {result}, expected {(2147483647, -2147483648)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = Swap(-1, 1)
        assert result == (1, -1), f"Test 8 failed: got {result}, expected {(1, -1)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = Swap(9223372036854775807, -5)
        assert result == (-5, 9223372036854775807), f"Test 9 failed: got {result}, expected {(-5, 9223372036854775807)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = Swap(-333333333333333333333333333333, 444444444444444444444444444444)
        assert result == (444444444444444444444444444444, -333333333333333333333333333333), f"Test 10 failed: got {result}, expected {(444444444444444444444444444444, -333333333333333333333333333333)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = Swap(0, -999999999999999999999999999999)
        assert result == (-999999999999999999999999999999, 0), f"Test 11 failed: got {result}, expected {(-999999999999999999999999999999, 0)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = Swap(1, 9223372036854775807)
        assert result == (9223372036854775807, 1), f"Test 12 failed: got {result}, expected {(9223372036854775807, 1)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = Swap(-1000000000000000000000000, 0)
        assert result == (0, -1000000000000000000000000), f"Test 13 failed: got {result}, expected {(0, -1000000000000000000000000)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = Swap(1, 19)
        assert result == (19, 1), f"Test 14 failed: got {result}, expected {(19, 1)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = Swap(3, -1)
        assert result == (-1, 3), f"Test 15 failed: got {result}, expected {(-1, 3)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = Swap(-2, 5)
        assert result == (5, -2), f"Test 16 failed: got {result}, expected {(5, -2)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = Swap(99, -2147483647)
        assert result == (-2147483647, 99), f"Test 17 failed: got {result}, expected {(-2147483647, 99)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = Swap(100, 1)
        assert result == (1, 100), f"Test 18 failed: got {result}, expected {(1, 100)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = Swap(102, 0)
        assert result == (0, 102), f"Test 19 failed: got {result}, expected {(0, 102)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = Swap(100, 0)
        assert result == (0, 100), f"Test 20 failed: got {result}, expected {(0, 100)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = Swap(1, -83)
        assert result == (-83, 1), f"Test 21 failed: got {result}, expected {(-83, 1)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = Swap(-9, 0)
        assert result == (0, -9), f"Test 22 failed: got {result}, expected {(0, -9)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = Swap(-2, -18446744073709551616)
        assert result == (-18446744073709551616, -2), f"Test 23 failed: got {result}, expected {(-18446744073709551616, -2)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = Swap(18446744073709551614, -9223372036854775804)
        assert result == (-9223372036854775804, 18446744073709551614), f"Test 24 failed: got {result}, expected {(-9223372036854775804, 18446744073709551614)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = Swap(123456788, 12)
        assert result == (12, 123456788), f"Test 25 failed: got {result}, expected {(12, 123456788)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = Swap(-9223372036854775807, 9223372036854775807)
        assert result == (9223372036854775807, -9223372036854775807), f"Test 26 failed: got {result}, expected {(9223372036854775807, -9223372036854775807)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = Swap(6, 8589934590)
        assert result == (8589934590, 6), f"Test 27 failed: got {result}, expected {(8589934590, 6)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = Swap(2147483649, 0)
        assert result == (0, 2147483649), f"Test 28 failed: got {result}, expected {(0, 2147483649)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = Swap(5, -999999999999999998)
        assert result == (-999999999999999998, 5), f"Test 29 failed: got {result}, expected {(-999999999999999998, 5)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = Swap(-1999999999999999998, -1000000000000000000)
        assert result == (-1000000000000000000, -1999999999999999998), f"Test 30 failed: got {result}, expected {(-1000000000000000000, -1999999999999999998)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = Swap(-16, 999999999999999999)
        assert result == (999999999999999999, -16), f"Test 31 failed: got {result}, expected {(999999999999999999, -16)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = Swap(1000000000000000000000000, -987654321)
        assert result == (-987654321, 1000000000000000000000000), f"Test 32 failed: got {result}, expected {(-987654321, 1000000000000000000000000)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = Swap(-246913578, -987654321)
        assert result == (-987654321, -246913578), f"Test 33 failed: got {result}, expected {(-987654321, -246913578)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = Swap(2147483646, 7)
        assert result == (7, 2147483646), f"Test 34 failed: got {result}, expected {(7, 2147483646)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = Swap(123456790, -987654320)
        assert result == (-987654320, 123456790), f"Test 35 failed: got {result}, expected {(-987654320, 123456790)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = Swap(123456789, -987654320)
        assert result == (-987654320, 123456789), f"Test 36 failed: got {result}, expected {(-987654320, 123456789)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = Swap(-201, -4)
        assert result == (-4, -201), f"Test 37 failed: got {result}, expected {(-4, -201)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = Swap(1000000000000000000, -7)
        assert result == (-7, 1000000000000000000), f"Test 38 failed: got {result}, expected {(-7, 1000000000000000000)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = Swap(12, -2)
        assert result == (-2, 12), f"Test 39 failed: got {result}, expected {(-2, 12)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = Swap(34, 0)
        assert result == (0, 34), f"Test 40 failed: got {result}, expected {(0, 34)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = Swap(-1000000000000000000000000, 1)
        assert result == (1, -1000000000000000000000000), f"Test 41 failed: got {result}, expected {(1, -1000000000000000000000000)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = Swap(-1975308646, 0)
        assert result == (0, -1975308646), f"Test 42 failed: got {result}, expected {(0, -1975308646)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = Swap(314159265358979323847, 0)
        assert result == (0, 314159265358979323847), f"Test 43 failed: got {result}, expected {(0, 314159265358979323847)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = Swap(-314159265358979323847, 271828182845904523536)
        assert result == (271828182845904523536, -314159265358979323847), f"Test 44 failed: got {result}, expected {(271828182845904523536, -314159265358979323847)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = Swap(271828182845904523535, -314159265358979323846)
        assert result == (-314159265358979323846, 271828182845904523535), f"Test 45 failed: got {result}, expected {(-314159265358979323846, 271828182845904523535)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = Swap(246913578024691357802469135778, 1000000000000000000000001)
        assert result == (1000000000000000000000001, 246913578024691357802469135778), f"Test 46 failed: got {result}, expected {(1000000000000000000000001, 246913578024691357802469135778)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = Swap(-123456789012345678901234567890, 123456789012345678901234567888)
        assert result == (123456789012345678901234567888, -123456789012345678901234567890), f"Test 47 failed: got {result}, expected {(123456789012345678901234567888, -123456789012345678901234567890)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = Swap(8, 123456789012345678901234567890)
        assert result == (123456789012345678901234567890, 8), f"Test 48 failed: got {result}, expected {(123456789012345678901234567890, 8)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = Swap(-4294967296, -333333333333333333333333333333)
        assert result == (-333333333333333333333333333333, -4294967296), f"Test 49 failed: got {result}, expected {(-333333333333333333333333333333, -4294967296)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = Swap(34, -1)
        assert result == (-1, 34), f"Test 50 failed: got {result}, expected {(-1, 34)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = Swap(-333333333333333333333333333333, -200)
        assert result == (-200, -333333333333333333333333333333), f"Test 51 failed: got {result}, expected {(-200, -333333333333333333333333333333)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = Swap(9, 0)
        assert result == (0, 9), f"Test 52 failed: got {result}, expected {(0, 9)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = Swap(-1256637061435917295384, -8)
        assert result == (-8, -1256637061435917295384), f"Test 53 failed: got {result}, expected {(-8, -1256637061435917295384)}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = Swap(8, -9)
        assert result == (-9, 8), f"Test 54 failed: got {result}, expected {(-9, 8)}"
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
