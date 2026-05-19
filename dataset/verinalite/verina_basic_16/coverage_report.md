# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def replaceChars(s, oldChar, newChar):
2: ✓     return ''.join(newChar if ch == oldChar else ch for ch in s)
```

## Complete Test File

```python
def replaceChars(s, oldChar, newChar):
    return ''.join(newChar if ch == oldChar else ch for ch in s)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = replaceChars('hello, world!', ',', ';')
        assert result == 'hello; world!', f"Test 1 failed: got {result}, expected {'hello; world!'}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = replaceChars('a,b.c', ',', ':')
        assert result == 'a:b.c', f"Test 2 failed: got {result}, expected {'a:b.c'}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = replaceChars('hello, world!', 'o', 'O')
        assert result == 'hellO, wOrld!', f"Test 3 failed: got {result}, expected {'hellO, wOrld!'}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = replaceChars('', 'x', 'y')
        assert result == '', f"Test 4 failed: got {result}, expected {''}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = replaceChars('test', 'x', 'y')
        assert result == 'test', f"Test 5 failed: got {result}, expected {'test'}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = replaceChars('unchanged', 'u', 'u')
        assert result == 'unchanged', f"Test 6 failed: got {result}, expected {'unchanged'}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = replaceChars('aaa', 'a', 'b')
        assert result == 'bbb', f"Test 7 failed: got {result}, expected {'bbb'}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = replaceChars('a', 'a', 'b')
        assert result == 'b', f"Test 8 failed: got {result}, expected {'b'}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = replaceChars('a b  c   d', ' ', '_')
        assert result == '_ b  c   d', f"Test 9 failed: got {result}, expected {'_ b  c   d'}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = replaceChars('123-456-7890', '-', ':')
        assert result == '123:456:7890', f"Test 10 failed: got {result}, expected {'123:456:7890'}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = replaceChars('AbrAcadAbrA', 'A', 'a')
        assert result == 'abracadabra', f"Test 11 failed: got {result}, expected {'abracadabra'}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = replaceChars('ha😂ha😂!', '😂', '🤣')
        assert result == 'ha🤣ha🤣!', f"Test 12 failed: got {result}, expected {'ha🤣ha🤣!'}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = replaceChars('𝄞music𝄞', '𝄞', '♪')
        assert result == '♪music♪', f"Test 13 failed: got {result}, expected {'♪music♪'}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = replaceChars('élan', '́', '~')
        assert result == 'e~lan', f"Test 14 failed: got {result}, expected {'e~lan'}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = replaceChars('path\\to\\file', '\\', '/')
        assert result == 'path/to/file', f"Test 15 failed: got {result}, expected {'path/to/file'}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = replaceChars('abababab', 'a', 'b')
        assert result == 'bbbbbbbb', f"Test 16 failed: got {result}, expected {'bbbbbbbb'}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = replaceChars('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'x', 'y')
        assert result == 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy', f"Test 17 failed: got {result}, expected {'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = replaceChars('zero\u200bwidth\u200bspace', '\u200b', '-')
        assert result == 'zero-width-space', f"Test 18 failed: got {result}, expected {'zero-width-space'}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = replaceChars('🔥🔥🔥', '🔥', '❄')
        assert result == '❄❄❄', f"Test 19 failed: got {result}, expected {'❄❄❄'}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = replaceChars('\x01\x02\x03abc\x03\x02\x01', '\x03', '*')
        assert result == '\\x01\\x02*abc*\\x02\\x01', f"Test 20 failed: got {result}, expected {'\\x01\\x02*abc*\\x02\\x01'}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = replaceChars('مرحبا بالعالم', 'ا', 'أ')
        assert result == 'مرحبأ بألعألم', f"Test 21 failed: got {result}, expected {'مرحبأ بألعألم'}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = replaceChars('hello, world!_x', ',', ';')
        assert result == 'hello; world!_x', f"Test 22 failed: got {result}, expected {'hello; world!_x'}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = replaceChars('hello, world!', 'e', '')
        assert result == 'hallo, world!', f"Test 23 failed: got {result}, expected {'hallo, world!'}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = replaceChars('hello, world!', ',', 'x_x_ナカタカ')
        assert result == 'hellox world!', f"Test 24 failed: got {result}, expected {'hellox world!'}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = replaceChars('c.b,a', ',', ':')
        assert result == 'c.b:a', f"Test 25 failed: got {result}, expected {'c.b:a'}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = replaceChars('c.b,a', ',', '')
        assert result == 'c.baa', f"Test 26 failed: got {result}, expected {'c.baa'}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = replaceChars('a,b.c_x', ',', ':')
        assert result == 'a:b.c_x', f"Test 27 failed: got {result}, expected {'a:b.c_x'}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = replaceChars('hello, world! 1', 'hello, 0', 'O_x')
        assert result == 'Oello, world! 1', f"Test 28 failed: got {result}, expected {'Oello, world! 1'}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = replaceChars('hello, world! edge', 'o_x', 'O 1')
        assert result == 'hellO, wOrld! edge', f"Test 29 failed: got {result}, expected {'hellO, wOrld! edge'}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = replaceChars('_', '_x', 'O_x')
        assert result == 'O', f"Test 30 failed: got {result}, expected {'O'}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = replaceChars('a edge_x', 'x', 'y edge')
        assert result == 'a edge_y', f"Test 31 failed: got {result}, expected {'a edge_y'}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = replaceChars('degnahcnu 0', 'u', '')
        assert result == 'degnahcna 0', f"Test 32 failed: got {result}, expected {'degnahcna 0'}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = replaceChars('degnahcnu', 'a,b.c', 'u')
        assert result == 'degnuhcnu', f"Test 33 failed: got {result}, expected {'degnuhcnu'}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = replaceChars('a', 'a_x', 'row2_x')
        assert result == 'r', f"Test 34 failed: got {result}, expected {'r'}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = replaceChars('a/b/c/d', 'a', 'b')
        assert result == 'b/b/c/d', f"Test 35 failed: got {result}, expected {'b/b/c/d'}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = replaceChars('a', 'a', 'O 1')
        assert result == 'O', f"Test 36 failed: got {result}, expected {'O'}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = replaceChars('aaaaaa', '', 'z')
        assert result == 'zzzzzz', f"Test 37 failed: got {result}, expected {'zzzzzz'}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = replaceChars('aaaaaa 0', 'a', 'z')
        assert result == 'zzzzzz 0', f"Test 38 failed: got {result}, expected {'zzzzzz 0'}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = replaceChars('replace nothing changes 1', '', 'e')
        assert result == 'replece nothing chenges 1', f"Test 39 failed: got {result}, expected {'replece nothing chenges 1'}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = replaceChars('élan 0', 'e', 'x_e')
        assert result == 'x́lan 0', f"Test 40 failed: got {result}, expected {'x́lan 0'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = replaceChars('replace nothing changes 0_x', '', 'e')
        assert result == 'replece nothing chenges 0_x', f"Test 41 failed: got {result}, expected {'replece nothing chenges 0_x'}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = replaceChars('replace nothing changes', '', 'row1')
        assert result == 'replrce nothing chrnges', f"Test 42 failed: got {result}, expected {'replrce nothing chrnges'}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = replaceChars('replace nothing changes', 'e', '|')
        assert result == 'r|plac| nothing chang|s', f"Test 43 failed: got {result}, expected {'r|plac| nothing chang|s'}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = replaceChars('replace nothing changes_x', 'e edge', 'x_e')
        assert result == 'rxplacx nothing changxs_x', f"Test 44 failed: got {result}, expected {'rxplacx nothing changxs_x'}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = replaceChars('replace nothing changes', 'e', 'x_e_x')
        assert result == 'rxplacx nothing changxs', f"Test 45 failed: got {result}, expected {'rxplacx nothing changxs'}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = replaceChars('replace nothing changes', 'e_x', 'aaa')
        assert result == 'raplaca nothing changas', f"Test 46 failed: got {result}, expected {'raplaca nothing changas'}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = replaceChars('a b  c   d_x', '', '_')
        assert result == '_ b  c   d_x', f"Test 47 failed: got {result}, expected {'_ b  c   d_x'}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = replaceChars('d   c  b a edge', '', '__x')
        assert result == 'd   c  b _ edge', f"Test 48 failed: got {result}, expected {'d   c  b _ edge'}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = replaceChars('path\\to\\file', ' ', '_')
        assert result == 'p_th\\to\\file', f"Test 49 failed: got {result}, expected {'p_th\\to\\file'}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = replaceChars('a b  c   d', ' ', 'unchanged')
        assert result == 'u b  c   d', f"Test 50 failed: got {result}, expected {'u b  c   d'}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = replaceChars('a b  c   d', '', '_')
        assert result == '_ b  c   d', f"Test 51 failed: got {result}, expected {'_ b  c   d'}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = replaceChars('AbrAcadAbrA 0', 'A 1', 'a')
        assert result == 'abracadabra 0', f"Test 52 failed: got {result}, expected {'abracadabra 0'}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = replaceChars('replace nothing changes', '', 'x_a')
        assert result == 'replxce nothing chxnges', f"Test 53 failed: got {result}, expected {'replxce nothing chxnges'}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = replaceChars('ArbAdacArbA', 'A', 'a')
        assert result == 'arbadacarba', f"Test 54 failed: got {result}, expected {'arbadacarba'}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
