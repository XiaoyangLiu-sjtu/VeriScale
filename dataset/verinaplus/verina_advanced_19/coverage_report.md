# Coverage Report

Total executable lines: 3
Covered lines: 3
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def isCleanPalindrome(s: str) -> bool:
2: ✓     filtered = [char.lower() for char in s if char.isalpha()]
3: ✓     return filtered == filtered[::-1]
```

## Complete Test File

```python
def isCleanPalindrome(s: str) -> bool:
    filtered = [char.lower() for char in s if char.isalpha()]
    return filtered == filtered[::-1]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = isCleanPalindrome('A man, a plan, a canal, Panama')
        assert result == True, f"Test 1 failed: got {result}, expected {True}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = isCleanPalindrome('No lemon, no melon')
        assert result == True, f"Test 2 failed: got {result}, expected {True}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = isCleanPalindrome('OpenAI')
        assert result == False, f"Test 3 failed: got {result}, expected {False}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = isCleanPalindrome('Was it a car or a cat I saw?')
        assert result == True, f"Test 4 failed: got {result}, expected {True}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = isCleanPalindrome('Hello, World!')
        assert result == False, f"Test 5 failed: got {result}, expected {False}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = isCleanPalindrome('')
        assert result == True, f"Test 6 failed: got {result}, expected {True}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = isCleanPalindrome('a')
        assert result == True, f"Test 7 failed: got {result}, expected {True}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = isCleanPalindrome('aa')
        assert result == True, f"Test 8 failed: got {result}, expected {True}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = isCleanPalindrome('ab')
        assert result == False, f"Test 9 failed: got {result}, expected {False}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = isCleanPalindrome('A')
        assert result == True, f"Test 10 failed: got {result}, expected {True}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = isCleanPalindrome('Aa')
        assert result == True, f"Test 11 failed: got {result}, expected {True}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = isCleanPalindrome('Aba')
        assert result == True, f"Test 12 failed: got {result}, expected {True}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = isCleanPalindrome('abba')
        assert result == True, f"Test 13 failed: got {result}, expected {True}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = isCleanPalindrome('abcba')
        assert result == True, f"Test 14 failed: got {result}, expected {True}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = isCleanPalindrome('abccba')
        assert result == True, f"Test 15 failed: got {result}, expected {True}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = isCleanPalindrome('A man, a plan, a canal, Panama!')
        assert result == True, f"Test 16 failed: got {result}, expected {True}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = isCleanPalindrome("Madam, I'm Adam.")
        assert result == True, f"Test 17 failed: got {result}, expected {True}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = isCleanPalindrome('Never odd or even.')
        assert result == True, f"Test 18 failed: got {result}, expected {True}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = isCleanPalindrome('Step on no pets')
        assert result == True, f"Test 19 failed: got {result}, expected {True}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = isCleanPalindrome('Able was I ere I saw Elba')
        assert result == True, f"Test 20 failed: got {result}, expected {True}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = isCleanPalindrome('palindrome')
        assert result == False, f"Test 21 failed: got {result}, expected {False}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = isCleanPalindrome('12321')
        assert result == True, f"Test 22 failed: got {result}, expected {True}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = isCleanPalindrome('123abccba321')
        assert result == True, f"Test 23 failed: got {result}, expected {True}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = isCleanPalindrome('1a2')
        assert result == True, f"Test 24 failed: got {result}, expected {True}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = isCleanPalindrome('1ab2')
        assert result == False, f"Test 25 failed: got {result}, expected {False}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = isCleanPalindrome('!!!')
        assert result == True, f"Test 26 failed: got {result}, expected {True}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = isCleanPalindrome('.,, ,,,')
        assert result == True, f"Test 27 failed: got {result}, expected {True}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = isCleanPalindrome('A Toyota! Race fast, safe car! A Toyota!')
        assert result == True, f"Test 28 failed: got {result}, expected {True}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = isCleanPalindrome('Mr. Owl ate my metal worm')
        assert result == True, f"Test 29 failed: got {result}, expected {True}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = isCleanPalindrome('Do geese see God?')
        assert result == True, f"Test 30 failed: got {result}, expected {True}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = isCleanPalindrome('Eva, can I see bees in a cave?')
        assert result == True, f"Test 31 failed: got {result}, expected {True}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = isCleanPalindrome('あいいあ')
        assert result == True, f"Test 32 failed: got {result}, expected {True}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = isCleanPalindrome('été')
        assert result == True, f"Test 33 failed: got {result}, expected {True}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = isCleanPalindrome('Ésope reste ici et se repose')
        assert result == False, f"Test 34 failed: got {result}, expected {False}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = isCleanPalindrome('А роза упала на лапу Азора')
        assert result == True, f"Test 35 failed: got {result}, expected {True}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = isCleanPalindrome('🙂madam🙂')
        assert result == True, f"Test 36 failed: got {result}, expected {True}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = isCleanPalindrome('ma\x00dam')
        assert result == True, f"Test 37 failed: got {result}, expected {True}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = isCleanPalindrome('\nA man\t,\na plan\r,\na canal: Panama\n')
        assert result == True, f"Test 38 failed: got {result}, expected {True}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = isCleanPalindrome('áb́á')
        assert result == True, f"Test 39 failed: got {result}, expected {True}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = isCleanPalindrome('𝔄b𝔄')
        assert result == True, f"Test 40 failed: got {result}, expected {True}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = isCleanPalindrome('   ')
        assert result == True, f"Test 41 failed: got {result}, expected {True}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = isCleanPalindrome('A man, a plan, a canal, Panama_x')
        assert result == False, f"Test 42 failed: got {result}, expected {False}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = isCleanPalindrome('Was')
        assert result == False, f"Test 43 failed: got {result}, expected {False}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = isCleanPalindrome(' 0')
        assert result == True, f"Test 44 failed: got {result}, expected {True}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = isCleanPalindrome('amanaP ,lanac a ,nalp a ,nam A')
        assert result == True, f"Test 45 failed: got {result}, expected {True}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = isCleanPalindrome('A man, a plan, a canal, Panama 0')
        assert result == True, f"Test 46 failed: got {result}, expected {True}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = isCleanPalindrome('1 ')
        assert result == True, f"Test 47 failed: got {result}, expected {True}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = isCleanPalindrome('amanaP ,lanac a ,nalp a ,nam A_x')
        assert result == False, f"Test 48 failed: got {result}, expected {False}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = isCleanPalindrome('Ésope')
        assert result == False, f"Test 49 failed: got {result}, expected {False}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = isCleanPalindrome('áb́á edge_x')
        assert result == False, f"Test 50 failed: got {result}, expected {False}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = isCleanPalindrome('No lemon, no melon_x')
        assert result == False, f"Test 51 failed: got {result}, expected {False}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = isCleanPalindrome('saw')
        assert result == False, f"Test 52 failed: got {result}, expected {False}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = isCleanPalindrome('A man, a plan, a canal, Panama_x 0')
        assert result == False, f"Test 53 failed: got {result}, expected {False}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = isCleanPalindrome('Madam,')
        assert result == True, f"Test 54 failed: got {result}, expected {True}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = isCleanPalindrome('A man, a plan, a canal, Panama! edge')
        assert result == False, f"Test 55 failed: got {result}, expected {False}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = isCleanPalindrome('canal:')
        assert result == False, f"Test 56 failed: got {result}, expected {False}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = isCleanPalindrome('car')
        assert result == False, f"Test 57 failed: got {result}, expected {False}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = isCleanPalindrome('plan,_x 0_x')
        assert result == False, f"Test 58 failed: got {result}, expected {False}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = isCleanPalindrome('Mr.')
        assert result == False, f"Test 59 failed: got {result}, expected {False}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = isCleanPalindrome('0')
        assert result == True, f"Test 60 failed: got {result}, expected {True}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = isCleanPalindrome('Able_x')
        assert result == False, f"Test 61 failed: got {result}, expected {False}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = isCleanPalindrome('x_ro_x')
        assert result == False, f"Test 62 failed: got {result}, expected {False}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = isCleanPalindrome('Mr. 0 1_x')
        assert result == False, f"Test 63 failed: got {result}, expected {False}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = isCleanPalindrome('1 IAnepO')
        assert result == False, f"Test 64 failed: got {result}, expected {False}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = isCleanPalindrome('egde')
        assert result == False, f"Test 65 failed: got {result}, expected {False}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = isCleanPalindrome('IAnepO')
        assert result == False, f"Test 66 failed: got {result}, expected {False}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = isCleanPalindrome(' 1_x')
        assert result == True, f"Test 67 failed: got {result}, expected {True}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = isCleanPalindrome('egde IAnepO')
        assert result == False, f"Test 68 failed: got {result}, expected {False}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = isCleanPalindrome('x_IAnepO_x_x')
        assert result == False, f"Test 69 failed: got {result}, expected {False}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = isCleanPalindrome('OpenAI_x')
        assert result == False, f"Test 70 failed: got {result}, expected {False}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = isCleanPalindrome('_x')
        assert result == True, f"Test 71 failed: got {result}, expected {True}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = isCleanPalindrome('worm edge')
        assert result == False, f"Test 72 failed: got {result}, expected {False}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = isCleanPalindrome('на')
        assert result == True, f"Test 73 failed: got {result}, expected {True}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = isCleanPalindrome('palindrome_x')
        assert result == False, f"Test 74 failed: got {result}, expected {False}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = isCleanPalindrome('Was it a car or a cat I saw? 1')
        assert result == True, f"Test 75 failed: got {result}, expected {True}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = isCleanPalindrome('Was it a car or a cat I saw? edge')
        assert result == False, f"Test 76 failed: got {result}, expected {False}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = isCleanPalindrome('?was I tac a ro rac a ti saW')
        assert result == True, f"Test 77 failed: got {result}, expected {True}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = isCleanPalindrome('egde ?was I tac a ro rac a ti saW 1')
        assert result == False, f"Test 78 failed: got {result}, expected {False}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = isCleanPalindrome('my')
        assert result == False, f"Test 79 failed: got {result}, expected {False}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = isCleanPalindrome('se')
        assert result == False, f"Test 80 failed: got {result}, expected {False}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = isCleanPalindrome('even.')
        assert result == False, f"Test 81 failed: got {result}, expected {False}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = isCleanPalindrome('Was it a car or a cat I saw?_x')
        assert result == False, f"Test 82 failed: got {result}, expected {False}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = isCleanPalindrome(' 1')
        assert result == True, f"Test 83 failed: got {result}, expected {True}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = isCleanPalindrome('x_?was I tac a ro rac a ti saW')
        assert result == False, f"Test 84 failed: got {result}, expected {False}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = isCleanPalindrome(' 0 edge')
        assert result == False, f"Test 85 failed: got {result}, expected {False}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = isCleanPalindrome('abcba 1')
        assert result == True, f"Test 86 failed: got {result}, expected {True}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = isCleanPalindrome('1 1')
        assert result == True, f"Test 87 failed: got {result}, expected {True}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = isCleanPalindrome('pets')
        assert result == False, f"Test 88 failed: got {result}, expected {False}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = isCleanPalindrome('Do geese see God?_x')
        assert result == False, f"Test 89 failed: got {result}, expected {False}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = isCleanPalindrome('А')
        assert result == True, f"Test 90 failed: got {result}, expected {True}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = isCleanPalindrome('saw?_x')
        assert result == False, f"Test 91 failed: got {result}, expected {False}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = isCleanPalindrome('ro_x')
        assert result == False, f"Test 92 failed: got {result}, expected {False}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = isCleanPalindrome('it edge')
        assert result == False, f"Test 93 failed: got {result}, expected {False}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = isCleanPalindrome('ici')
        assert result == True, f"Test 94 failed: got {result}, expected {True}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = isCleanPalindrome('Eva,_x')
        assert result == False, f"Test 95 failed: got {result}, expected {False}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = isCleanPalindrome('_x 1 edge 1')
        assert result == False, f"Test 96 failed: got {result}, expected {False}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = isCleanPalindrome('it')
        assert result == False, f"Test 97 failed: got {result}, expected {False}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = isCleanPalindrome('x_Was it a car or a cat I saw?_x 1_x')
        assert result == False, f"Test 98 failed: got {result}, expected {False}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = isCleanPalindrome('World!')
        assert result == False, f"Test 99 failed: got {result}, expected {False}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = isCleanPalindrome('Ésope reste ici et se repose edge')
        assert result == False, f"Test 100 failed: got {result}, expected {False}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = isCleanPalindrome('Panama!')
        assert result == False, f"Test 101 failed: got {result}, expected {False}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = isCleanPalindrome('God?')
        assert result == False, f"Test 102 failed: got {result}, expected {False}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = isCleanPalindrome('А роза упала на лапу Азора_x')
        assert result == True, f"Test 103 failed: got {result}, expected {True}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = isCleanPalindrome('x_Was')
        assert result == False, f"Test 104 failed: got {result}, expected {False}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = isCleanPalindrome(',,,')
        assert result == True, f"Test 105 failed: got {result}, expected {True}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = isCleanPalindrome('x_0 a')
        assert result == False, f"Test 106 failed: got {result}, expected {False}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = isCleanPalindrome('egde x_a_x')
        assert result == False, f"Test 107 failed: got {result}, expected {False}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = isCleanPalindrome('?was I tac a ro rac a ti saW 0')
        assert result == True, f"Test 108 failed: got {result}, expected {True}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = isCleanPalindrome('x_0 a_x')
        assert result == True, f"Test 109 failed: got {result}, expected {True}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = isCleanPalindrome('a_x')
        assert result == False, f"Test 110 failed: got {result}, expected {False}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = isCleanPalindrome('_x_x')
        assert result == True, f"Test 111 failed: got {result}, expected {True}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = isCleanPalindrome('x_a_x')
        assert result == True, f"Test 112 failed: got {result}, expected {True}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = isCleanPalindrome('saw?')
        assert result == False, f"Test 113 failed: got {result}, expected {False}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = isCleanPalindrome('a 0')
        assert result == True, f"Test 114 failed: got {result}, expected {True}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = isCleanPalindrome('.,,_x_x 1')
        assert result == True, f"Test 115 failed: got {result}, expected {True}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = isCleanPalindrome(',')
        assert result == True, f"Test 116 failed: got {result}, expected {True}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = isCleanPalindrome('aa edge')
        assert result == False, f"Test 117 failed: got {result}, expected {False}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = isCleanPalindrome('ate')
        assert result == False, f"Test 118 failed: got {result}, expected {False}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = isCleanPalindrome('aa_x')
        assert result == False, f"Test 119 failed: got {result}, expected {False}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = isCleanPalindrome('plan')
        assert result == False, f"Test 120 failed: got {result}, expected {False}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = isCleanPalindrome('1 ablE_x')
        assert result == False, f"Test 121 failed: got {result}, expected {False}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = isCleanPalindrome('IAnepO_x')
        assert result == False, f"Test 122 failed: got {result}, expected {False}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = isCleanPalindrome('aa 1')
        assert result == True, f"Test 123 failed: got {result}, expected {True}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = isCleanPalindrome('reste 0')
        assert result == False, f"Test 124 failed: got {result}, expected {False}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = isCleanPalindrome('x_ba')
        assert result == False, f"Test 125 failed: got {result}, expected {False}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = isCleanPalindrome('reste 0_x 0 edge')
        assert result == False, f"Test 126 failed: got {result}, expected {False}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = isCleanPalindrome('на_x')
        assert result == True, f"Test 127 failed: got {result}, expected {True}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = isCleanPalindrome('_x 0 0')
        assert result == True, f"Test 128 failed: got {result}, expected {True}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = isCleanPalindrome('ba 0_x')
        assert result == False, f"Test 129 failed: got {result}, expected {False}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = isCleanPalindrome('ym')
        assert result == False, f"Test 130 failed: got {result}, expected {False}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = isCleanPalindrome('12321 1')
        assert result == True, f"Test 131 failed: got {result}, expected {True}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = isCleanPalindrome('was 1 edge')
        assert result == False, f"Test 132 failed: got {result}, expected {False}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = isCleanPalindrome('A 1')
        assert result == True, f"Test 133 failed: got {result}, expected {True}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = isCleanPalindrome('0_x edge')
        assert result == False, f"Test 134 failed: got {result}, expected {False}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = isCleanPalindrome('x_aA')
        assert result == False, f"Test 135 failed: got {result}, expected {False}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = isCleanPalindrome('odd')
        assert result == False, f"Test 136 failed: got {result}, expected {False}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = isCleanPalindrome('x_')
        assert result == True, f"Test 137 failed: got {result}, expected {True}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = isCleanPalindrome('egde азор 1')
        assert result == False, f"Test 138 failed: got {result}, expected {False}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = isCleanPalindrome('Aa_x 0')
        assert result == False, f"Test 139 failed: got {result}, expected {False}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = isCleanPalindrome('amanaP ,lanac a ,nalp a ,nam A_x 1 0 1')
        assert result == False, f"Test 140 failed: got {result}, expected {False}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = isCleanPalindrome('Aba edge')
        assert result == False, f"Test 141 failed: got {result}, expected {False}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = isCleanPalindrome('?was 0')
        assert result == False, f"Test 142 failed: got {result}, expected {False}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = isCleanPalindrome('reste 0_x 0 edge edge edge')
        assert result == False, f"Test 143 failed: got {result}, expected {False}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = isCleanPalindrome('abA')
        assert result == True, f"Test 144 failed: got {result}, expected {True}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = isCleanPalindrome('1 упал')
        assert result == True, f"Test 145 failed: got {result}, expected {True}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = isCleanPalindrome('роза')
        assert result == True, f"Test 146 failed: got {result}, expected {True}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = isCleanPalindrome('1 eta')
        assert result == False, f"Test 147 failed: got {result}, expected {False}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = isCleanPalindrome('Aba_x')
        assert result == False, f"Test 148 failed: got {result}, expected {False}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = isCleanPalindrome('ici 0')
        assert result == True, f"Test 149 failed: got {result}, expected {True}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = isCleanPalindrome('_x 1')
        assert result == True, f"Test 150 failed: got {result}, expected {True}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = isCleanPalindrome('на edge')
        assert result == False, f"Test 151 failed: got {result}, expected {False}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = isCleanPalindrome('melon')
        assert result == False, f"Test 152 failed: got {result}, expected {False}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = isCleanPalindrome('abba 1 1')
        assert result == True, f"Test 153 failed: got {result}, expected {True}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = isCleanPalindrome('abba edge')
        assert result == False, f"Test 154 failed: got {result}, expected {False}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = isCleanPalindrome(' edge')
        assert result == False, f"Test 155 failed: got {result}, expected {False}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = isCleanPalindrome('melon_x')
        assert result == False, f"Test 156 failed: got {result}, expected {False}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = isCleanPalindrome('ba 1')
        assert result == False, f"Test 157 failed: got {result}, expected {False}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = isCleanPalindrome('x_A')
        assert result == False, f"Test 158 failed: got {result}, expected {False}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = isCleanPalindrome('canal,')
        assert result == False, f"Test 159 failed: got {result}, expected {False}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = isCleanPalindrome('pets_x_x')
        assert result == False, f"Test 160 failed: got {result}, expected {False}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = isCleanPalindrome('abcba edge')
        assert result == False, f"Test 161 failed: got {result}, expected {False}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = isCleanPalindrome('abcba 0')
        assert result == True, f"Test 162 failed: got {result}, expected {True}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = isCleanPalindrome('x_ro_x 0')
        assert result == False, f"Test 163 failed: got {result}, expected {False}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = isCleanPalindrome('x_egde abccba')
        assert result == False, f"Test 164 failed: got {result}, expected {False}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = isCleanPalindrome('abccba 1 1')
        assert result == True, f"Test 165 failed: got {result}, expected {True}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = isCleanPalindrome(',nam')
        assert result == False, f"Test 166 failed: got {result}, expected {False}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = isCleanPalindrome('abccba_x_x')
        assert result == False, f"Test 167 failed: got {result}, expected {False}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = isCleanPalindrome('азор_x 1')
        assert result == True, f"Test 168 failed: got {result}, expected {True}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = isCleanPalindrome('abccba_x')
        assert result == False, f"Test 169 failed: got {result}, expected {False}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = isCleanPalindrome('Adam.')
        assert result == False, f"Test 170 failed: got {result}, expected {False}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = isCleanPalindrome('Азора_x')
        assert result == True, f"Test 171 failed: got {result}, expected {True}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = isCleanPalindrome('x_elbA 1')
        assert result == False, f"Test 172 failed: got {result}, expected {False}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = isCleanPalindrome('!amanaP ,lanac a ,nalp a ,nam A_x_x_x 0')
        assert result == False, f"Test 173 failed: got {result}, expected {False}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = isCleanPalindrome('Eva, can I see bees in a cave?_x')
        assert result == False, f"Test 174 failed: got {result}, expected {False}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = isCleanPalindrome('А роза упала на лапу Азора_x edge edge')
        assert result == False, f"Test 175 failed: got {result}, expected {False}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = isCleanPalindrome('No edge 0')
        assert result == False, f"Test 176 failed: got {result}, expected {False}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = isCleanPalindrome('rac_x')
        assert result == False, f"Test 177 failed: got {result}, expected {False}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = isCleanPalindrome(".madA m'I ,madaM_x")
        assert result == False, f"Test 178 failed: got {result}, expected {False}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = isCleanPalindrome('egde ?was I tac a ro rac a ti saW 1_x')
        assert result == False, f"Test 179 failed: got {result}, expected {False}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = isCleanPalindrome('abccba_x 1')
        assert result == False, f"Test 180 failed: got {result}, expected {False}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = isCleanPalindrome('x_Was it a car or a cat I saw?_x 1_x_x')
        assert result == False, f"Test 181 failed: got {result}, expected {False}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = isCleanPalindrome('0 x_?doG ees eseeg oD')
        assert result == False, f"Test 182 failed: got {result}, expected {False}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = isCleanPalindrome("Madam, I'm Adam._x")
        assert result == False, f"Test 183 failed: got {result}, expected {False}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = isCleanPalindrome('?evac_x')
        assert result == False, f"Test 184 failed: got {result}, expected {False}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = isCleanPalindrome('Never odd or even. 0_x')
        assert result == False, f"Test 185 failed: got {result}, expected {False}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = isCleanPalindrome('Never odd or even. 1')
        assert result == True, f"Test 186 failed: got {result}, expected {True}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = isCleanPalindrome('1 1 abba')
        assert result == True, f"Test 187 failed: got {result}, expected {True}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = isCleanPalindrome('Never odd or even. edge')
        assert result == False, f"Test 188 failed: got {result}, expected {False}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = isCleanPalindrome('_x_x_x')
        assert result == True, f"Test 189 failed: got {result}, expected {True}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = isCleanPalindrome('x_elbA')
        assert result == False, f"Test 190 failed: got {result}, expected {False}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = isCleanPalindrome('.,,')
        assert result == True, f"Test 191 failed: got {result}, expected {True}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = isCleanPalindrome('Aa_x')
        assert result == False, f"Test 192 failed: got {result}, expected {False}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = isCleanPalindrome('Aba_x 0')
        assert result == False, f"Test 193 failed: got {result}, expected {False}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = isCleanPalindrome('1 _x')
        assert result == True, f"Test 194 failed: got {result}, expected {True}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = isCleanPalindrome('1 12321')
        assert result == True, f"Test 195 failed: got {result}, expected {True}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = isCleanPalindrome('Panama edge')
        assert result == False, f"Test 196 failed: got {result}, expected {False}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = isCleanPalindrome('Able was I ere I saw Elba edge')
        assert result == False, f"Test 197 failed: got {result}, expected {False}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = isCleanPalindrome('it edge_x')
        assert result == False, f"Test 198 failed: got {result}, expected {False}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = isCleanPalindrome('ablE was I ere I saw elbA 1')
        assert result == True, f"Test 199 failed: got {result}, expected {True}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = isCleanPalindrome('x_x_ablE was I ere I saw elbA edge_x')
        assert result == False, f"Test 200 failed: got {result}, expected {False}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = isCleanPalindrome('ti')
        assert result == False, f"Test 201 failed: got {result}, expected {False}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = isCleanPalindrome('ablE was I ere I saw elbA_x_x')
        assert result == False, f"Test 202 failed: got {result}, expected {False}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = isCleanPalindrome('se_x_x')
        assert result == False, f"Test 203 failed: got {result}, expected {False}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = isCleanPalindrome('egde  edge')
        assert result == True, f"Test 204 failed: got {result}, expected {True}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = isCleanPalindrome('Able was I ere I saw Elba_x')
        assert result == False, f"Test 205 failed: got {result}, expected {False}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = isCleanPalindrome('лапу')
        assert result == True, f"Test 206 failed: got {result}, expected {True}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = isCleanPalindrome('palindrome 0')
        assert result == False, f"Test 207 failed: got {result}, expected {False}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = isCleanPalindrome('ere')
        assert result == True, f"Test 208 failed: got {result}, expected {True}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = isCleanPalindrome('0 palindrome')
        assert result == False, f"Test 209 failed: got {result}, expected {False}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = isCleanPalindrome('saW')
        assert result == False, f"Test 210 failed: got {result}, expected {False}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = isCleanPalindrome(' edge 0')
        assert result == False, f"Test 211 failed: got {result}, expected {False}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = isCleanPalindrome('12321 edge_x 1')
        assert result == False, f"Test 212 failed: got {result}, expected {False}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = isCleanPalindrome('egde ')
        assert result == False, f"Test 213 failed: got {result}, expected {False}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = isCleanPalindrome('cave?_x')
        assert result == False, f"Test 214 failed: got {result}, expected {False}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = isCleanPalindrome('saw?_x_x')
        assert result == False, f"Test 215 failed: got {result}, expected {False}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = isCleanPalindrome('12321 edge_x 0')
        assert result == False, f"Test 216 failed: got {result}, expected {False}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = isCleanPalindrome('ablE_x_x')
        assert result == False, f"Test 217 failed: got {result}, expected {False}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = isCleanPalindrome('упала 1')
        assert result == True, f"Test 218 failed: got {result}, expected {True}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = isCleanPalindrome('.madA')
        assert result == False, f"Test 219 failed: got {result}, expected {False}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = isCleanPalindrome('12321_x')
        assert result == True, f"Test 220 failed: got {result}, expected {True}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = isCleanPalindrome('x__x')
        assert result == True, f"Test 221 failed: got {result}, expected {True}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = isCleanPalindrome('elbA_x_x')
        assert result == False, f"Test 222 failed: got {result}, expected {False}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = isCleanPalindrome('0_x 0')
        assert result == True, f"Test 223 failed: got {result}, expected {True}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = isCleanPalindrome('x_egde x_12321 0')
        assert result == False, f"Test 224 failed: got {result}, expected {False}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = isCleanPalindrome('no_x')
        assert result == False, f"Test 225 failed: got {result}, expected {False}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = isCleanPalindrome('ees')
        assert result == False, f"Test 226 failed: got {result}, expected {False}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = isCleanPalindrome('1')
        assert result == True, f"Test 227 failed: got {result}, expected {True}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = isCleanPalindrome('egde азор 1 0')
        assert result == False, f"Test 228 failed: got {result}, expected {False}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = isCleanPalindrome('x_egde ti')
        assert result == False, f"Test 229 failed: got {result}, expected {False}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = isCleanPalindrome('2a1')
        assert result == True, f"Test 230 failed: got {result}, expected {True}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = isCleanPalindrome(' 0_x 0_x')
        assert result == True, f"Test 231 failed: got {result}, expected {True}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = isCleanPalindrome('x_x_egde 2a1_x')
        assert result == False, f"Test 232 failed: got {result}, expected {False}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = isCleanPalindrome('x_1a2')
        assert result == False, f"Test 233 failed: got {result}, expected {False}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = isCleanPalindrome('x_2a1 edge')
        assert result == False, f"Test 234 failed: got {result}, expected {False}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = isCleanPalindrome('Elba_x_x')
        assert result == False, f"Test 235 failed: got {result}, expected {False}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = isCleanPalindrome('1_x_x')
        assert result == True, f"Test 236 failed: got {result}, expected {True}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = isCleanPalindrome('amanaP 0')
        assert result == False, f"Test 237 failed: got {result}, expected {False}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = isCleanPalindrome('1ab2_x')
        assert result == False, f"Test 238 failed: got {result}, expected {False}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = isCleanPalindrome('Panama_x')
        assert result == False, f"Test 239 failed: got {result}, expected {False}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = isCleanPalindrome('1ab2_x edge')
        assert result == False, f"Test 240 failed: got {result}, expected {False}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = isCleanPalindrome('А_x')
        assert result == True, f"Test 241 failed: got {result}, expected {True}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = isCleanPalindrome('!!!_x')
        assert result == True, f"Test 242 failed: got {result}, expected {True}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = isCleanPalindrome('!amanaP')
        assert result == False, f"Test 243 failed: got {result}, expected {False}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = isCleanPalindrome('egde _x')
        assert result == False, f"Test 244 failed: got {result}, expected {False}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = isCleanPalindrome('ici 0 0')
        assert result == True, f"Test 245 failed: got {result}, expected {True}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = isCleanPalindrome('x_!!! 0')
        assert result == True, f"Test 246 failed: got {result}, expected {True}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = isCleanPalindrome('!!! 1 1 0')
        assert result == True, f"Test 247 failed: got {result}, expected {True}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = isCleanPalindrome('.,, ,,,_x_x')
        assert result == True, f"Test 248 failed: got {result}, expected {True}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = isCleanPalindrome('x_!!! 0_x 0')
        assert result == True, f"Test 249 failed: got {result}, expected {True}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = isCleanPalindrome('No')
        assert result == False, f"Test 250 failed: got {result}, expected {False}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = isCleanPalindrome(',,, ,,.')
        assert result == True, f"Test 251 failed: got {result}, expected {True}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = isCleanPalindrome('!atoyoT A !rac efas ,tsaf ecaR !atoyoT A')
        assert result == True, f"Test 252 failed: got {result}, expected {True}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = isCleanPalindrome('a 0 1')
        assert result == True, f"Test 253 failed: got {result}, expected {True}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = isCleanPalindrome('A Toyota! Race fast, safe car! A Toyota!_x_x_x_x')
        assert result == False, f"Test 254 failed: got {result}, expected {False}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = isCleanPalindrome('A Toyota! Race fast, safe car! A Toyota! edge')
        assert result == False, f"Test 255 failed: got {result}, expected {False}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = isCleanPalindrome('mrow latem ym eta lwO .rM')
        assert result == True, f"Test 256 failed: got {result}, expected {True}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = isCleanPalindrome('x_egde egde Mr. Owl ate my metal worm')
        assert result == False, f"Test 257 failed: got {result}, expected {False}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = isCleanPalindrome('0 12321_x edge_x 1')
        assert result == False, f"Test 258 failed: got {result}, expected {False}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = isCleanPalindrome('Toyota!')
        assert result == False, f"Test 259 failed: got {result}, expected {False}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = isCleanPalindrome('edge_x')
        assert result == False, f"Test 260 failed: got {result}, expected {False}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = isCleanPalindrome('упал_x')
        assert result == True, f"Test 261 failed: got {result}, expected {True}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = isCleanPalindrome('0 12321_x edge_x 1 edge')
        assert result == False, f"Test 262 failed: got {result}, expected {False}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = isCleanPalindrome('man,')
        assert result == False, f"Test 263 failed: got {result}, expected {False}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = isCleanPalindrome('x_x_Able was I ere I saw Elba')
        assert result == False, f"Test 264 failed: got {result}, expected {False}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = isCleanPalindrome('Elba_x_x edge')
        assert result == False, f"Test 265 failed: got {result}, expected {False}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = isCleanPalindrome('x_0 ?doG ees eseeg oD')
        assert result == False, f"Test 266 failed: got {result}, expected {False}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = isCleanPalindrome('cave?')
        assert result == False, f"Test 267 failed: got {result}, expected {False}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = isCleanPalindrome('x_0 Panama 0')
        assert result == False, f"Test 268 failed: got {result}, expected {False}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = isCleanPalindrome('?evac a ni seeb ees I nac ,avE 1')
        assert result == True, f"Test 269 failed: got {result}, expected {True}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = isCleanPalindrome('egde ?evac a ni seeb ees I nac ,avE_x')
        assert result == False, f"Test 270 failed: got {result}, expected {False}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = isCleanPalindrome('nac_x')
        assert result == False, f"Test 271 failed: got {result}, expected {False}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = isCleanPalindrome('0 Eva, can I see bees in a cave? 1')
        assert result == True, f"Test 272 failed: got {result}, expected {True}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = isCleanPalindrome('Eva,')
        assert result == False, f"Test 273 failed: got {result}, expected {False}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = isCleanPalindrome('x_あいいあ')
        assert result == True, f"Test 274 failed: got {result}, expected {True}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = isCleanPalindrome('A_x')
        assert result == False, f"Test 275 failed: got {result}, expected {False}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = isCleanPalindrome('x_あいいあ_x')
        assert result == True, f"Test 276 failed: got {result}, expected {True}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = isCleanPalindrome('あいいあ 1_x_x_x')
        assert result == True, f"Test 277 failed: got {result}, expected {True}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = isCleanPalindrome('1  1')
        assert result == True, f"Test 278 failed: got {result}, expected {True}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = isCleanPalindrome('été edge_x')
        assert result == False, f"Test 279 failed: got {result}, expected {False}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = isCleanPalindrome('été 1')
        assert result == True, f"Test 280 failed: got {result}, expected {True}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = isCleanPalindrome('x_0')
        assert result == True, f"Test 281 failed: got {result}, expected {True}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = isCleanPalindrome('x_x_car!')
        assert result == False, f"Test 282 failed: got {result}, expected {False}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = isCleanPalindrome('ro')
        assert result == False, f"Test 283 failed: got {result}, expected {False}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = isCleanPalindrome('x_été')
        assert result == False, f"Test 284 failed: got {result}, expected {False}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = isCleanPalindrome('été_x')
        assert result == False, f"Test 285 failed: got {result}, expected {False}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = isCleanPalindrome('0 !!!_x')
        assert result == True, f"Test 286 failed: got {result}, expected {True}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = isCleanPalindrome('no_x edge_x_x')
        assert result == False, f"Test 287 failed: got {result}, expected {False}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = isCleanPalindrome('Ésope reste ici et se repose 1')
        assert result == False, f"Test 288 failed: got {result}, expected {False}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = isCleanPalindrome('Ésope reste ici et se repose_x')
        assert result == False, f"Test 289 failed: got {result}, expected {False}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = isCleanPalindrome('esoper es te ici etser eposÉ')
        assert result == False, f"Test 290 failed: got {result}, expected {False}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = isCleanPalindrome('0 1 x_esoper es te ici etser eposÉ')
        assert result == False, f"Test 291 failed: got {result}, expected {False}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = isCleanPalindrome('tac')
        assert result == False, f"Test 292 failed: got {result}, expected {False}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = isCleanPalindrome('Ésope reste ici et se repose 0')
        assert result == False, f"Test 293 failed: got {result}, expected {False}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = isCleanPalindrome('repose_x')
        assert result == False, f"Test 294 failed: got {result}, expected {False}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = isCleanPalindrome('x_12321_x')
        assert result == True, f"Test 295 failed: got {result}, expected {True}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = isCleanPalindrome('0 арозА упал ан алапу азор А')
        assert result == True, f"Test 296 failed: got {result}, expected {True}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = isCleanPalindrome('0 palindrome 0')
        assert result == False, f"Test 297 failed: got {result}, expected {False}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = isCleanPalindrome('арозА упал ан алапу азор А 0')
        assert result == True, f"Test 298 failed: got {result}, expected {True}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = isCleanPalindrome('God?_x edge')
        assert result == False, f"Test 299 failed: got {result}, expected {False}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = isCleanPalindrome('.,,_x_x')
        assert result == True, f"Test 300 failed: got {result}, expected {True}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = isCleanPalindrome(' edge 1')
        assert result == False, f"Test 301 failed: got {result}, expected {False}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = isCleanPalindrome('🙂madam🙂 edge')
        assert result == False, f"Test 302 failed: got {result}, expected {False}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = isCleanPalindrome('can edge edge_x')
        assert result == False, f"Test 303 failed: got {result}, expected {False}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = isCleanPalindrome('egde 🙂madam🙂')
        assert result == False, f"Test 304 failed: got {result}, expected {False}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = isCleanPalindrome('OpenAI 1')
        assert result == False, f"Test 305 failed: got {result}, expected {False}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = isCleanPalindrome('x_egde abccba_x_x')
        assert result == False, f"Test 306 failed: got {result}, expected {False}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = isCleanPalindrome('x_🙂madam🙂')
        assert result == False, f"Test 307 failed: got {result}, expected {False}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = isCleanPalindrome('🙂madam🙂 1')
        assert result == True, f"Test 308 failed: got {result}, expected {True}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = isCleanPalindrome('Elba 1_x')
        assert result == False, f"Test 309 failed: got {result}, expected {False}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = isCleanPalindrome('Elba')
        assert result == False, f"Test 310 failed: got {result}, expected {False}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = isCleanPalindrome('Never_x')
        assert result == False, f"Test 311 failed: got {result}, expected {False}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = isCleanPalindrome('1 0 x_x_x_A man, a plan, a canal, Panama!')
        assert result == False, f"Test 312 failed: got {result}, expected {False}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = isCleanPalindrome('edge_x_x')
        assert result == False, f"Test 313 failed: got {result}, expected {False}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = isCleanPalindrome('seeb')
        assert result == False, f"Test 314 failed: got {result}, expected {False}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = isCleanPalindrome('x_egde ti_x')
        assert result == False, f"Test 315 failed: got {result}, expected {False}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = isCleanPalindrome('mad\x00am 0')
        assert result == True, f"Test 316 failed: got {result}, expected {True}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = isCleanPalindrome('\namanaP :lanac a\n,\rnalp a\n,\tnam A\n')
        assert result == True, f"Test 317 failed: got {result}, expected {True}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = isCleanPalindrome('\nA man\t,\na plan\r,\na canal: Panama\n_x')
        assert result == False, f"Test 318 failed: got {result}, expected {False}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = isCleanPalindrome('\nA man\t,\na plan\r,\na canal: Panama\n 1')
        assert result == True, f"Test 319 failed: got {result}, expected {True}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = isCleanPalindrome('egde x_\namanaP :lanac a\n,\rnalp a\n,\tnam A\n')
        assert result == False, f"Test 320 failed: got {result}, expected {False}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = isCleanPalindrome('А роза упала на лапу Азора_x edge edge_x')
        assert result == False, f"Test 321 failed: got {result}, expected {False}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = isCleanPalindrome('1 x_abccba')
        assert result == False, f"Test 322 failed: got {result}, expected {False}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = isCleanPalindrome('ba')
        assert result == False, f"Test 323 failed: got {result}, expected {False}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = isCleanPalindrome('in 0 0')
        assert result == False, f"Test 324 failed: got {result}, expected {False}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = isCleanPalindrome('eposÉ_x_x')
        assert result == False, f"Test 325 failed: got {result}, expected {False}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = isCleanPalindrome('abcba 0_x')
        assert result == False, f"Test 326 failed: got {result}, expected {False}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = isCleanPalindrome('áb́á_x_x 0')
        assert result == False, f"Test 327 failed: got {result}, expected {False}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = isCleanPalindrome('elbA edge')
        assert result == False, f"Test 328 failed: got {result}, expected {False}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = isCleanPalindrome('egde seeb')
        assert result == False, f"Test 329 failed: got {result}, expected {False}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = isCleanPalindrome('Able')
        assert result == False, f"Test 330 failed: got {result}, expected {False}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = isCleanPalindrome('x_seeb 1')
        assert result == False, f"Test 331 failed: got {result}, expected {False}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = isCleanPalindrome('x_𝔄b𝔄')
        assert result == False, f"Test 332 failed: got {result}, expected {False}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = isCleanPalindrome('𝔄b𝔄 0')
        assert result == True, f"Test 333 failed: got {result}, expected {True}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = isCleanPalindrome('𝔄b𝔄_x')
        assert result == False, f"Test 334 failed: got {result}, expected {False}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = isCleanPalindrome('x_A_x')
        assert result == True, f"Test 335 failed: got {result}, expected {True}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = isCleanPalindrome('see')
        assert result == False, f"Test 336 failed: got {result}, expected {False}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = isCleanPalindrome("x_.madA m'I ,madaM")
        assert result == False, f"Test 337 failed: got {result}, expected {False}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = isCleanPalindrome('nalp')
        assert result == False, f"Test 338 failed: got {result}, expected {False}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = isCleanPalindrome(' 0_x')
        assert result == True, f"Test 339 failed: got {result}, expected {True}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = isCleanPalindrome('oD')
        assert result == False, f"Test 340 failed: got {result}, expected {False}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = isCleanPalindrome('egde x_a_x_x')
        assert result == False, f"Test 341 failed: got {result}, expected {False}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = isCleanPalindrome('x_1 ')
        assert result == True, f"Test 342 failed: got {result}, expected {True}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = isCleanPalindrome('   _x edge')
        assert result == False, f"Test 343 failed: got {result}, expected {False}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = isCleanPalindrome('nolem on ,nomel oN')
        assert result == True, f"Test 344 failed: got {result}, expected {True}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = isCleanPalindrome('0 edge 0')
        assert result == False, f"Test 345 failed: got {result}, expected {False}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = isCleanPalindrome('А роза упала на лапу Азора 1')
        assert result == True, f"Test 346 failed: got {result}, expected {True}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
