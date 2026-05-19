# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def reverseString(s):
2: ✓     return s[::-1]
```

## Complete Test File

```python
def reverseString(s):
    return s[::-1]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = reverseString('hello')
        assert result == 'olleh', f"Test 1 failed: got {result}, expected {'olleh'}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = reverseString('a')
        assert result == 'a', f"Test 2 failed: got {result}, expected {'a'}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = reverseString('')
        assert result == '', f"Test 3 failed: got {result}, expected {''}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = reverseString('racecar')
        assert result == 'racecar', f"Test 4 failed: got {result}, expected {'racecar'}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = reverseString('Lean')
        assert result == 'naeL', f"Test 5 failed: got {result}, expected {'naeL'}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = reverseString('Lean4')
        assert result == '4naeL', f"Test 6 failed: got {result}, expected {'4naeL'}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = reverseString('  leading')
        assert result == 'gnidael  ', f"Test 7 failed: got {result}, expected {'gnidael  '}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = reverseString('trailing  ')
        assert result == '  gniliart', f"Test 8 failed: got {result}, expected {'  gniliart'}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = reverseString('  both  ')
        assert result == '  htob  ', f"Test 9 failed: got {result}, expected {'  htob  '}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = reverseString('line1\nline2')
        assert result == '2enil\n1enil', f"Test 10 failed: got {result}, expected {'2enil\n1enil'}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = reverseString('line1\r\nline2')
        assert result == '2enil\\n\\x0d1enil', f"Test 11 failed: got {result}, expected {'2enil\\n\\x0d1enil'}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = reverseString('hello, world!')
        assert result == '!dlrow ,olleh', f"Test 12 failed: got {result}, expected {'!dlrow ,olleh'}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = reverseString('1234567890')
        assert result == '0987654321', f"Test 13 failed: got {result}, expected {'0987654321'}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = reverseString('AaBbCcDdEe')
        assert result == 'eEdDcCbBaA', f"Test 14 failed: got {result}, expected {'eEdDcCbBaA'}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = reverseString('éclair')
        assert result == 'rialcé', f"Test 15 failed: got {result}, expected {'rialcé'}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = reverseString('你好，世界')
        assert result == '界世，好你', f"Test 16 failed: got {result}, expected {'界世，好你'}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = reverseString('こんにちは世界')
        assert result == '界世はちにんこ', f"Test 17 failed: got {result}, expected {'界世はちにんこ'}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = reverseString('안녕하세요')
        assert result == '요세하녕안', f"Test 18 failed: got {result}, expected {'요세하녕안'}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = reverseString('مرحبا')
        assert result == 'ابحرم', f"Test 19 failed: got {result}, expected {'ابحرم'}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = reverseString('שלום')
        assert result == 'םולש', f"Test 20 failed: got {result}, expected {'םולש'}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = reverseString('नमस्ते')
        assert result == 'ेत्समन', f"Test 21 failed: got {result}, expected {'ेत्समन'}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = reverseString('👨\u200d👩\u200d👧\u200d👦')
        assert result == '👦\u200d👧\u200d👩\u200d👨', f"Test 22 failed: got {result}, expected {'👦\u200d👧\u200d👩\u200d👨'}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = reverseString('𝄞music')
        assert result == 'cisum𝄞', f"Test 23 failed: got {result}, expected {'cisum𝄞'}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = reverseString('"quoted" and \\backslash\\')
        assert result == '\\hsalskcab\\ dna "detouq"', f"Test 24 failed: got {result}, expected {'\\hsalskcab\\ dna "detouq"'}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = reverseString('{ "key": [1, 2, 3] }')
        assert result == '} ]3 ,2 ,1[ :"yek" {', f"Test 25 failed: got {result}, expected {'} ]3 ,2 ,1[ :"yek" {'}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = reverseString('\x00null-byte')
        assert result == 'etyb-llun\\x00', f"Test 26 failed: got {result}, expected {'etyb-llun\\x00'}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = reverseString('control-\x01-\x02-end')
        assert result == 'dne-\\x02-\\x01-lortnoc', f"Test 27 failed: got {result}, expected {'dne-\\x02-\\x01-lortnoc'}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = reverseString('\u200fabc')
        assert result == 'cba\u200f', f"Test 28 failed: got {result}, expected {'cba\u200f'}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = reverseString('Z̶͑͗ͣ̓ͪͫ͊̚a̷l̵g̡o̴')
        assert result == '̴o̡g̵l̷a̶͊ͫͪ̓ͣ͗͑̚Z', f"Test 29 failed: got {result}, expected {'̴o̡g̵l̷a̶͊ͫͪ̓ͣ͗͑̚Z'}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = reverseString('a̐éö̲')
        assert result == '̲̈óe̐a', f"Test 30 failed: got {result}, expected {'̲̈óe̐a'}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = reverseString('hello_x')
        assert result == 'x_olleh', f"Test 31 failed: got {result}, expected {'x_olleh'}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = reverseString('world!')
        assert result == '!dlrow', f"Test 32 failed: got {result}, expected {'!dlrow'}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = reverseString('olleh')
        assert result == 'hello', f"Test 33 failed: got {result}, expected {'hello'}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = reverseString('hello 0')
        assert result == '0 olleh', f"Test 34 failed: got {result}, expected {'0 olleh'}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = reverseString('olleh_x')
        assert result == 'x_hello', f"Test 35 failed: got {result}, expected {'x_hello'}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = reverseString('[1, 1_x')
        assert result == 'x_1 ,1[', f"Test 36 failed: got {result}, expected {'x_1 ,1['}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = reverseString('0 hello')
        assert result == 'olleh 0', f"Test 37 failed: got {result}, expected {'olleh 0'}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = reverseString('x_\n 0')
        assert result == '0 \n_x', f"Test 38 failed: got {result}, expected {'0 \n_x'}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = reverseString('\\backslash\\')
        assert result == '\\hsalskcab\\', f"Test 39 failed: got {result}, expected {'\\hsalskcab\\'}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = reverseString('leading')
        assert result == 'gnidael', f"Test 40 failed: got {result}, expected {'gnidael'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = reverseString('a_x')
        assert result == 'x_a', f"Test 41 failed: got {result}, expected {'x_a'}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = reverseString('world! edge')
        assert result == 'egde !dlrow', f"Test 42 failed: got {result}, expected {'egde !dlrow'}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = reverseString('hello,')
        assert result == ',olleh', f"Test 43 failed: got {result}, expected {',olleh'}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = reverseString('a_x 0 1_x')
        assert result == 'x_1 0 x_a', f"Test 44 failed: got {result}, expected {'x_1 0 x_a'}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = reverseString('界世はちにんこ')
        assert result == 'こんにちは世界', f"Test 45 failed: got {result}, expected {'こんにちは世界'}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = reverseString(' 1_x')
        assert result == 'x_1 ', f"Test 46 failed: got {result}, expected {'x_1 '}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = reverseString('egde ')
        assert result == ' edge', f"Test 47 failed: got {result}, expected {' edge'}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = reverseString('x__x_x')
        assert result == 'x_x__x', f"Test 48 failed: got {result}, expected {'x_x__x'}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = reverseString('\u200b edge')
        assert result == 'egde \u200b', f"Test 49 failed: got {result}, expected {'egde \u200b'}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = reverseString('שלום_x')
        assert result == 'x_םולש', f"Test 50 failed: got {result}, expected {'x_םולש'}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = reverseString('racecar 1')
        assert result == '1 racecar', f"Test 51 failed: got {result}, expected {'1 racecar'}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = reverseString('racecar edge')
        assert result == 'egde racecar', f"Test 52 failed: got {result}, expected {'egde racecar'}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = reverseString('egde racecar 1')
        assert result == '1 racecar edge', f"Test 53 failed: got {result}, expected {'1 racecar edge'}"
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
