# Coverage Report

Total executable lines: 6
Covered lines: 6
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def SquareRoot(N):
2: ✓     def helper(r):
3: ✓         if (r + 1) * (r + 1) > N:
4: ✓             return r
5: ✓         return helper(r + 1)
6: ✓     return helper(0)
```

## Complete Test File

```python
def SquareRoot(N):
    def helper(r):
        if (r + 1) * (r + 1) > N:
            return r
        return helper(r + 1)
    return helper(0)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = SquareRoot(0)
        assert result == 0, f"Test 1 failed: got {result}, expected {0}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = SquareRoot(1)
        assert result == 1, f"Test 2 failed: got {result}, expected {1}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = SquareRoot(15)
        assert result == 3, f"Test 3 failed: got {result}, expected {3}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = SquareRoot(16)
        assert result == 4, f"Test 4 failed: got {result}, expected {4}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = SquareRoot(26)
        assert result == 5, f"Test 5 failed: got {result}, expected {5}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = SquareRoot(2)
        assert result == 1, f"Test 6 failed: got {result}, expected {1}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = SquareRoot(3)
        assert result == 1, f"Test 7 failed: got {result}, expected {1}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = SquareRoot(4)
        assert result == 2, f"Test 8 failed: got {result}, expected {2}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = SquareRoot(8)
        assert result == 2, f"Test 9 failed: got {result}, expected {2}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = SquareRoot(9)
        assert result == 3, f"Test 10 failed: got {result}, expected {3}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = SquareRoot(10)
        assert result == 3, f"Test 11 failed: got {result}, expected {3}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = SquareRoot(17)
        assert result == 4, f"Test 12 failed: got {result}, expected {4}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = SquareRoot(24)
        assert result == 4, f"Test 13 failed: got {result}, expected {4}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = SquareRoot(25)
        assert result == 5, f"Test 14 failed: got {result}, expected {5}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = SquareRoot(35)
        assert result == 5, f"Test 15 failed: got {result}, expected {5}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = SquareRoot(36)
        assert result == 6, f"Test 16 failed: got {result}, expected {6}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = SquareRoot(37)
        assert result == 6, f"Test 17 failed: got {result}, expected {6}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = SquareRoot(48)
        assert result == 6, f"Test 18 failed: got {result}, expected {6}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = SquareRoot(49)
        assert result == 7, f"Test 19 failed: got {result}, expected {7}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = SquareRoot(50)
        assert result == 7, f"Test 20 failed: got {result}, expected {7}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = SquareRoot(63)
        assert result == 7, f"Test 21 failed: got {result}, expected {7}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = SquareRoot(64)
        assert result == 8, f"Test 22 failed: got {result}, expected {8}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = SquareRoot(65)
        assert result == 8, f"Test 23 failed: got {result}, expected {8}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = SquareRoot(80)
        assert result == 8, f"Test 24 failed: got {result}, expected {8}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = SquareRoot(81)
        assert result == 9, f"Test 25 failed: got {result}, expected {9}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = SquareRoot(82)
        assert result == 9, f"Test 26 failed: got {result}, expected {9}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = SquareRoot(99)
        assert result == 9, f"Test 27 failed: got {result}, expected {9}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = SquareRoot(100)
        assert result == 10, f"Test 28 failed: got {result}, expected {10}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = SquareRoot(101)
        assert result == 10, f"Test 29 failed: got {result}, expected {10}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = SquareRoot(255)
        assert result == 15, f"Test 30 failed: got {result}, expected {15}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = SquareRoot(256)
        assert result == 16, f"Test 31 failed: got {result}, expected {16}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = SquareRoot(257)
        assert result == 16, f"Test 32 failed: got {result}, expected {16}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = SquareRoot(1023)
        assert result == 31, f"Test 33 failed: got {result}, expected {31}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = SquareRoot(1024)
        assert result == 32, f"Test 34 failed: got {result}, expected {32}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = SquareRoot(1025)
        assert result == 32, f"Test 35 failed: got {result}, expected {32}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = SquareRoot(1048575)
        assert result == 1023, f"Test 36 failed: got {result}, expected {1023}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = SquareRoot(1048576)
        assert result == 1024, f"Test 37 failed: got {result}, expected {1024}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = SquareRoot(1048577)
        assert result == 1024, f"Test 38 failed: got {result}, expected {1024}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = SquareRoot(2147395600)
        assert result == 46340, f"Test 39 failed: got {result}, expected {46340}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = SquareRoot(2147395601)
        assert result == 46340, f"Test 40 failed: got {result}, expected {46340}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = SquareRoot(18)
        assert result == 4, f"Test 41 failed: got {result}, expected {4}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = SquareRoot(44)
        assert result == 6, f"Test 42 failed: got {result}, expected {6}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = SquareRoot(19)
        assert result == 4, f"Test 43 failed: got {result}, expected {4}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = SquareRoot(4294791200)
        assert result == 65534, f"Test 44 failed: got {result}, expected {65534}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = SquareRoot(20)
        assert result == 4, f"Test 45 failed: got {result}, expected {4}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = SquareRoot(45)
        assert result == 6, f"Test 46 failed: got {result}, expected {6}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = SquareRoot(34)
        assert result == 5, f"Test 47 failed: got {result}, expected {5}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = SquareRoot(13)
        assert result == 3, f"Test 48 failed: got {result}, expected {3}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = SquareRoot(2047)
        assert result == 45, f"Test 49 failed: got {result}, expected {45}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = SquareRoot(199)
        assert result == 14, f"Test 50 failed: got {result}, expected {14}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = SquareRoot(162)
        assert result == 12, f"Test 51 failed: got {result}, expected {12}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = SquareRoot(125)
        assert result == 11, f"Test 52 failed: got {result}, expected {11}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = SquareRoot(6)
        assert result == 2, f"Test 53 failed: got {result}, expected {2}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = SquareRoot(514)
        assert result == 22, f"Test 54 failed: got {result}, expected {22}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = SquareRoot(258)
        assert result == 16, f"Test 55 failed: got {result}, expected {16}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = SquareRoot(1028)
        assert result == 32, f"Test 56 failed: got {result}, expected {32}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = SquareRoot(32)
        assert result == 5, f"Test 57 failed: got {result}, expected {5}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = SquareRoot(127)
        assert result == 11, f"Test 58 failed: got {result}, expected {11}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = SquareRoot(2147395599)
        assert result == 46339, f"Test 59 failed: got {result}, expected {46339}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = SquareRoot(7)
        assert result == 2, f"Test 60 failed: got {result}, expected {2}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = SquareRoot(86)
        assert result == 9, f"Test 61 failed: got {result}, expected {9}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = SquareRoot(198)
        assert result == 14, f"Test 62 failed: got {result}, expected {14}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = SquareRoot(79)
        assert result == 8, f"Test 63 failed: got {result}, expected {8}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = SquareRoot(510)
        assert result == 22, f"Test 64 failed: got {result}, expected {22}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = SquareRoot(172)
        assert result == 13, f"Test 65 failed: got {result}, expected {13}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = SquareRoot(2044)
        assert result == 45, f"Test 66 failed: got {result}, expected {45}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = SquareRoot(200)
        assert result == 14, f"Test 67 failed: got {result}, expected {14}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = SquareRoot(201)
        assert result == 14, f"Test 68 failed: got {result}, expected {14}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = SquareRoot(33)
        assert result == 5, f"Test 69 failed: got {result}, expected {5}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = SquareRoot(96)
        assert result == 9, f"Test 70 failed: got {result}, expected {9}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = SquareRoot(2046)
        assert result == 45, f"Test 71 failed: got {result}, expected {45}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = SquareRoot(88)
        assert result == 9, f"Test 72 failed: got {result}, expected {9}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = SquareRoot(98)
        assert result == 9, f"Test 73 failed: got {result}, expected {9}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = SquareRoot(51)
        assert result == 7, f"Test 74 failed: got {result}, expected {7}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = SquareRoot(62)
        assert result == 7, f"Test 75 failed: got {result}, expected {7}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = SquareRoot(61)
        assert result == 7, f"Test 76 failed: got {result}, expected {7}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = SquareRoot(87)
        assert result == 9, f"Test 77 failed: got {result}, expected {9}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = SquareRoot(124)
        assert result == 11, f"Test 78 failed: got {result}, expected {11}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = SquareRoot(4092)
        assert result == 63, f"Test 79 failed: got {result}, expected {63}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = SquareRoot(164)
        assert result == 12, f"Test 80 failed: got {result}, expected {12}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = SquareRoot(12)
        assert result == 3, f"Test 81 failed: got {result}, expected {3}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = SquareRoot(52)
        assert result == 7, f"Test 82 failed: got {result}, expected {7}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = SquareRoot(342)
        assert result == 18, f"Test 83 failed: got {result}, expected {18}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = SquareRoot(4294791202)
        assert result == 65534, f"Test 84 failed: got {result}, expected {65534}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = SquareRoot(14)
        assert result == 3, f"Test 85 failed: got {result}, expected {3}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = SquareRoot(39)
        assert result == 6, f"Test 86 failed: got {result}, expected {6}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = SquareRoot(1048574)
        assert result == 1023, f"Test 87 failed: got {result}, expected {1023}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = SquareRoot(97)
        assert result == 9, f"Test 88 failed: got {result}, expected {9}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = SquareRoot(394)
        assert result == 19, f"Test 89 failed: got {result}, expected {19}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = SquareRoot(404)
        assert result == 20, f"Test 90 failed: got {result}, expected {20}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = SquareRoot(5)
        assert result == 2, f"Test 91 failed: got {result}, expected {2}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = SquareRoot(254)
        assert result == 15, f"Test 92 failed: got {result}, expected {15}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = SquareRoot(515)
        assert result == 22, f"Test 93 failed: got {result}, expected {22}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = SquareRoot(2052)
        assert result == 45, f"Test 94 failed: got {result}, expected {45}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = SquareRoot(202)
        assert result == 14, f"Test 95 failed: got {result}, expected {14}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = SquareRoot(2048)
        assert result == 45, f"Test 96 failed: got {result}, expected {45}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = SquareRoot(2050)
        assert result == 45, f"Test 97 failed: got {result}, expected {45}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = SquareRoot(194)
        assert result == 13, f"Test 98 failed: got {result}, expected {13}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = SquareRoot(89)
        assert result == 9, f"Test 99 failed: got {result}, expected {9}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = SquareRoot(40)
        assert result == 6, f"Test 100 failed: got {result}, expected {6}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = SquareRoot(248)
        assert result == 15, f"Test 101 failed: got {result}, expected {15}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = SquareRoot(4094)
        assert result == 63, f"Test 102 failed: got {result}, expected {63}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = SquareRoot(68)
        assert result == 8, f"Test 103 failed: got {result}, expected {8}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = SquareRoot(173)
        assert result == 13, f"Test 104 failed: got {result}, expected {13}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = SquareRoot(66)
        assert result == 8, f"Test 105 failed: got {result}, expected {8}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = SquareRoot(171)
        assert result == 13, f"Test 106 failed: got {result}, expected {13}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
