# Coverage Report

Total executable lines: 14
Covered lines: 14
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def runLengthEncode(s):
2: ✓     if not s:
3: ✓         return []
4: ✓     result = []
5: ✓     current = s[0]
6: ✓     count = 1
7: ✓     for char in s[1:]:
8: ✓         if char == current:
9: ✓             count += 1
10:           else:
11: ✓             result.append((current, count))
12: ✓             current = char
13: ✓             count = 1
14: ✓     result.append((current, count))
15: ✓     return result
```

## Complete Test File

```python
def runLengthEncode(s):
    if not s:
        return []
    result = []
    current = s[0]
    count = 1
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            result.append((current, count))
            current = char
            count = 1
    result.append((current, count))
    return result

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = runLengthEncode('')
        assert result == [], f"Test 1 failed: got {result}, expected {[]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = runLengthEncode('aaa')
        assert result == [('a', 3)], f"Test 2 failed: got {result}, expected {[('a', 3)]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = runLengthEncode('abbbcccaa')
        assert result == [('a', 1), ('b', 3), ('c', 3), ('a', 2)], f"Test 3 failed: got {result}, expected {[('a', 1), ('b', 3), ('c', 3), ('a', 2)]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = runLengthEncode('xyz')
        assert result == [('x', 1), ('y', 1), ('z', 1)], f"Test 4 failed: got {result}, expected {[('x', 1), ('y', 1), ('z', 1)]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = runLengthEncode('aabbaa')
        assert result == [('a', 2), ('b', 2), ('a', 2)], f"Test 5 failed: got {result}, expected {[('a', 2), ('b', 2), ('a', 2)]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = runLengthEncode('aaaabbbccdaa')
        assert result == [('a', 4), ('b', 3), ('c', 2), ('d', 1), ('a', 2)], f"Test 6 failed: got {result}, expected {[('a', 4), ('b', 3), ('c', 2), ('d', 1), ('a', 2)]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = runLengthEncode('1111223331')
        assert result == [('1', 4), ('2', 2), ('3', 3), ('1', 1)], f"Test 7 failed: got {result}, expected {[('1', 4), ('2', 2), ('3', 3), ('1', 1)]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = runLengthEncode('AAaaBBbb')
        assert result == [('A', 2), ('a', 2), ('B', 2), ('b', 2)], f"Test 8 failed: got {result}, expected {[('A', 2), ('a', 2), ('B', 2), ('b', 2)]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = runLengthEncode('a  b')
        assert result == [('a', 1), (' ', 2), ('b', 1)], f"Test 9 failed: got {result}, expected {[('a', 1), (' ', 2), ('b', 1)]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = runLengthEncode('\t\tabc\t')
        assert result == [('\t', 2), ('a', 1), ('b', 1), ('c', 1), ('\t', 1)], f"Test 10 failed: got {result}, expected {[('\t', 2), ('a', 1), ('b', 1), ('c', 1), ('\t', 1)]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = runLengthEncode('😊😊😊😢😢a')
        assert result == [('😊', 3), ('😢', 2), ('a', 1)], f"Test 11 failed: got {result}, expected {[('😊', 3), ('😢', 2), ('a', 1)]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = runLengthEncode('🍎🍎🍏🍏🍏')
        assert result == [('🍎', 2), ('🍏', 3)], f"Test 12 failed: got {result}, expected {[('🍎', 2), ('🍏', 3)]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = runLengthEncode('汉汉字字字')
        assert result == [('汉', 2), ('字', 3)], f"Test 13 failed: got {result}, expected {[('汉', 2), ('字', 3)]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = runLengthEncode('a\x00a\x00\x00')
        assert result == [('a', 1), ('\x00', 1), ('a', 1), ('\x00', 2)], f"Test 14 failed: got {result}, expected {[('a', 1), ('\x00', 1), ('a', 1), ('\x00', 2)]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = runLengthEncode('!@##$$$%%%^^^&&&*')
        assert result == [('!', 1), ('@', 1), ('#', 2), ('$', 3), ('%', 3), ('^', 3), ('&', 3), ('*', 1)], f"Test 15 failed: got {result}, expected {[('!', 1), ('@', 1), ('#', 2), ('$', 3), ('%', 3), ('^', 3), ('&', 3), ('*', 1)]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = runLengthEncode('abcccccccccccd')
        assert result == [('a', 1), ('b', 1), ('c', 11), ('d', 1)], f"Test 16 failed: got {result}, expected {[('a', 1), ('b', 1), ('c', 11), ('d', 1)]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = runLengthEncode('ااا ب')
        assert result == [('ا', 3), (' ', 1), ('ب', 1)], f"Test 17 failed: got {result}, expected {[('ا', 3), (' ', 1), ('ب', 1)]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = runLengthEncode('ΓΓγγΓ')
        assert result == [('Γ', 2), ('γ', 2), ('Γ', 1)], f"Test 18 failed: got {result}, expected {[('Γ', 2), ('γ', 2), ('Γ', 1)]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = runLengthEncode('끝끝끝시작')
        assert result == [('끝', 3), ('시', 1), ('작', 1)], f"Test 19 failed: got {result}, expected {[('끝', 3), ('시', 1), ('작', 1)]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = runLengthEncode('abbaaaaccbbbba')
        assert result == [('a', 1), ('b', 2), ('a', 4), ('c', 2), ('b', 4), ('a', 1)], f"Test 20 failed: got {result}, expected {[('a', 1), ('b', 2), ('a', 4), ('c', 2), ('b', 4), ('a', 1)]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = runLengthEncode('xYZZZZYx')
        assert result == [('x', 1), ('Y', 1), ('Z', 4), ('Y', 1), ('x', 1)], f"Test 21 failed: got {result}, expected {[('x', 1), ('Y', 1), ('Z', 4), ('Y', 1), ('x', 1)]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = runLengthEncode('a\nb\n\nb\na')
        assert result == [('a', 1), ('\n', 1), ('b', 1), ('\n', 2), ('b', 1), ('\n', 1), ('a', 1)], f"Test 22 failed: got {result}, expected {[('a', 1), ('\n', 1), ('b', 1), ('\n', 2), ('b', 1), ('\n', 1), ('a', 1)]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = runLengthEncode('""\'\'')
        assert result == '[(\'\\"\', 2), (\'\'\', 2)]', f"Test 23 failed: got {result}, expected {'[(\'\\"\', 2), (\'\'\', 2)]'}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = runLengthEncode('a  b edge_x')
        assert result == [('a', 1), (' ', 2), ('b', 1), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1), ('_', 1), ('x', 1)], f"Test 24 failed: got {result}, expected {[('a', 1), (' ', 2), ('b', 1), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1), ('_', 1), ('x', 1)]}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = runLengthEncode('!@##$$$%%%^^^&&&*_x')
        assert result == [('!', 1), ('@', 1), ('#', 2), ('$', 3), ('%', 3), ('^', 3), ('&', 3), ('*', 1), ('_', 1), ('x', 1)], f"Test 25 failed: got {result}, expected {[('!', 1), ('@', 1), ('#', 2), ('$', 3), ('%', 3), ('^', 3), ('&', 3), ('*', 1), ('_', 1), ('x', 1)]}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = runLengthEncode('aaa edge_x')
        assert result == [('a', 3), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1), ('_', 1), ('x', 1)], f"Test 26 failed: got {result}, expected {[('a', 3), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1), ('_', 1), ('x', 1)]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = runLengthEncode('aaa_x')
        assert result == [('a', 3), ('_', 1), ('x', 1)], f"Test 27 failed: got {result}, expected {[('a', 3), ('_', 1), ('x', 1)]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = runLengthEncode('a  b_x')
        assert result == [('a', 1), (' ', 2), ('b', 1), ('_', 1), ('x', 1)], f"Test 28 failed: got {result}, expected {[('a', 1), (' ', 2), ('b', 1), ('_', 1), ('x', 1)]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = runLengthEncode('1 aacccbbba')
        assert result == [('1', 1), (' ', 1), ('a', 2), ('c', 3), ('b', 3), ('a', 1)], f"Test 29 failed: got {result}, expected {[('1', 1), (' ', 1), ('a', 2), ('c', 3), ('b', 3), ('a', 1)]}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = runLengthEncode('aacccbbba_x edge')
        assert result == [('a', 2), ('c', 3), ('b', 3), ('a', 1), ('_', 1), ('x', 1), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)], f"Test 30 failed: got {result}, expected {[('a', 2), ('c', 3), ('b', 3), ('a', 1), ('_', 1), ('x', 1), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = runLengthEncode('\\\\_x')
        assert result == [('\\', 2), ('_', 1), ('x', 1)], f"Test 31 failed: got {result}, expected {[('\\', 2), ('_', 1), ('x', 1)]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = runLengthEncode('abbbcccaa 1')
        assert result == [('a', 1), ('b', 3), ('c', 3), ('a', 2), (' ', 1), ('1', 1)], f"Test 32 failed: got {result}, expected {[('a', 1), ('b', 3), ('c', 3), ('a', 2), (' ', 1), ('1', 1)]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = runLengthEncode('abbbcccaa 1 1')
        assert result == [('a', 1), ('b', 3), ('c', 3), ('a', 2), (' ', 1), ('1', 1), (' ', 1), ('1', 1)], f"Test 33 failed: got {result}, expected {[('a', 1), ('b', 3), ('c', 3), ('a', 2), (' ', 1), ('1', 1), (' ', 1), ('1', 1)]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = runLengthEncode('ااا_x')
        assert result == [('ا', 3), ('_', 1), ('x', 1)], f"Test 34 failed: got {result}, expected {[('ا', 3), ('_', 1), ('x', 1)]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = runLengthEncode('abbbcccaa_x')
        assert result == [('a', 1), ('b', 3), ('c', 3), ('a', 2), ('_', 1), ('x', 1)], f"Test 35 failed: got {result}, expected {[('a', 1), ('b', 3), ('c', 3), ('a', 2), ('_', 1), ('x', 1)]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = runLengthEncode('汉汉字字字 edge')
        assert result == [('汉', 2), ('字', 3), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)], f"Test 36 failed: got {result}, expected {[('汉', 2), ('字', 3), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = runLengthEncode('egde x_aa_x')
        assert result == [('e', 1), ('g', 1), ('d', 1), ('e', 1), (' ', 1), ('x', 1), ('_', 1), ('a', 2), ('_', 1), ('x', 1)], f"Test 37 failed: got {result}, expected {[('e', 1), ('g', 1), ('d', 1), ('e', 1), (' ', 1), ('x', 1), ('_', 1), ('a', 2), ('_', 1), ('x', 1)]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = runLengthEncode('汉汉字字字_x')
        assert result == [('汉', 2), ('字', 3), ('_', 1), ('x', 1)], f"Test 38 failed: got {result}, expected {[('汉', 2), ('字', 3), ('_', 1), ('x', 1)]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = runLengthEncode('aa_x')
        assert result == [('a', 2), ('_', 1), ('x', 1)], f"Test 39 failed: got {result}, expected {[('a', 2), ('_', 1), ('x', 1)]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = runLengthEncode('aa 0')
        assert result == [('a', 2), (' ', 1), ('0', 1)], f"Test 40 failed: got {result}, expected {[('a', 2), (' ', 1), ('0', 1)]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = runLengthEncode('ééé_x_x 1')
        assert result == [('é', 3), ('_', 1), ('x', 1), ('_', 1), ('x', 1), (' ', 1), ('1', 1)], f"Test 41 failed: got {result}, expected {[('é', 3), ('_', 1), ('x', 1), ('_', 1), ('x', 1), (' ', 1), ('1', 1)]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = runLengthEncode('ééé_x_x')
        assert result == [('é', 3), ('_', 1), ('x', 1), ('_', 1), ('x', 1)], f"Test 42 failed: got {result}, expected {[('é', 3), ('_', 1), ('x', 1), ('_', 1), ('x', 1)]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = runLengthEncode('x_x__x')
        assert result == [('x', 1), ('_', 1), ('x', 1), ('_', 2), ('x', 1)], f"Test 43 failed: got {result}, expected {[('x', 1), ('_', 1), ('x', 1), ('_', 2), ('x', 1)]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = runLengthEncode('aaaabbbccdaa edge')
        assert result == [('a', 4), ('b', 3), ('c', 2), ('d', 1), ('a', 2), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)], f"Test 44 failed: got {result}, expected {[('a', 4), ('b', 3), ('c', 2), ('d', 1), ('a', 2), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = runLengthEncode('aadccbbbaaaa 1_x')
        assert result == [('a', 2), ('d', 1), ('c', 2), ('b', 3), ('a', 4), (' ', 1), ('1', 1), ('_', 1), ('x', 1)], f"Test 45 failed: got {result}, expected {[('a', 2), ('d', 1), ('c', 2), ('b', 3), ('a', 4), (' ', 1), ('1', 1), ('_', 1), ('x', 1)]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = runLengthEncode('aadccbbbaaaa_x')
        assert result == [('a', 2), ('d', 1), ('c', 2), ('b', 3), ('a', 4), ('_', 1), ('x', 1)], f"Test 46 failed: got {result}, expected {[('a', 2), ('d', 1), ('c', 2), ('b', 3), ('a', 4), ('_', 1), ('x', 1)]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = runLengthEncode('x_aa_x')
        assert result == [('x', 1), ('_', 1), ('a', 2), ('_', 1), ('x', 1)], f"Test 47 failed: got {result}, expected {[('x', 1), ('_', 1), ('a', 2), ('_', 1), ('x', 1)]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = runLengthEncode('aaaabbbccdaa 1 edge')
        assert result == [('a', 4), ('b', 3), ('c', 2), ('d', 1), ('a', 2), (' ', 1), ('1', 1), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)], f"Test 48 failed: got {result}, expected {[('a', 4), ('b', 3), ('c', 2), ('d', 1), ('a', 2), (' ', 1), ('1', 1), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = runLengthEncode('x_1333221111')
        assert result == [('x', 1), ('_', 1), ('1', 1), ('3', 3), ('2', 2), ('1', 4)], f"Test 49 failed: got {result}, expected {[('x', 1), ('_', 1), ('1', 1), ('3', 3), ('2', 2), ('1', 4)]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = runLengthEncode('egde  0')
        assert result == [('e', 1), ('g', 1), ('d', 1), ('e', 1), (' ', 2), ('0', 1)], f"Test 50 failed: got {result}, expected {[('e', 1), ('g', 1), ('d', 1), ('e', 1), (' ', 2), ('0', 1)]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = runLengthEncode('aaa edge_x 1')
        assert result == [('a', 3), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1), ('_', 1), ('x', 1), (' ', 1), ('1', 1)], f"Test 51 failed: got {result}, expected {[('a', 3), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1), ('_', 1), ('x', 1), (' ', 1), ('1', 1)]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = runLengthEncode('x_1333221111 edge')
        assert result == [('x', 1), ('_', 1), ('1', 1), ('3', 3), ('2', 2), ('1', 4), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)], f"Test 52 failed: got {result}, expected {[('x', 1), ('_', 1), ('1', 1), ('3', 3), ('2', 2), ('1', 4), (' ', 1), ('e', 1), ('d', 1), ('g', 1), ('e', 1)]}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = runLengthEncode('bbBBaaAA')
        assert result == [('b', 2), ('B', 2), ('a', 2), ('A', 2)], f"Test 53 failed: got {result}, expected {[('b', 2), ('B', 2), ('a', 2), ('A', 2)]}"
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
