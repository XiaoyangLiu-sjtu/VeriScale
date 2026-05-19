# Coverage Report

Total executable lines: 3
Covered lines: 3
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def palindromeIgnoreNonAlnum(s):
2: ✓     cleaned = ''.join(c.lower() for c in s if c.isalnum())
3: ✓     return cleaned == cleaned[::-1]
```

## Complete Test File

```python
def palindromeIgnoreNonAlnum(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = palindromeIgnoreNonAlnum('')
        assert result == True, f"Test 1 failed: got {result}, expected {True}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = palindromeIgnoreNonAlnum('A man, a plan, a canal: Panama')
        assert result == True, f"Test 2 failed: got {result}, expected {True}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = palindromeIgnoreNonAlnum('race a car')
        assert result == False, f"Test 3 failed: got {result}, expected {False}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = palindromeIgnoreNonAlnum("No 'x' in Nixon")
        assert result == True, f"Test 4 failed: got {result}, expected {True}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = palindromeIgnoreNonAlnum('abc!!cba?')
        assert result == True, f"Test 5 failed: got {result}, expected {True}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = palindromeIgnoreNonAlnum('Hello, world!')
        assert result == False, f"Test 6 failed: got {result}, expected {False}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = palindromeIgnoreNonAlnum(' ')
        assert result == True, f"Test 7 failed: got {result}, expected {True}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = palindromeIgnoreNonAlnum('a')
        assert result == True, f"Test 8 failed: got {result}, expected {True}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = palindromeIgnoreNonAlnum('Z')
        assert result == True, f"Test 9 failed: got {result}, expected {True}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = palindromeIgnoreNonAlnum('aa')
        assert result == True, f"Test 10 failed: got {result}, expected {True}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = palindromeIgnoreNonAlnum('Aa')
        assert result == True, f"Test 11 failed: got {result}, expected {True}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = palindromeIgnoreNonAlnum('ab')
        assert result == False, f"Test 12 failed: got {result}, expected {False}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = palindromeIgnoreNonAlnum('aba')
        assert result == True, f"Test 13 failed: got {result}, expected {True}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = palindromeIgnoreNonAlnum('abba')
        assert result == True, f"Test 14 failed: got {result}, expected {True}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = palindromeIgnoreNonAlnum('abcba')
        assert result == True, f"Test 15 failed: got {result}, expected {True}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = palindromeIgnoreNonAlnum('abca')
        assert result == False, f"Test 16 failed: got {result}, expected {False}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = palindromeIgnoreNonAlnum('Was it a car or a cat I saw?')
        assert result == True, f"Test 17 failed: got {result}, expected {True}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = palindromeIgnoreNonAlnum("Madam, I'm Adam.")
        assert result == True, f"Test 18 failed: got {result}, expected {True}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = palindromeIgnoreNonAlnum('!!!')
        assert result == True, f"Test 19 failed: got {result}, expected {True}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = palindromeIgnoreNonAlnum('.,;:!?-')
        assert result == True, f"Test 20 failed: got {result}, expected {True}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = palindromeIgnoreNonAlnum('0P')
        assert result == False, f"Test 21 failed: got {result}, expected {False}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = palindromeIgnoreNonAlnum('1a2')
        assert result == False, f"Test 22 failed: got {result}, expected {False}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = palindromeIgnoreNonAlnum('12321')
        assert result == True, f"Test 23 failed: got {result}, expected {True}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = palindromeIgnoreNonAlnum('12,321')
        assert result == True, f"Test 24 failed: got {result}, expected {True}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = palindromeIgnoreNonAlnum('1 2 3 2 1')
        assert result == True, f"Test 25 failed: got {result}, expected {True}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = palindromeIgnoreNonAlnum('Able was I, ere I saw Elba')
        assert result == True, f"Test 26 failed: got {result}, expected {True}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = palindromeIgnoreNonAlnum('Never odd or even')
        assert result == True, f"Test 27 failed: got {result}, expected {True}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = palindromeIgnoreNonAlnum('Step on no pets')
        assert result == True, f"Test 28 failed: got {result}, expected {True}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = palindromeIgnoreNonAlnum('Top spot')
        assert result == True, f"Test 29 failed: got {result}, expected {True}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = palindromeIgnoreNonAlnum('A1b2B1a')
        assert result == True, f"Test 30 failed: got {result}, expected {True}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = palindromeIgnoreNonAlnum('𝔄bba𝔞')
        assert result == False, f"Test 31 failed: got {result}, expected {False}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = palindromeIgnoreNonAlnum('Åbbaå')
        assert result == False, f"Test 32 failed: got {result}, expected {False}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = palindromeIgnoreNonAlnum('Ésope reste ici et se repose')
        assert result == False, f"Test 33 failed: got {result}, expected {False}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = palindromeIgnoreNonAlnum('あいいあ')
        assert result == True, f"Test 34 failed: got {result}, expected {True}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = palindromeIgnoreNonAlnum('😀a😀')
        assert result == True, f"Test 35 failed: got {result}, expected {True}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = palindromeIgnoreNonAlnum('a😀b😀a')
        assert result == True, f"Test 36 failed: got {result}, expected {True}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = palindromeIgnoreNonAlnum('\x00')
        assert result == True, f"Test 37 failed: got {result}, expected {True}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = palindromeIgnoreNonAlnum('a\x00a')
        assert result == True, f"Test 38 failed: got {result}, expected {True}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = palindromeIgnoreNonAlnum('\nA\n')
        assert result == True, f"Test 39 failed: got {result}, expected {True}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = palindromeIgnoreNonAlnum('\t')
        assert result == True, f"Test 40 failed: got {result}, expected {True}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = palindromeIgnoreNonAlnum('abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba')
        assert result == True, f"Test 41 failed: got {result}, expected {True}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = palindromeIgnoreNonAlnum('_x')
        assert result == True, f"Test 42 failed: got {result}, expected {True}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = palindromeIgnoreNonAlnum('Madam,')
        assert result == True, f"Test 43 failed: got {result}, expected {True}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = palindromeIgnoreNonAlnum(' 0')
        assert result == True, f"Test 44 failed: got {result}, expected {True}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = palindromeIgnoreNonAlnum('0 ')
        assert result == True, f"Test 45 failed: got {result}, expected {True}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = palindromeIgnoreNonAlnum('1 _x')
        assert result == False, f"Test 46 failed: got {result}, expected {False}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = palindromeIgnoreNonAlnum('in_x')
        assert result == False, f"Test 47 failed: got {result}, expected {False}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = palindromeIgnoreNonAlnum('aba 1')
        assert result == False, f"Test 48 failed: got {result}, expected {False}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = palindromeIgnoreNonAlnum('0 aba')
        assert result == False, f"Test 49 failed: got {result}, expected {False}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = palindromeIgnoreNonAlnum('or')
        assert result == False, f"Test 50 failed: got {result}, expected {False}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = palindromeIgnoreNonAlnum('ici')
        assert result == True, f"Test 51 failed: got {result}, expected {True}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = palindromeIgnoreNonAlnum('2')
        assert result == True, f"Test 52 failed: got {result}, expected {True}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = palindromeIgnoreNonAlnum('man,')
        assert result == False, f"Test 53 failed: got {result}, expected {False}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = palindromeIgnoreNonAlnum('A man, a plan, a canal: Panama edge_x')
        assert result == False, f"Test 54 failed: got {result}, expected {False}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = palindromeIgnoreNonAlnum('A man, a plan, a canal: Panama_x')
        assert result == False, f"Test 55 failed: got {result}, expected {False}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = palindromeIgnoreNonAlnum("x_'x'")
        assert result == True, f"Test 56 failed: got {result}, expected {True}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = palindromeIgnoreNonAlnum('amanaP :lanac a ,nalp a ,nam A')
        assert result == True, f"Test 57 failed: got {result}, expected {True}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = palindromeIgnoreNonAlnum('P0')
        assert result == False, f"Test 58 failed: got {result}, expected {False}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = palindromeIgnoreNonAlnum('Never odd or even edge_x')
        assert result == False, f"Test 59 failed: got {result}, expected {False}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = palindromeIgnoreNonAlnum('0 _x')
        assert result == False, f"Test 60 failed: got {result}, expected {False}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = palindromeIgnoreNonAlnum('1 rac a ecar')
        assert result == False, f"Test 61 failed: got {result}, expected {False}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = palindromeIgnoreNonAlnum('neve ro ddo reveN')
        assert result == True, f"Test 62 failed: got {result}, expected {True}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = palindromeIgnoreNonAlnum('rac a ecar')
        assert result == False, f"Test 63 failed: got {result}, expected {False}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = palindromeIgnoreNonAlnum('spot')
        assert result == False, f"Test 64 failed: got {result}, expected {False}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = palindromeIgnoreNonAlnum(' 1_x')
        assert result == False, f"Test 65 failed: got {result}, expected {False}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = palindromeIgnoreNonAlnum('egde rac a ecar')
        assert result == False, f"Test 66 failed: got {result}, expected {False}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = palindromeIgnoreNonAlnum('x_rac a ecar_x_x')
        assert result == False, f"Test 67 failed: got {result}, expected {False}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = palindromeIgnoreNonAlnum('race a car_x')
        assert result == False, f"Test 68 failed: got {result}, expected {False}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = palindromeIgnoreNonAlnum('x_rac a ecar_x_x edge')
        assert result == False, f"Test 69 failed: got {result}, expected {False}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = palindromeIgnoreNonAlnum('world!')
        assert result == False, f"Test 70 failed: got {result}, expected {False}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = palindromeIgnoreNonAlnum('2_x')
        assert result == False, f"Test 71 failed: got {result}, expected {False}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = palindromeIgnoreNonAlnum("No 'x' in Nixon 1")
        assert result == False, f"Test 72 failed: got {result}, expected {False}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = palindromeIgnoreNonAlnum("No 'x' in Nixon edge")
        assert result == False, f"Test 73 failed: got {result}, expected {False}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = palindromeIgnoreNonAlnum("noxiN ni 'x' oN")
        assert result == True, f"Test 74 failed: got {result}, expected {True}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = palindromeIgnoreNonAlnum("egde noxiN ni 'x' oN 1")
        assert result == False, f"Test 75 failed: got {result}, expected {False}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = palindromeIgnoreNonAlnum('Was')
        assert result == False, f"Test 76 failed: got {result}, expected {False}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = palindromeIgnoreNonAlnum('_x_x')
        assert result == True, f"Test 77 failed: got {result}, expected {True}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = palindromeIgnoreNonAlnum("x_noxiN ni 'x' oN")
        assert result == False, f"Test 78 failed: got {result}, expected {False}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = palindromeIgnoreNonAlnum('on')
        assert result == False, f"Test 79 failed: got {result}, expected {False}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = palindromeIgnoreNonAlnum("x_x_noxiN ni 'x' oN")
        assert result == False, f"Test 80 failed: got {result}, expected {False}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = palindromeIgnoreNonAlnum(' 0 edge')
        assert result == False, f"Test 81 failed: got {result}, expected {False}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = palindromeIgnoreNonAlnum(' 0 1')
        assert result == False, f"Test 82 failed: got {result}, expected {False}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = palindromeIgnoreNonAlnum("1 No 'x' in Nixon")
        assert result == False, f"Test 83 failed: got {result}, expected {False}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = palindromeIgnoreNonAlnum('was')
        assert result == False, f"Test 84 failed: got {result}, expected {False}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = palindromeIgnoreNonAlnum('I')
        assert result == True, f"Test 85 failed: got {result}, expected {True}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = palindromeIgnoreNonAlnum('Was_x')
        assert result == False, f"Test 86 failed: got {result}, expected {False}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = palindromeIgnoreNonAlnum('Was_x edge')
        assert result == False, f"Test 87 failed: got {result}, expected {False}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = palindromeIgnoreNonAlnum("'x'")
        assert result == True, f"Test 88 failed: got {result}, expected {True}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = palindromeIgnoreNonAlnum('12,321_x')
        assert result == False, f"Test 89 failed: got {result}, expected {False}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = palindromeIgnoreNonAlnum('abc!!cba?_x 1 edge')
        assert result == False, f"Test 90 failed: got {result}, expected {False}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = palindromeIgnoreNonAlnum('Never')
        assert result == False, f"Test 91 failed: got {result}, expected {False}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = palindromeIgnoreNonAlnum('x_egde x_x_race a car_x 1_x')
        assert result == False, f"Test 92 failed: got {result}, expected {False}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = palindromeIgnoreNonAlnum('𝔄bba𝔞 edge')
        assert result == False, f"Test 93 failed: got {result}, expected {False}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = palindromeIgnoreNonAlnum('x_x_noxiN')
        assert result == False, f"Test 94 failed: got {result}, expected {False}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = palindromeIgnoreNonAlnum('Was 0')
        assert result == False, f"Test 95 failed: got {result}, expected {False}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = palindromeIgnoreNonAlnum('x_poT')
        assert result == False, f"Test 96 failed: got {result}, expected {False}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = palindromeIgnoreNonAlnum('egde !dlrow ,olleH 0')
        assert result == False, f"Test 97 failed: got {result}, expected {False}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = palindromeIgnoreNonAlnum('pets')
        assert result == False, f"Test 98 failed: got {result}, expected {False}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = palindromeIgnoreNonAlnum('!dlrow ,olleH')
        assert result == False, f"Test 99 failed: got {result}, expected {False}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = palindromeIgnoreNonAlnum('egde !dlrow ,olleH 0_x')
        assert result == False, f"Test 100 failed: got {result}, expected {False}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = palindromeIgnoreNonAlnum('Hello, world! 0')
        assert result == False, f"Test 101 failed: got {result}, expected {False}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = palindromeIgnoreNonAlnum('x_0  ')
        assert result == False, f"Test 102 failed: got {result}, expected {False}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = palindromeIgnoreNonAlnum('se')
        assert result == False, f"Test 103 failed: got {result}, expected {False}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = palindromeIgnoreNonAlnum('egde x_ _x')
        assert result == False, f"Test 104 failed: got {result}, expected {False}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = palindromeIgnoreNonAlnum("No 'x' in Nixon 0")
        assert result == False, f"Test 105 failed: got {result}, expected {False}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = palindromeIgnoreNonAlnum('\nA\n_x')
        assert result == False, f"Test 106 failed: got {result}, expected {False}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = palindromeIgnoreNonAlnum(' _x')
        assert result == True, f"Test 107 failed: got {result}, expected {True}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = palindromeIgnoreNonAlnum(' 1')
        assert result == True, f"Test 108 failed: got {result}, expected {True}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = palindromeIgnoreNonAlnum('  0')
        assert result == True, f"Test 109 failed: got {result}, expected {True}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = palindromeIgnoreNonAlnum('1 x_.madA')
        assert result == False, f"Test 110 failed: got {result}, expected {False}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = palindromeIgnoreNonAlnum('in')
        assert result == False, f"Test 111 failed: got {result}, expected {False}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = palindromeIgnoreNonAlnum('a edge')
        assert result == False, f"Test 112 failed: got {result}, expected {False}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = palindromeIgnoreNonAlnum('a_x')
        assert result == False, f"Test 113 failed: got {result}, expected {False}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = palindromeIgnoreNonAlnum('2_x 0')
        assert result == False, f"Test 114 failed: got {result}, expected {False}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = palindromeIgnoreNonAlnum('abca 1')
        assert result == False, f"Test 115 failed: got {result}, expected {False}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = palindromeIgnoreNonAlnum('Z 1')
        assert result == False, f"Test 116 failed: got {result}, expected {False}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = palindromeIgnoreNonAlnum('1 2 3 2 1 0')
        assert result == False, f"Test 117 failed: got {result}, expected {False}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = palindromeIgnoreNonAlnum('Z_x 0 edge')
        assert result == False, f"Test 118 failed: got {result}, expected {False}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = palindromeIgnoreNonAlnum('A man, a plan, a canal: Panama_x_x')
        assert result == False, f"Test 119 failed: got {result}, expected {False}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = palindromeIgnoreNonAlnum('_x 0 0')
        assert result == False, f"Test 120 failed: got {result}, expected {False}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = palindromeIgnoreNonAlnum('Z 0_x')
        assert result == False, f"Test 121 failed: got {result}, expected {False}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = palindromeIgnoreNonAlnum('x_amanaP')
        assert result == False, f"Test 122 failed: got {result}, expected {False}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = palindromeIgnoreNonAlnum('  0 1')
        assert result == False, f"Test 123 failed: got {result}, expected {False}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = palindromeIgnoreNonAlnum('Able')
        assert result == False, f"Test 124 failed: got {result}, expected {False}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = palindromeIgnoreNonAlnum('0_x 1 edge')
        assert result == False, f"Test 125 failed: got {result}, expected {False}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = palindromeIgnoreNonAlnum('aa 1')
        assert result == False, f"Test 126 failed: got {result}, expected {False}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = palindromeIgnoreNonAlnum('in edge')
        assert result == False, f"Test 127 failed: got {result}, expected {False}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = palindromeIgnoreNonAlnum('x_aA')
        assert result == False, f"Test 128 failed: got {result}, expected {False}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = palindromeIgnoreNonAlnum('Z_x')
        assert result == False, f"Test 129 failed: got {result}, expected {False}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = palindromeIgnoreNonAlnum('x_')
        assert result == True, f"Test 130 failed: got {result}, expected {True}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = palindromeIgnoreNonAlnum('egde ,I 1')
        assert result == False, f"Test 131 failed: got {result}, expected {False}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = palindromeIgnoreNonAlnum('Aa_x 0')
        assert result == False, f"Test 132 failed: got {result}, expected {False}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = palindromeIgnoreNonAlnum('it 1 0 1')
        assert result == False, f"Test 133 failed: got {result}, expected {False}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = palindromeIgnoreNonAlnum('amanaP')
        assert result == False, f"Test 134 failed: got {result}, expected {False}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = palindromeIgnoreNonAlnum('Panama_x')
        assert result == False, f"Test 135 failed: got {result}, expected {False}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = palindromeIgnoreNonAlnum('_x edge')
        assert result == False, f"Test 136 failed: got {result}, expected {False}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = palindromeIgnoreNonAlnum('0P 0')
        assert result == True, f"Test 137 failed: got {result}, expected {True}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = palindromeIgnoreNonAlnum('_x_x edge edge')
        assert result == False, f"Test 138 failed: got {result}, expected {False}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = palindromeIgnoreNonAlnum('ba')
        assert result == False, f"Test 139 failed: got {result}, expected {False}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = palindromeIgnoreNonAlnum('1 x_\nA\n')
        assert result == False, f"Test 140 failed: got {result}, expected {False}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = palindromeIgnoreNonAlnum('1 No')
        assert result == False, f"Test 141 failed: got {result}, expected {False}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = palindromeIgnoreNonAlnum('ab_x')
        assert result == False, f"Test 142 failed: got {result}, expected {False}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = palindromeIgnoreNonAlnum('😀a😀 0')
        assert result == False, f"Test 143 failed: got {result}, expected {False}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = palindromeIgnoreNonAlnum('_x 1')
        assert result == False, f"Test 144 failed: got {result}, expected {False}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = palindromeIgnoreNonAlnum('esoper')
        assert result == False, f"Test 145 failed: got {result}, expected {False}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = palindromeIgnoreNonAlnum(',olleH edge')
        assert result == False, f"Test 146 failed: got {result}, expected {False}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = palindromeIgnoreNonAlnum('aba 1 1')
        assert result == False, f"Test 147 failed: got {result}, expected {False}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = palindromeIgnoreNonAlnum('aba edge')
        assert result == False, f"Test 148 failed: got {result}, expected {False}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = palindromeIgnoreNonAlnum(' edge')
        assert result == False, f"Test 149 failed: got {result}, expected {False}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = palindromeIgnoreNonAlnum('no')
        assert result == False, f"Test 150 failed: got {result}, expected {False}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = palindromeIgnoreNonAlnum('rac a ecar 1')
        assert result == False, f"Test 151 failed: got {result}, expected {False}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = palindromeIgnoreNonAlnum('ablE')
        assert result == False, f"Test 152 failed: got {result}, expected {False}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = palindromeIgnoreNonAlnum('1')
        assert result == True, f"Test 153 failed: got {result}, expected {True}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = palindromeIgnoreNonAlnum('canal:')
        assert result == False, f"Test 154 failed: got {result}, expected {False}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = palindromeIgnoreNonAlnum('Aa_x_x_x')
        assert result == False, f"Test 155 failed: got {result}, expected {False}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = palindromeIgnoreNonAlnum('race')
        assert result == False, f"Test 156 failed: got {result}, expected {False}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = palindromeIgnoreNonAlnum('abba edge')
        assert result == False, f"Test 157 failed: got {result}, expected {False}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = palindromeIgnoreNonAlnum('abba 0')
        assert result == False, f"Test 158 failed: got {result}, expected {False}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = palindromeIgnoreNonAlnum('x_ti')
        assert result == False, f"Test 159 failed: got {result}, expected {False}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = palindromeIgnoreNonAlnum('abcba edge_x')
        assert result == False, f"Test 160 failed: got {result}, expected {False}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = palindromeIgnoreNonAlnum(',I')
        assert result == True, f"Test 161 failed: got {result}, expected {True}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = palindromeIgnoreNonAlnum('abcba 1 1')
        assert result == False, f"Test 162 failed: got {result}, expected {False}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = palindromeIgnoreNonAlnum('abcba 1 0')
        assert result == False, f"Test 163 failed: got {result}, expected {False}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = palindromeIgnoreNonAlnum('aA')
        assert result == True, f"Test 164 failed: got {result}, expected {True}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = palindromeIgnoreNonAlnum('2_x_x')
        assert result == False, f"Test 165 failed: got {result}, expected {False}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = palindromeIgnoreNonAlnum('åabbÅ')
        assert result == False, f"Test 166 failed: got {result}, expected {False}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = palindromeIgnoreNonAlnum('abcba_x_x')
        assert result == False, f"Test 167 failed: got {result}, expected {False}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = palindromeIgnoreNonAlnum("x_'x'_x 1")
        assert result == False, f"Test 168 failed: got {result}, expected {False}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = palindromeIgnoreNonAlnum('abcba_x')
        assert result == False, f"Test 169 failed: got {result}, expected {False}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = palindromeIgnoreNonAlnum('ere')
        assert result == True, f"Test 170 failed: got {result}, expected {True}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = palindromeIgnoreNonAlnum('acba_x_x_x 0')
        assert result == False, f"Test 171 failed: got {result}, expected {False}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = palindromeIgnoreNonAlnum("x_'x'_x")
        assert result == True, f"Test 172 failed: got {result}, expected {True}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = palindromeIgnoreNonAlnum('Hello, world! edge edge')
        assert result == False, f"Test 173 failed: got {result}, expected {False}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = palindromeIgnoreNonAlnum('abca edge')
        assert result == False, f"Test 174 failed: got {result}, expected {False}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = palindromeIgnoreNonAlnum('_x_x edge edge edge 0')
        assert result == False, f"Test 175 failed: got {result}, expected {False}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = palindromeIgnoreNonAlnum('x_?abc!!cba_x')
        assert result == True, f"Test 176 failed: got {result}, expected {True}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = palindromeIgnoreNonAlnum('?was I tac a ro rac a ti saW_x')
        assert result == False, f"Test 177 failed: got {result}, expected {False}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = palindromeIgnoreNonAlnum('abcba 1')
        assert result == False, f"Test 178 failed: got {result}, expected {False}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = palindromeIgnoreNonAlnum('a\x00a_x')
        assert result == False, f"Test 179 failed: got {result}, expected {False}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = palindromeIgnoreNonAlnum('ecar_x_x_x')
        assert result == False, f"Test 180 failed: got {result}, expected {False}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = palindromeIgnoreNonAlnum("Madam, I'm Adam._x 0_x 1")
        assert result == False, f"Test 181 failed: got {result}, expected {False}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = palindromeIgnoreNonAlnum("Madam, I'm Adam. edge")
        assert result == False, f"Test 182 failed: got {result}, expected {False}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = palindromeIgnoreNonAlnum(' 1_x_x')
        assert result == False, f"Test 183 failed: got {result}, expected {False}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = palindromeIgnoreNonAlnum('x_x_Z')
        assert result == False, f"Test 184 failed: got {result}, expected {False}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = palindromeIgnoreNonAlnum(".madA m'I ,madaM")
        assert result == True, f"Test 185 failed: got {result}, expected {True}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = palindromeIgnoreNonAlnum("m'I")
        assert result == False, f"Test 186 failed: got {result}, expected {False}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = palindromeIgnoreNonAlnum('12321_x')
        assert result == False, f"Test 187 failed: got {result}, expected {False}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = palindromeIgnoreNonAlnum('I edge')
        assert result == False, f"Test 188 failed: got {result}, expected {False}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = palindromeIgnoreNonAlnum(' 0_x')
        assert result == False, f"Test 189 failed: got {result}, expected {False}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = palindromeIgnoreNonAlnum('x_1 ')
        assert result == False, f"Test 190 failed: got {result}, expected {False}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = palindromeIgnoreNonAlnum('1_x')
        assert result == False, f"Test 191 failed: got {result}, expected {False}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = palindromeIgnoreNonAlnum('it 1 0 1 edge')
        assert result == False, f"Test 192 failed: got {result}, expected {False}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = palindromeIgnoreNonAlnum('!!!_x')
        assert result == True, f"Test 193 failed: got {result}, expected {True}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = palindromeIgnoreNonAlnum('ni')
        assert result == False, f"Test 194 failed: got {result}, expected {False}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = palindromeIgnoreNonAlnum('.,;:!?-_x')
        assert result == True, f"Test 195 failed: got {result}, expected {True}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = palindromeIgnoreNonAlnum('Top spot edge')
        assert result == False, f"Test 196 failed: got {result}, expected {False}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = palindromeIgnoreNonAlnum('𝔄bba𝔞 edge_x 0')
        assert result == False, f"Test 197 failed: got {result}, expected {False}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = palindromeIgnoreNonAlnum('.,;:!?- 0')
        assert result == True, f"Test 198 failed: got {result}, expected {True}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = palindromeIgnoreNonAlnum('-?!:;,._x_x')
        assert result == True, f"Test 199 failed: got {result}, expected {True}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = palindromeIgnoreNonAlnum('I_x_x')
        assert result == False, f"Test 200 failed: got {result}, expected {False}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = palindromeIgnoreNonAlnum("m'I edge")
        assert result == False, f"Test 201 failed: got {result}, expected {False}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = palindromeIgnoreNonAlnum('_x_x_x_x')
        assert result == True, f"Test 202 failed: got {result}, expected {True}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = palindromeIgnoreNonAlnum('Panama_x_x edge')
        assert result == False, f"Test 203 failed: got {result}, expected {False}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = palindromeIgnoreNonAlnum('0P_x')
        assert result == False, f"Test 204 failed: got {result}, expected {False}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = palindromeIgnoreNonAlnum('0 aba 0')
        assert result == True, f"Test 205 failed: got {result}, expected {True}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = palindromeIgnoreNonAlnum('saw')
        assert result == False, f"Test 206 failed: got {result}, expected {False}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = palindromeIgnoreNonAlnum('0 0P')
        assert result == False, f"Test 207 failed: got {result}, expected {False}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = palindromeIgnoreNonAlnum('0_x')
        assert result == False, f"Test 208 failed: got {result}, expected {False}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = palindromeIgnoreNonAlnum(' edge 0')
        assert result == False, f"Test 209 failed: got {result}, expected {False}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = palindromeIgnoreNonAlnum('1a2 edge_x 1')
        assert result == False, f"Test 210 failed: got {result}, expected {False}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = palindromeIgnoreNonAlnum('egde ')
        assert result == False, f"Test 211 failed: got {result}, expected {False}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = palindromeIgnoreNonAlnum('x_1')
        assert result == False, f"Test 212 failed: got {result}, expected {False}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = palindromeIgnoreNonAlnum('Top spot_x')
        assert result == False, f"Test 213 failed: got {result}, expected {False}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = palindromeIgnoreNonAlnum('1a2 edge_x 0')
        assert result == False, f"Test 214 failed: got {result}, expected {False}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = palindromeIgnoreNonAlnum('x_egde_x')
        assert result == False, f"Test 215 failed: got {result}, expected {False}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = palindromeIgnoreNonAlnum('edge_x edge')
        assert result == False, f"Test 216 failed: got {result}, expected {False}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = palindromeIgnoreNonAlnum('2a1')
        assert result == False, f"Test 217 failed: got {result}, expected {False}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = palindromeIgnoreNonAlnum('race a car_x edge')
        assert result == False, f"Test 218 failed: got {result}, expected {False}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = palindromeIgnoreNonAlnum('1a2 1 1_x')
        assert result == False, f"Test 219 failed: got {result}, expected {False}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = palindromeIgnoreNonAlnum('1a2_x_x')
        assert result == False, f"Test 220 failed: got {result}, expected {False}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = palindromeIgnoreNonAlnum('12321 0_x_x')
        assert result == False, f"Test 221 failed: got {result}, expected {False}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = palindromeIgnoreNonAlnum('Elba')
        assert result == False, f"Test 222 failed: got {result}, expected {False}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = palindromeIgnoreNonAlnum('egde')
        assert result == False, f"Test 223 failed: got {result}, expected {False}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = palindromeIgnoreNonAlnum('1 0  _x')
        assert result == False, f"Test 224 failed: got {result}, expected {False}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = palindromeIgnoreNonAlnum('x_neve ro ddo reveN')
        assert result == False, f"Test 225 failed: got {result}, expected {False}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = palindromeIgnoreNonAlnum('123,21')
        assert result == True, f"Test 226 failed: got {result}, expected {True}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = palindromeIgnoreNonAlnum(' 0_x 0_x')
        assert result == False, f"Test 227 failed: got {result}, expected {False}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = palindromeIgnoreNonAlnum('x_x_egde 123,21_x')
        assert result == False, f"Test 228 failed: got {result}, expected {False}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = palindromeIgnoreNonAlnum('x_12,321')
        assert result == False, f"Test 229 failed: got {result}, expected {False}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = palindromeIgnoreNonAlnum('x_\nA\n edge')
        assert result == False, f"Test 230 failed: got {result}, expected {False}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = palindromeIgnoreNonAlnum('2a1_x')
        assert result == False, f"Test 231 failed: got {result}, expected {False}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = palindromeIgnoreNonAlnum(',nam 0')
        assert result == False, f"Test 232 failed: got {result}, expected {False}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = palindromeIgnoreNonAlnum('1 2 3 2 1_x')
        assert result == False, f"Test 233 failed: got {result}, expected {False}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = palindromeIgnoreNonAlnum('reste')
        assert result == False, f"Test 234 failed: got {result}, expected {False}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = palindromeIgnoreNonAlnum('1 2 3 2 1_x edge')
        assert result == False, f"Test 235 failed: got {result}, expected {False}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = palindromeIgnoreNonAlnum('Top')
        assert result == False, f"Test 236 failed: got {result}, expected {False}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = palindromeIgnoreNonAlnum('neve_x')
        assert result == False, f"Test 237 failed: got {result}, expected {False}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = palindromeIgnoreNonAlnum('Able was I, ere I saw Elba_x')
        assert result == False, f"Test 238 failed: got {result}, expected {False}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = palindromeIgnoreNonAlnum('\x00 0')
        assert result == True, f"Test 239 failed: got {result}, expected {True}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = palindromeIgnoreNonAlnum('reveN')
        assert result == False, f"Test 240 failed: got {result}, expected {False}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = palindromeIgnoreNonAlnum('x_neve ro ddo reveN 0')
        assert result == False, f"Test 241 failed: got {result}, expected {False}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = palindromeIgnoreNonAlnum('Never odd or even 1 1 0')
        assert result == False, f"Test 242 failed: got {result}, expected {False}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = palindromeIgnoreNonAlnum('Nixon')
        assert result == False, f"Test 243 failed: got {result}, expected {False}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = palindromeIgnoreNonAlnum('odd')
        assert result == False, f"Test 244 failed: got {result}, expected {False}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = palindromeIgnoreNonAlnum('x_1  edge')
        assert result == False, f"Test 245 failed: got {result}, expected {False}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = palindromeIgnoreNonAlnum('Step on no pets_x 1_x')
        assert result == False, f"Test 246 failed: got {result}, expected {False}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = palindromeIgnoreNonAlnum('step on no petS_x_x_x')
        assert result == False, f"Test 247 failed: got {result}, expected {False}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = palindromeIgnoreNonAlnum('step on no petS')
        assert result == True, f"Test 248 failed: got {result}, expected {True}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = palindromeIgnoreNonAlnum('  1')
        assert result == True, f"Test 249 failed: got {result}, expected {True}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = palindromeIgnoreNonAlnum('Step on no pets_x_x_x_x')
        assert result == False, f"Test 250 failed: got {result}, expected {False}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = palindromeIgnoreNonAlnum('Step on no pets edge')
        assert result == False, f"Test 251 failed: got {result}, expected {False}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = palindromeIgnoreNonAlnum('tops poT')
        assert result == True, f"Test 252 failed: got {result}, expected {True}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = palindromeIgnoreNonAlnum('x_?abc!!cba_x_x')
        assert result == False, f"Test 253 failed: got {result}, expected {False}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = palindromeIgnoreNonAlnum('x_egde egde Top spot')
        assert result == False, f"Test 254 failed: got {result}, expected {False}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = palindromeIgnoreNonAlnum('amanaP :lanac a ,nalp a ,nam A 1')
        assert result == False, f"Test 255 failed: got {result}, expected {False}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = palindromeIgnoreNonAlnum('reveN_x')
        assert result == False, f"Test 256 failed: got {result}, expected {False}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = palindromeIgnoreNonAlnum('egde x_egde 0')
        assert result == False, f"Test 257 failed: got {result}, expected {False}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = palindromeIgnoreNonAlnum('ti')
        assert result == False, f"Test 258 failed: got {result}, expected {False}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = palindromeIgnoreNonAlnum('x_x_2a1')
        assert result == False, f"Test 259 failed: got {result}, expected {False}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = palindromeIgnoreNonAlnum("I'm")
        assert result == False, f"Test 260 failed: got {result}, expected {False}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = palindromeIgnoreNonAlnum('x_x_race')
        assert result == False, f"Test 261 failed: got {result}, expected {False}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = palindromeIgnoreNonAlnum('x_0 a1B2b1A')
        assert result == False, f"Test 262 failed: got {result}, expected {False}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = palindromeIgnoreNonAlnum('x_egde')
        assert result == False, f"Test 263 failed: got {result}, expected {False}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = palindromeIgnoreNonAlnum('x_123,21 0')
        assert result == False, f"Test 264 failed: got {result}, expected {False}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = palindromeIgnoreNonAlnum('𝔞abb𝔄 1')
        assert result == False, f"Test 265 failed: got {result}, expected {False}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = palindromeIgnoreNonAlnum('egde 𝔞abb𝔄_x')
        assert result == False, f"Test 266 failed: got {result}, expected {False}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = palindromeIgnoreNonAlnum('Able was I, ere I saw Elba_x_x')
        assert result == False, f"Test 267 failed: got {result}, expected {False}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = palindromeIgnoreNonAlnum('𝔄bba𝔞_x')
        assert result == False, f"Test 268 failed: got {result}, expected {False}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = palindromeIgnoreNonAlnum('0 𝔄bba𝔞 1')
        assert result == False, f"Test 269 failed: got {result}, expected {False}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = palindromeIgnoreNonAlnum('step')
        assert result == False, f"Test 270 failed: got {result}, expected {False}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = palindromeIgnoreNonAlnum('𝔞abb𝔄')
        assert result == False, f"Test 271 failed: got {result}, expected {False}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = palindromeIgnoreNonAlnum('x_Åbbaå')
        assert result == False, f"Test 272 failed: got {result}, expected {False}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = palindromeIgnoreNonAlnum('x_åabbÅ_x')
        assert result == False, f"Test 273 failed: got {result}, expected {False}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = palindromeIgnoreNonAlnum('Åbbaå 1_x_x_x')
        assert result == False, f"Test 274 failed: got {result}, expected {False}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = palindromeIgnoreNonAlnum(' edge 0 1')
        assert result == False, f"Test 275 failed: got {result}, expected {False}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = palindromeIgnoreNonAlnum('petS_x_x_x')
        assert result == False, f"Test 276 failed: got {result}, expected {False}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = palindromeIgnoreNonAlnum('Åbbaå edge_x')
        assert result == False, f"Test 277 failed: got {result}, expected {False}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = palindromeIgnoreNonAlnum('esoper es te ici etser eposÉ 1')
        assert result == False, f"Test 278 failed: got {result}, expected {False}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = palindromeIgnoreNonAlnum('0 aba 0 0')
        assert result == False, f"Test 279 failed: got {result}, expected {False}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = palindromeIgnoreNonAlnum('Ésope reste ici et se repose_x_x')
        assert result == False, f"Test 280 failed: got {result}, expected {False}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = palindromeIgnoreNonAlnum('Ésope reste ici et se repose 1')
        assert result == False, f"Test 281 failed: got {result}, expected {False}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = palindromeIgnoreNonAlnum('x_esoper es te ici etser eposÉ')
        assert result == False, f"Test 282 failed: got {result}, expected {False}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = palindromeIgnoreNonAlnum('Ésope reste ici et se repose edge')
        assert result == False, f"Test 283 failed: got {result}, expected {False}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = palindromeIgnoreNonAlnum('esoper es te ici etser eposÉ')
        assert result == False, f"Test 284 failed: got {result}, expected {False}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = palindromeIgnoreNonAlnum('x_12321')
        assert result == False, f"Test 285 failed: got {result}, expected {False}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = palindromeIgnoreNonAlnum('1 0 egde ')
        assert result == False, f"Test 286 failed: got {result}, expected {False}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = palindromeIgnoreNonAlnum('Was_x edge edge_x_x')
        assert result == False, f"Test 287 failed: got {result}, expected {False}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = palindromeIgnoreNonAlnum('あいいあ 1')
        assert result == True, f"Test 288 failed: got {result}, expected {True}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = palindromeIgnoreNonAlnum('あいいあ_x')
        assert result == True, f"Test 289 failed: got {result}, expected {True}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = palindromeIgnoreNonAlnum('0 1 x_あいいあ')
        assert result == False, f"Test 290 failed: got {result}, expected {False}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = palindromeIgnoreNonAlnum('x_egde abcba')
        assert result == False, f"Test 291 failed: got {result}, expected {False}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = palindromeIgnoreNonAlnum('あいいあ 0')
        assert result == True, f"Test 292 failed: got {result}, expected {True}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = palindromeIgnoreNonAlnum("Madam, I'm Adam. edge_x")
        assert result == False, f"Test 293 failed: got {result}, expected {False}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = palindromeIgnoreNonAlnum('eposÉ_x')
        assert result == False, f"Test 294 failed: got {result}, expected {False}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = palindromeIgnoreNonAlnum('0 😀a😀')
        assert result == False, f"Test 295 failed: got {result}, expected {False}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = palindromeIgnoreNonAlnum('egde x_ _x 0')
        assert result == False, f"Test 296 failed: got {result}, expected {False}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = palindromeIgnoreNonAlnum('abcba edge')
        assert result == False, f"Test 297 failed: got {result}, expected {False}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = palindromeIgnoreNonAlnum('ecar')
        assert result == False, f"Test 298 failed: got {result}, expected {False}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = palindromeIgnoreNonAlnum(' edge 1')
        assert result == False, f"Test 299 failed: got {result}, expected {False}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = palindromeIgnoreNonAlnum('a😀b😀a edge')
        assert result == False, f"Test 300 failed: got {result}, expected {False}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = palindromeIgnoreNonAlnum(' 1 edge edge_x')
        assert result == False, f"Test 301 failed: got {result}, expected {False}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = palindromeIgnoreNonAlnum('egde a😀b😀a')
        assert result == False, f"Test 302 failed: got {result}, expected {False}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = palindromeIgnoreNonAlnum('neve_x_x_x')
        assert result == False, f"Test 303 failed: got {result}, expected {False}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = palindromeIgnoreNonAlnum('x_a😀b😀a')
        assert result == False, f"Test 304 failed: got {result}, expected {False}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = palindromeIgnoreNonAlnum('a😀b😀a 1')
        assert result == False, f"Test 305 failed: got {result}, expected {False}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = palindromeIgnoreNonAlnum('Hello, 1_x')
        assert result == False, f"Test 306 failed: got {result}, expected {False}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = palindromeIgnoreNonAlnum('Hello,')
        assert result == False, f"Test 307 failed: got {result}, expected {False}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = palindromeIgnoreNonAlnum('_x_x_x')
        assert result == True, f"Test 308 failed: got {result}, expected {True}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = palindromeIgnoreNonAlnum('1 x_saW')
        assert result == False, f"Test 309 failed: got {result}, expected {False}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = palindromeIgnoreNonAlnum('petS')
        assert result == False, f"Test 310 failed: got {result}, expected {False}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = palindromeIgnoreNonAlnum('egde rac a ecar 1 edge 1')
        assert result == False, f"Test 311 failed: got {result}, expected {False}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = palindromeIgnoreNonAlnum('poT')
        assert result == False, f"Test 312 failed: got {result}, expected {False}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = palindromeIgnoreNonAlnum('egde ,I 1_x')
        assert result == False, f"Test 313 failed: got {result}, expected {False}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = palindromeIgnoreNonAlnum('a\x00a 1')
        assert result == False, f"Test 314 failed: got {result}, expected {False}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = palindromeIgnoreNonAlnum('egde x_a\x00a')
        assert result == False, f"Test 315 failed: got {result}, expected {False}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = palindromeIgnoreNonAlnum('1 2 3 2 1 0_x')
        assert result == False, f"Test 316 failed: got {result}, expected {False}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = palindromeIgnoreNonAlnum('x_x_egde egde x_saW')
        assert result == False, f"Test 317 failed: got {result}, expected {False}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = palindromeIgnoreNonAlnum('Adam._x')
        assert result == False, f"Test 318 failed: got {result}, expected {False}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = palindromeIgnoreNonAlnum('amanaP :lanac a ,nalp a ,nam A 1 0 0')
        assert result == False, f"Test 319 failed: got {result}, expected {False}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = palindromeIgnoreNonAlnum('x_x_2a1_x_x')
        assert result == False, f"Test 320 failed: got {result}, expected {False}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = palindromeIgnoreNonAlnum('1a2_x_x_x')
        assert result == False, f"Test 321 failed: got {result}, expected {False}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = palindromeIgnoreNonAlnum('\nA\n_x_x 0')
        assert result == False, f"Test 322 failed: got {result}, expected {False}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = palindromeIgnoreNonAlnum('ab edge')
        assert result == False, f"Test 323 failed: got {result}, expected {False}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = palindromeIgnoreNonAlnum('egde car_x')
        assert result == False, f"Test 324 failed: got {result}, expected {False}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = palindromeIgnoreNonAlnum('ecar_x_x')
        assert result == False, f"Test 325 failed: got {result}, expected {False}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = palindromeIgnoreNonAlnum('x_egde 0  1')
        assert result == False, f"Test 326 failed: got {result}, expected {False}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = palindromeIgnoreNonAlnum('x_\nA\n')
        assert result == False, f"Test 327 failed: got {result}, expected {False}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = palindromeIgnoreNonAlnum('\t 0')
        assert result == True, f"Test 328 failed: got {result}, expected {True}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = palindromeIgnoreNonAlnum('\t_x')
        assert result == True, f"Test 329 failed: got {result}, expected {True}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = palindromeIgnoreNonAlnum("Madam, I'm Adam._x 0_x 1_x")
        assert result == False, f"Test 330 failed: got {result}, expected {False}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = palindromeIgnoreNonAlnum('1 ')
        assert result == True, f"Test 331 failed: got {result}, expected {True}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = palindromeIgnoreNonAlnum('edge_x_x 0_x')
        assert result == False, f"Test 332 failed: got {result}, expected {False}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = palindromeIgnoreNonAlnum('rac')
        assert result == False, f"Test 333 failed: got {result}, expected {False}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = palindromeIgnoreNonAlnum(' 0 1_x')
        assert result == False, f"Test 334 failed: got {result}, expected {False}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = palindromeIgnoreNonAlnum('abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba_x edge')
        assert result == False, f"Test 335 failed: got {result}, expected {False}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = palindromeIgnoreNonAlnum('oN')
        assert result == False, f"Test 336 failed: got {result}, expected {False}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = palindromeIgnoreNonAlnum('  0 edge 0')
        assert result == False, f"Test 337 failed: got {result}, expected {False}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
