# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def insert(oline, l, nl, p, atPos):
2: ✓     return oline[:atPos] + nl[:p] + oline[atPos:l]
```

## Complete Test File

```python
def insert(oline, l, nl, p, atPos):
    return oline[:atPos] + nl[:p] + oline[atPos:l]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = insert("#['a','b','c','d','e']", 5, "#['X','Y']", 2, 2)
        assert result == "#['a', 'b', 'X', 'Y', 'c', 'd', 'e']", f"Test 1 failed: got {result}, expected {"#['a', 'b', 'X', 'Y', 'c', 'd', 'e']"}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = insert("#['H','e','l','l','o']", 5, "#['W','o','r','l','d']", 5, 0)
        assert result == "#['W', 'o', 'r', 'l', 'd', 'H', 'e', 'l', 'l', 'o']", f"Test 2 failed: got {result}, expected {"#['W', 'o', 'r', 'l', 'd', 'H', 'e', 'l', 'l', 'o']"}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = insert("#['L','e','a','n']", 4, "#['4']", 1, 4)
        assert result == "#['L', 'e', 'a', 'n', '4']", f"Test 3 failed: got {result}, expected {"#['L', 'e', 'a', 'n', '4']"}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = insert("#['T','e','s','t']", 4, '#[]', 0, 2)
        assert result == "#['T', 'e', 's', 't']", f"Test 4 failed: got {result}, expected {"#['T', 'e', 's', 't']"}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = insert("#['1','2','3','4','5','6']", 5, "#['a','b','c']", 3, 3)
        assert result == "#['1', '2', '3', 'a', 'b', 'c', '4', '5']", f"Test 5 failed: got {result}, expected {"#['1', '2', '3', 'a', 'b', 'c', '4', '5']"}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = insert('#[]', 0, "#['x']", 1, 0)
        assert result == "#['x']", f"Test 6 failed: got {result}, expected {"#['x']"}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = insert("#['a']", 1, '#[]', 0, 0)
        assert result == "#['a']", f"Test 7 failed: got {result}, expected {"#['a']"}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = insert("#['a']", 1, '#[]', 0, 1)
        assert result == "#['a']", f"Test 8 failed: got {result}, expected {"#['a']"}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = insert("#['a']", 1, "#['b']", 1, 0)
        assert result == "#['b', 'a']", f"Test 9 failed: got {result}, expected {"#['b', 'a']"}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = insert("#['a']", 1, "#['b']", 1, 1)
        assert result == "#['a', 'b']", f"Test 10 failed: got {result}, expected {"#['a', 'b']"}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = insert("#['a','b','c']", 3, "#['X','Y']", 2, 0)
        assert result == "#['X', 'Y', 'a', 'b', 'c']", f"Test 11 failed: got {result}, expected {"#['X', 'Y', 'a', 'b', 'c']"}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = insert("#['a','b','c']", 3, "#['X','Y']", 2, 3)
        assert result == "#['a', 'b', 'c', 'X', 'Y']", f"Test 12 failed: got {result}, expected {"#['a', 'b', 'c', 'X', 'Y']"}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = insert("#['a','b','c']", 3, "#['X','Y']", 2, 1)
        assert result == "#['a', 'X', 'Y', 'b', 'c']", f"Test 13 failed: got {result}, expected {"#['a', 'X', 'Y', 'b', 'c']"}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = insert("#['q','w','e','r']", 2, "#['m','n','o']", 3, 2)
        assert result == "#['q', 'w', 'm', 'n', 'o']", f"Test 14 failed: got {result}, expected {"#['q', 'w', 'm', 'n', 'o']"}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = insert("#['h','e','l','l','o']", 4, "#['1','2','3','4']", 0, 2)
        assert result == "#['h', 'e', 'l', 'l']", f"Test 15 failed: got {result}, expected {"#['h', 'e', 'l', 'l']"}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = insert("#['h','e','l','l','o']", 4, "#['1','2','3','4']", 4, 0)
        assert result == "#['1', '2', '3', '4', 'h', 'e', 'l', 'l']", f"Test 16 failed: got {result}, expected {"#['1', '2', '3', '4', 'h', 'e', 'l', 'l']"}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = insert("#['h','e','l','l','o']", 4, "#['1','2','3','4']", 4, 4)
        assert result == "#['h', 'e', 'l', 'l', '1', '2', '3', '4']", f"Test 17 failed: got {result}, expected {"#['h', 'e', 'l', 'l', '1', '2', '3', '4']"}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = insert("#['u','v','w','x','y','z']", 6, "#['!']", 1, 6)
        assert result == "#['u', 'v', 'w', 'x', 'y', 'z', '!']", f"Test 18 failed: got {result}, expected {"#['u', 'v', 'w', 'x', 'y', 'z', '!']"}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = insert("#['u','v','w','x','y','z']", 6, "#['!']", 1, 0)
        assert result == "#['!', 'u', 'v', 'w', 'x', 'y', 'z']", f"Test 19 failed: got {result}, expected {"#['!', 'u', 'v', 'w', 'x', 'y', 'z']"}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = insert("#['p','q','r','s','t','u']", 5, "#['A','B','C']", 2, 5)
        assert result == "#['p', 'q', 'r', 's', 't', 'A', 'B']", f"Test 20 failed: got {result}, expected {"#['p', 'q', 'r', 's', 't', 'A', 'B']"}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = insert("#['p','q','r','s','t','u']", 5, "#['A','B','C']", 2, 3)
        assert result == "#['p', 'q', 'r', 'A', 'B', 's', 't']", f"Test 21 failed: got {result}, expected {"#['p', 'q', 'r', 'A', 'B', 's', 't']"}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['k','l','m','n','o','p','q','r','s','t']", 10, 5)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'f', 'g', 'h', 'i', 'j']", f"Test 22 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'f', 'g', 'h', 'i', 'j']"}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 7, "#['k','l','m','n','o','p','q','r','s','t']", 7, 7)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q']", f"Test 23 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q']"}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = insert("#['r','s','t']", 0, "#['1','2','3']", 3, 0)
        assert result == "#['1', '2', '3']", f"Test 24 failed: got {result}, expected {"#['1', '2', '3']"}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = insert("#['r','s','t']", 2, '#[]', 0, 1)
        assert result == "#['r', 's']", f"Test 25 failed: got {result}, expected {"#['r', 's']"}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = insert("#['L','e','a','n']", 4, "#['4','!']", 1, 2)
        assert result == "#['L', 'e', '4', 'a', 'n']", f"Test 26 failed: got {result}, expected {"#['L', 'e', '4', 'a', 'n']"}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = insert("#['L','e','a','n']", 4, "#['4','!']", 2, 2)
        assert result == "#['L', 'e', '4', '!', 'a', 'n']", f"Test 27 failed: got {result}, expected {"#['L', 'e', '4', '!', 'a', 'n']"}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = insert("#['d','a','t','a']", 3, "#['x','y','z','u','v']", 5, 0)
        assert result == "#['x', 'y', 'z', 'u', 'v', 'd', 'a', 't']", f"Test 28 failed: got {result}, expected {"#['x', 'y', 'z', 'u', 'v', 'd', 'a', 't']"}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = insert("#['d','a','t','a']", 3, "#['x','y','z','u','v']", 4, 3)
        assert result == "#['d', 'a', 't', 'x', 'y', 'z', 'u']", f"Test 29 failed: got {result}, expected {"#['d', 'a', 't', 'x', 'y', 'z', 'u']"}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = insert("#['n','u','m','b','e','r','s','1']", 8, '#[]', 0, 8)
        assert result == "#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']", f"Test 30 failed: got {result}, expected {"#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']"}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = insert("#['n','u','m','b','e','r','s','1']", 8, '#[]', 0, 0)
        assert result == "#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']", f"Test 31 failed: got {result}, expected {"#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']"}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?']", 2, 6)
        assert result == "#['c', 'o', 'n', 't', 'e', 'x', '?', '?']", f"Test 32 failed: got {result}, expected {"#['c', 'o', 'n', 't', 'e', 'x', '?', '?']"}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?']", 1, 4)
        assert result == "#['c', 'o', 'n', 't', '?', 'e', 'x']", f"Test 33 failed: got {result}, expected {"#['c', 'o', 'n', 't', '?', 'e', 'x']"}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = insert("#['g','h']", 1, "#['Z']", 1, 1)
        assert result == "#['g', 'Z']", f"Test 34 failed: got {result}, expected {"#['g', 'Z']"}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = insert("#['g','h']", 2, "#['a','b','c','d']", 3, 1)
        assert result == "#['g', 'a', 'b', 'c', 'h']", f"Test 35 failed: got {result}, expected {"#['g', 'a', 'b', 'c', 'h']"}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = insert("#['s','a','m','p','l','e','d']", 7, "#['+','-','*']", 3, 7)
        assert result == "#['s', 'a', 'm', 'p', 'l', 'e', 'd', '+', '-', '*']", f"Test 36 failed: got {result}, expected {"#['s', 'a', 'm', 'p', 'l', 'e', 'd', '+', '-', '*']"}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = insert("#['a','b','c','d','e']", 5, "#['X','Y']", 0, 2)
        assert result == "#['a', 'b', 'c', 'd', 'e']", f"Test 37 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e']"}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = insert("#['a','b','c','d','e']", 5, "#['X','Y']", 0, 1)
        assert result == "#['a', 'b', 'c', 'd', 'e']", f"Test 38 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e']"}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = insert("#['H','e','l','l','o']", 0, "#['W','o','r','l','d']", 5, 0)
        assert result == "#['W', 'o', 'r', 'l', 'd']", f"Test 39 failed: got {result}, expected {"#['W', 'o', 'r', 'l', 'd']"}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = insert("#['H','e','l','l','o']", 5, "#['W','o','r','l','d']", 5, 4)
        assert result == "#['H', 'e', 'l', 'l', 'W', 'o', 'r', 'l', 'd', 'o']", f"Test 40 failed: got {result}, expected {"#['H', 'e', 'l', 'l', 'W', 'o', 'r', 'l', 'd', 'o']"}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = insert("#['d','a','t','a']", 4, "]'4'[#", 1, 4)
        assert result == "#['d', 'a', 't', 'a', ']']", f"Test 41 failed: got {result}, expected {"#['d', 'a', 't', 'a', ']']"}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = insert("#['L','e','a','n']", 4, "]'4'[#", 1, 3)
        assert result == "#['L', 'e', 'a', ']', 'n']", f"Test 42 failed: got {result}, expected {"#['L', 'e', 'a', ']', 'n']"}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = insert("#['L','e','a','n']", 4, "#['4']_x", 0, 0)
        assert result == "#['L', 'e', 'a', 'n']", f"Test 43 failed: got {result}, expected {"#['L', 'e', 'a', 'n']"}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = insert("#['L','e','a','n']", 4, "#['L','e','a','n']_x", 1, 4)
        assert result == "#['L', 'e', 'a', 'n', '#']", f"Test 44 failed: got {result}, expected {"#['L', 'e', 'a', 'n', '#']"}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = insert("#['L','e','a','n']", 3, "#['W','o','r','l','d'] edge", 1, 0)
        assert result == "#['#', 'L', 'e', 'a']", f"Test 45 failed: got {result}, expected {"#['#', 'L', 'e', 'a']"}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = insert("#['T','e','s','t']", 4, "#['a','b','c','d','e','f','g','h','i','j']", 0, 2)
        assert result == "#['T', 'e', 's', 't']", f"Test 46 failed: got {result}, expected {"#['T', 'e', 's', 't']"}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = insert("#['T','e','s','t']", 4, ' 1', 0, 1)
        assert result == "#['T', 'e', 's', 't']", f"Test 47 failed: got {result}, expected {"#['T', 'e', 's', 't']"}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = insert("#['1','2','3','4','5','6']", 5, "#['a','b','c']", 3, 4)
        assert result == "#['1', '2', '3', '4', 'a', 'b', 'c', '5']", f"Test 48 failed: got {result}, expected {"#['1', '2', '3', '4', 'a', 'b', 'c', '5']"}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = insert("#['1','2','3','4','5','6']", 6, "#['a','b','c']", 3, 3)
        assert result == "#['1', '2', '3', 'a', 'b', 'c', '4', '5', '6']", f"Test 49 failed: got {result}, expected {"#['1', '2', '3', 'a', 'b', 'c', '4', '5', '6']"}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = insert("#['1','2','3','4','5','6']", 5, "#['a','b','c']", 0, 3)
        assert result == "#['1', '2', '3', '4', '5']", f"Test 50 failed: got {result}, expected {"#['1', '2', '3', '4', '5']"}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = insert('', 0, '#[]', 0, 0)
        assert result == '#[]', f"Test 51 failed: got {result}, expected {'#[]'}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = insert("#['X','Y'] 0 edge 0", 0, "#['a','b','c','d','e']", 0, 0)
        assert result == '#[]', f"Test 52 failed: got {result}, expected {'#[]'}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = insert('#[] edge', 0, '', 0, 0)
        assert result == '#[]', f"Test 53 failed: got {result}, expected {'#[]'}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = insert('][#', 0, "#['x'] 1_x", 1, 0)
        assert result == "#['#']", f"Test 54 failed: got {result}, expected {"#['#']"}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = insert("#['W','o','r','l','d'] 1", 0, "#['x']_x", 1, 0)
        assert result == "#['#']", f"Test 55 failed: got {result}, expected {"#['#']"}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = insert('#[]_x', 0, "#['x']", 1, 0)
        assert result == "#['x']", f"Test 56 failed: got {result}, expected {"#['x']"}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = insert("#['a']", 1, "#['4']_x", 0, 0)
        assert result == "#['a']", f"Test 57 failed: got {result}, expected {"#['a']"}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = insert('', 1, '', 0, 1)
        assert result == "#['a']", f"Test 58 failed: got {result}, expected {"#['a']"}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = insert("#['a','b','c','d','e']", 1, '#[]_x', 0, 0)
        assert result == "#['a']", f"Test 59 failed: got {result}, expected {"#['a']"}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = insert("#['a']", 1, '#[]_x', 0, 0)
        assert result == "#['a']", f"Test 60 failed: got {result}, expected {"#['a']"}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = insert("#['a']", 1, '#[] 1 0', 0, 0)
        assert result == "#['a']", f"Test 61 failed: got {result}, expected {"#['a']"}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = insert('', 1, '0_x', 0, 0)
        assert result == "#['a']", f"Test 62 failed: got {result}, expected {"#['a']"}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = insert("#['W','o','r','l','d']", 1, '#[]_x', 0, 0)
        assert result == "#['W']", f"Test 63 failed: got {result}, expected {"#['W']"}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = insert('', 1, '#[]', 0, 0)
        assert result == "#['a']", f"Test 64 failed: got {result}, expected {"#['a']"}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = insert("#['a']_x", 1, "#['p','q','r','s','t','u']", 0, 1)
        assert result == "#['#']", f"Test 65 failed: got {result}, expected {"#['#']"}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = insert('', 1, '#[] edge', 0, 1)
        assert result == "#['a']", f"Test 66 failed: got {result}, expected {"#['a']"}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = insert("#['a','b','c'] edge", 1, '#[]', 0, 0)
        assert result == "#['#']", f"Test 67 failed: got {result}, expected {"#['#']"}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = insert("#['a'] edge", 1, '#[] 1', 0, 1)
        assert result == "#['#']", f"Test 68 failed: got {result}, expected {"#['#']"}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = insert("#['a']", 1, "#['a','b','c','d']", 0, 1)
        assert result == "#['a']", f"Test 69 failed: got {result}, expected {"#['a']"}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = insert("]'e','d','c','b','a'[#", 1, "#['b']", 1, 0)
        assert result == "#['b', ']']", f"Test 70 failed: got {result}, expected {"#['b', ']']"}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = insert("]'a'[#", 0, "#['b'] edge 1", 0, 0)
        assert result == '#[]', f"Test 71 failed: got {result}, expected {'#[]'}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = insert("]'a'[#", 1, '', 0, 0)
        assert result == "#[']']", f"Test 72 failed: got {result}, expected {"#[']']"}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = insert("#['a']", 0, "]'e','d','c','b','a'[#", 1, 0)
        assert result == "#[']']", f"Test 73 failed: got {result}, expected {"#[']']"}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = insert("#['a'] 0", 1, "#['b']", 1, 1)
        assert result == "#['#', 'b']", f"Test 74 failed: got {result}, expected {"#['#', 'b']"}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = insert("#['a']_x", 1, "#['b']", 0, 1)
        assert result == "#['#']", f"Test 75 failed: got {result}, expected {"#['#']"}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = insert("#['a']_x", 1, '', 0, 1)
        assert result == "#['#']", f"Test 76 failed: got {result}, expected {"#['#']"}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = insert("#['a','b','c']", 2, "#['X','Y']", 0, 0)
        assert result == "#['a', 'b']", f"Test 77 failed: got {result}, expected {"#['a', 'b']"}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = insert("#['a','b','c']", 0, "#['X','Y']", 2, 0)
        assert result == "#['X', 'Y']", f"Test 78 failed: got {result}, expected {"#['X', 'Y']"}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = insert("#['a','b','c']", 3, "#['X','Y']", 0, 0)
        assert result == "#['a', 'b', 'c']", f"Test 79 failed: got {result}, expected {"#['a', 'b', 'c']"}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = insert("#['a','b','c']", 3, '', 0, 0)
        assert result == "#['a', 'b', 'c']", f"Test 80 failed: got {result}, expected {"#['a', 'b', 'c']"}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = insert("#['a','b','c']", 3, "]'Y','X'[#", 0, 3)
        assert result == "#['a', 'b', 'c']", f"Test 81 failed: got {result}, expected {"#['a', 'b', 'c']"}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = insert("#['a','b','c']", 3, "#['X','Y']_x", 1, 0)
        assert result == "#['#', 'a', 'b', 'c']", f"Test 82 failed: got {result}, expected {"#['#', 'a', 'b', 'c']"}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = insert("#['q','w','e','r']", 2, "#['m','n','o']", 1, 0)
        assert result == "#['m', 'q', 'w']", f"Test 83 failed: got {result}, expected {"#['m', 'q', 'w']"}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = insert("#['h','e','l','l','o']", 4, "#['4']", 0, 2)
        assert result == "#['h', 'e', 'l', 'l']", f"Test 84 failed: got {result}, expected {"#['h', 'e', 'l', 'l']"}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = insert("#['h','e','l','l','o']", 0, "#['1','2','3','4']", 4, 0)
        assert result == "#['1', '2', '3', '4']", f"Test 85 failed: got {result}, expected {"#['1', '2', '3', '4']"}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = insert("#['u','v','w','x','y','z']", 4, "egde ]'4','3','2','1'[#", 0, 4)
        assert result == "#['u', 'v', 'w', 'x']", f"Test 86 failed: got {result}, expected {"#['u', 'v', 'w', 'x']"}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = insert("#['u','v','w','x','y','z']", 6, "#['!'] 0", 0, 0)
        assert result == "#['u', 'v', 'w', 'x', 'y', 'z']", f"Test 87 failed: got {result}, expected {"#['u', 'v', 'w', 'x', 'y', 'z']"}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = insert("#['u','v','w','x','y','z']", 6, "#['1','2']", 0, 0)
        assert result == "#['u', 'v', 'w', 'x', 'y', 'z']", f"Test 88 failed: got {result}, expected {"#['u', 'v', 'w', 'x', 'y', 'z']"}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = insert("#['u','v','w','x','y','z']", 3, "#['!'] 0", 1, 0)
        assert result == "#['#', 'u', 'v', 'w']", f"Test 89 failed: got {result}, expected {"#['#', 'u', 'v', 'w']"}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = insert("#['p','q','r','s','t','u']", 5, "#['A','B','C']", 2, 4)
        assert result == "#['p', 'q', 'r', 's', 'A', 'B', 't']", f"Test 90 failed: got {result}, expected {"#['p', 'q', 'r', 's', 'A', 'B', 't']"}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['k','l','m','n','o','p','q','r','s','t']", 10, 6)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'f', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'g', 'h', 'i', 'j']", f"Test 91 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'f', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'g', 'h', 'i', 'j']"}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['k','l','m','n','o','p','q','r','s','t']", 2, 5)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'f', 'g', 'h', 'i', 'j']", f"Test 92 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'f', 'g', 'h', 'i', 'j']"}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['k','l','m','n','o','p','q','r','s','t']", 10, 1)
        assert result == "#['a', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']", f"Test 93 failed: got {result}, expected {"#['a', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']"}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['a'] 0", 1, 6)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'f', '#', 'g', 'h', 'i', 'j']", f"Test 94 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'f', '#', 'g', 'h', 'i', 'j']"}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 7, "#['k','l','m','n','o','p','q','r','s','t']", 4, 0)
        assert result == "#['k', 'l', 'm', 'n', 'a', 'b', 'c', 'd', 'e', 'f', 'g']", f"Test 95 failed: got {result}, expected {"#['k', 'l', 'm', 'n', 'a', 'b', 'c', 'd', 'e', 'f', 'g']"}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 6, "#['k','l','m','n','o','p','q','r','s','t']", 2, 5)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'f']", f"Test 96 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'f']"}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 7, "#['k','l','m','n','o','p','q','r','s','t']", 7, 5)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'f', 'g']", f"Test 97 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'f', 'g']"}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = insert("#['r','s','t']", 0, "#['1','2','3'] edge 0", 0, 0)
        assert result == '#[]', f"Test 98 failed: got {result}, expected {'#[]'}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = insert("#['r','s','t']", 2, "]'o','l','l','e','h'[#", 0, 1)
        assert result == "#['r', 's']", f"Test 99 failed: got {result}, expected {"#['r', 's']"}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = insert("#['r','s','t']", 2, '#[]_x', 0, 1)
        assert result == "#['r', 's']", f"Test 100 failed: got {result}, expected {"#['r', 's']"}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = insert("#['r','s','t']", 2, "]'s','t','x','e','t','n','o','c'[#_x", 0, 1)
        assert result == "#['r', 's']", f"Test 101 failed: got {result}, expected {"#['r', 's']"}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = insert("#['r','s','t']", 1, '#[]', 0, 1)
        assert result == "#['r']", f"Test 102 failed: got {result}, expected {"#['r']"}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = insert("#['r','s','t']", 2, '#[] 1', 0, 0)
        assert result == "#['r', 's']", f"Test 103 failed: got {result}, expected {"#['r', 's']"}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = insert("#['L','e','a','n']", 4, "#['1','2','3']", 3, 2)
        assert result == "#['L', 'e', '1', '2', '3', 'a', 'n']", f"Test 104 failed: got {result}, expected {"#['L', 'e', '1', '2', '3', 'a', 'n']"}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = insert("#['L','e','a','n']", 4, "egde x_]'o','l','l','e','h'[#", 1, 3)
        assert result == "#['L', 'e', 'a', 'e', 'n']", f"Test 105 failed: got {result}, expected {"#['L', 'e', 'a', 'e', 'n']"}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 4, "#['4','!']", 1, 2)
        assert result == "#['c', 'o', '4', 'n', 't']", f"Test 106 failed: got {result}, expected {"#['c', 'o', '4', 'n', 't']"}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = insert("#['L','e','a','n']", 4, "#['4','!']_x", 1, 4)
        assert result == "#['L', 'e', 'a', 'n', '#']", f"Test 107 failed: got {result}, expected {"#['L', 'e', 'a', 'n', '#']"}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = insert("#['L','e','a','n']", 4, "#['4','!']", 2, 4)
        assert result == "#['L', 'e', 'a', 'n', '4', '!']", f"Test 108 failed: got {result}, expected {"#['L', 'e', 'a', 'n', '4', '!']"}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = insert("#['d','a','t','a']", 3, "#['x','y','z','u','v']", 0, 0)
        assert result == "#['d', 'a', 't']", f"Test 109 failed: got {result}, expected {"#['d', 'a', 't']"}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = insert("#['d','a','t','a']", 3, "#['x','y','z','u','v']_x", 0, 0)
        assert result == "#['d', 'a', 't']", f"Test 110 failed: got {result}, expected {"#['d', 'a', 't']"}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = insert("]'a','t','a','d'[#", 1, "#['x','y','z','u','v']", 0, 0)
        assert result == "#[']']", f"Test 111 failed: got {result}, expected {"#[']']"}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = insert("#['n','u','m','b','e','r','s','1']", 8, '#[]_x', 0, 8)
        assert result == "#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']", f"Test 112 failed: got {result}, expected {"#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']"}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = insert("#['n','u','m','b','e','r','s','1']", 8, '#[]_x', 0, 0)
        assert result == "#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']", f"Test 113 failed: got {result}, expected {"#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']"}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = insert("#['n','u','m','b','e','r','s','1']", 8, '][#', 0, 0)
        assert result == "#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']", f"Test 114 failed: got {result}, expected {"#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']"}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = insert("#['n','u','m','b','e','r','s','1']", 8, "]'a','t','a','d'[#", 0, 0)
        assert result == "#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']", f"Test 115 failed: got {result}, expected {"#['n', 'u', 'm', 'b', 'e', 'r', 's', '1']"}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = insert("#['n','u','m','b','e','r','s','1']", 0, '#[]', 0, 0)
        assert result == '#[]', f"Test 116 failed: got {result}, expected {'#[]'}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?']", 1, 5)
        assert result == "#['c', 'o', 'n', 't', 'e', '?', 'x']", f"Test 117 failed: got {result}, expected {"#['c', 'o', 'n', 't', 'e', '?', 'x']"}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?']", 1, 0)
        assert result == "#['?', 'c', 'o', 'n', 't', 'e', 'x']", f"Test 118 failed: got {result}, expected {"#['?', 'c', 'o', 'n', 't', 'e', 'x']"}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "]'?','?'[#", 1, 4)
        assert result == "#['c', 'o', 'n', 't', ']', 'e', 'x']", f"Test 119 failed: got {result}, expected {"#['c', 'o', 'n', 't', ']', 'e', 'x']"}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?'] edge", 1, 4)
        assert result == "#['c', 'o', 'n', 't', '#', 'e', 'x']", f"Test 120 failed: got {result}, expected {"#['c', 'o', 'n', 't', '#', 'e', 'x']"}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = insert("#['g','h']", 1, '', 1, 1)
        assert result == "#['g', 'a']", f"Test 121 failed: got {result}, expected {"#['g', 'a']"}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = insert("egde ]'4','3','2','1'[#", 1, "#['Q']", 1, 0)
        assert result == "#['Q', 'e']", f"Test 122 failed: got {result}, expected {"#['Q', 'e']"}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = insert("#['g','h']", 1, "#['Z']", 1, 0)
        assert result == "#['Z', 'g']", f"Test 123 failed: got {result}, expected {"#['Z', 'g']"}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = insert("1 ]'h','g'[#", 1, "#['Z']", 1, 1)
        assert result == "#['1', 'Z']", f"Test 124 failed: got {result}, expected {"#['1', 'Z']"}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = insert("#['g','h']", 0, "]'n','a','e','L'[#", 1, 0)
        assert result == "#[']']", f"Test 125 failed: got {result}, expected {"#[']']"}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = insert("#['g','h']", 1, "1 ]'n','a','e','L'[#", 1, 1)
        assert result == "#['g', '1']", f"Test 126 failed: got {result}, expected {"#['g', '1']"}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = insert('', 1, "#['Z']", 1, 1)
        assert result == "#['a', 'Z']", f"Test 127 failed: got {result}, expected {"#['a', 'Z']"}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = insert("#['g','h']", 2, "x_1 ]'x'[#", 0, 0)
        assert result == "#['g', 'h']", f"Test 128 failed: got {result}, expected {"#['g', 'h']"}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = insert("#['w','x','y','z']", 1, "]'d','e','l','p','m','a','s'[#", 0, 0)
        assert result == "#['w']", f"Test 129 failed: got {result}, expected {"#['w']"}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = insert('#[]_x', 1, '][#', 0, 0)
        assert result == "#['#']", f"Test 130 failed: got {result}, expected {"#['#']"}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = insert('#[]_x_x', 1, "#['h','e','l','l','o'] 1", 0, 0)
        assert result == "#['#']", f"Test 131 failed: got {result}, expected {"#['#']"}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = insert('#[] 1', 1, '#[]', 0, 1)
        assert result == "#['#']", f"Test 132 failed: got {result}, expected {"#['#']"}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = insert("#['m']", 1, "#['+','-','*'] 0", 1, 0)
        assert result == "#['#', 'm']", f"Test 133 failed: got {result}, expected {"#['#', 'm']"}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = insert("#['w','x','y','z']", 2, "#['1','2']", 2, 2)
        assert result == "#['w', 'x', '1', '2']", f"Test 134 failed: got {result}, expected {"#['w', 'x', '1', '2']"}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = insert("#['w','x','y','z']", 4, "#['1','2']", 2, 3)
        assert result == "#['w', 'x', 'y', '1', '2', 'z']", f"Test 135 failed: got {result}, expected {"#['w', 'x', 'y', '1', '2', 'z']"}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
