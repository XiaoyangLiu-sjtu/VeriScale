# Coverage Report

Total executable lines: 16
Covered lines: 16
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def runLengthEncoder(input):
2: ✓     if not input:
3: ✓         return ""
4: ✓     encoded = []
5: ✓     count = 1
6: ✓     current = input[0]
7: ✓     for char in input[1:]:
8: ✓         if char == current:
9: ✓             count += 1
10:           else:
11: ✓             encoded.append(current)
12: ✓             encoded.append(str(count))
13: ✓             current = char
14: ✓             count = 1
15: ✓     encoded.append(current)
16: ✓     encoded.append(str(count))
17: ✓     return "".join(encoded)
```

## Complete Test File

```python
def runLengthEncoder(input):
    if not input:
        return ""
    encoded = []
    count = 1
    current = input[0]
    for char in input[1:]:
        if char == current:
            count += 1
        else:
            encoded.append(current)
            encoded.append(str(count))
            current = char
            count = 1
    encoded.append(current)
    encoded.append(str(count))
    return "".join(encoded)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = runLengthEncoder('aaabbbcc')
        assert result == 'a3b3c2', f"Test 1 failed: got {result}, expected {'a3b3c2'}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = runLengthEncoder('!!!$$$%%%')
        assert result == '!3$3%3', f"Test 2 failed: got {result}, expected {'!3$3%3'}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = runLengthEncoder('aaaaa')
        assert result == 'a5', f"Test 3 failed: got {result}, expected {'a5'}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = runLengthEncoder('abcd')
        assert result == 'a1b1c1d1', f"Test 4 failed: got {result}, expected {'a1b1c1d1'}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = runLengthEncoder('')
        assert result == '', f"Test 5 failed: got {result}, expected {''}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = runLengthEncoder('AaABb')
        assert result == 'A1a1A1B1b1', f"Test 6 failed: got {result}, expected {'A1a1A1B1b1'}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = runLengthEncoder('wwwwwwwwwwwwwwwww')
        assert result == 'w17', f"Test 7 failed: got {result}, expected {'w17'}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = runLengthEncoder('a')
        assert result == 'a1', f"Test 8 failed: got {result}, expected {'a1'}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = runLengthEncoder('  ')
        assert result == ' 2', f"Test 9 failed: got {result}, expected {' 2'}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = runLengthEncoder('aaaaaa')
        assert result == 'a6', f"Test 10 failed: got {result}, expected {'a6'}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = runLengthEncoder('AaAaAAaa')
        assert result == 'A1a1A1a1A2a2', f"Test 11 failed: got {result}, expected {'A1a1A1a1A2a2'}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = runLengthEncoder('   ')
        assert result == ' 3', f"Test 12 failed: got {result}, expected {' 3'}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = runLengthEncoder('\t\t\t')
        assert result == '\t3', f"Test 13 failed: got {result}, expected {'\t3'}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = runLengthEncoder('\n\n\n')
        assert result == '\n3', f"Test 14 failed: got {result}, expected {'\n3'}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = runLengthEncoder('aabccccccccccdde')
        assert result == 'a2b1c10d2e1', f"Test 15 failed: got {result}, expected {'a2b1c10d2e1'}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = runLengthEncoder('xyzzy')
        assert result == 'x1y1z2y1', f"Test 16 failed: got {result}, expected {'x1y1z2y1'}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = runLengthEncoder('🙂🙂🙃🙃🙃')
        assert result == '🙂2🙃3', f"Test 17 failed: got {result}, expected {'🙂2🙃3'}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = runLengthEncoder('éééèê')
        assert result == 'é3è1ê1', f"Test 18 failed: got {result}, expected {'é3è1ê1'}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = runLengthEncoder('ααββγγγ')
        assert result == 'α2β2γ3', f"Test 19 failed: got {result}, expected {'α2β2γ3'}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = runLengthEncoder('汉汉字字字')
        assert result == '汉2字3', f"Test 20 failed: got {result}, expected {'汉2字3'}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = runLengthEncoder('~~@@@###***')
        assert result == '~2@3#3*3', f"Test 21 failed: got {result}, expected {'~2@3#3*3'}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = runLengthEncoder('abababab')
        assert result == 'a1b1a1b1a1b1a1b1', f"Test 22 failed: got {result}, expected {'a1b1a1b1a1b1a1b1'}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = runLengthEncoder('zzzzzzzzzzzzzzzzzzzz')
        assert result == 'z20', f"Test 23 failed: got {result}, expected {'z20'}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = runLengthEncoder('qwertyuiopasdfghjklzxcvbnm')
        assert result == 'q1w1e1r1t1y1u1i1o1p1a1s1d1f1g1h1j1k1l1z1x1c1v1b1n1m1', f"Test 24 failed: got {result}, expected {'q1w1e1r1t1y1u1i1o1p1a1s1d1f1g1h1j1k1l1z1x1c1v1b1n1m1'}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = runLengthEncoder('QWERTY')
        assert result == 'Q1W1E1R1T1Y1', f"Test 25 failed: got {result}, expected {'Q1W1E1R1T1Y1'}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = runLengthEncoder('mixedCASEwithNoDigits')
        assert result == 'm1i1x1e1d1C1A1S1E1w1i1t1h1N1o1D1i1g1i1t1s1', f"Test 26 failed: got {result}, expected {'m1i1x1e1d1C1A1S1E1w1i1t1h1N1o1D1i1g1i1t1s1'}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = runLengthEncoder('___---___')
        assert result == '_3-3_3', f"Test 27 failed: got {result}, expected {'_3-3_3'}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = runLengthEncoder('.,;:!?.,;:!?')
        assert result == '.1,1;1:1!1?1.1,1;1:1!1?1', f"Test 28 failed: got {result}, expected {'.1,1;1:1!1?1.1,1;1:1!1?1'}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = runLengthEncoder('((((()))))')
        assert result == '(5)5', f"Test 29 failed: got {result}, expected {'(5)5'}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = runLengthEncoder('a a a   b b')
        assert result == 'a1 1a1 1a1 3b1 1b1', f"Test 30 failed: got {result}, expected {'a1 1a1 1a1 3b1 1b1'}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = runLengthEncoder('line\nbreak\ntest')
        assert result == 'l1i1n1e1\n1b1r1e1a1k1\n1t1e1s1t1', f"Test 31 failed: got {result}, expected {'l1i1n1e1\n1b1r1e1a1k1\n1t1e1s1t1'}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = runLengthEncoder('tab\tseparated\ttext')
        assert result == 't1a1b1\t1s1e1p1a1r1a1t1e1d1\t1t1e1x1t1', f"Test 32 failed: got {result}, expected {'t1a1b1\t1s1e1p1a1r1a1t1e1d1\t1t1e1x1t1'}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = runLengthEncoder('""\'\'')
        assert result == '"2\'2', f"Test 33 failed: got {result}, expected {'"2\'2'}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = runLengthEncoder('back\\slash')
        assert result == 'b1a1c1k1\\1s1l1a1s1h1', f"Test 34 failed: got {result}, expected {'b1a1c1k1\\1s1l1a1s1h1'}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = runLengthEncoder('😀😀😀😀😀')
        assert result == '😀5', f"Test 35 failed: got {result}, expected {'😀5'}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = runLengthEncoder('end.')
        assert result == 'e1n1d1.1', f"Test 36 failed: got {result}, expected {'e1n1d1.1'}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = runLengthEncoder('aaabbbcc_x')
        assert result == 'a3b3c2_1x1', f"Test 37 failed: got {result}, expected {'a3b3c2_1x1'}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = runLengthEncoder('ccbbbaaa')
        assert result == 'c2b3a3', f"Test 38 failed: got {result}, expected {'c2b3a3'}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = runLengthEncoder('ccbbbaaa_x')
        assert result == 'c2b3a3_1x1', f"Test 39 failed: got {result}, expected {'c2b3a3_1x1'}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = runLengthEncoder('line edge_x')
        assert result == 'l1i1n1e1 1e1d1g1e1_1x1', f"Test 40 failed: got {result}, expected {'l1i1n1e1 1e1d1g1e1_1x1'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = runLengthEncoder('AaAaAAaa edge')
        assert result == 'A1a1A1a1A2a2 1e1d1g1e1', f"Test 41 failed: got {result}, expected {'A1a1A1a1A2a2 1e1d1g1e1'}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = runLengthEncoder('!!!$$$%%%_x')
        assert result == '!3$3%3_1x1', f"Test 42 failed: got {result}, expected {'!3$3%3_1x1'}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = runLengthEncoder('%%%$$$!!!')
        assert result == '%3$3!3', f"Test 43 failed: got {result}, expected {'%3$3!3'}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = runLengthEncoder('mnbvcxzlkjhgfdsapoiuytrewq')
        assert result == 'm1n1b1v1c1x1z1l1k1j1h1g1f1d1s1a1p1o1i1u1y1t1r1e1w1q1', f"Test 44 failed: got {result}, expected {'m1n1b1v1c1x1z1l1k1j1h1g1f1d1s1a1p1o1i1u1y1t1r1e1w1q1'}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = runLengthEncoder('line')
        assert result == 'l1i1n1e1', f"Test 45 failed: got {result}, expected {'l1i1n1e1'}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = runLengthEncoder('egde aaaaa')
        assert result == 'e1g1d1e1 1a5', f"Test 46 failed: got {result}, expected {'e1g1d1e1 1a5'}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = runLengthEncoder('x_aaaaa_x_x')
        assert result == 'x1_1a5_1x1_1x1', f"Test 47 failed: got {result}, expected {'x1_1a5_1x1_1x1'}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = runLengthEncoder('aaaaa_x')
        assert result == 'a5_1x1', f"Test 48 failed: got {result}, expected {'a5_1x1'}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = runLengthEncoder('_x')
        assert result == '_1x1', f"Test 49 failed: got {result}, expected {'_1x1'}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = runLengthEncoder('mnbvcxzlkjhgfdsapoiuytrewq edge')
        assert result == 'm1n1b1v1c1x1z1l1k1j1h1g1f1d1s1a1p1o1i1u1y1t1r1e1w1q1 1e1d1g1e1', f"Test 50 failed: got {result}, expected {'m1n1b1v1c1x1z1l1k1j1h1g1f1d1s1a1p1o1i1u1y1t1r1e1w1q1 1e1d1g1e1'}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = runLengthEncoder('b')
        assert result == 'b1', f"Test 51 failed: got {result}, expected {'b1'}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
