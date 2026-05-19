# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def SwapSimultaneous(X, Y):
2: ✓     return (Y, X)
```

## Complete Test File

```python
def SwapSimultaneous(X, Y):
    return (Y, X)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = SwapSimultaneous(3, 4)
        assert result == (4, 3), f"Test 1 failed: got {result}, expected {(4, 3)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = SwapSimultaneous(-10, 20)
        assert result == (20, -10), f"Test 2 failed: got {result}, expected {(20, -10)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = SwapSimultaneous(0, 0)
        assert result == (0, 0), f"Test 3 failed: got {result}, expected {(0, 0)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = SwapSimultaneous(123, -456)
        assert result == (-456, 123), f"Test 4 failed: got {result}, expected {(-456, 123)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = SwapSimultaneous(-1, -2)
        assert result == (-2, -1), f"Test 5 failed: got {result}, expected {(-2, -1)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = SwapSimultaneous(2, 1)
        assert result == (1, 2), f"Test 6 failed: got {result}, expected {(1, 2)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = SwapSimultaneous(-5, -10)
        assert result == (-10, -5), f"Test 7 failed: got {result}, expected {(-10, -5)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = SwapSimultaneous(314159265358979323, -271828182845904523)
        assert result == (-271828182845904523, 314159265358979323), f"Test 8 failed: got {result}, expected {(-271828182845904523, 314159265358979323)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = SwapSimultaneous(-100, 100)
        assert result == (100, -100), f"Test 9 failed: got {result}, expected {(100, -100)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = SwapSimultaneous(3, -3)
        assert result == (-3, 3), f"Test 10 failed: got {result}, expected {(-3, 3)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = SwapSimultaneous(-3, 4)
        assert result == (4, -3), f"Test 11 failed: got {result}, expected {(4, -3)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = SwapSimultaneous(2, 4)
        assert result == (4, 2), f"Test 12 failed: got {result}, expected {(4, 2)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = SwapSimultaneous(-1, 5)
        assert result == (5, -1), f"Test 13 failed: got {result}, expected {(5, -1)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = SwapSimultaneous(-100, 20)
        assert result == (20, -100), f"Test 14 failed: got {result}, expected {(20, -100)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = SwapSimultaneous(-20, 111111111111111111)
        assert result == (111111111111111111, -20), f"Test 15 failed: got {result}, expected {(111111111111111111, -20)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = SwapSimultaneous(100, 5)
        assert result == (5, 100), f"Test 16 failed: got {result}, expected {(5, 100)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = SwapSimultaneous(0, -459)
        assert result == (-459, 0), f"Test 17 failed: got {result}, expected {(-459, 0)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = SwapSimultaneous(122, 6)
        assert result == (6, 122), f"Test 18 failed: got {result}, expected {(6, 122)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = SwapSimultaneous(-1, -1836)
        assert result == (-1836, -1), f"Test 19 failed: got {result}, expected {(-1836, -1)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = SwapSimultaneous(-271828182845904523, -1)
        assert result == (-1, -271828182845904523), f"Test 20 failed: got {result}, expected {(-1, -271828182845904523)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = SwapSimultaneous(-914, 0)
        assert result == (0, -914), f"Test 21 failed: got {result}, expected {(0, -914)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = SwapSimultaneous(1, 222222222222222222)
        assert result == (222222222222222222, 1), f"Test 22 failed: got {result}, expected {(222222222222222222, 1)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = SwapSimultaneous(2, -7)
        assert result == (-7, 2), f"Test 23 failed: got {result}, expected {(-7, 2)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = SwapSimultaneous(2, 18446744073709551614)
        assert result == (18446744073709551614, 2), f"Test 24 failed: got {result}, expected {(18446744073709551614, 2)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = SwapSimultaneous(65535, 1)
        assert result == (1, 65535), f"Test 25 failed: got {result}, expected {(1, 65535)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = SwapSimultaneous(-5000000000, 1)
        assert result == (1, -5000000000), f"Test 26 failed: got {result}, expected {(1, -5000000000)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = SwapSimultaneous(2, 0)
        assert result == (0, 2), f"Test 27 failed: got {result}, expected {(0, 2)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = SwapSimultaneous(36893488147419103228, 243)
        assert result == (243, 36893488147419103228), f"Test 28 failed: got {result}, expected {(243, 36893488147419103228)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = SwapSimultaneous(0, -9)
        assert result == (-9, 0), f"Test 29 failed: got {result}, expected {(-9, 0)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = SwapSimultaneous(-5, 20)
        assert result == (20, -5), f"Test 30 failed: got {result}, expected {(20, -5)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = SwapSimultaneous(-9, 5)
        assert result == (5, -9), f"Test 31 failed: got {result}, expected {(5, -9)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = SwapSimultaneous(2147483647, 0)
        assert result == (0, 2147483647), f"Test 32 failed: got {result}, expected {(0, 2147483647)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = SwapSimultaneous(-999, 10)
        assert result == (10, -999), f"Test 33 failed: got {result}, expected {(10, -999)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = SwapSimultaneous(-42, 1)
        assert result == (1, -42), f"Test 34 failed: got {result}, expected {(1, -42)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = SwapSimultaneous(-5000000000, 131068)
        assert result == (131068, -5000000000), f"Test 35 failed: got {result}, expected {(131068, -5000000000)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = SwapSimultaneous(543656365691809048, -43)
        assert result == (-43, 543656365691809048), f"Test 36 failed: got {result}, expected {(-43, 543656365691809048)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = SwapSimultaneous(-916, -2147483648)
        assert result == (-2147483648, -916), f"Test 37 failed: got {result}, expected {(-2147483648, -916)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = SwapSimultaneous(-2147483648, -2147483647)
        assert result == (-2147483647, -2147483648), f"Test 38 failed: got {result}, expected {(-2147483647, -2147483648)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = SwapSimultaneous(2147483648, 2147483647)
        assert result == (2147483647, 2147483648), f"Test 39 failed: got {result}, expected {(2147483647, 2147483648)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = SwapSimultaneous(42, 1000000000000)
        assert result == (1000000000000, 42), f"Test 40 failed: got {result}, expected {(1000000000000, 42)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = SwapSimultaneous(-1000000000000, 0)
        assert result == (0, -1000000000000), f"Test 41 failed: got {result}, expected {(0, -1000000000000)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = SwapSimultaneous(1000000000000000000, -999999999999999999)
        assert result == (-999999999999999999, 1000000000000000000), f"Test 42 failed: got {result}, expected {(-999999999999999999, 1000000000000000000)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = SwapSimultaneous(1999999999999999996, -1000000000000000000)
        assert result == (-1000000000000000000, 1999999999999999996), f"Test 43 failed: got {result}, expected {(-1000000000000000000, 1999999999999999996)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = SwapSimultaneous(-14, -9223372036854775809)
        assert result == (-9223372036854775809, -14), f"Test 44 failed: got {result}, expected {(-9223372036854775809, -14)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = SwapSimultaneous(1, -5)
        assert result == (-5, 1), f"Test 45 failed: got {result}, expected {(-5, 1)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = SwapSimultaneous(314159265358979322, 4000000000000)
        assert result == (4000000000000, 314159265358979322), f"Test 46 failed: got {result}, expected {(4000000000000, 314159265358979322)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = SwapSimultaneous(131072, 65538)
        assert result == (65538, 131072), f"Test 47 failed: got {result}, expected {(65538, 131072)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = SwapSimultaneous(-65535, -40)
        assert result == (-40, -65535), f"Test 48 failed: got {result}, expected {(-40, -65535)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = SwapSimultaneous(17, 18)
        assert result == (18, 17), f"Test 49 failed: got {result}, expected {(18, 17)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = SwapSimultaneous(5, -19)
        assert result == (-19, 5), f"Test 50 failed: got {result}, expected {(-19, 5)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = SwapSimultaneous(1000000000000000000, 37)
        assert result == (37, 1000000000000000000), f"Test 51 failed: got {result}, expected {(37, 1000000000000000000)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = SwapSimultaneous(-1993, 0)
        assert result == (0, -1993), f"Test 52 failed: got {result}, expected {(0, -1993)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = SwapSimultaneous(100, -9223372036854775806)
        assert result == (-9223372036854775806, 100), f"Test 53 failed: got {result}, expected {(-9223372036854775806, 100)}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = SwapSimultaneous(111111111111111112, -16)
        assert result == (-16, 111111111111111112), f"Test 54 failed: got {result}, expected {(-16, 111111111111111112)}"
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
