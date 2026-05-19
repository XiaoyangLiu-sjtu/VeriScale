# Coverage Report

Total executable lines: 6
Covered lines: 6
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def countDigits(s):
2: ✓     count = 0
3: ✓     for char in s:
4: ✓         if '0' <= char <= '9':
5: ✓             count += 1
6: ✓     return count
```

## Complete Test File

```python
def countDigits(s):
    count = 0
    for char in s:
        if '0' <= char <= '9':
            count += 1
    return count

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = countDigits('123abc456')
        assert result == 6, f"Test 1 failed: got {result}, expected {6}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = countDigits('no digits here!')
        assert result == 0, f"Test 2 failed: got {result}, expected {0}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = countDigits('1234567890')
        assert result == 10, f"Test 3 failed: got {result}, expected {10}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = countDigits('')
        assert result == 0, f"Test 4 failed: got {result}, expected {0}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = countDigits('a1b2c3')
        assert result == 3, f"Test 5 failed: got {result}, expected {3}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = countDigits('0')
        assert result == 1, f"Test 6 failed: got {result}, expected {1}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = countDigits('abc')
        assert result == 0, f"Test 7 failed: got {result}, expected {0}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = countDigits('9')
        assert result == 1, f"Test 8 failed: got {result}, expected {1}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = countDigits('a')
        assert result == 0, f"Test 9 failed: got {result}, expected {0}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = countDigits('00000')
        assert result == 5, f"Test 10 failed: got {result}, expected {5}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = countDigits('abcDEF')
        assert result == 0, f"Test 11 failed: got {result}, expected {0}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = countDigits('   1   ')
        assert result == 1, f"Test 12 failed: got {result}, expected {1}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = countDigits('\n\t\r')
        assert result == 0, f"Test 13 failed: got {result}, expected {0}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = countDigits('line1\nline2\n3')
        assert result == 3, f"Test 14 failed: got {result}, expected {3}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = countDigits('!@#$%^&*()')
        assert result == 0, f"Test 15 failed: got {result}, expected {0}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = countDigits('１２３')
        assert result == 0, f"Test 16 failed: got {result}, expected {0}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = countDigits('١٢٣')
        assert result == 0, f"Test 17 failed: got {result}, expected {0}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = countDigits('𝟙𝟚𝟛')
        assert result == 0, f"Test 18 failed: got {result}, expected {0}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = countDigits('0xFF')
        assert result == 1, f"Test 19 failed: got {result}, expected {1}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = countDigits('-123.45')
        assert result == 5, f"Test 20 failed: got {result}, expected {5}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = countDigits('+00123')
        assert result == 5, f"Test 21 failed: got {result}, expected {5}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = countDigits('version2.0.1')
        assert result == 3, f"Test 22 failed: got {result}, expected {3}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = countDigits('Room 101')
        assert result == 3, f"Test 23 failed: got {result}, expected {3}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = countDigits('٩lives')
        assert result == 0, f"Test 24 failed: got {result}, expected {0}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = countDigits('０1２3')
        assert result == 2, f"Test 25 failed: got {result}, expected {2}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = countDigits('🙂2🙃3')
        assert result == 2, f"Test 26 failed: got {result}, expected {2}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = countDigits('²³45')
        assert result == 2, f"Test 27 failed: got {result}, expected {2}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = countDigits('1e10')
        assert result == 3, f"Test 28 failed: got {result}, expected {3}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = countDigits('NaN')
        assert result == 0, f"Test 29 failed: got {result}, expected {0}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = countDigits('999999999999999999999999999999')
        assert result == 30, f"Test 30 failed: got {result}, expected {30}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = countDigits('abc123XYZ789!0?')
        assert result == 7, f"Test 31 failed: got {result}, expected {7}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = countDigits('\x00\x015\x02')
        assert result == 1, f"Test 32 failed: got {result}, expected {1}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = countDigits('\\d+\\d*')
        assert result == 0, f"Test 33 failed: got {result}, expected {0}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = countDigits('"123"')
        assert result == 3, f"Test 34 failed: got {result}, expected {3}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = countDigits('tab\t7\tend')
        assert result == 1, f"Test 35 failed: got {result}, expected {1}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = countDigits('newline\n8\n')
        assert result == 1, f"Test 36 failed: got {result}, expected {1}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = countDigits('carriage\r9')
        assert result == 1, f"Test 37 failed: got {result}, expected {1}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = countDigits('mix٠1٢2३3४4')
        assert result == 4, f"Test 38 failed: got {result}, expected {4}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = countDigits('🚀✨')
        assert result == 0, f"Test 39 failed: got {result}, expected {0}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = countDigits('The year is 2026, room 42, code 007.')
        assert result == 9, f"Test 40 failed: got {result}, expected {9}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = countDigits(' ')
        assert result == 0, f"Test 41 failed: got {result}, expected {0}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = countDigits('123abc456_x')
        assert result == 6, f"Test 42 failed: got {result}, expected {6}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = countDigits(' 0')
        assert result == 1, f"Test 43 failed: got {result}, expected {1}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = countDigits('0 ')
        assert result == 1, f"Test 44 failed: got {result}, expected {1}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = countDigits('1 _x')
        assert result == 1, f"Test 45 failed: got {result}, expected {1}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = countDigits('2026,_x')
        assert result == 4, f"Test 46 failed: got {result}, expected {4}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = countDigits('8')
        assert result == 1, f"Test 47 failed: got {result}, expected {1}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = countDigits('123abc456 edge')
        assert result == 6, f"Test 48 failed: got {result}, expected {6}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = countDigits('_x_x')
        assert result == 0, f"Test 49 failed: got {result}, expected {0}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = countDigits('𝟙𝟚𝟛_x')
        assert result == 0, f"Test 50 failed: got {result}, expected {0}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = countDigits('no digits here!_x 0')
        assert result == 1, f"Test 51 failed: got {result}, expected {1}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = countDigits('1e10 edge')
        assert result == 3, f"Test 52 failed: got {result}, expected {3}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = countDigits('3')
        assert result == 1, f"Test 53 failed: got {result}, expected {1}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = countDigits('newline')
        assert result == 0, f"Test 54 failed: got {result}, expected {0}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = countDigits('no digits here! edge_x')
        assert result == 0, f"Test 55 failed: got {result}, expected {0}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = countDigits('no digits here!_x')
        assert result == 0, f"Test 56 failed: got {result}, expected {0}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = countDigits('x_enilwen')
        assert result == 0, f"Test 57 failed: got {result}, expected {0}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = countDigits('0987654321')
        assert result == 10, f"Test 58 failed: got {result}, expected {10}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = countDigits('1234567890_x')
        assert result == 10, f"Test 59 failed: got {result}, expected {10}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = countDigits('x_!ereh stigid on_x')
        assert result == 0, f"Test 60 failed: got {result}, expected {0}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = countDigits('2026, 0 1_x')
        assert result == 6, f"Test 61 failed: got {result}, expected {6}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = countDigits('1 0987654321')
        assert result == 11, f"Test 62 failed: got {result}, expected {11}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = countDigits('ehT')
        assert result == 0, f"Test 63 failed: got {result}, expected {0}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = countDigits(' 1_x')
        assert result == 1, f"Test 64 failed: got {result}, expected {1}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = countDigits('egde 0987654321')
        assert result == 10, f"Test 65 failed: got {result}, expected {10}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = countDigits('x_0987654321_x_x')
        assert result == 10, f"Test 66 failed: got {result}, expected {10}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = countDigits('_x')
        assert result == 0, f"Test 67 failed: got {result}, expected {0}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = countDigits('\x00\x015\x02 edge')
        assert result == 1, f"Test 68 failed: got {result}, expected {1}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = countDigits('end')
        assert result == 0, f"Test 69 failed: got {result}, expected {0}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = countDigits(' 1_x_x')
        assert result == 1, f"Test 70 failed: got {result}, expected {1}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = countDigits(' 1')
        assert result == 1, f"Test 71 failed: got {result}, expected {1}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = countDigits(' edge')
        assert result == 0, f"Test 72 failed: got {result}, expected {0}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = countDigits('egde  1')
        assert result == 1, f"Test 73 failed: got {result}, expected {1}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = countDigits('stigid')
        assert result == 0, f"Test 74 failed: got {result}, expected {0}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = countDigits('x_')
        assert result == 0, f"Test 75 failed: got {result}, expected {0}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = countDigits(' 0 edge')
        assert result == 1, f"Test 76 failed: got {result}, expected {1}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = countDigits('🙂2🙃3 1')
        assert result == 3, f"Test 77 failed: got {result}, expected {3}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = countDigits('1 !ereh stigid on')
        assert result == 1, f"Test 78 failed: got {result}, expected {1}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = countDigits('dne\t7\tbat')
        assert result == 1, f"Test 79 failed: got {result}, expected {1}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = countDigits('1')
        assert result == 1, f"Test 80 failed: got {result}, expected {1}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = countDigits('🙂2🙃3 1_x')
        assert result == 3, f"Test 81 failed: got {result}, expected {3}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = countDigits('101 edge')
        assert result == 3, f"Test 82 failed: got {result}, expected {3}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = countDigits('tab')
        assert result == 0, f"Test 83 failed: got {result}, expected {0}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = countDigits('no_x')
        assert result == 0, f"Test 84 failed: got {result}, expected {0}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = countDigits('3c2b1a_x 1 edge 1')
        assert result == 5, f"Test 85 failed: got {result}, expected {5}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = countDigits('0 0')
        assert result == 2, f"Test 86 failed: got {result}, expected {2}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = countDigits('room_x')
        assert result == 0, f"Test 87 failed: got {result}, expected {0}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = countDigits('here!_x')
        assert result == 0, f"Test 88 failed: got {result}, expected {0}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = countDigits('abc 0')
        assert result == 1, f"Test 89 failed: got {result}, expected {1}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = countDigits('cba')
        assert result == 0, f"Test 90 failed: got {result}, expected {0}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = countDigits('no')
        assert result == 0, f"Test 91 failed: got {result}, expected {0}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = countDigits('egde x_abc_x')
        assert result == 0, f"Test 92 failed: got {result}, expected {0}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = countDigits('101 0')
        assert result == 4, f"Test 93 failed: got {result}, expected {4}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = countDigits('stigid_x')
        assert result == 0, f"Test 94 failed: got {result}, expected {0}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = countDigits('abc_x')
        assert result == 0, f"Test 95 failed: got {result}, expected {0}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = countDigits('The')
        assert result == 0, f"Test 96 failed: got {result}, expected {0}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = countDigits('Room')
        assert result == 0, f"Test 97 failed: got {result}, expected {0}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = countDigits('9 0')
        assert result == 2, f"Test 98 failed: got {result}, expected {2}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = countDigits('abcDEF_x_x 1')
        assert result == 1, f"Test 99 failed: got {result}, expected {1}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = countDigits('egde 9')
        assert result == 1, f"Test 100 failed: got {result}, expected {1}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = countDigits('x_x_9')
        assert result == 1, f"Test 101 failed: got {result}, expected {1}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = countDigits('9 edge')
        assert result == 1, f"Test 102 failed: got {result}, expected {1}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = countDigits('9 1')
        assert result == 2, f"Test 103 failed: got {result}, expected {2}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = countDigits('9_x')
        assert result == 1, f"Test 104 failed: got {result}, expected {1}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = countDigits('carriage_x')
        assert result == 0, f"Test 105 failed: got {result}, expected {0}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = countDigits('a_x')
        assert result == 0, f"Test 106 failed: got {result}, expected {0}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = countDigits('a 1')
        assert result == 1, f"Test 107 failed: got {result}, expected {1}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = countDigits('end 0')
        assert result == 1, f"Test 108 failed: got {result}, expected {1}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = countDigits('a_x 0 edge')
        assert result == 1, f"Test 109 failed: got {result}, expected {1}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = countDigits('_x 0 0')
        assert result == 2, f"Test 110 failed: got {result}, expected {2}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = countDigits('a 0_x')
        assert result == 1, f"Test 111 failed: got {result}, expected {1}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = countDigits('"321"')
        assert result == 3, f"Test 112 failed: got {result}, expected {3}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = countDigits('123abc456 1')
        assert result == 7, f"Test 113 failed: got {result}, expected {7}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = countDigits('abcDEF_x_x 1 1 edge')
        assert result == 2, f"Test 114 failed: got {result}, expected {2}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = countDigits('00000 1')
        assert result == 6, f"Test 115 failed: got {result}, expected {6}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = countDigits('egde edge')
        assert result == 0, f"Test 116 failed: got {result}, expected {0}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = countDigits('x_FEDcba')
        assert result == 0, f"Test 117 failed: got {result}, expected {0}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = countDigits('egde x_0 1')
        assert result == 2, f"Test 118 failed: got {result}, expected {2}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = countDigits('abcDEF_x 0')
        assert result == 1, f"Test 119 failed: got {result}, expected {1}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = countDigits('x_0 1 0 1')
        assert result == 4, f"Test 120 failed: got {result}, expected {4}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = countDigits('+00123 edge')
        assert result == 5, f"Test 121 failed: got {result}, expected {5}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = countDigits('x_enilwen 0')
        assert result == 1, f"Test 122 failed: got {result}, expected {1}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = countDigits(' 1_x edge')
        assert result == 1, f"Test 123 failed: got {result}, expected {1}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = countDigits('1 .700')
        assert result == 4, f"Test 124 failed: got {result}, expected {4}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = countDigits('!ereh')
        assert result == 0, f"Test 125 failed: got {result}, expected {0}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = countDigits('   1    0')
        assert result == 2, f"Test 126 failed: got {result}, expected {2}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = countDigits('   1   _x 1')
        assert result == 2, f"Test 127 failed: got {result}, expected {2}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = countDigits('abcDEF_x_x')
        assert result == 0, f"Test 128 failed: got {result}, expected {0}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = countDigits('7 edge')
        assert result == 1, f"Test 129 failed: got {result}, expected {1}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = countDigits('\n\t\r 1 1')
        assert result == 2, f"Test 130 failed: got {result}, expected {2}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = countDigits('\r\t\n')
        assert result == 0, f"Test 131 failed: got {result}, expected {0}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = countDigits('\n\t\r edge')
        assert result == 0, f"Test 132 failed: got {result}, expected {0}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = countDigits('carriage 1')
        assert result == 1, f"Test 133 failed: got {result}, expected {1}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = countDigits('x_x_1234567890_x')
        assert result == 10, f"Test 134 failed: got {result}, expected {10}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = countDigits('3\n2enil\n1enil')
        assert result == 3, f"Test 135 failed: got {result}, expected {3}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = countDigits('edge_x')
        assert result == 0, f"Test 136 failed: got {result}, expected {0}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = countDigits('x_egde 654cba321')
        assert result == 6, f"Test 137 failed: got {result}, expected {6}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = countDigits(')(*&^%$#@! 1 1')
        assert result == 2, f"Test 138 failed: got {result}, expected {2}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = countDigits('edge')
        assert result == 0, f"Test 139 failed: got {result}, expected {0}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = countDigits('1 ')
        assert result == 1, f"Test 140 failed: got {result}, expected {1}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = countDigits(')(*&^%$#@!_x_x')
        assert result == 0, f"Test 141 failed: got {result}, expected {0}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = countDigits('\x00\x015\x02 edge_x 1')
        assert result == 2, f"Test 142 failed: got {result}, expected {2}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = countDigits('１２３_x')
        assert result == 0, f"Test 143 failed: got {result}, expected {0}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = countDigits('３２１_x_x_x 0')
        assert result == 1, f"Test 144 failed: got {result}, expected {1}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = countDigits('no_x_x')
        assert result == 0, f"Test 145 failed: got {result}, expected {0}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = countDigits(' 1_x edge edge edge')
        assert result == 1, f"Test 146 failed: got {result}, expected {1}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = countDigits('１２３ edge')
        assert result == 0, f"Test 147 failed: got {result}, expected {0}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = countDigits('2026,_x edge 0')
        assert result == 5, f"Test 148 failed: got {result}, expected {5}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = countDigits('carriage\r9 0')
        assert result == 2, f"Test 149 failed: got {result}, expected {2}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = countDigits('3c2b1a_x 1')
        assert result == 4, f"Test 150 failed: got {result}, expected {4}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = countDigits(' 0 edge_x')
        assert result == 1, f"Test 151 failed: got {result}, expected {1}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = countDigits('0 0 x_x_x_１２３')
        assert result == 2, f"Test 152 failed: got {result}, expected {2}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = countDigits('1.0.2noisrev_x')
        assert result == 3, f"Test 153 failed: got {result}, expected {3}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = countDigits('𝟙𝟚𝟛 0_x')
        assert result == 1, f"Test 154 failed: got {result}, expected {1}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = countDigits('𝟙𝟚𝟛 1')
        assert result == 1, f"Test 155 failed: got {result}, expected {1}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = countDigits('0 x_!ereh stigid on')
        assert result == 1, f"Test 156 failed: got {result}, expected {1}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = countDigits('𝟙𝟚𝟛 edge')
        assert result == 0, f"Test 157 failed: got {result}, expected {0}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = countDigits('١٢٣_x')
        assert result == 0, f"Test 158 failed: got {result}, expected {0}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = countDigits('abcDEF_x')
        assert result == 0, f"Test 159 failed: got {result}, expected {0}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = countDigits('x_abcDEF_x')
        assert result == 0, f"Test 160 failed: got {result}, expected {0}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = countDigits('0xFF_x')
        assert result == 1, f"Test 161 failed: got {result}, expected {1}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = countDigits('line2')
        assert result == 1, f"Test 162 failed: got {result}, expected {1}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = countDigits('room_x_x')
        assert result == 0, f"Test 163 failed: got {result}, expected {0}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = countDigits(' 0_x')
        assert result == 1, f"Test 164 failed: got {result}, expected {1}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = countDigits('1 x_   1   ')
        assert result == 2, f"Test 165 failed: got {result}, expected {2}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = countDigits('here!')
        assert result == 0, f"Test 166 failed: got {result}, expected {0}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = countDigits('🙂2🙃3 1 0')
        assert result == 4, f"Test 167 failed: got {result}, expected {4}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = countDigits('-123.45 edge')
        assert result == 5, f"Test 168 failed: got {result}, expected {5}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = countDigits(' 1_x_x_x_x')
        assert result == 1, f"Test 169 failed: got {result}, expected {1}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = countDigits('654cba321')
        assert result == 6, f"Test 170 failed: got {result}, expected {6}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = countDigits('7')
        assert result == 1, f"Test 171 failed: got {result}, expected {1}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = countDigits('egde -123.45 edge_x')
        assert result == 5, f"Test 172 failed: got {result}, expected {5}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = countDigits('+00123 0')
        assert result == 6, f"Test 173 failed: got {result}, expected {6}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = countDigits('x_x_x_１２３')
        assert result == 0, f"Test 174 failed: got {result}, expected {0}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = countDigits('0 +00123')
        assert result == 6, f"Test 175 failed: got {result}, expected {6}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = countDigits('\x00\x015\x02 edge_x 1_x edge_x')
        assert result == 2, f"Test 176 failed: got {result}, expected {2}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = countDigits('１２３_x_x 0_x')
        assert result == 1, f"Test 177 failed: got {result}, expected {1}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = countDigits('0 32100+')
        assert result == 6, f"Test 178 failed: got {result}, expected {6}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = countDigits('abcDEF_x 0 edge_x')
        assert result == 1, f"Test 179 failed: got {result}, expected {1}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = countDigits('0 x_FEDcba')
        assert result == 1, f"Test 180 failed: got {result}, expected {1}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = countDigits('end 0_x edge')
        assert result == 1, f"Test 181 failed: got {result}, expected {1}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = countDigits('32100+')
        assert result == 5, f"Test 182 failed: got {result}, expected {5}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = countDigits('line1')
        assert result == 1, f"Test 183 failed: got {result}, expected {1}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = countDigits('1.0.2noisrev 0_x edge')
        assert result == 4, f"Test 184 failed: got {result}, expected {4}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = countDigits('FFx0 0')
        assert result == 2, f"Test 185 failed: got {result}, expected {2}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = countDigits('\n\t\r_x')
        assert result == 0, f"Test 186 failed: got {result}, expected {0}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = countDigits('Room 101 0')
        assert result == 4, f"Test 187 failed: got {result}, expected {4}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = countDigits('00000_x edge')
        assert result == 5, f"Test 188 failed: got {result}, expected {5}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = countDigits('1234567890 1_x')
        assert result == 11, f"Test 189 failed: got {result}, expected {11}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = countDigits('x_FFx0')
        assert result == 1, f"Test 190 failed: got {result}, expected {1}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = countDigits('𝟙𝟚𝟛 1 edge_x')
        assert result == 1, f"Test 191 failed: got {result}, expected {1}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = countDigits('x_٩lives_x_x')
        assert result == 0, f"Test 192 failed: got {result}, expected {0}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = countDigits('sevil٩_x')
        assert result == 0, f"Test 193 failed: got {result}, expected {0}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = countDigits('sevil٩ edge')
        assert result == 0, f"Test 194 failed: got {result}, expected {0}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = countDigits(' 1_x edge_x_x_x')
        assert result == 1, f"Test 195 failed: got {result}, expected {1}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = countDigits('sevil٩')
        assert result == 0, f"Test 196 failed: got {result}, expected {0}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = countDigits('1enil 0')
        assert result == 2, f"Test 197 failed: got {result}, expected {2}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = countDigits('０1２3_x')
        assert result == 2, f"Test 198 failed: got {result}, expected {2}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = countDigits('is')
        assert result == 0, f"Test 199 failed: got {result}, expected {0}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = countDigits('egairrac')
        assert result == 0, f"Test 200 failed: got {result}, expected {0}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = countDigits(',24')
        assert result == 2, f"Test 201 failed: got {result}, expected {2}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = countDigits('🙂2🙃3_x_x')
        assert result == 2, f"Test 202 failed: got {result}, expected {2}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = countDigits('🙂2🙃3_x')
        assert result == 2, f"Test 203 failed: got {result}, expected {2}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = countDigits('egde _x')
        assert result == 0, f"Test 204 failed: got {result}, expected {0}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = countDigits('𝟙𝟚𝟛 0_x 0')
        assert result == 2, f"Test 205 failed: got {result}, expected {2}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = countDigits('x_3🙃2🙂 0')
        assert result == 3, f"Test 206 failed: got {result}, expected {3}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = countDigits('²³45 1 1 0')
        assert result == 5, f"Test 207 failed: got {result}, expected {5}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = countDigits('²³45_x_x')
        assert result == 2, f"Test 208 failed: got {result}, expected {2}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = countDigits(' 0 1')
        assert result == 2, f"Test 209 failed: got {result}, expected {2}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = countDigits(' edge 0')
        assert result == 1, f"Test 210 failed: got {result}, expected {1}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = countDigits('FFx0_x 0')
        assert result == 2, f"Test 211 failed: got {result}, expected {2}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = countDigits('01e1')
        assert result == 3, f"Test 212 failed: got {result}, expected {3}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = countDigits('FFx0_x')
        assert result == 1, f"Test 213 failed: got {result}, expected {1}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = countDigits('\x00\x015\x02 edge_x 1_x')
        assert result == 2, f"Test 214 failed: got {result}, expected {2}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = countDigits('1e10_x_x')
        assert result == 3, f"Test 215 failed: got {result}, expected {3}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = countDigits('1e10_x_x_x_x')
        assert result == 3, f"Test 216 failed: got {result}, expected {3}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = countDigits('NaN edge')
        assert result == 0, f"Test 217 failed: got {result}, expected {0}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = countDigits('version2.0.1_x')
        assert result == 3, f"Test 218 failed: got {result}, expected {3}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = countDigits('x_egde egde NaN')
        assert result == 0, f"Test 219 failed: got {result}, expected {0}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = countDigits('x_x_x_x_1  1')
        assert result == 2, f"Test 220 failed: got {result}, expected {2}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = countDigits('FFx0_x 0_x')
        assert result == 2, f"Test 221 failed: got {result}, expected {2}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = countDigits('x_٩lives_x_x edge')
        assert result == 0, f"Test 222 failed: got {result}, expected {0}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = countDigits('carriage\r9 0 edge edge')
        assert result == 2, f"Test 223 failed: got {result}, expected {2}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = countDigits('NaN_x')
        assert result == 0, f"Test 224 failed: got {result}, expected {0}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = countDigits('9_x_x')
        assert result == 1, f"Test 225 failed: got {result}, expected {1}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = countDigits('x_0 𝟛𝟚𝟙')
        assert result == 1, f"Test 226 failed: got {result}, expected {1}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = countDigits('0_x')
        assert result == 1, f"Test 227 failed: got {result}, expected {1}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = countDigits('x_egde !ereh stigid on')
        assert result == 0, f"Test 228 failed: got {result}, expected {0}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = countDigits('0 egde 999999999999999999999999999999')
        assert result == 31, f"Test 229 failed: got {result}, expected {31}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = countDigits('on')
        assert result == 0, f"Test 230 failed: got {result}, expected {0}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = countDigits('x_egde')
        assert result == 0, f"Test 231 failed: got {result}, expected {0}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = countDigits('egde line1\nline2\n3 0')
        assert result == 4, f"Test 232 failed: got {result}, expected {4}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = countDigits('?0!987ZYX321cba 1')
        assert result == 8, f"Test 233 failed: got {result}, expected {8}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = countDigits('egde ?0!987ZYX321cba_x')
        assert result == 7, f"Test 234 failed: got {result}, expected {7}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = countDigits('０1２3_x_x')
        assert result == 2, f"Test 235 failed: got {result}, expected {2}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = countDigits('abc123XYZ789!0?_x')
        assert result == 7, f"Test 236 failed: got {result}, expected {7}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = countDigits('0 abc123XYZ789!0? 1')
        assert result == 9, f"Test 237 failed: got {result}, expected {9}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = countDigits('?0!987ZYX321cba')
        assert result == 7, f"Test 238 failed: got {result}, expected {7}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = countDigits('x_\x00\x015\x02')
        assert result == 1, f"Test 239 failed: got {result}, expected {1}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = countDigits('\x025\x01\x00')
        assert result == 1, f"Test 240 failed: got {result}, expected {1}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = countDigits('x_\x025\x01\x00_x')
        assert result == 1, f"Test 241 failed: got {result}, expected {1}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = countDigits('\x00\x015\x02 1_x_x_x')
        assert result == 2, f"Test 242 failed: got {result}, expected {2}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = countDigits('0 1')
        assert result == 2, f"Test 243 failed: got {result}, expected {2}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = countDigits('*d\\+d\\ 1')
        assert result == 1, f"Test 244 failed: got {result}, expected {1}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = countDigits('🙂2🙃3 1 0 0')
        assert result == 5, f"Test 245 failed: got {result}, expected {5}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = countDigits('\\d+\\d*_x_x')
        assert result == 0, f"Test 246 failed: got {result}, expected {0}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = countDigits('\\d+\\d* 1')
        assert result == 1, f"Test 247 failed: got {result}, expected {1}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = countDigits('x_*d\\+d\\')
        assert result == 0, f"Test 248 failed: got {result}, expected {0}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = countDigits('\\d+\\d* edge')
        assert result == 0, f"Test 249 failed: got {result}, expected {0}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = countDigits('\\d+\\d*_x')
        assert result == 0, f"Test 250 failed: got {result}, expected {0}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = countDigits(' 1 0')
        assert result == 2, f"Test 251 failed: got {result}, expected {2}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = countDigits('"321" edge_x')
        assert result == 3, f"Test 252 failed: got {result}, expected {3}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = countDigits('x_1 ?0!987ZYX321cba 0_x')
        assert result == 9, f"Test 253 failed: got {result}, expected {9}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = countDigits('0 1 x_"321"')
        assert result == 5, f"Test 254 failed: got {result}, expected {5}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = countDigits('0 egde "321"')
        assert result == 4, f"Test 255 failed: got {result}, expected {4}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = countDigits('"123"_x edge_x_x')
        assert result == 3, f"Test 256 failed: got {result}, expected {3}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = countDigits('tab\t7\tend 1')
        assert result == 2, f"Test 257 failed: got {result}, expected {2}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = countDigits('0 9')
        assert result == 2, f"Test 258 failed: got {result}, expected {2}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = countDigits('x_dne\t7\tbat 1_x')
        assert result == 2, f"Test 259 failed: got {result}, expected {2}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = countDigits('tab\t7\tend 0')
        assert result == 2, f"Test 260 failed: got {result}, expected {2}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = countDigits('tab\t7\tend edge 1')
        assert result == 2, f"Test 261 failed: got {result}, expected {2}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = countDigits('year')
        assert result == 0, f"Test 262 failed: got {result}, expected {0}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = countDigits('x_٩lives_x_x_x')
        assert result == 0, f"Test 263 failed: got {result}, expected {0}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = countDigits('x_3🙃2🙂')
        assert result == 2, f"Test 264 failed: got {result}, expected {2}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = countDigits('🙂2🙃3 1_x_x_x')
        assert result == 3, f"Test 265 failed: got {result}, expected {3}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = countDigits('_x 1')
        assert result == 1, f"Test 266 failed: got {result}, expected {1}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = countDigits('x_\n8\nenilwen')
        assert result == 1, f"Test 267 failed: got {result}, expected {1}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = countDigits('newline\n8\n 1')
        assert result == 2, f"Test 268 failed: got {result}, expected {2}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = countDigits('newline\n8\n edge')
        assert result == 1, f"Test 269 failed: got {result}, expected {1}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = countDigits('x_x_x_x_1 1_x')
        assert result == 2, f"Test 270 failed: got {result}, expected {2}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = countDigits('x_x_x_x_1')
        assert result == 1, f"Test 271 failed: got {result}, expected {1}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = countDigits('01e1_x')
        assert result == 3, f"Test 272 failed: got {result}, expected {3}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = countDigits('1 9')
        assert result == 2, f"Test 273 failed: got {result}, expected {2}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = countDigits('carriage')
        assert result == 0, f"Test 274 failed: got {result}, expected {0}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = countDigits(' edge 1')
        assert result == 1, f"Test 275 failed: got {result}, expected {1}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = countDigits('x_x_on 0')
        assert result == 1, f"Test 276 failed: got {result}, expected {1}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = countDigits('9\regairrac')
        assert result == 1, f"Test 277 failed: got {result}, expected {1}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = countDigits('carriage\r9 edge')
        assert result == 1, f"Test 278 failed: got {result}, expected {1}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = countDigits('carriage\r9_x')
        assert result == 1, f"Test 279 failed: got {result}, expected {1}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = countDigits('mix٠1٢2३3४4 1')
        assert result == 5, f"Test 280 failed: got {result}, expected {5}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = countDigits('mix٠1٢2३3४4_x')
        assert result == 4, f"Test 281 failed: got {result}, expected {4}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = countDigits('1 abc123XYZ789!0? edge')
        assert result == 8, f"Test 282 failed: got {result}, expected {8}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = countDigits('stigid_x_x')
        assert result == 0, f"Test 283 failed: got {result}, expected {0}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = countDigits('1 x_   1   _x')
        assert result == 2, f"Test 284 failed: got {result}, expected {2}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = countDigits('0 x_x_x_１２３')
        assert result == 1, f"Test 285 failed: got {result}, expected {1}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = countDigits('x_1.0.2noisrev')
        assert result == 3, f"Test 286 failed: got {result}, expected {3}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = countDigits('𝟙𝟚𝟛 0_x 0_x_x')
        assert result == 2, f"Test 287 failed: got {result}, expected {2}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = countDigits('Room 101 0_x')
        assert result == 4, f"Test 288 failed: got {result}, expected {4}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = countDigits('mix٠1٢2३3४4_x_x 0')
        assert result == 5, f"Test 289 failed: got {result}, expected {5}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = countDigits('2enil')
        assert result == 1, f"Test 290 failed: got {result}, expected {1}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = countDigits('✨🚀')
        assert result == 0, f"Test 291 failed: got {result}, expected {0}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = countDigits('1 🚀✨_x')
        assert result == 1, f"Test 292 failed: got {result}, expected {1}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = countDigits('0 _x')
        assert result == 1, f"Test 293 failed: got {result}, expected {1}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = countDigits('x_cba')
        assert result == 0, f"Test 294 failed: got {result}, expected {0}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = countDigits('0 _x_x')
        assert result == 1, f"Test 295 failed: got {result}, expected {1}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = countDigits('egde -123.45 edge_x 0_x')
        assert result == 6, f"Test 296 failed: got {result}, expected {6}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = countDigits('!ereh_x')
        assert result == 0, f"Test 297 failed: got {result}, expected {0}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = countDigits('.700 edoc ,24 moor ,6202 si raey ehT')
        assert result == 9, f"Test 298 failed: got {result}, expected {9}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = countDigits('x_1 ')
        assert result == 1, f"Test 299 failed: got {result}, expected {1}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = countDigits('  0')
        assert result == 1, f"Test 300 failed: got {result}, expected {1}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = countDigits(' _x')
        assert result == 0, f"Test 301 failed: got {result}, expected {0}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = countDigits('1 x_   1   _x_x')
        assert result == 2, f"Test 302 failed: got {result}, expected {2}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = countDigits('0  ')
        assert result == 1, f"Test 303 failed: got {result}, expected {1}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = countDigits('1_x_x 0')
        assert result == 2, f"Test 304 failed: got {result}, expected {2}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
