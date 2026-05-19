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
        result = Triple(-3)
        assert result == -9, f"Test 6 failed: got {result}, expected {-9}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = Triple(10)
        assert result == 30, f"Test 7 failed: got {result}, expected {30}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = Triple(-99)
        assert result == -297, f"Test 8 failed: got {result}, expected {-297}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = Triple(-128)
        assert result == -384, f"Test 9 failed: got {result}, expected {-384}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = Triple(2147483647)
        assert result == 6442450941, f"Test 10 failed: got {result}, expected {6442450941}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = Triple(-2147483648)
        assert result == -6442450944, f"Test 11 failed: got {result}, expected {-6442450944}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = Triple(2147483648)
        assert result == 6442450944, f"Test 12 failed: got {result}, expected {6442450944}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = Triple(-2147483649)
        assert result == -6442450947, f"Test 13 failed: got {result}, expected {-6442450947}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = Triple(-9223372036854775808)
        assert result == -27670116110564327424, f"Test 14 failed: got {result}, expected {-27670116110564327424}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = Triple(9223372036854775808)
        assert result == 27670116110564327424, f"Test 15 failed: got {result}, expected {27670116110564327424}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = Triple(-9223372036854775809)
        assert result == -27670116110564327427, f"Test 16 failed: got {result}, expected {-27670116110564327427}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = Triple(-999999999999999999)
        assert result == -2999999999999999997, f"Test 17 failed: got {result}, expected {-2999999999999999997}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = Triple(-123456789)
        assert result == -370370367, f"Test 18 failed: got {result}, expected {-370370367}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = Triple(7)
        assert result == 21, f"Test 19 failed: got {result}, expected {21}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = Triple(-1023)
        assert result == -3069, f"Test 20 failed: got {result}, expected {-3069}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = Triple(-1026)
        assert result == -3078, f"Test 21 failed: got {result}, expected {-3078}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = Triple(-246913577)
        assert result == -740740731, f"Test 22 failed: got {result}, expected {-740740731}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = Triple(4294967301)
        assert result == 12884901903, f"Test 23 failed: got {result}, expected {12884901903}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = Triple(-12)
        assert result == -36, f"Test 24 failed: got {result}, expected {-36}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = Triple(20)
        assert result == 60, f"Test 25 failed: got {result}, expected {60}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = Triple(-164)
        assert result == -492, f"Test 26 failed: got {result}, expected {-492}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = Triple(202)
        assert result == 606, f"Test 27 failed: got {result}, expected {606}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = Triple(199)
        assert result == 597, f"Test 28 failed: got {result}, expected {597}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = Triple(197)
        assert result == 591, f"Test 29 failed: got {result}, expected {591}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = Triple(-246913578)
        assert result == -740740734, f"Test 30 failed: got {result}, expected {-740740734}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = Triple(-127)
        assert result == -381, f"Test 31 failed: got {result}, expected {-381}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = Triple(510)
        assert result == 1530, f"Test 32 failed: got {result}, expected {1530}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = Triple(-82)
        assert result == -246, f"Test 33 failed: got {result}, expected {-246}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = Triple(1020)
        assert result == 3060, f"Test 34 failed: got {result}, expected {3060}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = Triple(1021)
        assert result == 3063, f"Test 35 failed: got {result}, expected {3063}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = Triple(203)
        assert result == 609, f"Test 36 failed: got {result}, expected {609}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = Triple(-4294967296)
        assert result == -12884901888, f"Test 37 failed: got {result}, expected {-12884901888}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = Triple(45)
        assert result == 135, f"Test 38 failed: got {result}, expected {135}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = Triple(17179869176)
        assert result == 51539607528, f"Test 39 failed: got {result}, expected {51539607528}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = Triple(-22)
        assert result == -66, f"Test 40 failed: got {result}, expected {-66}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = Triple(9223372036854775809)
        assert result == 27670116110564327427, f"Test 41 failed: got {result}, expected {27670116110564327427}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = Triple(4294967299)
        assert result == 12884901897, f"Test 42 failed: got {result}, expected {12884901897}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = Triple(-515)
        assert result == -1545, f"Test 43 failed: got {result}, expected {-1545}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = Triple(8000000000008)
        assert result == 24000000000024, f"Test 44 failed: got {result}, expected {24000000000024}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = Triple(4000000000000)
        assert result == 12000000000000, f"Test 45 failed: got {result}, expected {12000000000000}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = Triple(-1000000000001)
        assert result == -3000000000003, f"Test 46 failed: got {result}, expected {-3000000000003}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = Triple(509)
        assert result == 1527, f"Test 47 failed: got {result}, expected {1527}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = Triple(-4294967302)
        assert result == -12884901906, f"Test 48 failed: got {result}, expected {-12884901906}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = Triple(-123456787)
        assert result == -370370361, f"Test 49 failed: got {result}, expected {-370370361}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = Triple(-15)
        assert result == -45, f"Test 50 failed: got {result}, expected {-45}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = Triple(1256637062)
        assert result == 3769911186, f"Test 51 failed: got {result}, expected {3769911186}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = Triple(314159263)
        assert result == 942477789, f"Test 52 failed: got {result}, expected {942477789}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = Triple(99999999999999999999)
        assert result == 299999999999999999997, f"Test 53 failed: got {result}, expected {299999999999999999997}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
