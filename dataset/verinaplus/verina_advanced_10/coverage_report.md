# Coverage Report

Total executable lines: 9
Covered lines: 9
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def findExponents(n, primes):
2: ✓     result = []
3: ✓     for p in primes:
4: ✓         exponent = 0
5: ✓         while n % p == 0:
6: ✓             n //= p
7: ✓             exponent += 1
8: ✓         result.append((p, exponent))
9: ✓     return result
```

## Complete Test File

```python
def findExponents(n, primes):
    result = []
    for p in primes:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        result.append((p, exponent))
    return result

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = findExponents(6, [2, 3])
        assert result == [(2, 1), (3, 1)], f"Test 1 failed: got {result}, expected {[(2, 1), (3, 1)]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = findExponents(6285195213566005335561053533150026217291776, [2, 3, 5])
        assert result == [(2, 55), (3, 55), (5, 0)], f"Test 2 failed: got {result}, expected {[(2, 55), (3, 55), (5, 0)]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = findExponents(360, [2, 3, 5])
        assert result == [(2, 3), (3, 2), (5, 1)], f"Test 3 failed: got {result}, expected {[(2, 3), (3, 2), (5, 1)]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = findExponents(18903812908, [2, 43, 823, 133543])
        assert result == [(2, 2), (43, 1), (823, 1), (133543, 1)], f"Test 4 failed: got {result}, expected {[(2, 2), (43, 1), (823, 1), (133543, 1)]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = findExponents(114514, [2, 31, 1847])
        assert result == [(2, 1), (31, 1), (1847, 1)], f"Test 5 failed: got {result}, expected {[(2, 1), (31, 1), (1847, 1)]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = findExponents(20241147794175, [3, 5, 7, 11, 31, 47])
        assert result == [(3, 3), (5, 2), (7, 1), (11, 3), (31, 1), (47, 3)], f"Test 6 failed: got {result}, expected {[(3, 3), (5, 2), (7, 1), (11, 3), (31, 1), (47, 3)]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = findExponents(1, [2])
        assert result == [(2, 0)], f"Test 7 failed: got {result}, expected {[(2, 0)]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = findExponents(1, [2, 3, 5])
        assert result == [(2, 0), (3, 0), (5, 0)], f"Test 8 failed: got {result}, expected {[(2, 0), (3, 0), (5, 0)]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = findExponents(2, [2])
        assert result == [(2, 1)], f"Test 9 failed: got {result}, expected {[(2, 1)]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = findExponents(4, [2])
        assert result == [(2, 2)], f"Test 10 failed: got {result}, expected {[(2, 2)]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = findExponents(8, [2])
        assert result == [(2, 3)], f"Test 11 failed: got {result}, expected {[(2, 3)]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = findExponents(9, [3])
        assert result == [(3, 2)], f"Test 12 failed: got {result}, expected {[(3, 2)]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = findExponents(27, [3])
        assert result == [(3, 3)], f"Test 13 failed: got {result}, expected {[(3, 3)]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = findExponents(12, [2, 3])
        assert result == [(2, 2), (3, 1)], f"Test 14 failed: got {result}, expected {[(2, 2), (3, 1)]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = findExponents(18, [2, 3])
        assert result == [(2, 1), (3, 2)], f"Test 15 failed: got {result}, expected {[(2, 1), (3, 2)]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = findExponents(72, [2, 3])
        assert result == [(2, 3), (3, 2)], f"Test 16 failed: got {result}, expected {[(2, 3), (3, 2)]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = findExponents(540, [2, 3, 5])
        assert result == [(2, 2), (3, 3), (5, 1)], f"Test 17 failed: got {result}, expected {[(2, 2), (3, 3), (5, 1)]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = findExponents(625, [5])
        assert result == [(5, 4)], f"Test 18 failed: got {result}, expected {[(5, 4)]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = findExponents(1001, [7, 11, 13])
        assert result == [(7, 1), (11, 1), (13, 1)], f"Test 19 failed: got {result}, expected {[(7, 1), (11, 1), (13, 1)]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = findExponents(2310, [2, 3, 5, 7, 11])
        assert result == [(2, 1), (3, 1), (5, 1), (7, 1), (11, 1)], f"Test 20 failed: got {result}, expected {[(2, 1), (3, 1), (5, 1), (7, 1), (11, 1)]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = findExponents(30030, [2, 3, 5, 7, 11, 13])
        assert result == [(2, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1)], f"Test 21 failed: got {result}, expected {[(2, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1)]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = findExponents(9699690, [2, 3, 5, 7, 11, 13, 17, 19])
        assert result == [(2, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1)], f"Test 22 failed: got {result}, expected {[(2, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1)]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = findExponents(1024, [2, 3])
        assert result == [(2, 10), (3, 0)], f"Test 23 failed: got {result}, expected {[(2, 10), (3, 0)]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = findExponents(6561, [3, 2])
        assert result == [(3, 8), (2, 0)], f"Test 24 failed: got {result}, expected {[(3, 8), (2, 0)]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = findExponents(7776, [2, 3])
        assert result == [(2, 5), (3, 5)], f"Test 25 failed: got {result}, expected {[(2, 5), (3, 5)]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = findExponents(46656, [2, 3])
        assert result == [(2, 6), (3, 6)], f"Test 26 failed: got {result}, expected {[(2, 6), (3, 6)]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = findExponents(15625, [2, 5])
        assert result == [(2, 0), (5, 6)], f"Test 27 failed: got {result}, expected {[(2, 0), (5, 6)]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = findExponents(44100, [2, 3, 5, 7])
        assert result == [(2, 2), (3, 2), (5, 2), (7, 2)], f"Test 28 failed: got {result}, expected {[(2, 2), (3, 2), (5, 2), (7, 2)]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = findExponents(97, [97])
        assert result == [(97, 1)], f"Test 29 failed: got {result}, expected {[(97, 1)]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = findExponents(9409, [97])
        assert result == [(97, 2)], f"Test 30 failed: got {result}, expected {[(97, 2)]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = findExponents(10403, [101, 103])
        assert result == [(101, 1), (103, 1)], f"Test 31 failed: got {result}, expected {[(101, 1), (103, 1)]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = findExponents(7429, [17, 19, 23])
        assert result == [(17, 1), (19, 1), (23, 1)], f"Test 32 failed: got {result}, expected {[(17, 1), (19, 1), (23, 1)]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = findExponents(223092870, [2, 3, 5, 7, 11, 13, 17, 19, 23])
        assert result == [(2, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1)], f"Test 33 failed: got {result}, expected {[(2, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1)]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = findExponents(4294967296, [2])
        assert result == [(2, 32)], f"Test 34 failed: got {result}, expected {[(2, 32)]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = findExponents(3486784401, [3])
        assert result == [(3, 20)], f"Test 35 failed: got {result}, expected {[(3, 20)]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = findExponents(244140625, [5, 2, 3])
        assert result == [(5, 12), (2, 0), (3, 0)], f"Test 36 failed: got {result}, expected {[(5, 12), (2, 0), (3, 0)]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = findExponents(4, [2, 3])
        assert result == [(2, 2), (3, 0)], f"Test 37 failed: got {result}, expected {[(2, 2), (3, 0)]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = findExponents(1, [2, 3, 5])
        assert result == [(2, 0), (3, 0), (5, 0)], f"Test 38 failed: got {result}, expected {[(2, 0), (3, 0), (5, 0)]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = findExponents(64, [101, 5, 3, 2])
        assert result == [(101, 0), (5, 0), (3, 0), (2, 6)], f"Test 39 failed: got {result}, expected {[(101, 0), (5, 0), (3, 0), (2, 6)]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = findExponents(15625, [2, 3, 5])
        assert result == [(2, 0), (3, 0), (5, 6)], f"Test 40 failed: got {result}, expected {[(2, 0), (3, 0), (5, 6)]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = findExponents(7776, [5, 3, 2])
        assert result == [(5, 0), (3, 5), (2, 5)], f"Test 41 failed: got {result}, expected {[(5, 0), (3, 5), (2, 5)]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = findExponents(46656, [2, 3, 5])
        assert result == [(2, 6), (3, 6), (5, 0)], f"Test 42 failed: got {result}, expected {[(2, 6), (3, 6), (5, 0)]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = findExponents(18903812908, [133543, 823, 43, 2])
        assert result == [(133543, 1), (823, 1), (43, 1), (2, 2)], f"Test 43 failed: got {result}, expected {[(133543, 1), (823, 1), (43, 1), (2, 2)]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = findExponents(2, [2, 43, 823, 133543])
        assert result == [(2, 1), (43, 0), (823, 0), (133543, 0)], f"Test 44 failed: got {result}, expected {[(2, 1), (43, 0), (823, 0), (133543, 0)]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = findExponents(64, [1847, 31, 2])
        assert result == [(1847, 0), (31, 0), (2, 6)], f"Test 45 failed: got {result}, expected {[(1847, 0), (31, 0), (2, 6)]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = findExponents(1, [2, 3])
        assert result == [(2, 0), (3, 0)], f"Test 46 failed: got {result}, expected {[(2, 0), (3, 0)]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = findExponents(12, [3, 2])
        assert result == [(3, 1), (2, 2)], f"Test 47 failed: got {result}, expected {[(3, 1), (2, 2)]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = findExponents(3, [5, 3, 2])
        assert result == [(5, 0), (3, 1), (2, 0)], f"Test 48 failed: got {result}, expected {[(5, 0), (3, 1), (2, 0)]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = findExponents(2, [5, 3, 2])
        assert result == [(5, 0), (3, 0), (2, 1)], f"Test 49 failed: got {result}, expected {[(5, 0), (3, 0), (2, 1)]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = findExponents(2, [2, 3, 5])
        assert result == [(2, 1), (3, 0), (5, 0)], f"Test 50 failed: got {result}, expected {[(2, 1), (3, 0), (5, 0)]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = findExponents(1, [3, 5])
        assert result == [(3, 0), (5, 0)], f"Test 51 failed: got {result}, expected {[(3, 0), (5, 0)]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = findExponents(8, [2, 19])
        assert result == [(2, 3), (19, 0)], f"Test 52 failed: got {result}, expected {[(2, 3), (19, 0)]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = findExponents(24, [2, 3])
        assert result == [(2, 3), (3, 1)], f"Test 53 failed: got {result}, expected {[(2, 3), (3, 1)]}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = findExponents(24, [3, 2])
        assert result == [(3, 1), (2, 3)], f"Test 54 failed: got {result}, expected {[(3, 1), (2, 3)]}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = findExponents(1, [2, 3])
        assert result == [(2, 0), (3, 0)], f"Test 55 failed: got {result}, expected {[(2, 0), (3, 0)]}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = findExponents(36, [2, 3])
        assert result == [(2, 2), (3, 2)], f"Test 56 failed: got {result}, expected {[(2, 2), (3, 2)]}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = findExponents(72, [3, 2])
        assert result == [(3, 2), (2, 3)], f"Test 57 failed: got {result}, expected {[(3, 2), (2, 3)]}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = findExponents(1440, [2, 3, 5])
        assert result == [(2, 5), (3, 2), (5, 1)], f"Test 58 failed: got {result}, expected {[(2, 5), (3, 2), (5, 1)]}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = findExponents(36, [2, 3, 5])
        assert result == [(2, 2), (3, 2), (5, 0)], f"Test 59 failed: got {result}, expected {[(2, 2), (3, 2), (5, 0)]}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = findExponents(540, [5, 3, 2])
        assert result == [(5, 1), (3, 3), (2, 2)], f"Test 60 failed: got {result}, expected {[(5, 1), (3, 3), (2, 2)]}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = findExponents(4, [2, 3, 5, 11])
        assert result == [(2, 2), (3, 0), (5, 0), (11, 0)], f"Test 61 failed: got {result}, expected {[(2, 2), (3, 0), (5, 0), (11, 0)]}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = findExponents(4620, [2, 3, 5, 7, 11])
        assert result == [(2, 2), (3, 1), (5, 1), (7, 1), (11, 1)], f"Test 62 failed: got {result}, expected {[(2, 2), (3, 1), (5, 1), (7, 1), (11, 1)]}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = findExponents(2310, [13, 11, 7, 5, 3, 2])
        assert result == [(13, 0), (11, 1), (7, 1), (5, 1), (3, 1), (2, 1)], f"Test 63 failed: got {result}, expected {[(13, 0), (11, 1), (7, 1), (5, 1), (3, 1), (2, 1)]}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = findExponents(9699690, [19, 17, 13, 11, 7, 5, 3, 2])
        assert result == [(19, 1), (17, 1), (13, 1), (11, 1), (7, 1), (5, 1), (3, 1), (2, 1)], f"Test 64 failed: got {result}, expected {[(19, 1), (17, 1), (13, 1), (11, 1), (7, 1), (5, 1), (3, 1), (2, 1)]}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = findExponents(70, [2, 5, 7, 11, 13, 17, 19])
        assert result == [(2, 1), (5, 1), (7, 1), (11, 0), (13, 0), (17, 0), (19, 0)], f"Test 65 failed: got {result}, expected {[(2, 1), (5, 1), (7, 1), (11, 0), (13, 0), (17, 0), (19, 0)]}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = findExponents(19399380, [2, 3, 5, 7, 11, 13, 17, 19])
        assert result == [(2, 2), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1)], f"Test 66 failed: got {result}, expected {[(2, 2), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1)]}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = findExponents(3, [2, 3])
        assert result == [(2, 0), (3, 1)], f"Test 67 failed: got {result}, expected {[(2, 0), (3, 1)]}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = findExponents(6561, [2, 3])
        assert result == [(2, 0), (3, 8)], f"Test 68 failed: got {result}, expected {[(2, 0), (3, 8)]}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = findExponents(93312, [2, 3])
        assert result == [(2, 7), (3, 6)], f"Test 69 failed: got {result}, expected {[(2, 7), (3, 6)]}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = findExponents(15625, [5, 2])
        assert result == [(5, 6), (2, 0)], f"Test 70 failed: got {result}, expected {[(5, 6), (2, 0)]}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = findExponents(1024, [2, 5])
        assert result == [(2, 10), (5, 0)], f"Test 71 failed: got {result}, expected {[(2, 10), (5, 0)]}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = findExponents(10, [5, 2])
        assert result == [(5, 1), (2, 1)], f"Test 72 failed: got {result}, expected {[(5, 1), (2, 1)]}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = findExponents(15625, [5])
        assert result == [(5, 6)], f"Test 73 failed: got {result}, expected {[(5, 6)]}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = findExponents(88200, [2, 3, 5, 7])
        assert result == [(2, 3), (3, 2), (5, 2), (7, 2)], f"Test 74 failed: got {result}, expected {[(2, 3), (3, 2), (5, 2), (7, 2)]}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = findExponents(24, [2, 3, 5, 7])
        assert result == [(2, 3), (3, 1), (5, 0), (7, 0)], f"Test 75 failed: got {result}, expected {[(2, 3), (3, 1), (5, 0), (7, 0)]}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = findExponents(10403, [103, 101])
        assert result == [(103, 1), (101, 1)], f"Test 76 failed: got {result}, expected {[(103, 1), (101, 1)]}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = findExponents(103, [103])
        assert result == [(103, 1)], f"Test 77 failed: got {result}, expected {[(103, 1)]}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = findExponents(7429, [17, 19, 23, 5])
        assert result == [(17, 1), (19, 1), (23, 1), (5, 0)], f"Test 78 failed: got {result}, expected {[(17, 1), (19, 1), (23, 1), (5, 0)]}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = findExponents(6285195213566005335561053533150026217291776, [23, 19, 17, 13, 11, 7, 5, 3, 2])
        assert result == [(23, 0), (19, 0), (17, 0), (13, 0), (11, 0), (7, 0), (5, 0), (3, 55), (2, 55)], f"Test 79 failed: got {result}, expected {[(23, 0), (19, 0), (17, 0), (13, 0), (11, 0), (7, 0), (5, 0), (3, 55), (2, 55)]}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = findExponents(4620, [23, 19, 17, 13, 11, 7, 5, 3, 2])
        assert result == [(23, 0), (19, 0), (17, 0), (13, 0), (11, 1), (7, 1), (5, 1), (3, 1), (2, 2)], f"Test 80 failed: got {result}, expected {[(23, 0), (19, 0), (17, 0), (13, 0), (11, 1), (7, 1), (5, 1), (3, 1), (2, 2)]}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = findExponents(68, [23, 19, 17, 13, 11, 7, 5, 3, 2])
        assert result == [(23, 0), (19, 0), (17, 1), (13, 0), (11, 0), (7, 0), (5, 0), (3, 0), (2, 2)], f"Test 81 failed: got {result}, expected {[(23, 0), (19, 0), (17, 1), (13, 0), (11, 0), (7, 0), (5, 0), (3, 0), (2, 2)]}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = findExponents(446185740, [2, 3, 5, 7, 11, 13, 17, 19, 23])
        assert result == [(2, 2), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1)], f"Test 82 failed: got {result}, expected {[(2, 2), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1)]}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = findExponents(244140625, [3, 2, 5])
        assert result == [(3, 0), (2, 0), (5, 12)], f"Test 83 failed: got {result}, expected {[(3, 0), (2, 0), (5, 12)]}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
