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
        assert result == "#['T','e','s','t']", f"Test 4 failed: got {result}, expected {"#['T','e','s','t']"}"
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
        result = insert("#['a']", 1, "#['b']", 1, 0)
        assert result == "#['b', 'a']", f"Test 6 failed: got {result}, expected {"#['b', 'a']"}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = insert("#['a']", 1, "#['b']", 1, 1)
        assert result == "#['a', 'b']", f"Test 7 failed: got {result}, expected {"#['a', 'b']"}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = insert("#['a','b','c']", 3, "#['X','Y']", 2, 0)
        assert result == "#['X', 'Y', 'a', 'b', 'c']", f"Test 8 failed: got {result}, expected {"#['X', 'Y', 'a', 'b', 'c']"}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = insert("#['a','b','c']", 3, "#['X','Y']", 2, 3)
        assert result == "#['a', 'b', 'c', 'X', 'Y']", f"Test 9 failed: got {result}, expected {"#['a', 'b', 'c', 'X', 'Y']"}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = insert("#['a','b','c']", 3, "#['X','Y']", 2, 1)
        assert result == "#['a', 'X', 'Y', 'b', 'c']", f"Test 10 failed: got {result}, expected {"#['a', 'X', 'Y', 'b', 'c']"}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = insert("#['q','w','e','r']", 2, "#['m','n','o']", 3, 2)
        assert result == "#['q', 'w', 'm', 'n', 'o']", f"Test 11 failed: got {result}, expected {"#['q', 'w', 'm', 'n', 'o']"}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = insert("#['h','e','l','l','o']", 4, "#['1','2','3','4']", 4, 0)
        assert result == "#['1', '2', '3', '4', 'h', 'e', 'l', 'l']", f"Test 12 failed: got {result}, expected {"#['1', '2', '3', '4', 'h', 'e', 'l', 'l']"}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = insert("#['h','e','l','l','o']", 4, "#['1','2','3','4']", 4, 4)
        assert result == "#['h', 'e', 'l', 'l', '1', '2', '3', '4']", f"Test 13 failed: got {result}, expected {"#['h', 'e', 'l', 'l', '1', '2', '3', '4']"}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = insert("#['u','v','w','x','y','z']", 6, "#['!']", 1, 6)
        assert result == "#['u', 'v', 'w', 'x', 'y', 'z', '!']", f"Test 14 failed: got {result}, expected {"#['u', 'v', 'w', 'x', 'y', 'z', '!']"}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = insert("#['u','v','w','x','y','z']", 6, "#['!']", 1, 0)
        assert result == "#['!', 'u', 'v', 'w', 'x', 'y', 'z']", f"Test 15 failed: got {result}, expected {"#['!', 'u', 'v', 'w', 'x', 'y', 'z']"}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = insert("#['p','q','r','s','t','u']", 5, "#['A','B','C']", 2, 5)
        assert result == "#['p', 'q', 'r', 's', 't', 'A', 'B']", f"Test 16 failed: got {result}, expected {"#['p', 'q', 'r', 's', 't', 'A', 'B']"}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = insert("#['p','q','r','s','t','u']", 5, "#['A','B','C']", 2, 3)
        assert result == "#['p', 'q', 'r', 'A', 'B', 's', 't']", f"Test 17 failed: got {result}, expected {"#['p', 'q', 'r', 'A', 'B', 's', 't']"}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['k','l','m','n','o','p','q','r','s','t']", 10, 5)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'f', 'g', 'h', 'i', 'j']", f"Test 18 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'f', 'g', 'h', 'i', 'j']"}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 7, "#['k','l','m','n','o','p','q','r','s','t']", 7, 7)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q']", f"Test 19 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q']"}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = insert("#['L','e','a','n']", 4, "#['4','!']", 1, 2)
        assert result == "#['L', 'e', '4', 'a', 'n']", f"Test 20 failed: got {result}, expected {"#['L', 'e', '4', 'a', 'n']"}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = insert("#['L','e','a','n']", 4, "#['4','!']", 2, 2)
        assert result == "#['L', 'e', '4', '!', 'a', 'n']", f"Test 21 failed: got {result}, expected {"#['L', 'e', '4', '!', 'a', 'n']"}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = insert("#['d','a','t','a']", 3, "#['x','y','z','u','v']", 5, 0)
        assert result == "#['x', 'y', 'z', 'u', 'v', 'd', 'a', 't']", f"Test 22 failed: got {result}, expected {"#['x', 'y', 'z', 'u', 'v', 'd', 'a', 't']"}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = insert("#['d','a','t','a']", 3, "#['x','y','z','u','v']", 4, 3)
        assert result == "#['d', 'a', 't', 'x', 'y', 'z', 'u']", f"Test 23 failed: got {result}, expected {"#['d', 'a', 't', 'x', 'y', 'z', 'u']"}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?']", 2, 6)
        assert result == "#['c', 'o', 'n', 't', 'e', 'x', '?', '?']", f"Test 24 failed: got {result}, expected {"#['c', 'o', 'n', 't', 'e', 'x', '?', '?']"}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?']", 1, 4)
        assert result == "#['c', 'o', 'n', 't', '?', 'e', 'x']", f"Test 25 failed: got {result}, expected {"#['c', 'o', 'n', 't', '?', 'e', 'x']"}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = insert("#['g','h']", 1, "#['Z']", 1, 1)
        assert result == "#['g', 'Z']", f"Test 26 failed: got {result}, expected {"#['g', 'Z']"}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = insert("#['g','h']", 2, "#['a','b','c','d']", 3, 1)
        assert result == "#['g', 'a', 'b', 'c', 'h']", f"Test 27 failed: got {result}, expected {"#['g', 'a', 'b', 'c', 'h']"}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = insert("#['s','a','m','p','l','e','d']", 7, "#['+','-','*']", 3, 7)
        assert result == "#['s', 'a', 'm', 'p', 'l', 'e', 'd', '+', '-', '*']", f"Test 28 failed: got {result}, expected {"#['s', 'a', 'm', 'p', 'l', 'e', 'd', '+', '-', '*']"}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = insert("#['H','e','l','l','o']", 5, "#['W','o','r','l','d']", 5, 4)
        assert result == "#['H', 'e', 'l', 'l', 'W', 'o', 'r', 'l', 'd', 'o']", f"Test 29 failed: got {result}, expected {"#['H', 'e', 'l', 'l', 'W', 'o', 'r', 'l', 'd', 'o']"}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = insert("#['d','a','t','a']", 4, "]'4'[#", 1, 4)
        assert result == "#['d', 'a', 't', 'a', ']']", f"Test 30 failed: got {result}, expected {"#['d', 'a', 't', 'a', ']']"}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = insert("#['L','e','a','n']", 4, "]'4'[#", 1, 3)
        assert result == "#['L', 'e', 'a', ']', 'n']", f"Test 31 failed: got {result}, expected {"#['L', 'e', 'a', ']', 'n']"}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = insert("#['L','e','a','n']", 4, "#['L','e','a','n']_x", 1, 4)
        assert result == "#['L', 'e', 'a', 'n', '#']", f"Test 32 failed: got {result}, expected {"#['L', 'e', 'a', 'n', '#']"}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = insert("#['L','e','a','n']", 3, "#['W','o','r','l','d'] edge", 1, 0)
        assert result == "#['#', 'L', 'e', 'a']", f"Test 33 failed: got {result}, expected {"#['#', 'L', 'e', 'a']"}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = insert("#['1','2','3','4','5','6']", 5, "#['a','b','c']", 3, 4)
        assert result == "#['1', '2', '3', '4', 'a', 'b', 'c', '5']", f"Test 34 failed: got {result}, expected {"#['1', '2', '3', '4', 'a', 'b', 'c', '5']"}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = insert("#['1','2','3','4','5','6']", 6, "#['a','b','c']", 3, 3)
        assert result == "#['1', '2', '3', 'a', 'b', 'c', '4', '5', '6']", f"Test 35 failed: got {result}, expected {"#['1', '2', '3', 'a', 'b', 'c', '4', '5', '6']"}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = insert("]'e','d','c','b','a'[#", 1, "#['b']", 1, 0)
        assert result == "#['b', ']']", f"Test 36 failed: got {result}, expected {"#['b', ']']"}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = insert("#['a'] 0", 1, "#['b']", 1, 1)
        assert result == "#['#', 'b']", f"Test 37 failed: got {result}, expected {"#['#', 'b']"}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = insert("#['p','q','r','s','t','u']", 5, "#['A','B','C']", 2, 4)
        assert result == "#['p', 'q', 'r', 's', 'A', 'B', 't']", f"Test 38 failed: got {result}, expected {"#['p', 'q', 'r', 's', 'A', 'B', 't']"}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['k','l','m','n','o','p','q','r','s','t']", 10, 6)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'f', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'g', 'h', 'i', 'j']", f"Test 39 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'f', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'g', 'h', 'i', 'j']"}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['k','l','m','n','o','p','q','r','s','t']", 2, 5)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'f', 'g', 'h', 'i', 'j']", f"Test 40 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'f', 'g', 'h', 'i', 'j']"}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['k','l','m','n','o','p','q','r','s','t']", 10, 1)
        assert result == "#['a', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']", f"Test 41 failed: got {result}, expected {"#['a', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']"}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 10, "#['a'] 0", 1, 6)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'f', '#', 'g', 'h', 'i', 'j']", f"Test 42 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'f', '#', 'g', 'h', 'i', 'j']"}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 6, "#['k','l','m','n','o','p','q','r','s','t']", 2, 5)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'f']", f"Test 43 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'f']"}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = insert("#['a','b','c','d','e','f','g','h','i','j']", 7, "#['k','l','m','n','o','p','q','r','s','t']", 7, 5)
        assert result == "#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'f', 'g']", f"Test 44 failed: got {result}, expected {"#['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'f', 'g']"}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = insert("#['L','e','a','n']", 4, "#['1','2','3']", 3, 2)
        assert result == "#['L', 'e', '1', '2', '3', 'a', 'n']", f"Test 45 failed: got {result}, expected {"#['L', 'e', '1', '2', '3', 'a', 'n']"}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = insert("#['L','e','a','n']", 4, "egde x_]'o','l','l','e','h'[#", 1, 3)
        assert result == "#['L', 'e', 'a', 'e', 'n']", f"Test 46 failed: got {result}, expected {"#['L', 'e', 'a', 'e', 'n']"}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 4, "#['4','!']", 1, 2)
        assert result == "#['c', 'o', '4', 'n', 't']", f"Test 47 failed: got {result}, expected {"#['c', 'o', '4', 'n', 't']"}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?']", 1, 5)
        assert result == "#['c', 'o', 'n', 't', 'e', '?', 'x']", f"Test 48 failed: got {result}, expected {"#['c', 'o', 'n', 't', 'e', '?', 'x']"}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "]'?','?'[#", 1, 4)
        assert result == "#['c', 'o', 'n', 't', ']', 'e', 'x']", f"Test 49 failed: got {result}, expected {"#['c', 'o', 'n', 't', ']', 'e', 'x']"}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = insert("#['c','o','n','t','e','x','t','s']", 6, "#['?','?'] edge", 1, 4)
        assert result == "#['c', 'o', 'n', 't', '#', 'e', 'x']", f"Test 50 failed: got {result}, expected {"#['c', 'o', 'n', 't', '#', 'e', 'x']"}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = insert("#['w','x','y','z']", 4, "#['1','2']", 2, 3)
        assert result == "#['w', 'x', 'y', '1', '2', 'z']", f"Test 51 failed: got {result}, expected {"#['w', 'x', 'y', '1', '2', 'z']"}"
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
