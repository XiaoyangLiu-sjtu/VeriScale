# Coverage Report

Total executable lines: 26
Covered lines: 26
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def shortestBeautifulSubstring(s, k):
2: ✓     n = len(s)
3: ✓     p = [0] * (n + 1)
4: ✓     for i in range(n):
5: ✓         p[i+1] = p[i] + (1 if s[i] == '1' else 0)
6: ✓     indices = {}
7: ✓     for i, val in enumerate(p):
8: ✓         if val not in indices:
9: ✓             indices[val] = []
10: ✓         indices[val].append(i)
11: ✓     from bisect import bisect_right
12: ✓     best = None
13: ✓     best_len = float('inf')
14: ✓     for i in range(n):
15: ✓         req = p[i] + k
16: ✓         if req in indices:
17: ✓             lst = indices[req]
18: ✓             pos = bisect_right(lst, i)
19: ✓             if pos < len(lst):
20: ✓                 j = lst[pos]
21: ✓                 candidate = s[i:j]
22: ✓                 cand_len = j - i
23: ✓                 if cand_len < best_len or (cand_len == best_len and candidate < best):
24: ✓                     best = candidate
25: ✓                     best_len = cand_len
26: ✓     return best if best is not None else ""
```

## Complete Test File

```python
def shortestBeautifulSubstring(s, k):
    n = len(s)
    p = [0] * (n + 1)
    for i in range(n):
        p[i+1] = p[i] + (1 if s[i] == '1' else 0)
    indices = {}
    for i, val in enumerate(p):
        if val not in indices:
            indices[val] = []
        indices[val].append(i)
    from bisect import bisect_right
    best = None
    best_len = float('inf')
    for i in range(n):
        req = p[i] + k
        if req in indices:
            lst = indices[req]
            pos = bisect_right(lst, i)
            if pos < len(lst):
                j = lst[pos]
                candidate = s[i:j]
                cand_len = j - i
                if cand_len < best_len or (cand_len == best_len and candidate < best):
                    best = candidate
                    best_len = cand_len
    return best if best is not None else ""

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = shortestBeautifulSubstring('100011001', 3)
        assert result == '11001', f"Test 1 failed: got {result}, expected {'11001'}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = shortestBeautifulSubstring('1011', 2)
        assert result == '11', f"Test 2 failed: got {result}, expected {'11'}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = shortestBeautifulSubstring('000', 1)
        assert result == '', f"Test 3 failed: got {result}, expected {''}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = shortestBeautifulSubstring('11111', 3)
        assert result == '111', f"Test 4 failed: got {result}, expected {'111'}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = shortestBeautifulSubstring('10100101', 2)
        assert result == '101', f"Test 5 failed: got {result}, expected {'101'}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = shortestBeautifulSubstring('1001001', 2)
        assert result == '1001', f"Test 6 failed: got {result}, expected {'1001'}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = shortestBeautifulSubstring('10010001', 1)
        assert result == '1', f"Test 7 failed: got {result}, expected {'1'}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = shortestBeautifulSubstring('1001', 0)
        assert result == '0', f"Test 8 failed: got {result}, expected {'0'}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = shortestBeautifulSubstring('11011', 3)
        assert result == '1011', f"Test 9 failed: got {result}, expected {'1011'}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = shortestBeautifulSubstring('0', 1)
        assert result == '', f"Test 10 failed: got {result}, expected {''}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = shortestBeautifulSubstring('1', 2)
        assert result == '', f"Test 11 failed: got {result}, expected {''}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = shortestBeautifulSubstring('0000', 0)
        assert result == '0', f"Test 12 failed: got {result}, expected {'0'}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = shortestBeautifulSubstring('0000', 1)
        assert result == '', f"Test 13 failed: got {result}, expected {''}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = shortestBeautifulSubstring('1111', 2)
        assert result == '11', f"Test 14 failed: got {result}, expected {'11'}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = shortestBeautifulSubstring('1111', 5)
        assert result == '', f"Test 15 failed: got {result}, expected {''}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = shortestBeautifulSubstring('1010', 1)
        assert result == '1', f"Test 16 failed: got {result}, expected {'1'}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = shortestBeautifulSubstring('1010', 2)
        assert result == '101', f"Test 17 failed: got {result}, expected {'101'}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = shortestBeautifulSubstring('1010', 3)
        assert result == '', f"Test 18 failed: got {result}, expected {''}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = shortestBeautifulSubstring('01010', 1)
        assert result == '1', f"Test 19 failed: got {result}, expected {'1'}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = shortestBeautifulSubstring('01010', 2)
        assert result == '101', f"Test 20 failed: got {result}, expected {'101'}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = shortestBeautifulSubstring('01010', 0)
        assert result == '0', f"Test 21 failed: got {result}, expected {'0'}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = shortestBeautifulSubstring('10001', 1)
        assert result == '1', f"Test 22 failed: got {result}, expected {'1'}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = shortestBeautifulSubstring('10001', 2)
        assert result == '10001', f"Test 23 failed: got {result}, expected {'10001'}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = shortestBeautifulSubstring('0011100', 2)
        assert result == '11', f"Test 24 failed: got {result}, expected {'11'}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = shortestBeautifulSubstring('0011100', 3)
        assert result == '111', f"Test 25 failed: got {result}, expected {'111'}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = shortestBeautifulSubstring('0011100', 4)
        assert result == '', f"Test 26 failed: got {result}, expected {''}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = shortestBeautifulSubstring('1100101001110', 4)
        assert result == '100111', f"Test 27 failed: got {result}, expected {'100111'}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = shortestBeautifulSubstring('101010101010', 6)
        assert result == '10101010101', f"Test 28 failed: got {result}, expected {'10101010101'}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = shortestBeautifulSubstring('101010101010', 7)
        assert result == '', f"Test 29 failed: got {result}, expected {''}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = shortestBeautifulSubstring('0001000', 1)
        assert result == '1', f"Test 30 failed: got {result}, expected {'1'}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = shortestBeautifulSubstring('10', 0)
        assert result == '0', f"Test 31 failed: got {result}, expected {'0'}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = shortestBeautifulSubstring('101010101010', 3)
        assert result == '10101', f"Test 32 failed: got {result}, expected {'10101'}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = shortestBeautifulSubstring('1101', 2)
        assert result == '11', f"Test 33 failed: got {result}, expected {'11'}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = shortestBeautifulSubstring('1101', 0)
        assert result == '0', f"Test 34 failed: got {result}, expected {'0'}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = shortestBeautifulSubstring('11111', 4)
        assert result == '1111', f"Test 35 failed: got {result}, expected {'1111'}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = shortestBeautifulSubstring('10100101', 0)
        assert result == '0', f"Test 36 failed: got {result}, expected {'0'}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = shortestBeautifulSubstring('1001001', 0)
        assert result == '0', f"Test 37 failed: got {result}, expected {'0'}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = shortestBeautifulSubstring('10010001', 0)
        assert result == '0', f"Test 38 failed: got {result}, expected {'0'}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = shortestBeautifulSubstring('10010001', 2)
        assert result == '1001', f"Test 39 failed: got {result}, expected {'1001'}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = shortestBeautifulSubstring('11011', 0)
        assert result == '0', f"Test 40 failed: got {result}, expected {'0'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = shortestBeautifulSubstring('11011', 2)
        assert result == '11', f"Test 41 failed: got {result}, expected {'11'}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = shortestBeautifulSubstring('100011001', 0)
        assert result == '0', f"Test 42 failed: got {result}, expected {'0'}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = shortestBeautifulSubstring('0101', 2)
        assert result == '101', f"Test 43 failed: got {result}, expected {'101'}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = shortestBeautifulSubstring('1010', 0)
        assert result == '0', f"Test 44 failed: got {result}, expected {'0'}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = shortestBeautifulSubstring('10001', 0)
        assert result == '0', f"Test 45 failed: got {result}, expected {'0'}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = shortestBeautifulSubstring('0111001010011', 2)
        assert result == '11', f"Test 46 failed: got {result}, expected {'11'}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = shortestBeautifulSubstring('0111001010011', 4)
        assert result == '111001', f"Test 47 failed: got {result}, expected {'111001'}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = shortestBeautifulSubstring('0111001010011', 5)
        assert result == '11100101', f"Test 48 failed: got {result}, expected {'11100101'}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = shortestBeautifulSubstring('010101010101', 6)
        assert result == '10101010101', f"Test 49 failed: got {result}, expected {'10101010101'}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = shortestBeautifulSubstring('101010101010', 4)
        assert result == '1010101', f"Test 50 failed: got {result}, expected {'1010101'}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
