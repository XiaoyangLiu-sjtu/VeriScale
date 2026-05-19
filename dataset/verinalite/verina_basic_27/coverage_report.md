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
        result = findFirstRepeatedChar('🙂🙃😉')
        assert result == None, f"Test 9 failed: got {result}, expected {None}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = findFirstRepeatedChar('abc ABC abc')
        assert result == ' ', f"Test 10 failed: got {result}, expected {' '}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = findFirstRepeatedChar('xyzXYZ')
        assert result == None, f"Test 11 failed: got {result}, expected {None}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = findFirstRepeatedChar('qwerty')
        assert result == None, f"Test 12 failed: got {result}, expected {None}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = findFirstRepeatedChar('uniq')
        assert result == None, f"Test 13 failed: got {result}, expected {None}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = findFirstRepeatedChar('0')
        assert result == None, f"Test 14 failed: got {result}, expected {None}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = findFirstRepeatedChar('01')
        assert result == None, f"Test 15 failed: got {result}, expected {None}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = findFirstRepeatedChar(' 0')
        assert result == None, f"Test 16 failed: got {result}, expected {None}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = findFirstRepeatedChar('0 ')
        assert result == None, f"Test 17 failed: got {result}, expected {None}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = findFirstRepeatedChar('1 _x')
        assert result == None, f"Test 18 failed: got {result}, expected {None}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = findFirstRepeatedChar('abcdef_x')
        assert result == None, f"Test 19 failed: got {result}, expected {None}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = findFirstRepeatedChar('x_ 1')
        assert result == None, f"Test 20 failed: got {result}, expected {None}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = findFirstRepeatedChar(' 1_x')
        assert result == None, f"Test 21 failed: got {result}, expected {None}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = findFirstRepeatedChar('x_ccbbaa_x_x')
        assert result == 'c', f"Test 22 failed: got {result}, expected {'c'}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = findFirstRepeatedChar('_x')
        assert result == None, f"Test 23 failed: got {result}, expected {None}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = findFirstRepeatedChar(' 1')
        assert result == None, f"Test 24 failed: got {result}, expected {None}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = findFirstRepeatedChar('x_')
        assert result == None, f"Test 25 failed: got {result}, expected {None}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = findFirstRepeatedChar('x_ccbbaa_x_x 1')
        assert result == 'c', f"Test 26 failed: got {result}, expected {'c'}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = findFirstRepeatedChar('Aa_x')
        assert result == None, f"Test 27 failed: got {result}, expected {None}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = findFirstRepeatedChar('aA')
        assert result == None, f"Test 28 failed: got {result}, expected {None}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = findFirstRepeatedChar('aA 0')
        assert result == None, f"Test 29 failed: got {result}, expected {None}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = findFirstRepeatedChar('a 0')
        assert result == None, f"Test 30 failed: got {result}, expected {None}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = findFirstRepeatedChar('x_0 a')
        assert result == None, f"Test 31 failed: got {result}, expected {None}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = findFirstRepeatedChar('x_0 a_x')
        assert result == '_', f"Test 32 failed: got {result}, expected {'_'}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = findFirstRepeatedChar('a_x')
        assert result == None, f"Test 33 failed: got {result}, expected {None}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = findFirstRepeatedChar('x_a_x')
        assert result == '_', f"Test 34 failed: got {result}, expected {'_'}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = findFirstRepeatedChar('x_0')
        assert result == None, f"Test 35 failed: got {result}, expected {None}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = findFirstRepeatedChar('aA_x')
        assert result == None, f"Test 36 failed: got {result}, expected {None}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = findFirstRepeatedChar('ba 1_x')
        assert result == None, f"Test 37 failed: got {result}, expected {None}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = findFirstRepeatedChar('🙂🙃😉_x')
        assert result == None, f"Test 38 failed: got {result}, expected {None}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = findFirstRepeatedChar('x_1')
        assert result == None, f"Test 39 failed: got {result}, expected {None}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = findFirstRepeatedChar('x_a 0_x')
        assert result == '_', f"Test 40 failed: got {result}, expected {'_'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = findFirstRepeatedChar('abc')
        assert result == None, f"Test 41 failed: got {result}, expected {None}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = findFirstRepeatedChar('1 ')
        assert result == None, f"Test 42 failed: got {result}, expected {None}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = findFirstRepeatedChar('x_a_x_x_x')
        assert result == '_', f"Test 43 failed: got {result}, expected {'_'}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = findFirstRepeatedChar('_x 1')
        assert result == None, f"Test 44 failed: got {result}, expected {None}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = findFirstRepeatedChar('Aa_x 0')
        assert result == None, f"Test 45 failed: got {result}, expected {None}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = findFirstRepeatedChar('01_x')
        assert result == None, f"Test 46 failed: got {result}, expected {None}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = findFirstRepeatedChar('1_x')
        assert result == None, f"Test 47 failed: got {result}, expected {None}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = findFirstRepeatedChar(' 0_x')
        assert result == None, f"Test 48 failed: got {result}, expected {None}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = findFirstRepeatedChar('10')
        assert result == None, f"Test 49 failed: got {result}, expected {None}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = findFirstRepeatedChar('abcdef_x edge_x')
        assert result == 'e', f"Test 50 failed: got {result}, expected {'e'}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = findFirstRepeatedChar('1')
        assert result == None, f"Test 51 failed: got {result}, expected {None}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = findFirstRepeatedChar('x__x')
        assert result == '_', f"Test 52 failed: got {result}, expected {'_'}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = findFirstRepeatedChar('uniq 0')
        assert result == None, f"Test 53 failed: got {result}, expected {None}"
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
