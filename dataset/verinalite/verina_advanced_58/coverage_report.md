# Coverage Report

Total executable lines: 17
Covered lines: 17
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def nthUglyNumber(n):
2: ✓     ugly = [0] * n
3: ✓     ugly[0] = 1
4: ✓     i2 = i3 = i5 = 0
5: ✓     for i in range(1, n):
6: ✓         next2 = ugly[i2] * 2
7: ✓         next3 = ugly[i3] * 3
8: ✓         next5 = ugly[i5] * 5
9: ✓         next_ugly = min(next2, next3, next5)
10: ✓         ugly[i] = next_ugly
11: ✓         if next_ugly == next2:
12: ✓             i2 += 1
13: ✓         if next_ugly == next3:
14: ✓             i3 += 1
15: ✓         if next_ugly == next5:
16: ✓             i5 += 1
17: ✓     return ugly[-1]
```

## Complete Test File

```python
def nthUglyNumber(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    for i in range(1, n):
        next2 = ugly[i2] * 2
        next3 = ugly[i3] * 3
        next5 = ugly[i5] * 5
        next_ugly = min(next2, next3, next5)
        ugly[i] = next_ugly
        if next_ugly == next2:
            i2 += 1
        if next_ugly == next3:
            i3 += 1
        if next_ugly == next5:
            i5 += 1
    return ugly[-1]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = nthUglyNumber(1)
        assert result == 1, f"Test 1 failed: got {result}, expected {1}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = nthUglyNumber(10)
        assert result == 12, f"Test 2 failed: got {result}, expected {12}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = nthUglyNumber(15)
        assert result == 24, f"Test 3 failed: got {result}, expected {24}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = nthUglyNumber(5)
        assert result == 5, f"Test 4 failed: got {result}, expected {5}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = nthUglyNumber(7)
        assert result == 8, f"Test 5 failed: got {result}, expected {8}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = nthUglyNumber(2)
        assert result == 2, f"Test 6 failed: got {result}, expected {2}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = nthUglyNumber(3)
        assert result == 3, f"Test 7 failed: got {result}, expected {3}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = nthUglyNumber(4)
        assert result == 4, f"Test 8 failed: got {result}, expected {4}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = nthUglyNumber(6)
        assert result == 6, f"Test 9 failed: got {result}, expected {6}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = nthUglyNumber(8)
        assert result == 9, f"Test 10 failed: got {result}, expected {9}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = nthUglyNumber(9)
        assert result == 10, f"Test 11 failed: got {result}, expected {10}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = nthUglyNumber(11)
        assert result == 15, f"Test 12 failed: got {result}, expected {15}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = nthUglyNumber(12)
        assert result == 16, f"Test 13 failed: got {result}, expected {16}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = nthUglyNumber(20)
        assert result == 36, f"Test 14 failed: got {result}, expected {36}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = nthUglyNumber(25)
        assert result == 54, f"Test 15 failed: got {result}, expected {54}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = nthUglyNumber(30)
        assert result == 80, f"Test 16 failed: got {result}, expected {80}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = nthUglyNumber(31)
        assert result == 81, f"Test 17 failed: got {result}, expected {81}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = nthUglyNumber(32)
        assert result == 90, f"Test 18 failed: got {result}, expected {90}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = nthUglyNumber(33)
        assert result == 96, f"Test 19 failed: got {result}, expected {96}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = nthUglyNumber(34)
        assert result == 100, f"Test 20 failed: got {result}, expected {100}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = nthUglyNumber(50)
        assert result == 243, f"Test 21 failed: got {result}, expected {243}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = nthUglyNumber(75)
        assert result == 675, f"Test 22 failed: got {result}, expected {675}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = nthUglyNumber(100)
        assert result == 1536, f"Test 23 failed: got {result}, expected {1536}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = nthUglyNumber(125)
        assert result == 3125, f"Test 24 failed: got {result}, expected {3125}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = nthUglyNumber(150)
        assert result == 5832, f"Test 25 failed: got {result}, expected {5832}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = nthUglyNumber(169)
        assert result == 8748, f"Test 26 failed: got {result}, expected {8748}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = nthUglyNumber(200)
        assert result == 16200, f"Test 27 failed: got {result}, expected {16200}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = nthUglyNumber(256)
        assert result == 43200, f"Test 28 failed: got {result}, expected {43200}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = nthUglyNumber(500)
        assert result == 937500, f"Test 29 failed: got {result}, expected {937500}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = nthUglyNumber(1000)
        assert result == 51200000, f"Test 30 failed: got {result}, expected {51200000}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = nthUglyNumber(1500)
        assert result == 859963392, f"Test 31 failed: got {result}, expected {859963392}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = nthUglyNumber(1690)
        assert result == 2123366400, f"Test 32 failed: got {result}, expected {2123366400}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = nthUglyNumber(338)
        assert result == 144000, f"Test 33 failed: got {result}, expected {144000}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = nthUglyNumber(71)
        assert result == 600, f"Test 34 failed: got {result}, expected {600}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = nthUglyNumber(1691)
        assert result == 2125764000, f"Test 35 failed: got {result}, expected {2125764000}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = nthUglyNumber(1689)
        assert result == 2109375000, f"Test 36 failed: got {result}, expected {2109375000}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = nthUglyNumber(300)
        assert result == 82944, f"Test 37 failed: got {result}, expected {82944}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = nthUglyNumber(1692)
        assert result == 2147483648, f"Test 38 failed: got {result}, expected {2147483648}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = nthUglyNumber(17)
        assert result == 27, f"Test 39 failed: got {result}, expected {27}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = nthUglyNumber(999)
        assert result == 51018336, f"Test 40 failed: got {result}, expected {51018336}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = nthUglyNumber(123)
        assert result == 3000, f"Test 41 failed: got {result}, expected {3000}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = nthUglyNumber(399)
        assert result == 307200, f"Test 42 failed: got {result}, expected {307200}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = nthUglyNumber(64)
        assert result == 450, f"Test 43 failed: got {result}, expected {450}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = nthUglyNumber(63)
        assert result == 432, f"Test 44 failed: got {result}, expected {432}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = nthUglyNumber(68)
        assert result == 512, f"Test 45 failed: got {result}, expected {512}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = nthUglyNumber(16)
        assert result == 25, f"Test 46 failed: got {result}, expected {25}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = nthUglyNumber(245)
        assert result == 36000, f"Test 47 failed: got {result}, expected {36000}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = nthUglyNumber(19)
        assert result == 32, f"Test 48 failed: got {result}, expected {32}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = nthUglyNumber(35)
        assert result == 108, f"Test 49 failed: got {result}, expected {108}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = nthUglyNumber(2000)
        assert result == 8062156800, f"Test 50 failed: got {result}, expected {8062156800}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = nthUglyNumber(18)
        assert result == 30, f"Test 51 failed: got {result}, expected {30}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = nthUglyNumber(138)
        assert result == 4320, f"Test 52 failed: got {result}, expected {4320}"
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
