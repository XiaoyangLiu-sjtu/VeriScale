# Coverage Report

Total executable lines: 4
Covered lines: 4
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def Triple(x):
2: ✓     if x < 18:
3: ✓         return 3 * x
4:       else:
5: ✓         return 3 * x
```

## Complete Test File

```python
def Triple(x):
    if x < 18:
        return 3 * x
    else:
        return 3 * x

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = Triple(10)
        assert result == 30, f"Test 1 failed: got {result}, expected {30}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = Triple(18)
        assert result == 54, f"Test 2 failed: got {result}, expected {54}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = Triple(0)
        assert result == 0, f"Test 3 failed: got {result}, expected {0}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = Triple(-5)
        assert result == -15, f"Test 4 failed: got {result}, expected {-15}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = Triple(25)
        assert result == 75, f"Test 5 failed: got {result}, expected {75}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = Triple(-100)
        assert result == -300, f"Test 6 failed: got {result}, expected {-300}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = Triple(-19)
        assert result == -57, f"Test 7 failed: got {result}, expected {-57}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = Triple(-17)
        assert result == -51, f"Test 8 failed: got {result}, expected {-51}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = Triple(5)
        assert result == 15, f"Test 9 failed: got {result}, expected {15}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = Triple(16)
        assert result == 48, f"Test 10 failed: got {result}, expected {48}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = Triple(17)
        assert result == 51, f"Test 11 failed: got {result}, expected {51}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = Triple(19)
        assert result == 57, f"Test 12 failed: got {result}, expected {57}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = Triple(20)
        assert result == 60, f"Test 13 failed: got {result}, expected {60}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = Triple(100)
        assert result == 300, f"Test 14 failed: got {result}, expected {300}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = Triple(1000)
        assert result == 3000, f"Test 15 failed: got {result}, expected {3000}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = Triple(-1000)
        assert result == -3000, f"Test 16 failed: got {result}, expected {-3000}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = Triple(2147483647)
        assert result == 6442450941, f"Test 17 failed: got {result}, expected {6442450941}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = Triple(-2147483648)
        assert result == -6442450944, f"Test 18 failed: got {result}, expected {-6442450944}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = Triple(9223372036854775807)
        assert result == 27670116110564327421, f"Test 19 failed: got {result}, expected {27670116110564327421}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = Triple(-9223372036854775808)
        assert result == -27670116110564327424, f"Test 20 failed: got {result}, expected {-27670116110564327424}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = Triple(2147483648)
        assert result == 6442450944, f"Test 21 failed: got {result}, expected {6442450944}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = Triple(7)
        assert result == 21, f"Test 22 failed: got {result}, expected {21}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = Triple(-7)
        assert result == -21, f"Test 23 failed: got {result}, expected {-21}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = Triple(100000000000000000000)
        assert result == 300000000000000000000, f"Test 24 failed: got {result}, expected {300000000000000000000}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = Triple(-100000000000000000000)
        assert result == -300000000000000000000, f"Test 25 failed: got {result}, expected {-300000000000000000000}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = Triple(-10)
        assert result == -30, f"Test 26 failed: got {result}, expected {-30}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = Triple(8)
        assert result == 24, f"Test 27 failed: got {result}, expected {24}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = Triple(28)
        assert result == 84, f"Test 28 failed: got {result}, expected {84}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = Triple(-4)
        assert result == -12, f"Test 29 failed: got {result}, expected {-12}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = Triple(22)
        assert result == 66, f"Test 30 failed: got {result}, expected {66}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = Triple(-22)
        assert result == -66, f"Test 31 failed: got {result}, expected {-66}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = Triple(41)
        assert result == 123, f"Test 32 failed: got {result}, expected {123}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = Triple(-2)
        assert result == -6, f"Test 33 failed: got {result}, expected {-6}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = Triple(-11)
        assert result == -33, f"Test 34 failed: got {result}, expected {-33}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = Triple(11)
        assert result == 33, f"Test 35 failed: got {result}, expected {33}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = Triple(-16)
        assert result == -48, f"Test 36 failed: got {result}, expected {-48}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = Triple(23)
        assert result == 69, f"Test 37 failed: got {result}, expected {69}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = Triple(-398)
        assert result == -1194, f"Test 38 failed: got {result}, expected {-1194}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = Triple(-394)
        assert result == -1182, f"Test 39 failed: got {result}, expected {-1182}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = Triple(-101)
        assert result == -303, f"Test 40 failed: got {result}, expected {-303}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = Triple(43)
        assert result == 129, f"Test 41 failed: got {result}, expected {129}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = Triple(-1001)
        assert result == -3003, f"Test 42 failed: got {result}, expected {-3003}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = Triple(-38)
        assert result == -114, f"Test 43 failed: got {result}, expected {-114}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = Triple(38)
        assert result == 114, f"Test 44 failed: got {result}, expected {114}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = Triple(-14)
        assert result == -42, f"Test 45 failed: got {result}, expected {-42}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = Triple(-397)
        assert result == -1191, f"Test 46 failed: got {result}, expected {-1191}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = Triple(-1000000000003)
        assert result == -3000000000009, f"Test 47 failed: got {result}, expected {-3000000000009}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = Triple(14)
        assert result == 42, f"Test 48 failed: got {result}, expected {42}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = Triple(4)
        assert result == 12, f"Test 49 failed: got {result}, expected {12}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = Triple(-200)
        assert result == -600, f"Test 50 failed: got {result}, expected {-600}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = Triple(-2147483650)
        assert result == -6442450950, f"Test 51 failed: got {result}, expected {-6442450950}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = Triple(-20)
        assert result == -60, f"Test 52 failed: got {result}, expected {-60}"
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
