# Coverage Report

Total executable lines: 4
Covered lines: 4
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def Triple(x):
2: ✓     double = x * 2
3: ✓     result = double + x
4: ✓     return result
```

## Complete Test File

```python
def Triple(x):
    double = x * 2
    result = double + x
    return result

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = Triple(0)
        assert result == 0, f"Test 1 failed: got {result}, expected {0}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = Triple(1)
        assert result == 3, f"Test 2 failed: got {result}, expected {3}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = Triple(-1)
        assert result == -3, f"Test 3 failed: got {result}, expected {-3}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = Triple(5)
        assert result == 15, f"Test 4 failed: got {result}, expected {15}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = Triple(-10)
        assert result == -30, f"Test 5 failed: got {result}, expected {-30}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = Triple(2)
        assert result == 6, f"Test 6 failed: got {result}, expected {6}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = Triple(-2)
        assert result == -6, f"Test 7 failed: got {result}, expected {-6}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = Triple(3)
        assert result == 9, f"Test 8 failed: got {result}, expected {9}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = Triple(-3)
        assert result == -9, f"Test 9 failed: got {result}, expected {-9}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = Triple(-5)
        assert result == -15, f"Test 10 failed: got {result}, expected {-15}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = Triple(10)
        assert result == 30, f"Test 11 failed: got {result}, expected {30}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = Triple(42)
        assert result == 126, f"Test 12 failed: got {result}, expected {126}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = Triple(-42)
        assert result == -126, f"Test 13 failed: got {result}, expected {-126}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = Triple(99)
        assert result == 297, f"Test 14 failed: got {result}, expected {297}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = Triple(-99)
        assert result == -297, f"Test 15 failed: got {result}, expected {-297}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = Triple(127)
        assert result == 381, f"Test 16 failed: got {result}, expected {381}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = Triple(-128)
        assert result == -384, f"Test 17 failed: got {result}, expected {-384}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = Triple(255)
        assert result == 765, f"Test 18 failed: got {result}, expected {765}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = Triple(-256)
        assert result == -768, f"Test 19 failed: got {result}, expected {-768}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = Triple(1024)
        assert result == 3072, f"Test 20 failed: got {result}, expected {3072}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = Triple(-1024)
        assert result == -3072, f"Test 21 failed: got {result}, expected {-3072}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = Triple(2147483647)
        assert result == 6442450941, f"Test 22 failed: got {result}, expected {6442450941}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = Triple(-2147483648)
        assert result == -6442450944, f"Test 23 failed: got {result}, expected {-6442450944}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = Triple(2147483648)
        assert result == 6442450944, f"Test 24 failed: got {result}, expected {6442450944}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = Triple(-2147483649)
        assert result == -6442450947, f"Test 25 failed: got {result}, expected {-6442450947}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = Triple(9223372036854775807)
        assert result == 27670116110564327421, f"Test 26 failed: got {result}, expected {27670116110564327421}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = Triple(-9223372036854775808)
        assert result == -27670116110564327424, f"Test 27 failed: got {result}, expected {-27670116110564327424}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = Triple(9223372036854775808)
        assert result == 27670116110564327424, f"Test 28 failed: got {result}, expected {27670116110564327424}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = Triple(-9223372036854775809)
        assert result == -27670116110564327427, f"Test 29 failed: got {result}, expected {-27670116110564327427}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = Triple(1000000000000)
        assert result == 3000000000000, f"Test 30 failed: got {result}, expected {3000000000000}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = Triple(-1000000000000)
        assert result == -3000000000000, f"Test 31 failed: got {result}, expected {-3000000000000}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = Triple(999999999999999999)
        assert result == 2999999999999999997, f"Test 32 failed: got {result}, expected {2999999999999999997}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = Triple(-999999999999999999)
        assert result == -2999999999999999997, f"Test 33 failed: got {result}, expected {-2999999999999999997}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = Triple(123456789)
        assert result == 370370367, f"Test 34 failed: got {result}, expected {370370367}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = Triple(-123456789)
        assert result == -370370367, f"Test 35 failed: got {result}, expected {-370370367}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = Triple(7)
        assert result == 21, f"Test 36 failed: got {result}, expected {21}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = Triple(-7)
        assert result == -21, f"Test 37 failed: got {result}, expected {-21}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = Triple(314159265)
        assert result == 942477795, f"Test 38 failed: got {result}, expected {942477795}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = Triple(-271828182)
        assert result == -815484546, f"Test 39 failed: got {result}, expected {-815484546}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = Triple(-100000000000000000000)
        assert result == -300000000000000000000, f"Test 40 failed: got {result}, expected {-300000000000000000000}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = Triple(-1023)
        assert result == -3069, f"Test 41 failed: got {result}, expected {-3069}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = Triple(8)
        assert result == 24, f"Test 42 failed: got {result}, expected {24}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = Triple(128)
        assert result == 384, f"Test 43 failed: got {result}, expected {384}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = Triple(-4)
        assert result == -12, f"Test 44 failed: got {result}, expected {-12}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = Triple(129)
        assert result == 387, f"Test 45 failed: got {result}, expected {387}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = Triple(-1025)
        assert result == -3075, f"Test 46 failed: got {result}, expected {-3075}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = Triple(-1026)
        assert result == -3078, f"Test 47 failed: got {result}, expected {-3078}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = Triple(4)
        assert result == 12, f"Test 48 failed: got {result}, expected {12}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = Triple(18446744073709551615)
        assert result == 55340232221128654845, f"Test 49 failed: got {result}, expected {55340232221128654845}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = Triple(-11)
        assert result == -33, f"Test 50 failed: got {result}, expected {-33}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = Triple(-8)
        assert result == -24, f"Test 51 failed: got {result}, expected {-24}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = Triple(-246913577)
        assert result == -740740731, f"Test 52 failed: got {result}, expected {-740740731}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = Triple(-4294967300)
        assert result == -12884901900, f"Test 53 failed: got {result}, expected {-12884901900}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = Triple(9223372036854775806)
        assert result == 27670116110564327418, f"Test 54 failed: got {result}, expected {27670116110564327418}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = Triple(6)
        assert result == 18, f"Test 55 failed: got {result}, expected {18}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = Triple(4294967301)
        assert result == 12884901903, f"Test 56 failed: got {result}, expected {12884901903}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = Triple(123456790)
        assert result == 370370370, f"Test 57 failed: got {result}, expected {370370370}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = Triple(-6)
        assert result == -18, f"Test 58 failed: got {result}, expected {-18}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = Triple(246913579)
        assert result == 740740737, f"Test 59 failed: got {result}, expected {740740737}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = Triple(-13)
        assert result == -39, f"Test 60 failed: got {result}, expected {-39}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = Triple(-512)
        assert result == -1536, f"Test 61 failed: got {result}, expected {-1536}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = Triple(43)
        assert result == 129, f"Test 62 failed: got {result}, expected {129}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = Triple(-12)
        assert result == -36, f"Test 63 failed: got {result}, expected {-36}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = Triple(-18446744073709551614)
        assert result == -55340232221128654842, f"Test 64 failed: got {result}, expected {-55340232221128654842}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = Triple(4294967302)
        assert result == 12884901906, f"Test 65 failed: got {result}, expected {12884901906}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = Triple(18446744073709551616)
        assert result == 55340232221128654848, f"Test 66 failed: got {result}, expected {55340232221128654848}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = Triple(-9)
        assert result == -27, f"Test 67 failed: got {result}, expected {-27}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = Triple(21)
        assert result == 63, f"Test 68 failed: got {result}, expected {63}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = Triple(-2147483650)
        assert result == -6442450950, f"Test 69 failed: got {result}, expected {-6442450950}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = Triple(-4096)
        assert result == -12288, f"Test 70 failed: got {result}, expected {-12288}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = Triple(9)
        assert result == 27, f"Test 71 failed: got {result}, expected {27}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = Triple(20)
        assert result == 60, f"Test 72 failed: got {result}, expected {60}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = Triple(-45)
        assert result == -135, f"Test 73 failed: got {result}, expected {-135}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = Triple(87)
        assert result == 261, f"Test 74 failed: got {result}, expected {261}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = Triple(86)
        assert result == 258, f"Test 75 failed: got {result}, expected {258}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = Triple(4294967294)
        assert result == 12884901882, f"Test 76 failed: got {result}, expected {12884901882}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = Triple(-18446744073709551616)
        assert result == -55340232221128654848, f"Test 77 failed: got {result}, expected {-55340232221128654848}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = Triple(-83)
        assert result == -249, f"Test 78 failed: got {result}, expected {-249}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = Triple(-164)
        assert result == -492, f"Test 79 failed: got {result}, expected {-492}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = Triple(-84)
        assert result == -252, f"Test 80 failed: got {result}, expected {-252}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = Triple(-41)
        assert result == -123, f"Test 81 failed: got {result}, expected {-123}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = Triple(-19)
        assert result == -57, f"Test 82 failed: got {result}, expected {-57}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = Triple(202)
        assert result == 606, f"Test 83 failed: got {result}, expected {606}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = Triple(-166)
        assert result == -498, f"Test 84 failed: got {result}, expected {-498}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = Triple(-20)
        assert result == -60, f"Test 85 failed: got {result}, expected {-60}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = Triple(199)
        assert result == 597, f"Test 86 failed: got {result}, expected {597}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = Triple(201)
        assert result == 603, f"Test 87 failed: got {result}, expected {603}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = Triple(-192)
        assert result == -576, f"Test 88 failed: got {result}, expected {-576}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = Triple(-98)
        assert result == -294, f"Test 89 failed: got {result}, expected {-294}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = Triple(197)
        assert result == 591, f"Test 90 failed: got {result}, expected {591}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = Triple(-246913578)
        assert result == -740740734, f"Test 91 failed: got {result}, expected {-740740734}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = Triple(-2147483651)
        assert result == -6442450953, f"Test 92 failed: got {result}, expected {-6442450953}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = Triple(15)
        assert result == 45, f"Test 93 failed: got {result}, expected {45}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = Triple(256)
        assert result == 768, f"Test 94 failed: got {result}, expected {768}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = Triple(-513)
        assert result == -1539, f"Test 95 failed: got {result}, expected {-1539}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = Triple(-129)
        assert result == -387, f"Test 96 failed: got {result}, expected {-387}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = Triple(-127)
        assert result == -381, f"Test 97 failed: got {result}, expected {-381}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = Triple(-253)
        assert result == -759, f"Test 98 failed: got {result}, expected {-759}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = Triple(16)
        assert result == 48, f"Test 99 failed: got {result}, expected {48}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = Triple(18)
        assert result == 54, f"Test 100 failed: got {result}, expected {54}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = Triple(-36893488147419103234)
        assert result == -110680464442257309702, f"Test 101 failed: got {result}, expected {-110680464442257309702}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = Triple(-131)
        assert result == -393, f"Test 102 failed: got {result}, expected {-393}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = Triple(-193)
        assert result == -579, f"Test 103 failed: got {result}, expected {-579}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = Triple(-254)
        assert result == -762, f"Test 104 failed: got {result}, expected {-762}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = Triple(510)
        assert result == 1530, f"Test 105 failed: got {result}, expected {1530}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = Triple(257)
        assert result == 771, f"Test 106 failed: got {result}, expected {771}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = Triple(-8589934588)
        assert result == -25769803764, f"Test 107 failed: got {result}, expected {-25769803764}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = Triple(-514)
        assert result == -1542, f"Test 108 failed: got {result}, expected {-1542}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = Triple(-257)
        assert result == -771, f"Test 109 failed: got {result}, expected {-771}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = Triple(11)
        assert result == 33, f"Test 110 failed: got {result}, expected {33}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = Triple(2052)
        assert result == 6156, f"Test 111 failed: got {result}, expected {6156}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = Triple(1023)
        assert result == 3069, f"Test 112 failed: got {result}, expected {3069}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = Triple(-82)
        assert result == -246, f"Test 113 failed: got {result}, expected {-246}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = Triple(2049)
        assert result == 6147, f"Test 114 failed: got {result}, expected {6147}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = Triple(1022)
        assert result == 3066, f"Test 115 failed: got {result}, expected {3066}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = Triple(1020)
        assert result == 3060, f"Test 116 failed: got {result}, expected {3060}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = Triple(-17179869176)
        assert result == -51539607528, f"Test 117 failed: got {result}, expected {-51539607528}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = Triple(85)
        assert result == 255, f"Test 118 failed: got {result}, expected {255}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = Triple(200)
        assert result == 600, f"Test 119 failed: got {result}, expected {600}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = Triple(-2048)
        assert result == -6144, f"Test 120 failed: got {result}, expected {-6144}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = Triple(-2046)
        assert result == -6138, f"Test 121 failed: got {result}, expected {-6138}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = Triple(-252)
        assert result == -756, f"Test 122 failed: got {result}, expected {-756}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = Triple(-246913576)
        assert result == -740740728, f"Test 123 failed: got {result}, expected {-740740728}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = Triple(8589934586)
        assert result == 25769803758, f"Test 124 failed: got {result}, expected {25769803758}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = Triple(4294967293)
        assert result == 12884901879, f"Test 125 failed: got {result}, expected {12884901879}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = Triple(2147483646)
        assert result == 6442450938, f"Test 126 failed: got {result}, expected {6442450938}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = Triple(258)
        assert result == 774, f"Test 127 failed: got {result}, expected {774}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = Triple(-2147483647)
        assert result == -6442450941, f"Test 128 failed: got {result}, expected {-6442450941}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = Triple(-4294967299)
        assert result == -12884901897, f"Test 129 failed: got {result}, expected {-12884901897}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = Triple(1021)
        assert result == 3063, f"Test 130 failed: got {result}, expected {3063}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = Triple(203)
        assert result == 609, f"Test 131 failed: got {result}, expected {609}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = Triple(4294967296)
        assert result == 12884901888, f"Test 132 failed: got {result}, expected {12884901888}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = Triple(-4294967296)
        assert result == -12884901888, f"Test 133 failed: got {result}, expected {-12884901888}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = Triple(246913578)
        assert result == 740740734, f"Test 134 failed: got {result}, expected {740740734}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = Triple(2147483649)
        assert result == 6442450947, f"Test 135 failed: got {result}, expected {6442450947}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = Triple(-2147483652)
        assert result == -6442450956, f"Test 136 failed: got {result}, expected {-6442450956}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = Triple(-4294967297)
        assert result == -12884901891, f"Test 137 failed: got {result}, expected {-12884901891}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = Triple(-259)
        assert result == -777, f"Test 138 failed: got {result}, expected {-777}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = Triple(45)
        assert result == 135, f"Test 139 failed: got {result}, expected {135}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = Triple(4294967297)
        assert result == 12884901891, f"Test 140 failed: got {result}, expected {12884901891}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = Triple(-9223372036854775807)
        assert result == -27670116110564327421, f"Test 141 failed: got {result}, expected {-27670116110564327421}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = Triple(17179869176)
        assert result == 51539607528, f"Test 142 failed: got {result}, expected {51539607528}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = Triple(-9223372036854775806)
        assert result == -27670116110564327418, f"Test 143 failed: got {result}, expected {-27670116110564327418}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = Triple(163)
        assert result == 489, f"Test 144 failed: got {result}, expected {489}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = Triple(-22)
        assert result == -66, f"Test 145 failed: got {result}, expected {-66}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = Triple(9223372036854775809)
        assert result == 27670116110564327427, f"Test 146 failed: got {result}, expected {27670116110564327427}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = Triple(4294967299)
        assert result == 12884901897, f"Test 147 failed: got {result}, expected {12884901897}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = Triple(174)
        assert result == 522, f"Test 148 failed: got {result}, expected {522}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = Triple(-8589934594)
        assert result == -25769803782, f"Test 149 failed: got {result}, expected {-25769803782}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = Triple(-511)
        assert result == -1533, f"Test 150 failed: got {result}, expected {-1533}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = Triple(4294967300)
        assert result == 12884901900, f"Test 151 failed: got {result}, expected {12884901900}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = Triple(-133)
        assert result == -399, f"Test 152 failed: got {result}, expected {-399}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = Triple(-515)
        assert result == -1545, f"Test 153 failed: got {result}, expected {-1545}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = Triple(-2000000000002)
        assert result == -6000000000006, f"Test 154 failed: got {result}, expected {-6000000000006}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = Triple(8000000000008)
        assert result == 24000000000024, f"Test 155 failed: got {result}, expected {24000000000024}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = Triple(4000000000000)
        assert result == 12000000000000, f"Test 156 failed: got {result}, expected {12000000000000}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = Triple(192)
        assert result == 576, f"Test 157 failed: got {result}, expected {576}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = Triple(-1000000000001)
        assert result == -3000000000003, f"Test 158 failed: got {result}, expected {-3000000000003}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = Triple(-1999999999996)
        assert result == -5999999999988, f"Test 159 failed: got {result}, expected {-5999999999988}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = Triple(999999999997)
        assert result == 2999999999991, f"Test 160 failed: got {result}, expected {2999999999991}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = Triple(-4000000000000)
        assert result == -12000000000000, f"Test 161 failed: got {result}, expected {-12000000000000}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = Triple(509)
        assert result == 1527, f"Test 162 failed: got {result}, expected {1527}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = Triple(-2050)
        assert result == -6150, f"Test 163 failed: got {result}, expected {-6150}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = Triple(193)
        assert result == 579, f"Test 164 failed: got {result}, expected {579}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = Triple(-2000000000004)
        assert result == -6000000000012, f"Test 165 failed: got {result}, expected {-6000000000012}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = Triple(-203)
        assert result == -609, f"Test 166 failed: got {result}, expected {-609}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = Triple(17179869175)
        assert result == 51539607525, f"Test 167 failed: got {result}, expected {51539607525}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = Triple(-4294967302)
        assert result == -12884901906, f"Test 168 failed: got {result}, expected {-12884901906}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = Triple(1000000000000000001)
        assert result == 3000000000000000003, f"Test 169 failed: got {result}, expected {3000000000000000003}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = Triple(-198)
        assert result == -594, f"Test 170 failed: got {result}, expected {-594}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = Triple(-1022)
        assert result == -3066, f"Test 171 failed: got {result}, expected {-3066}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = Triple(-246913575)
        assert result == -740740725, f"Test 172 failed: got {result}, expected {-740740725}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = Triple(-2000000000001)
        assert result == -6000000000003, f"Test 173 failed: got {result}, expected {-6000000000003}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = Triple(-258)
        assert result == -774, f"Test 174 failed: got {result}, expected {-774}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = Triple(123456788)
        assert result == 370370364, f"Test 175 failed: got {result}, expected {370370364}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = Triple(-18446744073709551615)
        assert result == -55340232221128654845, f"Test 176 failed: got {result}, expected {-55340232221128654845}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = Triple(-123456788)
        assert result == -370370364, f"Test 177 failed: got {result}, expected {-370370364}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = Triple(-271828181)
        assert result == -815484543, f"Test 178 failed: got {result}, expected {-815484543}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = Triple(-246913580)
        assert result == -740740740, f"Test 179 failed: got {result}, expected {-740740740}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = Triple(-18446744073709551617)
        assert result == -55340232221128654851, f"Test 180 failed: got {result}, expected {-55340232221128654851}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = Triple(-25)
        assert result == -75, f"Test 181 failed: got {result}, expected {-75}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = Triple(-123456787)
        assert result == -370370361, f"Test 182 failed: got {result}, expected {-370370361}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = Triple(2147483650)
        assert result == 6442450950, f"Test 183 failed: got {result}, expected {6442450950}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = Triple(-4294967294)
        assert result == -12884901882, f"Test 184 failed: got {result}, expected {-12884901882}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = Triple(-15)
        assert result == -45, f"Test 185 failed: got {result}, expected {-45}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = Triple(49)
        assert result == 147, f"Test 186 failed: got {result}, expected {147}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = Triple(-44)
        assert result == -132, f"Test 187 failed: got {result}, expected {-132}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = Triple(198)
        assert result == 594, f"Test 188 failed: got {result}, expected {594}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = Triple(-251)
        assert result == -753, f"Test 189 failed: got {result}, expected {-753}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = Triple(1256637062)
        assert result == 3769911186, f"Test 190 failed: got {result}, expected {3769911186}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = Triple(314159263)
        assert result == 942477789, f"Test 191 failed: got {result}, expected {942477789}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = Triple(-543656365)
        assert result == -1630969095, f"Test 192 failed: got {result}, expected {-1630969095}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = Triple(314159267)
        assert result == 942477801, f"Test 193 failed: got {result}, expected {942477801}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = Triple(-493827147)
        assert result == -1481481441, f"Test 194 failed: got {result}, expected {-1481481441}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = Triple(2042)
        assert result == 6126, f"Test 195 failed: got {result}, expected {6126}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = Triple(271828182)
        assert result == 815484546, f"Test 196 failed: got {result}, expected {815484546}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = Triple(-46)
        assert result == -138, f"Test 197 failed: got {result}, expected {-138}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = Triple(-271828184)
        assert result == -815484552, f"Test 198 failed: got {result}, expected {-815484552}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = Triple(-200000000000000000000)
        assert result == -600000000000000000000, f"Test 199 failed: got {result}, expected {-600000000000000000000}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = Triple(-100000000000000000001)
        assert result == -300000000000000000003, f"Test 200 failed: got {result}, expected {-300000000000000000003}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = Triple(-999999999999999998)
        assert result == -2999999999999999994, f"Test 201 failed: got {result}, expected {-2999999999999999994}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = Triple(99999999999999999999)
        assert result == 299999999999999999997, f"Test 202 failed: got {result}, expected {299999999999999999997}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = Triple(-21)
        assert result == -63, f"Test 203 failed: got {result}, expected {-63}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
