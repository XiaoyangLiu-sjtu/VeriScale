# Coverage Report

Total executable lines: 5
Covered lines: 5
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def findFirstRepeatedChar(str1):
2: ✓   for index,c in enumerate(str1):
3: ✓     if str1[:index+1].count(c) > 1:
4: ✓       return c 
5: ✓   return "None"
```

## Complete Test File

```python
def findFirstRepeatedChar(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c 
  return "None"

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = findFirstRepeatedChar('abca')
        assert result == 'a', f"Test 1 failed: got {result}, expected {'a'}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = findFirstRepeatedChar('abcdef')
        assert result == None, f"Test 2 failed: got {result}, expected {None}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = findFirstRepeatedChar('aabbcc')
        assert result == 'a', f"Test 3 failed: got {result}, expected {'a'}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = findFirstRepeatedChar('')
        assert result == None, f"Test 4 failed: got {result}, expected {None}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = findFirstRepeatedChar('abbc')
        assert result == 'b', f"Test 5 failed: got {result}, expected {'b'}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = findFirstRepeatedChar('Aa')
        assert result == None, f"Test 6 failed: got {result}, expected {None}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = findFirstRepeatedChar('a')
        assert result == None, f"Test 7 failed: got {result}, expected {None}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = findFirstRepeatedChar('ab')
        assert result == None, f"Test 8 failed: got {result}, expected {None}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = findFirstRepeatedChar('abccba')
        assert result == 'c', f"Test 9 failed: got {result}, expected {'c'}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = findFirstRepeatedChar('112233')
        assert result == '1', f"Test 10 failed: got {result}, expected {'1'}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = findFirstRepeatedChar('🙂🙃😉')
        assert result == None, f"Test 11 failed: got {result}, expected {None}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = findFirstRepeatedChar('éfgé')
        assert result == 'e', f"Test 12 failed: got {result}, expected {'e'}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = findFirstRepeatedChar('abc ABC abc')
        assert result == ' ', f"Test 13 failed: got {result}, expected {' '}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = findFirstRepeatedChar('xyzXYZ')
        assert result == None, f"Test 14 failed: got {result}, expected {None}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = findFirstRepeatedChar('a1!a1!')
        assert result == 'a', f"Test 15 failed: got {result}, expected {'a'}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = findFirstRepeatedChar('qwerty')
        assert result == None, f"Test 16 failed: got {result}, expected {None}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = findFirstRepeatedChar('uniq')
        assert result == None, f"Test 17 failed: got {result}, expected {None}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = findFirstRepeatedChar('abababab')
        assert result == 'a', f"Test 18 failed: got {result}, expected {'a'}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = findFirstRepeatedChar('0')
        assert result == None, f"Test 19 failed: got {result}, expected {None}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = findFirstRepeatedChar('01')
        assert result == None, f"Test 20 failed: got {result}, expected {None}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = findFirstRepeatedChar('a\u200db\u200da')
        assert result == '\u200d', f"Test 21 failed: got {result}, expected {'\u200d'}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = findFirstRepeatedChar(' 0')
        assert result == None, f"Test 22 failed: got {result}, expected {None}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = findFirstRepeatedChar('0 ')
        assert result == None, f"Test 23 failed: got {result}, expected {None}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = findFirstRepeatedChar('1 _x')
        assert result == None, f"Test 24 failed: got {result}, expected {None}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = findFirstRepeatedChar('abcdef edge_x')
        assert result == 'e', f"Test 25 failed: got {result}, expected {'e'}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = findFirstRepeatedChar('abcdef_x')
        assert result == None, f"Test 26 failed: got {result}, expected {None}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = findFirstRepeatedChar('aabbcc_x')
        assert result == 'a', f"Test 27 failed: got {result}, expected {'a'}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = findFirstRepeatedChar('x_ 1')
        assert result == None, f"Test 28 failed: got {result}, expected {None}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = findFirstRepeatedChar('\n\t\n edge_x')
        assert result == '\n', f"Test 29 failed: got {result}, expected {'\n'}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = findFirstRepeatedChar('ccbbaa')
        assert result == 'c', f"Test 30 failed: got {result}, expected {'c'}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = findFirstRepeatedChar(' 1_x')
        assert result == None, f"Test 31 failed: got {result}, expected {None}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = findFirstRepeatedChar('egde ccbbaa')
        assert result == 'e', f"Test 32 failed: got {result}, expected {'e'}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = findFirstRepeatedChar('x_ccbbaa_x_x')
        assert result == 'c', f"Test 33 failed: got {result}, expected {'c'}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = findFirstRepeatedChar('_x')
        assert result == None, f"Test 34 failed: got {result}, expected {None}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = findFirstRepeatedChar(' 1')
        assert result == None, f"Test 35 failed: got {result}, expected {None}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = findFirstRepeatedChar('egde  1')
        assert result == 'e', f"Test 36 failed: got {result}, expected {'e'}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = findFirstRepeatedChar('x_')
        assert result == None, f"Test 37 failed: got {result}, expected {None}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = findFirstRepeatedChar(' 0 edge')
        assert result == ' ', f"Test 38 failed: got {result}, expected {' '}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = findFirstRepeatedChar('x_ccbbaa_x_x 1')
        assert result == 'c', f"Test 39 failed: got {result}, expected {'c'}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = findFirstRepeatedChar('éèêëé_x_x')
        assert result == 'é', f"Test 40 failed: got {result}, expected {'é'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = findFirstRepeatedChar('aabbcc_x edge')
        assert result == 'a', f"Test 41 failed: got {result}, expected {'a'}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = findFirstRepeatedChar('abababab_x')
        assert result == 'a', f"Test 42 failed: got {result}, expected {'a'}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = findFirstRepeatedChar('aA_x 1 edge 1')
        assert result == ' ', f"Test 43 failed: got {result}, expected {' '}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = findFirstRepeatedChar('x_a\u200db\u200da 1_x')
        assert result == '\u200d', f"Test 44 failed: got {result}, expected {'\u200d'}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = findFirstRepeatedChar('𐍈𐍉𐍈 edge')
        assert result == '𐍈', f"Test 45 failed: got {result}, expected {'𐍈'}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = findFirstRepeatedChar('Aa_x')
        assert result == None, f"Test 46 failed: got {result}, expected {None}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = findFirstRepeatedChar('aA')
        assert result == None, f"Test 47 failed: got {result}, expected {None}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = findFirstRepeatedChar('aA 0')
        assert result == None, f"Test 48 failed: got {result}, expected {None}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = findFirstRepeatedChar('a 0')
        assert result == None, f"Test 49 failed: got {result}, expected {None}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = findFirstRepeatedChar('x_0 a')
        assert result == None, f"Test 50 failed: got {result}, expected {None}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = findFirstRepeatedChar('egde x_a_x')
        assert result == 'e', f"Test 51 failed: got {result}, expected {'e'}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = findFirstRepeatedChar('aabbcc_x 0')
        assert result == 'a', f"Test 52 failed: got {result}, expected {'a'}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = findFirstRepeatedChar('x_0 a_x')
        assert result == '_', f"Test 53 failed: got {result}, expected {'_'}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = findFirstRepeatedChar('a_x')
        assert result == None, f"Test 54 failed: got {result}, expected {None}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = findFirstRepeatedChar('_x_x')
        assert result == '_', f"Test 55 failed: got {result}, expected {'_'}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = findFirstRepeatedChar('x_a_x')
        assert result == '_', f"Test 56 failed: got {result}, expected {'_'}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = findFirstRepeatedChar('fedcba edge_x_x 1')
        assert result == 'e', f"Test 57 failed: got {result}, expected {'e'}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = findFirstRepeatedChar('1 x_x_egde abcdef')
        assert result == 'x', f"Test 58 failed: got {result}, expected {'x'}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = findFirstRepeatedChar('aa edge')
        assert result == 'a', f"Test 59 failed: got {result}, expected {'a'}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = findFirstRepeatedChar('x_0')
        assert result == None, f"Test 60 failed: got {result}, expected {None}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = findFirstRepeatedChar('aA_x')
        assert result == None, f"Test 61 failed: got {result}, expected {None}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = findFirstRepeatedChar('ba 1_x')
        assert result == None, f"Test 62 failed: got {result}, expected {None}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = findFirstRepeatedChar('ab_x 0 edge')
        assert result == ' ', f"Test 63 failed: got {result}, expected {' '}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = findFirstRepeatedChar('ab_x 0 0 1')
        assert result == ' ', f"Test 64 failed: got {result}, expected {' '}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = findFirstRepeatedChar('🙂🙃😉_x')
        assert result == None, f"Test 65 failed: got {result}, expected {None}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = findFirstRepeatedChar('abccba 0')
        assert result == 'c', f"Test 66 failed: got {result}, expected {'c'}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = findFirstRepeatedChar('uniq 1 edge')
        assert result == ' ', f"Test 67 failed: got {result}, expected {' '}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = findFirstRepeatedChar('edge edge')
        assert result == 'e', f"Test 68 failed: got {result}, expected {'e'}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = findFirstRepeatedChar('egde ccbbaa 1')
        assert result == 'e', f"Test 69 failed: got {result}, expected {'e'}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = findFirstRepeatedChar('egde  0')
        assert result == 'e', f"Test 70 failed: got {result}, expected {'e'}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = findFirstRepeatedChar('abca_x 0 1')
        assert result == 'a', f"Test 71 failed: got {result}, expected {'a'}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = findFirstRepeatedChar('egde  1 edge')
        assert result == 'e', f"Test 72 failed: got {result}, expected {'e'}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = findFirstRepeatedChar('x_0 a edge')
        assert result == ' ', f"Test 73 failed: got {result}, expected {' '}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = findFirstRepeatedChar('1 ab edge')
        assert result == ' ', f"Test 74 failed: got {result}, expected {' '}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = findFirstRepeatedChar('abcdea_x_x 1')
        assert result == 'a', f"Test 75 failed: got {result}, expected {'a'}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = findFirstRepeatedChar('edge edge_x 1')
        assert result == 'e', f"Test 76 failed: got {result}, expected {'e'}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = findFirstRepeatedChar('abccba_x')
        assert result == 'c', f"Test 77 failed: got {result}, expected {'c'}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = findFirstRepeatedChar('abcddefg edge edge')
        assert result == 'd', f"Test 78 failed: got {result}, expected {'d'}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = findFirstRepeatedChar('abcdea_x_x')
        assert result == 'a', f"Test 79 failed: got {result}, expected {'a'}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = findFirstRepeatedChar('abcddefg 1 1')
        assert result == 'd', f"Test 80 failed: got {result}, expected {'d'}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = findFirstRepeatedChar('abcddefg edge')
        assert result == 'd', f"Test 81 failed: got {result}, expected {'d'}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = findFirstRepeatedChar(' edge 0')
        assert result == 'e', f"Test 82 failed: got {result}, expected {'e'}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = findFirstRepeatedChar('x_1')
        assert result == None, f"Test 83 failed: got {result}, expected {None}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = findFirstRepeatedChar('x_a 0_x')
        assert result == '_', f"Test 84 failed: got {result}, expected {'_'}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = findFirstRepeatedChar('aabbcc_x edge 1_x')
        assert result == 'a', f"Test 85 failed: got {result}, expected {'a'}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = findFirstRepeatedChar('332211 1 1')
        assert result == '3', f"Test 86 failed: got {result}, expected {'3'}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = findFirstRepeatedChar('abc')
        assert result == None, f"Test 87 failed: got {result}, expected {None}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = findFirstRepeatedChar('1 ')
        assert result == None, f"Test 88 failed: got {result}, expected {None}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = findFirstRepeatedChar('332211_x_x')
        assert result == '3', f"Test 89 failed: got {result}, expected {'3'}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = findFirstRepeatedChar('x_a_x_x_x')
        assert result == '_', f"Test 90 failed: got {result}, expected {'_'}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = findFirstRepeatedChar('413121_x_x_x 0')
        assert result == '1', f"Test 91 failed: got {result}, expected {'1'}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = findFirstRepeatedChar('abca_x_x')
        assert result == 'a', f"Test 92 failed: got {result}, expected {'a'}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = findFirstRepeatedChar('x_a\u200db\u200da 1_x edge edge')
        assert result == '\u200d', f"Test 93 failed: got {result}, expected {'\u200d'}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = findFirstRepeatedChar('121314 edge')
        assert result == '1', f"Test 94 failed: got {result}, expected {'1'}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = findFirstRepeatedChar('abcdea_x edge')
        assert result == 'a', f"Test 95 failed: got {result}, expected {'a'}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = findFirstRepeatedChar('_x 1')
        assert result == None, f"Test 96 failed: got {result}, expected {None}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = findFirstRepeatedChar('Aa_x 0')
        assert result == None, f"Test 97 failed: got {result}, expected {None}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = findFirstRepeatedChar('abca_x_x 1')
        assert result == 'a', f"Test 98 failed: got {result}, expected {'a'}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = findFirstRepeatedChar('x_𐍈𐍉𐍈_x')
        assert result == '𐍈', f"Test 99 failed: got {result}, expected {'𐍈'}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = findFirstRepeatedChar('0 abccba')
        assert result == 'c', f"Test 100 failed: got {result}, expected {'c'}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = findFirstRepeatedChar('́egf́e_x')
        assert result == '́', f"Test 101 failed: got {result}, expected {'́'}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = findFirstRepeatedChar('🙂🙃🙂 edge')
        assert result == '🙂', f"Test 102 failed: got {result}, expected {'🙂'}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = findFirstRepeatedChar('01_x')
        assert result == None, f"Test 103 failed: got {result}, expected {None}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = findFirstRepeatedChar('1_x')
        assert result == None, f"Test 104 failed: got {result}, expected {None}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = findFirstRepeatedChar(' 0_x')
        assert result == None, f"Test 105 failed: got {result}, expected {None}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = findFirstRepeatedChar('10')
        assert result == None, f"Test 106 failed: got {result}, expected {None}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = findFirstRepeatedChar('aA 0 edge')
        assert result == ' ', f"Test 107 failed: got {result}, expected {' '}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = findFirstRepeatedChar('😉🙃🙂_x_x')
        assert result == '_', f"Test 108 failed: got {result}, expected {'_'}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = findFirstRepeatedChar('x_x_éëêèé edge_x')
        assert result == 'x', f"Test 109 failed: got {result}, expected {'x'}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = findFirstRepeatedChar('éëêèé_x_x')
        assert result == 'é', f"Test 110 failed: got {result}, expected {'é'}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = findFirstRepeatedChar('413121_x_x_x 0_x_x')
        assert result == '1', f"Test 111 failed: got {result}, expected {'1'}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = findFirstRepeatedChar('\u202efed\u202ecba edge')
        assert result == '\u202e', f"Test 112 failed: got {result}, expected {'\u202e'}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = findFirstRepeatedChar('0_x_x')
        assert result == '_', f"Test 113 failed: got {result}, expected {'_'}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = findFirstRepeatedChar('332211')
        assert result == '3', f"Test 114 failed: got {result}, expected {'3'}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = findFirstRepeatedChar('éfgé 0')
        assert result == 'e', f"Test 115 failed: got {result}, expected {'e'}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = findFirstRepeatedChar('0 éfgé')
        assert result == 'e', f"Test 116 failed: got {result}, expected {'e'}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = findFirstRepeatedChar('abcdef_x edge_x')
        assert result == 'e', f"Test 117 failed: got {result}, expected {'e'}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = findFirstRepeatedChar('faedacba_x 0_x')
        assert result == 'a', f"Test 118 failed: got {result}, expected {'a'}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = findFirstRepeatedChar('0 ́egf́e')
        assert result == '́', f"Test 119 failed: got {result}, expected {'́'}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = findFirstRepeatedChar('1')
        assert result == None, f"Test 120 failed: got {result}, expected {None}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = findFirstRepeatedChar('abcdea_x_x 1_x')
        assert result == 'a', f"Test 121 failed: got {result}, expected {'a'}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = findFirstRepeatedChar('AaA 0_x edge')
        assert result == 'A', f"Test 122 failed: got {result}, expected {'A'}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = findFirstRepeatedChar('x_x_éëêèé')
        assert result == 'x', f"Test 123 failed: got {result}, expected {'x'}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = findFirstRepeatedChar('x__x')
        assert result == '_', f"Test 124 failed: got {result}, expected {'_'}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = findFirstRepeatedChar('uniq 0')
        assert result == None, f"Test 125 failed: got {result}, expected {None}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = findFirstRepeatedChar('x_egde x_\n\t\n 0')
        assert result == 'e', f"Test 126 failed: got {result}, expected {'e'}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = findFirstRepeatedChar('🙂🙃😉_x_x')
        assert result == '_', f"Test 127 failed: got {result}, expected {'_'}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = findFirstRepeatedChar('abcdea_x edge_x edge')
        assert result == 'a', f"Test 128 failed: got {result}, expected {'a'}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = findFirstRepeatedChar('x_egde 0 x_ba')
        assert result == 'e', f"Test 129 failed: got {result}, expected {'e'}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = findFirstRepeatedChar('🙂🙃🙂 edge_x')
        assert result == '🙂', f"Test 130 failed: got {result}, expected {'🙂'}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = findFirstRepeatedChar('x_x_egde cba CBA cba_x')
        assert result == 'x', f"Test 131 failed: got {result}, expected {'x'}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = findFirstRepeatedChar('x_abc ABC abc')
        assert result == ' ', f"Test 132 failed: got {result}, expected {' '}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = findFirstRepeatedChar('x_0 egde  edge')
        assert result == 'e', f"Test 133 failed: got {result}, expected {'e'}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = findFirstRepeatedChar('egde abc\u202edef\u202e')
        assert result == 'e', f"Test 134 failed: got {result}, expected {'e'}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = findFirstRepeatedChar('x_abc ABC abc 0_x')
        assert result == ' ', f"Test 135 failed: got {result}, expected {' '}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = findFirstRepeatedChar('漢字かな漢_x_x')
        assert result == '漢', f"Test 136 failed: got {result}, expected {'漢'}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = findFirstRepeatedChar('漢字かな漢 1 1 0')
        assert result == '漢', f"Test 137 failed: got {result}, expected {'漢'}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = findFirstRepeatedChar('413121_x_x_x')
        assert result == '1', f"Test 138 failed: got {result}, expected {'1'}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = findFirstRepeatedChar('𐍈𐍉𐍈_x_x')
        assert result == '𐍈', f"Test 139 failed: got {result}, expected {'𐍈'}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = findFirstRepeatedChar('0_x')
        assert result == None, f"Test 140 failed: got {result}, expected {None}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = findFirstRepeatedChar('a1!a1!_x_x')
        assert result == 'a', f"Test 141 failed: got {result}, expected {'a'}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = findFirstRepeatedChar('a1!a1!_x_x_x_x')
        assert result == 'a', f"Test 142 failed: got {result}, expected {'a'}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = findFirstRepeatedChar('a1!a1! edge')
        assert result == 'a', f"Test 143 failed: got {result}, expected {'a'}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = findFirstRepeatedChar('!1a!1a')
        assert result == '!', f"Test 144 failed: got {result}, expected {'!'}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = findFirstRepeatedChar('01_x_x')
        assert result == '_', f"Test 145 failed: got {result}, expected {'_'}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = findFirstRepeatedChar('x_egde egde a1!a1!')
        assert result == 'e', f"Test 146 failed: got {result}, expected {'e'}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = findFirstRepeatedChar('ABC_x')
        assert result == None, f"Test 147 failed: got {result}, expected {None}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = findFirstRepeatedChar('egde x_x_0')
        assert result == 'e', f"Test 148 failed: got {result}, expected {'e'}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = findFirstRepeatedChar('ABC')
        assert result == None, f"Test 149 failed: got {result}, expected {None}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = findFirstRepeatedChar('qinu edge 0')
        assert result == 'e', f"Test 150 failed: got {result}, expected {'e'}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = findFirstRepeatedChar('1 ccbbaa edge')
        assert result == 'c', f"Test 151 failed: got {result}, expected {'c'}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = findFirstRepeatedChar('x_egde égfédcba')
        assert result == 'e', f"Test 152 failed: got {result}, expected {'e'}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = findFirstRepeatedChar('qwerty_x')
        assert result == None, f"Test 153 failed: got {result}, expected {None}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = findFirstRepeatedChar('x_x_éëêèé 1')
        assert result == 'x', f"Test 154 failed: got {result}, expected {'x'}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = findFirstRepeatedChar('egde 0 ')
        assert result == 'e', f"Test 155 failed: got {result}, expected {'e'}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = findFirstRepeatedChar('qwerty 1_x')
        assert result == None, f"Test 156 failed: got {result}, expected {None}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = findFirstRepeatedChar('ytrewq')
        assert result == None, f"Test 157 failed: got {result}, expected {None}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = findFirstRepeatedChar('x_qwerty')
        assert result == None, f"Test 158 failed: got {result}, expected {None}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = findFirstRepeatedChar('qinu')
        assert result == None, f"Test 159 failed: got {result}, expected {None}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = findFirstRepeatedChar('x_qinu_x')
        assert result == '_', f"Test 160 failed: got {result}, expected {'_'}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = findFirstRepeatedChar('uniq 1_x_x_x')
        assert result == '_', f"Test 161 failed: got {result}, expected {'_'}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = findFirstRepeatedChar('egde x_egde x_aedcba')
        assert result == 'e', f"Test 162 failed: got {result}, expected {'e'}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = findFirstRepeatedChar('abcdef_x edge_x_x')
        assert result == 'e', f"Test 163 failed: got {result}, expected {'e'}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = findFirstRepeatedChar('egde x_egde x_aedcba 1')
        assert result == 'e', f"Test 164 failed: got {result}, expected {'e'}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = findFirstRepeatedChar('babababa 1')
        assert result == 'b', f"Test 165 failed: got {result}, expected {'b'}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = findFirstRepeatedChar('aA 0 0_x')
        assert result == ' ', f"Test 166 failed: got {result}, expected {' '}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = findFirstRepeatedChar('abababab_x_x')
        assert result == 'a', f"Test 167 failed: got {result}, expected {'a'}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = findFirstRepeatedChar('abababab 1')
        assert result == 'a', f"Test 168 failed: got {result}, expected {'a'}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = findFirstRepeatedChar('x_babababa')
        assert result == 'b', f"Test 169 failed: got {result}, expected {'b'}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = findFirstRepeatedChar('abababab edge')
        assert result == 'a', f"Test 170 failed: got {result}, expected {'a'}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = findFirstRepeatedChar('x_a 0')
        assert result == None, f"Test 171 failed: got {result}, expected {None}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = findFirstRepeatedChar('babababa edge_x')
        assert result == 'b', f"Test 172 failed: got {result}, expected {'b'}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = findFirstRepeatedChar('0 1 x_0')
        assert result == ' ', f"Test 173 failed: got {result}, expected {' '}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = findFirstRepeatedChar('0 egde 0')
        assert result == 'e', f"Test 174 failed: got {result}, expected {'e'}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = findFirstRepeatedChar('0_x edge_x_x')
        assert result == 'e', f"Test 175 failed: got {result}, expected {'e'}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = findFirstRepeatedChar('0 1')
        assert result == None, f"Test 176 failed: got {result}, expected {None}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = findFirstRepeatedChar('x_10 1_x')
        assert result == '1', f"Test 177 failed: got {result}, expected {'1'}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = findFirstRepeatedChar('́egf́e')
        assert result == '́', f"Test 178 failed: got {result}, expected {'́'}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = findFirstRepeatedChar('01 edge 1')
        assert result == 'e', f"Test 179 failed: got {result}, expected {'e'}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = findFirstRepeatedChar('x_égfédcba_x')
        assert result == 'é', f"Test 180 failed: got {result}, expected {'é'}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = findFirstRepeatedChar('ab_x 0 edge_x_x')
        assert result == ' ', f"Test 181 failed: got {result}, expected {' '}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = findFirstRepeatedChar('010 1')
        assert result == '0', f"Test 182 failed: got {result}, expected {'0'}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = findFirstRepeatedChar('010 edge')
        assert result == '0', f"Test 183 failed: got {result}, expected {'0'}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = findFirstRepeatedChar('x_x_0')
        assert result == 'x', f"Test 184 failed: got {result}, expected {'x'}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = findFirstRepeatedChar('AaA 0_x_x')
        assert result == 'A', f"Test 185 failed: got {result}, expected {'A'}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = findFirstRepeatedChar('1 1 x_x_egde abcdef')
        assert result == '1', f"Test 186 failed: got {result}, expected {'1'}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = findFirstRepeatedChar(' edge 1')
        assert result == 'e', f"Test 187 failed: got {result}, expected {'e'}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = findFirstRepeatedChar('a1!a1! 0')
        assert result == 'a', f"Test 188 failed: got {result}, expected {'a'}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = findFirstRepeatedChar('𝔞𝔟𝔠𝔞 edge')
        assert result == '𝔞', f"Test 189 failed: got {result}, expected {'𝔞'}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = findFirstRepeatedChar('x_10')
        assert result == None, f"Test 190 failed: got {result}, expected {None}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = findFirstRepeatedChar('egde x_1 aA 0')
        assert result == 'e', f"Test 191 failed: got {result}, expected {'e'}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = findFirstRepeatedChar('ab_x')
        assert result == None, f"Test 192 failed: got {result}, expected {None}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = findFirstRepeatedChar('0  edge')
        assert result == ' ', f"Test 193 failed: got {result}, expected {' '}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = findFirstRepeatedChar('\x00a\x00_x_x 0')
        assert result == '\x00', f"Test 194 failed: got {result}, expected {'\x00'}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = findFirstRepeatedChar('\x00a\x00_x_x')
        assert result == '\x00', f"Test 195 failed: got {result}, expected {'\x00'}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = findFirstRepeatedChar('1 a\u200db\u200da_x')
        assert result == '\u200d', f"Test 196 failed: got {result}, expected {'\u200d'}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = findFirstRepeatedChar('0 _x')
        assert result == None, f"Test 197 failed: got {result}, expected {None}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = findFirstRepeatedChar('ABC_x_x')
        assert result == '_', f"Test 198 failed: got {result}, expected {'_'}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = findFirstRepeatedChar('x_x_egde')
        assert result == 'x', f"Test 199 failed: got {result}, expected {'x'}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = findFirstRepeatedChar('a\u200db\u200da 0')
        assert result == '\u200d', f"Test 200 failed: got {result}, expected {'\u200d'}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = findFirstRepeatedChar('AaA_x_x')
        assert result == 'A', f"Test 201 failed: got {result}, expected {'A'}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = findFirstRepeatedChar('x_1 ')
        assert result == None, f"Test 202 failed: got {result}, expected {None}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = findFirstRepeatedChar('abccba 0_x')
        assert result == 'c', f"Test 203 failed: got {result}, expected {'c'}"
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
